# Acquiring modern geometry

[`acquire-geo.py`](acquire-geo.py) downloads Census TIGER/Line geometry for San
Francisco, clips it, thins it, and writes GeoJSON plus a provenance sidecar to
`04-normalized/geo/`.

## Why TIGER, and why it is the default

This repository is MIT. **MIT is a software licence and cannot relicense
somebody else's data**, so whatever geometry gets committed here has to be
compatible with that file or the file becomes untrue.

TIGER/Line is produced by the U.S. Census Bureau, so it is a work of the
federal government and **public domain** under 17 U.S.C. §105. No licence, no
attribution obligation, no share-alike. MIT stays accurate across every file.

Overture Maps is better data — richer attributes, cleaner geometry — and its
`transportation` and `divisions` themes derive from OpenStreetMap and carry
**ODbL**. ODbL separates a *Produced Work* (a rendered map image, which may
carry any licence given attribution) from a *Derivative Database* (which must
itself be ODbL). A committed `.geojson` extract is unambiguously the second.
Using it would mean an MIT repository containing ODbL files, attribution
required on every surface including dhk.io, and — the part that actually
matters — a live argument that place-name geometry georeferenced *against* it
is itself a derivative database. That would put ODbL on the research output,
which is the one thing here that is genuinely original.

`--source overture` therefore prints the reasoning and exits non-zero rather
than doing it quietly. If the trade is ever worth making, it should be made on
purpose.

Neither choice affects the historical evidence. The SF Planning documents are
quoted, cited and unchanged by any of this.

## Running it

Needs a host with open egress — lobster, not a session container, whose
allowlist reaches S3 and GitHub but not `census.gov`. The only dependency is
[pyshp](https://pypi.org/project/pyshp/), which is pure Python, so there is no
binary toolchain and no extension download to be blocked.

```bash
cd ~/src/alexandria-corpus/research/2026-08-21-sf-downtown-place-names/02-run-plan

uv run --no-project --with pyshp python acquire-geo.py --list-years
uv run --no-project --with pyshp python acquire-geo.py --dry-run     # prints URLs, fetches nothing
uv run --no-project --with pyshp python acquire-geo.py               # all of San Francisco
uv run --no-project --with pyshp python acquire-geo.py --extent soma # the pilot, with its alleys
```

`--dry-run` works anywhere. TIGER ships one file per county and San Francisco
is FIPS `06075`, so the download is already city-scoped; the bounding box only
trims.

## Layers and extents

| Layer | TIGER product | Gives |
|---|---|---|
| `roads` | `ROADS` | street centrelines with `FULLNAME` and an `MTFCC` class code |
| `water` | `AREAWATER` | water polygons — **today's shoreline as data**, replacing a hand-drawn curve |

| `--extent` | Covers |
|---|---|
| `city` *(default)* | Peninsula plus Treasure Island |
| `soma` | The downtown pilot |

**There is no class filter, and that is a finding rather than an oversight.**
`--report` on the real file gave this for the city box:

| MTFCC | total | named | |
|---|---:|---:|---|
| `S1400` | 3,715 | 3,593 | local street |
| `S1630` | 237 | **0** | ramp |
| `S1200` | 34 | 34 | secondary road |
| `S1100` | 30 | 30 | primary road |
| `S1730` | 24 | 21 | alley |
| others | 50 | 23 | walkways, private roads, census artefacts |

Every unnamed segment is noise — ramps and census-internal geometry, none of
which carry a name — so **requiring a name is the whole filter**. It takes
4,090 segments to 3,678 and loses nothing anyone could point at on a map,
which is the right rule for an atlas about street names. `--include-unnamed`
turns it off; `--mtfcc` still allows class filtering if a use ever needs it.

Two things this corrected, both worth recording because both were confidently
wrong beforehand:

- **TIGER's classes are federal-functional, not urban-arterial.** `S1100` is
  limited-access freeway and `S1200` is US or state highway. Geary, Mission,
  Market and Clement are all `S1400`. A city-wide filter of `S1100` plus
  `S1200` returned **64 features while the SoMa pilot returned 326** — a subset
  larger than its superset, which is the signal that a filter is wrong rather
  than merely tight.
- **Alleys are not `S1730`.** There are 24 of those in the entire city. Minna,
  Natoma, Russ, Shipley and Tehama — the alleys the place-name sources actually
  name — are coded `S1400` like everything else, so the pilot's alley tier was
  buying about two dozen features rather than the alley network.

Class tiering was also solving a size problem that does not exist. 3,678 named
segments is a couple of megabytes, against a 16 MB artifact ceiling.

Run `--report` before trusting any filter:

```bash
uv run --no-project --with pyshp python acquire-geo.py --report
```

Both boxes are hand-chosen and approximate. **They bound and trim a download
and assert no extent** — never cite one as a boundary. The `city` box omits the
Farallon Islands: legally part of the City and County, 27 miles out, nothing
but ocean in between.

## What the sidecar records

`04-normalized/geo/sources.json`, one entry per layer per extent, re-runnable
without dropping entries for the other extent:

- the source ZIP URL and its sha256 as fetched, plus the TIGER vintage
- retrieval timestamp in UTC
- feature count, byte size, and a sha256 of the written GeoJSON
- licence, and `attribution_required: false`
- the CRS note: TIGER is NAD83 (EPSG:4269), used here as WGS84 for display,
  a sub-metre difference at this scale and worth stating rather than assuming
- the `MTFCC` filter that produced it
- `FETCHED`, the same marker the textual evidence carries

Same standard as a quoted page: where it came from, when, under what terms, and
whether the bytes still match.
