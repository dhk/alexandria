# Seven Grids — the browser viewer for this investigation

`index.html` is every named street in San Francisco, coloured by which of seven
survey grids laid it out, with a bearing rose, a per-grid legend, and the
measurements. One self-contained file — open it, no server, no build step to
read it.

Published: <https://claude.ai/code/artifact/08fa997f-d2fb-4f94-b5af-813ab3b7b78b>

## It is generated, and that is the point

`index.html` is **derived, not authored**. Edit `template.html` and rebuild:

```
python3 06-viewer/build.py            # write index.html
python3 06-viewer/build.py --check    # fail if the committed file is stale
python3 06-viewer/build.py --bare     # print the page without the html skeleton
```

`template.html` carries page content only — no doctype, no `<html>`, no `<head>`,
no `<body>` — because that is the shape a published Claude Artifact wants, where
the host supplies the skeleton. A file on disk needs the skeleton to be a
document, so `index.html` is written wrapped and `--bare` prints the unwrapped
form for an Artifact publish. One authored template, two derived shapes, neither
hand-maintained.

The wrapping is not cosmetic: `dhk-website`'s `scripts/sync-study.mjs` derives
its copy of this page by slicing `<body>` out of `index.html`, and cannot find
it in a fragment.

Every line on the page comes from `../04-normalized/geo/city-roads.geojson` and
`city-water.geojson` — committed, checksummed, public domain, with provenance in
`geo/sources.json`. `build.py` is stdlib-only and touches no network, so the page
is reproducible from this repository alone.

`scripts/validate.py` runs `build.py --check` on every pass, so a corrected
template and a stale `index.html` cannot both pass. An investigation that ships
its own `06-viewer/build.py` is checked by running it; one without falls through
to the matrix builder as before.

## What the page claims, and what it does not

It **classifies**. Each street is assigned to a survey grid by the direction it
runs. That says which survey drew a street.

It does **not measure**. It cannot tell you a grid's block module the way
`../05-analysis/measure-grid.py` measures O'Farrell's to 2.84 ft. The limits are
in [`../05-analysis/grid-classification.md`](../05-analysis/grid-classification.md)
and are also printed on the page itself, under *Hair on it*, because a reader
looking at seven confident colours deserves to know which parts are soft.

## Design

The page shares the house idiom with the SoMa place-name plate: Instrument
Serif display, Newsreader body, IBM Plex Mono for data, on the same toned-paper
and brass token set, with all three theme states (bare `:root`, the
`prefers-color-scheme` media query, and the `[data-theme]` stamp) defining the
complete palette rather than patching it.

The seven grid inks are drawn from hand-tinted survey plats — iron blue, madder,
verdigris, ochre, indigo, olive, plum — with the ungridded third in faint ink so
the holes read as absence rather than as an eighth category.
