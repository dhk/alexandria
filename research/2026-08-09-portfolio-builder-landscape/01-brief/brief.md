# Research brief: Portfolio-website brand-interview pipeline — market scan and build vs. buy

Revision: 1 (2026-08-09). Checksum of this revision is recorded in
[`../03-runs/claude-2026-08-09/run-metadata.yaml`](../03-runs/claude-2026-08-09/run-metadata.yaml).

## Background

The operator is scoping an unbuilt product: a service that helps people
design a portfolio website congruent with their personal brand, via a
five-step process — (1) a brand-discovery interview seeded from a resume
and LinkedIn profile plus direct questions, (2) adaptive follow-up
questions, (3) explicit audience definition, (4) a colour-scheme and
layout proposal, (5) build. Full source material:
[`../00-topic/source-material.md`](../00-topic/source-material.md).

The research runs in two passes. Q1 is the first pass: a broad market
scan. Q2–Q6 are a verification pass, drafted for dispatch through
Alexandria's `begin_research`/`run_research` commission flow but run
single-source after three dispatch attempts failed (see `topic.yaml`'s
`notes` and [dhk/minority-report#33](https://github.com/dhk/minority-report/issues/33)).

## Scope

In scope: consumer/prosumer and freelancer/creator tools for personal
portfolio and personal-brand websites; brand-identity and colour-palette
generators; AI website builders with onboarding questionnaires; personal
branding/voice tooling; general portfolio-site hosting platforms;
build-vs-buy economics for the specific unbuilt piece (the interview →
brief → proposal reasoning layer), not generic software economics.

Out of scope: enterprise portfolio-management/PMO software (a different
meaning of "portfolio"); non-English sources; hands-on testing of any
vendor's product.

## Comparison set

See `topic.yaml`. Assembled across both passes: the first pass's tools by
pipeline step, plus two additions from the verification pass — Cactus (YC
S25), the nearest miss found when hunting for a product that chains all
five steps, and Lemlist's ICP Generator, the nearest miss when checking
whether the audience-definition gap is real or just under a different
label.

## Research questions

### Q1 — Landscape by pipeline step (first pass)

For each of the five steps, what tools already exist, and which step(s)
does each one actually cover versus merely gesture at? Specifically:
resume/LinkedIn-to-site parsers (step 1+5, one-shot); personal
brand-voice/discovery AI (step 1-2, but for ongoing content, not a
one-time site brief); audience/persona tooling (step 3); palette and
brand-identity generators, and AI site builders that auto-theme from an
onboarding questionnaire (step 4); commodity hosting/page-builder
platforms (step 5).

### Q2 — Does anything chain all five steps?

Core claim to verify or refute: no existing product chains brand-discovery
interview → follow-up → audience definition → traceable palette/layout
proposal → build into one reviewable pipeline. Hunt specifically in
2025–2026 Product Hunt launches, Y Combinator batches, and stealth-startup
directories — not SEO-optimized blog listicles, which a first pass
over-indexes on.

### Q3 — Is the audience-definition gap real, or mislabeled?

Q1's first pass found only generic marketing-persona templates for step
3, nothing portfolio-specific. Pressure-test whether that's genuinely
unserved, or exists under a different label — inside UX-research tools,
brand-strategy SaaS, ICP-generation tools, or human web-design-agency
intake processes that a portfolio-focused search would miss.

### Q4 — Stealth or emerging competitive threats

Beyond named, launched products, is any team visibly building this exact
combined pipeline right now, even in early or stealth form?

### Q5 — LLM-orchestrated interview-pipeline economics

Generic "custom SaaS vs. starter kit" build-vs-buy benchmarks don't
capture this pipeline's actual shape. Estimate realistic per-user LLM
cost for a multi-turn structured interview plus a palette/layout proposal
step at current flagship pricing, and a realistic time-to-MVP for that
reasoning layer alone — explicitly excluding hosting, parsing, and colour
infrastructure, which the recommendation below treats as bought, not
built.

### Q6 — LinkedIn data: legal/ToS risk for the parsing step

The build-vs-buy recommendation calls for buying/integrating resume and
LinkedIn parsing as commodity. What does that actually require ingesting
LinkedIn profile data safely — LinkedIn's User Agreement terms on
scraping/automation, the relevant case law (hiQ Labs v. LinkedIn and its
CFAA holding), and the practical risk gradient between an individual
supplying their own data versus an automated third-party fetch?

### Q7 (synthesis question, answer in analysis not findings)

Given Q1–Q6, does the build-vs-buy recommendation already drafted — buy
parsing, colour math, and hosting as commodity; build the interview
logic, audience step, and brand-to-proposal reasoning layer — hold up,
and what, if anything, changes about it? This requires judgment across
sources, not independent findings.

## Output format for a findings submission

One section per question (Q1–Q6). Q1 organized by pipeline step, each
tool with a one-line note on what it actually covers versus what it
merely claims. Q2–Q6 each end with a closed-set verdict —
`confirmed` / `refuted` / `partially confirmed` / `no equivalent found` —
with rationale in prose below the verdict, not invented labels in the
verdict itself. Every claim carries a citation. Q7 is answered only in
`05-analysis/analysis.md`.
