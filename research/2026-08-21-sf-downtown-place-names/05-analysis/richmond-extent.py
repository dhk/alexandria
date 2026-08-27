#!/usr/bin/env python3
"""Measure the Richmond/Seacliff study area from committed geometry.

    python3 richmond-extent.py            # report
    python3 richmond-extent.py --json     # machine-readable

Stdlib only, no network. Inputs are committed and checksummed:
`04-normalized/geo/neighborhoods.geojson` (DataSF, PDDL, FETCHED) and
`04-normalized/geo/city-roads.geojson` (TIGER 2025, public domain, FETCHED).

WHY THIS EXISTS

The handoff's standing warning is that street names are not unique city-wide --
there is a second `1st St` on Treasure Island -- so every name lookup must be
bounded by a box. This measures what that box actually costs in the northern
part of the city, where the neighbourhoods interleave with the Presidio, Lincoln
Park and Golden Gate Park.

A bounding box is a rectangle and a neighbourhood is not. The gap between them
is not a rounding error here: it is most of the study area.
"""
from __future__ import annotations

import argparse
import json
import math
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
GEO = HERE.parent / "04-normalized" / "geo"

# The neighbourhood set this study is about. Seacliff and Lincoln Park are
# included because they are the western end of the same survey and the same
# shoreline; the Presidio and Golden Gate Park deliberately are NOT -- they are
# federal and municipal reservations that the Outside Lands survey went around
# rather than through.
STUDY = ["Seacliff", "Outer Richmond", "Inner Richmond", "Lincoln Park"]

# The Richmond & Sunset grid, from 05-analysis/grid-classification.md: a
# length-weighted peak at 3.5 degrees over 635.8 km, 31.6% of the city's
# centreline. A grid is two orthogonal families, so a bearing is tested against
# both theta and theta+90 -- testing only theta throws every cross street into
# "ungridded" and still draws a plausible map.
GRID_BEARING = 3.5
GRID_TOL = 2.5
MIN_SEGMENT_M = 8.0


def load(name: str) -> dict:
    return json.loads((GEO / name).read_text())


def rings(geom: dict) -> list[list[tuple[float, float]]]:
    if geom["type"] == "Polygon":
        return [[(x, y) for x, y in r] for r in geom["coordinates"]]
    out = []
    for poly in geom["coordinates"]:
        for r in poly:
            out.append([(x, y) for x, y in r])
    return out


def bbox_of(points) -> tuple[float, float, float, float]:
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    return min(xs), min(ys), max(xs), max(ys)


def in_ring(x: float, y: float, ring) -> bool:
    """Ray casting. Odd crossings means inside."""
    inside = False
    n = len(ring)
    for i in range(n):
        x0, y0 = ring[i]
        x1, y1 = ring[(i + 1) % n]
        if (y0 > y) != (y1 > y):
            xint = (x1 - x0) * (y - y0) / (y1 - y0) + x0
            if x < xint:
                inside = not inside
    return inside


class Area:
    """A neighbourhood, with a bbox pre-filter so point tests stay cheap."""

    def __init__(self, name: str, geom: dict):
        self.name = name
        self.rings = rings(geom)
        pts = [p for r in self.rings for p in r]
        self.bbox = bbox_of(pts)

    def contains(self, x: float, y: float) -> bool:
        x0, y0, x1, y1 = self.bbox
        if not (x0 <= x <= x1 and y0 <= y <= y1):
            return False
        # Even-odd across every ring handles holes without tracking winding.
        return sum(1 for r in self.rings if in_ring(x, y, r)) % 2 == 1


def coords_of(geom: dict) -> list[tuple[float, float]]:
    if geom["type"] == "LineString":
        return [(x, y) for x, y in geom["coordinates"]]
    out = []
    for part in geom["coordinates"]:
        out.extend((x, y) for x, y in part)
    return out


def segments(geom: dict):
    parts = ([geom["coordinates"]] if geom["type"] == "LineString"
             else geom["coordinates"])
    for part in parts:
        for i in range(len(part) - 1):
            yield tuple(part[i][:2]), tuple(part[i + 1][:2])


def seg_metres(a, b) -> float:
    lat = math.radians((a[1] + b[1]) / 2)
    dx = (b[0] - a[0]) * 111_320 * math.cos(lat)
    dy = (b[1] - a[1]) * 110_540
    return math.hypot(dx, dy)


def bearing_deg(a, b) -> float:
    """Bearing folded to [0,90) -- a grid has no direction, only an angle.

    Measured from EAST (atan2(dy, dx)), which is the convention
    grid-classification.md uses. Measuring from north instead returns the
    complement, 90 - theta, and the mistake is nearly invisible: the city-wide
    histogram still shows seven sharp peaks, they are just all mirrored. It
    survived a first pass here because the South of Market grid sits at 45
    degrees, which is its own complement, so the one grid a reader would check
    by eye agrees under either convention. The Richmond, at 3.5, came out as
    86.5 and scored 2.1% against its own grid.
    """
    lat = math.radians((a[1] + b[1]) / 2)
    dx = (b[0] - a[0]) * 111_320 * math.cos(lat)
    dy = (b[1] - a[1]) * 110_540
    ang = math.degrees(math.atan2(dy, dx)) % 180.0
    return ang - 90.0 if ang >= 90.0 else ang


def on_grid(theta: float) -> bool:
    """Test both families. One family is not a grid."""
    for target in (GRID_BEARING, GRID_BEARING + 90.0):
        t = target % 90.0
        d = abs(theta - t)
        d = min(d, 90.0 - d)
        if d <= GRID_TOL:
            return True
    return False


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    nb = load("neighborhoods.geojson")
    roads = load("city-roads.geojson")
    areas = {f["properties"]["nhood"]: Area(f["properties"]["nhood"], f["geometry"])
             for f in nb["features"]}
    missing = [n for n in STUDY if n not in areas]
    if missing:
        raise SystemExit(f"not in the neighbourhood set: {missing}")

    study = [areas[n] for n in STUDY]
    x0 = min(a.bbox[0] for a in study); y0 = min(a.bbox[1] for a in study)
    x1 = max(a.bbox[2] for a in study); y1 = max(a.bbox[3] for a in study)

    box_hits, poly_hits = [], []
    per_area: dict[str, set] = {n: set() for n in STUDY}
    per_len: dict[str, float] = {n: 0.0 for n in STUDY}
    per_grid: dict[str, float] = {n: 0.0 for n in STUDY}
    length_in, length_on_grid = 0.0, 0.0

    for f in roads["features"]:
        name = (f["properties"].get("name") or "").strip()
        if not name:
            continue
        pts = coords_of(f["geometry"])
        if not pts:
            continue
        if any(x0 <= x <= x1 and y0 <= y <= y1 for x, y in pts):
            box_hits.append(name)
        hit_area = None
        for a in study:
            if sum(1 for x, y in pts if a.contains(x, y)) * 2 >= len(pts):
                hit_area = a.name
                break
        if hit_area:
            poly_hits.append(name)
            per_area[hit_area].add(name)
            for p, q in segments(f["geometry"]):
                m = seg_metres(p, q)
                if m < MIN_SEGMENT_M:
                    continue
                length_in += m
                per_len[hit_area] += m
                if on_grid(bearing_deg(p, q)):
                    length_on_grid += m
                    per_grid[hit_area] += m

    box_names, poly_names = set(box_hits), set(poly_hits)
    extra = box_names - poly_names
    # Names that exist both inside the study area and elsewhere in the city.
    elsewhere = set()
    for f in roads["features"]:
        name = (f["properties"].get("name") or "").strip()
        if name not in poly_names:
            continue
        pts = coords_of(f["geometry"])
        if pts and not any(a.contains(x, y) for x, y in pts for a in study):
            elsewhere.add(name)

    result = {
        "study_neighbourhoods": STUDY,
        "bbox": [round(x0, 6), round(y0, 6), round(x1, 6), round(y1, 6)],
        "bbox_km": [round((x1 - x0) * 88.6, 2), round((y1 - y0) * 111.0, 2)],
        "named_streets_in_polygons": len(poly_names),
        "named_streets_in_bbox": len(box_names),
        "bbox_over_capture": len(extra),
        "bbox_over_capture_share": round(len(extra) / len(box_names), 4) if box_names else 0,
        "per_neighbourhood": {
            k: {"named_streets": len(v),
                "centreline_km": round(per_len[k] / 1000, 2),
                "on_grid_km": round(per_grid[k] / 1000, 2),
                "on_grid_share": round(per_grid[k] / per_len[k], 4) if per_len[k] else 0}
            for k, v in per_area.items()},
        "names_also_found_outside": sorted(elsewhere),
        "centreline_km_in_study": round(length_in / 1000, 2),
        "on_grid_km": round(length_on_grid / 1000, 2),
        "on_grid_share": round(length_on_grid / length_in, 4) if length_in else 0,
        "grid_tested": {"bearing": GRID_BEARING, "tolerance": GRID_TOL,
                        "families": [GRID_BEARING, GRID_BEARING + 90]},
        "marker": "FETCHED (geometry) + derived measurement",
    }
    if args.json:
        print(json.dumps(result, indent=2))
        return 0

    print("Richmond / Seacliff study area\n")
    print(f"  neighbourhoods      {', '.join(STUDY)}")
    print(f"  bounding box        lon {x0:.5f}..{x1:.5f}  lat {y0:.5f}..{y1:.5f}")
    print(f"                      ~{result['bbox_km'][0]} km x {result['bbox_km'][1]} km")
    print(f"\n  named streets inside the polygons   {len(poly_names):>5}")
    print(f"  named streets inside the bbox       {len(box_names):>5}")
    print(f"  pulled in by the box alone          {len(extra):>5}"
          f"   ({result['bbox_over_capture_share']:.0%} of the box's streets)")
    print("\n  per neighbourhood:")
    print(f"    {'':<18}{'streets':>8}{'km':>9}{'on grid':>10}")
    for n in STUDY:
        share = per_grid[n] / per_len[n] if per_len[n] else 0
        print(f"    {n:<18}{len(per_area[n]):>8}{per_len[n]/1000:>9.2f}{share:>9.1%}")
    print(f"\n  centreline in the study area        {result['centreline_km_in_study']:>8.2f} km")
    print(f"  on the Richmond & Sunset grid       {result['on_grid_km']:>8.2f} km"
          f"   ({result['on_grid_share']:.1%})")
    print(f"    tested against {GRID_BEARING} and {GRID_BEARING + 90}, "
          f"tolerance {GRID_TOL}")
    print(f"\n  street names that also occur outside the study area: {len(elsewhere)}")
    for n in sorted(elsewhere)[:12]:
        print(f"    {n}")
    if len(elsewhere) > 12:
        print(f"    … and {len(elsewhere) - 12} more")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
