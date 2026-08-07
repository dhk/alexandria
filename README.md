# Alexandria

Alexandria is the durable, git-backed corpus for multi-model research. It owns
briefs, source records, preserved evidence, analyses, synthesis, publication,
schemas, policy, provenance, and research governance.

[Minority Report](https://github.com/dhk/minority-report) is the separate
executable system that operates on this corpus: provider adapters, commission
orchestration, MCP and web surfaces, packaging, deployment, and host operations.

## Why the split matters

Research tooling is replaceable; the evidence trail is not. Providers, models,
interfaces, and deployment machinery can change in Minority Report without
rewriting Alexandria's reviewed artifacts or their Git history. Conversely, a
corpus contract can be reviewed here without importing host-specific concerns.

## Architecture

![Two-repository architecture: Minority Report produces candidate artifacts through an explicit review boundary; Alexandria preserves the reviewed corpus and its governance.](docs/assets/alexandria-architecture.svg)

The arrow into Alexandria is a deliberate promotion and review step, not an
automatic write. A successful local run is not yet a reviewed corpus artifact.

## Repository map

```text
docs/          Corpus design, contracts, governance, and historical pointers
schemas/       Machine-readable artifact contracts
research/      Reviewed investigations and their evidence lifecycle
generated/     Rebuildable indexes derived from reviewed artifacts
scripts/       Corpus validation
```

Start with the durable [documentation index](docs/README.md) and
[corpus design](docs/DESIGN.md).

## Clone, configure, and validate

Alexandria has no product installation step:

```bash
git clone https://github.com/dhk/alexandria.git
cd alexandria
uv sync --frozen
uv run --frozen python scripts/validate.py
```

To use the executable tooling, clone Minority Report separately and point its
`ALEXANDRIA_REPO` setting at this checkout. Do not point it at a packaged release
or at Minority Report's own checkout.

## Research lifecycle

```text
research/<date>-<slug>/
├── topic.yaml
├── README.md
├── 00-topic/       source framing
├── 01-brief/       reviewed question and constraints
├── 02-run-plan/    intended models, modes, and budgets
├── 03-runs/        preserved responses and execution metadata
├── 04-normalized/  derived, non-destructive normalization
├── 05-analysis/    claims, comparison, and limitations
├── 06-synthesis/   traceable conclusions
├── 07-review/      human review and adjudication
└── 08-published/   approved expression
```

Raw evidence is immutable after merge. Corrections and superseding work are new,
linked artifacts. Model agreement is evidence of convergence, not factual proof.

## Public data handling

Only commit material that may be public. Record source identity, retrieval date,
rights or license constraints, and transformations where applicable. Minimize or
redact personal data before promotion. Never commit credentials, capability URLs,
private research inputs, local run records, hidden reasoning, private host details,
or copyrighted source corpora without permission. Preserve useful excerpts and
citations only when their use is authorized and proportionate.

See [CONTRIBUTING.md](CONTRIBUTING.md) for ownership routing and review rules.

## Status

The repository split is implemented and both repositories have independent
validation paths. The complete live provider-to-publication workflow has not been
verified end to end on an operator host; do not infer operational readiness from
corpus validation or unit tests alone.
