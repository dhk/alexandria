#!/usr/bin/env python3
"""Acquire Overture Maps geometry for the downtown/SoMa pilot, clipped and stamped.

Run this where the network is open — lobster, not a session container, whose
egress allowlist reaches S3 but little else. It writes derived GeoJSON plus a
provenance sidecar into 04-normalized/geo/, which is what a viewer inlines.

The point is not the download. It is that the output carries where it came
from, when, under what licence, and a checksum — so a reader can check it the
same way they can check a quoted page.

    uv run --no-project --with duckdb python acquire-geo.py --list-releases
    uv run --no-project --with duckdb python acquire-geo.py --dry-run
    uv run --no-project --with duckdb python acquire-geo.py
"""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import pathlib
import sys
import urllib.request
import xml.etree.ElementTree as ET

BUCKET = "overturemaps-us-west-2"
S3_HTTPS = f"https://{BUCKET}.s3.amazonaws.com"

# Bounding boxes are hand-chosen and approximate. They exist to bound a
# download and assert no extent — never cite one as a boundary.
#
# "city" covers the peninsula plus Treasure Island, which is where the street
# grid and the place names are. It deliberately excludes the Farallon Islands,
# which are legally part of the City and County of San Francisco and 27 miles
# out to sea; including them would stretch the box across mostly empty ocean
# for no gain.
PRESETS = {
    "city": {
        "bbox": {"west": -122.5250, "south": 37.7000, "east": -122.3550, "north": 37.8400},
        # City-wide with every residential street is far more geometry than a
        # single page should carry, so the default keeps the through-network.
        "road_classes": ["motorway", "trunk", "primary", "secondary", "tertiary"],
    },
    "soma": {
        "bbox": {"west": -122.4100, "south": 37.7720, "east": -122.3860, "north": 37.7970},
        # The pilot is small enough to take the full local grid, which is what
        # the place-name boundaries are actually described in terms of.
        "road_classes": ["motorway", "trunk", "primary", "secondary", "tertiary",
                         "residential", "unclassified", "living_street"],
    },
}

# Overture themes carry different licences per theme; transportation and
# divisions derive from OpenStreetMap and are ODbL, which obliges attribution
# and share-alike on anything published from them. Recorded per layer so the
# obligation travels with the data instead of living in someone's memory.
LAYERS = {
    "transportation": {
        "path": "theme=transportation/type=segment",
        "licence": "ODbL 1.0 (derived from OpenStreetMap)",
        "attribution": "© OpenStreetMap contributors, via Overture Maps Foundation",
        "columns": "id, names.primary AS name, class, subtype",
        "where": "class IS NOT NULL AND names.primary IS NOT NULL",
    },
    "divisions": {
        "path": "theme=divisions/type=division_area",
        "licence": "ODbL 1.0 (derived from OpenStreetMap)",
        "attribution": "© OpenStreetMap contributors, via Overture Maps Foundation",
        "columns": "id, names.primary AS name, subtype, class",
        "where": "names.primary IS NOT NULL",
    },
}


def latest_release() -> str:
    """Newest release prefix in the public bucket, read from the listing."""
    url = f"{S3_HTTPS}/?list-type=2&prefix=release/&delimiter=/&max-keys=1000"
    with urllib.request.urlopen(url, timeout=60) as r:
        root = ET.fromstring(r.read())
    ns = {"s3": "http://s3.amazonaws.com/doc/2006-03-01/"}
    prefixes = [p.text for p in root.findall(".//s3:CommonPrefixes/s3:Prefix", ns) if p.text]
    releases = sorted(p.split("/")[1] for p in prefixes if p.count("/") == 2)
    if not releases:
        raise SystemExit("no releases found in the bucket listing")
    return releases[-1]


def sql_for(layer: str, release: str, out_path: pathlib.Path, bbox: dict, road_classes: list[str]) -> str:
    spec = LAYERS[layer]
    src = f"s3://{BUCKET}/release/{release}/{spec['path']}/*"
    extra = ""
    if layer == "transportation" and road_classes:
        allowed = ", ".join(f"'{c}'" for c in road_classes)
        extra = f"\n    AND class IN ({allowed})"
    return f"""
INSTALL httpfs; LOAD httpfs;
INSTALL spatial; LOAD spatial;
SET s3_region='us-west-2';
COPY (
  SELECT {spec['columns']},
         ST_GeomFromWKB(geometry) AS geometry
  FROM read_parquet('{src}', hive_partitioning=1)
  WHERE bbox.xmin > {bbox['west']} AND bbox.xmax < {bbox['east']}
    AND bbox.ymin > {bbox['south']} AND bbox.ymax < {bbox['north']}
    AND {spec['where']}{extra}
) TO '{out_path}' (FORMAT GDAL, DRIVER 'GeoJSON', LAYER_CREATION_OPTIONS 'COORDINATE_PRECISION=6');
""".strip()


def thin(path: pathlib.Path) -> int:
    """Drop nulls and trim to 6dp (~0.1 m). Returns the feature count."""
    doc = json.loads(path.read_text())
    feats = doc.get("features", [])

    def rd(x):
        if isinstance(x, list):
            return [rd(i) for i in x]
        return round(x, 6) if isinstance(x, float) else x

    for f in feats:
        f.pop("bbox", None)
        f["properties"] = {k: v for k, v in (f.get("properties") or {}).items() if v not in (None, "")}
        if f.get("geometry"):
            f["geometry"]["coordinates"] = rd(f["geometry"]["coordinates"])
    doc["features"] = feats
    path.write_text(json.dumps(doc, separators=(",", ":"), sort_keys=True))
    return len(feats)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--release", help="Overture release, e.g. 2026-08-19.0 (default: newest)")
    ap.add_argument("--extent", default="city", choices=sorted(PRESETS),
                    help="city = all of San Francisco (default); soma = the downtown pilot")
    ap.add_argument("--road-classes", help="comma-separated override for the transportation filter")
    ap.add_argument("--layers", default=",".join(LAYERS), help="comma-separated: " + ", ".join(LAYERS))
    ap.add_argument("--out", default=str(pathlib.Path(__file__).resolve().parent.parent / "04-normalized" / "geo"),
                    help="output directory (default: this investigation's 04-normalized/geo)")
    ap.add_argument("--dry-run", action="store_true", help="print the SQL and exit; fetch nothing")
    ap.add_argument("--list-releases", action="store_true", help="print the newest release and exit")
    args = ap.parse_args()

    if args.list_releases:
        print(latest_release())
        return 0

    preset = PRESETS[args.extent]
    bbox = preset["bbox"]
    road_classes = ([c.strip() for c in args.road_classes.split(",") if c.strip()]
                    if args.road_classes else preset["road_classes"])
    release = args.release or latest_release()
    out_dir = pathlib.Path(args.out).resolve()
    layers = [l.strip() for l in args.layers.split(",") if l.strip()]
    unknown = [l for l in layers if l not in LAYERS]
    if unknown:
        raise SystemExit(f"unknown layer(s): {', '.join(unknown)}")

    if args.dry_run:
        for layer in layers:
            print(f"-- {layer} ({args.extent})\n"
                  f"{sql_for(layer, release, out_dir / f'{args.extent}-{layer}.geojson', bbox, road_classes)}\n")
        return 0

    import duckdb  # imported late so --dry-run and --list-releases need no extension download

    out_dir.mkdir(parents=True, exist_ok=True)
    stamped = _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    records = []
    con = duckdb.connect()
    for layer in layers:
        target = out_dir / f"{args.extent}-{layer}.geojson"
        print(f"… {layer} ({args.extent}) from release {release}", file=sys.stderr)
        con.execute(sql_for(layer, release, target, bbox, road_classes))
        count = thin(target)
        digest = hashlib.sha256(target.read_bytes()).hexdigest()
        records.append({
            "layer": layer,
            "file": target.name,
            "features": count,
            "bytes": target.stat().st_size,
            "sha256": digest,
            "source": f"s3://{BUCKET}/release/{release}/{LAYERS[layer]['path']}/",
            "source_https": f"{S3_HTTPS}/release/{release}/{LAYERS[layer]['path']}/",
            "release": release,
            "retrieved_utc": stamped,
            "licence": LAYERS[layer]["licence"],
            "attribution": LAYERS[layer]["attribution"],
            "marker": "FETCHED",
            "extent": args.extent,
            "road_classes": road_classes if layer == "transportation" else None,
        })
        mb = target.stat().st_size / 1_048_576
        print(f"  {count} features · {mb:.1f} MB · {digest[:12]}…", file=sys.stderr)
        if mb > 12:
            print(f"  ! {target.name} is {mb:.1f} MB. A published artifact caps at 16 MB total, "
                  f"so this needs a tighter class filter or a coarser extent before it is inlined.",
                  file=sys.stderr)

    sidecar = out_dir / "sources.json"
    sidecar_path_note = out_dir / "sources.json"
    existing = {}
    if sidecar_path_note.exists():
        try:
            existing = json.loads(sidecar_path_note.read_text())
        except json.JSONDecodeError:
            existing = {}
    kept = [r for r in existing.get("layers", [])
            if (r.get("extent"), r.get("layer")) not in {(r2["extent"], r2["layer"]) for r2 in records}]
    records = sorted(kept + records, key=lambda r: (r.get("extent", ""), r["layer"]))
    sidecar.write_text(json.dumps({
        "note": (
            "Derived geometry, clipped to a hand-chosen bounding box and thinned to 6 decimal "
            "places. The bbox bounds the download and asserts no extent. Licence obligations "
            "below travel with any publication of this data."
        ),
        "bbox_by_extent": {k: v["bbox"] for k, v in PRESETS.items()},
        "duckdb": duckdb.__version__,
        "generated_by": "02-run-plan/acquire-geo.py",
        "layers": records,
    }, indent=2, sort_keys=True) + "\n")
    print(f"wrote {sidecar}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
