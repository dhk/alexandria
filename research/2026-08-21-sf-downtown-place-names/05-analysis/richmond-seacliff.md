# The Richmond and Seacliff: one survey, measured

**Status:** analysis, single-analyst, not graded. Reproducible —
`python3 richmond-extent.py`, stdlib only, no network.
**Inputs:** `04-normalized/geo/neighborhoods.geojson` (DataSF, PDDL, `FETCHED`),
`04-normalized/geo/city-roads.geojson` (TIGER 2025, public domain, `FETCHED`),
and `04-normalized/sources/manifest.json` entry `sunset-hcs` (`FETCHED`).

## Why this area

It is the largest survey grid in San Francisco. `grid-classification.md` puts
**Richmond & Sunset at 31.6% of the city's centreline** — 635.8 km, more than
the Western Addition and South of Market grids combined. Whatever is true of
the survey record at scale is most true here.

## What the ground says

Study area: **Seacliff, Outer Richmond, Inner Richmond, Lincoln Park.** The
Presidio and Golden Gate Park are deliberately excluded — they are reservations
the survey went around, not through.

| neighbourhood | named streets | centreline | on the 1868 grid |
|---|---:|---:|---:|
| Inner Richmond | 16 | 19.87 km | **95.1%** |
| Outer Richmond | 43 | 64.37 km | **93.2%** |
| Seacliff | 16 | 7.92 km | 57.8% |
| Lincoln Park | 10 | 7.45 km | 21.2% |
| **study area** | **82** | **99.61 km** | **85.4%** |

Tested against 3.5° and 93.5° with a 2.5° tolerance — both families, because a
grid is two of them.

The split is the point. The Richmond proper is as close to a pure survey
artefact as this city offers: better than nine streets in ten, by length, lie on
the bearing Potter and Humphrey set. Seacliff and Lincoln Park fall away exactly
as `grid-classification.md` predicts they should — it names Sea Cliff among the
"deliberate curvilinear plats" that land in *ungridded*, and Lincoln Park is
park roads. **That is a prediction made before this measurement and confirmed
by it**, which is worth more than either statement alone.

## The survey, now cited rather than merely named

`grid-classification.md` attributed this grid to "Potter & Humphrey, 18 May
1868" and cited nothing. The Sunset context statement says it outright:

> During the course of the negotiations, the City commissioned George C. Potter
> and William T. Humphrey to plat the former Outside Lands, a project that was
> completed on May 18, 1868. They mapped the Richmond and Sunset Districts in
> the now familiar rectilinear grid pattern of blocks and streets.

— `sunset-hcs`, printed p.20 (PDF p.20). `FETCHED`.

The same document places the Richmond inside the Outside Lands explicitly: the
area "contained what is now Golden Gate Park and the neighborhoods adjacent to
the park: the Sunset District (to the south) and Richmond District (to the
north)" (printed p.19). So the grid measured here and the survey named there are
the same object, and the attribution is no longer floating.

It also dates the *paper*, not the ground: "The platted streets existed only on
paper for decades, and some were not graded and/or paved until the 1940s."
A street's bearing is 1868; its existence may be seventy years younger.

## Behaviour at scale: the bounding box costs 41%

The standing rule in `HANDOFF.md` is that street names are not unique city-wide,
so every lookup must be bounded by a box. Measured here, that box is expensive:

| | |
|---|---:|
| named streets inside the four polygons | 82 |
| named streets inside their bounding box | 139 |
| pulled in by the box alone | **57 (41%)** |

The box is 5.01 × 2.23 km and its rectangle also covers Golden Gate Park, the
Presidio, Presidio Heights and Lone Mountain/USF — four neighbourhoods nobody
asked for. In the northern city a bounding box is not an approximation of a
neighbourhood; it is roughly twice one. Point-in-polygon against the committed
DataSF boundaries costs little and is what `richmond-extent.py` uses.

## The shared names are the survey, not a collision

50 of the 82 names also occur outside the study area, which reads like the
Treasure Island `1st St` problem. It is not.

**45 of the 50 are numbered Avenues** — 2nd through 48th — and their
out-of-area occurrences land in Sunset/Parkside (44) and Inner Sunset (26).
Those are the other half of the same plat. The avenues repeat because Potter and
Humphrey drew Richmond and Sunset as one grid in one act, and the numbering runs
straight across Golden Gate Park between them.

The remaining five are ordinary continuations east — Geary Blvd, Golden Gate
Ave, Funston Ave, La Playa St, and one unnamed `Easement`.

So a name lookup here needs a box for correctness, and the box's *hits* are
evidence about the survey rather than noise to discard.

## The gap this leaves

**San Francisco Planning has no historic context statement for the Richmond or
Seacliff.** Its citywide context statement is an index of neighbourhood
statements, and no entry covers either. Checked against the department's own
index and its project list; the nearest covering document is the Sunset
statement used above, which describes the Richmond only in passing.

Across the eleven documents now in `04-normalized/sources/manifest.json`,
"Richmond District", "Outer/Inner Richmond", "Sea Cliff" and "Outside Lands"
appear 29 times in total, nearly all incidental.

This is the largest survey grid in the city and the least documented
neighbourhood in this corpus. Closing it needs sources outside SF Planning.

## Everything soft about it

- **The neighbourhood boundaries are modern administrative ones.** DataSF
  analysis neighbourhoods are a frame to hang history on. "Seacliff" the
  polygon is not "Sea Cliff" the 1912 plat, and this document does not claim it
  is.
- **The 3.5° peak and the 2.5° tolerance are inherited**, hand-chosen in
  `grid-classification.md` and not fitted. Change either and these shares move.
- **A street is assigned to one neighbourhood** by a majority of its vertices,
  so a street straddling a boundary lands wholly on one side.
- **`William T. Humphrey`** is the name as the Sunset statement prints it.
  Whether the initial and the singular surname are correct — other accounts of
  the City surveyor of this period give a different middle initial and a plural
  surname — is `RECALLED` and unverified here. It wants a second document.
- **The ruler is the same flat-earth approximation** used elsewhere in this
  investigation: fine for bearings and lengths at city scale.
