# Conversation 4: What it means to learn in an age of AI

Goal: move from "what happened in mathematics" to "how should we learn, and what is learning for, when machines can produce verified answers faster than we can understand them?"

## Pre-reading
- [04 Perspectives](04_perspectives.md), sections C and H
- [The Dartmouth piece](https://www.thedartmouth.com/article/2026/10/rodriguez-nagle-dartmouth-mathematicians-weigh-artificial-intelligences-role-in-the-future-of-their-work)
- Thurston, ["On proof and progress in mathematics"](https://arxiv.org/abs/math/9404236)

## Five tensions

1. **Answer vs understanding.** van Erp: "Just answering the questions is not the point" ([The Dartmouth](https://www.thedartmouth.com/article/2026/10/rodriguez-nagle-dartmouth-mathematicians-weigh-artificial-intelligences-role-in-the-future-of-their-work)). Lamzouri says the goal is to "explain them, teach them and build on them" ([IBM Think](https://www.ibm.com/think/news/anthropic-claude-riemann-hypothesis-math-proof)). RH-2026 is a clean case: the answer is known, and nobody yet knows why.
2. **The skills that rise and the skills that fall.** Saha predicts that asking questions, choosing directions, writing exposition, and conducting AI will matter more, and that "technical brilliance in constructing proofs may become less so" ([Al Jazeera](https://www.aljazeera.com/news/2026/11/21/riemann-hypothesis-has-the-worlds-most-famous-maths-problem-been-cracked)). Buzzard adds that "The AI doesn't have taste, not yet anyway" (same source).
3. **The telescope vs the alien.** Buzzard: "We've basically got our own telescope" (same source). DeDeo: "the alien spaceship has crashed" ([Science](https://www.science.org/content/article/ai-may-have-solved-math-s-greatest-mystery-can-humans-understand-answer)). These two images suggest different ways of learning. A telescope extends what you can see yourself. An alien artifact is something you study from outside.
4. **Meaning and motivation.**
   - Hanlon: the "emotional thrill" of being first ([The Dartmouth](https://www.thedartmouth.com/article/2026/10/rodriguez-nagle-dartmouth-mathematicians-weigh-artificial-intelligences-role-in-the-future-of-their-work)).
   - Alpöge, on the loss of a "principal guiding light" ([New Scientist](https://www.newscientist.com/article/2600134-anthropic-mathematician-claims-ai-assisted-proof-of-the-riemann-hypothesis/)).
   - Singer, a student: "I really enjoy doing mathematics… And I'm going to continue to do it" ([The Dartmouth](https://www.thedartmouth.com/article/2026/10/rodriguez-nagle-dartmouth-mathematicians-weigh-artificial-intelligences-role-in-the-future-of-their-work)).
5. **Access and concentration.** Buzzard says AI is starting to make mathematics more widely accessible, but breakthroughs sit with labs that have internal models ([Al Jazeera](https://www.aljazeera.com/news/2026/11/21/riemann-hypothesis-has-the-worlds-most-famous-maths-problem-been-cracked)). Guillen says "That ring should be melted and distributed" ([Science](https://www.science.org/content/article/ai-may-have-solved-math-s-greatest-mystery-can-humans-understand-answer)).

## Learning patterns visible in this episode

| Pattern | Who | What it suggests |
|---|---|---|
| Ask AI for the big picture first, then fill in details yourself | Bryce Kerr (UNSW Canberra): "I generally won't read AI papers directly"; he starts by asking AI to explain the "big picture" ([Quanta Transformation](https://www.quantamagazine.org/updates/transformation/)) | AI as a tutor that points you in the right direction |
| Informalise: have AI translate machine proofs back into English | Experts described by Buzzard ([Xena Project](https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/)) | Understanding is rebuilt by translating, not by reading every line |
| Community proof maps and named-theorem tables | GitHub issues [#5](https://github.com/leanprover-community/riemann-hypothesis/issues/5) and [#39](https://github.com/leanprover-community/riemann-hypothesis/issues/39); Jaswal's map | Learning in public, with each part linked back to its source |
| Run AI in a loop on a hard question, then correct it | van Erp on Baum–Connes ([The Dartmouth](https://www.thedartmouth.com/article/2026/10/rodriguez-nagle-dartmouth-mathematicians-weigh-artificial-intelligences-role-in-the-future-of-their-work)) | A human supervises an AI searcher |
| AI supplies background so you can "make the connection" | Yao Xiao (same source) | AI shortens the time to reach the frontier |
| A missing-background problem | van Erp: "AI talks as if I know everything that's ever been published" (same source) | Expert-level output can be unreadable to non-experts. Learning still needs scaffolding |
| A spec-first habit | dev.to: "Read the specification before the code" ([dev.to](https://dev.to/axrisi/riemann-hypothesis-lean-proof-what-the-checkers-actually-check-31i6)) | The skill that matters most is knowing what question has actually been answered |

## A working synthesis to argue with

Learning with AI seems to split into three activities:
1. **Specifying.** Know precisely what question is being asked. This is the statement-fidelity skill.
2. **Verifying.** Know how to tell whether an answer is right, without having to trust whoever produced it. This is the comparator and independent-kernels habit.
3. **Understanding.** Rebuild the "why" in your own head, well enough to teach it and extend it.

AI is very good at producing answers, and is getting good at helping with verification. Understanding still has to happen in a person. Buzzard's prediction that understanding will arrive "in a matter of weeks" is a bet that AI can speed up understanding too. That bet is testable over the coming weeks.

## Discussion questions

1. If a verified answer exists that nobody understands, is anything learned? By whom?
2. Which of your own skills are like "technical brilliance in constructing proofs", and which are like "asking the right questions"?
3. Is the student who keeps doing mathematics for the joy of it making a mistake, or protecting something important?
4. What would you want a 25-year-old to learn now? Compare van Erp's "I'd have to think twice" with Bartel's "we are needed more than ever" ([New Scientist](https://www.newscientist.com/article/2600235-mathematicians-are-amazed-by-holy-grail-proof-of-riemann-hypothesis/)).
5. In this series you used an AI to learn about an AI result. What did you understand at the end that you did not understand at the start, and what did you only collect?
