# Analysis and recommendation

This interpretation is derived from the successful commission
`r-2026-0730-03`. It is separate from raw evidence and model-generated synthesis.

## Scope correction

This analysis addresses technical plausibility, not prior art. It does not determine
whether commercial products, open-source frameworks, or existing infrastructure
already implement the proposed system in whole or in part. The recommendation below
is therefore a hypothesis for landscape testing, not authorization to build.

## Recommendation

Build a **single-role, evidence-gated agent lifecycle** first. The initial system
should include a role contract, constrained tools, scheduled work orders, immutable
traces, structured human feedback, candidate skill revisions, held-out evaluation,
and tested suspension and offboarding. It should not initially include manager bots,
peer organizations, autonomous authority expansion, or persistent employment
identity across model upgrades.

## Why this is the narrowest credible test

All three research models judged the individual control mechanisms plausible while
treating the integrated organization as an unproven composition claim. They agreed
that a single governed agent may capture most of the proposed value with much less
coordination cost. They also agreed that multi-agent overhead is a binding empirical
constraint and that organizational structure should earn its complexity.

## Load-bearing unknown

The onboarding compiler is the weakest assumption. No supplied evidence establishes
that a natural-language job description can be transformed into reliable skills,
permissions, schedules, and qualification tests with acceptable human effort. The
first prototype should measure this directly against hand-authored configuration.

## Hard gates

1. Revocation, schedule cancellation, work reassignment, and rollback drills pass.
2. Candidate skill changes improve held-out performance without policy regression.
3. Human effort per accepted output declines relative to a fixed single-agent baseline.
4. A second agent is added only after demonstrating incremental value above its cost.

## Important disagreement

The collective-misalignment claim from Shen et al. received opposing scores because
one model would not accept it without the primary study in the supplied material.
That claim should be independently source-verified before it is used as an
architectural premise.
