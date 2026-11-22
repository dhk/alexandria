# Conversation 3: How these systems fit together, and what is new

Goal: see the whole socio-technical system (people, tools, institutions, incentives) and compare it with how mathematics has established truth before.

## Pre-reading
- [06 Precedents and context](06_precedents_and_context.md)
- [02 How the Lean process works](02_how_the_lean_process_works.md), especially "Who did what"

## The system as it ran this week

```
Alpöge (direction, taste) ⇄ Claude (search, construction, Lean generation)
          │
          ▼
  17.4M-line Lean archive  ──►  Mathlib (human-curated definitions, incl. RiemannHypothesis)
          │
          ▼
  Community verification layer
    ├─ Compile (Sutherland, DeDeo, "dozens of people")
    ├─ Comparator: trusted Challenge.lean vs untrusted proof
    ├─ Independent kernels: Lean, nanoda (Rust), lean4lean, con-leche/con-ron (verified)
    ├─ Cross-formalization: formal-conjectures GRH equivalence (#34)
    └─ Consequence check: Robin/Lagarias inequalities (no zeta)
          │
          ▼
  Institutions: Lean FRO + Mathlib Initiative statement → journals? → Clay (2+ years)
          │
          ▼
  Understanding layer (just starting): proof maps (#5, Jaswal), named-theorem table (#39),
  AI-assisted "informalisation" back to English, Alpöge's promised write-up
          │
          ▼
  Media and markets: press wave, IPO timing, rival-lab context
```

Sources: [Lean community blog](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/); [MIT](https://math.mit.edu/~drew/grh/); [GitHub issues](https://github.com/leanprover-community/riemann-hypothesis/issues); [Tao comments](https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/).

## What carries over from the past

| Pattern | Past example | 2026 version |
|---|---|---|
| Announcement comes before acceptance | Wiles 1993 | Alpöge, 20 Nov |
| An expert's questions surface problems | Katz's questions to Wiles | AI-assisted readers finding problems in Masullo's draft within hours |
| Computer-assisted proofs cause discomfort | The four colour theorem, "monstrous coincidence" | "Alien spaceship has crashed" (DeDeo); "gobbledygook" (Buzzard) |
| Formalization resolves a refereeing deadlock | Kepler and Flyspeck | The whole RH verification took about a day |
| Publication is not acceptance | Mochizuki and RIMS | Clay's two-year rule |
| Reputation is not evidence | Atiyah 2018 | The verifiers explicitly ignore who Alpöge is and check the artifact |

## What is different

1. **Order reversed.** Historically, understanding came first and verification followed, if it happened at all. Now verification comes first and understanding follows, if it happens at all.
2. **Trust moved from people to a small, checkable core.** The trust base is the kernels plus Mathlib's definitions, plus an independent consequence check (Robin's inequality). It is no longer referees reading every step.
3. **Speed and scale.** Seventeen million lines were produced in weeks and checked in a day. Referees for Kepler took four years and reached 99%.
4. **AI is on every layer.** It generated the proof, ran the checks (Claude Code), did the critical reading (of Masullo's draft), and helps with understanding (informalisation).
5. **The work was distributed.** Verification was done by an open community that coordinated on GitHub and Zulip, not by a journal's referee panel.
6. **Capital and timing matter.** IPOs, rival labs, and "theorem dumps" set the tempo ([New Scientist](https://www.newscientist.com/article/2592421-openai-announces-722-mathematical-discoveries-in-one-go/)).

## What they have in common

Every one of these systems is a way of distributing trust. Each asks the same question: how can a community come to believe something no single member has fully checked? The tools have changed: referees, then reruns of programs, then proof assistants, then independent kernels. The underlying question has not.

## Bridges to software and product work

- `Challenge.lean` and Comparator are a spec and a contract test. The same pattern applies to AI-written code ([dev.to](https://dev.to/axrisi/riemann-hypothesis-lean-proof-what-the-checkers-actually-check-31i6)).
- Independent kernels are N-version programming.
- The "Internal" path convention, which separates human-vetted files from machine-generated proof material, is a provenance signal. A commenter on Buzzard's post proposed it ([Xena Project comments](https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/)).
- Reproducibility bugs, such as `.olean` hashes depending on the build path, are supply-chain hygiene ([issue #6](https://github.com/leanprover-community/riemann-hypothesis/issues/6)).

## Discussion questions

1. Which layer of this system would you remove last? Which is already redundant?
2. Where does trust really sit now: in Lean's kernel, in Mathlib's maintainers, in Sutherland's machine, or in the social fact that many independent people got the same answer?
3. The four colour theorem took about 30 years to go from computer proof to full formal certainty, and RH took about a day. What did the community build in between that made the difference?
4. What would this system look like for a scientific claim that cannot be formalized, such as a biology result?
