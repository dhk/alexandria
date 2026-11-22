# 05: The competing claim from Masullo, Conrad, and Vakil

## What happened

- Hours after Alpöge's post on 20 November, Ravi Vakil (Stanford; AMS president) posted a "hurried announcement" sharing Alessandro Masullo's draft proof of GRH. The draft is about 940 pages and titled "The Music of the Primes" ([The Decoder](https://the-decoder.com/hours-after-anthropic-claims-a-claude-proof-of-the-riemann-hypothesis-stanford-releases-an-all-human-competing-draft/); [The Defiant](https://thedefiant.io/frontier/ai/masullo-s-riemann-claim-draws-ai-assisted-objections)).
- Vakil: "Brian Conrad has been looking closely at it for months and gave extensive feedback which is being incorporated, and it is so far looking good. It is all human, with no AI. The hope was to bring Alessandro to Stanford for a year to polish the writing… Now it seems best to put out the current draft" ([Quanta](https://www.quantamagazine.org/updates/transformation/)).
- About eight hours later, Vakil updated the post. Several people had reported problems, found with help from different AI models. He wrote: "As is usual, all issues need to be resolved to the satisfaction of the community before this proof would be accepted as true. (I make no claim as to the correctness of the proof strategy.)" ([The Decoder](https://the-decoder.com/hours-after-anthropic-claims-a-claude-proof-of-the-riemann-hypothesis-stanford-releases-an-all-human-competing-draft/)).
- Masullo himself said the draft needed significant revisions and was not ready for publication. Its introduction includes the line "We are still here. We are very much alive. We are not going anywhere." ([Washington Post](https://www.washingtonpost.com/technology/2026/11/20/using-anthropic-ai-mathematician-claims-have-solved-riemann-hypothesis/)).
- Conrad on why they released it early: "Remaining silent sets a narrative" ([Science](https://www.science.org/content/article/ai-may-have-solved-math-s-greatest-mystery-can-humans-understand-answer)). Masullo's earlier RH attempt from several years ago did not hold up, and number theorists are withholding judgment ([Quanta](https://www.quantamagazine.org/updates/transformation/)).

## Side-by-side

| Dimension | Alpöge + Claude | Masullo (with Conrad's review) |
|---|---|---|
| Artifact | 17.4 M lines of Lean, plus a 4-page note | A roughly 940-page human-readable PDF draft |
| Claimed scope | RH, plus GRH for Dirichlet L-functions | GRH (scope as described by Vakil) |
| Machine verification | Compiled and accepted by multiple independent kernels. Comparator statement check passed. Official kernel replay of the full export was still running at 12:55 UTC on 21 Nov ([MIT](https://math.mit.edu/~drew/grh/)) | None. Vakil urged translation into Lean ([The Decoder](https://the-decoder.com/hours-after-anthropic-claims-a-claude-proof-of-the-riemann-hypothesis-stanford-releases-an-all-human-competing-draft/)) |
| Human understanding | Essentially none yet ("we don't even know why the theorem is true", per Buzzard in [Al Jazeera](https://www.aljazeera.com/news/2026/11/21/riemann-hypothesis-has-the-worlds-most-famous-maths-problem-been-cracked)) | Readable in principle, and one senior expert reviewed it for months |
| Known problems | None found in the formal proof. The prose note was called "garbled" ([Nature](https://www.nature.com/articles/d41586-026-03812-7)) | Problems reported within hours, many found with AI help |
| Use of AI | Central | None in the writing; AI was used by the critics |
| Status | Strong formal evidence; unread | A disputed draft "undergoing major revision" (Conrad, via [dev.to](https://dev.to/axrisi/riemann-hypothesis-lean-proof-what-the-checkers-actually-check-31i6)) |

## Discrepancies across outlets (useful for conversation 2)

- **Conrad's role.** Some outlets call Conrad a reviewer giving feedback ([The Defiant](https://thedefiant.io/frontier/ai/masullo-s-riemann-claim-draws-ai-assisted-objections)), some call him Masullo's PhD adviser ([Washington Post](https://www.washingtonpost.com/technology/2026/11/20/using-anthropic-ai-mathematician-claims-have-solved-riemann-hypothesis/)), and the extracted Science text calls him a co-author ([Science](https://www.science.org/content/article/ai-may-have-solved-math-s-greatest-mystery-can-humans-understand-answer)). The page extraction was garbled, so the co-author claim is unconfirmed.
- **Masullo's affiliation.** Quanta cites a LinkedIn page that lists him as a Stanford postdoc ([Quanta](https://www.quantamagazine.org/updates/transformation/)). Science describes him as a mathematician in Rome (garbled extraction).
- **The headline.** The Decoder's headline says "Stanford releases" the draft. What actually happened is that a Stanford professor posted it on his personal blog.

## The irony worth discussing

The all-human proof was stress-tested by AI within hours. The AI proof is waiting on human understanding. Each method is strongest where the other is weakest. Formal checking answers "is it valid?" quickly but says nothing about "why?". Human prose carries the "why" but is slow and error-prone to validate.
