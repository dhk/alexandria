# Conversation 2: Adjudicating the claims

Goal: separate the different kinds of claims being made, decide what evidence each kind needs, and see why reasonable experts disagree.

## Pre-reading
- [02 How the Lean process works](02_how_the_lean_process_works.md)
- [04 Perspectives](04_perspectives.md)
- [05 Competing claim](05_competing_claim_masullo.md)
- [11 Claim ledger](11_claim_ledger.md)

## There are several separate claims here

| # | Claim | Kind of claim | Evidence that would settle it | Current state |
|---|---|---|---|---|
| 1 | The Lean statement is the standard RH. | Semantic or definitional | Expert reading, cross-formalization equivalence, and consequences such as Robin's inequality | Strongly supported ([01](01_statement_check.md)) |
| 2 | The Lean proof is valid. | Formal | Compilation, an axiom audit, a comparator run, and independent kernels | Strongly supported. Three official-kernel runs on the full export were still running at 12:55 UTC on 21 Nov ([MIT](https://math.mit.edu/~drew/grh/)) |
| 3 | Therefore RH is true. | Mathematical | Claims 1 and 2, plus trust in the foundations | Follows if claims 1 and 2 hold. This is the Lean FRO's position ([Lean community blog](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)) |
| 4 | RH is "proved" in the community's sense. | Social | Understanding, exposition, and general acceptance | Not yet. Radziwiłł and Sarnak tie the word "theorem" to understanding ([Quanta](https://www.quantamagazine.org/updates/transformation/); [Quanta](https://www.quantamagazine.org/ai-proved-the-quasi-riemann-hypothesis-what-happens-now-20261019/)) |
| 5 | Prize-eligible. | Institutional | Publication, two years of scrutiny, and general acceptance | Not started. Clay lists RH as "Unsolved" ([Clay](https://www.claymath.org/millennium/riemann-hypothesis/)) |
| 6 | Alpöge deserves the credit, or Claude does. | Normative attribution | Knowing the division of labor: prompts, logs, and who contributed which ideas | Contested. Saha says Alpöge; Alpöge's own framing gives Claude the lead "near the finish line" |
| 7 | The timing was a PR move. | Motive | Internal communications | Alpöge denies it ("The precise timing is horrible"). It is unresolvable from public evidence |
| 8 | Masullo's human proof is correct. | Mathematical | Expert review or formalization | Problems were reported within hours, and the draft is under major revision |
| 9 | This shows AI can do superhuman science. | Interpretation or forecast | Repeated results across fields | SciAm's interpretation ([SciAm](https://www.scientificamerican.com/article/what-the-riemann-hypothesis-proof-really-means-about-ai-and-the-future/)). It goes beyond what the evidence shows |

## Why experts disagree

Most of the disagreement is about which claim each person is answering, not about the facts.

- **Verifiers** (Sutherland, Buzzard, Lean FRO) answer claims 1–3.
- **Understanding-first mathematicians** (Radziwiłł, Lamzouri, Sarnak, van Erp) answer claim 4. They think claim 4 is the one that matters.
- **Critics of the political economy** (Granville, Guillen, Glazer) answer claims 6 and 7, and the wider question of what labs are doing to the field.
- **The awed** (Strogatz, Keating, Skorobogatov) react to claim 3 as true and talk about claim 9.

## Fault lines worth arguing

1. **"Does it matter that nobody understands it?"** On one side, Thurston and Radziwiłł: mathematics is human understanding. On the other, the formalist position: the statement is now known true, and understanding is a separate project. Buzzard's position in between is that understanding will come "in a matter of weeks" because people can now read Lean with AI help ([Al Jazeera](https://www.aljazeera.com/news/2026/11/21/riemann-hypothesis-has-the-worlds-most-famous-maths-problem-been-cracked)).
2. **"Is the trust base small enough?"** Buzzard says possible kernel bugs "do not matter" because there are many independent kernels. Commenters push back, arguing that joint bugs are possible and that Gödel limits self-verification ([Xena Project comments](https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/)). A useful framing from tchow8 in the same thread: assess the specific mechanisms by which this could go wrong.
3. **"Why trust a 17 M-line AI proof more than a 940-page human one?"** The formal proof's correctness can be checked mechanically, and the human draft's cannot. But the human draft could teach you something today.
4. **Conflict of interest everywhere.**
   - The claimant works at the lab that just went public.
   - The first checker used that lab's tool.
   - WaPo has a content partnership with a rival lab ([Washington Post](https://www.washingtonpost.com/technology/2026/11/20/using-anthropic-ai-mathematician-claims-have-solved-riemann-hypothesis/)).
   - This corpus was assembled by Claude.

   What makes the formal evidence robust to these conflicts is the use of independent kernels written by different people in different languages.

## Exercise

Take three quotes from [04](04_perspectives.md) that seem to contradict each other. For each one, identify which numbered claim above it addresses. How many of the contradictions disappear?

## Discussion questions

1. If you had to bet, what probability would you put on each of claims 1, 2, 4, and 8? What evidence would move you?
2. Sutherland put the chance of error at "approximately zero" ([SciAm](https://www.scientificamerican.com/article/the-ai-riemann-hypothesis-proof-is-almost-certainly-true-independent-mathematicians-attest/)), and the Kepler referees put their confidence at "99%". What has changed about where confidence comes from?
3. Should the word "proof" mean a verified formal derivation, or an argument that a community understands?
4. What would a fair credit statement for this result look like?
