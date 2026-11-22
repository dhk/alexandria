# The Lean proof of the Riemann hypothesis

A source corpus on the claimed Lean-only proof of the Riemann hypothesis
(November 2026). It is built to support a four-part conversation series on
learning with AI.

**State: Bronze, single model, ungraded.** One interactive Claude run produced
everything here. That is a conflict of interest, since the result was produced
with Claude. Read `03-runs/claude-corpus-2026-11-21/00_README.md` for the
disclosure and the provenance conventions.

## What exists

| Stage | Contents |
|---|---|
| `00-topic/` | The primary artifacts that prompted the question |
| `01-brief/` | The operator's requests, verbatim (revision 1) |
| `03-runs/claude-corpus-2026-11-21/` | The run's output as produced, plus `run-metadata.yaml` with checksums |
| `05-analysis/` to `08-published/` | Not started |

## Headline finding, unadjudicated

The headline theorem proves Mathlib's standard `RiemannHypothesis` statement.
That is the run's reading of
[Mathlib at v4.33.1](https://github.com/leanprover-community/mathlib4/blob/v4.33.1/Mathlib/NumberTheory/LSeries/RiemannZeta.lean),
and it relies on comparator and kernel results that others reported on
[Sutherland's status page](https://math.mit.edu/~drew/grh/). Treat it as a
claim made by one model, not as a reviewed conclusion.

## Map of the run's files to later stages

When the analysis and synthesis stages begin, these files are the natural
inputs. They have not been reviewed or promoted.

| Run file | Candidate stage |
|---|---|
| 01 statement check, 04 perspectives, 05 Masullo comparison, 11 claim ledger | `05-analysis/` |
| 02 Lean process (with the non-mathematician primer), 03 timeline, 06 precedents | `06-synthesis/` |
| 07 to 10 conversation briefs | the learning-with-AI series, outside this lifecycle |
| 12 sources | the future source audit |

## Open tasks

- Run the same brief through at least one non-Anthropic model, blind, and
  compare the claim landscapes.
- Recheck verification status: the kernel replays, the end-to-end comparator,
  and the NOTES in the community repository.
- Check the flagged quotes from Science, and the "from memory; verify" items in
  06, against their originals.
- Operator: write `origin`, `claim_under_test`, `why_now`, and `scope` in
  `topic.yaml`.
