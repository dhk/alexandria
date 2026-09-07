#!/usr/bin/env python3
"""Measure the Richmond/Seacliff study area from committed geometry.

    python3 richmond-extent.py            # report
    python3 richmond-extent.py --json     # machine-readable
    python3 richmond-extent.py --band     # the whole northern band, two grids

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

# --band widens the study to the whole northern edge of the city, so the two
# largest surveys can be measured against each other rather than one at a time.
# Both peaks are inherited from grid-classification.md; neither is fitted.
# 3.5 +/- 2.5 spans [1.0, 6.0] and 9.5 +/- 2.5 spans [7.0, 12.0]: the windows do
# not overlap, so no segment can be counted twice, and the two shares plus
# "neither" sum to 1.
GRIDS = [
    (3.5, "Richmond & Sunset", "Potter & Humphrey, 18 May 1868"),
    (9.5, "Western Addition", "Van Ness Ordinance, 1855-56"),
]

# West to east along the northern shore, then the hills. This deliberately
# includes the Presidio and Golden Gate Park, which the four-neighbourhood
# study excludes: in the band they are the question rather than a distraction,
# because a reservation the survey went around should score low on both grids.
BAND = [
    "Seacliff",
    "Outer Richmond",
    "Inner Richmond",
    "Lincoln Park",
    "Presidio",
    "Golden Gate Park",
    "Presidio Heights",
    "Lone Mountain/USF",
    "Marina",
    "Pacific Heights",
    "Western Addition",
    "Japantown",
    "Russian Hill",
    "Nob Hill",
    "North Beach",
]


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


def on_grid(theta: float, bearing: float = GRID_BEARING) -> bool:
    """Test both families. One family is not a grid.

    Generalised over `bearing` so the same test can be run against more than one
    survey; the default keeps the single-grid behaviour the four-neighbourhood
    study was written against. `theta` is already folded to [0,90), so both
    families collapse onto the same target -- the loop is kept because dropping
    it is exactly the mistake this project has already shipped once.
    """
    for target in (bearing, bearing + 90.0):
        t = target % 90.0
        d = abs(theta - t)
        d = min(d, 90.0 - d)
        if d <= GRID_TOL:
            return True
    return False


def tally(roads: dict, areas: list, bearings: list[float]):
    """Assign each named street to one area, then measure its segments.

    A street belongs to the first area holding a majority of its vertices, so a
    street straddling a boundary lands wholly on one side. Segment length is
    then split between the grids in `bearings` and a "neither" remainder.
    """
    names: dict[str, set] = {a.name: set() for a in areas}
    length: dict[str, float] = {a.name: 0.0 for a in areas}
    on: dict[str, list[float]] = {a.name: [0.0] * len(bearings) for a in areas}
    hits: list[str] = []
    # Running totals rather than a sum() over the per-area dicts, so the
    # floating-point addition sequence is identical to the pre-band version and
    # the default report's numbers cannot drift by a last-digit rounding.
    total = 0.0
    total_on = [0.0] * len(bearings)
    for f in roads["features"]:
        name = (f["properties"].get("name") or "").strip()
        if not name:
            continue
        pts = coords_of(f["geometry"])
        if not pts:
            continue
        hit = None
        for a in areas:
            if sum(1 for x, y in pts if a.contains(x, y)) * 2 >= len(pts):
                hit = a.name
                break
        if hit is None:
            continue
        hits.append(name)
        names[hit].add(name)
        for p, q in segments(f["geometry"]):
            m = seg_metres(p, q)
            if m < MIN_SEGMENT_M:
                continue
            total += m
            length[hit] += m
            theta = bearing_deg(p, q)
            for i, b in enumerate(bearings):
                if on_grid(theta, b):
                    total_on[i] += m
                    on[hit][i] += m
                    break
    return names, length, on, hits, total, total_on


def load_areas(names: list[str]) -> list:
    nb = load("neighborhoods.geojson")
    areas = {f["properties"]["nhood"]: Area(f["properties"]["nhood"], f["geometry"])
             for f in nb["features"]}
    missing = [n for n in names if n not in areas]
    if missing:
        raise SystemExit(f"not in the neighbourhood set: {missing}")
    return [areas[n] for n in names]


COLUMN_DEG = 0.005  # ~440 m of longitude at this latitude


def longitude_profile(roads: dict, areas: list, bearings: list[float]):
    """Grid shares in north-south columns across the band.

    A per-neighbourhood table cannot say where a boundary falls, because a
    neighbourhood is not a point and a street is not a point either -- averaging
    a street's vertices puts a long east-west boulevard in the middle of nothing.
    This bins the *segments* instead, so each 440 m column is a real place.
    """
    cols: dict[int, list[float]] = {}
    for f in roads["features"]:
        name = (f["properties"].get("name") or "").strip()
        if not name:
            continue
        pts = coords_of(f["geometry"])
        if not pts:
            continue
        if not any(sum(1 for x, y in pts if a.contains(x, y)) * 2 >= len(pts)
                   for a in areas):
            continue
        for p, q in segments(f["geometry"]):
            m = seg_metres(p, q)
            if m < MIN_SEGMENT_M:
                continue
            k = math.floor(((p[0] + q[0]) / 2) / COLUMN_DEG)
            slot = cols.setdefault(k, [0.0] * (len(bearings) + 1))
            theta = bearing_deg(p, q)
            hit = len(bearings)
            for i, b in enumerate(bearings):
                if on_grid(theta, b):
                    hit = i
                    break
            slot[hit] += m
    out = []
    for k in sorted(cols):
        v = cols[k]
        t = sum(v)
        if t < 1000.0:  # under a km of centreline; too little to read anything into
            continue
        out.append({"lon": round(k * COLUMN_DEG, 4), "km": round(t / 1000, 2),
                    "on_1868_share": round(v[0] / t, 4),
                    "on_1855_share": round(v[1] / t, 4),
                    "on_neither_share": round(v[2] / t, 4)})
    return out


def band(as_json: bool) -> int:
    """The northern band, measured against both surveys at once.

    The four-neighbourhood study answers "how much of the Richmond is on its own
    grid". This answers a different question: walking east along the northern
    edge of the city, where does the 1868 Outside Lands survey stop and the
    1855-56 Van Ness Ordinance survey start?
    """
    roads = load("city-roads.geojson")
    areas = load_areas(BAND)
    bearings = [g[0] for g in GRIDS]
    names, length, on, _hits, total, total_on = tally(roads, areas, bearings)
    profile = longitude_profile(roads, areas, bearings)

    rows = []
    for n in BAND:
        L = length[n]
        shares = [(on[n][i] / L if L else 0.0) for i in range(len(bearings))]
        rows.append({
            "neighbourhood": n,
            "named_streets": len(names[n]),
            "centreline_km": round(L / 1000, 2),
            "on_1868_km": round(on[n][0] / 1000, 2),
            "on_1868_share": round(shares[0], 4),
            "on_1855_km": round(on[n][1] / 1000, 2),
            "on_1855_share": round(shares[1], 4),
            "on_neither_share": round(1.0 - shares[0] - shares[1], 4) if L else 0.0,
            "verdict": verdict(shares[0], shares[1]),
        })

    result = {
        "band_neighbourhoods": BAND,
        "grids_tested": [
            {"bearing": b, "name": nm, "survey": s,
             "families": [b, b + 90.0], "tolerance": GRID_TOL}
            for b, nm, s in GRIDS],
        "per_neighbourhood": rows,
        "longitude_profile": profile,
        "longitude_column_deg": COLUMN_DEG,
        "named_streets_in_band": len({s for n in BAND for s in names[n]}),
        "centreline_km_in_band": round(total / 1000, 2),
        "on_1868_km": round(total_on[0] / 1000, 2),
        "on_1868_share": round(total_on[0] / total, 4) if total else 0,
        "on_1855_km": round(total_on[1] / 1000, 2),
        "on_1855_share": round(total_on[1] / total, 4) if total else 0,
        "marker": "FETCHED (geometry) + derived measurement",
    }
    if as_json:
        print(json.dumps(result, indent=2))
        return 0

    print("The northern band: two surveys, measured against each other\n")
    for b, nm, s in GRIDS:
        print(f"  {nm:<18} {b:>5.1f} and {b + 90.0:>5.1f}   {s}")
    print(f"  tolerance {GRID_TOL} degrees, both orthogonal families per grid")
    print(f"\n    {'':<20}{'streets':>8}{'km':>9}{'1868':>9}{'1855-56':>9}"
          f"{'neither':>9}   verdict")
    for r in rows:
        print(f"    {r['neighbourhood']:<20}{r['named_streets']:>8}"
              f"{r['centreline_km']:>9.2f}{r['on_1868_share']:>8.1%}"
              f"{r['on_1855_share']:>9.1%}{r['on_neither_share']:>9.1%}"
              f"   {r['verdict']}")
    n1868 = result["on_1868_share"]
    n1855 = result["on_1855_share"]
    print(f"\n    {'band total':<20}{result['named_streets_in_band']:>8}"
          f"{result['centreline_km_in_band']:>9.2f}{n1868:>8.1%}{n1855:>9.1%}"
          f"{1 - n1868 - n1855:>9.1%}")
    print(f"\n  on the 1868 grid   {result['on_1868_km']:>8.2f} km")
    print(f"  on the 1855-56 grid{result['on_1855_km']:>8.2f} km")
    print("\n  The two windows are [1.0, 6.0] and [7.0, 12.0] degrees: disjoint,")
    print("  so no segment is counted twice and the three shares sum to 100%.")

    print(f"\n  West to east in {COLUMN_DEG} deg columns (~440 m), segments binned")
    print("  by their own midpoint rather than by their street's average:")
    print(f"    {'lon':>10}{'km':>8}{'1868':>8}{'1855-56':>9}{'neither':>9}   lead")
    for c in profile:
        lead = ("1868" if c["on_1868_share"] > c["on_1855_share"] * 1.5 else
                "1855-56" if c["on_1855_share"] > c["on_1868_share"] * 1.5
                else "--")
        print(f"    {c['lon']:>10.3f}{c['km']:>8.2f}{c['on_1868_share']:>7.0%}"
              f"{c['on_1855_share']:>9.0%}{c['on_neither_share']:>9.0%}   {lead}")
    return 0


def verdict(s1868: float, s1855: float) -> str:
    """A label, not a finding -- the numbers beside it are the finding."""
    if max(s1868, s1855) < 0.40:
        return "on neither"
    if min(s1868, s1855) >= 0.20:
        return "mixed"
    return "1868" if s1868 > s1855 else "1855-56"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--band", action="store_true",
                    help="measure the whole northern band against both surveys")
    args = ap.parse_args()

    if args.band:
        return band(args.json)

    roads = load("city-roads.geojson")
    study = load_areas(STUDY)
    x0 = min(a.bbox[0] for a in study); y0 = min(a.bbox[1] for a in study)
    x1 = max(a.bbox[2] for a in study); y1 = max(a.bbox[3] for a in study)

    per_area, per_len, on, poly_hits, length_in, on_totals = tally(
        roads, study, [GRID_BEARING])
    per_grid = {n: on[n][0] for n in STUDY}
    length_on_grid = on_totals[0]

    box_hits = []
    for f in roads["features"]:
        name = (f["properties"].get("name") or "").strip()
        if not name:
            continue
        pts = coords_of(f["geometry"])
        if not pts:
            continue
        if any(x0 <= x <= x1 and y0 <= y <= y1 for x, y in pts):
            box_hits.append(name)

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
