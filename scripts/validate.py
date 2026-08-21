#!/usr/bin/env python3
"""Validate Alexandria's tracked research/documentation artifacts.

Alexandria is the research corpus now — no src/ or tests/ to lint, type
check, or run. That half of this script moved to
dhk/minority-report/scripts/validate.py along with the tooling it checked;
see https://github.com/dhk/alexandria/issues/33.

This half checks the corpus. Parsing every tracked JSON/TOML/YAML artifact so
a malformed one fails fast was the whole of it; that was too little. A
normative rule nobody runs is documentation, not a contract, and every defect
found in the corpus so far has been a written rule with no runner: supply
scores that left their declared scale, a grader that diverged from the
calibration spec on three axes, scores whose quotes nothing checks. So the
checks below apply the schemas in `schemas/` to the artifacts they govern, and
enforce the parts of docs/confidence-calibration.md that are mechanical.

Every check collects its failures rather than raising on the first, so one run
reports the whole picture.
"""

from __future__ import annotations

import csv
import json
import subprocess
import sys
import tomllib
from pathlib import Path
from statistics import median

import yaml
from jsonschema import Draft202012Validator

try:  # run as `python scripts/validate.py`, which is how CI invokes it
    from matrices import derive, parse_tables, publishable, render_median, strip_markers
except ImportError:  # pragma: no cover - imported as a package instead
    from scripts.matrices import derive, parse_tables, publishable, render_median, strip_markers

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research"
SCHEMAS = ROOT / "schemas"

SCORE_COLUMNS = ["claim_id", "model_id", "score", "quote", "grading_call_id"]
TOPIC_REQUIRED = ["title", "slug", "status", "assurance_level", "opened"]
ASSURANCE_LEVELS = {"bronze", "silver", "gold"}

# docs/instrument.md §3 — conformance is derived from recorded facts, never stored.
CONFORMING_INSTRUMENT = {
    "grader_topology": "per-model-blind",
    "score_derivation": "derived-lookup",
    "extraction_pass": "separate",
}


def _schema(name: str) -> Draft202012Validator:
    return Draft202012Validator(json.loads((SCHEMAS / name).read_text()))


def _rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def _load(path: Path, errors: list[str]) -> object | None:
    """Read a JSON or YAML artifact, recording a failure instead of raising.

    check_parse proves every tracked artifact parses, but each later check
    re-reads the files it cares about. An artifact that fails there is exactly
    the one a later check would blow up on — and a traceback would discard
    every problem collected so far, which is the opposite of what this script
    promises. Unreadable returns None and the caller skips it; the parse
    failure is already reported once, by whichever check reached it first.
    """
    try:
        raw = path.read_text()
        return json.loads(raw) if path.suffix == ".json" else yaml.safe_load(raw)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        message = f"{_rel(path)}: could not be read — {exc}"
        if message not in errors:
            errors.append(message)
        return None


def tracked_artifacts() -> list[Path]:
    """Return tracked data/configuration artifacts with parseable formats."""
    result = subprocess.run(
        ["git", "ls-files", "-z", "*.json", "*.toml", "*.yaml", "*.yml"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return [ROOT / path.decode() for path in result.stdout.split(b"\0") if path]


def investigations() -> list[Path]:
    """Every investigation directory under research/."""
    return sorted(p for p in RESEARCH.iterdir() if p.is_dir())


def run_records() -> list[Path]:
    """Run records under 03-runs/.

    Keyed on the r-<date>-<nn>.json filename convention. The single
    pre-convention investigation stores a manifest.json of a different shape
    and is deliberately out of scope — see run-record.schema.json.
    """
    return sorted(RESEARCH.glob("*/03-runs/r-*.json"))


def check_parse(errors: list[str]) -> None:
    """Parse every tracked JSON, TOML, and YAML artifact."""
    artifacts = tracked_artifacts()
    print(f"==> parse {len(artifacts)} tracked data/configuration artifacts")

    for path in artifacts:
        try:
            # Inside the try: git lists what is tracked, which is not the same
            # as what is on disk. A tracked file deleted in the working tree is
            # a real state, and reporting it beats crashing on it.
            raw = path.read_bytes()
            match path.suffix:
                case ".json":
                    json.loads(raw)
                case ".toml":
                    tomllib.loads(raw.decode())
                case ".yaml" | ".yml":
                    yaml.safe_load(raw)
        except OSError as exc:
            errors.append(f"{_rel(path)}: tracked but unreadable — {exc}")
        except (ValueError, yaml.YAMLError) as exc:
            errors.append(f"{_rel(path)}: does not parse — {exc}")


def check_run_records(errors: list[str]) -> None:
    """Every run record satisfies the run-record schema, instrument block included."""
    records = run_records()
    print(f"==> schema {len(records)} run records")
    validator = _schema("run-record.schema.json")

    for path in records:
        data = _load(path, errors)
        if not isinstance(data, dict):
            continue
        for problem in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
            location = "/".join(str(part) for part in problem.path) or "(root)"
            errors.append(f"{_rel(path)}: {location}: {problem.message}")
        if data.get("run_id") and data["run_id"] != path.stem:
            errors.append(f"{_rel(path)}: run_id {data['run_id']!r} does not match its filename")


def check_claim_lists(errors: list[str]) -> None:
    """Every claims.json satisfies the claim-list schema, with unique claim ids."""
    lists = sorted(RESEARCH.glob("**/claims.json"))
    print(f"==> schema {len(lists)} claim lists")
    validator = _schema("claims.schema.json")

    for path in lists:
        data = _load(path, errors)
        if data is None:
            continue
        for problem in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
            location = "/".join(str(part) for part in problem.path) or "(root)"
            errors.append(f"{_rel(path)}: {location}: {problem.message}")
        if isinstance(data, list):
            # Only well-formed ids: a claim missing one is already a schema
            # failure, and letting None reach the join turns that report into a
            # crash that swallows every other problem in the run.
            ids = [
                claim.get("claim_id")
                for claim in data
                if isinstance(claim, dict) and isinstance(claim.get("claim_id"), str)
            ]
            duplicates = sorted({i for i in ids if ids.count(i) > 1})
            if duplicates:
                errors.append(f"{_rel(path)}: duplicate claim_id: {', '.join(duplicates)}")


def check_score_tables(errors: list[str]) -> None:
    """Enforce the mechanical half of docs/confidence-calibration.md.

    §2 the score is one of seven integers; §5 a non-silent stance requires a
    quotable span and silence forbids one; and every scored claim must exist in
    the claim list beside it, in both directions.
    """
    tables = sorted(RESEARCH.glob("**/scores.csv"))
    print(f"==> scores {len(tables)} score tables")
    score_schema = _schema("claim-score.schema.json")

    for path in tables:
        try:
            with path.open(newline="") as handle:
                rows = list(csv.DictReader(handle))
        except (OSError, ValueError) as exc:
            errors.append(f"{_rel(path)}: could not be read — {exc}")
            continue

        if not rows:
            errors.append(f"{_rel(path)}: no score rows")
            continue

        missing_columns = [c for c in SCORE_COLUMNS if c not in rows[0]]
        if missing_columns:
            errors.append(f"{_rel(path)}: missing columns: {', '.join(missing_columns)}")
            continue

        claims_path = path.parent / "claims.json"
        claim_ids: set[str] = set()
        if not claims_path.exists():
            errors.append(f"{_rel(path)}: no claims.json beside it")
        else:
            claims = _load(claims_path, errors)
            if isinstance(claims, list):
                claim_ids = {
                    claim["claim_id"]
                    for claim in claims
                    if isinstance(claim, dict) and isinstance(claim.get("claim_id"), str)
                }

        scored_ids: set[str] = set()
        for line, row in enumerate(rows, start=2):
            where = f"{_rel(path)}:{line}"
            scored_ids.add(row["claim_id"])

            try:
                score = int(row["score"])
            except (TypeError, ValueError):
                errors.append(f"{where}: score {row['score']!r} is not an integer")
                continue

            for problem in score_schema.iter_errors(score):
                errors.append(f"{where}: score {score}: {problem.message}")

            quote = (row["quote"] or "").strip()
            if score != 0 and not quote:
                errors.append(
                    f"{where}: score {score:+d} has no quote — "
                    "a non-silent stance requires a quotable span (spec §5)"
                )
            if score == 0 and quote:
                errors.append(
                    f"{where}: score 0 carries a quote — "
                    "graded-silent means no bearing statement was found (spec §5)"
                )

            if claim_ids and row["claim_id"] not in claim_ids:
                errors.append(f"{where}: claim_id {row['claim_id']!r} is not in claims.json")

        unscored = sorted(claim_ids - scored_ids)
        if unscored:
            errors.append(f"{_rel(path)}: claims present but never scored: {', '.join(unscored)}")


def check_normalized_matrices(errors: list[str]) -> None:
    """Stage 04-normalized: votes stay on their declared scale and still derive the published value.

    This is the check whose absence let a control run publish a supply matrix
    holding votes from a different scale — see dhk/alexandria#62. Cell values
    are never stored, so the only way a matrix can disagree with its votes is
    for the published cross-reference to have drifted, which is exactly what
    published_value is here to catch.
    """
    sets = sorted(RESEARCH.glob("*/04-normalized/matrices.json"))
    print(f"==> matrices {len(sets)} normalized matrix sets")
    validator = _schema("normalized-matrix.schema.json")

    for path in sets:
        data = _load(path, errors)
        if data is None:
            continue
        problems = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
        for problem in problems:
            location = "/".join(str(part) for part in problem.path) or "(root)"
            errors.append(f"{_rel(path)}: {location}: {problem.message}")
        if problems:
            continue

        complete = data["coverage"] == "complete"
        responding = data["responding_model_count"]
        for matrix in data["matrices"]:
            label = f"{_rel(path)}: {matrix['matrix_id']}"
            low, high = matrix["scale"]["min"], matrix["scale"]["max"]
            rows, columns = matrix.get("rows"), matrix.get("columns")

            if complete and not (rows and columns):
                errors.append(f"{label}: coverage 'complete' requires rows and columns declared")

            seen: set[tuple[str, str]] = set()
            for cell in matrix["cells"]:
                where = f"{label}: {cell['row']} x {cell['column']}"
                seen.add((cell["row"], cell["column"]))

                stray = [v for v in cell["votes"] if not low <= v <= high]
                if stray:
                    errors.append(
                        f"{where}: vote(s) {stray} outside the declared scale "
                        f"{low}..{high} — a vote on another scale is not a datum"
                    )

                if cell["votes_attributed"] and len(cell.get("models") or []) != len(cell["votes"]):
                    errors.append(f"{where}: votes_attributed but models do not match votes 1:1")

                unrecorded = cell.get("unrecorded_model_count", 0)
                accounted = len(cell["votes"]) + unrecorded
                if accounted != responding:
                    errors.append(
                        f"{where}: {len(cell['votes'])} vote(s) + {unrecorded} unrecorded "
                        f"accounts for {accounted} of {responding} responding models — an "
                        "unaccounted model is how a partial sample passes as a full one"
                    )
                if unrecorded and not cell.get("unrecorded_reason"):
                    errors.append(
                        f"{where}: {unrecorded} unrecorded vote(s) with no reason — "
                        "'model declined' and 'not published' are different facts"
                    )

                if rows and cell["row"] not in rows:
                    errors.append(f"{where}: row is not in the declared row vocabulary")
                if columns and cell["column"] not in columns:
                    errors.append(f"{where}: column is not in the declared column vocabulary")

                published = cell.get("published_value")
                if published is not None:
                    # docs/normalization.md §7: the median is publishable only
                    # when it returns a category some model chose. Where it does
                    # not, the cell carries no value rather than a number nobody
                    # assigned.
                    permitted = publishable(cell["votes"])
                    if permitted != published:
                        derived = render_median(median(cell["votes"]))
                        reason = (
                            f"derive {derived}, which no model assigned, so §7 permits only "
                            f"{permitted!r}"
                            if permitted != derived
                            else f"derive {derived}"
                        )
                        errors.append(
                            f"{where}: votes {cell['votes']} {reason}, "
                            f"but the published analysis carries {published!r}"
                        )

            if complete and rows and columns:
                missing = [(r, c) for r in rows for c in columns if (r, c) not in seen]
                if missing:
                    shown = ", ".join(f"{r} x {c}" for r, c in missing[:5])
                    errors.append(
                        f"{label}: coverage 'complete' but {len(missing)} cell(s) "
                        f"carry no votes: {shown}{' …' if len(missing) > 5 else ''}"
                    )



def check_published_tables(errors: list[str]) -> None:
    """The digits printed in an analysis must be the ones its votes derive.

    check_normalized_matrices closes half of the cross-reference: the votes
    derive published_value. This closes the other half — that the number in
    05-analysis/matrices.md is that same number. Without it published_value is
    a hand-copied claim about a hand-written table and the two can drift
    together, which is the shape dhk/alexandria#62 took.

    Only cells whose votes are recorded can be checked. At coverage
    'contested-cells-only' that is ten of two hundred, and the count is printed
    rather than left to be assumed.
    """
    sets = sorted(RESEARCH.glob("*/04-normalized/matrices.json"))
    checked = 0

    for path in sets:
        data = _load(path, errors)
        if not isinstance(data, dict):
            continue
        document = path.parent.parent / "05-analysis" / "matrices.md"
        if not document.exists():
            errors.append(f"{_rel(path)}: no 05-analysis/matrices.md to cross-check against")
            continue
        try:
            tables = parse_tables(document.read_text())
        except OSError as exc:
            errors.append(f"{_rel(document)}: unreadable — {exc}")
            continue

        for matrix in data.get("matrices", []):
            for cell in matrix.get("cells", []):
                if not isinstance(cell, dict) or cell.get("published_value") is None:
                    continue
                key = (cell["row"], cell["column"])
                printed = [table[key] for table in tables if key in table]
                where = f"{_rel(document)}: {cell['row']} x {cell['column']}"
                if not printed:
                    errors.append(
                        f"{where}: 04-normalized records a published value for this cell, "
                        "but no table in the analysis carries that row and column"
                    )
                    continue
                expected = publishable(cell["votes"])
                for raw in printed:
                    if strip_markers(raw) != expected:
                        errors.append(
                            f"{where}: votes {cell['votes']} derive {expected}, "
                            f"but the analysis prints {raw!r}"
                        )
                checked += 1

        # A signed zero is never a value a model assigned: it is the midpoint of
        # two differing votes, which is what §7 forbids. Unlike the check above
        # this needs no recorded votes, so it reaches the cells whose votes were
        # never promoted — which is most of them.
        for table in tables:
            for (row, column), raw in table.items():
                if strip_markers(raw) in {"+0", "-0"}:
                    errors.append(
                        f"{_rel(document)}: {row} x {column}: prints {raw!r}. A signed zero is "
                        "the midpoint of two differing votes and is not a value on the scale; "
                        "§7 permits no value here"
                    )

    print(f"==> published {checked} matrix cell(s) cross-checked against their votes")


SUBSTANTIVE_SUPPORT = {"supports", "partially-supports", "contradicts", "absent"}


def check_source_audits(errors: list[str]) -> None:
    """A source audit may only claim what opening the source can establish.

    The rule worth enforcing is the one that is easy to break by accident: a
    substantive verdict about what a work argues requires that the work was
    read. A catalogue record or a search result establishes that a source
    exists, never what it says, and letting the second pass as the first would
    rebuild the Silver gap inside the artifact meant to close it.
    """
    audits = sorted(RESEARCH.glob("*/05-analysis/source-audit.json"))
    print(f"==> sources {len(audits)} source audits")
    validator = _schema("source-audit.schema.json")

    for path in audits:
        data = _load(path, errors)
        if data is None:
            continue
        problems = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
        for problem in problems:
            location = "/".join(str(part) for part in problem.path) or "(root)"
            errors.append(f"{_rel(path)}: {location}: {problem.message}")
        if problems:
            continue

        investigation = path.parent.parent
        if data["investigation"] != investigation.name:
            errors.append(
                f"{_rel(path)}: investigation {data['investigation']!r} does not match its directory"
            )

        claims = _load(investigation / "05-analysis" / "claims.json", errors)
        known = (
            {c["claim_id"] for c in claims if isinstance(c, dict) and "claim_id" in c}
            if isinstance(claims, list)
            else set()
        )

        for entry in data["entries"]:
            where = f"{_rel(path)}: {entry['source_id']}"

            for field in ("citation_accuracy", "claim_support"):
                check = entry[field]
                verdict, method = check["verdict"], check.get("method")
                if verdict == "unchecked":
                    continue
                substantive = field == "claim_support" and verdict in SUBSTANTIVE_SUPPORT
                if not method:
                    errors.append(f"{where}: {field} verdict {verdict!r} records no method")
                elif substantive and method != "primary-source":
                    errors.append(
                        f"{where}: claim_support {verdict!r} rests on method {method!r} — "
                        "only reading the source itself can settle what it argues"
                    )
                if not check.get("checked_on"):
                    errors.append(f"{where}: {field} verdict {verdict!r} records no date")
                if substantive and not (check.get("quote") or "").strip():
                    errors.append(
                        f"{where}: claim_support {verdict!r} shows no passage from the source — "
                        "a verdict a reader cannot check against the words is an assertion"
                    )

            unknown = [c for c in entry["supports_claims"] if known and c not in known]
            if unknown:
                errors.append(f"{where}: cites claims not in claims.json: {', '.join(unknown)}")


def check_assurance(errors: list[str]) -> None:
    """Gold requires the audit that earns it, covering every claim that cites a source."""
    print("==> assurance gold claims require a completed source audit")

    for directory in investigations():
        topic = (
            _load(directory / "topic.yaml", errors) if (directory / "topic.yaml").exists() else None
        )
        if not isinstance(topic, dict) or topic.get("assurance_level") != "gold":
            continue

        audit_path = directory / "05-analysis" / "source-audit.json"
        if not audit_path.exists():
            errors.append(
                f"{_rel(directory)}: assurance_level 'gold' with no 05-analysis/source-audit.json — "
                "Gold is the level at which somebody has opened the sources"
            )
            continue

        audit = _load(audit_path, errors)
        if not isinstance(audit, dict):
            continue
        pending = [
            entry["source_id"]
            for entry in audit.get("entries", [])
            if entry.get("claim_support", {}).get("verdict") in (None, "unchecked")
        ]
        if pending:
            errors.append(
                f"{_rel(directory)}: assurance_level 'gold' with {len(pending)} source(s) "
                f"whose claim support is unchecked: {', '.join(pending[:5])}"
            )


def check_investigations(errors: list[str]) -> None:
    """Every investigation carries a topic.yaml and README.md that agree with it."""
    directories = investigations()
    print(f"==> contract {len(directories)} investigations")

    for directory in directories:
        topic_path = directory / "topic.yaml"
        if not (directory / "README.md").exists():
            errors.append(f"{_rel(directory)}: no README.md")
        if not topic_path.exists():
            errors.append(f"{_rel(directory)}: no topic.yaml")
            continue

        topic = _load(topic_path, errors)
        if not isinstance(topic, dict):
            continue
        for field in TOPIC_REQUIRED:
            if not topic.get(field):
                errors.append(f"{_rel(topic_path)}: missing required field {field!r}")

        if topic.get("slug") and topic["slug"] != directory.name:
            errors.append(
                f"{_rel(topic_path)}: slug {topic['slug']!r} does not match its directory"
            )
        level = topic.get("assurance_level")
        if level and level not in ASSURANCE_LEVELS:
            errors.append(
                f"{_rel(topic_path)}: assurance_level {level!r} is not one of "
                f"{', '.join(sorted(ASSURANCE_LEVELS))}"
            )


def report_instruments() -> None:
    """Derive conformance per run and print it. Informational, never fatal.

    A non-conforming run that says so is behaving correctly; the block's job is
    to state what a run is. What fails — in check_run_records, via the schema —
    is a run that declines to say. See docs/instrument.md §3.
    """
    records = run_records()
    if not records:
        return

    print(f"\n==> instrument conformance ({len(records)} runs, derived not stored)")
    for path in records:
        unreadable: list[str] = []
        data = _load(path, unreadable)
        if not isinstance(data, dict):
            print(f"    {path.stem:<16} unreadable — reported above")
            continue
        instrument = data.get("instrument") or {}
        divergences = [
            field
            for field, required in CONFORMING_INSTRUMENT.items()
            if instrument.get(field) != required
        ]
        verdict = "conforming" if not divergences else "diverges: " + ", ".join(divergences)
        print(f"    {path.stem:<16} {verdict}")


def _report(errors: list[str]) -> None:
    print(f"\n{len(errors)} problem(s):", file=sys.stderr)
    for error in errors:
        print(f"  {error}", file=sys.stderr)


def main() -> int:
    errors: list[str] = []
    try:
        check_parse(errors)
        check_run_records(errors)
        check_claim_lists(errors)
        check_score_tables(errors)
        check_normalized_matrices(errors)
        check_published_tables(errors)
        check_source_audits(errors)
        check_investigations(errors)
        check_assurance(errors)
    except Exception as exc:  # noqa: BLE001 - a backstop, not a handler
        # Each check guards its own reads, so reaching here means a defect in
        # this script rather than in the corpus. Report what was collected
        # before saying so: a traceback that discards ten real findings to
        # announce an eleventh problem is worse than useless.
        if errors:
            _report(errors)
        print(f"\nvalidation aborted: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1

    report_instruments()

    if errors:
        _report(errors)
        return 1

    print("\nValidation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
