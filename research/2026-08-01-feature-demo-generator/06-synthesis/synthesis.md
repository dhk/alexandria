# Synthesis: validate the script-first seam, not a demo-generation platform

The useful hypothesis is narrower than “automatically generate product demos.”
It is that merge-time repository facts can pre-fill a short product-context
interview, and that the confirmed answers can become a structured,
provenance-bearing demo specification. A markdown script is the first renderer
worth testing because it exposes whether the context is accurate and useful
without coupling the experiment to browser automation.

That sequencing matters. Automated capture inherits difficult per-product
requirements: authenticated state, representative seed data, stable navigation,
feature flags, preview deployments, and selectors that survive UI change. If the
interview-to-script loop does not produce artifacts that PM, sales, support, or
enablement teams actually reuse, solving those capture problems creates no
durable value.

The most useful first experiment is therefore a manual or thinly automated
concierge workflow. Select genuinely demo-worthy merged changes, pre-fill five
product-context fields from repository evidence, ask the appropriate human to
confirm or correct them, and measure completion time, confident errors, and
downstream reuse. The PR author should not be assumed to be the right respondent;
that is itself an experiment.

This run does not establish a market gap. It had no live web access, so named
competitor capabilities, APIs, recent entrants, market size, and willingness to
pay remain unverified. The apparent convergence of three models is a reason to
test the workflow, not evidence that the product opportunity exists. A Silver
follow-up should verify current products against primary sources and collect
buyer evidence before any external positioning claim is made.
