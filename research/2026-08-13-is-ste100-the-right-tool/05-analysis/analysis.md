## Comparative Analysis Report

### Overview

All three outputs reach the same headline verdict—ASD-STE100 is not a general-purpose writing standard and is actively harmful for persuasive writing—and share a common structural argument: STE is well-specified for its original domain (safety-critical aerospace procedures, L2 readers, translation pipelines) and poorly specified for everything else. The outputs differ substantially in depth of external citation, specificity of historical claims, and the granularity of their decision frameworks.

### Points of Strong Agreement

**Verdict on the circulating claim.** All three reject the claim that STE is the right tool for clear, concise, *persuasive* writing. The rejection is unambiguous and identically reasoned: STE removes the devices persuasion depends on (varied rhythm, synonymy, figurative language, voice, narrative) by design, and those removals are virtues in a maintenance manual and liabilities in an essay or argument.

**STE's genuine strengths.** All three affirm STE's value for procedural, safety-critical, multilingual technical documentation. The mechanism is consistently identified: one-word-one-meaning, short sentences, imperative structure, and controlled vocabulary reduce ambiguity and translation cost for L2 technician readers under operational pressure.

**The missing dictionary problem.** All three flag that the repository's STE skill encodes rules without the approved-word dictionary, making it an incomplete implementation. All three agree this matters because the dictionary is where STE's distinctive anti-ambiguity value lives.

**The missing context router.** All three independently identify the absence of a context router—a mechanism that selects writing techniques based on purpose, audience, and context—as the key architectural gap in the repository.

**Readability formulas as misused diagnostics.** All three treat readability formulas as diagnostic tools that become harmful when used as writing targets. Two explicitly flag the CV > 0.4 sentence-variance threshold in the repository as an ungrounded heuristic.

**Why the enthusiasm is epistemically suspect.** All three explain the current popularity of STE in AI/writing-tool communities as driven by its machine-operability and rule-based legibility rather than its original safety rationale—a form of tool transfer from a bounded domain to a general one.

### Points of Meaningful Difference

**Depth of external citation.** Output 2 is the most heavily cited, naming specific studies (Chervak & Drury on aircraft maintenance instructions; Sopory & Dillard's 2002 metaphor meta-analysis; Green & Brock 2000 on narrative transportation; Kincaid et al. 1975 on readability formulas; Pullum 2009 on Strunk & White), specific editions of key texts (Williams 12th ed., O'Keefe 3rd ed., Toulmin updated 2003), and a specific survey article (Kuhn 2014 in *Computational Linguistics*). Output 3 cites many of the same sources but with slightly less specificity on study details. Output 1 makes no external citations and explicitly acknowledges that the supplied materials do not include the texts of ISO 24495-1, Gopen & Swan, or Williams—a methodologically honest but substantively thinner position.

**Historical specificity on STE's origins.** Outputs 2 and 3 provide the founding lineage (AECMA Simplified English, early 1980s; Fokker and Douglas involvement; 2004/2005 renaming to ASD-STE100). Output 1 explicitly declines to assert this history, noting it is not established by the supplied materials—a defensible epistemic choice but one that leaves the historical account incomplete.

**Approved-verb list size.** Only Output 2 specifies the approved-verb list as "roughly 80 verbs." The other two do not quantify it.

**Sentence-length caps by text type.** Only Output 3 specifies the differential caps (~20 words for procedures, ~25 for descriptions). Output 1 notes caps exist; Output 2 does not differentiate.

**Strunk and White critique.** Only Output 2 explicitly names Strunk & White as containing factual grammatical errors and cites Pullum's 2009 critique. The others do not address this.

**Narrative transportation as a persuasion mechanism.** Only Output 2 explicitly cites Green & Brock (2000) on narrative transportation as among the strongest persuasion effects in the literature and connects it to devices STE bans. Output 3 references narrative persuasion literature generically; Output 1 does not.

**Decision framework granularity.** All three provide decision tables, but they differ in structure. Output 2's table is the most compact and action-oriented. Output 3's is the most granular, with a four-step procedure and explicit layering rules. Output 1's is the most discursive, embedding the decision logic in prose with a summary router at the end.

**Treatment of ISO 24495-1.** All three mention ISO 24495-1:2023 as the relevant plain-language standard. Outputs 2 and 3 describe it as principles-based and contrast it with STE's rule-based approach. Output 1 mentions it only in passing in a comparison table.

### What This Run Does Not Establish

**Direct experimental evidence on STE and persuasion.** No output cites an RCT or controlled study comparing STE-restricted persuasive text against rhetorically crafted text on attitude change, behavioral compliance, or trust. All three acknowledge this gap; Output 2 states explicitly that no such study exists to its knowledge. The anti-persuasion conclusion rests on strong theoretical grounds (the persuasion literature identifies devices STE removes as load-bearing) but not on STE-specific experimental data.

**Clean causal evidence that STE reduces accident rates.** All three note that isolating STE's contribution to safety outcomes from other concurrent changes (training, tooling, design, workflow) is methodologically difficult. The safety case rests on mechanism and institutional adoption, not clean experimental isolation.

**Whether the dictionary or the syntactic rules drive STE's L2 comprehension benefit.** All three flag this as an open question with practical implications for the repository's rules-only implementation. No output resolves it.

**Validation of any sentence-variance threshold as a comprehension predictor.** The CV > 0.4 threshold is flagged as ungrounded by two outputs, but neither provides a validated alternative threshold. Sentence-length variation is endorsed as a marker of rhetorical rhythm (Williams tradition), not as a numeric quality gate.

**Whether ISO 24495-1:2023's principles produce measurable comprehension gains.** Output 2 notes the standard is new (2023) and that follow-through empirical studies have not yet appeared. The plain-language recommendation rests on the older plain-language evidence base and the standard's codification of that consensus, not on ISO 24495-1-specific trials.

**LLM-specific failure mode distribution.** All three note that the case for STE as an LLM guardrail depends on what LLM prose actually fails at. None provides a systematic taxonomy of LLM writing failures across genres tested against different remediation techniques.
