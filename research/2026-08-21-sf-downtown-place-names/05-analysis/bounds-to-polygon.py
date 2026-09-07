#!/usr/bin/env python3
"""Turn a boundary sentence into a polygon, with an honest precision marker.

    python3 bounds-to-polygon.py "bounded by Market, Howard, 1st and 2nd streets"
    python3 bounds-to-polygon.py --geojson "bounded by ..." > shape.geojson
    python3 bounds-to-polygon.py --self-test

Stdlib only, no network. Reads ../04-normalized/geo/city-roads.geojson, which is
committed, public domain and checksummed -- so a shape produced here is
reproducible from this repository alone.

WHAT IT DOES

Extracts street names from a bounding description, resolves each against the
committed centrelines, intersects them pairwise, and returns the convex hull of
the corners. 88% of real bounding descriptions in this corpus name enough
streets for that to close -- see prose-to-polygon-feasibility.md.

WHAT IT REFUSES TO PRETEND

The precision marker is the point, not the polygon. A description hedged with
"generally bounded" produces `approximate`, never `exact`, because the hedge is
evidence about how well the source knew the edge. Two streets produce
`corridor`, not a sliver of area. Anything it cannot close is reported as
`unresolved` with the reason, and callers get no geometry rather than a guess.

The convex hull is itself an assumption: it is right for the rectangles that
four cross streets describe and wrong for an L-shaped district. A hull whose
vertex count does not match the street count is therefore demoted to
`approximate` and says so.

KNOWN GAPS, all recorded in the feasibility note

Renamed streets ("Dupont (now Grant Avenue)") resolve only under their modern
name, so pre-rename boundaries need the provenance table from alexandria#78.
Streets erased by redevelopment have no centreline at all. Landform edges
("the old shoreline") are not streets and are out of scope here.
"""
from __future__ import annotations

import argparse
import collections
import json
import math
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
GEO = HERE.parent / "04-normalized" / "geo" / "city-roads.geojson"

LAT_M = 111132.0
LON_M = 111320.0 * math.cos(math.radians(37.76))

SPELLED = {n: f"{i+1}" for i, n in enumerate(
    "first second third fourth fifth sixth seventh eighth ninth tenth eleventh twelfth "
    "thirteenth fourteenth fifteenth sixteenth seventeenth eighteenth nineteenth twentieth".split())}
SUFFIX = {"street": "St", "st": "St", "avenue": "Ave", "ave": "Ave", "av": "Ave",
          "boulevard": "Blvd", "blvd": "Blvd", "road": "Rd", "rd": "Rd", "way": "Way",
          "place": "Pl", "pl": "Pl", "alley": "Aly", "aly": "Aly", "drive": "Dr", "dr": "Dr"}
# Tried in order when a description names a street without saying what kind it is.
GUESS = ["St", "Ave", "Blvd", "Way", "Blvd", "Rd", "Pl", "Aly", "Dr", ""]

HEDGE = re.compile(r"\b(generally|roughly|approximately|about|circa|more or less|"
                   r"in the (?:area|vicinity)|around)\b", re.I)

_cache: dict = {}


def load():
    if "segs" not in _cache:
        segs = collections.defaultdict(list)
        for f in json.loads(GEO.read_text())["features"]:
            segs[f["properties"]["name"]].append(f["geometry"]["coordinates"])
        _cache["segs"] = segs
    return _cache["segs"]


def ordinalise(word: str) -> str:
    """Seventeenth -> 17th; 27 -> 27th; 3rd -> 3rd."""
    w = word.lower().strip()
    if w in SPELLED:
        w = SPELLED[w]
    m = re.fullmatch(r"(\d{1,3})\s*(st|nd|rd|th)?", w)
    if not m:
        return word
    n = int(m.group(1))
    tail = "th" if 11 <= n % 100 <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{tail}"


def extract(text: str) -> list[str]:
    """Street names out of a bounding description.

    The list ends at the plural thoroughfare noun that closes it -- the common
    form is "Webster, Sutter, Bush and Laguna streets", one noun for four names.
    Reading past it swallows the rest of the sentence as street names, which is
    how a first attempt at this measurement came out 36 points wrong.
    """
    body = re.split(r"\b(?:bounded|bordered)\s+(?:generally\s+|roughly\s+|approximately\s+)?"
                    r"(?:by|on)\b", text, flags=re.I)[-1]
    cut = re.search(r"\b(streets|avenues|st\.|ave\.)\b", body, re.I)
    seg = body[:cut.start()] if cut else re.split(r"[.;]", body)[0]

    # The leading name may be an ordinal -- "27th Avenue" -- so digits are allowed
    # here. Requiring a capital letter dropped every numbered avenue in the
    # Sunset and the Richmond, which is most of their street names.
    names, singular = [], re.compile(
        r"\b((?:\d{1,3}\s*(?:st|nd|rd|th)|[A-Z][A-Za-z'\-]+)(?:\s[A-Z][A-Za-z'\-]+)?)\s+"
        r"(Street|St|Avenue|Ave|Av|Boulevard|Blvd|Road|Rd|Way|Place|Pl|Alley|Aly|Drive|Dr)\b")
    for m in singular.finditer(seg):
        names.append(f"{ordinalise(m.group(1))} {SUFFIX.get(m.group(2).lower(), m.group(2))}")
        seg = seg.replace(m.group(0), " ")
    for tok in re.split(r",|\band\b|&", seg):
        tok = tok.strip(" .;:()")
        if not tok:
            continue
        m = re.fullmatch(r"([A-Z][A-Za-z'\-]+(?:\s[A-Z][A-Za-z'\-]+)?|\d{1,3}\s*(?:st|nd|rd|th)?)", tok)
        if m:
            names.append(ordinalise(m.group(1)))
    return list(dict.fromkeys(n for n in names if len(n) > 1))


def resolve(name: str, box=None):
    """A named street's pieces, trying each thoroughfare suffix in turn."""
    segs = load()
    cands = [name] if re.search(r"\b(St|Ave|Blvd|Way|Rd|Pl|Aly|Dr)$", name) else \
            [f"{name} {s}".strip() for s in GUESS]
    for c in cands:
        if c in segs:
            out = []
            for line in segs[c]:
                for a, b in zip(line, line[1:]):
                    if box is None or (box[0] <= (a[0]+b[0])/2 <= box[2]
                                       and box[1] <= (a[1]+b[1])/2 <= box[3]):
                        out.append((a, b))
            if out:
                return c, out
    return None, []


def cross(p1, p2, p3, p4):
    d = (p2[0]-p1[0])*(p4[1]-p3[1]) - (p2[1]-p1[1])*(p4[0]-p3[0])
    if abs(d) < 1e-13:
        return None
    t = ((p3[0]-p1[0])*(p4[1]-p3[1]) - (p3[1]-p1[1])*(p4[0]-p3[0])) / d
    u = ((p3[0]-p1[0])*(p2[1]-p1[1]) - (p3[1]-p1[1])*(p2[0]-p1[0])) / d
    if -0.02 <= t <= 1.02 and -0.02 <= u <= 1.02:
        return (p1[0] + t*(p2[0]-p1[0]), p1[1] + t*(p2[1]-p1[1]))
    return None


def dedupe(corners, tol=3e-4):
    """Merge intersections that are the same corner found twice.

    Two streets cross once, but their centrelines are many two-point pieces, so
    adjacent pieces yield hits a fraction of a metre apart. `set()` only catches
    exact ties, and a convex hull is acutely sensitive to the rest: a
    near-duplicate adds a phantom vertex, or makes a real corner look collinear
    and drops it. That is worth a comment because it cost both self-test
    failures at once -- five corners on one case and three on another, from the
    same missing line.
    """
    out = []
    for c in corners:
        if not any(abs(c[0] - k[0]) < tol and abs(c[1] - k[1]) < tol for k in out):
            out.append(c)
    return out


def prune(corners):
    """Drop intersections that belong to a same-named street somewhere else.

    Street names are not unique city-wide -- there is a second `1st St` on
    Treasure Island, and `1st St`'s own geometry is fragmentary enough to meet
    Bryant St 246 m from where the grid puts it. Both inject corners hundreds of
    metres to kilometres from the real figure, and a convex hull is maximally
    sensitive to exactly that.

    So: keep the corners near the median corner. The threshold scales with the
    figure, which is what lets one rule serve a city block and a whole district.
    """
    if len(corners) < 4:
        return corners
    mx = sorted(c[0] for c in corners)[len(corners) // 2]
    my = sorted(c[1] for c in corners)[len(corners) // 2]
    d = [math.hypot((c[0] - mx) * LON_M, (c[1] - my) * LAT_M) for c in corners]
    med = sorted(d)[len(d) // 2] or 1.0
    keep = [c for c, dist in zip(corners, d) if dist <= max(4 * med, 250.0)]
    return keep if len(keep) >= 3 else corners


def hull(pts):
    pts = sorted(set(pts))
    if len(pts) < 3:
        return pts
    def turn(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
    lo = []
    for p in pts:
        while len(lo) >= 2 and turn(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    up = []
    for p in reversed(pts):
        while len(up) >= 2 and turn(up[-2], up[-1], p) <= 0:
            up.pop()
        up.append(p)
    return lo[:-1] + up[:-1]


def solve(text: str, box=None) -> dict:
    names = extract(text)
    hedged = bool(HEDGE.search(text))
    resolved, missing = [], []
    for n in names:
        actual, pieces = resolve(n, box)
        (resolved if pieces else missing).append(actual or n)
    out = {"description": text.strip(), "streets_named": names,
           "streets_resolved": resolved, "streets_unresolved": missing,
           "hedged": hedged}

    if len(resolved) < 2:
        return {**out, "precision": "unresolved",
                "why": f"only {len(resolved)} of {len(names)} street name(s) match the centrelines"}
    if len(resolved) == 2:
        return {**out, "precision": "corridor",
                "why": "two streets describe a corridor, not an enclosed area"}

    corners = []
    for i in range(len(resolved)):
        for j in range(i + 1, len(resolved)):
            _, a = resolve(resolved[i], box)
            _, b = resolve(resolved[j], box)
            for p1, p2 in a:
                for p3, p4 in b:
                    hit = cross(p1, p2, p3, p4)
                    if hit:
                        corners.append((round(hit[0], 6), round(hit[1], 6)))
    corners = prune(dedupe(corners))
    ring = hull(corners)
    if len(ring) < 3:
        return {**out, "precision": "unresolved",
                "why": f"{len(resolved)} streets resolved but they do not intersect into a figure"}

    # A hull with more vertices than streets means the streets meet more than
    # once -- a bend, a duplicate name elsewhere in the city, or a non-convex
    # district. The shape is still useful; it is not exact.
    exact = len(ring) == len(resolved) and not hedged and len(resolved) >= 4
    prec = "exact" if exact else "approximate"
    why = ("four or more streets closing a figure with one corner each"
           if exact else
           "hedged in the source" if hedged else
           f"{len(ring)} hull corners from {len(resolved)} streets, so the figure is not a simple "
           f"one-corner-per-street quadrilateral" if len(ring) != len(resolved) else
           "three streets closed against each other, the fourth edge inferred")
    return {**out, "precision": prec, "why": why, "corners": len(ring), "ring": ring}


def to_geojson(r: dict) -> dict:
    ring = list(r["ring"]) + [r["ring"][0]]
    props = {k: v for k, v in r.items() if k != "ring"}
    props["marker"] = "DERIVED"
    props["source"] = "05-analysis/bounds-to-polygon.py over 04-normalized/geo/city-roads.geojson"
    return {"type": "Feature", "properties": props,
            "geometry": {"type": "Polygon", "coordinates": [[list(p) for p in ring]]}}


SELF_TEST = [
    # description, expected precision, a note on why it is in the suite
    ("bounded by Market, Howard, 1st and 2nd streets", "exact",
     "Happy Valley, the case measured by hand earlier"),
    ("bounded by Webster, Sutter, Bush and Laguna streets", None,
     "the bare-list form that broke the first classifier"),
    ("generally bounded by Mission, 4th, Folsom, and 10th streets", "approximate",
     "hedged in the source, so it must not come back exact"),
    ("bounded by 27th Avenue, 39th Avenue, Kirkham Street, and Quintara", None,
     "a Doelger tract in the Sunset -- numbered avenues, one bare name"),
    ("bounded by Market and Mission streets", "corridor",
     "two streets are a corridor, not an area"),
    ("bounded on the northeast by the Old Mission Road", "unresolved",
     "a road that is not in the modern centrelines"),
]


def self_test() -> int:
    bad = 0
    for text, expect, note in SELF_TEST:
        r = solve(text)
        got = r["precision"]
        ok = expect is None or got == expect
        bad += not ok
        print(f"  {'ok ' if ok else 'BAD'}  {got:12} {'(want ' + expect + ')' if expect and not ok else '':22} {note}")
        print(f"        named {r['streets_named']}")
        print(f"        resolved {r['streets_resolved']}"
              + (f"  unresolved {r['streets_unresolved']}" if r["streets_unresolved"] else ""))
        print(f"        {r['why']}\n")
    print("all expectations met" if not bad else f"{bad} case(s) off expectation")
    return 1 if bad else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("description", nargs="?", help="a bounding description in prose")
    ap.add_argument("--geojson", action="store_true", help="emit a GeoJSON Feature")
    ap.add_argument("--self-test", action="store_true", help="run the built-in cases")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    if not args.description:
        ap.error("give a description, or --self-test")
    r = solve(args.description)
    if args.geojson:
        if "ring" not in r:
            print(json.dumps(r, indent=2), file=sys.stderr)
            return 2
        print(json.dumps(to_geojson(r), indent=2))
        return 0
    print(json.dumps({k: v for k, v in r.items() if k != "ring"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
