# Alexandria

**The research corpus: a git-backed, auditable record of multi-model research — briefs, raw model outputs, comparative analysis, synthesis, and publication.**

Alexandria treats this repository as the durable system of record for research. The tooling that produces these artifacts — the MCP server, commission dispatch, and deploy machinery — now lives separately in [dhk/minority-report](https://github.com/dhk/minority-report), so models and orchestration logic can keep changing without touching this repo's evidence trail or its history. See [issue #33](https://github.com/dhk/alexandria/issues/33) for the split.

## What this corpus records

1. A defined research topic.
2. A drafted and approved research brief.
3. The brief dispatched to multiple model families and research modes.
4. Prompts, inputs, raw outputs, citations, errors, and execution metadata, preserved as received.
5. Normalized outputs, without changing the raw evidence.
6. Findings, disagreements, omissions, and unusual outliers, compared.
7. A traceable synthesis.
8. Review and publication through Git branches and pull requests.

Producing steps 1–7 is Minority Report's job, dispatched against briefs that live here. This repo is where the result — and the trail behind it — is kept.

## Architecture

### System flow

![How Alexandria works: operator surfaces feed an explicit review gate, independent model research, grading, immutable local run artifacts, and a separate Git research system of record.](docs/assets/alexandria-architecture.svg)

The review gate is the boundary before model spend. Completed commission runs
remain immutable local records; promotion into this repository is deliberate
rather than automatic. (The "operator surfaces" and dispatch machinery this
diagram shows now live in
[dhk/minority-report](https://github.com/dhk/minority-report); this diagram
predates the split and hasn't been redrawn yet.)

### Model comparison and synthesis

![How Alexandria dispatches one approved brief to independent models, preserves their raw responses, blindly grades claims, and presents consensus, disagreement, novelty, thin coverage, and silence.](docs/assets/alexandria-model-synthesis.svg)

Every research model receives the same brief and inputs without seeing another
model's answer. The dispatching tool preserves those answers, grades the union
of material claims, and produces a report plus a claim landscape that keeps
disagreement, silence, and failure visibly distinct — the artifact this
repository then holds.

## Research assurance levels

Alexandria supports three cumulative levels:

- **Bronze — exploratory:** fast multi-model mapping of a topic and its main uncertainties.
- **Silver — decision-support:** broader provider coverage, source auditing, targeted follow-up, and independent review.
- **Gold — high assurance:** claim-level verification, adversarial analysis, source-lineage review, and expert approval.

A level describes the strength of the research process. It does not guarantee that a proposition is true.

## Core rules

- The repository is the system of record.
- All substantive work is performed on a branch and reviewed through a pull request.
- Raw model outputs are immutable after merge.
- Derived analyses declare their exact inputs.
- Agreement among models is not treated as independent verification.
- Published conclusions must be traceable to claims, sources, runs, prompts, and the approved brief.
- Human approval is required at consequential research boundaries.

## Repository map

```text
.github/       Issue, pull-request, and validation workflows
docs/          Architecture and operating rules
docs/ux/       Published user-interface specifications and prototypes
policies/      Bronze, Silver, and Gold assurance policies
schemas/       Machine-readable artifact contracts
prompts/       Versioned model instructions
research/      Individual investigations
scripts/       Validation of tracked research/documentation artifacts
generated/     Rebuildable indexes and reports
```

The tooling that used to live in `src/`, `deploy/`, `templates/mcp-server/`,
and `tests/` moved to [dhk/minority-report](https://github.com/dhk/minority-report).

## Using the tooling against this corpus

Point [dhk/minority-report](https://github.com/dhk/minority-report)'s
`ALEXANDRIA_REPO` at a checkout of this repository:

```bash
export ALEXANDRIA_REPO=/path/to/this/checkout
```

See that repo's README for running the MCP server, the commission web
surface, and the deploy/packaging tooling.

Each investigation follows a standard lifecycle:

```text
research/<date>-<slug>/
├── topic.yaml
├── README.md
├── 00-topic/
├── 01-brief/
├── 02-run-plan/
├── 03-runs/
├── 04-normalized/
├── 05-analysis/
├── 06-synthesis/
├── 07-review/
└── 08-published/
```

## Status

Alexandria's corpus structure supports read/status recall and a guarded
commission-and-publish path via the Minority Report tooling. The published
UX contract still describes work beyond this first vertical slice.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md). The design is described in [docs/DESIGN.md](docs/DESIGN.md).
