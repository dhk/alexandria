#!/usr/bin/env python3
"""Acquire San Francisco neighbourhood boundaries from DataSF, licence first.

    uv run --no-project python acquire-neighborhoods.py --licence     # check only
    uv run --no-project python acquire-neighborhoods.py --dry-run
    uv run --no-project python acquire-neighborhoods.py               # fetch + write

Run where the network is open -- lobster, not a session container, whose egress
does not reach data.sfgov.org.

WHY THIS LEADS WITH THE LICENCE

This repository is MIT. TIGER/Line is public domain under 17 U.S.C. 105, which
is why 04-normalized/geo/ carries no obligation and the MIT licence stays true.
DataSF is a different publisher with its own terms, and this script does not
know them: the container it was written in cannot reach data.sfgov.org, so
hardcoding "DataSF is public domain" would be an unverified claim of exactly
the kind the rest of this investigation refuses to make.

So the terms are read at run time, from the dataset's own metadata, and the
data is written only if they are on the allowlist below. An unrecognised
licence stops the run and prints what it found. That is a refusal, not a
failure -- the right move is to read the terms and decide, not to widen the
allowlist to make the error go away.

WHAT THIS IS FOR, AND WHAT IT IS NOT

These are MODERN ADMINISTRATIVE boundaries: one authoritative polygon per
neighbourhood, city-wide, no disputes. They are a frame to hang history on.

They are NOT historical place names. Happy Valley, Tar Flat and the Barbary
Coast have contested extents assembled out of sources, and no open-data
download produces those. Drawing a DataSF polygon and labelling it with a
historical name would assert a precision the record does not support.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import pathlib
import sys
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent / "04-normalized" / "geo"

HOST = "https://data.sfgov.org"

# The dataset id below is RECALLED, not verified -- it is the identifier this
# script's author believed corresponded to DataSF's "Analysis Neighborhoods".
# It may be wrong. The run therefore prints the dataset's own name and
# description before writing anything, so a wrong id is caught by eye rather
# than silently fetching some other polygon set. --dataset overrides it.
DATASET = "p5b7-5n3h"

PRECISION = 6

# Licences this repository can carry. The test is share-alike, not openness:
# an ODbL extract committed here would put ODbL on an MIT repository and
# arguably on any geometry georeferenced against it -- the same reasoning that
# made acquire-geo.py refuse Overture and default to TIGER.
ALLOWED = {
    "public domain": "no obligation",
    "public domain dedication and license": "PDDL, no obligation",
    "pddl": "PDDL, no obligation",
    "cc0": "no obligation",
    "creative commons 1.0 universal": "CC0, no obligation",
    "cc-by": "attribution required, no share-alike",
    "creative commons attribution": "attribution required, no share-alike",
    "creative commons attribution 3.0": "attribution required, no share-alike",
    "creative commons attribution 4.0": "attribution required, no share-alike",
}
REFUSED = {
    "odbl": "share-alike; would qualify this repository's MIT licence",
    "open database license": "share-alike; would qualify this repository's MIT licence",
    "cc-by-sa": "share-alike; would qualify this repository's MIT licence",
    "creative commons attribution share-alike": "share-alike; would qualify this MIT repository",
}


def get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "alexandria-corpus/acquire-neighborhoods"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read()


def metadata(dataset: str) -> dict:
    return json.loads(get(f"{HOST}/api/views/{dataset}.json"))


def read_licence(meta: dict):
    """Return (raw label, verdict, reason). Verdict is allow / refuse / unknown."""
    raw = ""
    for key in ("licenseId", "license"):
        v = meta.get(key)
        if isinstance(v, str) and v.strip():
            raw = v.strip(); break
        if isinstance(v, dict):
            raw = (v.get("name") or v.get("termsLink") or "").strip()
            if raw:
                break
    norm = raw.lower().replace("_", " ").replace("-", "-").strip()
    for key, why in REFUSED.items():
        if key in norm:
            return raw, "refuse", why
    for key, why in ALLOWED.items():
        if key in norm:
            return raw, "allow", why
    return raw or "(none stated)", "unknown", "not on the allowlist in this script"


def geojson(dataset: str) -> bytes:
    """Socrata serves map datasets from the geospatial endpoint and tabular ones
    from /resource. Try the first, fall back to the second, and say which won."""
    urls = [
        f"{HOST}/api/geospatial/{dataset}?method=export&format=GeoJSON",
        f"{HOST}/resource/{dataset}.geojson?$limit=5000",
    ]
    last = None
    for u in urls:
        try:
            payload = get(u)
            json.loads(payload)          # a Socrata error page is not GeoJSON
            print(f"  fetched from {u}", file=sys.stderr)
            return payload
        except Exception as exc:         # noqa: BLE001 - report and try the next
            last = f"{u}: {exc}"
    raise SystemExit(f"no GeoJSON endpoint answered.\n  last error: {last}")


def thin(obj: dict) -> dict:
    def r(x):
        if isinstance(x, list):
            return [r(i) for i in x]
        if isinstance(x, float):
            return round(x, PRECISION)
        return x
    for f in obj.get("features", []):
        f["geometry"]["coordinates"] = r(f["geometry"]["coordinates"])
    return obj


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--dataset", default=DATASET, help=f"Socrata dataset id (default {DATASET})")
    ap.add_argument("--licence", action="store_true", help="report the terms and exit, write nothing")
    ap.add_argument("--dry-run", action="store_true", help="say what would be fetched and written")
    ap.add_argument("--out", default=str(OUT), help="output directory")
    ap.add_argument("--force", action="store_true",
                    help="write despite an unknown licence. Only after reading the terms "
                         "yourself; the sidecar records that this was used.")
    args = ap.parse_args()

    print(f"dataset {args.dataset} at {HOST}", file=sys.stderr)
    if args.dry_run:
        print(f"  would read {HOST}/api/views/{args.dataset}.json for terms")
        print(f"  would fetch GeoJSON and write {pathlib.Path(args.out).resolve()}/neighborhoods.geojson")
        return 0

    meta = metadata(args.dataset)
    name = meta.get("name", "(unnamed)")
    attribution = meta.get("attribution") or "(none stated)"
    print(f'\n  name         {name}')
    print(f'  attribution  {attribution}')
    desc = (meta.get("description") or "").strip().replace("\n", " ")
    if desc:
        print(f'  description  {desc[:160]}{"…" if len(desc) > 160 else ""}')

    raw, verdict, why = read_licence(meta)
    print(f'  licence      {raw}  ->  {verdict.upper()} ({why})\n')
    print("  Check the name above is the dataset you meant before trusting anything below.\n")

    if args.licence:
        return 0
    if verdict == "refuse":
        print(f"REFUSED: {raw} is {why}.\n"
              "Nothing written. This is the same reasoning that made acquire-geo.py\n"
              "default to TIGER rather than Overture.", file=sys.stderr)
        return 2
    if verdict == "unknown" and not args.force:
        print(f"STOPPED: licence {raw!r} is {why}.\n"
              "Read the dataset's terms, then either add it to ALLOWED with a reason\n"
              "or re-run with --force, which records the override in the sidecar.",
              file=sys.stderr)
        return 3

    obj = thin(json.loads(geojson(args.dataset)))
    feats = obj.get("features", [])
    out_dir = pathlib.Path(args.out).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "neighborhoods.geojson"
    target.write_text(json.dumps({"type": "FeatureCollection", "features": feats},
                                 separators=(",", ":"), sort_keys=True))
    size = target.stat().st_size

    props = sorted(feats[0]["properties"].keys()) if feats else []
    print(f"  {len(feats)} features · {size / 1_048_576:.2f} MB", file=sys.stderr)
    print(f"  properties: {', '.join(props)}", file=sys.stderr)

    sidecar = out_dir / "neighborhoods-sources.json"
    sidecar.write_text(json.dumps({
        "note": ("Modern administrative neighbourhood boundaries. One authoritative polygon "
                 "each, city-wide, no disputes -- a frame to hang history on, NOT historical "
                 "place names. Historical extents are contested and assembled from sources; "
                 "labelling one of these polygons with a historical name would assert a "
                 "precision the record does not support."),
        "generated_by": "02-run-plan/acquire-neighborhoods.py",
        "host": HOST,
        "dataset": args.dataset,
        "dataset_name": name,
        "metadata_url": f"{HOST}/api/views/{args.dataset}.json",
        "licence": raw,
        "licence_verdict": verdict,
        "licence_reason": why,
        "licence_forced": bool(args.force and verdict == "unknown"),
        "attribution": attribution,
        "attribution_required": verdict == "allow" and "attribution" in why,
        "retrieved_utc": _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "file": target.name,
        "features": len(feats),
        "bytes": size,
        "sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
        "properties": props,
        "crs": "WGS84 (EPSG:4326) as served",
        "precision": PRECISION,
        "marker": "FETCHED",
    }, indent=2, sort_keys=True) + "\n")
    print(f"wrote {sidecar}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
