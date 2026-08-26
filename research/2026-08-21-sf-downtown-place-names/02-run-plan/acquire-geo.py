#!/usr/bin/env python3
"""Acquire modern street and water geometry for San Francisco, stamped with provenance.

Default source is Census TIGER/Line, which is a work of the U.S. federal
government and therefore public domain (17 U.S.C. §105): no licence, no
attribution obligation, no share-alike. That keeps this repository's MIT
licence accurate across every file in it.

Overture Maps is available behind --source overture and is BETTER data, but its
transportation and divisions themes derive from OpenStreetMap and carry ODbL.
ODbL's share-alike attaches to a Derivative Database, and a committed .geojson
extract is exactly that — so using it would make this an MIT repository
containing ODbL files, and would arguably put ODbL on the place-name geometry
derived against it. Hence the default.

Run where the network is open — lobster, not a session container, whose egress
reaches S3 and GitHub and little else.

    uv run --no-project --with pyshp python acquire-geo.py --list-years
    uv run --no-project --with pyshp python acquire-geo.py --dry-run
    uv run --no-project --with pyshp python acquire-geo.py               # all of San Francisco
    uv run --no-project --with pyshp python acquire-geo.py --extent soma
"""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import io
import json
import pathlib
import re
import sys
import urllib.request
import zipfile

# San Francisco is FIPS state 06, county 075. TIGER ships one file per county,
# so the download is already city-scoped and the bbox only trims.
STATE_COUNTY = "06075"
TIGER_ROOT = "https://www2.census.gov/geo/tiger"

# Bounding boxes are hand-chosen and approximate. They exist to bound and trim,
# and assert no extent — never cite one as a boundary. "city" covers the
# peninsula plus Treasure Island and deliberately omits the Farallon Islands:
# legally part of the City and County, 27 miles out, nothing but ocean between.
PRESETS = {
    # No class filter. --report on the real file settled it: of 4,090 segments
    # in the city box, every unnamed one is noise — 237 ramps and 10
    # census-internal features, none of them named — while S1400 "local street"
    # is 3,715 segments of which 3,593 carry a name. Requiring a name drops
    # 412 features and loses nothing anyone could point at, which is the right
    # rule for an atlas about street names. Class tiers were solving a size
    # problem that does not exist: 3,678 named segments is a couple of MB.
    "city": {
        "bbox": {"west": -122.5250, "south": 37.7000, "east": -122.3550, "north": 37.8400},
        "mtfcc": [],
    },
    "soma": {
        "bbox": {"west": -122.4100, "south": 37.7720, "east": -122.3860, "north": 37.7970},
        "mtfcc": [],
    },
}

MTFCC_LABEL = {
    "S1100": "primary road", "S1200": "secondary road", "S1400": "local street",
    "S1500": "vehicular trail", "S1630": "ramp", "S1640": "service drive",
    "S1730": "alley", "S1740": "private road", "S1780": "parking lot road",
}

TIGER_LAYERS = {
    "roads": {"kind": "ROADS", "file": "roads", "geom": "LineString"},
    "water": {"kind": "AREAWATER", "file": "areawater", "geom": "Polygon"},
}

PUBLIC_DOMAIN = "Public domain — work of the U.S. Census Bureau (17 U.S.C. §105)"


def list_years() -> list[str]:
    with urllib.request.urlopen(TIGER_ROOT + "/", timeout=60) as r:
        html = r.read().decode("utf-8", "replace")
    return sorted({m for m in re.findall(r"TIGER(\d{4})", html)})


def zip_url(year: str, layer: str) -> str:
    spec = TIGER_LAYERS[layer]
    return f"{TIGER_ROOT}/TIGER{year}/{spec['kind']}/tl_{year}_{STATE_COUNTY}_{spec['file']}.zip"


def fetch(url: str) -> bytes:
    with urllib.request.urlopen(url, timeout=600) as r:
        return r.read()


def overlaps(shp_bbox, box) -> bool:
    xmin, ymin, xmax, ymax = shp_bbox
    return not (xmax < box["west"] or xmin > box["east"] or ymax < box["south"] or ymin > box["north"])


def to_geojson(payload: bytes, layer: str, box: dict, mtfcc: list[str], named_only: bool = True) -> list[dict]:
    """Read the shapefile out of the zip in memory and emit filtered features."""
    import shapefile  # pyshp — pure python, no binary dependency

    feats = []
    with zipfile.ZipFile(io.BytesIO(payload)) as z:
        stem = next(n[:-4] for n in z.namelist() if n.endswith(".shp"))
        parts = {ext: io.BytesIO(z.read(f"{stem}.{ext}")) for ext in ("shp", "dbf", "shx")}
        rdr = shapefile.Reader(shp=parts["shp"], dbf=parts["dbf"], shx=parts["shx"])
        for sr in rdr.iterShapeRecords():
            shp = sr.shape
            if not getattr(shp, "points", None) or not overlaps(shp.bbox, box):
                continue
            rec = sr.record.as_dict()
            code = rec.get("MTFCC")
            if layer == "roads":
                if mtfcc and code not in mtfcc:
                    continue
                if named_only and not rec.get("FULLNAME"):
                    continue
            geo = shp.__geo_interface__
            geo["coordinates"] = _round(geo["coordinates"])
            props = {"name": rec.get("FULLNAME") or None}
            if layer == "roads":
                props["mtfcc"] = code
                props["kind"] = MTFCC_LABEL.get(code, code)
            else:
                props["kind"] = rec.get("MTFCC")
            feats.append({"type": "Feature",
                          "properties": {k: v for k, v in props.items() if v},
                          "geometry": geo})
    return feats


PRECISION = 6
def _round(x):
    if isinstance(x, (list, tuple)):
        return [_round(i) for i in x]
    return round(x, PRECISION) if isinstance(x, float) else x


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", default="tiger", choices=("tiger", "overture"),
                    help="tiger = public domain (default); overture = richer but ODbL")
    ap.add_argument("--year", help="TIGER vintage, e.g. 2025 (default: newest published)")
    ap.add_argument("--extent", default="city", choices=sorted(PRESETS),
                    help="city = all of San Francisco (default); soma = the downtown pilot")
    ap.add_argument("--layers", default="roads,water", help="comma-separated: roads, water")
    ap.add_argument("--mtfcc", help="comma-separated MTFCC filter; default is every class, since the name test does the work")
    ap.add_argument("--include-unnamed", action="store_true",
                    help="keep unnamed road segments (ramps, census artefacts). Off by default: on the real file every unnamed segment was noise")
    ap.add_argument("--out", default=str(pathlib.Path(__file__).resolve().parent.parent / "04-normalized" / "geo"),
                    help="output directory (default: this investigation's 04-normalized/geo)")
    ap.add_argument("--precision", type=int, default=5,
                    help="coordinate decimal places (default 5, about a metre)")
    ap.add_argument("--report", action="store_true",
                    help="fetch and print the MTFCC class histogram for the extent, write nothing")
    ap.add_argument("--dry-run", action="store_true", help="print what would be fetched; fetch nothing")
    ap.add_argument("--list-years", action="store_true", help="print available TIGER vintages and exit")
    args = ap.parse_args()

    if args.source == "overture":
        print("! Overture's transportation and divisions themes are ODbL. Share-alike attaches to a\n"
              "! committed extract, which would put ODbL files in an MIT repository. See acquire-geo.md.\n"
              "! Not implemented here on purpose: choose it deliberately, not by default.", file=sys.stderr)
        return 2

    if args.list_years:
        print(" ".join(list_years()))
        return 0

    preset = PRESETS[args.extent]
    box = preset["bbox"]
    mtfcc = ([c.strip().upper() for c in args.mtfcc.split(",") if c.strip()]
             if args.mtfcc else preset["mtfcc"])
    layers = [l.strip() for l in args.layers.split(",") if l.strip()]
    unknown = [l for l in layers if l not in TIGER_LAYERS]
    if unknown:
        raise SystemExit(f"unknown layer(s): {', '.join(unknown)}")

    global PRECISION
    PRECISION = args.precision

    if args.report:
        import shapefile, collections
        year = args.year or list_years()[-1]
        payload = fetch(zip_url(year, "roads"))
        counts, named = collections.Counter(), collections.Counter()
        with zipfile.ZipFile(io.BytesIO(payload)) as z:
            stem = next(n[:-4] for n in z.namelist() if n.endswith(".shp"))
            parts = {e: io.BytesIO(z.read(f"{stem}.{e}")) for e in ("shp", "dbf", "shx")}
            rdr = shapefile.Reader(shp=parts["shp"], dbf=parts["dbf"], shx=parts["shx"])
            for sr in rdr.iterShapeRecords():
                if not getattr(sr.shape, "points", None) or not overlaps(sr.shape.bbox, box):
                    continue
                rec = sr.record.as_dict(); c = rec.get("MTFCC")
                counts[c] += 1
                if rec.get("FULLNAME"):
                    named[c] += 1
        print(f"TIGER{year}, extent {args.extent}: {sum(counts.values())} segments in the box\n")
        print(f"{'MTFCC':8} {'total':>7} {'named':>7}  meaning")
        for c, n in counts.most_common():
            print(f"{c:8} {n:7} {named[c]:7}  {MTFCC_LABEL.get(c, '?')}")
        return 0

    year = args.year
    if not year and not args.dry_run:
        year = list_years()[-1]
    year = year or "YYYY"

    if args.dry_run:
        for layer in layers:
            print(f"{layer:6} <- {zip_url(year, layer)}")
        print(f"extent {args.extent} {box}")
        print(f"road classes {mtfcc or 'all'}; named segments only: {not args.include_unnamed}")
        print(f"out    {pathlib.Path(args.out).resolve()}")
        return 0

    out_dir = pathlib.Path(args.out).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    stamped = _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    records = []

    for layer in layers:
        url = zip_url(year, layer)
        print(f"… {layer} ({args.extent}) from TIGER{year}", file=sys.stderr)
        payload = fetch(url)
        feats = to_geojson(payload, layer, box, mtfcc, not args.include_unnamed)
        target = out_dir / f"{args.extent}-{layer}.geojson"
        target.write_text(json.dumps(
            {"type": "FeatureCollection", "features": feats}, separators=(",", ":"), sort_keys=True))
        mb = target.stat().st_size / 1_048_576
        records.append({
            "layer": layer, "extent": args.extent, "file": target.name,
            "features": len(feats), "bytes": target.stat().st_size,
            "sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
            "source_zip": url, "source_zip_sha256": hashlib.sha256(payload).hexdigest(),
            "vintage": f"TIGER{year}", "retrieved_utc": stamped,
            "licence": PUBLIC_DOMAIN, "attribution_required": False,
            "crs": "NAD83 (EPSG:4269), used as WGS84 for display; the difference is sub-metre here",
            "mtfcc_filter": (mtfcc or "all classes") if layer == "roads" else None,
            "named_only": (not args.include_unnamed) if layer == "roads" else None,
            "marker": "FETCHED",
        })
        print(f"  {len(feats)} features · {mb:.1f} MB", file=sys.stderr)
        if mb > 12:
            print(f"  ! {target.name} is {mb:.1f} MB. A published artifact caps at 16 MB in total,\n"
                  f"  ! so this needs a tighter class filter before it is inlined.", file=sys.stderr)

    sidecar = out_dir / "sources.json"
    existing = {}
    if sidecar.exists():
        try:
            existing = json.loads(sidecar.read_text())
        except json.JSONDecodeError:
            existing = {}
    fresh = {(r["extent"], r["layer"]) for r in records}
    kept = [r for r in existing.get("layers", []) if (r.get("extent"), r.get("layer")) not in fresh]
    sidecar.write_text(json.dumps({
        "note": ("Derived geometry, clipped to a hand-chosen bounding box and thinned to 6 decimal "
                 "places. The bbox bounds a download and asserts no extent. Source is public domain, "
                 "so this data carries no licence obligation and does not qualify the repository's "
                 "MIT licence."),
        "bbox_by_extent": {k: v["bbox"] for k, v in PRESETS.items()},
        "generated_by": "02-run-plan/acquire-geo.py",
        "layers": sorted(kept + records, key=lambda r: (r.get("extent", ""), r["layer"])),
    }, indent=2, sort_keys=True) + "\n")
    print(f"wrote {sidecar}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
