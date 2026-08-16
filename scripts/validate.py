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
        raw = path.read_bytes()
        try:
            match path.suffix:
                case ".json":
                    json.loads(raw)
                case ".toml":
                    tomllib.loads(raw.decode())
                case ".yaml" | ".yml":
                    yaml.safe_load(raw)
        except (ValueError, yaml.YAMLError) as exc:
            errors.append(f"{_rel(path)}: does not parse — {exc}")


def check_run_records(errors: list[str]) -> None:
    """Every run record satisfies the run-record schema, instrument block included."""
    records = run_records()
    print(f"==> schema {len(records)} run records")
    validator = _schema("run-record.schema.json")

    for path in records:
        data = json.loads(path.read_text())
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
        data = json.loads(path.read_text())
        for problem in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
            location = "/".join(str(part) for part in problem.path) or "(root)"
            errors.append(f"{_rel(path)}: {location}: {problem.message}")
        if isinstance(data, list):
            ids = [claim.get("claim_id") for claim in data if isinstance(claim, dict)]
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
        with path.open(newline="") as handle:
            rows = list(csv.DictReader(handle))

        if not rows:
            errors.append(f"{_rel(path)}: no score rows")
            continue

        missing_columns = [c for c in SCORE_COLUMNS if c not in rows[0]]
        if missing_columns:
            errors.append(f"{_rel(path)}: missing columns: {', '.join(missing_columns)}")
            continue

        claims_path = path.parent / "claims.json"
        claim_ids: set[str] = set()
        if claims_path.exists():
            claim_ids = {
                claim["claim_id"]
                for claim in json.loads(claims_path.read_text())
                if isinstance(claim, dict) and "claim_id" in claim
            }
        else:
            errors.append(f"{_rel(path)}: no claims.json beside it")

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


def _render_median(value: float) -> str:
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
        data = json.loads(path.read_text())
        problems = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
        for problem in problems:
            location = "/".join(str(part) for part in problem.path) or "(root)"
            errors.append(f"{_rel(path)}: {location}: {problem.message}")
        if problems:
            continue

        complete = data["coverage"] == "complete"
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

                if rows and cell["row"] not in rows:
                    errors.append(f"{where}: row is not in the declared row vocabulary")
                if columns and cell["column"] not in columns:
                    errors.append(f"{where}: column is not in the declared column vocabulary")

                published = cell.get("published_value")
                if published is not None:
                    derived = _render_median(median(cell["votes"]))
                    if derived != published:
                        errors.append(
                            f"{where}: votes {cell['votes']} derive {derived}, "
                            f"but the published analysis carries {published}"
                        )

            if complete and rows and columns:
                missing = [(r, c) for r in rows for c in columns if (r, c) not in seen]
                if missing:
                    shown = ", ".join(f"{r} x {c}" for r, c in missing[:5])
                    errors.append(
                        f"{label}: coverage 'complete' but {len(missing)} cell(s) "
                        f"carry no votes: {shown}{' …' if len(missing) > 5 else ''}"
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

        topic = yaml.safe_load(topic_path.read_text()) or {}
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
        instrument = json.loads(path.read_text()).get("instrument") or {}
        divergences = [
            field
            for field, required in CONFORMING_INSTRUMENT.items()
            if instrument.get(field) != required
        ]
        verdict = "conforming" if not divergences else "diverges: " + ", ".join(divergences)
        print(f"    {path.stem:<16} {verdict}")


def main() -> int:
    errors: list[str] = []
    try:
        check_parse(errors)
        check_run_records(errors)
        check_claim_lists(errors)
        check_score_tables(errors)
        check_normalized_matrices(errors)
        check_investigations(errors)
    except (OSError, RuntimeError, subprocess.CalledProcessError) as exc:
        print(f"\nvalidation failed: {exc}", file=sys.stderr)
        return 1

    report_instruments()

    if errors:
        print(f"\n{len(errors)} problem(s):", file=sys.stderr)
        for error in errors:
            print(f"  {error}", file=sys.stderr)
        return 1

    print("\nValidation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
