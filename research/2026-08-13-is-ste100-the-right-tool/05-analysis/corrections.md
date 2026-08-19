# Corrections

Per [AGENTS.md](../../../AGENTS.md) rule 5, published artifacts are not
rewritten. Where a check finds a published claim wrong, the correction is
recorded here and the original is left standing, because a correction is only
legible next to what it corrected.

---

## C-1 — `c-032` overstates the absence of comprehension evidence

**Published claim, unchanged in
[`claims.json`](claims.json):**

> **c-032** No strong empirical outcome studies (e.g., RCTs showing STE
> improves comprehension, error reduction, or safety outcomes) were found in
> open sources.
>
> `group: consensus` · `responding_model_count: 3`

**Status: partly wrong.** The "were found in open sources" half does not hold.

**What settled it.** Kuhn 2014 — a source *this investigation already cites* —
was opened on 2026-08-18 and §5.5 "Evaluations" read in full. That section
exists to ask whether controlled natural languages achieve what they were
designed for, and answers it with reported results (p. 145):

> For type C, two studies on AECMA-SE showed that the use of controlled English
> significantly improves text comprehension, with a particularly large effect
> for complex texts and non-native speakers (Shubert et al. 1995; Chervak,
> Drury, and Ouellette 1996). The results of other studies were similar but not
> significant (Stewart 1998).

AECMA-SE is STE under its former name. The same paper's appendix records that
*"AECMA Simplified English (AECMA-SE) (AECMA 1986) was the predecessor of ASD
Simplified Technical English."*

**The corrected statement.** Empirical comprehension studies on Simplified
English *do* exist and *are* locatable in open sources — two reporting
significant improvement, one reporting the same direction without significance.
Whether they meet the bar c-032 sets with the word **strong** is a separate
question that Kuhn 2014 cannot answer: a survey reports findings, not designs.
Settling that requires opening Shubert et al. 1995 and Chervak, Drury and
Ouellette 1996 themselves. Until then the honest position is:

> The comprehension evidence for Simplified English exists and is citable. Its
> methodological strength is unassessed. No study of *safety outcomes* or
> *error reduction* has been located either way.

**Scope of the damage.** c-032 is one of the claims behind the investigation's
position that STE's efficacy is institutionally documented but causally
unestablished. That position survives, narrowed: it is unestablished for safety
and error outcomes, and *established but unweighed* for comprehension. The
verdict on the headline question — that STE is not a general writing standard —
does not rest on c-032 and is untouched. It rests on what STE removes by
design, which the models argued from STEMG's own material.

**Why the claim was wrong.** Three models converged on it, and the convergence
was mistaken for verification. Nobody had opened the survey; the run's own
`scores.csv` for the superseded `r-2026-0813-01` shows a model citing Kuhn 2014
for the *opposite* proposition — that studies summarised there find Simplified
English improves maintenance-procedure comprehension — and the two positions
sat in the same corpus without colliding. That is the failure the source audit
was built to catch, and it caught it.

**Recorded in** [`source-audit.json`](source-audit.json), entry `kuhn-2014`,
`claim_support.verdict: contradicts`, `method: primary-source`.
