## Comparative analysis report

### Scope
Three outputs address the same commissioned brief: settle ASD-STE100 provenance from primary sources, widen the comparison set to include Hemingway Editor, Hotaling (2020), and the full `claude-writing-skills` repository, and produce an updated decision procedure. All three outputs were produced independently.

---

### High-confidence consensus (all three agree, sourced)

**Provenance.** All three outputs converge on the same core lineage: AECMA (European Association of Aerospace Industries) originated STE in the late 1970s with AIA collaboration; the SEWG was formally constituted in 1983 at a meeting associated with Fokker in Amsterdam; the first public guide appeared in 1986 as PSC-85-16598; the organizational rename to ASD and STEMG occurred in 2004; the first issue under the ASD-STE100 specification title appeared in 2005; and Issue 9 (15 January 2025) is the current release, now designated an international standard. All three explicitly retract or refuse to confirm Douglas/McDonnell Douglas involvement as unsourceable from authoritative primary materials.

**Substantive conclusions.** All three confirm the prior run's three main findings without revision: (1) STE is not a general-purpose writing standard; (2) it is actively harmful for persuasion because it removes by design the devices persuasion depends on; (3) its current popularity in AI/tooling circles tracks machine-operability, not fitness for general prose.

**Shared-assumption analysis.** All three independently identify the same cluster of assumptions across rule-list and readability-formula tools—that surface features proxy quality and that shorter is generally better—and all three reach the same verdict: valid as a diagnostic, not as an optimization target. The Goodhart's Law framing (optimize the score, worsen the prose) appears in all three.

**AI-tell catalog.** All three characterize the `humanize` skill's tell list as practitioner consensus or folklore derived from community-maintained sources (Wikipedia's 'Signs of AI writing'), not validated experimental research.

---

### Partial agreement and nuance differences

**1985 vs. 1986 first release.** One output explicitly resolves this as Issue 0 (pre-release, 1985) vs. Issue 1 (first public guide, 1986), citing a CEUR-WS paper. The other two collapse to 1986 as the official figure. The three-way picture is: the official STEMG site says 1986; secondary sources say 1985; the most granular output reconciles both as distinct releases. The 1985/1986 ambiguity is real and should not be flattened.

**ATA requirement date.** One output gives 1987 (citing Issue 9 directly); another gives 1986 (collapsing it with the guide's first release). The Issue 9 citation is the stronger source.

**Hemingway formula identification.** Two outputs confidently identify ARI as the formula used; one notes that product articles mention both ARI and Flesch–Kincaid and that third-party tests have treated the grade as ARI. The uncertainty is real: Hemingway does not publish a peer-reviewed methodology paper.

**Hotaling's ten rules.** One output lists all ten rules verbatim; the others characterize them. The verbatim list is more useful for verification.

**Special usage rights in Issue 9.** Only one output details the eight categories of irrevocable free-of-charge usage rights. This is material for tool builders and researchers and is absent from the other two.

**EU Trade Mark dates.** Only one output notes the 2006 and 2018 EUTM grants. The others mention the trademark number without dates.

**Issue 10 scheduling.** Only one output notes that Issue 10 is scheduled for January 2028.

**`humanize` cadence CV threshold.** Two outputs explicitly flag the CV > 0.4 threshold as an ungrounded heuristic. One does not address it.

**STEMG's 'not for writers' quote.** One output quotes STEMG's own training material directly: *STE is not a simplified version of English for the writers.* The others convey the same idea without the direct quote.

---

### Divergences

**Fokker sourcing confidence.** One output treats Fokker's involvement as settled from official STEMG pages and a practitioner history (Chiarello 2013). A second output says it could find no authoritative primary source naming individual companies and treats all specific airframer claims as unverified. A third occupies a middle position, citing Chiarello 2013 for Fokker leadership while noting the meeting date rests on that secondary source rather than a scanned minute. The divergence reflects genuine source-access differences rather than factual disagreement: the Chiarello 2013 source (a STEMG-affiliated practitioner history) is treated as near-primary by two outputs and as unavailable by one.

**Scope of the `ste` skill's failure mode.** One output focuses on the skill being a lossy compression of the dictionary (copyright-correct but fidelity-limited). Another focuses on the skill's scope being broader than STE's intended domain (docs, READMEs, UI text vs. aircraft maintenance manuals) without justification for the transfer. Both are valid and complementary failure modes.

**Decision procedure format.** All three produce a decision procedure, but they differ in granularity and format: one uses a six-step prose procedure with sub-routines by genre; one uses a step-by-step procedure with a lookup table; one uses a six-step procedure with a one-page pseudocode cheat sheet. The underlying logic is consistent across all three.

---

### What this run does not establish

- **Full SEWG founding membership roster.** No output retrieved a primary scan of the 1983 SEWG membership list. Fokker's role rests on a practitioner history (Chiarello 2013), not on AECMA archival minutes. Any specific OEM seat claim beyond Fokker remains unverified.
- **Empirical outcome studies for STE.** All three outputs note the absence of RCTs or strong quasi-experiments showing STE rules improve comprehension, error reduction, or safety outcomes in open sources. The institutional adoption record (ATA, S1000D, airworthiness authorities) is documented; causal efficacy is not.
- **Hemingway's exact formula and validation.** No output retrieved a peer-reviewed Hemingway methodology paper. The ARI identification is based on product help pages and third-party reverse engineering, not a published white paper from the Hemingway team.
- **Empirical validation of AI-tell detection.** The tell catalog's effectiveness at improving reader perception has not been tested in controlled studies. All three outputs treat it as practitioner consensus that will shift as base models change.
- **Causal evidence that lowering ARI improves reader outcomes across genres.** All three outputs assert this is absent; none found a study supplying it.
- **The 1979 AEA request document.** The late-1970s/1979 origin date is repeated across practitioner literature but the primary letter or meeting record was not retrieved by any output.
- **Whether 'international standard' status for Issue 9 reflects external ISO-like ratification or is ASD's own characterization.** One output flags this explicitly; the others do not resolve it.
