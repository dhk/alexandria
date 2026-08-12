# x-ai/grok-4.5 — research output

Run `r-2026-0812-03`, dispatched 2026-08-12. Web search: on (this output rests on live sources read that day).

Completion tokens 7,144; prompt tokens 140,180; billed $0.269.

Verbatim model output, unedited.

---

I will gather external research on writing best practices first, then evaluate the repo against that evidence.Gathering primary sources on plain-language standards, classic style guidance, and AI-text research.Pulling primary guideline pages and additional research on controlled languages and AI text.# Research Brief: Written-Communication Best Practices and Evaluation of claude-writing-skills

**Prepared as an independent literature synthesis and collaborative pitch base**  
**Scope note:** Synthesis stands alone from the tool. Repo evaluation follows only after the evidence base. Uncertainty is flagged where evidence is thin, contested, or context-bound.

---

## (1) SYNTHESIS FIRST — Best Practices for Written Communication

Best practice is not a single checklist. It is a set of **context-conditioned constraints**: purpose (inform, instruct, persuade, document liability), audience (native vs. non-native, expert vs. lay, time-pressed vs. reflective), content type (procedure, description, argument, scientific claim, chat reply), and risk (safety-critical vs. low-stakes). The literature converges on clarity, specificity, and reader-centered structure, then diverges sharply on vocabulary control, voice, hedging, and disclosure.

### 1.1 Controlled languages and technical-writing standards (STE and peers)

**ASD-STE100 Simplified Technical English** is the dominant industrial controlled natural language (CNL) for technical documentation. Issue 9 (January 2025) comprises ~53 writing rules plus a dictionary of ~900 approved words, each with one approved part of speech and one approved meaning.[[1]](https://en.wikipedia.org/wiki/Simplified_Technical_English)

Core design goals: reduce ambiguity for non-native readers, improve human and machine translation, and lower maintenance/assembly error risk.[[1]](https://en.wikipedia.org/wiki/Simplified_Technical_English)

**Rule clusters that matter in practice:**
- **Vocabulary:** approved words only as specified POS/meaning; technical nouns/verbs allowed when domain-consistent; one term per concept.[[1]](https://en.wikipedia.org/wiki/Simplified_Technical_English)
- **Noun clusters:** max three words; longer clusters rewritten or hyphenated after first full form.[[1]](https://en.wikipedia.org/wiki/Simplified_Technical_English)
- **Verbs:** limited forms (infinitive, imperative, simple present/past/future, past participle as adjective); no complex tenses; no free “-ing” verb forms except inside technical nouns; active voice preferred; passive only when agent unknown (especially in description).[[1]](https://en.wikipedia.org/wiki/Simplified_Technical_English)
- **Sentences:** one topic per sentence; procedures ≤20 words; descriptions ≤25 words; no omitted words/contractions; vertical lists for complexity.[[1]](https://en.wikipedia.org/wiki/Simplified_Technical_English)
- **Procedures:** one instruction per sentence (unless simultaneous); imperative; condition first then command; notes never instruct.[[1]](https://en.wikipedia.org/wiki/Simplified_Technical_English)
- **Paragraphs:** one topic; ≤6 sentences.[[1]](https://en.wikipedia.org/wiki/Simplified_Technical_English)
- **Safety:** explicit WARNING/CAUTION levels; command/condition then risk/result.[[1]](https://en.wikipedia.org/wiki/Simplified_Technical_English)

**Comparable CNLs:** Basic English (Ogden), Caterpillar Fundamental/Technical English, IBM Easy English, Attempto Controlled English (more logic/KR-oriented). STE is the most operationalized for procedural tech docs and is required or recommended in aerospace/defense ecosystems (e.g., ATA, S1000D, EDSTAR contexts).[[2]](https://en.wikipedia.org/wiki/Controlled_natural_language)

**Context variation:** STE is optimized for **procedures and safety-critical description**, not for persuasive essays, literary voice, or open scientific argumentation. Official guidance stresses STE is **not a standalone style guide**—it must sit with domain specs and professional judgment. Over-application outside maintenance/procedure genres is a known misapplication risk.[[1]](https://en.wikipedia.org/wiki/Simplified_Technical_English)

**Uncertainty:** Full dictionary lookups and edge-case rule interactions require the official specification; secondary summaries (including skill compressions) can drift. Adoption outside aero/defense is real but uneven; many orgs prefer looser plain language instead.[[1]](https://en.wikipedia.org/wiki/Simplified_Technical_English)

### 1.2 Plain-language guidelines

Plain language is broader and less lexically rigid than STE. U.S. Federal Plain Language Guidelines (implementing the Plain Writing Act of 2010) and related agency distillations emphasize: write for the reader; major points first; one idea per short paragraph; active voice; short sentences; everyday words (explain necessary technical terms); omit needless words; keep subject and verb close; use headings/lists/tables; test with users.[[3]](https://www.archives.gov/open/plain-writing/10-principles.html)

**ISO 24495-1:2023** frames four governing principles: content is **relevant**, **findable**, **understandable**, and **usable** for the intended reader. Later parts extend to science writing and organizational implementation.[[4]](https://www.iplfederation.org/iso-standard/)

**International Plain Language Federation definition:** wording, structure, and design so clear that intended readers can easily find what they need, understand it, and use it.[[5]](https://www.iplfederation.org/plain-language/)

**Context variation:**
- **Public/government/consumer:** high plain-language pressure; pronouns (“you”), Q&A headings, task orientation.
- **Expert-to-expert technical:** plain structure + precise terminology (not dumbed-down vocabulary).
- **Legal/regulatory:** formality and defined terms can override “everyday word” defaults; still benefits from organization and active voice where possible.
- **Health/safety:** plain language + testing; readability formulas alone are insufficient (see 1.4).

**Uncertainty:** “Plain” is audience-relative. A term that is plain to a senior engineer is jargon to a citizen. Guidelines repeatedly stress audience analysis and usability testing over formulaic word bans.[[6]](https://digital.gov/guides/plain-language)

### 1.3 General style, rhetoric, and technical style standards

**Orwell (“Politics and the English Language”)** — six rules still widely taught: avoid stale figures of speech; prefer short words; cut words; prefer active; prefer everyday equivalents to jargon/foreign/scientific terms when possible; break any rule rather than say something barbarous.[[7]](https://www.writingclasses.com/toolbox/tips-masters/george-orwell-6-questions-6-rules)

**Barbara Minto — Pyramid Principle:** lead with the answer/conclusion; group supporting ideas in a logical pyramid (deductive or inductive); SCQA-style framing for introductions. Dominant in consulting and executive communication; maps poorly to mystery-narrative or pure exploratory science writing.[[8]](https://untools.co/minto-pyramid/)

**Gopen & Swan — “The Science of Scientific Writing” (1990):** reader-expectation principles—subject near verb; new/important information in the **stress position** (sentence end); old information in the **topic position** (sentence start); old-to-new flow across sentences; action in the verb; context before new complexity. These are among the strongest evidence-based micro-structure rules for dense professional prose.[[9]](https://cseweb.ucsd.edu/~swanson/papers/science-of-writing.pdf)

**Industry tech style guides (Microsoft Writing Style Guide; Google developer documentation style guide):** warm/clear/helpful voice (Microsoft); consistency, global audience, bias-free language, Chicago/Merriam-Webster baselines with tech-specific overrides (Google). Shared themes: simple grammar, necessary technical terms kept, scannability, consistency of terminology.[[10]](https://learn.microsoft.com/en-us/style-guide/welcome/)

**Context variation:**
| Purpose / type | Dominant pattern |
|---|---|
| Chat / advice / decision support | Answer-first (Pyramid), decide-don’t-survey, owned voice |
| Procedures / UI / runbooks | STE-like: imperative, short, one action, consistent terms |
| Blog / essay / thought leadership | Specific claims, varied cadence, voice, cut filler (Orwell + anti-generic) |
| Scientific paper | Calibrated hedges, IMRaD conventions, Gopen–Swan flow, citations; passive OK when method is subject |
| Legal / compliance | Defined terms, precision over brevity, controlled ambiguity reduction |

### 1.4 Readability research

**Flesch Reading Ease** and **Flesch–Kincaid Grade Level** remain the most deployed surface metrics (sentence length + syllables/word). Plain English often targets ~60–70 Reading Ease / ~8th–9th grade for general audiences; DoD and insurance regulations have used these scores as standards.[[11]](https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests)

**Critical limitations (well established):**
- Formulas ignore content difficulty, prior knowledge, layout, cohesion, and retrieval aids.[[11]](https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests)
- Different formulas can disagree by several grade levels on the same text.[[12]](https://www.sciencedirect.com/science/article/abs/pii/S1551741112000770)
- Recent work in health/comms finds traditional scores often track **perceived** difficulty better than actual comprehension/retention; style and modality matter more than formula alone.[[13]](https://www.jmir.org/2025/1/e69772)

**Practical implication:** Use readability scores as **smoke alarms**, not acceptance criteria. Prefer short sentences, familiar words, active voice, and structure—but validate with audience tasks when stakes are high (plain-language and health-literacy consensus).

### 1.5 Clearly AI-generated text, disclosure, detectability, and “humanization”

**Detectability is brittle.** Paraphrasing and light editing sharply degrade detector accuracy (e.g., DIPPER paraphrases collapsing DetectGPT-style performance while preserving semantics). OpenAI retired its own classifier citing low accuracy. Multiple 2024–2025 evaluations find mid-range, unstable accuracy and high sensitivity to minor edits; false positives have harmed non-native writers in academic settings.[[14]](https://arxiv.org/abs/2303.13408)

**Human identification** often relies on stylistic cues (redundancy, repetition, coherence failures, “AI vocabulary,” negative parallelisms, tricola, generic openers)—not deep semantic proof. Expert accuracy in some studies is moderate (~70% in one medical-text setting) and driven by linguistic attributes.[[15]](https://mededu.jmir.org/2025/1/e62779/)

**Practitioner catalogs** (e.g., Wikipedia’s “Signs of AI writing”) document high-frequency tells: delve/tapestry/testament-type vocabulary, “not X but Y” constructions, compulsive rule-of-three, scene-setting openers, symmetrical structure, unearned CTAs, stacked hedges, attribution to nobody. These are **probabilistic style markers**, not proof.[[16]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)

**Disclosure and trust — contested findings:**
- Readers often want disclosure more than writers do; necessity judgments depend on how central/irreplaceable AI contribution was.[[17]](https://arxiv.org/html/2604.27129v1)
- Multiple experiments find **disclosing AI use can reduce trust** in the actor (“transparency dilemma”).[[18]](https://www.sciencedirect.com/science/article/pii/S0749597825000172)
- Other work finds non-disclosure harms trust when discovered, and brand/authenticity effects depend on framing (AI-disclosed vs. human-attributed).[[19]](https://www.emerald.com/jpbm/article/32/7/1108/255698/To-disclose-or-not-disclose-is-no-longer-the)
- Scholarly norms increasingly push disclosure of material AI assistance; undisclosed use risks retraction and reputational harm.[[20]](https://www.enago.com/responsible-ai-movement/resources/700-research-papers-flagged-undisclosed-ai-use-crisis/)

**Risks of “humanize to pass as human”:**
- **Cat-and-mouse:** humanizers exist largely to evade detectors; detection and evasion co-evolve and neither is reliable.[[21]](https://effortlessacademic.com/how-reliable-are-ai-detectors/)
- **Over-smoothing / costume humanization:** staccato fragments, forced slang, intentional typos, manufactured contrarianism—editors learn these as second-order tells (practitioner consensus aligned with careful editorial practice).
- **Integrity risk:** tools that maximize “undetectable” output facilitate undisclosed AI use in academic/professional contexts where disclosure or human authorship is required.
- **Quality risk:** optimizing against detectors can trade away precision, calibrated hedging, or domain voice.

**Appropriate-use framing (evidence-grounded opinion):**  
For **published personal voice** (blog, Substack, email under one’s name), engineering specificity, commitment, and cadence variation is legitimate craft—equivalent to good editing. For **safety-critical procedures**, controlled language beats “human voice.” For **science**, calibrated uncertainty and citation beat forced decisiveness. For **high-stakes authenticity claims**, disclosure policies and provenance beat detector theater. Optimizing solely to fool detectors is the weakest ethical and technical objective.

**Uncertainty:** Trust effects of disclosure are domain- and framing-sensitive; literature is young and mixed. Detector benchmarks lag model releases. Long-term reader adaptation to “AI style” may shift which tells remain diagnostic.

### 1.6 Cross-cutting synthesis: what varies by context

| Dimension | Prefer | Avoid / relax |
|---|---|---|
| Safety procedures, non-native maintainers | STE-level control, imperative, ≤20 words, one action | Literary variation, contractions, rich synonymy |
| Public benefits/compliance info | Plain language + testing, points first, “you” | Unexplained jargon, buried lede |
| Executive/decision chat | Pyramid answer-first, decide-don’t-survey | Option menus, throat-clearing |
| Thought leadership under own name | Specific claims, voice, cut filler, varied rhythm | Generic business prose, both-sidesing without stake |
| Scientific results | Gopen–Swan flow, evidence-calibrated hedges, genre structure | Forced hot takes; treating “significant/robust” as AI tells |
| AI assistance | Improve clarity/specificity; disclose when norms/stakes require | Detector evasion as primary goal; fake human errors |

**Shared non-negotiables across almost all contexts:** one main idea per unit; subject–verb proximity; concrete specifics over abstractions; consistent terminology; cut empty metadiscourse; match length to task.

---

## (2) TOOL EVALUATION SECOND — ste, plainspoken, humanize vs. the synthesis

Evaluation uses only the supplied skill materials against Section 1.

### 2.1 `ste` — ASD-STE100 mode

**Fit (strong):**  
Compresses Issue 9 structure: word rules, noun clusters, verb forms, active voice, sentence caps (20/25), procedure vs. description split, safety pattern, punctuation (no semicolon), GR-1..8, recurring-error table, and full approved-verb list. Scope correctly targets docs/procedures/READMEs/reports/UI—not code identifiers. Aligns with STE’s purpose for technical prose and non-native clarity.[[1]](https://en.wikipedia.org/wiki/Simplified_Technical_English)

**Correct implementations:** active/imperative bias; one meaning per word heuristic; technical noun/verb escape hatch; condition-then-command; notes ≠ instructions; American spelling; gender-neutral GR-7.

**Divergences / simplifications:**
- **Dictionary completeness:** skill ships approved **verbs** and a replacement table, not the full ~900-word dictionary with POS/meaning columns. Writers still need the official Part 2 for true compliance. (Skill acknowledges full spec URL.)
- **Chat looseness:** “chat conversation only loosely (clarity rules yes, word-list strictness no)” is pragmatic but can produce hybrid non-STE output while the mode is “on.”
- **Persistence default ON when unsure** is operationally aggressive; STE misapplied to persuasive or narrative chat can harm register fit (synthesis: STE is genre-bound).[[1]](https://en.wikipedia.org/wiki/Simplified_Technical_English)

**Audience/purpose sensitivity:** Good procedural/descriptive split; weaker explicit branching for “expert API reference vs. novice tutorial vs. safety-critical” beyond the standard’s own procedure/description/safety sections. No built-in usability-test reminder (plain-language literature’s closing loop).

### 2.2 `plainspoken` — talking-register mode

**Fit (strong for chat/decision support):**  
Directly implements Pyramid answer-first, decide-don’t-survey, owned voice, cut preamble, quantify comparisons, kill high-signal AI tics (negative parallel, triad rhythm, hype adverbs, summary tails), length-matching. Matches consulting/executive and plain-language “major point first” guidance.[[8]](https://untools.co/minto-pyramid/)

**Correct implementations:** “Depends → state on what + default call”; “I don’t know” as first sentence; assumptions explicit; one idea per sentence; persistent mode with clean off-switch; explicitly **does not** govern deliverable genres (docs follow their own rules).

**Divergences / risks:**
- **Decide-don’t-survey** can under-serve genuine multi-criteria design spaces where surveying options *is* the professional move; skill escalates only “load-bearing” forks—judgment-heavy, easy to over-decide.
- **Em-dash near-ban** and triad ban are anti-tell heuristics, not universal rhetoric rules (human writers use both well).
- No explicit Gopen–Swan micro-structure (topic/stress positions)—less critical in short chat turns.

**Coverage:** Excellent for assistant chat. Not a document plain-language skill (no headings/lists/tables guidance, no audience analysis worksheet, no ISO findable/usable design layer).

### 2.3 `humanize` — rewrite + audit for human-appearing prose

**Fit (strong craft alignment; ethically double-edged):**  
Four-pass pipeline matches the synthesis’s quality hierarchy: (1) force specific/arguable content, (2) Orwell cutting, (3) break metronomic cadence without installing a new metronome, (4) mechanical tell audit with human judgment. Academic overrides (calibrated hedges, IMRaD, passive-as-tool, Gopen–Swan positive moves, don’t flag precise technical vocabulary) are unusually well aligned with scientific writing research.[[9]](https://cseweb.ucsd.edu/~swanson/papers/science-of-writing.pdf)

**Correct implementations:**
- Disease vs. symptom framing (hedging, vagueness, throat-clearing > word bans alone).
- Guard against overcorrection (staccato costume, fake typos, forced slang)—matches second-order tell risk.
- Voice-profile calibration outranking generic rules—addresses “generic human” failure mode.
- `tells.md` catalog tracks Wikipedia-style AI signs (vocabulary, negative parallel, tricola, openers, bold-colon lists, both-sidesing).[[16]](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- Acceptance criteria mix content tests + cadence CV + read-aloud.

**Divergences / tensions with research:**
- **Primary framing (“so a person appears to have written them”)** sits on the detectability/evasion axis. Research says detectors are unreliable and paraphrasing evades them; optimizing appearance can slide into integrity-sensitive use. Skill’s best self is **quality editing under own name**, not undetectability.[[14]](https://arxiv.org/abs/2303.13408)
- **Cadence CV > 0.4** is a reasonable anti-metronome heuristic but **not** a validated readability or “humanness” standard in the academic literature; risk of cargo-cult variation.
- **Pass 1 “take a position”** is right for blogs; academic override correctly softens it—but other genres (diplomacy, incident comms, early-stage exploration) may need similar explicit branches.
- **No disclosure guidance** despite trust/disclosure literature.[[18]](https://www.sciencedirect.com/science/article/pii/S0749597825000172)
- Blank voice-profile default → generic human until calibrated (AGENTS.md correctly treats calibration as first-class).

**Audience/purpose sensitivity:** Strong blog/essay/email/docs vs. paper split. Weaker explicit paths for UI microcopy, legal, or STE-governed procedures (humanize could fight STE if stacked carelessly).

---

## (3) GAP ANALYSIS — Strengths, weaknesses, product gaps

### Strengths
1. **Genre-split architecture is right:** STE for controlled technical prose, plainspoken for chat register, humanize for publishable voice—mirrors how best practices actually fragment by context.
2. **`ste` is unusually faithful** among LLM “skill” compressions: rules + verbs + GR + error table, Issue 9 dated.
3. **`humanize` prioritizes substance over synonym salad** and includes rare, correct scientific overrides (Gopen–Swan, calibrated hedges).
4. **Mechanical audit + judgment** (`audit.py` + tells.md) beats pure prompt vibes; voice-profile system is the correct long-term fix for generic de-slop.
5. **Anti-overcorrection** section shows editorial maturity beyond typical “humanizer” products.

### Weaknesses
1. **Audience model is implicit**, not operationalized (no lightweight audience/purpose/risk preamble before applying rules).
2. **Plain-language-as-document-standard is missing** as a first-class skill; plainspoken ≠ Federal/ISO plain language for public docs.
3. **STE dictionary gap** (verbs ≠ full dictionary) limits claim of full STE compliance.
4. **Humanize’s success metric leans “appear human”** more than “serve reader + meet genre norms + disclose when required.”
5. **Readability/usability validation** absent (no Flesch-as-smoke-alarm, no task-test prompt)—formulas are limited but still used as gates in industry.[[11]](https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests)
6. **Cross-skill conflict resolution** underspecified (e.g., ste + humanize on a README; plainspoken sentences inside an STE procedure).
7. **Disclosure / provenance / appropriate-use policy** absent despite material trust literature.[[17]](https://arxiv.org/html/2604.27129v1)
8. **International/global English** beyond STE and “American spelling”: limited guidance on localization, cultural references, bias-free language (Microsoft/Google emphasis).[[10]](https://learn.microsoft.com/en-us/style-guide/welcome/)

### Product gaps (relative to synthesis)
| Gap | Why it matters (evidence link) |
|---|---|
| Dedicated **plain language (document)** skill | Federal/ISO principles for public and mixed audiences |
| **Audience & risk router** | Best practice is conditional on purpose/audience/stakes |
| Fuller **STE dictionary support** or checker workflow | Compliance needs Part 2, not verbs alone |
| **Scientific/technical subtypes** beyond paper override | Grants, incident reports, API refs differ |
| **Disclosure / AI-use note** templates | Trust and scholarly/comms norms |
| **Usability/readability check** pass | Testing is core to plain language; formulas as weak signals |
| **Style-guide packs** (Microsoft/Google/Chicago toggles) | Real orgs write to house standards |
| Explicit **anti-evasion ethics** stance in humanize | Detectors brittle; integrity risk of “pass as human” framing |

---

## (4) PROPOSED EXTENSIONS — Prioritized collaborative pitch

Framed for the maintainer as optional, evidence-tied increments. Priority = impact × fidelity to literature ÷ implementation cost.

### P0 — High impact, natural fit

**E1. `audience-router` (pre-skill or shared frontmatter)**  
Before ste/plainspoken/humanize, collect or infer: purpose, audience expertise, native-language mix, risk (safety/legal/reputation), genre, disclosure needs. Emit a one-line “writing contract” that selects/parameterizes skills.  
*Tied to:* plain language and ISO emphasis on intended reader; STE genre bounds; Pyramid for decisions.[[4]](https://www.iplfederation.org/iso-standard/)

**E2. `plain` document skill (Federal/ISO-oriented)**  
Separate from plainspoken chat mode: points first, pronouns, everyday words + explain terms, headings/lists/tables, subject–verb proximity, omit needless words, active voice, short sections, optional “smoke-alarm” readability stats, prompt to name a comprehension test.  
*Tied to:* Federal top-10 / Plain Writing Act practice; ISO 24495 relevant/findable/understandable/usable.[[3]](https://www.archives.gov/open/plain-writing/10-principles.html)

**E3. Humanize reframing + ethics block**  
Rename success criteria toward **“specific, committed, reader-fit prose under the author’s voice”**; keep anti-tell audit as quality control. Add explicit: do not introduce errors; do not optimize primarily to evade detectors; offer disclosure blurb when publishing in contexts that expect it.  
*Tied to:* detector brittleness and paraphrase evasion; transparency dilemma; integrity risks of humanizer tools.[[14]](https://arxiv.org/abs/2303.13408)

**E4. Cross-skill precedence matrix**  
Document: safety/procedure → ste wins; chat register → plainspoken; personal publishable voice → humanize (+ voice profile); public benefits copy → plain; science paper → humanize academic overrides; never humanize away STE mandatory warnings.  
*Tied to:* STE “not alone” disclaimer and genre-conditioned synthesis.[[1]](https://en.wikipedia.org/wiki/Simplified_Technical_English)

### P1 — Strong evidence, moderate build

**E5. STE dictionary companion**  
`references/ste-dictionary-min.md` or script hooks: top unapproved→approved map beyond current table; link/workflow to official Issue 9 Part 2; optional lint mode “flag non-approved candidates” vs. “full rewrite.”  
*Tied to:* STE two-part structure (rules + dictionary).[[1]](https://en.wikipedia.org/wiki/Simplified_Technical_English)

**E6. Gopen–Swan pass as shared micro-skill**  
Optional pass usable by humanize (default on for papers/docs) and plain: topic position, stress position, old-to-new, subject–verb ≤~7 words.  
*Tied to:* Gopen & Swan reader-expectation research.[[9]](https://cseweb.ucsd.edu/~swanson/papers/science-of-writing.pdf)

**E7. Genre packs inside humanize**  
Beyond papers: `incident-comms`, `api-reference`, `fundraising/email`, `grant`. Each toggles Pass 1 position-taking, cadence targets, and tell sensitivity.  
*Tied to:* synthesis table of purpose/type variation; academic override precedent already in skill.

**E8. Voice-profile UX**  
One-command calibration flow (already in AGENTS.md) promoted into skill description; warn when BLANK; optional multi-voice profiles (blog vs. work email).  
*Tied to:* generic-human failure mode; plain-language “write for reader” + author authenticity.

### P2 — Differentiating, longer horizon

**E9. `disclose` micro-skill**  
Templates for Substack/blog, internal docs, academic acknowledgments—what was drafted/edited/generated; keep human accountable for facts. Neutral on whether to disclose; makes the choice explicit.  
*Tied to:* reader–writer disclosure gap; trust erosion studies; scholarly non-disclosure harms.[[17]](https://arxiv.org/html/2604.27129v1)

**E10. Readability + structure linter**  
Extend `audit.py`: sentence length distribution, passive rate, heading hierarchy, jargon density proxy, Flesch as informational only—with commentary that formulas ≠ comprehension.  
*Tied to:* Flesch ubiquity and documented limitations.[[11]](https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests)

**E11. House style adapters**  
Thin packs: `ms-style`, `google-dev-style` terminology/voice toggles composable with plain/ste.  
*Tied to:* real technical orgs write to these guides.[[22]](https://developers.google.com/style)

**E12. Controlled-language siblings (optional)**  
Research spike: Caterpillar-style or domain glossary import for non-aero industries that want CNL without full STE.  
*Tied to:* CNL family beyond STE.[[2]](https://en.wikipedia.org/wiki/Controlled_natural_language)

### Suggested pitch narrative to maintainer

The repo already encodes three of the highest-leverage clusters in the literature—**controlled technical English**, **answer-first conversational rhetoric**, and **anti-generic substantive editing with scientific exceptions**. The largest evidence-based gaps are not “more AI tells,” but **(a)** document-level plain language, **(b)** explicit audience/risk routing, **(c)** STE dictionary depth, and **(d)** aligning humanize’s north star with reader-serving craft and disclosure norms rather than detector evasion. A collaboration that adds `plain` + router + precedence + ethics/disclosure keeps the repo’s sharp opinionation while matching how standards bodies and research say writing quality actually works.

---

### Uncertainty register (brief-wide)
- STE Issue 9 full rule IDs and dictionary entries were synthesized from secondary/official descriptions and the skill’s compression—not a line-by-line audit of the paid/free official PDF.
- AI trust/disclosure effects are mixed across studies; recommendations favor **choice architecture** (templates, norms) over a single mandate.
- Cadence CV and tell lists are practitioner-validated more than RCT-validated; treat as heuristics.
- No empirical A/B of this repo’s outputs was run; evaluation is design-to-literature fit.

---

*End of brief.*