#!/usr/bin/env python3
"""Acquire San Francisco neighbourhood boundaries from DataSF, licence first.

    uv run --no-project python acquire-neighborhoods.py --licence     # check only
    uv run --no-project python acquire-neighborhoods.py --dry-run
    uv run --no-project python acquire-neighborhoods.py               # fetch + write

Run where the network is open -- lobster, not a session container, whose egress
does not reach data.sfgov.org.

On lobster, refresh with `git fetch && git reset --hard origin/<branch>`, never
`git pull`. The working branch is restarted from main after each squash-merge
and force-pushed, so its history is rewritten regularly; pull correctly refuses
to fast-forward across that and leaves the checkout diverged. Nothing originates
on lobster that is not pushed immediately, so a reset loses nothing.

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
import collections
import datetime as _dt
import hashlib
import json
import pathlib
import sys
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent / "04-normalized" / "geo"

HOST = "https://data.sfgov.org"

# FETCHED 2026-08-27, and the correction is worth keeping.
#
# This script first used p5b7-5n3h, which IS named "Analysis Neighborhoods" and
# DOES report count(*) = 41 -- the right name, the right count, and no data.
# /resource returned the single row `[{}]`, and the geospatial export returned a
# 53-byte FeatureCollection with an empty feature list. Both endpoints answered
# 200. Nothing announced itself as broken.
#
# p5b7-5n3h is not a dataset. Its displayType is `visualization_canvas_map` and
# its `columns` array is empty: it is a saved map VIEW, which is what the
# dataset description means by "as of November 2023 this map has been updated to
# use a new format". The polygons live in the view's `modifyingViewUid`, below,
# where the columns are `nhood` and `the_geom` (MultiPolygon).
#
# The lesson is the one in HANDOFF.md: a plausible name and a correct row count
# are not evidence that you fetched anything. --dataset overrides this.
DATASET = "j2bu-swwd"
WRAPPER_VIEW = "p5b7-5n3h"   # the canvas map that fronts it; kept so the id is greppable

PRECISION = 6

# Socrata pages at 1000 by default. This is far above any plausible neighbourhood
# count, and the run reports the feature count so a silent truncation would show.
ROW_LIMIT = 5000

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
        f"{HOST}/resource/{dataset}.geojson?$limit={ROW_LIMIT}",
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
            print(f"  (no luck with {u.split('?')[0]}: {exc})", file=sys.stderr)
    raise SystemExit(f"no GeoJSON endpoint answered.\n  last error: {last}")


def thin(obj: dict):
    """Round coordinates, and separate the features that have a shape from those
    that do not.

    Socrata's /resource endpoint emits a feature per ROW, and a row with no
    shape becomes a feature whose geometry is null. Those are not drawable and
    must not be written, but the count is worth reporting rather than swallowing:
    a neighbourhood set where some entries have no polygon is telling you
    something about the dataset.

    GeometryCollection has no top-level "coordinates" either, so it is reported
    the same way instead of crashing.
    """
    def r(x):
        if isinstance(x, list):
            return [r(i) for i in x]
        if isinstance(x, float):
            return round(x, PRECISION)
        return x

    kept, dropped, kinds = [], [], collections.Counter()
    for f in obj.get("features", []):
        g = f.get("geometry")
        kinds[(g or {}).get("type") or "null"] += 1
        if not g or "coordinates" not in g:
            dropped.append(f)
            continue
        g["coordinates"] = r(g["coordinates"])
        kept.append(f)
    return kept, dropped, kinds


def label_of(props: dict) -> str:
    """Best guess at the human name of a row, for reporting only."""
    for k in ("nhood", "name", "neighborhood", "neighbourhood", "analysis_neighborhood"):
        if props.get(k):
            return str(props[k])
    return "(unnamed)"



def probe(dataset: str) -> int:
    """Show what the endpoints actually return, so a wrong guess costs one run.

    Written because the first real fetch produced 41 rows with null geometry and
    no recognisable name column -- the dataset's own description warns it changed
    format in November 2023 -- and this container cannot reach data.sfgov.org to
    look. Guessing across several round trips is worse than one that reports.

    It paid immediately: section 1 printed no columns at all, which is what an
    empty row object looks like, and that is what identified p5b7-5n3h as a
    visualization view rather than a dataset. See the note on DATASET.
    """
    print("\n--- 1. /resource/<id>.json, one row: the columns as they really are")
    try:
        row = json.loads(get(f"{HOST}/resource/{dataset}.json?$limit=1"))
        if not row:
            print("   (no rows)")
        else:
            for k, v in sorted(row[0].items()):
                s = json.dumps(v) if not isinstance(v, str) else v
                s = s.replace("\n", " ")
                looks = ""
                if isinstance(v, dict) and "coordinates" in v: looks = "   <-- GEOMETRY (object)"
                elif isinstance(v, str) and v.lstrip()[:1] in "{[" and "coord" in v.lower():
                    looks = "   <-- GEOMETRY (encoded as text)"
                elif isinstance(v, str) and v.upper().startswith(("MULTIPOLYGON", "POLYGON")):
                    looks = "   <-- GEOMETRY (WKT)"
                print(f"   {k:28} {s[:88]}{'…' if len(s) > 88 else ''}{looks}")
    except Exception as exc:                                  # noqa: BLE001
        print(f"   failed: {exc}")

    print("\n--- 2. /api/geospatial/<id>, first 300 bytes verbatim")
    try:
        raw = get(f"{HOST}/api/geospatial/{dataset}?method=export&format=GeoJSON")
        print("   " + repr(raw[:300].decode("utf-8", "replace")))
    except Exception as exc:                                  # noqa: BLE001
        print(f"   failed: {exc}")

    print("\n--- 3. row count")
    try:
        n = json.loads(get(f"{HOST}/resource/{dataset}.json?$select=count(*)"))
        print(f"   {n}")
    except Exception as exc:                                  # noqa: BLE001
        print(f"   failed: {exc}")
    print("\nSend this output back. Nothing was written.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--dataset", default=DATASET, help=f"Socrata dataset id (default {DATASET})")
    ap.add_argument("--licence", action="store_true", help="report the terms and exit, write nothing")
    ap.add_argument("--probe", action="store_true",
                    help="show what each endpoint really returns, write nothing")
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
    if args.probe:
        return probe(args.dataset)
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

    raw_obj = json.loads(geojson(args.dataset))
    feats, dropped, kinds = thin(raw_obj)
    print(f"  geometry types: "
          + ", ".join(f"{k} x{n}" for k, n in kinds.most_common()), file=sys.stderr)
    if dropped:
        names = ", ".join(sorted(label_of(f.get("properties") or {}) for f in dropped)[:8])
        print(f"  ! {len(dropped)} feature(s) have no drawable geometry and were not written: "
              f"{names}", file=sys.stderr)
    if not feats:
        raise SystemExit("no features with geometry; nothing written")
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
        "wrapper_view": WRAPPER_VIEW,
        "wrapper_view_note": (
            f"{WRAPPER_VIEW} is DataSF's saved canvas map of this dataset. It carries the same "
            "name and reports the same row count, but serves no columns and an empty feature "
            "list. It is not the source of this file."),
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
        "features_without_geometry": len(dropped),
        "geometry_types": dict(kinds),
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
