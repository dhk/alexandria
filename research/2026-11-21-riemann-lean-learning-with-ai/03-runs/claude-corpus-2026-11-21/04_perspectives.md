# 04: Perspectives

People are grouped by the main question each one is answering. Many people appear in more than one group. Quotes are verbatim as they appear in the cited outlet. "Caution" notes mark places where the source text was garbled or where outlets disagree.

## A. The claimant

| Person | Role | What they said | Source |
|---|---|---|---|
| Levent Alpöge | Mathematician at Anthropic | "I believe I have, working with Claude, discovered a proof of the Riemann Hypothesis. In fact, the method easily extends much further, resolving the so-called Generalized Riemann Hypothesis, and I expect, with more time, the Extended Riemann Hypothesis too." | [Alpöge note](https://alpo.ge/remark.pdf), as quoted by [The Verge](https://www.theverge.com/ai-artificial-intelligence/1010051/anthropic-riemann-hypothesis-millennium-prize-problem) |
| | | On roles: "Claude far outpaced me near the finish line," which he follows immediately with "No, Claude flew, and danced, and sparkled near that finish line." | [The Economist](https://www.economist.com/science-and-technology/2026/11/20/ai-may-have-solved-the-most-important-problem-in-mathematics) |
| | | On the write-up, he says it would be "obviously inappropriate to attempt to post some massive unreadable travesty of 'slop'". He reports that the prose version ran past 250,000 pages. | [New Scientist](https://www.newscientist.com/article/2600134-anthropic-mathematician-claims-ai-assisted-proof-of-the-riemann-hypothesis/) |
| | | On timing: "The precise timing is horrible." He spoke to Amodei and found "there was a constraint to respect". | [New Scientist](https://www.newscientist.com/article/2600134-anthropic-mathematician-claims-ai-assisted-proof-of-the-riemann-hypothesis/) |
| | | On understanding: "An astounding amount of mathematics is present in the argument… My intuition insists it will be massively simplified, likely immediately." He also says: "I intend to do my best to understand and impart understanding of this argument." | [Quanta](https://www.quantamagazine.org/updates/transformation/); [Tao comments](https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/) |
| | | On method: Stepanov's multiplicity method, mimicked by chained theta lifts. The number of lifts needed is about √X, which was Claude's key insight. | [The Decoder](https://the-decoder.com/hours-after-anthropic-claims-a-claude-proof-of-the-riemann-hypothesis-stanford-releases-an-all-human-competing-draft/) |

## B. Verifiers: "Does the code prove the statement?"

| Person | Role | View | Source |
|---|---|---|---|
| Lean FRO and Mathlib Initiative | Institutions behind Lean and Mathlib | "We have full confidence that Alpöge's proof of the Riemann Hypothesis is correct." They base this on four criteria: statement, compile, comparator, and independent kernels. | [Lean community blog](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) |
| Andrew Sutherland | MIT number theorist | Did the first full compile and ran independent kernels with Claude Code. Combined the proof with Robin's criterion so the conclusion contains no zeta. Told SciAm the chance of error is "approximately zero". In October 2024 he had said: "An AI that can prove the Riemann hypothesis is not one I'd want to meet." | [MIT](https://math.mit.edu/~drew/grh/); [SciAm](https://www.scientificamerican.com/article/the-ai-riemann-hypothesis-proof-is-almost-certainly-true-independent-mathematicians-attest/); [The Decoder](https://the-decoder.com/hours-after-anthropic-claims-a-claude-proof-of-the-riemann-hypothesis-stanford-releases-an-all-human-competing-draft/) |
| Kevin Buzzard | Imperial College London | On 20 Nov: "Let's see if it compiles first." In his checklist post: "'It's true because it's checked in Lean' can be made to make sense. But one has to do some work beyond 'the Lean code compiles'." | [New Scientist](https://www.newscientist.com/article/2600134-anthropic-mathematician-claims-ai-assisted-proof-of-the-riemann-hypothesis/); [Xena Project](https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/) |
| Simon DeDeo | Carnegie Mellon | Compiled the proof independently. "I'd be very surprised if there were any secret tricks." | [Quanta](https://www.quantamagazine.org/updates/transformation/) |
| Joachim Breitner | Lean community | Says the proof was "very very thoroughly checked". | [dev.to](https://dev.to/axrisi/riemann-hypothesis-lean-proof-what-the-checkers-actually-check-31i6) |
| Scott Aaronson | Computer scientist | Notes that no Lean-certified AI result has yet needed retraction, while several uncertified ones have. Says mathematicians will be satisfied only when they understand the proof themselves, not merely when they have 17 million lines of Lean. That will take time because humans "only move at biological speeds" (paraphrase plus quoted fragment). | [dev.to](https://dev.to/axrisi/riemann-hypothesis-lean-proof-what-the-checkers-actually-check-31i6); [New Scientist](https://www.newscientist.com/article/2600235-mathematicians-are-amazed-by-holy-grail-proof-of-riemann-hypothesis/) |
| Nikoloz Turazashvili | Developer, dev.to | Gives the verdict "NEEDS REVIEW": "I'd ship the checking and hold the conclusion." | [dev.to](https://dev.to/axrisi/riemann-hypothesis-lean-proof-what-the-checkers-actually-check-31i6) |

## C. Understanding first: "A proof is an explanation"

| Person | Role | View | Source |
|---|---|---|---|
| Maksym Radziwiłł | NYU | "The object of mathematics as the rest of science is really the question 'why?' and this doesn't answer it at all." He says the 4-page note has "nonsensical statements". | [Quanta](https://www.quantamagazine.org/updates/transformation/) |
| | | Says the episode fits "a particular narrative that these companies are promoting, which is that understanding is unnecessary". Caution: this comes from a garbled page extraction, so verify before quoting. | [Science](https://www.science.org/content/article/ai-may-have-solved-math-s-greatest-mystery-can-humans-understand-answer) |
| Youness Lamzouri | Univ. of Lorraine | "Mathematics is mainly about understanding why something is true… We need to understand the ideas in the proof well enough to explain them, teach them and build on them." | [IBM Think](https://www.ibm.com/think/news/anthropic-claude-riemann-hypothesis-math-proof) |
| James Maynard | Oxford, Fields Medal 2022 | "If this fully checks out, it is clearly a historic milestone." He adds: "somewhat frustratingly, it looks like it will require quite a lot of work to really gain this understanding." | [IBM Think](https://www.ibm.com/think/news/anthropic-claude-riemann-hypothesis-math-proof) |
| Terence Tao | UCLA | Calls the GRH proof the least "digested" of the three results. It appears to use deep Langlands-program and arithmetic-geometry machinery, when analytic methods alone had been thought insufficient. Notes that there is a human author to talk to. | [Tao](https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/) |
| Peter Sarnak | Princeton/IAS | On quasi-RH: it becomes "a Theorem" only when it is understood. | [Quanta](https://www.quantamagazine.org/ai-proved-the-quasi-riemann-hypothesis-what-happens-now-20261019/) |
| Erik van Erp | Dartmouth | "Just answering the questions is not the point… It's what it takes to solve the problem and what you learn in the process." | [The Dartmouth](https://www.thedartmouth.com/article/2026/10/rodriguez-nagle-dartmouth-mathematicians-weigh-artificial-intelligences-role-in-the-future-of-their-work) |
| Kevin Buzzard | Imperial | "At the minute, we don't even know why the theorem is true." Also: "That will change. In a matter of weeks, that will change." | [Al Jazeera](https://www.aljazeera.com/news/2026/11/21/riemann-hypothesis-has-the-worlds-most-famous-maths-problem-been-cracked) |

## D. Awe and the significance of the result

| Person | Role | View | Source |
|---|---|---|---|
| Steven Strogatz | Cornell | "This is like reaching Mount Olympus." | [NYT](https://www.nytimes.com/2026/11/20/science/anthropic-ai-math-riemann-hypothesis.html) |
| Jonathan Keating | Oxford | Quasi-RH "was itself a colossal shock… But this is several orders of magnitude more shocking." | [The Economist](https://www.economist.com/science-and-technology/2026/11/20/ai-may-have-solved-the-most-important-problem-in-mathematics) |
| Thomas Bloom | Manchester | "In proportion to the magnitude of this claim, we should be appropriately sceptical." If true, it would be "one of the greatest proofs in the history of mathematics". | [New Scientist](https://www.newscientist.com/article/2600235-mathematicians-are-amazed-by-holy-grail-proof-of-riemann-hypothesis/) |
| Rainer Dietmann | Royal Holloway | Calls it "like having found the Holy Grail", but says it "will massively amplify the despair by many in the mathematical community". | [New Scientist](https://www.newscientist.com/article/2600235-mathematicians-are-amazed-by-holy-grail-proof-of-riemann-hypothesis/) |
| Alexei Skorobogatov | Imperial | Compares it to aliens arriving. "The only event in history I can compare it to is the discovery of a nuclear bomb." | [New Scientist](https://www.newscientist.com/article/2600235-mathematicians-are-amazed-by-holy-grail-proof-of-riemann-hypothesis/) |
| Filippo Nuccio | Jean Monnet Univ. | "WOW, this is gorgeous: it basically contains all number theory produced in the last 50 years." | [Quanta](https://www.quantamagazine.org/updates/transformation/) |
| Abhishek Saha | QMUL | "This claimed proof, if correct, shatters my model of reality." Describes the proof as a "wormhole" through infrastructure that had been built for other problems. | [Al Jazeera](https://www.aljazeera.com/news/2026/11/21/riemann-hypothesis-has-the-worlds-most-famous-maths-problem-been-cracked) |
| James McKee | Royal Holloway | "It is both a wonderful time and a terrible time to be a research mathematician." | [New Scientist](https://www.newscientist.com/article/2600134-anthropic-mathematician-claims-ai-assisted-proof-of-the-riemann-hypothesis/) |
| DeDeo; Melanie Wood | CMU; Harvard | DeDeo: "the alien spaceship has crashed." Wood is optimistic about "incredible developments". | [Science](https://www.science.org/content/article/ai-may-have-solved-math-s-greatest-mystery-can-humans-understand-answer) |

## E. Credit: is this Alpöge's proof, or Claude's?

| Person | View | Source |
|---|---|---|
| Abhishek Saha | "Much of the press is referring to this as a proof by Claude. I think they should instead credit the person involved… He should get a Fields Medal for this." | [Al Jazeera](https://www.aljazeera.com/news/2026/11/21/riemann-hypothesis-has-the-worlds-most-famous-maths-problem-been-cracked) |
| Steven Strogatz | "A very skilled AI jockey riding a very fast AI horse." Caution: the NYT gives a different wording. | [Washington Post](https://www.washingtonpost.com/technology/2026/11/20/using-anthropic-ai-mathematician-claims-have-solved-riemann-hypothesis/) |
| Kevin Buzzard | "The AI doesn't have taste, not yet anyway. You tell it what to do, and it does it." | [Al Jazeera](https://www.aljazeera.com/news/2026/11/21/riemann-hypothesis-has-the-worlds-most-famous-maths-problem-been-cracked) |
| Quanta (editorial) | Alpöge's expertise drove repeated, iterative attempts. That contrasts with OpenAI's results, "almost all" of which came from a simple prompt. | [Quanta](https://www.quantamagazine.org/updates/transformation/) |
| Radziwiłł | Says the analysis work shifts onto people "who won't receive recognition". Caution: from a garbled page extraction. | [Science](https://www.science.org/content/article/ai-may-have-solved-math-s-greatest-mystery-can-humans-understand-answer) |

## F. Political economy: money, timing, and concentration

| Person | View | Source |
|---|---|---|
| Andrew Granville | Calls the 4-page note "garbled" and says Alpöge should have prepared a clearer write-up before announcing. Nature places this alongside the timing, just after the IPO. | [Nature](https://www.nature.com/articles/d41586-026-03812-7) |
| Eliot Glazer (as spelled by Science; described there as at Principia Labs) | "This may represent the most resources ever dedicated to a single problem in any time frame." | [Science](https://www.science.org/content/article/ai-may-have-solved-math-s-greatest-mystery-can-humans-understand-answer) |
| Nestor Guillen | "That ring should not be wielded by anyone—it should be melted and distributed." | [Science](https://www.science.org/content/article/ai-may-have-solved-math-s-greatest-mystery-can-humans-understand-answer) |
| Kevin Buzzard | Breakthroughs are concentrated in labs with internal models, but "this will change". | [Al Jazeera](https://www.aljazeera.com/news/2026/11/21/riemann-hypothesis-has-the-worlds-most-famous-maths-problem-been-cracked) |
| Ben Allanach | Says labs see mathematics as "an intellectual trophy". Asks: "Is it coming into the cadre of human knowledge?" | [New Scientist](https://www.newscientist.com/article/2592421-openai-announces-722-mathematical-discoveries-in-one-go/) |
| Terence Tao | On the OpenAI release: results being "dumped" on the community may harm the field. | [New Scientist](https://www.newscientist.com/article/2592421-openai-announces-722-mathematical-discoveries-in-one-go/) |
| Juliette Bruce; Kevin Ventullo | Bruce, in Tao's comments, criticizes the viral framing. Ventullo defends Alpöge. | [Tao comments](https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/) |
| Advisory Group on Mathematics and AI | Recommends that labs disclose the model, prompts, compute cost, failed attempts, and problem selection, and formalize as far as possible. | [New Scientist](https://www.newscientist.com/article/2592421-openai-announces-722-mathematical-discoveries-in-one-go/) |

## G. The human counter-claim

| Person | View | Source |
|---|---|---|
| Alessandro Masullo | Wrote a 940-page all-human draft. Its introduction reads: "We are still here. We are very much alive. We are not going anywhere." | [Washington Post](https://www.washingtonpost.com/technology/2026/11/20/using-anthropic-ai-mathematician-claims-have-solved-riemann-hypothesis/) |
| Brian Conrad | Stanford; Masullo's adviser and reviewer. "Remaining silent sets a narrative." He describes being "between a rock and a hard place". | [Science](https://www.science.org/content/article/ai-may-have-solved-math-s-greatest-mystery-can-humans-understand-answer); [Washington Post](https://www.washingtonpost.com/technology/2026/11/20/using-anthropic-ai-mathematician-claims-have-solved-riemann-hypothesis/) |
| Ravi Vakil | AMS president. First says the draft "is all human, with no AI". Later: "I make no claim as to the correctness of the proof strategy." | [The Decoder](https://the-decoder.com/hours-after-anthropic-claims-a-claude-proof-of-the-riemann-hypothesis-stanford-releases-an-all-human-competing-draft/) |

## H. Students and the next generation

| Person | View | Source |
|---|---|---|
| Asher Auel | Dartmouth. Students "are worried that they may not see a place for themselves… They are looking to us for guidance." | [The Dartmouth](https://www.thedartmouth.com/article/2026/10/rodriguez-nagle-dartmouth-mathematicians-weigh-artificial-intelligences-role-in-the-future-of-their-work) |
| Benjamin Singer | Dartmouth undergraduate. "I really enjoy doing mathematics… And I'm going to continue to do it." Calls errors in hyped work that are "covered up" "very unhealthy". | same |
| Yao Xiao | Dartmouth postdoc. AI helps "accelerate the whole process" by supplying the background needed to "make the connection". | same |
| Erik van Erp | "If I was 25, would I want to be a graduate doing math? I'd have to think twice." | same |
| Phil Hanlon | Values the "emotional thrill" of being first to see something: "I would hate to give all that up." | same |
| Alex Bartel | "We are needed more than ever." | [New Scientist](https://www.newscientist.com/article/2600235-mathematicians-are-amazed-by-holy-grail-proof-of-riemann-hypothesis/) |
| Abhishek Saha | Expects that "Asking the right questions… writing good expositions, and acting as an effective director or conductor for AI" will matter more, and "technical brilliance in constructing proofs may become less so". | [Al Jazeera](https://www.aljazeera.com/news/2026/11/21/riemann-hypothesis-has-the-worlds-most-famous-maths-problem-been-cracked) |
| Kevin Buzzard | "Historically, astronomers were just staring at the sky… And then the telescope was invented… We've basically got our own telescope." | same |
