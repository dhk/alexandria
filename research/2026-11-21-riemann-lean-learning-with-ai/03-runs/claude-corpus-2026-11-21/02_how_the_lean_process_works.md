# 02: How the Lean process works, explained for non-specialists

This file explains what "checked in Lean" means and what it does not mean. It is written for someone who builds software rather than proves theorems.

## If you have never seen Lean (a five-minute read)

**What it is.** Lean is software that checks mathematical arguments the way a spell-checker checks spelling. The difference is that Lean checks every step of the logic, and nothing gets waved through. You write a claim and an argument for it in a precise computer language. Lean either accepts the argument or points to the exact step that doesn't follow.

**A tiny example.** This is a complete Lean "theorem" with a statement and a proof:

```lean
theorem two_plus_two : 2 + 2 = 4 := rfl
```

The part before `:=` is the claim. The part after it is the argument; `rfl` roughly means "both sides compute to the same thing". If you changed the claim to `2 + 2 = 5`, Lean would refuse it. The RH proof works the same way. The claim is one line. The argument is 17.4 million lines, which no person has read ([verification NOTES](https://github.com/leanprover-community/riemann-hypothesis/blob/main/verification/NOTES.md)).

**Why anyone trusts it without reading it.** Everything in Lean ultimately passes through a small core program called the kernel. Its only job is to check each step. The clever parts are untrusted, and that includes the AI that wrote the proof. If the kernel is correct, a proof it accepts is correct, no matter who or what wrote the proof. For extra assurance, people re-checked this proof with several independently written kernels, in different programming languages and by different people. One of them comes with a mathematical proof that it can't accept a false argument ([Lean community blog](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)). A forged proof would have to fool all of them at once.

**The catch: Lean checks the argument, not the question.** Lean proves exactly the claim it is given. If the claim is worded wrong, Lean will happily prove the wrong thing. Buzzard gives an example ([Xena Project](https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/)). A natural-looking Lean version of Fermat's Last Theorem is false, because Lean's counting numbers include 0, and 0 + 0 = 0 is a counterexample. So the first and most human question is always: does the Lean claim say what mathematicians mean? For RH, the claim was written by people years ago and kept in Mathlib, Lean's shared, human-reviewed library. It wasn't written by the AI. That is why the statement check in [01](01_statement_check.md) matters so much.

**What a "yes" from Lean does and doesn't tell you.**

| Lean can tell you | Lean cannot tell you |
|---|---|
| Every step of the argument follows from the rules of mathematics | Why the result is true, or what the key idea is |
| The proof uses no hidden assumptions beyond the standard foundations | Whether the claim was worded to mean what people intended (humans check that) |
| The answer is the same no matter who runs the check | Whether the result is important, elegant, or teachable |

**An everyday analogy.** Think of a building inspector with a precise checklist. The inspector can certify that every beam meets code without understanding the architect's design. They can't tell you whether you got the house you asked for. That depends on whether the blueprint you handed over was the right one. Lean is the inspector. The Mathlib statement is the blueprint. Understanding the design is the work mathematicians are starting now.

**Glossary.**
- **Proof assistant:** software that checks proofs step by step; Lean is one.
- **Mathlib:** Lean's large, community-maintained library of mathematical definitions and results.
- **Kernel:** the small trusted core that has the final say.
- **Compile:** have Lean process the whole proof. For this proof that takes 7–10 hours on a very large machine ([verification NOTES](https://github.com/leanprover-community/riemann-hypothesis/blob/main/verification/NOTES.md)).
- **Axioms:** the agreed starting rules of mathematics. This proof uses only Lean's three standard ones ([MIT](https://math.mit.edu/~drew/grh/)).
- **Comparator:** a tool that confirms the giant proof proves exactly the trusted claim, not a lookalike.
- **Formalization:** turning ordinary mathematical writing into Lean.

The rest of this file goes one level deeper.

## The one-paragraph version

Lean is a programming language and proof assistant. In Lean, a mathematical statement is a type, and a proof is a program whose type is that statement. A small trusted core called the kernel checks that the program really has that type. Mathlib is Lean's large, human-curated library of definitions and theorems.

If the kernel accepts a term of type `RiemannHypothesis` and the term uses only the standard axioms, then the statement follows from those axioms. That conclusion holds even if no human ever reads the 17 million lines of proof. Everything else in the checking process is about closing the gaps around that core guarantee.

## The pipeline, step by step

Buzzard's four-question checklist ([Xena Project, 12 Nov 2026](https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/)) supplies the backbone. The Lean FRO's four criteria ([Lean community blog](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)) map onto it.

| # | Question | Tooling | What it catches | Status for RH |
|---|---|---|---|---|
| 1 | Does the Lean statement mean what mathematicians mean? | Human reading; reuse of a vetted Mathlib definition; cross-formalization equivalence | Wrong definitions, missing hypotheses, ℕ-contains-0 style traps | Mathlib's long-standing `RiemannHypothesis`. Equivalence with DeepMind's GRH statement machine-checked ([issue #34](https://github.com/leanprover-community/riemann-hypothesis/issues/34)). See [01](01_statement_check.md). |
| 2 | Does it compile? | `lake build` | Syntax and type errors, missing proofs | Pass: 175,187 modules, 0 errors ([MIT](https://math.mit.edu/~drew/grh/)). This takes 7–10 h on 48 cores and 503 GB of RAM ([NOTES](https://github.com/leanprover-community/riemann-hypothesis/blob/main/verification/NOTES.md)). |
| 3 | Does it prove that exact statement, using only the allowed axioms? | `#print axioms`; `lake comparator`; con-leche `--compare` | A theorem with the right name and the wrong content; `sorry`; smuggled-in axioms; `native_decide` | Axioms are only `propext`, `Classical.choice`, `Quot.sound`. con-leche `--compare` reports all 5 theorems "justified" ([MIT](https://math.mit.edu/~drew/grh/)). A static scan found no `sorry`, no `axiom`, and no `native_decide` ([NOTES](https://github.com/leanprover-community/riemann-hypothesis/blob/main/verification/NOTES.md)). |
| 4 | Does it exploit a bug in Lean's kernel? | `lake comparator --paranoid`; independent kernels run on an exported proof | Reward hacking against one implementation | nanoda (Rust), lean4lean, and con-leche (proven consistent relative to set theory) accept ([MIT](https://math.mit.edu/~drew/grh/); [Lean community blog](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)). |

### Key concepts

- **Kernel.** This is the small program that has the final say. The design idea is called the de Bruijn criterion: keep the trusted part tiny so the large, clever parts (tactics, automation, AI) can be untrusted.
- **Elaborator and tactics.** These turn human-friendly or AI-generated scripts into kernel terms. They are untrusted. This proof uses custom `kexactB`/`kcopy` tactics that bypass elaborator type-checking in 67 files, so in those places the kernel is the only check ([NOTES](https://github.com/leanprover-community/riemann-hypothesis/blob/main/verification/NOTES.md)). That is legitimate, and it is the reason independent kernels matter so much here.
- **Export.** Lean writes the fully elaborated proof into a plain data file. Here that file is 61.57 GB ([MIT](https://math.mit.edu/~drew/grh/)). Other kernels can check the export without running any of the original, potentially malicious, build code. The Lean FRO calls this "an inert export" ([Lean community blog](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)).
- **Comparator.** It checks that the theorem in a small trusted file (`Challenge.lean`, which imports only Mathlib) is identical to the theorem proved through the huge untrusted imports. It also checks that only permitted axioms appear ([Xena Project](https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/)). This is the specification-versus-implementation pattern, and it carries straight over to AI-written code ([dev.to](https://dev.to/axrisi/riemann-hypothesis-lean-proof-what-the-checkers-actually-check-31i6)).
- **Independent kernels.** A forged proof would have to exploit "as-yet-undiscovered bugs in many independent systems all at once" ([Xena Project](https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/)). Lean began shipping verified kernels in October 2026, per Leo de Moura's post cited in the same thread.
- **Trusted Mathlib.** Comparator assumes Mathlib is genuine. Sutherland checked that the Mathlib build artifacts match the official cache byte for byte ([MIT](https://math.mit.edu/~drew/grh/)).

## Who did what

The checking work was spread across several groups:

- **Alpöge** released 14 archive parts, about 239 MB compressed, and published no prose proof ([Alpöge note](https://alpo.ge/remark.pdf); [dev.to](https://dev.to/axrisi/riemann-hypothesis-lean-proof-what-the-checkers-actually-check-31i6)).
- **Andrew Sutherland (MIT)** ran the first complete compile and many of the independent kernels. He did this with Claude Code and posted live status ([MIT](https://math.mit.edu/~drew/grh/)).
- **The Lean community** set up a Comparator harness and a build cache in [leanprover-community/riemann-hypothesis](https://github.com/leanprover-community/riemann-hypothesis). Dozens of people compiled the code and got the same export ([Lean community blog](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)).
- **Volunteers** opened GitHub issues:
  - a reduced build, whose author corrected his own estimate from "55%" down to about 9% savings ([issue #3](https://github.com/leanprover-community/riemann-hypothesis/issues/3));
  - a reader's proof-strategy map ([issue #5](https://github.com/leanprover-community/riemann-hypothesis/issues/5));
  - a reproducibility bug, where `.olean` hashes embed the absolute build path ([issue #6](https://github.com/leanprover-community/riemann-hypothesis/issues/6));
  - the formal-conjectures equivalence ([issue #34](https://github.com/leanprover-community/riemann-hypothesis/issues/34));
  - a table of 105 named classical theorems found inside the archive ([issue #39](https://github.com/leanprover-community/riemann-hypothesis/issues/39)).

## What Lean does not give you

1. **Understanding.** Buzzard: "At the minute, we don't even know why the theorem is true" ([Al Jazeera](https://www.aljazeera.com/news/2026/11/21/riemann-hypothesis-has-the-worlds-most-famous-maths-problem-been-cracked)). Lamzouri: "Mathematics is mainly about understanding why something is true" ([IBM Think](https://www.ibm.com/think/news/anthropic-claude-riemann-hypothesis-math-proof)).
2. **A correct paper.** A paper can be wrong even when its Lean code is right. The Navier–Stokes write-up has "instances where the pdf proof and the Lean proof diverge" ([Xena Project](https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/)).
3. **Absolute certainty.** A commenter on Buzzard's post: "there are never any absolute guarantees in this business… The point is to analyze carefully the mechanisms by which something could go wrong, and assess the risk" (tchow8, [Xena Project comments](https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/)). Other commenters pushed back on Buzzard's line "this does not matter" about possible kernel bugs.
4. **Social acceptance or prizes.** The Clay rules require publication, two years, and general acceptance ([The Verge](https://www.theverge.com/ai-artificial-intelligence/1010051/anthropic-riemann-hypothesis-millennium-prize-problem)).
5. **Safety of running the code.** Buzzard: "do not run random Lean code on your local machine unless you sandbox it first… AI-generated code is not [safe]" ([Xena Project](https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/)).

## Analogy for product people

| Software world | Lean world |
|---|---|
| API contract or spec | `Challenge.lean` (statement only, imports only Mathlib) |
| Implementation by an untrusted vendor | 17 M lines of AI-generated proof |
| Contract test that the implementation satisfies the spec | Comparator |
| Running the test suite on two different CPUs or runtimes | Independent kernels |
| Pinned, signed dependencies | Mathlib v4.33.1 matching the official cache byte for byte |
| Running untrusted code in a sandbox | Inert export; bubblewrap |
| Code review for maintainability | Human understanding, which has not happened yet |

The [dev.to piece](https://dev.to/axrisi/riemann-hypothesis-lean-proof-what-the-checkers-actually-check-31i6) turns this into developer practice: "Read the specification before the code", ask what compares the proof to the statement, run a second checker written by someone else, and treat reproducibility as something to test.
