# O'Farrell's module, measured from federal centrelines

**Status:** analysis, single-analyst, not graded. Reproducible from this
repository — `python3 measure-grid.py`, stdlib only, no network.
**Inputs:** `04-normalized/geo/city-roads.geojson` (TIGER 2025, public domain,
`FETCHED` — see the sidecar for URL, sha256 and retrieval time).

## The claim being tested

Page & Turnbull, *Historic Context Statement, South of the Market Area*
(30 June 2009), printed p.18 / PDF p.20 — `FETCHED`:

> From Yerba Buena Cove west to 1st Street, the street grid replicated the
> 50 Vara Survey north of Market Street but from 1st Street west to 5th
> Street, O'Farrell adhered to the larger blocks of the 100-Vara Survey.

And printed p.2 note 3 / PDF p.4 — `FETCHED`:

> The name "100 Vara Survey" was bestowed on the blocks south of Market
> because O'Farrell laid out each block as six equal lots measuring 100 varas
> square.

Both describe a survey. Neither gives a dimension in feet. Until now every
statement in this investigation rested on one document repeating another; this
is the first tested against independent physical measurement.

## Method

Street centrelines come from the committed TIGER extract. For each pair of
named streets the script solves for their single intersection, refusing the
answer when zero or more than one candidate survives — see *Data faults*, both
refusals matter. Centre-to-centre spacings are then measured between
consecutive cross streets, and between consecutive streets running into SoMa.

Two structural assumptions, both from the quotes above and nothing else:

- a **100-vara block** is six lots in a 3 × 2 array — `3L` along Market,
  `2L` deep, where `L` = 100 varas;
- a **50-vara block** is four lots in a 2 × 2 array, hence 100 varas square —
  `L` on a side.

That gives three predictions in two unknowns, `L` and the street width `s`:

| span | model |
|---|---|
| cross-street spacing east of 1st | `L + s` |
| cross-street spacing west of 1st | `3L + s` |
| depth from one SoMa street to the next | `2L + s` |

Sixteen measured spacings, two free parameters, ordinary least squares.
Nothing about feet, varas, or street widths is assumed — both fall out.

**Spacings are measured on Mission Street, not on Market.** Market is the seam
between two surveys, so a cross street's Market intersection is set by where
its *north*-of-Market counterpart lands. 3rd Street meets Market about 70 ft
off the SoMa grid, because north of Market it belongs to Kearny's line. Mission
is an interior street of the survey being measured. Market's own series is
printed as a diagnostic rather than dropped silently.

Market → Mission is held out of the fit for the same kind of reason: Market is
wider than an ordinary street, so it does not belong to the same model. It is
used afterwards, as a check.

## Result

```
100-vara lot L    =  274.93 ft     ->  1 vara = 32.991 in
street width s    =   83.30 ft
residual RMS      =    2.84 ft     max 7.49 ft

predicted east    =   358.2 ft     measured   358.1
predicted west    =   908.1 ft     measured   908.0
predicted depth   =   633.2 ft     measured   633.3
```

Three independent spans, each matching to about a tenth of a foot on the mean,
with a per-observation scatter under three feet across a survey laid out in
1847 and rebuilt after 1906.

Then the held-out check. Market → Mission measures 650 ft. With the block depth
and street width above, an ordinary street there would give 633 ft. The excess
implies **Market Street is 117 ft wide**. O'Farrell's Market Street is
described as 120 feet — the same figure this investigation's own chronology
carries for 1847. That number was not used to obtain any of the parameters.

**What is established:** the survey seam is at 1st Street exactly, as Page &
Turnbull say — 362 ft on the last span east of it, 903 ft on the first span
west. The 3 : 2 block proportion is confirmed. The module continues unchanged
through 6th Street, one block further than their sentence claims — an extension
of the source, not a contradiction of it.

## What the ruler can and cannot settle

The vara does not resolve.

| standard | implied `L` | distance from the fit |
|---|---:|---:|
| 33 in — the figure Page & Turnbull give | 275.0 ft | 0.03 RMS |
| 33⅓ in — a standard elsewhere in Spanish and Mexican survey practice (`RECALLED`, unverified) | 277.8 ft | 1.00 RMS |

The measurement leans hard toward 33 inches. It does not exclude 33⅓, and the
reason is not the survey — it is the ruler:

- distances here come from a **local flat-earth approximation**, constants in
  the script's docstring, not a geodetic computation on the GRS80 ellipsoid;
- a **0.5% scale error moves `L` by 1.4 ft**, half the gap between the two
  candidate varas;
- TIGER is **NAD83 (EPSG:4269)**, used throughout this investigation as WGS84
  for display — sub-metre at this scale, and stated rather than assumed, but
  not nothing when the question is a 2.8 ft difference;
- the geometry is **modern**. It records where the streets are now, after the
  1906 fire, the fills, and every resurvey since. That it still yields the
  1847 module to within three feet is the finding; it is not evidence about
  where any 1847 monument stood.

Settling the vara means replacing the ruler first. Until someone does, this
measurement constrains the module and reports a preference about the vara.

## Measurement standards are themselves historical

The vara is not an awkward edge case. It is the general problem in miniature,
and this corpus currently has no way to record it.

Every extent in the gazetteer is ultimately a number attached to a standard,
and the standards move:

- **Units get redefined.** The vara above is one instance. The US survey foot
  and the international foot differ by 2 ppm and the survey foot was retired in
  the United States at the end of 2022 (`RECALLED`, unverified) — over a
  city-sized span that is centimetres, but a boundary described in one and
  measured in the other is a boundary that has moved on paper and not on the
  ground.
- **Datums get replaced.** NAD27 → NAD83 → NAD83(2011), with NATRF2022 in
  progress (`RECALLED`, unverified). The same physical corner has different
  coordinates in each, differing by tens of metres between the first two. A
  polygon digitised from a map georeferenced in one datum and overlaid on data
  in another disagrees with itself for no historical reason at all.
- **Surveys get corrected.** This investigation's own spine is corrections: the
  Van Ness Ordinance of 1855 and its 1856 map, Potter & Humphrey's survey of
  18 May 1868. A resurvey that moves a line is a historical event about the
  line, not an error in the record of it.
- **Monuments are lost.** A description anchored to a marker that no longer
  exists cannot be re-measured, only re-derived — and two people re-deriving it
  will not agree.

So a disagreement between two extents has at least two different causes, and
the corpus cannot currently tell them apart:

> **They disagree about the world** — two sources genuinely put a boundary in
> different places. This is what the conflict register is for, and three such
> conflicts are already recorded, all unadjudicated.
>
> **They disagree about the ruler** — same boundary, different unit, datum,
> survey epoch, or projection. This is not a conflict about San Francisco. It
> is a units problem wearing a conflict's clothes, and filing it in the
> conflict register would corrupt the register.

### Proposed: a `frame` block on anything carrying a measurement

Alongside `basis` (what kind of authority the extent rests on) and `prec` (how
sharply it can be drawn), a third axis — what it was measured *with*:

```yaml
frame:
  unit: vara
  unit_definition: "33 in, per Page & Turnbull 2009 p.2 n.3"   # FETCHED
  unit_alternatives: ["33 1/3 in"]        # RECALLED, unverified — see above
  datum: NAD83
  datum_note: "used as WGS84 for display; sub-metre at this scale"
  survey: "O'Farrell 1847"
  survey_superseded_by: ["Van Ness Ordinance 1855", "Potter & Humphrey 1868"]
  epoch: modern                            # geometry as it stands today
  monument: none                           # no surviving physical reference
```

Two rules make it earn its place:

1. **Two extents may only be compared when their frames are stated.** A
   comparison across differing frames is reported as *frame-divergent* and does
   not enter the conflict register until the frames are reconciled.
2. **A frame with an unresolved `unit_alternatives` bounds the precision of
   anything derived from it.** The 33 vs 33⅓ ambiguity is a ±1.4 ft floor on
   every vara-derived dimension in this corpus, and the map should not draw a
   line crisper than its frame allows.

Rule 2 is the same principle the viewer already implements as *shape encodes
precision*, pushed back one level — from how a place was described to what it
was described with. `unknown` blurs, `corridor` strokes, `exact` draws hard;
what the frame does is decide whether `exact` was ever available.

This is a proposal, not a schema change. Nothing in `04-normalized/` carries a
`frame` yet, and adopting one means revisiting every extent already recorded.

## Data faults found

Both are relevant to the street-name provenance map filed separately, and both
are properties of the source data rather than of this analysis.

- **Street names are not unique city-wide.** There is a second `1st St` on
  Treasure Island. Any lookup keyed on name alone conflates them; every lookup
  in `measure-grid.py` is bounded by a box for this reason.
- **1st Street's geometry is fragmentary.** Its named segments do not connect
  across Harrison, and a disconnected stub near the Embarcadero produces a
  spurious `1st St` × `Bryant St` intersection **246 m** from where the grid
  puts it. Real 1st Street does not reach Bryant. The script refuses any pair
  yielding more than one candidate rather than taking the first.

Thirteen of the eighty intersections implied by the viewer's schematic grid do
not exist at all: Steuart never reaches Folsom, Fremont stops before Bryant.
The schematic was drawing corners that are not there.

## What this changes in the viewer

The plate's projection is a hand-laid `(u, v)` frame at `TH = 34°`. Market's
true bearing is 44.9°, and a single affine fit over 66 real intersections
leaves 27 m RMS. Split at 1st Street, the two halves fit at **2.7 m and 3.8 m**
— they were never one grid measured badly. Rebuilding the projection on the
two-grid fit is tracked separately.
