# Commission web surface

The local web surface is the first executable path through RFC-0005: inputs and a
verbatim brief, a priced Review gate, independent OpenRouter dispatch, and a
persisted Result that distinguishes silence (`—`) from a failed call (`✕`).

## Configure

Alexandria resolves `OPENROUTER_API_KEY` from the process environment first. If it
is absent, it reads the key from:

```text
~/.config/alexandria/secrets.env
```

The file is ordinary environment-file syntax:

```text
OPENROUTER_API_KEY=...
```

Set `ALEXANDRIA_SECRETS_FILE` to use another path. The key never enters a draft,
run artifact, log message, or browser response.

## Run locally

```bash
uv sync
uv run alexandria-web
```

Open <http://127.0.0.1:8042>. The default bind is loopback only.

Drafts and runs live under `ALEXANDRIA_DATA_DIR`, or the platform user-data
directory when that variable is absent. Drafts are local scratch state. A run is
stored as an immutable directory after dispatch:

```text
runs/<run-id>/
├── run.json
├── brief.md
├── inputs/original/<sha256>.<ext>
├── inputs/extracted/<sha256>.txt
├── raw/<model>.json
├── raw/grading.json
├── claims.json
├── scores.csv
├── report.md
└── manifest.json
```

Actual per-call cost is read from the OpenRouter response's aggregator `usage.cost`
field. No vendor price table is committed. Review fetches the live Models API; if
that fetch fails, the page states that the estimate is unavailable and leaves the
provider-side key limit as the active ceiling.

The Result screen reads those immutable run artifacts through five views: Claim
landscape, Heatmap document, Report, Raw outputs, and Provenance. The Heatmap
document color-codes canonical claim blocks by their assigned group and exposes
each model's score and evidence cell. It deliberately does not color arbitrary
report prose because the current artifacts do not record exact claim-to-prose
spans. Report renders `report.md` as safe Markdown beside an artifact card; the
operator can copy the source Markdown or download the complete run directory as a
ZIP bundle. That ZIP adds self-contained `report.html` and `heatmap.html` readers,
an executable `open-report.py`, and human instructions alongside the unchanged run
artifacts, so a recipient can read either output without an Alexandria server. The
readers remain explicitly subordinate to the graded claims and raw evidence.

## Inputs

- Paste is retained verbatim as Markdown.
- Uploads accept PDF, HTML, text, and Markdown.
- GitHub resolution accepts HTTPS repository, issue, pull-request, and blob URLs.
- Repository and PR resolution selects up to eight brief-like supported files,
  prioritizing README, brief, design, research, and RFC paths.
- Limits are eight inputs, 20 MB of original bytes, and 400,000 extracted
  characters.
- PDF extraction uses `pypdf`; empty scanned pages are surfaced as warnings. OCR
  is not performed.

## Current boundary

This slice is synchronous: the browser waits while calls finish. It has no cancel,
retry, background worker, or draft-resume UI yet. Claim canonicalization and the
grading-failure surface remain provisional design questions. Runs are local
directory records rather than committed research artifacts until the repository
placement decision is made explicitly.
