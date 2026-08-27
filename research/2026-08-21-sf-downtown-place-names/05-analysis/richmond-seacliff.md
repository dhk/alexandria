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

## The northern band: where two surveys meet

Reproducible — `python3 richmond-extent.py --band`, stdlib only, no network.
Same inputs as above.

The four-neighbourhood study asks how much of the Richmond sits on its own grid.
It cannot ask the more interesting question, because it only tests one grid.
Widening the study to the whole northern edge of the city — fifteen DataSF
analysis neighbourhoods from the Pacific to the Bay, the four above plus the
Presidio, Golden Gate Park, Presidio Heights, Lone Mountain/USF, the Marina,
Pacific Heights, the Western Addition, Japantown, Russian Hill, Nob Hill and
North Beach — lets both city-scale surveys be tested against the same street at
once:

- **Richmond & Sunset, 3.5°** — Potter & Humphrey, 18 May 1868;
- **Western Addition, 9.5°** — Van Ness Ordinance, 1855–56.

Both at 2.5° tolerance, and each tested against **both** of its orthogonal
families (`θ` and `θ+90`), because a grid is two families and testing one throws
every cross street into "ungridded". The two windows, `[1.0, 6.0]` and
`[7.0, 12.0]`, do not overlap: no segment can be counted twice, and the three
shares sum to 100% by construction rather than by luck.

| neighbourhood | named streets | centreline | 1868 | 1855–56 | neither |
|---|---:|---:|---:|---:|---:|
| Seacliff | 16 | 7.92 km | 57.8% | 2.7% | 39.5% |
| Outer Richmond | 43 | 64.37 km | **93.2%** | 2.7% | 4.1% |
| Inner Richmond | 16 | 19.87 km | **95.1%** | 1.1% | 3.8% |
| Lincoln Park | 10 | 7.45 km | 21.2% | 3.8% | 75.0% |
| Presidio | 200 | 80.83 km | 16.8% | 7.1% | **76.1%** |
| Golden Gate Park | 34 | 45.74 km | 32.6% | 5.6% | **61.8%** |
| Presidio Heights | 24 | 13.72 km | 18.5% | 69.9% | 11.7% |
| Lone Mountain/USF | 46 | 15.45 km | 7.2% | **82.1%** | 10.7% |
| Marina | 50 | 35.36 km | 1.0% | **77.9%** | 21.1% |
| Pacific Heights | 16 | 16.38 km | 0.3% | **99.2%** | 0.5% |
| Western Addition | 33 | 18.61 km | 1.1% | **91.0%** | 8.0% |
| Japantown | 5 | 0.64 km | 0.0% | 90.1% | 9.9% |
| Russian Hill | 56 | 15.09 km | 1.0% | **93.0%** | 6.0% |
| Nob Hill | 51 | 6.12 km | 1.0% | **96.9%** | 2.0% |
| North Beach | 74 | 14.26 km | 0.4% | **85.4%** | 14.2% |
| **band** | **627** | **361.82 km** | 32.6% | 34.9% | 32.4% |

### Predictions made before the run, and how they fared

Thirteen of fifteen held. The two that did not are the useful ones.

**Held.** The Richmond pair stays above 93%. The three reservations — Presidio,
Golden Gate Park, Lincoln Park — land on *neither*, at 76%, 62% and 75%, exactly
as `grid-classification.md` says a park or a military road should. Pacific
Heights, the Western Addition, Japantown, Nob Hill, North Beach and the Marina
all sit on 9.5° above 77%. Presidio Heights was predicted 1855–56-dominant and
came in at 69.9%.

**Wrong: Lone Mountain/USF.** Predicted mixed, 20–50% on each, on the reasoning
that it lies west of Divisadero and so inside the Outside Lands. Measured
**7.2% / 82.1%** — as clean a Van Ness Ordinance neighbourhood as the Western
Addition itself. The prediction confused a *jurisdictional* boundary with a
*surveyed* one. The Outside Lands were land the city acquired; the bearing on
the ground records who drew the streets, and here the answer is the eastern
survey, carried west.

**Wrong: Russian Hill.** Predicted 50–80% on 1855–56, expecting the hill to
break the grid. Measured **93.0%**. A street climbing a 30% gradient keeps its
plan bearing; topography bends streets in section, not in plan. Only the
deliberately curvilinear ones (Lombard's crooked block, the Vallejo stairways)
fall out, and they are 6% of the length.

### Where the boundary actually falls

A per-neighbourhood table cannot answer this, and neither can a per-street one.
A street is a line, so averaging its vertices puts a long east–west boulevard in
the middle of nothing; sorting Presidio Heights' streets by mean longitude
produces an interleaving that is an artefact of that averaging, not a finding.

Binning the **segments** by their own midpoints into 0.005° columns (~440 m)
does answer it:

| column (lon) | km | 1868 | 1855–56 | neither |
|---|---:|---:|---:|---:|
| … | | | | |
| −122.470 | 23.14 | 47% | 3% | 51% |
| −122.465 | 20.82 | 50% | 3% | 47% |
| **−122.460** | **23.75** | **26%** | **23%** | **51%** |
| −122.455 | 21.20 | 7% | 46% | 47% |
| −122.450 | 21.97 | 2% | 60% | 38% |
| −122.445 | 18.86 | 3% | 88% | 9% |
| … | | | | |

The changeover is not gradual. It is one column wide. Across the ten columns
from −122.510 to −122.465 the 1855–56 grid never exceeds **3.7%**; across the
ten from −122.450 east, the 1868 grid never exceeds **3.0%**. In the single
column between them the two are level, 26% to 23%. (The eleventh western
column, the −122.515 sliver at the Lands End tip, is 2.08 km of centreline
reading 23% / 17% / 60% — too little to carry a claim, and excluded from the
two figures above for that reason rather than because it disagrees.)

That column spans lon −122.460 to −122.455. **Arguello Blvd runs from
−122.4616 to −122.4575** — measured from the committed centrelines — so it lies
inside that column and very nearly is it. On the ground, the 1868 Outside Lands
survey and the 1855–56 Van Ness Ordinance survey meet at Arguello Boulevard,
along a seam roughly 440 m wide.

The seam is a seam and not a line. Inside Presidio Heights, seven streets carry
the 1868 bearing — Commonwealth Ave and Jordan Ave at 100%, Palm Ave at 96%,
Heather Ave 71%, Iris Ave 55%, Euclid Ave 46%, Manzanita Ave 42% — while their
immediate neighbours Cherry, Maple, Locust, Cook, Blake, Walnut and Presidio Ave
are 100% on 9.5°. That is a block of Richmond-grid streets sitting east of
Arguello, which is why Presidio Heights reads 18.5% / 69.9% rather than 0% / 90%.

### What this cannot distinguish

**It measures bearing, not authorship.** The clearest demonstration is in the
Presidio, where the single most 1868-looking feature is **Golden Gate Brg, 97%
on the 1868 grid**, together with `State Rte 1` at 61% and `Arguello Blvd` at
54%. A 1937 suspension bridge is not an Outside Lands street; it runs at 3.5°
because it runs north. The same caution applies to the Jordan Park block above:
those streets share Potter and Humphrey's bearing, and this measurement cannot
say whether they were drawn by that survey, by a later subdivider continuing it,
or by coincidence. `RECALLED` and unverified here.

**The 9.5° label is broader than the survey it names.** Nob Hill, Russian Hill
and North Beach score 97%, 93% and 85% on a grid this corpus dates to 1855–56,
and those streets are older than that. The Van Ness Ordinance extended a bearing
westward; it did not invent it. So "1855–56" in the table is the name
`grid-classification.md` gives the 9.5° family, not a date for every street in
it. Separating the pre-1855 north-of-Market grid from the ordinance's extension
needs a spatial method this script does not have, and a document this corpus
does not hold.

**A reservation's "neither" is three things.** The Presidio's 76% and the park's
62% mix curvilinear design, roads that followed terrain, and service tracks. The
band cannot tell them apart, for the same reason `grid-classification.md` says
its own *ungridded* category cannot.

**Japantown is 640 m of centreline and five named streets.** Its 90.1% is a
real number about a very small sample; it is in the table because it is in the
band, not because it carries weight.

**Both peaks and the tolerance are still inherited**, hand-chosen in
`grid-classification.md` and not fitted. Widening the tolerance past 3.0° would
make the two windows touch, and the disjointness the three-way split relies on
would stop being true.
