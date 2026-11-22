# 03: Timeline

All dates are 2026 unless stated. Each item is tagged with the kind of evidence behind it. **[P]** marks a primary artifact or a first-person statement. **[R]** marks a claim reported by journalists. **[I]** marks an interpretation.

## The 2026 run-up

| Date | Event | Tag | Source |
|---|---|---|---|
| July | Alpöge announces that the Jacobian conjecture is false, with a 216-character counterexample found with Claude. The Verge instead describes this as having "solved the Jacobean conjecture". The two descriptions differ. | R | [New Scientist](https://www.newscientist.com/article/2600134-anthropic-mathematician-claims-ai-assisted-proof-of-the-riemann-hypothesis/); [The Verge](https://www.theverge.com/ai-artificial-intelligence/1010051/anthropic-riemann-hypothesis-millennium-prize-problem) |
| 10 Aug | Anthropic reports that Claude raised the proven proportion of zeta zeros on the critical line from 41.6% to about 67.2%. It also writes: "We don't expect that the techniques Claude used will lead to proving the Riemann hypothesis." | P | [Anthropic](https://www.anthropic.com/research/riemann-zeta); [The Verge](https://www.theverge.com/ai-artificial-intelligence/1010051/anthropic-riemann-hypothesis-millennium-prize-problem) |
| 4 Sep | Anthropic formalizes Fermat's Last Theorem in Lean: about 13 M lines in 11 days. Buzzard needed a machine with 96 cores and 500 GB of RAM to compile it. | P | [Anthropic](https://www.anthropic.com/research/formalizing-fermats-last-theorem); [Xena Project](https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/) |
| 8 Sep | OpenAI announces a Navier–Stokes solution. Clay calls it "apparently" settled but awards no prize. Buckmaster raises a dispute over prompts and credit, which OpenAI denies. | R | [The Dartmouth](https://www.thedartmouth.com/article/2026/10/rodriguez-nagle-dartmouth-mathematicians-weigh-artificial-intelligences-role-in-the-future-of-their-work); [Washington Post](https://www.washingtonpost.com/technology/2026/11/20/using-anthropic-ai-mathematician-claims-have-solved-riemann-hypothesis/) |
| 6 Oct | OpenAI releases 722 papers (372–377 results), including a "quasi-RH" zero-free region. Buzzard counts 30 papers relevant to number theory: 7 impressive, 1 Lean-verified. | R | [New Scientist](https://www.newscientist.com/article/2592421-openai-announces-722-mathematical-discoveries-in-one-go/); [Quanta](https://www.quantamagazine.org/ai-proved-the-quasi-riemann-hypothesis-what-happens-now-20261019/) |
| 7 Oct | OpenAI withdraws 3 Hodge-related manuscripts over "a sign error" and revises 14 others. | R | [The Dartmouth](https://www.thedartmouth.com/article/2026/10/rodriguez-nagle-dartmouth-mathematicians-weigh-artificial-intelligences-role-in-the-future-of-their-work) |
| 15 Oct | Leo de Moura: "Lean now ships with verified kernels" (con-leche). | P (relayed) | Linked in [Xena Project comments](https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/) |
| 12 Nov | Buzzard publishes "…and the proof is checked in Lean", a four-question checklist for AI-generated Lean. | P | [Xena Project](https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/) |
| 16 Nov (Mon) | Alpöge says he obtained the result. The Verge reports he texted Amodei "late Sunday night". | P/R | [Quanta](https://www.quantamagazine.org/updates/transformation/); [The Verge](https://www.theverge.com/ai-artificial-intelligence/1010051/anthropic-riemann-hypothesis-millennium-prize-problem) |
| 19 Nov (Thu) | Anthropic IPO. Nature reports a valuation of about $1.5 T. | R | [Nature](https://www.nature.com/articles/d41586-026-03812-7) |

## The announcement window

| Time | Event | Tag | Source |
|---|---|---|---|
| 20 Nov (Fri), morning | Alpöge posts a 4-page note and a 14-part Lean archive, with no prose proof. Tao's post the same day reports the GRH claim alongside Euler and Navier–Stokes blowup results. | P | [Alpöge note](https://alpo.ge/remark.pdf); [Tao](https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/) |
| 20 Nov, before noon | Sutherland (MIT) finishes the first complete compile; the MIT page logs 16:43 UTC. DeDeo compiles a few hours later. | P/R | [MIT](https://math.mit.edu/~drew/grh/); [Quanta](https://www.quantamagazine.org/updates/transformation/) |
| 20 Nov, hours later | Vakil posts Masullo's 940-page all-human GRH draft. About 8 hours later he reports problems found with AI help and says "I make no claim as to the correctness of the proof strategy." | R | [The Decoder](https://the-decoder.com/hours-after-anthropic-claims-a-claude-proof-of-the-riemann-hypothesis-stanford-releases-an-all-human-competing-draft/); [The Defiant](https://thedefiant.io/frontier/ai/masullo-s-riemann-claim-draws-ai-assisted-objections) |
| 20 Nov | Press wave: NYT, WaPo, The Economist, New Scientist, SciAm, IBM Think, The Verge, Nature. The Economist's World in Brief headline adds "the firm's shares slide". | R | See [12_sources.md](12_sources.md); [Economist](https://www.economist.com/the-world-in-brief/2026/11/20/e8ad2013-f322-4dca-ab32-0f67134f643f) |
| 20–21 Nov | Independent kernels accept: leanchecker replay at about 18:17 UTC, nanoda at 19:05, con-leche at 21:19, lean4lean at about 21:55. | P | [MIT](https://math.mit.edu/~drew/grh/) |
| 21 Nov | Community issues filed: the reduced build (#3, later corrected), the strategy map (#5), the `.olean` path bug (#6), the formal-conjectures GRH equivalence (#34), and 105 named theorems (#39). | P | [GitHub repo](https://github.com/leanprover-community/riemann-hypothesis/issues) |
| 21 Nov, 02:29–04:16 UTC | Robin/Lagarias cross-check: elementary divisor-sum inequalities, with no zeta in the statement, are accepted by several kernels. | P | [MIT](https://math.mit.edu/~drew/grh/) |
| 21 Nov, 12:55 UTC | MIT page update. The Lean default kernel, the paranoid kernel, and the end-to-end `lake comparator` on the full export are still running. | P | [MIT](https://math.mit.edu/~drew/grh/) |
| 21 Nov, 13:55 | Lean FRO and Mathlib Initiative: "We have full confidence that Alpöge's proof of the Riemann Hypothesis is correct." | P | [Lean community blog](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) |
| Open | Clay lists RH as "Unsolved". Its rules require publication, 2 years of scrutiny, and general acceptance. | P | [Clay](https://www.claymath.org/millennium/riemann-hypothesis/); [The Verge](https://www.theverge.com/ai-artificial-intelligence/1010051/anthropic-riemann-hypothesis-millennium-prize-problem) |

## Historical anchors used in later files

| Year | Event | Source |
|---|---|---|
| 1859 | Riemann's paper. | [Clay](https://www.claymath.org/millennium/riemann-hypothesis/) |
| 1976 | Appel–Haken four colour proof: 1,834 configurations and over 1,000 hours of computer time. | [Wikipedia](https://en.wikipedia.org/wiki/Four_color_theorem) |
| 1984 | Robin's criterion, equivalent to RH. | [Wikipedia](https://en.wikipedia.org/wiki/Robin%27s_theorem) |
| 1993–95 | Wiles announces his proof, a gap is found, and the proof is repaired with Taylor. | [Wikipedia](https://en.wikipedia.org/wiki/Wiles%27s_proof_of_Fermat%27s_Last_Theorem) |
| 1994 | Thurston, "On proof and progress in mathematics". | [arXiv](https://arxiv.org/abs/math/9404236) |
| 1998–2017 | Hales and the Kepler conjecture: referees were "99% certain", the Flyspeck formal proof was completed in 2014, and it was published in 2017. | [Wikipedia](https://en.wikipedia.org/wiki/Kepler_conjecture) |
| 2005 | Gonthier formalizes the four colour theorem in Coq. | [Wikipedia](https://en.wikipedia.org/wiki/Four_color_theorem) |
| 2012–present | Mochizuki's IUT and the abc conjecture. Scholze and Stix object (2018). The proof is still not accepted. | [Wikipedia](https://en.wikipedia.org/wiki/Abc_conjecture) |
| 2018 | Atiyah's RH claim is dismissed within days. | [Science](https://www.science.org/content/article/skepticism-surrounds-renowned-mathematician-s-attempted-proof-160-year-old-hypothesis) |
| 2021 | Liquid Tensor Experiment: Scholze's theorem is checked in Lean. | [Nature](https://www.nature.com/articles/d41586-021-01627-2) |
