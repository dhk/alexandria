# Acquiring modern geometry

[`acquire-geo.py`](acquire-geo.py) pulls street and boundary geometry from
Overture Maps' public S3 bucket, clips it to San Francisco, thins it, and
writes it to `04-normalized/geo/` with a provenance sidecar.

## Run it where the network is open

A session container reaches S3 and GitHub and very little else. That is enough
to *list* Overture releases but not to query them: DuckDB has to fetch its
`httpfs` extension, and `extensions.duckdb.org` is blocked —

```
HTTP Error: Failed to download extension "httpfs" at URL
"http://extensions.duckdb.org/v1.5.5/linux_amd64/httpfs.duckdb_extension.gz" (HTTP 403)
```

So acquisition runs on lobster, which has open egress and holds the corpus
checkout. The derived GeoJSON and its sidecar are committed; the download is
not repeated by readers.

```bash
cd ~/src/alexandria-corpus/research/2026-08-21-sf-downtown-place-names/02-run-plan

uv run --no-project --with duckdb python acquire-geo.py --list-releases
uv run --no-project --with duckdb python acquire-geo.py --dry-run          # prints SQL, fetches nothing
uv run --no-project --with duckdb python acquire-geo.py                    # all of San Francisco
uv run --no-project --with duckdb python acquire-geo.py --extent soma      # the pilot only
```

`--dry-run` and `--list-releases` work anywhere, including a container; they
need S3 and nothing else.

## Extents

| `--extent` | Covers | Road classes |
|---|---|---|
| `city` *(default)* | The peninsula plus Treasure Island | through-network only: motorway, trunk, primary, secondary, tertiary |
| `soma` | The downtown/SoMa pilot | the full local grid, down to `living_street` |

Both boxes are hand-chosen and approximate. **They bound a download and assert
no extent** — never cite one as a boundary. The `city` box deliberately omits
the Farallon Islands: legally part of the City and County, 27 miles out, and
nothing but ocean in between.

The class split is the reason city-wide is usable at all. Every residential
street in San Francisco is far more geometry than one page should carry, so
the wide extent keeps the through-network and the pilot keeps the local grid —
which is what the place-name boundaries are actually described in terms of
("bounded by Market, Howard, 1st, and 2nd streets").

The script warns when any layer exceeds 12 MB, because a published artifact
caps at 16 MB in total and the historical layers need room too.

## Licence — decide this before publishing

Overture's `transportation` and `divisions` themes derive from OpenStreetMap
and are **ODbL 1.0**. That obliges attribution and carries share-alike onto a
derived database. The sidecar records the obligation per layer so it travels
with the data instead of living in someone's memory, and any surface showing
this geometry needs "© OpenStreetMap contributors, via Overture Maps
Foundation" visible.

If that is unwelcome — for a page meant to be shown off without a licence
footnote — the alternative is **Census TIGER/Line**, which is a work of the US
federal government and therefore public domain, with no attribution
obligation and no share-alike. It is coarser than Overture and lacks the
richer attributes, but for a street basemap under historical polygons that
hardly matters. `census.gov` is blocked from a container but reachable from
lobster, so the choice costs nothing operationally.

**Recommendation:** TIGER for anything published publicly, Overture when the
extra attributes earn their licence. This script does Overture today; adding a
TIGER source is small if that is the call.

## What the sidecar records

`04-normalized/geo/sources.json`, one entry per layer, re-runnable without
losing entries for other extents:

- the `s3://` and `https://` source, and the Overture release
- retrieval timestamp in UTC
- feature count, byte size, and a sha256 of the written file
- licence and required attribution
- the extent and road-class filter that produced it
- `FETCHED`, the same marker the textual evidence uses

Same standard as a quoted page: a reader can tell where it came from, when,
under what terms, and whether the bytes still match.
