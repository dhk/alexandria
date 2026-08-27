#!/usr/bin/env python3
"""Fetch a document, checksum it, extract its text, settle its page offset, and
record the provenance -- stage 2 of the retrieval pipeline, mechanised.

    uv run --no-project --with pypdf python acquire-documents.py --selftest
    uv run --no-project --with pypdf python acquire-documents.py --list

    # stage 1 -- fetch and PROPOSE an offset. Writes local files, never the manifest.
    uv run --no-project --with pypdf python acquire-documents.py \
        --url https://example.org/soma.pdf --id soma-context

    # stage 2 -- settle the offset and record it
    uv run --no-project --with pypdf python acquire-documents.py \
        --url https://example.org/soma.pdf --id soma-context --offset 2

Run where the network is open -- lobster, not a session container, whose egress
reaches *.s3.amazonaws.com, raw.githubusercontent.com and api.github.com and
almost nothing else. Not archives.sfplanning.org.

On lobster, refresh with `git fetch && git reset --hard origin/<branch>`, never
`git pull`. The working branch is restarted from main after each squash-merge
and force-pushed, so its history is rewritten regularly; pull correctly refuses
to fast-forward across that.

WHAT IS COMMITTED, AND WHAT IS NOT

Committed: provenance. Source URL, sha256 as fetched, retrieval timestamp in
UTC, page count, the printed-to-PDF page offset, and the extraction method --
enough to re-fetch the document and prove it is the same bytes.

NOT committed: the documents or their extracted text. CONTRIBUTING.md forbids
committing copyrighted source corpora without permission, and these are
municipal planning documents whose terms have not been established. So the
local store carries its own .gitignore, written by this script, which ignores
everything beside the manifest. Belt and braces: the corpus cannot be committed
by an absent-minded `git add -A` even once.

WHY THE OFFSET IS NOT DECIDED BY THIS SCRIPT ALONE

Printed page numbers are not PDF page numbers. On the Page & Turnbull statement
the printed number runs two behind the PDF index, because of unnumbered front
matter. A citation of "p.20" is ambiguous until you say which one, and a reader
checking a quote against the wrong one concludes the quote is wrong.

This script reads footers and headers, tallies the implied offsets, and PROPOSES
one with the evidence printed beside it. It will not write that proposal to the
manifest on its own: stage 2 requires --offset, explicitly. A wrong offset
poisons every citation quote.py later emits, and it does so while looking
entirely correct -- which is the failure mode this whole investigation keeps
meeting. A number a human confirmed is worth more than a number a heuristic
asserted.

The corollary matters too: the plat extraction that returned a man's birth year
as a plat date did so by taking the "nearest four-digit year". A number found
near a thing is not that thing's number. Here, a candidate is rejected unless it
is a plausible page number for a document of this length -- which is why 1864 in
a footer never becomes page 1864.
"""
from __future__ import annotations

import argparse
import collections
import datetime as _dt
import hashlib
import html.parser
import json
import pathlib
import re
import shutil
import subprocess
import sys
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent / "04-normalized" / "sources"

USER_AGENT = "alexandria-corpus/acquire-documents"

# A printed page number is a small integer. Anything larger than the document
# plus this slack is something else that happens to be a number -- a year, a
# street number, a parcel id. This is the guard that keeps 1864 out.
PAGE_NUMBER_SLACK = 25

# How much of a page to look at. Printed numbers live in the footer, sometimes
# the header, never the middle.
FOOTER_LINES = 3
HEADER_LINES = 2
MAX_LINE_CHARS = 120        # a line of body prose is not a page number

# What it takes to propose an offset rather than shrug.
MIN_AGREEING_PAGES = 5
MIN_AGREEMENT_SHARE = 0.50

GITIGNORE = """\
# Written by 02-run-plan/acquire-documents.py. Do not delete.
#
# The documents and their extracted text stay local: CONTRIBUTING.md forbids
# committing copyrighted source corpora without permission, and these are
# municipal planning documents whose terms have not been established. Only the
# manifest -- provenance, not corpus -- is committed.
#
# This ignores everything in this directory except the manifest and itself, so
# a stray `git add -A` cannot commit a corpus even once.
*
!.gitignore
!manifest.json
"""

MANIFEST_NOTE = (
    "Provenance for documents retrieved by hand, NOT the documents themselves. "
    "Each entry carries enough to re-fetch the document and prove it is the same "
    "bytes: url, sha256 as fetched, retrieval time in UTC, page count, the "
    "printed-to-PDF page offset, and how the text was extracted. The documents and "
    "their extractions are deliberately absent -- CONTRIBUTING.md forbids committing "
    "copyrighted source corpora without permission, and these municipal planning "
    "documents have terms that have not been established. Cite as "
    "'printed p.18 (PDF p.20)': page_offset is pdf_page minus printed_page."
)


# --------------------------------------------------------------------------
# fetching


def get(url: str) -> tuple[bytes, str]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=300) as r:
        return r.read(), (r.headers.get("Content-Type") or "").split(";")[0].strip()


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def is_pdf(data: bytes) -> bool:
    return data[:5] == b"%PDF-"


# --------------------------------------------------------------------------
# extraction


class _Stripper(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.chunks: list[str] = []
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self._skip += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style") and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if not self._skip:
            self.chunks.append(data)


def extract(path: pathlib.Path, pdf: bool) -> tuple[list[str], str]:
    """Return (pages, method). One string per page; HTML is a single page.

    pdftotext is preferred when present -- it preserves the page's layout, so a
    footer stays at the foot -- and pypdf is the fallback that needs no system
    package. The method is recorded in the manifest because the two do not
    always agree about whitespace, and a quotation that cannot be found again
    is worth being able to explain.
    """
    if not pdf:
        parser = _Stripper()
        parser.feed(path.read_text(errors="replace"))
        return ["".join(parser.chunks)], "python html.parser (stdlib)"

    exe = shutil.which("pdftotext")
    if exe:
        proc = subprocess.run([exe, "-layout", str(path), "-"],
                              capture_output=True, check=True)
        version = subprocess.run([exe, "-v"], capture_output=True).stderr.decode(
            "utf-8", "replace").strip().splitlines()
        return (proc.stdout.decode("utf-8", "replace").split("\f"),
                version[0] if version else "pdftotext")

    try:
        import pypdf
    except ImportError:
        raise SystemExit(
            "no PDF text extractor available.\n"
            "  install poppler-utils for pdftotext, or re-run with:\n"
            "  uv run --no-project --with pypdf python acquire-documents.py ...")
    reader = pypdf.PdfReader(str(path))
    return ([(p.extract_text() or "") for p in reader.pages],
            f"pypdf {pypdf.__version__}")


# --------------------------------------------------------------------------
# the page offset


ROMAN = re.compile(r"^[ivxlcdm]{1,7}$")
NUMBER = re.compile(r"\d{1,4}")


def _edge_numbers(line: str) -> list[int]:
    """Numbers at either end of a short line -- where a page number sits.

    A number in the middle of a sentence is a quantity, not a page number, so
    only the first and last number token on the line are considered, and only
    when the line is short enough to be a running head or foot rather than
    prose.
    """
    line = line.strip()
    if not line or len(line) > MAX_LINE_CHARS:
        return []
    found = NUMBER.findall(line)
    if not found:
        return []
    edges = {found[0], found[-1]}
    return [int(n) for n in edges]


def page_candidates(text: str) -> list[int]:
    lines = [ln for ln in (text or "").splitlines() if ln.strip()]
    if not lines:
        return []
    looked_at = lines[-FOOTER_LINES:] + lines[:HEADER_LINES]
    out: list[int] = []
    for line in looked_at:
        out.extend(_edge_numbers(line))
    return out


def roman_pages(pages: list[str]) -> list[int]:
    """PDF indices whose footer is a roman numeral -- i.e. front matter.

    Reported because roman front matter is usually the REASON an offset exists,
    and a reader who sees "pages i-ii are roman, offset 2" understands the
    number instead of trusting it.
    """
    out = []
    for i, text in enumerate(pages, start=1):
        lines = [ln.strip() for ln in (text or "").splitlines() if ln.strip()]
        for line in lines[-FOOTER_LINES:]:
            if ROMAN.match(line.lower().strip(".")):
                out.append(i)
                break
    return out


def offset_evidence(pages: list[str]) -> tuple[collections.Counter, list[tuple]]:
    """Tally offset = pdf_index - printed_number over every plausible candidate.

    Returns the tally and a per-page trace for printing, so the human confirming
    the number can see the footers it came from rather than a bare integer.
    """
    n = len(pages)
    tally: collections.Counter = collections.Counter()
    trace: list[tuple] = []
    for i, text in enumerate(pages, start=1):
        best = None
        for cand in page_candidates(text):
            # A printed page number cannot plausibly exceed the document's own
            # length. This is what rejects years, street numbers and parcel ids.
            if not (1 <= cand <= n + PAGE_NUMBER_SLACK):
                continue
            off = i - cand
            if not (-5 <= off <= 200):
                continue
            tally[off] += 1
            if best is None:
                best = (cand, off)
        lines = [ln.strip() for ln in (text or "").splitlines() if ln.strip()]
        trace.append((i, lines[-1][:60] if lines else "", best))
    return tally, trace


def propose(tally: collections.Counter) -> tuple[int | None, int, float]:
    """Return (offset or None, agreeing pages, share of candidate-bearing pages)."""
    if not tally:
        return None, 0, 0.0
    offset, count = tally.most_common(1)[0]
    total = sum(tally.values())
    share = count / total if total else 0.0
    if count < MIN_AGREEING_PAGES or share < MIN_AGREEMENT_SHARE:
        return None, count, share
    return offset, count, share


def report_offset(pages: list[str], doc_id: str) -> int | None:
    tally, trace = offset_evidence(pages)
    romans = roman_pages(pages)
    print(f"\n--- page offset for {doc_id}: the evidence, not a decision")
    print(f"    {len(pages)} PDF pages")
    if romans:
        print(f"    roman-numbered front matter at PDF pages: "
              f"{', '.join(str(p) for p in romans[:12])}"
              f"{' …' if len(romans) > 12 else ''}")
    if not tally:
        print("    no page-number-like footers found at all.")
        print("    Read several footers yourself and pass --offset N.")
        return None

    print("\n    offsets implied by footers (offset = PDF page - printed page):")
    for off, count in tally.most_common(5):
        print(f"      offset {off:>4}   supported by {count:>4} candidate(s)")

    print("\n    sample pages (PDF page | last line | printed -> offset):")
    shown = [t for t in trace if t[2]][:8]
    for i, last, best in shown:
        cand, off = best
        print(f"      {i:>4} | {last:<60} | {cand} -> {off}")

    offset, count, share = propose(tally)
    if offset is None:
        print(f"\n    NO CONFIDENT PROPOSAL "
              f"(best had {count} supporter(s), {share:.0%} agreement; "
              f"needs {MIN_AGREEING_PAGES} and {MIN_AGREEMENT_SHARE:.0%}).")
        print("    Read the footers yourself and pass --offset N.")
        return None

    print(f"\n    PROPOSED offset {offset}  "
          f"({count} agreeing candidates, {share:.0%} of those found)")
    print(f"    Meaning: printed p.N is PDF p.N+{offset}. Spot-check two pages:")
    for i, last, best in shown[:3]:
        print(f"      PDF p.{i} should print '{i - offset}' -- its last line is: {last!r}")
    print("\n    Nothing was written to the manifest. To record it:")
    print(f"      --offset {offset}    (or --offset auto to accept this proposal)")
    return offset


# --------------------------------------------------------------------------
# manifest


def _citation_form(offset: int | None) -> str:
    """How a citation from this document should read.

    0 is a real offset, not a missing one, and a document that numbers its cover
    gives a negative one -- so this branches on `is None`, not on truthiness.
    """
    if offset is None:
        return "no printed pagination; cite the PDF page"
    if offset == 0:
        return "printed page equals PDF page"
    if offset > 0:
        return f"printed p.N is PDF p.N+{offset}"
    return f"printed p.N is PDF p.N-{abs(offset)}"


def load_manifest(path: pathlib.Path) -> dict:
    if not path.exists():
        return {"note": MANIFEST_NOTE,
                "generated_by": "02-run-plan/acquire-documents.py",
                "documents": []}
    data = json.loads(path.read_text())
    data.setdefault("documents", [])
    return data


def save_manifest(path: pathlib.Path, data: dict) -> None:
    """Rewrite the manifest, entries sorted by id.

    Sorted and stably formatted so a second document produces a one-entry diff
    rather than a reshuffle. Unlike geo/sources.json -- which merges on
    (extent, layer) and rewrites its own top-level note, so that two writers
    clobber each other -- this preserves every entry it did not touch.
    """
    data["note"] = MANIFEST_NOTE
    data["generated_by"] = "02-run-plan/acquire-documents.py"
    data["documents"] = sorted(data["documents"], key=lambda d: d.get("id", ""))
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")


def now_utc() -> str:
    return _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# --------------------------------------------------------------------------
# local store


def store_paths(out: pathlib.Path, doc_id: str, pdf: bool) -> tuple[pathlib.Path, ...]:
    docs, texts = out / "documents", out / "text"
    ext = ".pdf" if pdf else ".html"
    return (docs / f"{doc_id}{ext}", texts / f"{doc_id}.txt",
            docs / f"{doc_id}.fetch.json")


def ensure_store(out: pathlib.Path) -> None:
    (out / "documents").mkdir(parents=True, exist_ok=True)
    (out / "text").mkdir(parents=True, exist_ok=True)
    gitignore = out / ".gitignore"
    current = gitignore.read_text() if gitignore.exists() else None
    if current != GITIGNORE:
        gitignore.write_text(GITIGNORE)


# --------------------------------------------------------------------------
# commands


def cmd_list(out: pathlib.Path) -> int:
    manifest = out / "manifest.json"
    data = load_manifest(manifest)
    docs = data["documents"]
    if not docs:
        print(f"no documents recorded in {manifest}")
        return 0
    print(f"{len(docs)} document(s) in {manifest}\n")
    for d in docs:
        off = d.get("page_offset")
        off_s = "n/a" if off is None else f"+{off}" if off >= 0 else str(off)
        print(f"  {d['id']:<28} {str(d.get('pages','?')):>5}pp  offset {off_s:>4}  "
              f"{d.get('marker','?')}  {d['sha256'][:12]}…")
        print(f"      {d['url']}")
    return 0


def cmd_verify(out: pathlib.Path, only: str | None) -> int:
    """Re-fetch and compare. The manifest claims the bytes; this tests it."""
    data = load_manifest(out / "manifest.json")
    docs = [d for d in data["documents"] if not only or d["id"] == only]
    if not docs:
        print("nothing to verify")
        return 0
    bad = 0
    for d in docs:
        print(f"  {d['id']:<28} ", end="", flush=True)
        try:
            payload, _ = get(d["url"])
        except Exception as exc:                              # noqa: BLE001
            print(f"UNREACHABLE  {exc}")
            bad += 1
            continue
        got = sha256(payload)
        if got == d["sha256"]:
            print("OK")
        else:
            print(f"CHANGED\n      recorded {d['sha256']}\n      now      {got}")
            bad += 1
    print(f"\n{len(docs) - bad}/{len(docs)} verified")
    return 1 if bad else 0


def cmd_acquire(args) -> int:
    out = pathlib.Path(args.out).resolve()
    ensure_store(out)
    pdf_path, text_path, info_path = store_paths(out, args.id, True)

    # Reuse a document already fetched, so settling the offset in stage 2 costs
    # nothing. --refetch forces the network.
    cached = None
    for candidate in (pdf_path, pdf_path.with_suffix(".html")):
        if candidate.exists() and info_path.exists() and not args.refetch:
            cached = candidate
            break

    if cached is not None:
        info = json.loads(info_path.read_text())
        payload = cached.read_bytes()
        digest = sha256(payload)
        if digest != info["sha256"]:
            raise SystemExit(f"local copy of {args.id} does not match its recorded "
                             f"sha256; delete {cached} and re-fetch")
        print(f"  using local copy {cached.name} "
              f"(fetched {info['retrieved_utc']}, --refetch to re-download)",
              file=sys.stderr)
        pdf = is_pdf(payload)
        content_type = info.get("content_type", "")
    else:
        if not args.url:
            raise SystemExit(f"no local copy of {args.id}; --url is required")
        print(f"  fetching {args.url}", file=sys.stderr)
        payload, content_type = get(args.url)
        digest = sha256(payload)
        pdf = is_pdf(payload)
        target = pdf_path if pdf else pdf_path.with_suffix(".html")
        target.write_bytes(payload)
        info_path.write_text(json.dumps({
            "url": args.url, "sha256": digest, "bytes": len(payload),
            "content_type": content_type, "retrieved_utc": now_utc(),
        }, indent=2, sort_keys=True) + "\n")
        info = json.loads(info_path.read_text())
        cached = target
        print(f"  {len(payload) / 1_048_576:.2f} MB · {content_type or '?'} · "
              f"sha256 {digest[:16]}…", file=sys.stderr)

    pages, method = extract(cached, pdf)
    text_path.write_text("\f".join(pages))
    chars = sum(len(p) for p in pages)
    print(f"  extracted {len(pages)} page(s), {chars:,} chars, via {method}",
          file=sys.stderr)
    if pdf and chars < 200 * len(pages):
        print("  ! very little text per page -- this may be a scanned PDF with no "
              "text layer. Quoting from it will not work.", file=sys.stderr)

    # --- the offset
    if not pdf:
        settled, basis = None, "not applicable (not paginated)"
    elif args.offset is None:
        report_offset(pages, args.id)
        print("\nNothing was written to the manifest.")
        return 0
    elif args.offset == "auto":
        proposed = report_offset(pages, args.id)
        if proposed is None:
            print("\nNo proposal to accept. Nothing written.", file=sys.stderr)
            return 4
        settled, basis = proposed, "accepted the footer proposal (--offset auto)"
    elif args.offset == "none":
        settled, basis = None, "no printed page numbers (asserted by operator)"
    else:
        try:
            settled = int(args.offset)
        except ValueError:
            raise SystemExit("--offset takes an integer, 'auto', or 'none'")
        tally, _ = offset_evidence(pages)
        agree = tally.get(settled, 0)
        basis = f"confirmed by operator; {agree} footer candidate(s) agree"
        if agree == 0:
            print(f"  ! no footer supports offset {settled}. Recording it anyway "
                  f"because you asked; the manifest says so.", file=sys.stderr)

    entry = {
        "id": args.id,
        "title": args.title or args.id,
        "url": info["url"],
        "sha256": info["sha256"],
        "bytes": info["bytes"],
        "content_type": info.get("content_type") or "",
        "retrieved_utc": info["retrieved_utc"],
        "media": "pdf" if pdf else "html",
        "pages": len(pages) if pdf else None,
        "page_offset": settled,
        "page_offset_basis": basis,
        "citation_form": _citation_form(settled),
        "extraction_method": method,
        "extraction_chars": chars,
        "rights": args.rights,
        "local_document": str(cached.relative_to(out)),
        "local_text": str(text_path.relative_to(out)),
        "local_note": "NOT committed; re-fetch from url and check sha256",
        "marker": "FETCHED",
    }

    manifest_path = out / "manifest.json"
    data = load_manifest(manifest_path)
    existing = next((d for d in data["documents"] if d["id"] == args.id), None)
    if existing:
        if existing["sha256"] != entry["sha256"] and not args.replace:
            print(f"REFUSED: {args.id} is already recorded with a different sha256.\n"
                  f"  recorded {existing['sha256']}\n  now      {entry['sha256']}\n"
                  "The document changed at its URL. That is a finding, not a nuisance:\n"
                  "any quotation already taken from it may no longer be on the page\n"
                  "cited. Re-run with --replace once you have decided that is fine.",
                  file=sys.stderr)
            return 5
        data["documents"] = [d for d in data["documents"] if d["id"] != args.id]
    data["documents"].append(entry)
    save_manifest(manifest_path, data)

    print(f"\nrecorded {args.id}: {entry['pages']} pages, offset {settled}, "
          f"{basis}")
    print(f"wrote {manifest_path}")
    return 0


# --------------------------------------------------------------------------
# selftest


def selftest() -> int:
    """Prove the offset detector on pages whose answer is known.

    Says what it expects before it checks, because that is the discipline this
    investigation runs on: every bug here so far looked right, and was caught
    by a number compared against a prediction rather than by looking.
    """
    failures = 0

    def check(name: str, got, want) -> None:
        nonlocal failures
        ok = got == want
        failures += 0 if ok else 1
        print(f"  [{'ok' if ok else 'FAIL'}] {name}: expected {want!r}, got {got!r}")

    # 40 pages, 4 pages of unnumbered front matter, so printed = pdf - 4.
    pages = ["COVER", "CONTENTS", "i", "ii"]
    pages += [f"Historic Context Statement\n\nbody text on this page\n\n{i - 4}"
              for i in range(5, 41)]
    tally, _ = offset_evidence(pages)
    offset, count, share = propose(tally)
    print("Expect offset 4 recovered from 36 numbered pages:")
    check("offset", offset, 4)
    check("agreeing pages >= 30", count >= 30, True)

    # A footer carrying a year must not become a page number.
    print("\nExpect a 1864 footer to be rejected as a page number:")
    yearly = [f"text\n\nEureka Homestead Association, 1864\n\n{i}" for i in range(1, 31)]
    tally2, _ = offset_evidence(yearly)
    off2, _, _ = propose(tally2)
    check("offset", off2, 0)
    check("1864 never implied an offset", any(o < -1000 for o in tally2), False)

    # Prose must not be mined for page numbers.
    print("\nExpect a long prose line to yield no candidate:")
    check("edge numbers", _edge_numbers("In 1864 the association platted 240 lots "
                                        "between Seventeenth and Twentieth Streets, "
                                        "Noe and Douglass, covering some 40 acres."), [])

    print("\nExpect no proposal when footers disagree:")
    noisy = [f"text\n\n{i * 7 % 30 + 1}" for i in range(1, 31)]
    t3, _ = offset_evidence(noisy)
    o3, _, _ = propose(t3)
    check("offset", o3, None)

    print(f"\n{'PASSED' if not failures else str(failures) + ' FAILURE(S)'}")
    return 1 if failures else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--url", help="document URL")
    ap.add_argument("--id", help="short slug, e.g. corbett-heights-context")
    ap.add_argument("--title", help="human title for the manifest")
    ap.add_argument("--offset", help="integer, 'auto' to accept the proposal, or "
                                     "'none'. Omit to report the evidence and write nothing.")
    ap.add_argument("--rights", default="not established",
                    help="terms under which the document is published (default: not established)")
    ap.add_argument("--replace", action="store_true",
                    help="record even though the sha256 changed at the URL")
    ap.add_argument("--refetch", action="store_true", help="ignore the local copy")
    ap.add_argument("--list", action="store_true", help="list recorded documents")
    ap.add_argument("--verify", action="store_true",
                    help="re-fetch every recorded document and compare sha256")
    ap.add_argument("--selftest", action="store_true",
                    help="prove the offset detector against known pages; no network")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--out", default=str(OUT))
    args = ap.parse_args()

    if args.selftest:
        return selftest()
    out = pathlib.Path(args.out).resolve()
    if args.list:
        return cmd_list(out)
    if args.verify:
        return cmd_verify(out, args.id)
    if args.dry_run:
        print(f"  would fetch {args.url}")
        print(f"  would write the document and text under {out} (not committed)")
        print(f"  would append provenance to {out / 'manifest.json'} (committed)")
        return 0
    if not args.id:
        ap.error("--id is required")
    return cmd_acquire(args)


if __name__ == "__main__":
    raise SystemExit(main())
