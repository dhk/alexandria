#!/usr/bin/env python3
"""Build 06-viewer/index.html from template.html and the committed geometry.

    python3 build.py            # write index.html
    python3 build.py --check    # rebuild in memory, diff against the committed
                                # file, exit 1 if they differ

index.html is DERIVED, not authored. Edit template.html and rebuild. Stdlib
only, no network: the geometry it reads is committed under 04-normalized/geo/
with a checksummed sidecar, so the page is reproducible from this repository.

WHAT THIS DOES, AND WHAT IT DOES NOT CLAIM

Every named street in San Francisco is assigned to one of seven survey grids by
the direction it runs, or to none. That is a classification, not a measurement.
It says which survey drew a street; it does not say what that survey's block
module was. See ../05-analysis/grid-classification.md for the limits, which are
real and are printed on the page itself.

The seven bearings below were read off the length-weighted bearing histogram by
eye, not fitted. TOL is likewise chosen, not derived. Change either and the
shares move -- which is the honest way to say the boundaries are soft.
"""
from __future__ import annotations

import argparse
import collections
import json
import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
GEO = HERE.parent / "04-normalized" / "geo"

# Projection origin. A local flat-earth approximation, the same ruler
# 05-analysis/measure-grid.py uses and with the same caveat: fine for drawing a
# city-sized page, not a geodetic computation.
LAT0, LON0 = 37.7600, -122.4400
LAT_M = 111132.0
LON_M = 111320.0 * math.cos(math.radians(LAT0))

# (bearing in degrees CCW from east, folded to 0-180; stable id)
# (bearing, id, survey year or None, survey as cited)
#
# Only three of the seven can be dated from this corpus. The other four are
# measured and deliberately undated: no source here says when they were laid
# out, and a guessed year would be worse than a gap -- the gap is what someone
# who knows can correct.
GRIDS = [
    (3.5,  "richmond-sunset",  1868, "Potter & Humphrey, 18 May 1868"),
    (9.5,  "western-addition", 1855, "Van Ness Ordinance, 1855-56"),
    (45.0, "south-of-market",  1847, "O'Farrell, 1847"),
    (54.5, "bayview",          None, None),
    (18.0, "portola",          None, None),
    (86.5, "lakeside",         None, None),
    (59.0, "excelsior",        None, None),
]
TOL = 2.5          # degrees; a street beyond this from every peak is ungridded
MIN_SEG = 8.0      # metres; shorter pieces have unreliable bearings
PRECISION = 1      # decimal places on projected metres, ~10 cm


def project(p):
    """lon/lat -> metres east/south of the origin. y is flipped for SVG."""
    return ((p[0] - LON0) * LON_M, -(p[1] - LAT0) * LAT_M)


def grid_of(bearing):
    """Index of the nearest peak within TOL, or -1 for ungridded.

    A survey grid is TWO orthogonal families of streets -- the ones running
    along it and the ones crossing it -- so a bearing must be tested against
    both `theta` and `theta + 90`. Testing only `theta` keeps the along-family
    and throws the cross-family into "ungridded", which looks plausible (the
    map still draws streets, the shares still sum) and is wrong: it took
    ungridded from 33% to 70% and quietly deleted half of every grid.
    """
    best, best_d = -1, 999.0
    for i, (theta, *_rest) in enumerate(GRIDS):
        d = min(abs(((bearing - theta + 90) % 180) - 90),
                abs(((bearing - theta) % 180) - 90))
        if d < best_d:
            best, best_d = i, d
    return best if best_d <= TOL else -1


def build_data():
    roads = json.loads((GEO / "city-roads.geojson").read_text())["features"]
    waters = json.loads((GEO / "city-water.geojson").read_text())["features"]

    feats, km, rose = [], collections.Counter(), [0.0] * 180
    for f in roads:
        pts = [project(p) for p in f["geometry"]["coordinates"]]
        # A street is assigned by a length-weighted vote over its own pieces, so
        # one short jog cannot reclassify a long straight run.
        vote = collections.Counter()
        for a, b in zip(pts, pts[1:]):
            length = math.hypot(b[0] - a[0], b[1] - a[1])
            if length < MIN_SEG:
                continue
            bearing = math.degrees(math.atan2(-(b[1] - a[1]), b[0] - a[0])) % 180
            rose[int(bearing) % 180] += length
            vote[grid_of(bearing)] += length
        if not vote:
            continue
        k = vote.most_common(1)[0][0]
        km[k] += sum(vote.values())
        flat = [round(q, PRECISION) for p in pts for q in p]
        feats.append([k, f["properties"]["name"], flat])

    water = []
    for w in waters:
        g = w["geometry"]
        if g["type"] == "LineString":
            rings = [g["coordinates"]]
        elif g["type"] == "MultiLineString":
            rings = g["coordinates"]
        else:
            rings = [g["coordinates"][0]]
        for r in rings:
            if len(r) > 2:
                water.append([round(q, PRECISION) for p in map(project, r) for q in p])

    return {
        "grids": [{"bearing": t, "id": n, "metres": round(km[i]),
                   "year": y, "survey": s}
                  for i, (t, n, y, s) in enumerate(GRIDS)],
        "unassigned_m": round(km[-1]),
        "rose": [round(x) for x in rose],
        "roads": feats,
        "water": water,
    }


# template.html carries page content only -- no doctype, no <html>, no <head>,
# no <body> -- because that is the shape a published Artifact wants; the host
# supplies the skeleton. A file on disk needs the skeleton to be a document, and
# so does dhk-website's scripts/sync-study.mjs, which slices <body> out of this
# page to derive its own markup. So index.html is written wrapped, and --bare
# prints the unwrapped form for an Artifact publish. One authored template, two
# shapes, neither of them hand-maintained.
# Both pages are built from the same data by the same script. The map and the
# timeline are separate pages rather than two modes of one because they are
# shared separately -- each gets its own URL and its own argument.
PAGES = {
    "index":    {"template": "template.html",          "out": "index.html"},
    "timeline": {"template": "timeline-template.html", "out": "timeline.html"},
}

HEAD_OPEN = '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
VIEWPORT = '<meta name="viewport" content="width=device-width,initial-scale=1">\n'


def render(bare=False, page="index"):
    template = (HERE / PAGES[page]["template"]).read_text()
    if "__DATA__" not in template:
        raise SystemExit(f"{PAGES[page]['template']} has no __DATA__ placeholder")
    payload = json.dumps(build_data(), separators=(",", ":"), sort_keys=False)
    page = template.replace("__DATA__", payload)
    if bare:
        return page

    # Everything up to the end of </style> is head material; the rest is body.
    split = page.index("</style>") + len("</style>")
    return (HEAD_OPEN + VIEWPORT + page[:split].strip()
            + "\n</head>\n<body>\n" + page[split:].strip() + "\n</body>\n</html>\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true",
                    help="fail if the committed index.html is not what this builds")
    ap.add_argument("--page", choices=sorted(PAGES), default=None,
                    help="build just this page (default: all of them)")
    ap.add_argument("--bare", action="store_true",
                    help="print the page without the html/head/body skeleton, "
                         "the shape a published Artifact wants, and exit")
    args = ap.parse_args()

    if args.bare:
        sys.stdout.write(render(bare=True, page=args.page or "index"))
        return 0

    wanted = [args.page] if args.page else sorted(PAGES)
    if args.check:
        for name in wanted:
            built = render(page=name)
            target = HERE / PAGES[name]["out"]
            if not target.exists():
                print(f"{target.name} is missing; run build.py", file=sys.stderr)
                return 1
            if target.read_text() != built:
                print(f"{target.name} is stale; run build.py and commit the result",
                      file=sys.stderr)
                return 1
            print(f"{target.name} up to date ({len(built) / 1048576:.2f} MB)")
        return 0

    for name in wanted:
        if name != "index":
            out = HERE / PAGES[name]["out"]
            out.write_text(render(page=name))
            print(f"wrote {out.name} — {out.stat().st_size / 1048576:.2f} MB")

    page = render()
    target = HERE / "index.html"
    target.write_text(page)
    data = json.loads(page.split('type="application/json">', 1)[1].split("</script>", 1)[0])
    total = sum(g["metres"] for g in data["grids"]) + data["unassigned_m"]
    print(f"wrote {target.name} — {target.stat().st_size / 1048576:.2f} MB, "
          f"{len(data['roads'])} roads, {len(data['water'])} water rings")
    for g in data["grids"]:
        print(f"  {g['id']:18} {g['bearing']:5.1f}deg  {g['metres'] / 1000:7.1f} km"
              f"  {g['metres'] / total * 100:5.1f}%")
    print(f"  {'ungridded':18} {'':8}  {data['unassigned_m'] / 1000:7.1f} km"
          f"  {data['unassigned_m'] / total * 100:5.1f}%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
