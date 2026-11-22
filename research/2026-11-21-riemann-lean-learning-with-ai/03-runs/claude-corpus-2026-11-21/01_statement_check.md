# 01 — Does the Lean statement match the standard Riemann hypothesis?

Status snapshot: Saturday 21 November 2026. Everything below is checked against primary artifacts (Mathlib source, the repository's challenge file, the comparator config) unless marked otherwise.

## Verdict

**Yes.** The headline theorem proves Mathlib's `RiemannHypothesis`. That is a faithful formalization of the standard statement: every non-trivial zero of the Riemann zeta function has real part 1/2. Machine comparison confirms that the submitted proof targets exactly this statement and not a lookalike.

There are three qualifications, and none of them weakens the RH verdict:

1. The "GRH" in the archive is GRH **for Dirichlet L-functions only**. It does not cover Dedekind zeta functions, Hecke L-functions, or general automorphic L-functions, so it is not the "Extended" or "Grand" RH. Alpöge's own note says he expects ERH "with more time" ([Alpöge note](https://alpo.ge/remark.pdf)), and Sutherland's page flags the naming explicitly ([MIT verification page](https://math.mit.edu/~drew/grh/)).
2. A Lean proof is only as trustworthy as its trust base: the kernel(s), the Mathlib definitions, the export pipeline, and the build environment. Section 4 explains why that base is unusually well covered here.
3. Statement fidelity is a separate question from understanding. Nobody yet understands why the proof works ([Al Jazeera, quoting Buzzard](https://www.aljazeera.com/news/2026/11/21/riemann-hypothesis-has-the-worlds-most-famous-maths-problem-been-cracked)).

## 1. The standard statement

The Riemann zeta function \( \zeta(s) = \sum_{n\ge1} n^{-s} \) for \( \operatorname{Re} s > 1 \) extends to a meromorphic function on \( \mathbb{C} \). Its only pole is a simple pole at \( s = 1 \). It vanishes at \( s = -2, -4, -6, \dots \), the "trivial zeros". **RH:** every other zero has \( \operatorname{Re} s = 1/2 \). This is the form in the Clay problem description, and Clay still lists the problem as "Unsolved" ([Clay Mathematics Institute](https://www.claymath.org/millennium/riemann-hypothesis/)).

## 2. The Lean statement (Mathlib v4.33.1)

Source: [Mathlib `RiemannZeta.lean` at tag v4.33.1](https://github.com/leanprover-community/mathlib4/blob/v4.33.1/Mathlib/NumberTheory/LSeries/RiemannZeta.lean)

```lean
/-- A formal statement of the **Riemann hypothesis** – constructing a term of this type is worth a
million dollars. -/
@[wikidata Q205966]
def RiemannHypothesis : Prop :=
  ∀ (s : ℂ) (_ : riemannZeta s = 0) (_ : ¬∃ n : ℕ, s = -2 * (n + 1)) (_ : s ≠ 1), s.re = 1 / 2
```

Read in English: for every complex number s, if ζ(s) = 0, s is not one of −2, −4, −6, …, and s ≠ 1, then Re s = 1/2.

### Line-by-line fidelity

| Standard RH | Lean | Comment |
|---|---|---|
| ζ is the analytic continuation of \( \sum n^{-s} \) | `riemannZeta` | Mathlib defines it through Hurwitz zeta and proves that it equals the Dirichlet series for Re s > 1 and is differentiable away from 1. Uniqueness of analytic continuation then pins it down. This is a fact about Mathlib, not something the RH submission controls. |
| "zero" | `riemannZeta s = 0` | Direct. |
| excluding trivial zeros −2, −4, … | `¬∃ n : ℕ, s = -2 * (n + 1)` | With n = 0, 1, 2, … this gives −2, −4, −6, …. It excludes exactly the trivial zeros and does not exclude 0. |
| ζ has a pole at 1 | `s ≠ 1` | Lean functions are total, so Mathlib assigns ζ a conventional ("junk") value at the pole. The hypothesis ensures that value cannot matter. |
| whole complex plane | `∀ s : ℂ` | The statement does not restrict to the critical strip. It covers every s, so it is at least as strong as "all non-trivial zeros lie on the line". Classical theory shows there are no zeros with Re s ≥ 1 or with Re s ≤ 0 other than the trivial ones, so the two formulations are equivalent. |
| conclusion | `s.re = 1 / 2` | Direct. |

**Known pitfall that this avoids.** Buzzard's checklist post shows how a plausible-looking Lean statement can be wrong. A Fermat's Last Theorem stated over ℕ is trivially false because ℕ contains 0. He also found that about 38 of 290 Lean-accompanied OpenAI papers "do not even state, let alone prove, the main theorem of the paper" ([Xena Project](https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/)). The RH statement is not AI-written. It has been in human-curated Mathlib, which Buzzard describes as "human-curated and checked by human experts" (same post).

## 3. What the submission actually proves

The community verification repository is [leanprover-community/riemann-hypothesis](https://github.com/leanprover-community/riemann-hypothesis) (formerly `Deicyde/riemann-hypothesis`). It wraps Alpöge's unmodified source.

- `src/Main.lean` contains `theorem riemannHypothesis : RiemannHypothesis := rhOfAll`, plus four companion theorems.
- The trusted [`src/Challenge.lean`](https://github.com/leanprover-community/riemann-hypothesis/blob/main/src/Challenge.lean) imports only Mathlib and restates all five theorems with `sorry`:

```lean
import Mathlib

def RiemannZetaZerosOnLine : Prop :=
  ∀ s : ℂ, riemannZeta s = 0 → (¬∃ n : ℕ, s = -2 * ((n : ℂ) + 1)) → s ≠ 1 → s.re = 1 / 2

def DirichletLNonvanishingRightOfHalf : Prop :=
  ∀ (N : ℕ) [NeZero N] (χ : DirichletCharacter ℂ N) (s : ℂ),
    1 / 2 < s.re → (χ ≠ 1 ∨ s ≠ 1) → DirichletCharacter.LFunction χ s ≠ 0

def DirichletLZerosOnLine : Prop :=
  ∀ (N : ℕ) [NeZero N] (χ : DirichletCharacter ℂ N) (s : ℂ),
    0 < s.re → s.re < 1 → DirichletCharacter.LFunction χ s = 0 → s.re = 1 / 2

def PrimitiveDirichletLZerosOnLine : Prop :=
  ∀ (N : ℕ) [NeZero N] (χ : DirichletCharacter ℂ N), χ.IsPrimitive →
    ∀ s : ℂ, 0 < s.re → s.re < 1 → DirichletCharacter.LFunction χ s = 0 → s.re = 1 / 2

/-- The headline claim, stated with Mathlib's definition only. -/
theorem riemannHypothesis : RiemannHypothesis := by sorry
theorem riemannZeta_eq_zero_re : RiemannZetaZerosOnLine := by sorry
theorem LFunction_ne_zero_of_half_lt_re : DirichletLNonvanishingRightOfHalf := by sorry
theorem LFunction_eq_zero_re : DirichletLZerosOnLine := by sorry
theorem LFunction_eq_zero_re_of_isPrimitive : PrimitiveDirichletLZerosOnLine := by sorry
```

- [`comparator.json`](https://github.com/leanprover-community/riemann-hypothesis/blob/main/comparator.json) names these five theorems. It permits only the three standard axioms (`propext`, `Quot.sound`, `Classical.choice`) and adds two external kernels: Lean's paranoid checker and nanoda.

### Why the Dirichlet statements look restricted (and why that is correct)

- `DirichletLZerosOnLine` only speaks about 0 < Re s < 1. That restriction is necessary. For imprimitive characters, including the trivial character mod N, the L-function picks up Euler-factor zeros on Re s = 0. A statement over the whole plane would be false, so restricting it is the correct choice.
- `DirichletLNonvanishingRightOfHalf` excludes the pair (χ = 1, s = 1), where the L-function of the trivial character has its pole.
- The primitive version was machine-checked to be equivalent to Google DeepMind's independently written [formal-conjectures GRH statement](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/Millennium/RiemannHypothesis.lean#L83), using only standard axioms ([repository issue #34](https://github.com/leanprover-community/riemann-hypothesis/issues/34)). That gives two independent human formalizations that agree.

## 4. How the match is checked mechanically

- **Comparator.** It checks that the theorem stated in the trusted file and the theorem delivered through untrusted imports are identical, and that only the axioms of mathematics are used ([Xena Project](https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/)).
- **con-leche `--compare`.** It found all five theorems "justified by the solution" against the challenge ([MIT verification page](https://math.mit.edu/~drew/grh/)).
- **The Lean FRO and Mathlib Initiative joint statement.** It lists "statement correct (Mathlib's, vetted)" as the first of four criteria and states: "We have full confidence that Alpöge's proof of the Riemann Hypothesis is correct" ([Lean community blog](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)).
- **A cross-check from outside zeta entirely.** Sutherland combined the proof with an independent formalization of Robin's 1984 criterion (`kimihiro64/Robin1984`). That yields `robin_inequality` and `lagarias_inequality`: statements about divisor sums with no hypotheses and no mention of zeta. All checks passed except a still-running `lake comparator` stage ([MIT verification page](https://math.mit.edu/~drew/grh/)).
  - Robin's theorem says \( \sigma(n) < e^{\gamma} n \log\log n \) for all n > 5040 if and only if RH holds ([Wikipedia: divisor function](https://en.wikipedia.org/wiki/Robin%27s_theorem)).
  - The point of the cross-check: even if `riemannZeta` were subtly mis-defined, the conclusion would still be an elementary inequality about integers that is classically equivalent to RH. Sutherland notes that this "effectively rules out holes in the definitions", while still relying on the kernels and on Mathlib's definitions being as intended ([dev.to summary of Sutherland's Zulip remarks](https://dev.to/axrisi/riemann-hypothesis-lean-proof-what-the-checkers-actually-check-31i6)).

## 5. Residual trust base (what you still have to believe)

| Item | Risk | Mitigation in this case |
|---|---|---|
| Lean kernel bug | A proof exploits an unsound kernel. | Independent kernels in Rust (nanoda), in Lean (lean4lean), and con-leche/con-ron, which are formally proven sound relative to set theory, all accepted ([Lean community blog](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/); [MIT](https://math.mit.edu/~drew/grh/)). |
| Elaborator bypass | The source uses `kexactB`/`kcopy` tactics that skip elaborator type checks in 67 files ([verification NOTES](https://github.com/leanprover-community/riemann-hypothesis/blob/main/verification/NOTES.md)). | This is sound because the kernel still checks every term. It is also exactly why kernel independence matters. |
| Tampered Mathlib | Comparator cannot detect a modified Mathlib. | Sutherland reports that 8,322 Mathlib and 378 dependency `.olean` files match the official cache byte for byte ([MIT](https://math.mit.edu/~drew/grh/)). |
| Malicious build code | Lean code can run arbitrary programs at compile time. | The Lean FRO checks ran on "an inert export" ([Lean community blog](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)). Sutherland's builds were unsandboxed, which he discloses. |
| Mathlib definitions wrong | `riemannZeta` might not mean ζ. | Long human curation, the Robin/Lagarias cross-check, and the equivalence with formal-conjectures. |
| Older-version kernel quirks | Lean 4.33.1 lacks some later fixes. | Judging used Lean 4.36.0 tooling plus independent checkers ([verification NOTES](https://github.com/leanprover-community/riemann-hypothesis/blob/main/verification/NOTES.md)). |

## 6. Live status (as of the MIT page update, 21 Nov 2026 12:55 UTC)

All of these have passed or accepted:

- the full compile;
- the axiom audit;
- the Mathlib byte match;
- `leanchecker` replay of all 175,187 modules;
- nanoda;
- con-leche `--verified` and `--compare`;
- lean4lean.

Three slow, single-threaded runs were still **running**: the Lean default kernel on the full export, the Lean paranoid kernel on the full export, and `lake comparator` end to end. In the comparator run, statement comparison and the axiom check had already passed ([MIT verification page](https://math.mit.edu/~drew/grh/)). The repository's own NOTES still said "The build is in progress" ([verification NOTES](https://github.com/leanprover-community/riemann-hypothesis/blob/main/verification/NOTES.md)). The Lean FRO statement was published at 13:55 on the same day and expresses "full confidence" ([Lean community blog](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)).

The Clay Institute's acceptance standard is separate from all of this. It requires publication, two years of scrutiny, and "general acceptance in the global mathematics community" ([The Verge](https://www.theverge.com/ai-artificial-intelligence/1010051/anthropic-riemann-hypothesis-millennium-prize-problem)).
