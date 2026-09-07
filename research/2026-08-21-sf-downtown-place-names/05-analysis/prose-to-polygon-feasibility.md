# Can a boundary sentence become a polygon?

**Status:** feasibility measurement, single-analyst, not graded.
**Question:** the atlas's extents are prose — "bounded by Market, Howard, 1st,
and 2nd streets". Turning ~400 of those into geometry by hand is not viable.
How much of it can be done mechanically?

**Answer: 88% of real bounding descriptions name enough streets to close a
polygon.** That is higher than expected and it changes the sizing of the whole
place-name programme.

## What was measured

Every `bounded|bordered by|on` construction in the nine SF Planning documents
retrieved so far — 95 descriptions across 9 documents — classified by whether
the streets named are sufficient to close a figure.

| | count | share |
|---|---:|---:|
| A. four or more streets — a closed figure | 72 | 75.8% |
| B. three streets — closable against a fourth | 12 | 12.6% |
| C. streets plus a landform or structure | 6 | 6.3% |
| D. two streets — a corridor, not an area | 3 | 3.2% |
| E. fewer than two — not resolvable from streets | 2 | 2.1% |

A + B = **88%** resolvable against committed centrelines.

## What this costs

Roughly ten bounding descriptions per document. SF Planning has on the order of
forty context statements and surveys, so **order 400 shapes** from that source
alone, before counting tracts named without `bounded by` phrasing.

| | |
|---|---|
| `acquire-documents.py` — fetch ~40 PDFs, checksum, extract, page offsets | ~1 day |
| the extractor — find descriptions, propose street lists | ~½ day |
| the solver — street names + centrelines → polygon + precision | ~2 days |
| **the human pass — confirm each shape against its sentence** | **15–30 hours** |

The human pass is the long pole and does not compress: 400 shapes at two to five
minutes each. Everything before it exists to make those minutes possible.

## The first measurement was wrong, and how

A first pass reported 52% rather than 88%, from a classifier that required each
street name to carry its own thoroughfare noun — `Market Street`, `Geary Ave`.
The dominant real form lists names bare with one plural noun closing the list:

> bounded by Webster, Sutter, Bush and Laguna streets

That was filed as *"no street named at all."* The output was a clean table with
plausible percentages, and it was wrong by 36 points.

This is the third time in this investigation that a wrong answer looked right —
after the freeway filter and the one-family grid test. Recording it here for the
same reason as the others: the failure mode is not "the code crashed", it is
"the code produced a believable number".

## What does not yield to a tool

**Renamed streets are a dependency, not a detail.** The sample contains
`Dupont (now Grant Avenue)`. Historical descriptions use historical names; TIGER
carries modern ones. A rename table is therefore a *prerequisite* for resolving
pre-modern boundaries, which promotes
[#78](https://github.com/dhk/alexandria/issues/78) from a nice-to-have to a
blocker. `Army St` surviving beside `Cesar Chavez St` in TIGER 2025 was the
first sighting of the same problem.

**Vanished streets.** Redevelopment and the freeways erased streets that
historical boundaries reference. Western Addition A-2 removed many. No modern
centreline exists to intersect.

**Landforms are 6%, and they are the interesting 6%** — "the old shoreline", "a
ridge of sand dunes located east of what is today Second Street". These carry
the historical geography that street grids cannot, and each needs its own
reconstruction.

**"Generally bounded" is not "bounded."** The hedge is evidence about precision
and must survive into the shape, or the map asserts more than its source. The
viewer already renders this distinction: `approximate` gets a seeded wobble,
`exact` a hard edge.

## Coverage is a rate, not a finish line

There is no closed list of historical shapes. New documents surface new ones
indefinitely. The honest target is a coverage metric — shapes resolved, from how
many documents, covering what fraction of the city-years the timeline spans —
rather than a percentage of a total nobody can count.

## Where the documents actually are

Retrieved so far, all SF Planning: SoMa historic context statement, Central SoMa
EIR, Japantown, Market & Octavia, Mission, North Beach, Parkside, Corbett
Heights, and the citywide modern context statement.

Coverage is uneven and does not match where the work is wanted:

| district | dedicated document | bounding descriptions |
|---|---|---:|
| South of Market | yes | many |
| Sunset / Parkside | yes (`parkside`) | 1 naming the district |
| Richmond | **none** | **0** |
| Marina | **none** | 0 |
| Presidio | **none** | 0 |

Building the Richmond means fetching a Richmond document first. The tool does
not care which district it is pointed at; the corpus does.
