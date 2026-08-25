#!/usr/bin/env python3
"""Build an investigation's browser viewer from its published matrices.

    python scripts/build_viewer.py <investigation-slug>

The viewer used to carry its own copy of every cell, transcribed by hand into
a JSON island. That is a fourth place the same two hundred numbers lived, and
the only one nothing checked — the shape dhk/alexandria#62 took, one layer out.
This makes the island a derived artifact: `05-analysis/matrices.md` is read
through `scripts/matrices.py`, the same parser `validate.py` cross-checks the
published tables with, so a correction to the analysis reaches the page and
cannot reach it differently than it reaches the validator.

`04-normalized/matrices.json` would be the better source and is not yet a
usable one: at coverage 'contested-cells-only' it records votes for eleven of
two hundred cells, so a viewer built from it would be mostly gaps. When
coverage reaches 'complete', `generate_matrices.py` regenerates the analysis
from those votes and this keeps building from the analysis — the chain closes
without this script changing.

`06-viewer/index.html` is generated and may be rebuilt. `06-viewer/template.html`
holds everything that is not a cell value: the layout, the styles, the
behaviour, and the prose describing each technique.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

try:
    from matrices import WITHHELD, parse_tables, strip_markers
except ImportError:  # pragma: no cover - imported as a package instead
    from scripts.matrices import WITHHELD, parse_tables, strip_markers

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research"

#: Where the built island is substituted into the template.
PLACEHOLDER = "@@GRID@@"

#: A contested-cell bullet: "- **Row x Column** - +1, 0, +2".
CONTESTED = re.compile(r"^-\s+\*\*(?P<cell>[^*]+?)\*\*\s+[—–-]\s+(?P<votes>[-+\d,\s]+)$")

#: The markers a published cell may carry, and what each one means to the page.
#: `matrices.py` strips them; the viewer draws them, so it has to read them.
DECLINED = "†"
CONTESTED_MARK = "!"


def read_cell(raw: str) -> dict:
    """One published cell as the page consumes it: value, and its two flags."""
    text = strip_markers(raw)
    return {
        "v": None if text in {WITHHELD, ""} else int(text),
        "c": CONTESTED_MARK in raw,
        "d": DECLINED in raw,
    }


def shape(table: dict[tuple[str, str], str], rows: list[str], columns: list[str]) -> dict:
    """A parsed table in the row-major form the page's renderer expects."""
    return {
        "cols": columns,
        "rows": [
            {"name": row, "cells": [read_cell(table[(row, column)]) for column in columns]}
            for row in rows
        ],
    }


def _ordered(seen: list[str]) -> list[str]:
    """Distinct labels in first-seen order — the order the table prints them."""
    return list(dict.fromkeys(seen))


def _axes(table: dict[tuple[str, str], str]) -> tuple[list[str], list[str]]:
    return _ordered([row for row, _ in table]), _ordered([column for _, column in table])


def build_island(analysis: str, techniques: list[str]) -> dict:
    """The two matrices and the contested-cell votes, from the published document.

    The supply matrix is identified by its columns rather than by its position
    in the file: a document that gains a table above it would otherwise shift
    the wrong numbers onto the page silently, and this is the one thing here
    that a reader could not check by looking.
    """
    wanted = set(techniques)
    supply, demand = None, None
    for table in parse_tables(analysis):
        rows, columns = _axes(table)
        if set(columns) == wanted:
            if supply is not None:
                raise ViewerError("two tables carry the technique columns; cannot tell them apart")
            supply = (table, rows, columns)
        elif demand is None and supply is None and len(columns) == len(wanted):
            demand = (table, rows, columns)

    if supply is None:
        raise ViewerError("no table in the analysis carries the technique columns")
    if demand is None:
        raise ViewerError("no demand table found ahead of the technique table")
    if demand[1] != supply[1]:
        raise ViewerError("the two matrices do not share a consideration axis; they cannot be joined")

    contested = [
        {"cell": m.group("cell").strip(), "votes": " ".join(m.group("votes").split())}
        for line in analysis.splitlines()
        if (m := CONTESTED.match(line.strip()))
    ]
    return {"A": shape(*demand), "B": shape(*supply), "contested": contested}


class ViewerError(Exception):
    """The viewer cannot be built, with the reason a person needs to fix it."""


def build(slug: str) -> tuple[Path, str, dict]:
    """The page this investigation's analysis produces, without writing it.

    Returns where it belongs, what it should contain, and the island that went
    into it. Kept separate from `main` so `validate.py` can build a viewer to
    compare against the committed one without shelling out or writing a file.
    """
    viewer = RESEARCH / slug / "06-viewer"
    template_path = viewer / "template.html"
    analysis_path = RESEARCH / slug / "05-analysis" / "matrices.md"
    for path in (template_path, analysis_path):
        if not path.exists():
            raise ViewerError(f"missing {path.relative_to(ROOT)}")

    template = template_path.read_text()
    if PLACEHOLDER not in template:
        raise ViewerError(f"{template_path.relative_to(ROOT)} has no {PLACEHOLDER} to fill")

    declared = re.search(r"const TECH = (\{.*?\n  \});", template, re.S)
    if declared is None:
        raise ViewerError(f"{template_path.relative_to(ROOT)} declares no TECH record set")

    island = build_island(analysis_path.read_text(), list(json.loads(declared.group(1))))
    return viewer / "index.html", template.replace(PLACEHOLDER, json.dumps(island, ensure_ascii=False)), island


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slug", help="investigation directory under research/")
    parser.add_argument("--check", action="store_true",
                        help="exit non-zero if index.html is not what a build would write")
    args = parser.parse_args()

    try:
        output, built, island = build(args.slug)
    except ViewerError as exc:
        print(exc, file=sys.stderr)
        return 2

    if args.check:
        if (output.read_text() if output.exists() else "") != built:
            print(f"{output.relative_to(ROOT)} is not what the analysis builds", file=sys.stderr)
            return 1
        print(f"==> {output.relative_to(ROOT)} matches a fresh build")
        return 0

    output.write_text(built)
    cells = sum(len(m["rows"]) * len(m["cols"]) for m in (island["A"], island["B"]))
    print(f"wrote {output.relative_to(ROOT)}: {cells} cells, "
          f"{len(island['contested'])} contested, derived from 05-analysis/matrices.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
