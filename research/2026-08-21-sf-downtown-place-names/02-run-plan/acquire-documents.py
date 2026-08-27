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
# A header or footer is a BLOCK, not a line. The Corbett Heights statement
# prints its page number inside a running head at line four -- "Adopted August
# 16, 2017  113  Michael R. Corbett" -- which a two-line window never sees.
FOOTER_LINES = 6
HEADER_LINES = 6
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

# A page number is found by looking for the shapes a page number takes, in order
# of how much they mean, and stopping at the first shape that gives a confident
# answer.
#
# Learned from the Page & Turnbull SoMa statement, which defeated the first
# version of this detector. Its page number is "-10-", printed in the header
# BLOCK at line six -- past any plausible "first two lines" window -- while the
# last lines of every page are dense footnote text. Looking at the edges of a
# page found footnotes; looking for the SHAPE found the number on 115 of 118
# pages, all of them agreeing on offset 2, which is the value the handoff had
# already established by hand.
#
# The lesson generalises: position is a weak signal and shape is a strong one.
DASHED = re.compile(r"^[\-–—]\s*(\d{1,4})\s*[\-–—]$")
STANDALONE = re.compile(r"^[\[\(]?(\d{1,4})[\.\]\)]?$")
LABELLED = re.compile(r"^page\s+(\d{1,4})$", re.I)

# A sectioned document numbers its pages "IV.C-12", not "12". The number still
# implies an offset, but a citation that renders it "p.12" is wrong -- the page
# says IV.C-12 and a reader checking the quote will not find it. So the prefix
# is captured too, and stored, and quote.py is expected to use it.
#
# Found on the Central SoMa EIR's cultural resources chapter, where every page
# is IV.C-N and N happens to equal the PDF index. Offset 0 and a wrong label is
# a more dangerous result than no answer at all.
COMPOUND = re.compile(r"^([A-Z][A-Za-z0-9.]{0,12}?)[\-–—](\d{1,4})$")

TIERS = ("dashed", "compound", "standalone", "edge")
TIER_NOTE = {
    "dashed": "a number fenced by dashes, e.g. -10-",
    "compound": "a sectioned label, e.g. IV.C-12",
    "standalone": "a line that is nothing but a number",
    "edge": "a number at either end of a short header or footer line",
}


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


def candidates(text: str, tier: str) -> list[int]:
    """Numbers on this page that could be its printed page number, by tier.

    The two shape tiers read every line, because the number can sit anywhere in
    a header or footer block. The edge tier keeps the positional heuristic for
    documents that print a bare number inside a running head.
    """
    lines = [ln.strip() for ln in (text or "").splitlines() if ln.strip()]
    if not lines:
        return []
    if tier == "dashed":
        return [int(m.group(1)) for m in map(DASHED.match, lines) if m]
    if tier == "compound":
        return [int(m.group(2)) for m in map(COMPOUND.match, lines) if m]
    if tier == "standalone":
        out = []
        for line in lines:
            m = STANDALONE.match(line) or LABELLED.match(line)
            if m:
                out.append(int(m.group(1)))
        return out
    looked_at = lines[-FOOTER_LINES:] + lines[:HEADER_LINES]
    out: list[int] = []
    for line in looked_at:
        out.extend(_edge_numbers(line))
    return out


def roman_pages(pages: list[str]) -> list[int]:
    """PDF indices whose header or footer is a roman numeral -- i.e. front matter.

    Reported because roman front matter is usually the REASON an offset exists,
    and a reader who sees "pages i-ii are roman, offset 2" understands the
    number instead of trusting it.
    """
    out = []
    for i, text in enumerate(pages, start=1):
        lines = [ln.strip() for ln in (text or "").splitlines() if ln.strip()]
        for line in lines[:HEADER_LINES + 6] + lines[-FOOTER_LINES:]:
            bare = line.lower().strip("-–— .")
            if bare and ROMAN.match(bare):
                out.append(i)
                break
    return out


def label_prefix(pages: list[str]) -> tuple[str | None, int]:
    """The compound page-label prefix shared by most pages, e.g. "IV.C"."""
    seen: collections.Counter = collections.Counter()
    for text in pages:
        for line in [ln.strip() for ln in (text or "").splitlines() if ln.strip()]:
            m = COMPOUND.match(line)
            if m:
                seen[m.group(1)] += 1
    if not seen:
        return None, 0
    prefix, count = seen.most_common(1)[0]
    return (prefix, count) if count >= MIN_AGREEING_PAGES else (None, count)


def offset_evidence(pages: list[str], tier: str) -> tuple[collections.Counter, list[tuple]]:
    """Tally offset = pdf_index - printed_number over every plausible candidate.

    Returns the tally and a per-page trace for printing, so the human confirming
    the number can see what it came from rather than a bare integer.
    """
    n = len(pages)
    tally: collections.Counter = collections.Counter()
    trace: list[tuple] = []
    for i, text in enumerate(pages, start=1):
        best = None
        # A page votes at most ONCE for a given offset. Counting every candidate
        # instead let noise drown a real signal: on the Corbett Heights statement
        # the true offset had 265 supporters against a runner-up of 15, and still
        # scored 24% because footnote numbers were each counted separately.
        # Pages are the electorate; numbers on a page are not.
        seen_here: set[int] = set()
        for cand in candidates(text, tier):
            # A printed page number cannot plausibly exceed the document's own
            # length. This is what rejects years, street numbers and parcel ids:
            # on the SoMa statement it silently threw out 1880, 1873 and 1886,
            # each of which sat alone on a line and would otherwise have implied
            # an offset near -1880.
            if not (1 <= cand <= n + PAGE_NUMBER_SLACK):
                continue
            off = i - cand
            if not (-5 <= off <= 200):
                continue
            if off not in seen_here:
                seen_here.add(off)
                tally[off] += 1
            if best is None:
                best = (cand, off)
        trace.append((i, best))
    return tally, trace


def propose(tally: collections.Counter,
            pages_with_candidates: int = 0) -> tuple[int | None, int, float]:
    """Return (offset or None, agreeing pages, share of candidate-bearing pages)."""
    if not tally:
        return None, 0, 0.0
    offset, count = tally.most_common(1)[0]
    # Denominator is the pages that produced any candidate at all -- so a page
    # that offered nothing does not count against the answer, and a page that
    # offered five numbers does not count five times.
    total = pages_with_candidates if pages_with_candidates else sum(tally.values())
    share = count / total if total else 0.0
    if count < MIN_AGREEING_PAGES or share < MIN_AGREEMENT_SHARE:
        return None, count, share
    return offset, count, share


def best_proposal(pages: list[str]):
    """First tier that yields a confident offset. Returns (tier, offset, count, share)."""
    for tier in TIERS:
        tally, trace = offset_evidence(pages, tier)
        offset, count, share = propose(tally, sum(1 for _, b in trace if b))
        if offset is not None:
            return tier, offset, count, share
    return None, None, 0, 0.0


def agreement(pages: list[str], offset: int) -> tuple[int, str]:
    """How many candidates support an offset, in the STRONGEST tier that has any.

    Tier rank beats raw count. On the Central SoMa EIR the edge tier found 69
    supporters and the compound tier 68, and reporting the edge tier would have
    credited the weaker evidence -- the one that reads a number off the end of a
    line -- for a number the page-label shape had actually established.
    """
    fallback = (0, "none")
    for tier in TIERS:
        tally, _ = offset_evidence(pages, tier)
        count = tally.get(offset, 0)
        if count >= MIN_AGREEING_PAGES:
            return count, tier
        if count > fallback[0]:
            fallback = (count, tier)
    return fallback


def _ranges(nums: list[int]) -> str:
    """Compress [3,4,5,9] to "3-5, 9"."""
    if not nums:
        return ""
    out, start, prev = [], nums[0], nums[0]
    for n in nums[1:]:
        if n == prev + 1:
            prev = n
            continue
        out.append(f"{start}-{prev}" if prev > start else f"{start}")
        start = prev = n
    out.append(f"{start}-{prev}" if prev > start else f"{start}")
    return ", ".join(out)


def offset_exceptions(pages: list[str], offset: int, tier: str) -> tuple[int, int, str]:
    """Pages that offer a page number which the settled offset does not explain.

    One offset per document is a simplification, and back matter is where it
    breaks. North Beach numbers its appendix "-d2-"; the Modern Architecture
    statement restarts its appendix at 1. In both the offset is right for the
    body and wrong past it, and a citation from those pages would be confidently
    wrong. So the disagreeing pages are counted and their ranges recorded, and
    quote.py is expected to warn when a hit falls inside one.
    """
    agree, disagree = 0, []
    for i, text in enumerate(pages, start=1):
        cands = candidates(text, tier)
        if not cands:
            continue
        if (i - offset) in cands:
            agree += 1
        else:
            disagree.append(i)
    return agree, len(disagree), _ranges(disagree)


def report_offset(pages: list[str], doc_id: str) -> int | None:
    romans = roman_pages(pages)
    print(f"\n--- page offset for {doc_id}: the evidence, not a decision")
    print(f"    {len(pages)} PDF pages")
    if romans:
        print(f"    roman-numbered front matter at PDF pages: "
              f"{', '.join(str(p) for p in romans[:12])}"
              f"{' …' if len(romans) > 12 else ''}")

    print("\n    what each way of looking finds (offset = PDF page - printed page):")
    found_any = False
    for tier in TIERS:
        tally, _ = offset_evidence(pages, tier)
        if not tally:
            print(f"      {tier:<11} ({TIER_NOTE[tier]}): nothing")
            continue
        found_any = True
        top = ", ".join(f"offset {o} on {c} page(s)" for o, c in tally.most_common(3))
        _, tr = offset_evidence(pages, tier)
        seen = sum(1 for _, b in tr if b)
        print(f"      {tier:<11} ({TIER_NOTE[tier]}):")
        print(f"        {top}   [{seen} of {len(pages)} pages offered a number]")
    if not found_any:
        print("\n    no page-number-like text found at all. Read several pages "
              "yourself and pass --offset N.")
        return None

    tier, offset, count, share = best_proposal(pages)
    if offset is None:
        print(f"\n    NO CONFIDENT PROPOSAL from any tier "
              f"(needs {MIN_AGREEING_PAGES} agreeing candidates and "
              f"{MIN_AGREEMENT_SHARE:.0%} agreement).")
        print("    Read the page numbers yourself and pass --offset N.")
        return None

    # Show pages whose own candidate supports the proposed offset. Showing the
    # first candidate found instead let a page appear to contradict the very
    # number it was being used to justify.
    shown = [(i, i - offset) for i, text in enumerate(pages, start=1)
             if (i - offset) in candidates(text, tier)][:6]
    print(f"\n    PROPOSED offset {offset}, from the '{tier}' tier "
          f"({count} agreeing pages, {share:.0%} of pages offering a number)")
    pfx, _ = label_prefix(pages)
    lbl = f"{pfx}-N" if pfx and tier == "compound" else "p.N"
    print(f"    Meaning: printed {lbl} is PDF p.N+{offset}." if offset >= 0 else
          f"    Meaning: printed {lbl} is PDF p.N-{abs(offset)}.")
    print("    Spot-check -- these pages, by this offset, should print:")
    prefix, _ = label_prefix(pages)
    for i, printed in shown:
        label = f"{prefix}-{printed}" if prefix and tier == "compound" else str(printed)
        print(f"      PDF p.{i:<4} -> printed {label}")
    if prefix and tier == "compound":
        print(f"    NOTE: pages are labelled '{prefix}-N', not bare numbers. "
              f"Cite them that way.")
    print("\n    Nothing was written to the manifest. To record it:")
    print(f"      --offset {offset}    (or --offset auto to accept this proposal)")
    return offset


# --------------------------------------------------------------------------
# manifest


def _citation_form(offset: int | None, label_format: str) -> str:
    """How a citation from this document should read.

    0 is a real offset, not a missing one, and a document that numbers its cover
    gives a negative one -- so this branches on `is None`, not on truthiness.

    The label matters as much as the offset. A page printed "IV.C-12" cited as
    "p.12" sends a reader to a page that does not exist, and offset arithmetic
    alone will never notice.
    """
    if offset is None:
        return "no printed pagination; cite the PDF page"
    printed = label_format.replace("{n}", "N")
    if offset == 0:
        return f"printed {printed} is PDF p.N"
    if offset > 0:
        return f"printed {printed} is PDF p.N+{offset}"
    return f"printed {printed} is PDF p.N-{abs(offset)}"


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
        tier, _, count, share = best_proposal(pages)
        settled = proposed
        basis = (f"accepted the proposal (--offset auto); '{tier}' tier, "
                 f"{count} agreeing page(s), {share:.0%} agreement")
    elif args.offset == "none":
        # Precisely what is known: the extraction showed no page number. Whether
        # the document prints one that this extractor dropped is a different
        # claim, and not one this script is in a position to make.
        settled, basis = None, ("no page number appears in the extracted text "
                                "(--offset none); cite the PDF page")
    else:
        try:
            settled = int(args.offset)
        except ValueError:
            raise SystemExit("--offset takes an integer, 'auto', or 'none'")
        agree, tier = agreement(pages, settled)
        _, n_bad, bad_ranges = (offset_exceptions(pages, settled, tier)
                                if tier != "none" else (0, 0, ""))
        basis = (f"confirmed by operator; {agree} page(s) agree "
                 f"via the '{tier}' tier" if agree else
                 "asserted by operator; no page number found supports it")
        if agree == 0:
            print(f"  ! nothing on the page supports offset {settled}. Recording it "
                  f"anyway because you asked; the manifest says so.", file=sys.stderr)

    prefix, prefix_count = label_prefix(pages) if pdf else (None, 0)
    if args.label_format:
        label_format, label_basis = args.label_format, "given by operator (--label-format)"
    elif prefix:
        label_format = prefix + "-{n}"
        label_basis = f"read from {prefix_count} page label(s) of the form '{prefix}-N'"
    else:
        label_format, label_basis = "p.{n}", "bare page numbers"

    if settled is not None and pdf:
        best_tier = agreement(pages, settled)[1]
        if best_tier != "none":
            n_ok, n_bad, bad_ranges = offset_exceptions(pages, settled, best_tier)
        else:
            n_ok, n_bad, bad_ranges = 0, 0, ""
    else:
        n_ok, n_bad, bad_ranges = 0, 0, ""

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
        "citation_form": _citation_form(settled, label_format),
        "page_offset_pages_agreeing": n_ok,
        "page_offset_pages_disagreeing": n_bad,
        "page_offset_exception_pages": bad_ranges,
        "page_offset_exception_note": (
            "PDF pages that print a number the offset does not explain -- usually "
            "separately paginated back matter. A citation from these pages needs its "
            "printed number read directly." if bad_ranges else ""),
        "page_label_format": label_format,
        "page_label_basis": label_basis,
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
    print("Expect offset 4 recovered from 36 numbered pages:")
    tier, offset, count, share = best_proposal(pages)
    check("offset", offset, 4)
    check("agreeing pages >= 30", count >= 30, True)

    # The Page & Turnbull shape, which defeated the first detector: the number
    # is "-N-" high in the HEADER block, and every page ends in footnote text.
    # Looking at the edges of the page finds footnotes; looking for the shape
    # finds the number.
    print("\nExpect offset 2 from '-N-' in a header block, past any edge window:")
    pt = []
    for i in range(1, 41):
        pt.append(
            "Historic Context Statement   South of Market Area\n"
            "  San Francisco, California\n\n\n\n"
            "June 30, 2009  Page & Turnbull, Inc.\n"
            f"-{i - 2}-\n"
            "body text discussing the 1880s and the 1906 fire\n"
            "13 San Francisco Planning Department, Preservation Bulletin No. 11,\n"
            "3.")
    tier2, off2, count2, _ = best_proposal(pt)
    check("offset", off2, 2)
    check("tier", tier2, "dashed")
    check("agreeing pages", count2 >= 35, True)

    # A footer carrying a year must not become a page number.
    print("\nExpect a 1864 footer to be rejected as a page number:")
    yearly = [f"text\n\nEureka Homestead Association, 1864\n\n{i}" for i in range(1, 31)]
    _, off3, _, _ = best_proposal(yearly)
    check("offset", off3, 0)
    t3, _ = offset_evidence(yearly, "standalone")
    check("1864 never implied an offset", any(o < -1000 for o in t3), False)

    # A bare year alone on a line -- the real SoMa noise -- must also be rejected.
    print("\nExpect a bare '1886' line to be rejected too:")
    bare_year = [f"text about the fire\n1886\n-{i - 1}-" for i in range(1, 31)]
    _, off4, _, _ = best_proposal(bare_year)
    check("offset", off4, 1)

    # Prose must not be mined for page numbers.
    print("\nExpect a long prose line to yield no candidate:")
    check("edge numbers", _edge_numbers("In 1864 the association platted 240 lots "
                                        "between Seventeenth and Twentieth Streets, "
                                        "Noe and Douglass, covering some 40 acres."), [])

    print("\nExpect no proposal when the numbers disagree:")
    noisy = [f"text\n\n{i * 7 % 30 + 1}" for i in range(1, 31)]
    _, off5, _, _ = best_proposal(noisy)
    check("offset", off5, None)

    print(f"\n{'PASSED' if not failures else str(failures) + ' FAILURE(S)'}")
    return 1 if failures else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--url", help="document URL")
    ap.add_argument("--id", help="short slug, e.g. corbett-heights-context")
    ap.add_argument("--title", help="human title for the manifest")
    ap.add_argument("--offset", help="integer, 'auto' to accept the proposal, or "
                                     "'none'. Omit to report the evidence and write nothing.")
    ap.add_argument("--label-format", help="how a printed page is written, with {n} "
                                          "for the number, e.g. 'IV.C-{n}'. Read from the "
                                          "pages when not given.")
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
