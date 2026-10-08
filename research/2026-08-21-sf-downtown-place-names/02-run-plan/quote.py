#!/usr/bin/env python3
"""Search the local text extractions for a phrase and return each passage with a
citation that is formed, not invented -- stage 3 of the retrieval pipeline.

    uv run --no-project python quote.py --selftest
    uv run --no-project python quote.py --list

    uv run --no-project python quote.py "Outside Lands"
    uv run --no-project python quote.py "Potter and William T. Humphrey" --id sunset-hcs
    uv run --no-project python quote.py "Homestead Association of 18[0-9]{2}" --regex
    uv run --no-project python quote.py "Eureka Homestead" --json

Stdlib only, no network. It reads two things:

  04-normalized/sources/manifest.json   committed provenance for 11 documents
  04-normalized/sources/text/<id>.txt   the extractions, page-separated by \\f

The manifest is committed; the extractions are NOT, and never will be --
CONTRIBUTING.md forbids committing copyrighted source corpora without
permission. So this script works only where acquire-documents.py has already
run. Where an extraction is missing it says so and moves on, rather than
reporting zero hits in a document it never opened. A silent zero is the same
failure as the DataSF "dataset" that returned the right row count and no data.

WHAT THE PHRASE MATCHER CAN AND CANNOT MATCH

pypdf's text is not the page. On PDF p.20 of the Sunset statement it reads:

    ... commissioned George C. Potter and W illiam T. Humphrey
    to plat the former Outside Lands ...
    ... if the squatters don ated 10% of their land ...

"W illiam". "don ated". Also "favo r", "f or decades", "m ost", "far -flung".
A naive `phrase in page` misses every one of them, silently, and a silent miss
in a search tool is worse than an error: it reads as "the document does not say
that".

So a literal phrase is compiled to a pattern that tolerates:

  * a stray space (or several) inside a word          W illiam  <- William
  * line wrapping, and any run of whitespace          Ortega  Street
  * a word hyphenated across a line break             Sun-\\nset  <- Sunset
  * curly vs straight apostrophes and quotes          Francisco’s <- Francisco's
  * en dash, em dash and hyphen as each other         mid -1920s  <- mid-1920s
  * case

It cannot match, and does not pretend to:

  * a space the extraction DROPPED ("GoldenGate" for "Golden Gate"). Whitespace
    you type must be whitespace in the document; only the reverse is forgiven.
  * a phrase straddling a page break. Search is per page, because a citation is
    per page. Two half-sentences on two pages are two hits or none.
  * OCR or ligature substitutions, and anything in a scanned PDF with no text
    layer -- acquire-documents.py warns at extraction time when it sees one.
  * column and table order. pypdf reads in the PDF's own order, which in a
    two-column layout or a table interleaves text that is not adjacent on the
    page. A hit that reads as nonsense is usually this.

And the tolerance cuts both ways, which is worth knowing before you trust a hit
count: the rule that finds "W illiam" for "William" will also find "N o e" for
"Noe". Short phrases are noisy by construction. Every hit is printed with its
context for exactly that reason -- read the passage, not the number.

--regex is the escape hatch, applied to the raw page text with its line breaks
intact, so it is on you to write \\s+ where the page wraps.

WHY THE CITATION IS THE POINT

The offset is the trap this whole pipeline was built around: printed page
numbers are not PDF page numbers, and a citation that gets it wrong looks
entirely correct. acquire-documents.py refuses to guess an offset. This refuses
to use one it does not have.

Three ways a printed page is NOT claimed, each of them a real document here:

  1. page_offset is null -- japantown-hcs-2008. No offset was ever established,
     so there is no printed page to compute. Cite the document and the PDF page.
  2. the hit lands inside page_offset_exception_pages -- corbett-heights-hcs-2017
     records "1-7, 260-261". Those pages print a number the offset does not
     explain: separately paginated front and back matter. One offset per document
     is a simplification, and this is where it breaks.
  3. the local extraction's page count disagrees with the manifest. Then the PDF
     page index itself is unreliable, so nothing downstream of it is safe.

In all three the citation degrades to the document, with the reason attached,
because the standing instruction is: if the citation cannot be perfect down to
the page, at least name the paper it came from -- that is good enough. What is
never good enough is a page number that was made up.
"""
from __future__ import annotations

import argparse
import dataclasses
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
SOURCES = HERE.parent / "04-normalized" / "sources"

CONTEXT_CHARS = 180
MAX_HITS_PER_DOC = 0          # 0 = no limit

# Characters the extraction and a human keyboard spell differently. Folding these
# is not cosmetic: the Sunset statement prints "San Francisco's favo r" with
# U+2019, and a search for "Francisco's" typed on a keyboard finds nothing.
EQUIVALENT = [
    "'‘’ʼ´`",              # apostrophes
    '"“”„«»',         # quotation marks
    "-‐‑‒–—−",   # hyphens and dashes
]

# A gap allowed INSIDE a word. Either any whitespace -- which covers "W illiam",
# "don ated" and a line wrap -- or a hyphen that is immediately followed by a
# line break, which is a word broken across lines and not a real hyphen. The
# hyphen branch is deliberately narrow: "-" followed by a newline, never "-"
# on its own, so that searching "Outside" cannot match a genuine "Out-side".
WORD_GAP = r"(?:[-‐‑]\s*\n\s*|\s*)"

# A gap where the PHRASE has whitespace. At least one whitespace character must
# be there. Forgiving a dropped space would let "SoMa" match "S o M a" and every
# short phrase would drown in false hits.
WORD_SEP = r"\s+"


# --------------------------------------------------------------------------
# the phrase matcher


def _char_class(ch: str) -> str:
    for group in EQUIVALENT:
        if ch in group:
            return "[" + re.escape(group) + "]"
    return re.escape(ch)


def build_pattern(phrase: str, regex: bool = False) -> re.Pattern:
    """Compile a search phrase into a pattern tolerant of extraction damage.

    In --regex mode the phrase is passed through untouched; the raw page text,
    line breaks and all, is what it is matched against.
    """
    if regex:
        return re.compile(phrase, re.IGNORECASE)
    parts: list[str] = []
    for token in phrase.split():
        chars = [_char_class(c) for c in token]
        parts.append(WORD_GAP.join(chars))
    if not parts:
        raise SystemExit("empty phrase")
    return re.compile(WORD_SEP.join(parts), re.IGNORECASE)


def collapse(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


# --------------------------------------------------------------------------
# page ranges


def parse_ranges(spec: str) -> list[tuple[int, int]]:
    """Parse acquire-documents.py's compact ranges: "1-7, 260-261" -> [(1,7),(260,261)].

    Written to be the exact inverse of that script's _ranges(). Anything it
    cannot parse is ignored rather than guessed at -- but see in_ranges(), which
    treats an unparseable non-empty spec as covering everything, because a
    range list this cannot read is a warning that must not become silence.
    """
    out: list[tuple[int, int]] = []
    for chunk in spec.split(","):
        chunk = chunk.strip()
        if not chunk:
            continue
        m = re.fullmatch(r"(\d+)\s*[-–]\s*(\d+)", chunk)
        if m:
            out.append((int(m.group(1)), int(m.group(2))))
            continue
        if chunk.isdigit():
            out.append((int(chunk), int(chunk)))
    return out


def in_ranges(page: int, spec: str) -> bool:
    if not spec.strip():
        return False
    parsed = parse_ranges(spec)
    if not parsed:
        # A non-empty spec that parsed to nothing is a manifest this script does
        # not understand. Fail towards the honest citation, not the confident one.
        return True
    return any(lo <= page <= hi for lo, hi in parsed)


# --------------------------------------------------------------------------
# the citation


@dataclasses.dataclass
class Citation:
    doc_id: str
    title: str
    url: str
    sha256: str
    pdf_page: int
    pdf_pages: int | None
    printed: str | None          # e.g. "p.18" or "IV.C-12"; None means not claimed
    level: str                   # "page" | "document"
    reason: str                  # why the printed page is or is not claimed
    marker: str

    def text(self) -> str:
        where = f"PDF p.{self.pdf_page}"
        if self.pdf_pages:
            where += f" of {self.pdf_pages}"
        if self.level == "page":
            where = f"printed {self.printed} ({where})"
        head = f"{self.title} — {where}."
        if self.level != "page":
            head += f" Printed page not claimed: {self.reason}."
        return (f"{head} {self.url} "
                f"[{self.marker}; sha256 {self.sha256[:12]}…]")

    def as_dict(self) -> dict:
        return {
            "id": self.doc_id,
            "title": self.title,
            "url": self.url,
            "sha256": self.sha256,
            "pdf_page": self.pdf_page,
            "pdf_pages": self.pdf_pages,
            "printed_page": self.printed,
            "citation_level": self.level,
            "citation_reason": self.reason,
            "marker": self.marker,
            "citation": self.text(),
        }


def cite(entry: dict, pdf_page: int, page_count_ok: bool = True) -> Citation:
    """Form a citation for one PDF page of one document.

    Every branch that returns level="document" is a place where a printed page
    COULD have been computed and deliberately was not. That is the whole tool.
    """
    common = dict(
        doc_id=entry["id"],
        title=entry.get("title") or entry["id"],
        url=entry.get("url", ""),
        sha256=entry.get("sha256", ""),
        pdf_page=pdf_page,
        pdf_pages=entry.get("pages"),
        marker=entry.get("marker", "FETCHED"),
    )

    if not page_count_ok:
        return Citation(printed=None, level="document", **common, reason=(
            "the local extraction's page count disagrees with the manifest, so "
            "the PDF page index itself cannot be trusted"))

    offset = entry.get("page_offset")
    # 0 is a real offset and a document that numbers its cover gives a negative
    # one, so this branches on `is None`, not on truthiness -- same reason
    # acquire-documents.py's _citation_form() does.
    if offset is None:
        basis = entry.get("page_offset_basis") or "no basis recorded"
        return Citation(printed=None, level="document", **common, reason=(
            f"this document has no established printed-to-PDF page offset ({basis})"))

    exceptions = entry.get("page_offset_exception_pages") or ""
    if in_ranges(pdf_page, exceptions):
        return Citation(printed=None, level="document", **common, reason=(
            f"PDF p.{pdf_page} is inside {exceptions}, pages that print a number "
            f"the offset does not explain — read the printed number off the page"))

    printed_n = pdf_page - offset
    if printed_n < 1:
        return Citation(printed=None, level="document", **common, reason=(
            f"an offset of {offset} puts this page before printed page 1, i.e. in "
            f"unnumbered front matter"))

    fmt = entry.get("page_label_format") or "p.{n}"
    return Citation(printed=fmt.replace("{n}", str(printed_n)), level="page",
                    **common, reason=(
                        f"page_offset {offset}, {entry.get('page_offset_basis', '')}"))


# --------------------------------------------------------------------------
# the corpus


@dataclasses.dataclass
class Document:
    entry: dict
    pages: list[str] | None       # None when the extraction is not on this machine
    problem: str | None
    page_count_ok: bool = True


def load_manifest(sources: pathlib.Path) -> list[dict]:
    path = sources / "manifest.json"
    if not path.exists():
        raise SystemExit(f"no manifest at {path}\n"
                         "  run 02-run-plan/acquire-documents.py first")
    return json.loads(path.read_text()).get("documents", [])


def load_documents(sources: pathlib.Path, only: str | None = None) -> list[Document]:
    docs: list[Document] = []
    entries = load_manifest(sources)
    if only:
        entries = [e for e in entries if e["id"] == only]
        if not entries:
            raise SystemExit(f"no document with id {only!r} in the manifest; "
                             f"--list shows what there is")
    for entry in entries:
        rel = entry.get("local_text") or f"text/{entry['id']}.txt"
        path = sources / rel
        if not path.exists():
            docs.append(Document(entry, None, f"no local extraction at {path}"))
            continue
        pages = path.read_text(errors="replace").split("\f")
        recorded = entry.get("pages")
        ok = not (isinstance(recorded, int) and recorded != len(pages))
        problem = None if ok else (
            f"extraction has {len(pages)} page(s), manifest records {recorded}")
        docs.append(Document(entry, pages, problem, page_count_ok=ok))
    return docs


# --------------------------------------------------------------------------
# searching


@dataclasses.dataclass
class Hit:
    citation: Citation
    matched: str
    before: str
    after: str

    def window(self, marks: bool = True) -> str:
        m = f"«{self.matched}»" if marks else self.matched
        return f"{self.before}{m}{self.after}"

    def as_dict(self) -> dict:
        d = self.citation.as_dict()
        d["matched"] = self.matched
        d["context"] = self.window(marks=False)
        d["context_marked"] = self.window(marks=True)
        return d


def search_document(doc: Document, pattern: re.Pattern, context: int,
                    limit: int = 0) -> list[Hit]:
    hits: list[Hit] = []
    if doc.pages is None:
        return hits
    for index, text in enumerate(doc.pages, start=1):
        for m in pattern.finditer(text):
            start, end = m.span()
            if start == end:            # a pattern that matches nothing, e.g. `x*`
                continue
            lead = text[max(0, start - context):start]
            trail = text[end:end + context]
            hits.append(Hit(
                citation=cite(doc.entry, index, doc.page_count_ok),
                matched=collapse(m.group(0)),
                before=("…" if start - context > 0 else "") + collapse(lead) + " ",
                after=" " + collapse(trail) + ("…" if end + context < len(text) else ""),
            ))
            if limit and len(hits) >= limit:
                return hits
    return hits


# --------------------------------------------------------------------------
# commands


def cmd_list(sources: pathlib.Path) -> int:
    docs = load_documents(sources)
    print(f"{len(docs)} document(s) in {sources / 'manifest.json'}\n")
    missing = 0
    for doc in docs:
        e = doc.entry
        off = e.get("page_offset")
        off_s = "none" if off is None else (f"+{off}" if off >= 0 else str(off))
        state = "text OK"
        if doc.pages is None:
            state, missing = "NO TEXT", missing + 1
        elif not doc.page_count_ok:
            state = "PAGE COUNT MISMATCH"
        exc = e.get("page_offset_exception_pages") or "-"
        print(f"  {e['id']:<34} {str(e.get('pages', '?')):>4}pp  offset {off_s:>5}  "
              f"label {e.get('page_label_format', '?'):<10} except {exc:<14} {state}")
    if missing:
        print(f"\n  {missing} document(s) have no local extraction. They are not "
              f"committed and never will be;\n  re-fetch with "
              f"02-run-plan/acquire-documents.py on a host with open egress.")
    return 0


def cmd_search(args) -> int:
    sources = pathlib.Path(args.sources).resolve()
    docs = load_documents(sources, args.id)
    pattern = build_pattern(args.phrase, args.regex)

    results: list[tuple[Document, list[Hit]]] = []
    for doc in docs:
        results.append((doc, search_document(doc, pattern, args.context, args.max)))

    unread = [d for d in docs if d.pages is None]
    total = sum(len(h) for _, h in results)
    searched = len(docs) - len(unread)

    if args.json:
        print(json.dumps({
            "phrase": args.phrase,
            "regex": bool(args.regex),
            "documents_searched": searched,
            "documents_unreadable": [
                {"id": d.entry["id"], "problem": d.problem} for d in unread],
            "hits": [h.as_dict() for _, hs in results for h in hs],
            "hit_count": total,
        }, indent=2))
        return 0 if total else 1

    mode = "regex" if args.regex else "phrase"
    print(f"{mode} {args.phrase!r} — {total} hit(s) across {searched} "
          f"of {len(docs)} document(s)")
    for doc in docs:
        if doc.pages is not None and doc.problem:
            print(f"  ! {doc.entry['id']}: {doc.problem} — citations from it "
                  f"degrade to the document", file=sys.stderr)
    for doc in unread:
        print(f"  ! {doc.entry['id']}: {doc.problem} — NOT searched", file=sys.stderr)

    for doc, hits in results:
        if not hits:
            continue
        e = doc.entry
        print(f"\n{e['id']} · {e.get('title', '')}")
        for n, hit in enumerate(hits, start=1):
            c = hit.citation
            where = f"PDF p.{c.pdf_page}"
            where += (f"  ·  printed {c.printed}" if c.level == "page"
                      else "  ·  printed page NOT CLAIMED")
            print(f"  [{n}] {where}")
            print(f"      {hit.window()}")
            if c.level != "page":
                print(f"      why: {c.reason}")
            print(f"      cite: {c.text()}")
    return 0 if total else 1


# --------------------------------------------------------------------------
# selftest


SELFTEST_DOCS = [
    {   # (a) an ordinary document: printed runs two behind the PDF index.
        "id": "test-offset-2", "title": "A Historic Context Statement",
        "url": "https://example.org/a.pdf", "sha256": "a" * 64, "pages": 40,
        "page_offset": 2, "page_offset_basis": "confirmed by operator; 35 page(s) agree",
        "page_label_format": "p.{n}", "page_label_basis": "bare page numbers",
        "page_offset_exception_pages": "", "page_offset_exception_note": "",
        "marker": "FETCHED", "local_text": "text/test-offset-2.txt",
    },
    {   # (b) a sectioned EIR chapter: the label is IV.C-N, not a bare number.
        "id": "test-compound", "title": "Draft EIR, Section IV.C",
        "url": "https://example.org/b.pdf", "sha256": "b" * 64, "pages": 40,
        "page_offset": 0, "page_offset_basis": "confirmed by operator; 38 page(s) agree",
        "page_label_format": "IV.C-{n}", "page_label_basis": "read from 38 page label(s)",
        "page_offset_exception_pages": "", "page_offset_exception_note": "",
        "marker": "FETCHED", "local_text": "text/test-compound.txt",
    },
    {   # (c) the japantown-hcs-2008 shape: no offset was ever established.
        "id": "test-no-offset", "title": "A Better Neighborhood Plan Historic Context",
        "url": "https://example.org/c.pdf", "sha256": "c" * 64, "pages": 40,
        "page_offset": None,
        "page_offset_basis": "no page number appears in the extracted text",
        "page_label_format": "p.{n}", "page_label_basis": "bare page numbers",
        "page_offset_exception_pages": "", "page_offset_exception_note": "",
        "marker": "FETCHED", "local_text": "text/test-no-offset.txt",
    },
    {   # (d) the corbett-heights-hcs-2017 shape: an offset with holes in it.
        "id": "test-exceptions", "title": "A Statement With Back Matter",
        "url": "https://example.org/d.pdf", "sha256": "d" * 64, "pages": 40,
        "page_offset": 7, "page_offset_basis": "confirmed by operator; 30 page(s) agree",
        "page_label_format": "p.{n}", "page_label_basis": "bare page numbers",
        "page_offset_exception_pages": "1-7, 39-40",
        "page_offset_exception_note": "separately paginated back matter",
        "marker": "FETCHED", "local_text": "text/test-exceptions.txt",
    },
]


def _synthetic_pages(n: int, needle_on: list[int], needle: str) -> list[str]:
    pages = []
    for i in range(1, n + 1):
        body = f"page {i} of the synthetic document, ordinary body prose.\n"
        if i in needle_on:
            body += needle + "\n"
        pages.append(body)
    return pages


def selftest() -> int:
    """Prove the citation logic against synthetic entries. No network, and no
    dependence on the local extractions -- which are gitignored, so a selftest
    that needed them would pass only on the machine that fetched them.

    Says what it expects before it checks, because that is the discipline this
    investigation runs on: every bug here so far looked right, and each was
    caught by a number compared against a prediction made beforehand.
    """
    failures = 0

    def check(name: str, got, want) -> None:
        nonlocal failures
        ok = got == want
        failures += 0 if ok else 1
        print(f"  [{'ok' if ok else 'FAIL'}] {name}: expected {want!r}, got {got!r}")

    by_id = {d["id"]: d for d in SELFTEST_DOCS}

    # ---- (a) a normal offset document
    print("Expect PDF p.20 of a document with offset 2 to cite printed p.18:")
    c = cite(by_id["test-offset-2"], 20)
    check("level", c.level, "page")
    check("printed label", c.printed, "p.18")
    check("citation says 'printed p.18 (PDF p.20 of 40)'",
          "printed p.18 (PDF p.20 of 40)" in c.text(), True)
    print("Expect PDF p.1 of that same document to refuse a printed page "
          "(offset 2 puts it in front matter):")
    c = cite(by_id["test-offset-2"], 1)
    check("level", c.level, "document")
    check("printed label", c.printed, None)
    check("citation offers no printed page at all", "printed p." in c.text(), False)
    check("citation still names the document and the PDF page",
          "A Historic Context Statement — PDF p.1 of 40" in c.text(), True)

    # ---- (b) a compound-label document
    print("\nExpect a compound-label document to cite IV.C-12, never p.12 — a "
          "reader sent to 'p.12' finds no such page:")
    c = cite(by_id["test-compound"], 12)
    check("level", c.level, "page")
    check("printed label", c.printed, "IV.C-12")
    check("citation contains 'printed IV.C-12'", "printed IV.C-12" in c.text(), True)
    # The offset here is 0, so the PDF page is also 12 and "PDF p.12" is correct
    # and must stay. What must never appear is "printed p.12" -- the label, not
    # the index. That is the failure acquire-documents.py's COMPOUND regex exists
    # to prevent, and this is the end of the same wire.
    check("citation never says 'printed p.12'", "printed p.12" in c.text(), False)

    # ---- (c) a null-offset document
    print("\nExpect a null-offset document (the japantown-hcs-2008 case) to invent "
          "nothing:")
    c = cite(by_id["test-no-offset"], 12)
    check("level", c.level, "document")
    check("printed label", c.printed, None)
    check("citation names the PDF page", "PDF p.12 of 40" in c.text(), True)
    check("citation says why", "no established printed-to-PDF page offset" in c.text(),
          True)
    check("citation still names the document",
          "A Better Neighborhood Plan Historic Context" in c.text(), True)

    # ---- (d) a hit inside an exception range
    print("\nExpect offset 7 to hold on PDF p.20 and to be refused on PDF p.40, "
          "which is inside '1-7, 39-40':")
    good = cite(by_id["test-exceptions"], 20)
    check("p.20 level", good.level, "page")
    check("p.20 printed label", good.printed, "p.13")
    bad = cite(by_id["test-exceptions"], 40)
    check("p.40 level", bad.level, "document")
    check("p.40 printed label", bad.printed, None)
    check("p.40 would have been p.33 had the offset been trusted",
          "p.33" in bad.text(), False)
    check("p.40 citation names the exception range", "1-7, 39-40" in bad.text(), True)
    edge = cite(by_id["test-exceptions"], 7)
    check("p.7 (the top of the first range) also refused", edge.level, "document")
    check("p.8 (just past it) is claimed", cite(by_id["test-exceptions"], 8).printed,
          "p.1")

    # ---- range parsing, which the above rests on
    print("\nExpect acquire-documents.py's compact ranges to round-trip:")
    check("'1-7, 260-261'", parse_ranges("1-7, 260-261"), [(1, 7), (260, 261)])
    check("'310, 312-328'", parse_ranges("310, 312-328"), [(310, 310), (312, 328)])
    check("'4'", parse_ranges("4"), [(4, 4)])
    check("empty spec covers nothing", in_ranges(5, ""), False)
    print("Expect a range spec this script cannot parse to be treated as covering "
          "everything — an unreadable warning must not become silence:")
    check("unparseable spec", in_ranges(5, "appendix pages"), True)

    # ---- a page-count mismatch poisons the PDF index itself
    print("\nExpect a page-count mismatch to withdraw the printed page entirely:")
    c = cite(by_id["test-offset-2"], 20, page_count_ok=False)
    check("level", c.level, "document")
    check("printed label", c.printed, None)

    # ---- the matcher
    print("\nExpect the matcher to find the extraction damage that a literal "
          "search misses (all four are real strings from sunset-hcs PDF p.20):")
    for phrase, text in [
        ("William T. Humphrey", "commissioned George C. Potter and W illiam T. Humphrey"),
        ("donated", "if the squatters don ated 10% of their land"),
        ("favor", "ruled in San Francisco’s favo r."),
        ("for decades", "existed only on paper f or decades, and some"),
    ]:
        found = build_pattern(phrase).search(text)
        check(f"{phrase!r} in {text[:34]!r}…", found is not None, True)
    print("Expect a line wrap, a hyphenated line break and a curly apostrophe to "
          "be matched too:")
    check("wrapped phrase", build_pattern("Outside Lands").search(
        "the former\nOutside\nLands, which") is not None, True)
    check("hyphenated line break", build_pattern("Sunset").search(
        "the Sun-\nset District") is not None, True)
    check("curly apostrophe", build_pattern("Francisco's").search(
        "San Francisco’s favor") is not None, True)
    check("straight apostrophe finds curly and vice versa",
          build_pattern("Francisco’s").search("San Francisco's favor") is not None,
          True)
    print("Expect a space you TYPED to require a space in the document — the one "
          "damage that is not forgiven, because forgiving it makes every short "
          "phrase match noise:")
    check("'Outside Lands' does not match 'OutsideLands'",
          build_pattern("Outside Lands").search("the OutsideLands were") is not None,
          False)
    print("Expect the within-word tolerance to cut both ways, and to say so: the "
          "same rule that finds 'W illiam' will find a short phrase in letters "
          "that a table only happened to put side by side. Shown, not hidden:")
    check("'Noe' also matches 'N o e' — a known false positive of short phrases",
          build_pattern("Noe").search("N o e") is not None, True)

    # ---- end to end, on synthetic text, with no file on disk
    print("\nExpect an end-to-end search over synthetic pages to hit p.20 and p.40 "
          "of the exception document, and to cite them differently:")
    doc = Document(by_id["test-exceptions"],
                   _synthetic_pages(40, [20, 40], "the Eureka Homestead Association"),
                   None)
    hits = search_document(doc, build_pattern("Eureka Homestead Association"), 60)
    check("hit count", len(hits), 2)
    check("first hit PDF page", hits[0].citation.pdf_page, 20)
    check("first hit printed", hits[0].citation.printed, "p.13")
    check("second hit PDF page", hits[1].citation.pdf_page, 40)
    check("second hit printed", hits[1].citation.printed, None)
    check("matched text", hits[0].matched, "Eureka Homestead Association")
    check("context carries the page's own prose",
          "page 20 of the synthetic document" in hits[0].window(), True)

    print("\nExpect a document with no local extraction to be reported, not "
          "silently counted as zero hits:")
    absent = Document(by_id["test-no-offset"], None, "no local extraction at /nowhere")
    check("hits from an unread document", search_document(
        absent, build_pattern("anything"), 60), [])
    check("problem recorded", absent.problem is not None, True)

    print(f"\n{'PASSED' if not failures else str(failures) + ' FAILURE(S)'}")
    return 1 if failures else 0


# --------------------------------------------------------------------------


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("phrase", nargs="?", help="phrase to find, or a regex with --regex")
    ap.add_argument("--id", help="restrict to one document id (default: all)")
    ap.add_argument("--regex", action="store_true",
                    help="treat the phrase as a regex, matched against the raw page "
                         "text with its line breaks intact")
    ap.add_argument("--context", type=int, default=CONTEXT_CHARS,
                    help=f"characters of context either side (default {CONTEXT_CHARS})")
    ap.add_argument("--max", type=int, default=MAX_HITS_PER_DOC,
                    help="stop after this many hits per document (0 = no limit)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--list", action="store_true",
                    help="list the documents, their offsets and whether their text is here")
    ap.add_argument("--selftest", action="store_true",
                    help="prove the citation logic against synthetic entries; no "
                         "network, no dependence on the local extractions")
    ap.add_argument("--sources", default=str(SOURCES),
                    help="the 04-normalized/sources directory")
    args = ap.parse_args()

    if args.selftest:
        return selftest()
    if args.list:
        return cmd_list(pathlib.Path(args.sources).resolve())
    if not args.phrase:
        ap.error("a phrase is required (or --list / --selftest)")
    return cmd_search(args)


if __name__ == "__main__":
    raise SystemExit(main())
