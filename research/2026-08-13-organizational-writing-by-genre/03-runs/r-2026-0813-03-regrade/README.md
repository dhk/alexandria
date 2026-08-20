# Instrument ablation — re-grading `r-2026-0813-03` two ways

**What this is.** A new artifact, not a correction to `r-2026-0813-03`. The
published run stands exactly as it was. This measures what its *instrument* did
to it.

[`docs/instrument.md`](../../../../docs/instrument.md) §4 says every run in the
corpus was graded by an implementation diverging from
[`docs/confidence-calibration.md`](../../../../docs/confidence-calibration.md)
on all three axes, and that *the size of the effect is unmeasured*. This is the
measurement. It is tracked as
[dhk/minority-report#59](https://github.com/dhk/minority-report/issues/59).

## Method

Both passes re-grade the **same preserved raw responses** for
`r-2026-0813-03`. No research model was dispatched; the expensive half was
already banked. All four raw files were checksummed against
`raw_responses.files` on the run record before either pass ran.

| | pass A | pass B |
|---|---|---|
| `grader_topology` | `single-call-all-models` | `per-model-blind` |
| `score_derivation` | `model-assigned` | `derived-lookup` |
| `extraction_pass` | `fused` | `separate` |
| grading calls | 1 | 3, plus 1 extraction |

Pass A uses `alexandria.commission._grading_prompt` imported from the installed
package. It is not a reimplementation of the current behaviour; it *is* the
current behaviour.

Both passes were grouped by `alexandria.commission.classify_scores`, imported
unmodified, so the two group counts are produced by the same RFC-0005
precedence and are comparable to each other.

## Result

| | pass A | pass B | delta |
|---|---:|---:|---:|
| claims | 27 | 100 | **+73** |
| consensus | 25 | 95 | +70 |
| disagreement | 0 | 0 | 0 |
| novel | 2 | 5 | +3 |
| cost | $0.1858 | $0.4894 | |

**The group counts did not barely move. Claim identity nearly quadrupled from
identical evidence.**

That is the answer to the question this ablation was built to settle. The
hypothesis under test was that the grading defect had been overweighted — that
the topology is a spec violation without much consequence for what the corpus
records. It is not. Fusing extraction into a single all-outputs grading call
discards roughly three quarters of the claims the same three responses support.

## Why the pass A number can be trusted

The published `r-2026-0813-03` landscape holds 26 claims — 25 consensus, 1
novel. Pass A produced 27 — 25 consensus, 2 novel.

A harness that reproduces the published run to within one novel claim is
measuring the instrument rather than measuring itself. This check is the reason
pass A exists at all; without it the delta would be two unknowns compared
against each other.

## Three things this does not establish

**1. The delta conflates topology with prompt wording.** No implementation of
spec §3.1 or §3.2 exists. Pass B's extraction and per-model grading prompts
were written for this ablation from the spec text, so part of the +73 belongs
to the fact that a prompt asking only for claims behaves differently from a
prompt asking for claims, scores and a report in one payload. Separating those
two contributions needs the real implementation, which is the work #59 asks
for. What is *not* in doubt is the pass A side: that number came from
production code.

**2. +73 is a lower bound, not a point estimate.** Pass B returned exactly 100
claims. The extraction call was re-run and returned exactly 100 again, with no
truncation and completion tokens well inside the limit. A round number reached
twice is a model self-limiting, not a ceiling being hit, so the permissive
extraction the spec asks for would likely find more.

**3. It does not show that pass B's landscape is more correct.** It shows the
two are different, and that the difference is large. Which claim set better
represents what the three models actually asserted is a question about
faithfulness, and counting does not answer it. What the corpus can say today is
that its published claim counts are a property of the apparatus and not only of
the evidence — which is exactly what `docs/instrument.md` exists to make
visible.

## One confound, checked and refuted

Both matrices in this run hold exactly 100 cells. If the extraction pass had
enumerated matrix cells as claims, the whole delta would be an artefact.

The extraction call was re-run alone and its 100 claim texts inspected.
Across all 100: `matrix` 0 occurrences, `cell` 0, `scale` 0, `×` 0. The claims
are substantive prose propositions —

> `c1` No single set of writing principles serves all organizational writing
> genres.
>
> `c8` The `humanize` skill's Pass 1 instruction to 'force claims that commit'
> is a defect in genres where the honest epistemic state is uncertainty.
>
> `c50` Dissent is underserved because no single technique combines Toulmin's
> argument structure with blameless-postmortem's register discipline for
> avoiding ad hominem.

Refuted. Recorded here rather than dropped, because the suspicion was
reasonable and a reader should be able to see it was tested.

## What follows

- **dhk/minority-report#59 should be fixed**, in the order its issue gives.
  This measurement is the before half of its before/after.
- **Open decision 3 — whether to re-run affected investigations** — now has the
  number it was waiting on. Every group count in the corpus was produced by the
  pass A instrument.
- Nothing here changes a published claim or score. The delta is evidence about
  the instrument, not a replacement landscape.

## Cost

$0.8256 total: $0.1858 pass A, $0.4894 pass B, $0.1504 for the confound
re-check. Zero research dispatch.

Machine-readable results, including both `instrument` blocks in schema shape:
[`ablation.json`](ablation.json).
