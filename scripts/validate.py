#!/usr/bin/env python3
"""Validate Alexandria's tracked research/documentation artifacts.

Alexandria is the research corpus now — no src/ or tests/ to lint, type
check, or run. That half of this script moved to
dhk/minority-report/scripts/validate.py along with the tooling it checked;
see https://github.com/dhk/alexandria/issues/33. This half — parsing every
tracked JSON/TOML/YAML artifact so a malformed one fails fast — stays here,
against research/, schemas/, and the rest of the corpus.
"""

from __future__ import annotations

import json
import subprocess
import sys
import tomllib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def tracked_artifacts() -> list[Path]:
    """Return tracked data/configuration artifacts with parseable formats."""
    result = subprocess.run(
        ["git", "ls-files", "-z", "*.json", "*.toml", "*.yaml", "*.yml"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return [ROOT / path.decode() for path in result.stdout.split(b"\0") if path]


def validate_artifacts() -> None:
    """Parse every tracked JSON, TOML, and YAML artifact."""
    artifacts = tracked_artifacts()
    print(f"\n==> parse {len(artifacts)} tracked data/configuration artifacts", flush=True)

    for path in artifacts:
        raw = path.read_bytes()
        match path.suffix:
            case ".json":
                json.loads(raw)
            case ".toml":
                tomllib.loads(raw.decode())
            case ".yaml" | ".yml":
                yaml.safe_load(raw)
            case _:  # pragma: no cover - filtered by tracked_artifacts
                raise AssertionError(f"unsupported artifact type: {path}")


def main() -> int:
    try:
        validate_artifacts()
    except (OSError, RuntimeError, subprocess.CalledProcessError, ValueError) as exc:
        print(f"\nvalidation failed: {exc}", file=sys.stderr)
        return 1

    print("\nValidation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
