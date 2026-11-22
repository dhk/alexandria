# The Riemann hypothesis, Lean, and learning with AI: a source corpus

Assembled on 21 November 2026, about 30 hours after Levent Alpöge announced a Claude-assisted, Lean-only proof of the Riemann hypothesis (RH). The corpus supports a four-part conversation series about how we learn with AI.

## Bottom line
- **Statement check: it matches.** The headline theorem proves Mathlib's long-standing `RiemannHypothesis`. That is a faithful formalization of "every non-trivial zero of ζ has real part 1/2". A comparator confirmed that the proof targets exactly this statement. Two independent cross-checks back it up: equivalence with DeepMind's separately written GRH statement, and a derivation of Robin's inequality, which does not mention zeta at all. Details are in [01](01_statement_check.md).
- **Caveat: the "GRH" covers Dirichlet L-functions only.** It is not the Extended or Grand RH.
- **Verification status.** Validity is supported by independent kernels, including con-leche, whose soundness is formally proven, and the Lean FRO says it has "full confidence". As of 12:55 UTC on 21 Nov, the official Lean kernel replays of the full 62 GB export and the end-to-end `lake comparator` were still running ([MIT](https://math.mit.edu/~drew/grh/)).
- **Understanding: essentially none yet.** Clay still lists RH as unsolved, and its rules require two years and general acceptance.

## Files
| File | Purpose |
|---|---|
| [01_statement_check.md](01_statement_check.md) | Verdict, the Lean text side by side with the standard statement, the trust base, live status |
| [02_how_the_lean_process_works.md](02_how_the_lean_process_works.md) | Starts with a five-minute Lean primer for non-mathematicians, then the pipeline from compile to comparator to independent kernels, and what Lean does not give you |
| [03_timeline.md](03_timeline.md) | The 2026 run-up, the announcement window, historical anchors |
| [04_perspectives.md](04_perspectives.md) | About 40 people grouped by the question they are answering |
| [05_competing_claim_masullo.md](05_competing_claim_masullo.md) | The all-human Masullo draft, compared side by side |
| [06_precedents_and_context.md](06_precedents_and_context.md) | Four colour, Wiles, Kepler, Mochizuki, Atiyah, the Liquid Tensor Experiment, Thurston, and the 2026 AI wave |
| [07_conversation1_assembling_knowledge.md](07_conversation1_assembling_knowledge.md) | Brief and discussion questions for conversation 1 |
| [08_conversation2_adjudicating_claims.md](08_conversation2_adjudicating_claims.md) | Brief and discussion questions for conversation 2 |
| [09_conversation3_systems_old_and_new.md](09_conversation3_systems_old_and_new.md) | Brief and discussion questions for conversation 3 |
| [10_conversation4_learning_in_an_age_of_ai.md](10_conversation4_learning_in_an_age_of_ai.md) | Brief and discussion questions for conversation 4 |
| [11_claim_ledger.md](11_claim_ledger.md) | Claims tagged evidence, first-person, relayed, interpretation, or hype, plus ten documented mutations |
| [12_sources.md](12_sources.md) | Every source with its full URL, grouped by position in the source hierarchy |

## Provenance conventions
- Quotes are verbatim as printed by the cited outlet. Where outlets disagree, both versions are given (see the mutations in [11](11_claim_ledger.md)).
- The Science RH article's page text extracted with corruption, so quotes from it are flagged. Check them against the original before reusing them publicly.
- A few historical details are marked "from memory; verify" where the fetched page did not contain them.
- This is a fast-moving story. The verification status, Masullo's revisions, and expert readings will change within days.

## Conflict-of-interest disclosure
This corpus was assembled by Claude, an Anthropic model, about a result produced with Claude by an Anthropic employee. Sutherland's checks were also run with Claude Code. I tried to anchor every claim about correctness in artifacts that do not depend on Anthropic: Mathlib, the independent kernels, the community repository, and statements by non-Anthropic experts. I also included critics prominently. Even so, treat the framing choices as a possible source of bias, and test them in conversation 2.
