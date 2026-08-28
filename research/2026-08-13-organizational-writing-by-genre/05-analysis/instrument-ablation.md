# Instrument ablation — does grader topology change the landscape?

*Performed 2026-08-19 against run `r-2026-0813-03`. Data:
`instrument-ablation.json`. Issue: dhk/minority-report#7.*

## Why this was measured rather than argued

dhk/minority-report#59 says the grader reads all three research outputs before
scoring any of them, which is not the blind per-model grading
`docs/confidence-calibration.md` §3.2 requires. That is a hypothesis with a
plausible mechanism. Whether it costs anything is a separate question, and the
answer decides how much the fix is worth: if the landscape barely moves, the
defect has been overweighted.

Both passes re-grade the same preserved run from the same raw responses. No
research call was dispatched — that half was banked in August 2026 — and the
four raw files were verified byte-for-byte and by sha256 against the run
record's `raw_responses.files` before either pass ran.

## Result

| | pass A — as implemented | pass B — as specified |
|---|---|---|
| `grader_topology` | `single-call-all-models` | `per-model-blind` |
| `score_derivation` | `model-assigned` | `derived-lookup` |
| `extraction_pass` | `fused` | `separate` |
| grading calls | 1 | 4 |
| **claims** | **27** | **100** |
| consensus | 25 | 95 |
| novel | 2 | 5 |
| disagreement | 0 | 0 |
| cost | $0.1858 | $0.4894 |

The landscape did not barely move. Claim identity nearly quadrupled from
identical evidence.

## What licenses reading that as an effect

Pass A is not a reconstruction of the current grader. It calls
`commission.py`'s own `_grading_prompt`, imported from the installed package.
Against the published landscape of 26 claims — 25 consensus, 1 novel — it
returned 27 claims, 25 consensus, 2 novel. The harness reproduces the
instrument, and the instrument is stable across runs.

So the difference between 27 and 100 is attributable to what changed between
the passes, not to the apparatus that measured them.

## What this does not establish

- **Topology alone is not isolated.** No implementation of §3.1/§3.2 exists, so
  pass B's prompts were written for this ablation from the spec text. The delta
  conflates a change of topology with a change of prompt wording. Pass A's
  prompt is production code; pass B's is not.
- **+73 is a floor, not a measurement.** Both extraction runs returned exactly
  100 claims, at 5,660 and 5,669 completion tokens against a 16,000-token cap,
  with no truncation. A model stopping on a round number is not a limit being
  reached, so the true count under permissive extraction is at least 100.
- **One run.** One brief, one grading model, one set of three research models.
  Nothing here shows the ratio holds elsewhere in the corpus.
- **Which pass is closer to the truth is not settled by this.** A larger claim
  landscape is not self-evidently a better one. §3.1 is permissive by design —
  "if even one model treats something as a distinct claim, it gets its own
  claim_id" — and permissiveness admits noise along with novelty. What the
  ablation shows is that the two apparatus disagree by a factor of four about
  what the same evidence contains, not which of them is right.

The obvious confound was checked and rejected: this run's outputs contain two
100-cell matrices, and an extraction that had enumerated cells would land on 100
for an uninteresting reason. The claims are propositions — the strings
`matrix`, `cell` and `×` appear zero times across all 100.

## What follows

For dhk/minority-report#59, the fix is worth making: the divergence is not
cosmetic. For the open question of whether affected investigations should be
re-run, this supplies the number that was missing — every group count in the
corpus was produced by the fused grader, and the fused grader recovers roughly a
quarter of the claims the same raw responses support.

Per AGENTS.md rule 5 this is published alongside the original analysis, which is
not modified. The published claim landscape remains what the run produced.
