#!/usr/bin/env python3
"""Emit a published matrix table from the votes in 04-normalized.

The digits in `05-analysis/matrices.md` are hand-typed today, and hand-authored
numbers with no producer are where dhk/alexandria#62 hid. This is the producer.
It derives every cell it can from recorded votes and says plainly how many it
cannot, so a partial emission can never be mistaken for the whole table.

    python scripts/generate_matrices.py <investigation-slug> [--matrix supply]

At coverage 'contested-cells-only' most cells have no recorded votes and print
as a gap. The command exits non-zero in that case: it has not produced
something anyone should paste over a published table. Once coverage reaches
'complete' the same command emits the table in full and exits zero.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    from matrices import derive, emit_table, parse_tables
except ImportError:  # pragma: no cover - imported as a package instead
    from scripts.matrices import derive, emit_table, parse_tables

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slug", help="investigation directory under research/")
    parser.add_argument("--matrix", help="matrix_id to emit; default every matrix")
    args = parser.parse_args()

    investigation = RESEARCH / args.slug
    source = investigation / "04-normalized" / "matrices.json"
    if not source.exists():
        print(f"no 04-normalized/matrices.json under {args.slug}", file=sys.stderr)
        return 2

    data = json.loads(source.read_text())
    document = investigation / "05-analysis" / "matrices.md"
    printed = parse_tables(document.read_text()) if document.exists() else []
    complete = data["coverage"] == "complete"
    incomplete: list[str] = []

    for matrix in data["matrices"]:
        if args.matrix and matrix["matrix_id"] != args.matrix:
            continue
        values = {(c["row"], c["column"]): derive(c["votes"]) for c in matrix["cells"]}

        # Rows and columns are only required to be declared at complete
        # coverage. Below it, fall back to the vocabulary the published
        # document uses, so the emission lines up with the table it would
        # replace rather than inventing an order of its own.
        table = _best_match(printed, set(values))
        columns = matrix.get("columns") or _vocabulary(table, index=1)
        rows = matrix.get("rows") or _vocabulary(table, index=0)
        if not (rows and columns):
            print(f"{matrix['matrix_id']}: no row/column vocabulary to lay out", file=sys.stderr)
            incomplete.append(matrix["matrix_id"])
            continue

        missing = [(r, c) for r in rows for c in columns if (r, c) not in values]
        print(f"\n### {matrix.get('title', matrix['matrix_id'])}\n")
        print(emit_table(rows, columns, values))
        derived_count = len(rows) * len(columns) - len(missing)
        print(
            f"\n<!-- {derived_count} of {len(rows) * len(columns)} cells derived from recorded "
            f"votes; {len(missing)} carry no votes and print as · -->"
        )
        if missing:
            incomplete.append(matrix["matrix_id"])

    if incomplete and not complete:
        print(
            f"\ncoverage is {data['coverage']!r}: {', '.join(incomplete)} cannot be emitted in "
            "full. Promote the remaining votes into 04-normalized before this replaces a "
            "published table.",
            file=sys.stderr,
        )
        return 1
    return 0


def _best_match(
    tables: list[dict[tuple[str, str], str]], keys: set[tuple[str, str]]
) -> dict[tuple[str, str], str]:
    """The published table this matrix's cells actually live in.

    A matrices.md holds more than the matrices — distribution counts, contested
    listings — and taking the vocabulary from all of them at once invents rows
    the matrix does not have.
    """
    if not tables:
        return {}
    return max(tables, key=lambda table: len(keys & set(table)))


def _vocabulary(table: dict[tuple[str, str], str], index: int) -> list[str]:
    """Row or column labels in the order the published document uses them."""
    seen: list[str] = []
    for key in table:
        if key[index] not in seen:
            seen.append(key[index])
    return seen


if __name__ == "__main__":
    raise SystemExit(main())
