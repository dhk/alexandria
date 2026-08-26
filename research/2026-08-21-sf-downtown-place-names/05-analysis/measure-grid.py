#!/usr/bin/env python3
"""Measure O'Farrell's survey module from TIGER centrelines.

Reads 04-normalized/geo/city-roads.geojson (public domain, see the sidecar)
and solves for the block module of the 1847 survey south of Market Street.

    python3 measure-grid.py            # the table in survey-grid-measurement.md
    python3 measure-grid.py --json     # same numbers, machine-readable

Stdlib only, no network. The GeoJSON it reads is committed, so this is
reproducible from the repository alone — which is the point: the claim in
survey-grid-measurement.md is only worth as much as the ability to re-run it.

THE RULER. Distances come from a local flat-earth approximation, constants
below. TIGER is NAD83 (EPSG:4269). This is not a geodetic computation on the
GRS80 ellipsoid, and the difference matters at the precision this script
reports: a 0.5% scale error moves the 100-vara lot by about 1.4 ft, which is
half the gap between a 33-inch and a 33 1/3-inch vara. Anyone who wants to
settle the vara must replace this approximation first. See the note's
"What the ruler can and cannot settle".
"""
from __future__ import annotations

import argparse
import collections
import json
import math
import pathlib

GEO = pathlib.Path(__file__).resolve().parent.parent / "04-normalized" / "geo" / "city-roads.geojson"

# Clip to downtown/SoMa. Street names are NOT unique city-wide -- there is a
# second "1st St" on Treasure Island -- so every lookup here is bounded.
BOX = (-122.415, 37.770, -122.385, 37.800)

# The ruler. Local flat-earth constants at 37.785 N. See the module docstring.
LAT_M = 111132.0
LON_M = 111320.0 * math.cos(math.radians(37.785))
FT = 0.3048

# Cross streets in survey order along Market, from the waterfront southwest.
# Spear St is deliberately absent: it sits between Steuart and Main, so that
# one span covers two modules and is halved below.
CROSS = ["Steuart St", "Spear St", "Main St", "Beale St", "Fremont St",
         "1st St", "2nd St", "3rd St", "4th St", "5th St", "6th St"]
ALONG = ["Market St", "Mission St", "Howard St", "Folsom St",
         "Harrison St", "Bryant St", "Brannan St", "Townsend St"]

# The survey seam. Page & Turnbull 2009, printed p.18: the grid east of 1st
# Street replicates the 50-vara survey north of Market; west of 1st Street it
# is O'Farrell's larger 100-vara blocks.
SEAM = "1st St"


def load():
    feats = json.loads(GEO.read_text())["features"]
    segs = collections.defaultdict(list)
    for f in feats:
        segs[f["properties"]["name"]].append(f["geometry"]["coordinates"])
    return segs


def in_box(p):
    return BOX[0] <= p[0] <= BOX[2] and BOX[1] <= p[1] <= BOX[3]


def pieces(segs, name):
    """Two-point pieces of a named street whose midpoint is inside the box."""
    return [(a, b) for line in segs.get(name, []) for a, b in zip(line, line[1:])
            if in_box(((a[0] + b[0]) / 2, (a[1] + b[1]) / 2))]


def intersect(segs, n1, n2):
    """The single intersection of two named streets, or None.

    None covers both "these streets do not meet" (Steuart never reaches
    Folsom) and "more than one candidate", which on fragmentary geometry
    means the answer is not trustworthy. Both are refusals, not failures.
    """
    hits = []
    for p1, p2 in pieces(segs, n1):
        for p3, p4 in pieces(segs, n2):
            den = (p2[0] - p1[0]) * (p4[1] - p3[1]) - (p2[1] - p1[1]) * (p4[0] - p3[0])
            if abs(den) < 1e-13:
                continue
            t = ((p3[0] - p1[0]) * (p4[1] - p3[1]) - (p3[1] - p1[1]) * (p4[0] - p3[0])) / den
            s = ((p3[0] - p1[0]) * (p2[1] - p1[1]) - (p3[1] - p1[1]) * (p2[0] - p1[0])) / den
            if -0.02 <= t <= 1.02 and -0.02 <= s <= 1.02:
                hits.append((p1[0] + t * (p2[0] - p1[0]), p1[1] + t * (p2[1] - p1[1])))
    keep = []
    for h in hits:
        if not any(abs(h[0] - k[0]) < 3e-4 and abs(h[1] - k[1]) < 3e-4 for k in keep):
            keep.append(h)
    return keep[0] if len(keep) == 1 else None


def feet(p, q):
    return math.hypot((p[0] - q[0]) * LON_M, (p[1] - q[1]) * LAT_M) / FT


def spacings(segs, sequence, on):
    """Centreline spacing between consecutive members of `sequence`, measured
    along the street `on`. Skips any pair whose intersections do not resolve."""
    out, prev = [], None
    for name in sequence:
        p = intersect(segs, name, on)
        if p is None:
            prev = None
            continue
        if prev:
            out.append((prev[0], name, feet(prev[1], p)))
        prev = (name, p)
    return out


def solve(rows):
    """Least squares for L (100 varas, ft) and s (street width, ft) over
    observations of the form (n_lots, 1, measured_ft)."""
    a = b = c = d = e = 0.0
    for p, q, y in rows:
        a += p * p; b += p * q; c += q * q; d += p * y; e += q * y
    det = a * c - b * b
    L = (c * d - b * e) / det
    s = (-b * d + a * e) / det
    res = [y - (p * L + q * s) for p, q, y in rows]
    rms = math.sqrt(sum(r * r for r in res) / len(res))
    return L, s, rms, max(abs(r) for r in res)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()

    segs = load()
    seam = CROSS.index(SEAM)

    # Module along Market, split at the survey seam.
    #
    # Measured on MISSION, not on Market. Market is the seam between two
    # surveys, and a cross street's Market intersection is set by where its
    # north-of-Market counterpart lands -- 3rd Street meets Market about 70 ft
    # off the SoMa grid, because north of Market it is Kearny's grid. Mission
    # is an interior street of the survey being measured, so it carries the
    # module uncontaminated. Market's own series is computed anyway and printed
    # as a diagnostic: the jog is a finding, not an error to hide.
    along_market = spacings(segs, CROSS, "Market St")
    along_mission = spacings(segs, CROSS, "Mission St")

    def side(rows, west):
        out = []
        for a_, b_, ft_ in rows:
            ia, ib = CROSS.index(a_), CROSS.index(b_)
            span = ib - ia                      # 1 normally, 2 where Spear is missing
            if (ia >= seam) == west:
                out.append((a_, b_, ft_ / span, span))
        return out

    east = side(along_mission, False)
    west = side(along_mission, True)
    market_east = side(along_market, False)
    market_west = side(along_market, True)
    # Depth into SoMa, measured on 3rd St. Market -> Mission is held out: Market
    # is wider than an ordinary street, so it does not belong to the same model.
    depth_all = spacings(segs, ALONG, "3rd St")
    depth = [r for r in depth_all if r[0] != "Market St"]
    mkmi = [r for r in depth_all if r[0] == "Market St"]

    # 50-vara block: 2x2 lots of 50 varas = 100 varas square = L.
    # 100-vara block: 3x2 lots of 100 varas   = 3L along Market, 2L deep.
    rows = ([(1, 1, r[2]) for r in east]
            + [(3, 1, r[2]) for r in west]
            + [(2, 1, r[2]) for r in depth])
    L, s, rms, mx = solve(rows)

    market_w = 2 * (mkmi[0][2] - 2 * L - s / 2) if mkmi else None
    vara_in = L / 100 * 12

    if args.json:
        print(json.dumps({
            "source": "04-normalized/geo/city-roads.geojson",
            "observations": len(rows),
            "lot_100_vara_ft": round(L, 2), "street_width_ft": round(s, 2),
            "vara_inches": round(vara_in, 3),
            "residual_rms_ft": round(rms, 2), "residual_max_ft": round(mx, 2),
            "market_width_ft": round(market_w, 1) if market_w else None,
            "ruler": "local flat-earth, spherical constants; not geodetic",
        }, indent=2))
        return

    def table(title, rows_):
        print(f"\n{title}")
        for a_, b_, ft_, span in rows_:
            tag = f"  (span of {span}, halved)" if span > 1 else ""
            print(f"  {a_:11} -> {b_:11} {ft_ * FT:7.1f} m {ft_:7.0f} ft{tag}")

    table(f"East of {SEAM} on Mission - 50-vara grid, one block per module", east)
    table(f"West of {SEAM} on Mission - 100-vara grid, three lots per module", west)
    print("\nSame spacings measured on Market St - diagnostic, not fitted")
    for a_, b_, ft_, span in market_east + market_west:
        print(f"  {a_:11} -> {b_:11} {ft_ * FT:7.1f} m {ft_:7.0f} ft")
    print("\nDepth into SoMa, measured on 3rd St")
    for a_, b_, ft_ in depth:
        print(f"  {a_:11} -> {b_:11} {ft_ * FT:7.1f} m {ft_:7.0f} ft")
    for a_, b_, ft_ in mkmi:
        print(f"  {a_:11} -> {b_:11} {ft_ * FT:7.1f} m {ft_:7.0f} ft   (held out: Market is wider)")

    print(f"\nLeast squares, {len(rows)} spacings, 2 free parameters")
    print(f"  100-vara lot L    = {L:7.2f} ft    -> 1 vara = {vara_in:.3f} in")
    print(f"  street width s    = {s:7.2f} ft")
    print(f"  residual RMS      = {rms:7.2f} ft    max {mx:.2f} ft")
    print(f"  predicted east    = {L + s:7.1f} ft    measured {sum(r[2] for r in east) / len(east):7.1f}")
    print(f"  predicted west    = {3 * L + s:7.1f} ft    measured {sum(r[2] for r in west) / len(west):7.1f}")
    print(f"  predicted depth   = {2 * L + s:7.1f} ft    measured {sum(r[2] for r in depth) / len(depth):7.1f}")
    if market_w:
        print(f"  Market St width   = {market_w:7.1f} ft    (O'Farrell's is described as 120)")
    print(f"  3rd St meets Market about 70 ft off the SoMa grid: north of Market it")
    print(f"  is Kearny's grid, not O'Farrell's. Hence measuring the module on Mission.")
    print(f"\n  vara candidates:  33 in -> L = {33 * 100 / 12:.1f} ft"
          f"  ({abs(L - 33 * 100 / 12) / rms:.2f} RMS away)")
    print(f"                    33 1/3 in -> L = {100 * (33 + 1 / 3) / 12:.1f} ft"
          f"  ({abs(L - 100 * (33 + 1 / 3) / 12) / rms:.2f} RMS away)")
    print("\n  Neither is excluded. The ruler above is not geodetic and carries a")
    print("  systematic error comparable to the gap between them.")


if __name__ == "__main__":
    main()
