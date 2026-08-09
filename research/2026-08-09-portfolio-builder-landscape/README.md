# Portfolio-website brand-interview pipeline — market scan and build vs. buy

Feature-scoping investigation, opened 2026-08-09. Assurance level:
**Bronze (exploratory)** — single-source, not yet multi-model.

## What this is

The operator is scoping a five-step portfolio-website product — a
brand-discovery interview seeded from a resume and LinkedIn profile,
follow-up questions, an audience definition, a traceable palette/layout
proposal, and a build step. This investigation exists to map what
already exists across that pipeline, verify whether any product chains
all five steps, and pressure-test a draft build-vs-buy recommendation,
with sourced, falsifiable claims rather than a single unstructured
writeup.

It also documents, deliberately, a failure: dispatching this
investigation through Alexandria's own multi-model commission flow was
attempted three times and did not work. See
[dhk/minority-report#33](https://github.com/dhk/minority-report/issues/33).

## Read order

1. [`00-topic/source-material.md`](00-topic/source-material.md) — the
   operator's requests, verbatim, across three follow-ups in the same
   working session.
2. [`01-brief/brief.md`](01-brief/brief.md) — the research questions this
   investigation answers (Q1, first pass; Q2–Q6, verification pass), and
   how the comparison set was assembled.
3. [`03-runs/claude-2026-08-09/`](03-runs/claude-2026-08-09/) — the raw
   research pass: run metadata (provider, model, prompt, brief checksum,
   execution time, tool access, and the three failed commission-dispatch
   attempts) and the unedited findings output.
4. [`05-analysis/analysis.md`](05-analysis/analysis.md) — interpretation:
   whether the build-vs-buy recommendation holds up, and the hard
   constraint it gains (never scrape LinkedIn; require user-supplied
   input). Kept separate from the raw run per `AGENTS.md` rule 7 ("keep
   generated interpretation separate from source evidence").

Stages `02-run-plan`, `04-normalized`, `06-synthesis`, `07-review`, and
`08-published` are intentionally absent — this is a single-source Bronze
pass, not a graded multi-model comparison. A dispatch through Alexandria's
own `begin_research`/`run_research` commission flow would add independent
model runs, a claim landscape, and a synthesis stage, and was attempted
here three times toward exactly that; all three attempts failed
client-side before any model was reached. See
`03-runs/claude-2026-08-09/run-metadata.yaml` for the detail and
[dhk/minority-report#33](https://github.com/dhk/minority-report/issues/33)
for the tracked fix.

## Status

Single-source draft. Treat `05-analysis/analysis.md`'s claims as one
model's research, not verified consensus — `AGENTS.md`'s "do not treat
model agreement as factual validation" cuts the other way too: with only
one source, there is no agreement to lean on at all.

The hard constraint in `05-analysis/analysis.md` (never scrape LinkedIn;
require user-supplied input) is a product decision, not a research
finding under review — it's recorded here because it was reached in the
course of this investigation and should travel with it, but it doesn't
carry the same "single-source, unverified" caveat as the market-scan
claims around it.
