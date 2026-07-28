# Alexandria

**An open, auditable system for managing multi-model research—from brief creation and model dispatch through evidence capture, comparative analysis, synthesis, and publication.**

Alexandria treats a Git repository as the durable system of record for research. The orchestration harness is deliberately separate: models and tools may change, but the evidence trail, revisions, review decisions, and published conclusions remain visible.

## What Alexandria manages

1. Define a research topic.
2. Draft and approve a research brief.
3. Dispatch the brief to multiple model families and research modes.
4. Preserve prompts, inputs, raw outputs, citations, errors, and execution metadata.
5. Normalize outputs without changing the raw evidence.
6. Compare findings, disagreements, omissions, and unusual outliers.
7. Produce a traceable synthesis.
8. Review and publish through Git branches and pull requests.

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
templates/     Starting points for research artifacts
prompts/       Versioned model instructions
research/      Individual investigations
scripts/       Validation and repository utilities
tests/         Contract and provenance tests
generated/     Rebuildable indexes and reports
```

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

Alexandria is at the repository-contract stage. The first research project will test the proposition behind Alexandria itself: whether existing tools already provide most of this capability, whether this is genuinely useful white space, and which parts should be built rather than composed.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md). The design is described in [docs/DESIGN.md](docs/DESIGN.md).
