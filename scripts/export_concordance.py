#!/usr/bin/env python3
"""Regenerate generated/concordance-feed.json (issue #36).

Generated, derived data -- AGENTS.md's "Generated files: Generated indexes
may be rebuilt" applies directly. Run this, review the diff, and commit it
like any other change; nothing in this repository writes this file for you.

    uv run --frozen python scripts/export_concordance.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from alexandria.concordance import build_concordance_feed, feed_to_json
from alexandria.infrastructure.config import load_config

OUTPUT_PATH = ROOT / "generated" / "concordance-feed.json"


def main() -> int:
    config = load_config()
    feed = build_concordance_feed(config)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(feed_to_json(feed), indent=2, sort_keys=True) + "\n")
    print(f"Wrote {len(feed.entries)} concordance entries to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
