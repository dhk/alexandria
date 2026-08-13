## Comparative analysis report

### Overview

All three outputs address the same source repository and draw on overlapping bodies of literature. They agree on the major structural findings: the repo's three-skill architecture maps sensibly onto three distinct writing regimes; the STE skill is the most standards-grounded; the humanize skill's academic override is its strongest section; and the largest product gaps are a missing context router, a missing plain-language document mode, and absent AI-disclosure guidance. Agreement on these points is high enough that the differences are mostly in depth, citation specificity, and framing rather than in substance.

### Where the outputs converge strongly

**Context-dependence as the organizing principle.** All three treat the contingency insight—that writing quality is genre-, audience-, and purpose-relative—as the central finding, and all credit the repo for already encoding this in its three-skill split. The cross-cutting table in output 3 (purpose × audience × content type × context) is the most explicit formalization, but outputs 1 and 2 make the same argument in prose.

**STE fidelity and the dictionary gap.** All three identify the same structural limitation: the skill encodes STE Part 1 rules but not the Part 2 approved-word dictionary, making full STE compliance unverifiable from the skill alone. Output 3 is most precise about the practical consequence ('cannot guarantee STE compliance'); output 2 notes the tradeoff explicitly ('defensible for token budget but worth naming'); output 1 frames it as compression loss.

**Humanize's academic override as a model.** All three single out the scientific/academic override as the repo's best-executed section and recommend generalizing its pattern to other genres. The specific elements praised—calibrated hedging, passive voice in methods, Gopen & Swan application, suspension of cadence targets—are identical across outputs.

**Anti-costume-humanization.** All three affirm the repo's rejection of deliberate typos, forced slang, and staccato fragments as ethically and practically correct, and all note that over-humanization artifacts are themselves becoming detectable.

**The CV > 0.4 threshold.** All three flag this as a heuristic without readability-research grounding. Outputs 2 and 3 are more explicit that readability formulas are screening tools, not quality definitions; output 1 notes the threshold is uncited.

**Missing router, missing plain-language mode, missing disclosure layer.** These three gaps appear in all three outputs as the top product priorities.

### Where the outputs diverge

**Citation depth and specificity.** Output 2 is the most citation-dense: it names Kobak et al. (2024) and Liang et al. (2023/2024) for vocabulary-tell empirics, Bruce, Rubin & Starr (1981) for readability-formula misuse, Noy & Zhang (*Science*, 2023) for productivity and homogenization, and ISO 24495-1:2023 as the first international plain-language standard. Output 3 names most of the same sources but with slightly less specificity on dates and venues. Output 1 explicitly acknowledges it cannot perform a full external literature review because the supplied packet does not include external sources—a methodologically honest but substantively limiting stance that means it cannot independently confirm or contest the empirical claims the other two make.

**Non-native-writer risk.** Output 2 and output 3 both identify the Liang et al. finding on AI-detector false positives against L2 writing and draw the corollary that humanize's 'commit and assert in idiomatic English' defaults can disadvantage non-native writers. Output 1 does not raise this point, which is a meaningful omission given that the repo's STE skill was originally designed precisely for L2 maintenance readers.

**Orwell's sixth rule.** Output 2 specifically notes that rule 6 ('break any of these rules sooner than say anything outright barbarous') is essential and often dropped in derivative guides. Output 1 mentions Orwell's rules are applied in the repo but does not flag the omission risk. Output 3 does not address this.

**Mode-collision problem.** Output 2 is the only one to explicitly name the STE + humanize incompatibility as a session-level risk (STE bans contractions; humanize pushes informal committed prose) and to note that AGENTS.md does not resolve it. Output 3 lists inter-skill conflict rules as a gap item. Output 1 does not address this.

**Framing of the 'humanize' goal.** All three note the README framing risk, but output 2 is most direct: 'The tool implicitly optimizes for undisclosed passing.' Output 1 calls it a 'framing risk' and notes the body text is more ethical than the surface wording. Output 3 proposes a disclosure footer as the fix.

**Pyramid Principle attribution.** Outputs 2 and 3 correctly attribute the answer-first structure to Minto's Pyramid Principle and note it is optimized for decision-support contexts, not literary quality. Output 1 makes the same attribution but does not distinguish the Minto use case from plain-language document standards.

**Proposed extensions.** All three propose a context router as the top priority. Output 3 is the most structured in its extension roadmap (P0/P1/P2 tiers with explicit PR-slice framing). Output 2 proposes a 'controlled' skill as a stretch item that would generalize STE into a graduated restriction spectrum from plain-language to full STE—a more ambitious architectural proposal not present in the other two. Output 1's extensions are the most detailed in prose but less tightly tied to named literature findings.

### What this run does not establish

- **Exact Issue 9 (2025) rule-numbering deltas versus Issue 8.** All three outputs note this uncertainty; none had access to the official PDF.
- **Specific effect sizes for plain-language comprehension gains.** Output 2 references Kimble's collation directionally but explicitly flags that specific percentages vary by study. Outputs 1 and 3 do not quantify these effects.
- **Whether the CV > 0.4 threshold has any empirical basis at all, or is purely a repo invention.** All three flag it as ungrounded, but none can confirm whether the maintainer derived it from any source.
- **Current state of AI-detector accuracy.** All three treat detector performance as time-stamped and volatile; none can speak to post-2024 model generations.
- **Whether the repo's audit.py script implements the acceptance criteria as described in SKILL.md.** Output 3 explicitly notes it evaluated from text files only, not live model traces; the same caveat applies to all three.
- **Whether 'STE-inspired' output from the skill would pass a commercial STE checker.** The dictionary gap is identified, but no output tested this empirically.
- **The ethical and legal status of AI-assisted writing under specific venue policies.** All three note the disclosure gap; none adjudicate which specific uses would violate which specific policies.
- **Whether the homogenization finding from Noy & Zhang generalizes to the specific use patterns the repo targets.** Output 2 cites the study; output 3 references it; neither applies it to the repo's specific workflow.
