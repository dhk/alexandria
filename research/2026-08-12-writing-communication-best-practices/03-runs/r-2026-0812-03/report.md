# Comparative analysis — writing-practice brief

Produced by the grading model (`anthropic/claude-sonnet-4.6`) over the
three research outputs in [`outputs/`](outputs/). **Recovered from a
malformed response** — see [`provenance.md`](provenance.md); the run's
own `report.md` is an empty stub.

---

## Comparative Analysis Report

### Overview

All three outputs are substantive, well-organized research briefs that synthesize external literature before evaluating the repo. They share a common skeleton—controlled-language standards, plain-language guidelines, rhetoric/style standards, readability research, and AI-text ethics—and reach broadly compatible conclusions. Differences are matters of depth, sourcing specificity, and which sub-claims each output chooses to develop.

### Where the outputs converge strongly

**STE characterization.** All three correctly identify Issue 9 (January 2025), the ~53-rule / ~900-word-dictionary structure, the procedure/description split, and the safety-critical origin in aerospace maintenance. All three also reproduce the standard's own caveat that it was never intended as a general writing standard and that no tool can guarantee full compliance.

**Plain-language first principle.** All three treat audience identification as the logically prior step before any style rule, citing Federal guidelines and/or ISO 24495-1. All three criticize the repo for inverting this order—starting with stylistic transformation rather than audience/purpose analysis.

**Gopen and Swan.** All three credit the `humanize` scientific-paper override for correctly importing stress-position and topic-position principles, and all three treat this as the strongest evidence-aligned feature in the repo.

**AI-tell volatility.** All three note that tell catalogs are model-generation-specific and time-decaying, and that the practitioner literature itself acknowledges this instability.

**Disclosure ethics.** All three flag the `humanize` framing ("appear to have been written by a person") as ethically ambiguous, distinguishing legitimate quality editing from detector evasion, and all three note the absence of any disclosure or provenance support in the repo.

**Repo gaps.** All three independently identify the same three structural gaps: no dedicated plain-language document skill, no audience/purpose routing layer, and no disclosure/provenance tooling.

### Where the outputs diverge

**Sourcing specificity.** One output provides the most granular quantitative evidence: the 39.5% → 17.4% detector accuracy drop under light editing (Perkins et al.), the 61.3% false-positive rate on TOEFL essays, the Vanderbilt/Turnitin 750-wrongful-accusations calculation, and the GPT-4 vs. GPT-4o era-specific tell vocabulary lists. Another output cites the NIST GenAI pilot and a 2025 Scientific Reports paper on detector instability but does not supply the same numerical precision. The third output cites the DIPPER paraphrase result and OpenAI's classifier retirement but similarly lacks the Perkins figures.

**Caterpillar Fundamental English.** Only one output develops the CFE discontinuation story (1982, enforceability failure) as a cautionary precedent for rule-driven writing tools. The others mention CFE only in passing or not at all.

**Minto counter-cases.** One output explicitly quotes Minto's own literature on when not to use the Pyramid Principle (bad news, emotional engagement, no recommendation yet) and flags that `plainspoken` does not handle these cases. The others note the limitation more briefly.

**Rhetorical genre theory.** One output explicitly names Carolyn Miller's 1984 "Genre as Social Action" as the theoretical anchor for context-dependence. The others treat genre-conditionality as a practical finding without naming the theoretical source.

**ISO 24495-1:2023.** Only one output names and characterizes this standard (relevant, findable, understandable, usable). The others cite Federal plain-language guidelines without referencing the ISO framework.

**Human/AI language convergence.** One output cites a 2024 study detecting LLM influence on spoken conversational content, arguing that human and AI language are converging and that this further undermines static tell catalogs. The others note tell volatility without this specific mechanism.

**Transparency penalty nuance.** One output provides the most granular account of the transparency penalty, including the moderating role of AI literacy and the paradoxical finding that disclosure can increase perceived credibility of misinformation. The others note the penalty exists but do not develop these moderators.

**STE invocation-layer gap.** Two outputs explicitly criticize the `ste` skill for not gating procedure vs. description vs. safety-critical rules at invocation, since the standard itself applies different sentence-length caps (20 vs. 25 words) to each. One output notes the limitation less precisely.

**Proposed extensions.** All three propose an audience/purpose router, a plain-language document skill, and disclosure tooling as top priorities. One output additionally proposes versioning the tells catalog with model-generation metadata, a non-native-writer defense flag, and a bad-news override for `plainspoken`. Another proposes a standalone `scholarly-integrity` skill and a `brief`/Minto skill for artefacts. The third proposes house-style adapter packs (Microsoft/Google) and controlled-language siblings for non-aerospace industries.

### What this run does not establish

- **Empirical performance of the repo's outputs.** No output ran the skills on sample texts or measured output quality against any criterion. All evaluation is design-to-literature fit, not behavioral testing.
- **Full STE dictionary coverage.** All three outputs note the dictionary gap but none conducted a line-by-line audit of the skill's verb list against the official Part 2 dictionary.
- **Causal trust effects of disclosure.** The transparency-penalty findings cited are correlational and context-sensitive; no output claims to establish that disclosure causes trust loss in a generalizable way.
- **Validity of the 0.4 CV threshold.** All three outputs flag this as an unvalidated heuristic, but none cites a study that would establish what the correct threshold should be, or whether any threshold is appropriate.
- **Long-term reader adaptation.** One output raises the possibility that readers are adapting to AI style, which would shift which tells remain diagnostic, but no output cites longitudinal evidence on this question.
- **Whether the repo's maintainer intends `humanize` for detector evasion.** All three outputs flag the ethical ambiguity of the framing, but none has access to the maintainer's intent; the criticism is structural, not attributive.
- **Comparative effectiveness of the three skills against each other or against alternatives.** The outputs evaluate each skill against external literature but do not compare them to competing tools or to each other's outputs on shared tasks.
