#!/usr/bin/env python3
"""Run Alexandria's repository validation checks."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tomllib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def run(*command: str) -> None:
    """Run one validation command from the repository root."""
    executable = command[0]
    if shutil.which(executable) is None:
        raise RuntimeError(
            f"{executable!r} is unavailable; run this validator with "
            "`uv run --frozen python scripts/validate.py`"
        )

    print(f"\n==> {' '.join(command)}", flush=True)
    subprocess.run(command, cwd=ROOT, check=True)


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
        run("ruff", "check", ".")
        run("ruff", "format", "--check", "src", "tests", "scripts")
        run("mypy", "src", "tests")
        run("pytest")
    except (OSError, RuntimeError, subprocess.CalledProcessError, ValueError) as exc:
        print(f"\nvalidation failed: {exc}", file=sys.stderr)
        return 1

    print("\nValidation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
