# Alexandria Design

Alexandria is version control for research.

Its purpose is not merely to generate reports. It is to make research durable, inspectable, reproducible, and governable across people, models, tools, and time.

## Design thesis

Research should be treated as an engineering discipline. Briefs, prompts, source records, model outputs, claims, analyses, reviews, and publications are first-class artifacts. Each artifact has a lifecycle, provenance, and review history.

## Core principles

1. **Artifacts are primary.** Conversations are transient; reviewed artifacts endure.
2. **Evidence is preserved.** Raw inputs and model outputs are not silently rewritten after merge.
3. **Provenance is mandatory.** Conclusions should be traceable to sources, prompts, runs, models, and reviewers.
4. **Claims are reviewable units.** Synthesis should not obscure which evidence supports which proposition.
5. **Model disagreement is information.** Agreement is not automatically truth, and disagreement should be analyzed rather than averaged away.
6. **Human judgment is explicit.** Approval, adjudication, and unresolved uncertainty must be visible.
7. **Research is reproducible.** A future reviewer should be able to reconstruct how a conclusion was reached.

## System boundaries

The Git repository is the durable system of record. Provider adapters, orchestration services, user interfaces, and analysis engines are replaceable components around it.

Alexandria should avoid rebuilding commodity capabilities when existing tools can satisfy them. The first research project will test this assumption directly and identify where a thin integration layer is preferable to a new platform.

## Research assurance

Bronze, Silver, and Gold describe increasingly rigorous research processes. They are cumulative process requirements, not labels of factual certainty.

- **Bronze:** exploratory mapping and uncertainty identification.
- **Silver:** decision-support research with broader coverage, source auditing, and independent review.
- **Gold:** claim-level verification, adversarial testing, source-lineage review, and expert approval.

## Governance

All substantive changes are made on branches and merged through pull requests. Structural and methodological changes require the same review discipline as research outputs.
