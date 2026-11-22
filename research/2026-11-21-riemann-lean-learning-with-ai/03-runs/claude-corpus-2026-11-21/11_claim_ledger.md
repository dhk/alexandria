# 11: Claim ledger

Tags:
- **E**: evidence. A primary artifact or a reproducible check.
- **F**: a first-person statement by the actor.
- **R**: relayed by a journalist or aggregator.
- **I**: interpretation.
- **H**: hype or framing.
- **M**: mutation. The claim changed as it moved between sources.

Confidence is my assessment as of 21 Nov 2026.

## Core claims

| ID | Claim | Tag | Lineage | Confidence | Notes |
|---|---|---|---|---|---|
| C1 | Mathlib's `RiemannHypothesis` is the standard RH | E | [Mathlib source](https://github.com/leanprover-community/mathlib4/blob/v4.33.1/Mathlib/NumberTheory/LSeries/RiemannZeta.lean), then the [Lean FRO](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) | Very high | See [01](01_statement_check.md) |
| C2 | The submission proves exactly that statement | E | `comparator.json`, then con-leche `--compare` ([MIT](https://math.mit.edu/~drew/grh/)) | Very high | The end-to-end `lake comparator` kernel stages were still running at 12:55 UTC |
| C3 | Only the three standard axioms are used | E | `#print axioms` ([MIT](https://math.mit.edu/~drew/grh/)) | Very high | |
| C4 | Multiple independent kernels accept the proof | E | nanoda, con-leche, lean4lean, leanchecker ([MIT](https://math.mit.edu/~drew/grh/)) | Very high | |
| C5 | The "GRH" is for Dirichlet L-functions only | E | `Challenge.lean`; Sutherland's note | Very high | Some press says simply "the generalized Riemann hypothesis" without this qualifier |
| C6 | Alpöge expects ERH "with more time" | F | [Alpöge note](https://alpo.ge/remark.pdf) | Not yet a claim of proof | |
| C7 | The Lean FRO has "full confidence" | F | [Lean community blog](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) | Statement verified | This is an institutional judgment, not an extra check |
| C8 | Nobody understands the proof yet | R/I | Buzzard via [Al Jazeera](https://www.aljazeera.com/news/2026/11/21/riemann-hypothesis-has-the-worlds-most-famous-maths-problem-been-cracked) | High, as of 21 Nov | Expected to change quickly |
| C9 | The prose version would exceed 250,000 pages | F | Alpöge, via [New Scientist](https://www.newscientist.com/article/2600134-anthropic-mathematician-claims-ai-assisted-proof-of-the-riemann-hypothesis/) | Unverifiable | Not released |
| C10 | The key insight was about √X chained theta lifts, which mimic Stepanov's method | F/R | Alpöge note, then [The Decoder](https://the-decoder.com/hours-after-anthropic-claims-a-claude-proof-of-the-riemann-hypothesis-stanford-releases-an-all-human-competing-draft/) | Unverified | Only the 4-page note and the Lean code are public |
| C11 | The proof uses the full Langlands and arithmetic-geometry machinery | I | [Tao](https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/); Nuccio ([Quanta](https://www.quantamagazine.org/updates/transformation/)) | Moderate | Based on early reading. The named-theorem table in [#39](https://github.com/leanprover-community/riemann-hypothesis/issues/39) supports it |
| C12 | The timing was chosen around the IPO | F/I | Alpöge says it was a "constraint to respect" ([New Scientist](https://www.newscientist.com/article/2600134-anthropic-mathematician-claims-ai-assisted-proof-of-the-riemann-hypothesis/)) | Motive unknowable | Alpöge rejects the cynical reading |
| C13 | Masullo's draft is correct | R | [Vakil via The Decoder](https://the-decoder.com/hours-after-anthropic-claims-a-claude-proof-of-the-riemann-hypothesis-stanford-releases-an-all-human-competing-draft/) | Low to unknown | Vakil makes "no claim" about it, and it is under major revision |
| C14 | "The most resources ever dedicated to a single problem" | I/H | Glazer via [Science](https://www.science.org/content/article/ai-may-have-solved-math-s-greatest-mystery-can-humans-understand-answer) | Unverifiable | Compute was not disclosed |
| C15 | AI can now make "profoundly superhuman scientific discoveries" | I/H | [SciAm](https://www.scientificamerican.com/article/what-the-riemann-hypothesis-proof-really-means-about-ai-and-the-future/) | Speculative | Generalizes from a single case |

## Mutations to discuss

| ID | Original | Mutated version | Where |
|---|---|---|---|
| M1 | "Claude far outpaced me near the finish line" followed immediately by "No, Claude flew, and danced, and sparkled near that finish line" ([The Economist](https://www.economist.com/science-and-technology/2026/11/20/ai-may-have-solved-the-most-important-problem-in-mathematics)) | Only the first half quoted | [Al Jazeera](https://www.aljazeera.com/news/2026/11/21/riemann-hypothesis-has-the-worlds-most-famous-maths-problem-been-cracked) |
| M2 | "formalized the arguments without assumptions" (Alpöge) | The proof uses three standard axioms. It is not "assumption-free" in a literal sense, but it does not assume RH-like hypotheses | [The Defiant](https://thedefiant.io/frontier/ai/masullo-s-riemann-claim-draws-ai-assisted-objections) |
| M3 | The Jacobian conjecture was shown false with a counterexample ([New Scientist](https://www.newscientist.com/article/2600134-anthropic-mathematician-claims-ai-assisted-proof-of-the-riemann-hypothesis/)) | "solved the Jacobean conjecture" | [The Verge](https://www.theverge.com/ai-artificial-intelligence/1010051/anthropic-riemann-hypothesis-millennium-prize-problem) |
| M4 | Sutherland at a Harvard workshop, October 2024: "An AI that can prove the Riemann hypothesis is not one I'd want to meet" ([The Decoder](https://the-decoder.com/hours-after-anthropic-claims-a-claude-proof-of-the-riemann-hypothesis-stanford-releases-an-all-human-competing-draft/)) | "a prominent mathematician" who spoke "earlier in the year", unnamed | [SciAm](https://www.scientificamerican.com/article/what-the-riemann-hypothesis-proof-really-means-about-ai-and-the-future/) |
| M5 | Strogatz: "A very skilled AI jockey riding a very fast AI horse" ([Washington Post](https://www.washingtonpost.com/technology/2026/11/20/using-anthropic-ai-mathematician-claims-have-solved-riemann-hypothesis/)) | "a highly skilled jockey rides an exceptionally fast horse" | [NYT](https://www.nytimes.com/2026/11/20/science/anthropic-ai-math-riemann-hypothesis.html). Possibly two separate interviews |
| M6 | Proportion of zeros on the line "about 67.2%" ([Anthropic](https://www.anthropic.com/research/riemann-zeta)) | "67.25 percent" | [Al Jazeera](https://www.aljazeera.com/news/2026/11/21/riemann-hypothesis-has-the-worlds-most-famous-maths-problem-been-cracked); [IBM](https://www.ibm.com/think/news/anthropic-claude-riemann-hypothesis-math-proof). A rounding difference |
| M7 | A reduced build saves "about 55%" | Corrected by its own author to about 9% | [Issue #3](https://github.com/leanprover-community/riemann-hypothesis/issues/3). A good example of self-correction in the open |
| M8 | A blog post by a Stanford professor | "Stanford releases an all-human competing draft" | [The Decoder](https://the-decoder.com/hours-after-anthropic-claims-a-claude-proof-of-the-riemann-hypothesis-stanford-releases-an-all-human-competing-draft/) headline |
| M9 | Conrad as Masullo's reviewer or adviser | "co-authored" | The garbled extraction of the [Science](https://www.science.org/content/article/ai-may-have-solved-math-s-greatest-mystery-can-humans-understand-answer) page. Unconfirmed |
| M10 | The Verge: "has not been independently verified" (20 Nov) | Superseded within about 24 hours by multi-kernel checks | [The Verge](https://www.theverge.com/ai-artificial-intelligence/1010051/anthropic-riemann-hypothesis-millennium-prize-problem) vs [MIT](https://math.mit.edu/~drew/grh/). Accurate when written, now stale |

## Open questions

- Will the end-to-end `lake comparator` and the Lean default and paranoid kernel runs on the full export finish clean? Check [MIT](https://math.mit.edu/~drew/grh/) and [the repo NOTES](https://github.com/leanprover-community/riemann-hypothesis/blob/main/verification/NOTES.md).
- How much of the archive is genuinely new mathematics, and how much is routine infrastructure? Buzzard: "There is a chance that there's a thousand pages of new ideas" ([Al Jazeera](https://www.aljazeera.com/news/2026/11/21/riemann-hypothesis-has-the-worlds-most-famous-maths-problem-been-cracked)).
- What were the compute cost and the prompts? The Advisory Group asks labs to disclose both ([New Scientist](https://www.newscientist.com/article/2592421-openai-announces-722-mathematical-discoveries-in-one-go/)).
- Will a short human proof emerge? Alpöge expects the proof to be "massively simplified, likely immediately" ([Quanta](https://www.quantamagazine.org/updates/transformation/)).
