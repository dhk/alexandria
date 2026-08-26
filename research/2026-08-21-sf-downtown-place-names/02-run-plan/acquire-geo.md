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

| `--extent` | Covers | Road classes |
|---|---|---|
| `city` *(default)* | Peninsula plus Treasure Island | `S1100`, `S1200`, `S1400` |
| `soma` | The downtown pilot | adds `S1730` alleys |

**TIGER's road classes are federal-functional, not urban-arterial**, and this is
the trap. `S1100` is limited-access freeway; `S1200` is US and state highway.
Almost every street in San Francisco — Geary, Mission, Market, Clement — is
`S1400`, "Local Neighborhood Road." A city-wide filter of `S1100` plus `S1200`
returns the freeways and little else.

Found the hard way: that filter returned **64 features city-wide while the SoMa
pilot returned 326** — a subset larger than its superset, which is the signal
that a filter is wrong rather than merely tight. Run `--report` before trusting
any class filter:

```bash
uv run --no-project --with pyshp python acquire-geo.py --report
```

It fetches the roads file, clips to the extent, and prints a histogram of MTFCC
codes with how many carry a name — the numbers a tier decision should be made
on rather than guessed at.

The alleys are not a detail. Minna, Natoma, Russ, Shipley and Tehama are named
in the 2009 context statement, and the place-name boundaries are described in
terms of this grid — "bounded by Market, Howard, 1st, and 2nd streets" needs
1st and 2nd to exist. City-wide drops them because every local street in San
Francisco is far more geometry than one page should carry; the script warns
past 12 MB per layer, since a published artifact caps at 16 MB in total and the
historical layers need the rest.

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
