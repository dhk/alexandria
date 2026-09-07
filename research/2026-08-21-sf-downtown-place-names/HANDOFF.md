# Start here

You are picking up the San Francisco survey and place-name work, most likely in
a session running on **lobster**, where egress is open. This file is the state
of play and the things that will bite you. It is meant to be read in full before
you touch anything; it is short on purpose.

Read next: [`02-run-plan/retrieval-pipeline.md`](02-run-plan/retrieval-pipeline.md)
for the method, and [`topic.yaml`](topic.yaml) for the two decisions that shape
everything below.

## Two decisions already made

**Scope, 26 Aug.** The trunk is the **survey record read from public-domain
data**; place names are one strand on it. Not a retreat from the original brief
— San Francisco's place names are largely survey names, so the surveys are the
substrate the names sit on. Work that proceeds from committed public data beats
work that waits.

**Method, 26 Aug.** **Multi-model commissioning is abandoned.** It produced zero
findings across two briefs. Hand retrieval produced every source this corpus
holds. `02-run-plan/handoff-prompt.md` and the two briefs in `01-brief/` are
**obsolete as dispatch payloads** and are kept as the question list a retrieval
pass answers.

## What exists

| | state |
|---|---|
| `04-normalized/geo/` | TIGER 2025: 3,701 named streets, 46 water features, city-wide, PDDL/public domain, checksummed sidecar. Plus 41 DataSF analysis-neighbourhood polygons, own sidecar |
| `05-analysis/survey-grid-measurement.md` | O'Farrell's 1847 module measured from centrelines to 2.84 ft RMS. First claim here corroborated by measurement rather than a second document |
| `05-analysis/grid-classification.md` | Seven survey grids, and what the classification does not claim |
| `06-viewer/index.html` | **Seven Grids** — live at <https://www.dhk.io/work/seven-grids> |
| `06-viewer/timeline.html` | **Twenty-One Years** — built and committed, *not* on dhk.io yet |
| `04-normalized/sources/` | manifest + a `.gitignore` that makes committing a corpus impossible. Empty until documents are fetched on lobster |
| place names | ~20 SoMa entries from one probe, 3 conflicts unadjudicated |

Both viewers are derived: edit `06-viewer/*template.html`, run
`python3 06-viewer/build.py`, commit the result. `scripts/validate.py` runs
`build.py --check` and fails on a stale page.

## The neighbourhood boundaries, and what they cost to get

**Closed, 27 Aug.** `04-normalized/geo/neighborhoods.geojson` holds 41
MultiPolygons, city-wide, PDDL, with its own checksummed sidecar. It is the
modern frame a city-wide neighbourhood map hangs on.

Worth knowing why it took two sessions. The script pointed at DataSF dataset
`p5b7-5n3h`, which is named "Analysis Neighborhoods" and reports
`count(*) = 41` — the right name and the right count, arriving with **no data
and no error**. It is not a dataset: it is a saved canvas map *view*, with an
empty `columns` array, a `/resource` endpoint serving the single row `[{}]`, and
a 53-byte empty `FeatureCollection`. Every request returned 200.

The tell was `--probe` printing *no columns at all*. The polygons live in the
view's `modifyingViewUid`, `j2bu-swwd`, with columns `nhood` and `the_geom`.
Both ids are in the script, with the trap written out beside them.

Add it to the list below: **a plausible name and a correct row count are not
evidence that you fetched anything.**

## What to build, in order

1. **`quote.py`** — search the local extractions for a phrase, return the passage
   with printed and PDF page and a formed citation. This is what makes writing
   entries fast enough to be worth doing.
   `acquire-documents.py` is **built** and is what feeds it: it fetches,
   checksums, extracts, settles the page offset and records provenance. It
   proposes an offset from the footers but will not record one without
   `--offset`, because a wrong offset poisons every citation while looking
   correct. `--selftest` proves the detector without touching the network.
2. **Prose to polygon** — a bounding description plus the committed centrelines,
   producing a polygon and a precision marker. The intersection solver in
   `05-analysis/measure-grid.py` is already half of it. Without this, extents
   stay hand-drawn and cannot grow past what one person can draw.

Open issues that matter: [#82](https://github.com/dhk/alexandria/issues/82)
dossiers, [#78](https://github.com/dhk/alexandria/issues/78) street-name
provenance, [#79](https://github.com/dhk/alexandria/issues/79) network over
time, [#73](https://github.com/dhk/alexandria/issues/73) the bronze deposit.

## Things that will bite you

Each of these cost real time. None is obvious.

**Git on lobster: `git fetch && git reset --hard origin/<branch>`, never `git
pull`.** The working branch is restarted from `main` after every squash-merge
and force-pushed, so its history is rewritten regularly and `pull` correctly
refuses to fast-forward. Nothing originates on lobster that is not pushed
immediately, so a reset loses nothing. This has already cost one confused
session.

**Printed page numbers are not PDF page numbers.** On the Page & Turnbull
statement the printed number runs **two behind** the PDF index. Cite both:
`printed p.18 (PDF p.20)`. Establish the offset per document by reading footers
on several pages — never assume it.

**TIGER's road classes are federal-functional, not urban-arterial.** `S1100` is
limited-access freeway, `S1200` is US/state highway. Market, Mission, Geary and
Clement are all `S1400`. A city-wide filter of `S1100`+`S1200` returned **64
features while the SoMa pilot returned 326** — a subset larger than its
superset, which is how the bug announced itself. Requiring a *name* is the whole
filter.

**Street names are not unique city-wide.** There is a second `1st St` on
Treasure Island. Bound every name lookup by a box. `1st St`'s geometry is also
fragmentary enough to produce a spurious `1st St` × `Bryant St` intersection
**246 m** out of place.

**A survey grid is two orthogonal families**, so a bearing must be tested against
both `θ` and `θ+90`. Testing only `θ` keeps the along-family, throws every cross
street into "ungridded", and still draws a plausible map whose shares sum to
100%. It took ungridded from 33% to 70% and shipped once before being caught.

**The Artifact and dhk.io design systems disagree, correctly.** A published
Artifact must be theme-aware; dhk.io has no dark theme and its linter fails on a
`prefers-color-scheme` query. The site's copy is derived, so
`sync-study.mjs` strips dark rules and then *checks* no `var()` is left
dangling. Do not resolve this by making the source single-theme.

**`geo/sources.json` merges on `(extent, layer)` and rewrites its own top-level
note.** A second writer sharing that file clobbers it. Neighbourhoods get their
own sidecar for exactly this reason.

## The discipline this project actually runs on

Every one of the bugs above **looked right**. The freeway filter produced a map.
The one-family grid test produced a map with shares summing to 100%. The
duplicated JSON island produced a working page at twice the size. None was
caught by looking; each was caught by something mechanical that printed a number
and by that number being compared against a prediction made beforehand.

So: **say what you expect before you run it.** "Expect roughly 3,678 road
features, a couple of MB. If it lands wildly off that, something else is wrong."
That sentence is what caught the filter bug.

And mark every claim `FETCHED` / `SEARCH-SUMMARY` / `RECALLED`. `RECALLED` is
not an admission of weakness — it is what lets an unverified claim sit beside a
measured one without contaminating it. `AGENTS.md` rule 11: verify the claim
before you make it.

## What is not in this repository

Ten SF Planning text extractions — the SoMa context statement, Central SoMa EIR,
Japantown, Market & Octavia, Mission, North Beach, Parkside, Corbett Heights,
and the modern context statement — exist only in a previous session's scratch
directory. **Their provenance was never recorded**, which is exactly the gap
`acquire-documents.py` closes. Re-fetching them through that script is the first
real job for the new pipeline, and it converts nine ad-hoc downloads into a
manifest.

They are also why the method decision pays. Corbett Heights alone names dozens
of dated, bounded plats — the **Eureka Homestead Association of 1864** ("bound
by Seventeenth and Twentieth, Noe and Douglass Streets"), the **Market Street
Homestead Association of 1868** — each one a plat that would fill the space
between the three city-scale surveys on the timeline. A bulk extraction returned
131 named plats with 47 carrying a nearby year, and **none of it is trustworthy**:
the heuristic was "nearest four-digit year", which returned a man's birth year as
a plat date. Turning that into evidence is reading, one sentence at a time.
