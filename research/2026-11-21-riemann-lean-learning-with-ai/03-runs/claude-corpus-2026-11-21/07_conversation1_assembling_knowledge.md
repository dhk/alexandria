# Conversation 1: Assembling the knowledge

Goal: build a shared, sourced picture of what happened before anyone argues about what it means. The meta-lesson is about how a learner with AI builds a corpus quickly without losing provenance.

## Pre-reading
- [01 Statement check](01_statement_check.md), sections 1–3
- [03 Timeline](03_timeline.md)
- Primary artifacts:
  - [Alpöge's note](https://alpo.ge/remark.pdf)
  - [Mathlib's RH definition](https://github.com/leanprover-community/mathlib4/blob/v4.33.1/Mathlib/NumberTheory/LSeries/RiemannZeta.lean)
  - [Challenge.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/main/src/Challenge.lean)
  - [the MIT verification page](https://math.mit.edu/~drew/grh/)
  - [the Lean FRO statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)

## The source hierarchy for this event

1. **Artifacts** are things you can run or read directly: the Lean archive, Mathlib, `Challenge.lean`, `comparator.json`, and checker logs.
2. **First-person statements** come from the people who did the work: Alpöge's note, Sutherland's status page, Buzzard's blog, Tao's blog, the Lean FRO statement, and Vakil's post.
3. **Expert quotes as relayed by journalists**: Quanta, Science, New Scientist, Nature, The Economist, SciAm, IBM Think, Al Jazeera, WaPo, and NYT.
4. **Aggregators and derivative writing**: Wikipedia, The Decoder, The Defiant, dev.to, mathscholar, and Convika.
5. **Social posts and comment threads**: X, Hacker News, and blog comments.

Several pieces have already changed shape as they moved down this chain. [11 Claim ledger](11_claim_ledger.md) logs examples. For instance, Al Jazeera quoted only the first half of Alpöge's self-correction, "Claude far outpaced me near the finish line", while The Economist printed it together with the correction that follows ([Al Jazeera](https://www.aljazeera.com/news/2026/11/21/riemann-hypothesis-has-the-worlds-most-famous-maths-problem-been-cracked); [The Economist](https://www.economist.com/science-and-technology/2026/11/20/ai-may-have-solved-the-most-important-problem-in-mathematics)).

## Core concepts to establish

- **RH in one line.** Every non-trivial zero of ζ has real part 1/2.
- **GRH as used here.** The same statement, applied to every Dirichlet L-function. It is not the Extended or Grand RH.
- **Statement vs proof.** Buzzard: "humans are very good at referring to both ideas as 'a theorem'" ([Xena Project](https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/)).
- **What the evidence currently shows.** Formal validity is established to a very high standard. Human understanding is close to zero. Social acceptance is in progress. The prize process has not started.

## Exercise for the group (about 30 minutes)

Give each person one primary artifact and one news article about it. Each person reports back three things:
1. One fact the article got exactly right.
2. One fact that drifted from the artifact.
3. One thing the article claims that no artifact could tell you, such as motive, meaning, or significance.

## Discussion questions

1. Which sources did you trust before reading them, and why? Was it the institution, the person, or the format?
2. Within about 24 hours, a non-specialist could assemble most of what experts knew. What still required an expert?
3. A Lean file can be checked by anyone with a big enough machine. Does that make expertise less necessary, or does it just move expertise to new places such as writing statements, running kernels, and reading definitions?
4. When you used an AI to help assemble this, where did it save time, and where did you have to go back to the artifact?

## AI-and-learning angle

This conversation models a learning workflow: collect everything, tag where each piece came from, then read the primary artifacts. In this case the AI was fast at the first step but needed checking on attribution. Garbled extractions, such as the Science page, and secondhand quotes both need verification. One question for the group to keep returning to is whether an AI-assembled corpus counts as knowledge, or only as a map to knowledge.
