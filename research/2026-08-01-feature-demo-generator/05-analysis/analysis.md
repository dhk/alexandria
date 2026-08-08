# Analysis: Feature Demo Generator

This analysis promotes the comparative report from successful run
`r-2026-0801-02` into Alexandria's current lifecycle. The complete claim table,
model quotations, scores, and detailed comparison remain in
[`03-runs/r-2026-0801-02/report.md`](../03-runs/r-2026-0801-02/report.md).

## Areas of agreement

All three research models favored the same narrow product shape: repository
interrogation triggered by a merge, followed by a brief human product-context
interview, producing a provenance-bearing demo specification. They also agreed
that a script-first MVP is the appropriate validation scope, that visual capture
should be a separate and deferrable step, and that downstream reuse—not artifact
generation—is the meaningful success measure.

The outputs consistently identified authentication, seed data, nondeterministic
UI state, and selector brittleness as the dominant risks for automated capture.
They also warned that confidently wrong pre-filled customer or benefit fields
would damage trust faster than an explicit statement of uncertainty.

## Useful outliers

One model supplied several concrete extensions absent from the other outputs:
Storybook or visual-regression tooling as a low-cost screenshot source, Remotion
as a possible renderer for a structured script, Danger.js as PR-event
scaffolding, and a Phase 0 discovery exercise before implementation. The same
model raised the strategically important possibility that the concept belongs as
an integration layer over an existing demo platform rather than as a standalone
product.

These are hypotheses to verify, not validated recommendations.

## Evidence limits

The run had no live web access despite the brief asking for current attributable
evidence. Product capabilities, API availability, direct competitors, market
size, and willingness to pay therefore remain unverified. Model agreement only
shows convergence on the supplied RFC and training-data knowledge; it is not
independent factual validation.

The next pass should verify named products against primary documentation, search
for current direct prior art, and collect buyer evidence before any market-gap
claim is repeated externally.
