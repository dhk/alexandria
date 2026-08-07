# Alexandria corpus design

Alexandria is version control for research: a durable, inspectable record that
survives changes in models, providers, orchestration, interfaces, and hosts.

## Boundary

Alexandria owns the corpus and the rules that make it trustworthy:

- lifecycle and directory conventions;
- briefs, source records, raw evidence, analyses, synthesis, and publications;
- schemas, assurance policy, provenance, corrections, and review governance.

[Minority Report](https://github.com/dhk/minority-report) owns all executable
behavior: dispatch, grading, provider adapters, local run storage, MCP/web
surfaces, packaging, deployment, and host operations. Its output is a candidate
for promotion, not automatically part of the corpus.

This separation is consequential: tooling can be upgraded or replaced without
rewriting the evidence trail, and a reviewed evidence record does not inherit the
security or lifecycle assumptions of the machine that produced it.

## Architecture

![Minority Report and other replaceable tools produce candidate artifacts; a human review and promotion boundary leads to Alexandria's governed corpus.](assets/alexandria-architecture.svg)

There is no repository recombination. Cross-repository contracts are links and
schemas, not copied authoritative manuals. Alexandria defines what a promoted
artifact means; Minority Report documents how its code produces and reads it.

## Artifact lifecycle

1. **Frame** the topic and record permitted sources.
2. **Approve** a versioned brief and, where used, a run plan.
3. **Capture** provider/model/prompt identity, execution metadata, failures, and
   raw responses without alteration.
4. **Normalize** into derived artifacts without replacing the source evidence.
5. **Analyze** claims, disagreement, silence, coverage, uncertainty, and limits.
6. **Synthesize** conclusions with explicit inputs and traceable provenance.
7. **Review** evidence, methods, rights, privacy, and unresolved uncertainty.
8. **Publish** an approved expression while retaining the trail behind it.

Not every investigation reaches every stage. Missing, abandoned, failed, and
superseded states must remain visible rather than being smoothed into completion.

## Integrity rules

- Git history and reviewed artifacts are the system of record.
- Raw evidence is immutable after merge; corrections are additive.
- Derived work declares its exact inputs and must not masquerade as evidence.
- A provider failure is an observation; graded silence is a different state.
- Model agreement is not independent factual verification.
- Human approval is explicit at spend, promotion, and publication boundaries.
- Claims of completeness, identity, or current status require a named check.

## Provenance and schemas

A reconstructable run identifies the approved brief revision and checksum,
inputs and transformations, provider and model, prompt/instructions, execution
time, tool and network access, raw-response checksum, failures, and derived
artifacts. Normative machine shapes live in `schemas/`; implementations consume
those contracts but do not define them by accident.

## Assurance and governance

Bronze, Silver, and Gold are cumulative process levels, not truth labels.
Structural, methodological, schema, policy, and publication changes receive the
same branch-and-review discipline as research output. Reviewers must consider
source rights, personal data, secrets, citation quality, provenance, and whether
new work makes an existing analysis stale.

The [documentation index](README.md) classifies current contracts, shared
boundaries, history, and research outputs. Operational documentation lives only
in Minority Report.
