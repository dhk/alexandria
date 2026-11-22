# 06: Precedents and context

## How mathematics has handled unusual proofs before

| Case | What was unusual | How trust was established | Time to acceptance | Lesson for RH-2026 |
|---|---|---|---|---|
| Four colour theorem (1976) | First major computer-assisted proof. Appel and Haken checked 1,834 configurations (later 1,482) using over 1,000 hours of computing. Ian Stewart called it "a kind of monstrous coincidence" ([Wikipedia](https://en.wikipedia.org/wiki/Four_color_theorem)) | Programs were independently re-run. Robertson–Sanders–Seymour–Thomas simplified it to 633 configurations (1996). Gonthier and Werner formalized it in Coq (2005), so that "it was necessary only to trust the Coq kernel" (same source) | About 30 years until full formal certainty. Some unease persists | Machine certainty can come long before human satisfaction. Coxeter thought it "very unlikely that anyone can break that proof down into something that one would regard as an ordinary proof" |
| Fermat's Last Theorem, Wiles (1993–95) | Announced in June 1993. Referee Nick Katz's questions exposed a gap in September 1993. Repaired with Taylor in September 1994 ([Wikipedia](https://en.wikipedia.org/wiki/Wiles%27s_proof_of_Fermat%27s_Last_Theorem)) | Human refereeing, then publication as a whole issue of the Annals (May 1995) | About 2 years | Human review finds gaps. An expert asking "why does this step work?" was the error detector |
| Kepler conjecture, Hales (1998–2017) | 250 pages plus 3 GB of code. A panel of 12 referees was "99% certain" after 4 years but could not certify the computations ([Wikipedia](https://en.wikipedia.org/wiki/Kepler_conjecture)) | The Flyspeck formal proof in HOL Light and Isabelle was completed in 2014 and published in 2017 | About 19 years | Formal proof was invented to break a refereeing deadlock. Hales estimated 20 years; it took about 11 |
| abc conjecture, Mochizuki (2012–) | Four long papers in a new theory (IUT). Scholze and Stix (2018) found a gap "so severe that ... small modifications will not rescue the proof strategy" ([Wikipedia](https://en.wikipedia.org/wiki/Abc_conjecture)) | It was published in RIMS (2021), a journal Mochizuki edits, and remains unaccepted | Not accepted | Publication is not acceptance. When understanding fails to transfer between people, the community stalls. RH-2026 is the mirror image: validity established without understanding |
| Atiyah's RH claim (2018) | A famous mathematician presented a 5-page argument. John Baez: "The proof just stacks one impressive claim on top of another" ([Science](https://www.science.org/content/article/skepticism-surrounds-renowned-mathematician-s-attempted-proof-160-year-old-hypothesis)) | Rejected by experts within days | Rejected | Reputation does not substitute for checkable content. Colleagues hesitated to criticize publicly (same source) |
| Liquid Tensor Experiment (2020–22) | Scholze asked the Lean community to check a theorem he was unsure of ([Nature](https://www.nature.com/articles/d41586-021-01627-2)) | Lean formalization. Nature reported "a bigger role for software in mathematics" | The key part was done within months, by June 2021 (dates from memory; verify) | Formalization can produce understanding. Scholze is widely reported to have said the process clarified his own proof. This is from memory and the fetched page did not include it, so verify before using it |
| Thurston's "On proof and progress" (1994) | An essay, not a proof | Argues that mathematics advances human understanding, which formal proof does not capture ([arXiv](https://arxiv.org/abs/math/9404236)) | — | This is the canonical text for the "why?" camp (Radziwiłł, Lamzouri, van Erp) |

## What is new in 2026

1. **Scale.** 17.4 M lines; 175,187 files; 818,755 theorems ([verification NOTES](https://github.com/leanprover-community/riemann-hypothesis/blob/main/verification/NOTES.md)). The prose version ran past 250,000 pages ([New Scientist](https://www.newscientist.com/article/2600134-anthropic-mathematician-claims-ai-assisted-proof-of-the-riemann-hypothesis/)). No human can read it in a lifetime.
2. **Verification arrived before understanding.** The pattern of the four colour theorem and Kepler is reversed and compressed. The checks reached strong formal confidence in about a day ([Lean community blog](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)), and understanding is projected to take weeks to years.
3. **A verification ecosystem built in advance.** By late 2026 the tools were already in place:
   - Comparator;
   - verified kernels;
   - many independent kernels;
   - Buzzard's checklist;
   - a community repository with CI.

   These were assembled during the 2026 run of AI-generated mathematics ([Xena Project](https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/)).
4. **AI on both sides.** AI produced the proof and also helped check it. Sutherland ran checks "with Claude Code" ([MIT](https://math.mit.edu/~drew/grh/)), and AI found problems in the human competitor ([The Defiant](https://thedefiant.io/frontier/ai/masullo-s-riemann-claim-draws-ai-assisted-objections)). Humans use AI to "informalise the Lean proof back into English" ([Xena Project](https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/)).
5. **Commercial context.** The announcement came the day after the IPO ([New Scientist](https://www.newscientist.com/article/2600134-anthropic-mathematician-claims-ai-assisted-proof-of-the-riemann-hypothesis/)). It followed a year of lab "theorem dumps" that Tao said may harm the field ([New Scientist](https://www.newscientist.com/article/2592421-openai-announces-722-mathematical-discoveries-in-one-go/)).

## The 2026 AI-mathematics wave in brief

- **Anthropic zeta work (Aug).** The proven share of zeros on the critical line rose to about 67%. Anthropic explicitly said this would not lead to RH ([Anthropic](https://www.anthropic.com/research/riemann-zeta)).
- **FLT formalized (Sep).** 13 M lines in 11 days ([Anthropic](https://www.anthropic.com/research/formalizing-fermats-last-theorem)).
- **OpenAI's Navier–Stokes claim (Sep).** Shadowed by credit disputes and divergence between the PDF and the Lean code ([Xena Project](https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/)).
- **OpenAI's 722 papers (Oct).** These included quasi-RH, with a zero-free region of Re s > 7/8. Radziwiłł called it "staggering" but "horribly written" ([Quanta](https://www.quantamagazine.org/ai-proved-the-quasi-riemann-hypothesis-what-happens-now-20261019/)). About 38 of 290 Lean files did not state the paper's main theorem ([Xena Project](https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/)). Three Hodge papers were withdrawn ([The Dartmouth](https://www.thedartmouth.com/article/2026/10/rodriguez-nagle-dartmouth-mathematicians-weigh-artificial-intelligences-role-in-the-future-of-their-work)).
- **Other formal results.** Axiom's CFSG formalization relied on AI-written definitions that no human has checked ([Xena Project](https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/)).
- **Norms response.** The Advisory Group on Mathematics and AI asked labs to disclose prompts, costs, and failures ([New Scientist](https://www.newscientist.com/article/2592421-openai-announces-722-mathematical-discoveries-in-one-go/)).

The 2026 sources here are recent news coverage and community posts, so treat them as snapshots that may be revised.
