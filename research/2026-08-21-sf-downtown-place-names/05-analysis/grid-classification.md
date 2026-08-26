# Seven grids: classifying San Francisco's streets by survey

**Status:** analysis, single-analyst, not graded. Reproducible —
`python3 ../06-viewer/build.py`, stdlib only, no network.
**Inputs:** `04-normalized/geo/city-roads.geojson` (TIGER 2025, public domain,
`FETCHED`).
**Output:** [`06-viewer/index.html`](../06-viewer/), published at
<https://claude.ai/code/artifact/08fa997f-d2fb-4f94-b5af-813ab3b7b78b>.

## The observation

Street bearings across San Francisco are not smoothly distributed. Folded to a
quarter-turn and weighted by length over 1,954 km of centreline, they pile into
seven sharp peaks. Each peak is geographically compact — plot it and it names
itself from the streets inside it.

| grid | bearing | length | share | survey |
|---|---:|---:|---:|---|
| Richmond & Sunset | 3.5° | 635.8 km | 31.6% | Potter & Humphrey, 18 May 1868 |
| Western Addition | 9.5° | 356.1 km | 17.7% | Van Ness Ordinance, 1855–56 |
| South of Market | 45.0° | 116.3 km | 5.8% | O'Farrell, 1847 |
| Bayview | 54.5° | 94.3 km | 4.7% | not established |
| Portola | 18.0° | 59.9 km | 3.0% | not established |
| Lakeside | 86.5° | 51.2 km | 2.5% | not established |
| Excelsior | 59.0° | 43.5 km | 2.2% | not established |
| **ungridded** | — | 657.2 km | 32.6% | none |

The top three are the three acts of this investigation's survey spine, and the
45° peak is the grid measured independently in
[`survey-grid-measurement.md`](survey-grid-measurement.md) — its bearing there,
fitted from 66 real intersections, came out at 44.92°.

## Method

Each street is assigned by a **length-weighted vote over its own segments**, so
one short jog cannot reclassify a long straight run. Segments under 8 m are
ignored: their bearings are noise.

A grid is **two orthogonal families** — the streets running along it and the
streets crossing it — so a bearing is tested against both `θ` and `θ + 90`.
This is worth stating because getting it wrong is not obvious from the output:
testing only `θ` keeps the along-family, throws the cross-family into
*ungridded*, and still produces a map that draws streets and shares that sum to
100%. It took ungridded from 33% to 70% and silently deleted half of every grid.
It shipped once before it was caught.

## What this is not

**It classifies; it does not measure.** It says which survey drew a street. It
does not give a grid's block module.

I tried. The obvious method — cluster by bearing, project the members onto the
perpendicular, read the spacing of the resulting comb of parallel streets —
**fails city-wide**, because clustering by *angle alone* has no spatial term:
two parallel grids in different neighbourhoods merge into one comb and the gaps
between them mean nothing. Run against South of Market, whose module is
independently known here to be 358 × 908 ft, it returns a broad multi-modal
distribution with a median near half the true value. The Sunset's family comes
out clean and unimodal only because it happens to be geographically isolated at
its bearing — which is luck, not method.

Fixing it needs spatial clustering: connected components over a
bearing-coloured raster, so a grid is a contiguous region as well as an angle.
Not done.

## Everything soft about it

- **The seven peaks are hand-chosen.** `3.5 9.5 45 54.5 18 86.5 59`, read off
  the histogram by eye rather than fitted. `TOL = 2.5°` is likewise chosen.
  Change either and the shares move.
- **Four grids are undated.** Bayview, Portola, Lakeside and the Excelsior are
  measured here and cited nowhere. No source in this corpus says when they were
  laid out, and inventing a year would be worse than the gap.
- **Four of the seven names are mine**, taken from the streets inside each
  region — described, not cited. The three dated ones carry the names their
  sources use.
- **"Ungridded" is a category, not an explanation.** A third of the city's
  street length sits there, and it holds at least three different things:
  deliberate curvilinear plats (Sea Cliff, St Francis Wood, Forest Hill), park
  and Presidio roads, and streets that simply bent to a hill. They are one
  colour because I have not separated them, not because they are one thing.
- **The ruler is the same flat-earth approximation** used in
  `survey-grid-measurement.md`, with the same caveat. It is fine for bearings
  and for drawing a city-sized page.

The page states all of this on its own face, under *Hair on it*. A reader
looking at seven confident colours should be able to see which parts are soft
without reading the repository.
