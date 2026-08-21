"""The rendering rule for a derived matrix cell, and the markdown it produces.

One home for two things that were previously in two places and could drift:
how a derived median is printed, and how a published matrix table is read back.
`validate.py` uses this to check that the digits in a hand-written
`05-analysis/matrices.md` still agree with the votes in `04-normalized`;
`generate_matrices.py` uses it to emit those tables instead of a person typing
them, which is the direction the corpus is going (dhk/alexandria#62).
"""

from __future__ import annotations

import re
from statistics import median

#: Markers the published tables add to a cell and which carry no numeric
#: meaning: a dagger for a declined vote, bold-with-bang for a contested cell.
CELL_MARKERS = re.compile(r"[*†‡!]")


def render_median(value: float) -> str:
    """Render a derived median the way the published matrices print it.

    Sign-preserving truncation toward zero, so a half-step between two votes
    stays visible as a signed zero rather than being rounded into a real
    value: -0 is -0.5, +0 is +0.5, and a true zero is unsigned.
    """
    if value == 0:
        return "0"
    truncated = int(value) if value > 0 else -int(-value)
    if truncated == 0:
        return "+0" if value > 0 else "-0"
    return f"{truncated:+d}"


def derive(votes: list[int]) -> str:
    """The published value a cell's votes produce, with no cell value stored."""
    return render_median(median(votes))


def strip_markers(cell: str) -> str:
    """The numeric content of a published cell, without its annotation."""
    return CELL_MARKERS.sub("", cell).strip()


def _split(line: str) -> list[str]:
    return [part.strip() for part in line.strip().strip("|").split("|")]


def parse_tables(markdown: str) -> list[dict[tuple[str, str], str]]:
    """Every markdown table, as {(row label, column label): raw cell}.

    Deliberately forgiving about what surrounds the tables: this reads a
    hand-written document whose prose is not this module's business.
    """
    tables: list[dict[tuple[str, str], str]] = []
    lines = markdown.splitlines()
    index = 0
    while index < len(lines):
        if not lines[index].strip().startswith("|"):
            index += 1
            continue
        header = _split(lines[index])
        if index + 1 >= len(lines) or not set(_split(lines[index + 1])[0]) <= {"-", ":"}:
            index += 1
            continue
        table: dict[tuple[str, str], str] = {}
        index += 2
        while index < len(lines) and lines[index].strip().startswith("|"):
            cells = _split(lines[index])
            row = strip_markers(cells[0])
            for column, value in zip(header[1:], cells[1:], strict=False):
                table[(row, strip_markers(column))] = value
            index += 1
        if table:
            tables.append(table)
    return tables


def emit_table(rows: list[str], columns: list[str], values: dict[tuple[str, str], str]) -> str:
    """A markdown table of derived values. Missing cells print as a gap."""
    lines = [
        "| " + " | ".join(["Consideration", *columns]) + " |",
        "|" + "---|" * (len(columns) + 1),
    ]
    for row in rows:
        cells = [values.get((row, column), "·") for column in columns]
        lines.append("| " + " | ".join([row, *cells]) + " |")
    return "\n".join(lines)
