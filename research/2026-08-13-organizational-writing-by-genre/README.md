# Which writing technique for which organizational genre

**Question.** Does one set of writing principles serve organizational
communication whatever its purpose? If not, which technique suits which genre,
and how should a writer choose?

**Material examined.** The claim stated verbatim, plus the whole of
`github.com/nonatofabio/claude-writing-skills` (7 files). Techniques compared:
ASD-STE100, BLUF and the US Army writing standard, Minto's Pyramid Principle,
the Amazon six-page narrative memo and PR-FAQ, ISO 24495-1:2023 plain
language, blameless postmortem convention, classical and Toulmin
argumentation, readability optimisation as embodied by the Hemingway Editor,
Hotaling's rules for concise scientific writing, and the repo's three skills.

**Answered by** `openai/gpt-5.4` · `anthropic/claude-opus-4.7` ·
`x-ai/grok-4.5`. **Graded by** `anthropic/claude-sonnet-4.6`.
**Web search** on — not reproducible from its inputs.
**Run** `r-2026-0813-03`, 2026-08-13, $0.97, 26 claims.

## The verdict

No. One set of principles does not serve all organizational writing, and the
three models agree on why: every organizational genre is a decision genre —
facts are communicated so somebody acts, chooses, funds, trusts or forgives —
while the techniques on offer optimise for incompatible things.

## The finding that generalises

The prior run in this series found that *shorter is generally better* is valid
as a diagnostic and invalid as an optimization target. This run found its
twin:

> **"More committed is generally better" has the same Goodhart shape as
> "shorter is generally better."**

All three models independently identified the `humanize` skill's instruction to
*force claims that commit* as a **defect** in every genre whose honest state is
uncertainty — investigation summary, research proposal, incident notification,
status update — and as dangerous in one. One scored it −2 on confidence
calibration. All three noted the skill's scientific-papers override already
concedes the problem and scopes the fix far too narrowly.

A surface-feature audit cannot distinguish a weasel word from a confidence
interval. That is a limit on tooling, not a bug to be fixed.

## Where every technique fails

**Incident notification written while facts are still moving.** All three
identified it as the genre no available technique serves, and all three
converged — without being asked — on the same prescription: a dedicated
uncertainty-preserving schema with mandatory *known* / *unknown* /
*next update* fields.

**Status updates** are half outside craft's reach. Conventions can make an
honest update easier to write than a reassuring one; nothing in writing can
fix an incentive structure that rewards green. All three drew that boundary in
the same place.

## Read order

1. [`05-analysis/matrices.md`](05-analysis/matrices.md) — **start here.** The
   demand matrix, the supply matrix, and the ten cells the models disagree
   about.
2. [`01-brief/brief.md`](01-brief/brief.md) — the commission, verbatim.
3. [`05-analysis/analysis.md`](05-analysis/analysis.md) — convergence,
   divergence, and what the run does not establish.
4. [`05-analysis/scores.csv`](05-analysis/scores.csv) — 26 claims scored
   against every model, with quotes.

## How far to trust it

**Silver, with two caveats sharper than usual.**

**The brief may have led the models.** The grading model observed, unprompted,
that *"the degree of agreement on individual claims is unusually high,
suggesting the source materials strongly constrain the conclusions"*. The brief
named three tensions — commitment versus calibration, notification versus
postmortem, aggregation decay — and those three came back as findings. That is
what a well-aimed brief looks like and also what a leading question looks like,
and this run cannot tell them apart. A control run with the tensions removed
would.

**Zero disagreements does not mean agreement.** The claim landscape records 25
consensus claims and none disputed; the synthesised matrices show ten contested
cells across the same three outputs. Claim extraction represents disagreements
about *direction*, not about *degree*.

**No outcome evidence exists.** Every score is a judgement about mechanism. No
technique in the set has been shown to improve decision quality, trust
calibration, incident recurrence, or durability of reasoning — and Amazon's
prose-over-bullets claim, the most consequential assertion in the set, is
unproven outside Amazon.

## Related

Third in a series, after
[`2026-08-12-writing-communication-best-practices`](../2026-08-12-writing-communication-best-practices/)
and [`2026-08-13-is-ste100-the-right-tool`](../2026-08-13-is-ste100-the-right-tool/).
