# Is ASD-STE100 the right tool for clear, concise, persuasive writing?

**Question.** ASD-STE100 (Simplified Technical English) is circulating as a
general standard for good writing. Test that claim rather than assume it:
establish what STE was built for and by whom, what the evidence says it does
well and badly, how it contrasts with the other techniques available, and how
a writer should choose between them by purpose, audience, and context.

**Material examined.** The claim stated verbatim, plus one exhibit of it in
practice — `ste/SKILL.md` from `github.com/nonatofabio/claude-writing-skills`
(8,122 bytes). No external sources were supplied; see *How far to trust it*.

**Answered by.** `openai/gpt-5.4` · `anthropic/claude-opus-4.7` ·
`x-ai/grok-4.5`. **Graded by** `anthropic/claude-sonnet-4.6`.
**Web search** off — the models answered from training data.
**Run** `r-2026-0813-01`, 2026-08-13, $0.64.

## The verdict

All three models reject the claim, and reject it for the same reason: STE
removes, by design, the devices persuasion depends on — varied rhythm,
synonymy, figurative language, voice, narrative. Those removals are virtues in
a maintenance procedure read under operational pressure by a second-language
technician, and liabilities in an essay meant to change someone's mind.

They agree on what STE is genuinely good for — procedural, safety-critical,
multilingual technical documentation — and on the mechanism: one word one
meaning, short sentences, imperative structure, controlled vocabulary, all of
which cut ambiguity and translation cost.

On **why the enthusiasm exists now**, the three converge on an uncomfortable
answer: STE is popular in AI and writing-tool circles because it is
*machine-operable* — rule-based, checkable, legible to a tool — rather than
for any reason connected to what it was built for. Tool transfer from a
bounded domain to a general one.

## Read order

1. [`01-brief/brief.md`](01-brief/brief.md) — the commission, verbatim.
2. [`05-analysis/analysis.md`](05-analysis/analysis.md) — where the three
   outputs converge, where they differ, and what the run does not establish.
3. [`05-analysis/scores.csv`](05-analysis/scores.csv) — 28 claims scored
   against every model, each with the quote it rests on.

## How far to trust it

**Silver: three lineages, claims scored, quotes attached, no source audit.**
Web search was off, so every citation is model recall. They are specific
enough to check — Chervak & Drury on maintenance instructions, Sopory &
Dillard's 2002 metaphor meta-analysis, Green & Brock 2000 on narrative
transportation, Kincaid et al. 1975, Pullum 2009 on Strunk & White, Kuhn 2014
in *Computational Linguistics* — and **not one has been checked**.

Two things a reader should weigh before citing this:

**The landscape has no disagreements.** 25 consensus claims, 3 novel, zero
contested. On a system built to surface disagreement that is a finding about
the run, not a strength of the answer: either the question has a settled
answer, or the framing led all three models to the same place. No adversarial
pressure was bought here.

**The models split on history, and honesty lost.** Two supplied STE's founding
lineage — AECMA Simplified English, early 1980s, Fokker and Douglas
involvement, renamed ASD-STE100 in 2004–05. The third declined to assert any
of it, on the grounds that the supplied materials did not establish it. That
is the more rigorous position and it produced the thinner document. Which one
was actually right is unresolved, and resolving it needs a source, not another
model.

**What nobody has shown.** The anti-persuasion verdict rests on theory, not
experiment: no output could cite a controlled study comparing STE-restricted
persuasive text against rhetorically crafted text on attitude change or trust.
Likewise there is no clean causal evidence that STE reduces accident rates —
the safety case rests on mechanism and institutional adoption — and no one
knows whether STE's second-language comprehension benefit comes from the
approved-word dictionary or the syntactic rules, which is exactly the question
a rules-only implementation raises.

## Related

Follows [`2026-08-12-writing-communication-best-practices`](../2026-08-12-writing-communication-best-practices/),
which evaluated the same repo against the literature and identified the
missing context router this brief was commissioned to fill.
