# License & dependency purpose-compatibility auditing — prior art and feasibility

Feature-scoping investigation, opened 2026-08-01. Assurance level:
**Bronze (exploratory)** — single-source, not yet multi-model.

## What this is

While designing a repo-documentation-standard tool, a feature idea came up:
audit a repo's dependencies against its own license *and* its apparent
purpose (SaaS, closed-source, OSS redistribution), flagging "poisonous"
dependencies — not just license-vs-license conflicts (the well-covered
case) but license-vs-purpose conflicts, which a first-pass lightweight
search suggests nobody automates today. This investigation exists to
pressure-test that "nobody does this" claim properly, and scope what a
real build would need, before deciding whether to spend on a deeper pass.

**Hard constraint that must survive any deeper research and any eventual
build**: this stays a detection/reporting tool only. It must never choose,
author, or edit a LICENSE file — see `topic.yaml`'s `notes` field.

## Read order

1. [`00-topic/source-material.md`](00-topic/source-material.md) — the
   feature idea and the lightweight (single-agent, free) research pass
   that prompted commissioning this brief, as given.
2. [`01-brief/brief.md`](01-brief/brief.md) — the research questions a
   deeper pass would answer, and how the comparison set was chosen.

Stages `02-run-plan` through `08-published` are intentionally absent —
this is a single-source Bronze pass, not a graded multi-model comparison.
A dispatch through Alexandria's own `begin_research`/`run_research`
commission flow would add independent model runs, a claim landscape, and
a synthesis stage, but that is a spend-gated action requiring the
operator's explicit confirmation and was not run here.

## Status

Single-source draft. Treat the lightweight pass in
`00-topic/source-material.md` as one model's fast research, not verified
consensus — worth a real Silver-level (multi-model, source-audited) pass
before committing build time, specifically to firm up claim 4 in the
source material ("this appears to be genuinely unclaimed territory"),
which is exactly the kind of claim that's cheap to assert and expensive
to get wrong.
