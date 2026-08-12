# openai/gpt-5.4 — research output

Run `r-2026-0812-03`, dispatched 2026-08-12. Web search: on (this output rests on live sources read that day).

Completion tokens 8,285; prompt tokens 33,761; billed $0.243.

Verbatim model output, unedited.

---

Below is an **independent research brief** based on the supplied repo materials plus external evidence. I start from the literature and standards, then evaluate the repo’s three skills against that synthesis. Where evidence is thin or contested, I mark that explicitly.

---

# 1) SYNTHESIS FIRST — best practices for written communication, and how they vary by context

## Executive view

The strongest cross-context finding is simple: **good writing is audience-calibrated, purpose-driven, and genre-aware**. The stable core across standards is to help readers **find, understand, and use** information; to organize around user tasks and questions; to prefer concrete, precise, consistent wording; and to test communication against actual reader needs rather than surface style alone. Plain-language guidance, STE, and scientific-writing guidance all converge on clarity, but they **optimize for different constraints**: plain language for broad accessibility and actionability, STE for safety and translatability in technical contexts, and scientific rhetoric for evidential precision and reader expectation management. ([nces.ed.gov](https://nces.ed.gov/sites/default/files/rel-central/document/2024/10/Federal%20Plain%20Language%20Guidelines.pdf))

The emerging AI-writing literature adds a second principle: **do not optimize for “passing as human” at the expense of truth, provenance, or fit to genre**. Detection remains unstable and model-contingent, while disclosure norms are strengthening in at least some domains, especially scholarly publishing. That makes “humanization” defensible as a clarity/editing practice, but much less defensible when framed as concealment or impersonation. Evidence here is newer and less settled than the plain-language and technical-writing literatures. ([nature.com](https://www.nature.com/articles/s41598-025-27377-z))

---

## A. What remains constant across contexts

### A1. Start with audience, task, and intended use

The plain-language tradition is explicit that writers should begin with the audience before they draft, because users need to **find what they need, understand it, and use it**. The Federal Plain Language Guidelines make audience analysis the first step and tie organization, wording, and testing to user needs. ([nces.ed.gov](https://nces.ed.gov/sites/default/files/rel-central/document/2024/10/Federal%20Plain%20Language%20Guidelines.pdf))

For web and service content, this becomes even more task-centered: users come with a task, decide quickly whether content is useful, and benefit when pages surface top tasks and likely questions fast. ([nces.ed.gov](https://nces.ed.gov/sites/default/files/rel-central/document/2024/10/Federal%20Plain%20Language%20Guidelines.pdf))

**Implication:** “best writing” is not one style. It varies by:
- reader expertise,
- consequence of error,
- whether the text is read linearly or scanned,
- whether the goal is instruction, decision support, persuasion, explanation, or recordkeeping,
- and whether precision or accessibility is the binding constraint. ([nces.ed.gov](https://nces.ed.gov/sites/default/files/rel-central/document/2024/10/Federal%20Plain%20Language%20Guidelines.pdf))

### A2. Organize for usability before polishing style

Across plain-language guidance, strong organization comes before sentence-level cleanup. Readers do better when information is grouped by topic, headings reflect user questions, paragraphs stay on one topic, and key points appear where readers expect them. The Federal Guidelines emphasize organization, topic sentences, one topic per paragraph, and testing. ([nces.ed.gov](https://nces.ed.gov/sites/default/files/rel-central/document/2024/10/Federal%20Plain%20Language%20Guidelines.pdf))

Scientific-writing guidance reaches a similar conclusion from a cognitive angle: Gopen and Swan argue that clarity depends heavily on placing information where readers expect it, especially using sentence openings to orient readers and sentence endings to carry emphasis. ([plantscience.psu.edu](https://plantscience.psu.edu/research/labs/guiltinan/resources/readings-in-scientific-method-and-writing/the-science-of-scientific-writing/view?utm_source=openai))

### A3. Prefer precision, consistency, and concrete language

Plain-language guidance recommends precise and concise words, familiar vocabulary where it preserves meaning, and consistent terminology across a document. ([nces.ed.gov](https://nces.ed.gov/sites/default/files/rel-central/document/2024/10/Federal%20Plain%20Language%20Guidelines.pdf))

STE goes further by formalizing consistency: one word should carry one approved meaning, terminology should be stable, and ambiguity should be reduced because controlled language improves comprehension and reduces variation in source texts. That matters not just for readers, but also for maintenance, translation, and safety-critical use. ([asd-ste100.org](https://www.asd-ste100.org/about_STE.html?utm_source=openai))

### A4. Test against real readers or realistic tasks

Plain-language guidance explicitly includes testing techniques and recommends learning from user questions, metrics, and observed tasks. ([nces.ed.gov](https://nces.ed.gov/sites/default/files/rel-central/document/2024/10/Federal%20Plain%20Language%20Guidelines.pdf))

In health communication, agencies emphasize development and testing because clear communication is not achieved by simplification alone; materials must be accurate, accessible, and actionable. CDC also stresses that health-literacy best practices are not “dumbing down” science. ([cdc.gov](https://www.cdc.gov/health-literacy/php/develop-materials/develop-test-materials.html?utm_source=openai))

---

## B. Controlled language and technical-writing standards

## B1. What STE is for

ASD-STE100 is a controlled language standard originally developed for maintenance documentation and now used more broadly in technical documentation. The official STE site states that the current version is **Issue 9, January 15, 2025**, and that STE is now treated as an international standard. It is recommended or required in safety- and airworthiness-related settings and is also referenced beyond aerospace. ([asd-ste100.org](https://www.asd-ste100.org/about_STE.html?utm_source=openai))

Its core value proposition is not merely “simple writing.” It is **clarity under operational constraints**: reduce ambiguity, improve comprehension for international readers, support consistent maintenance instructions, and minimize variation that can create translation or safety problems. ([asd-ste100.org](https://www.asd-ste100.org/about_STE.html?utm_source=openai))

## B2. What STE emphasizes

The repo summary aligns with many central STE principles:
- approved words and controlled meanings,
- active voice by default,
- imperative form for instructions,
- sentence-length limits,
- one topic per sentence/paragraph,
- consistent terminology,
- caution about ambiguity,
- and strict distinctions between procedure, description, and safety text. ([asd-ste100.org](https://www.asd-ste100.org/about_STE.html?utm_source=openai))

These are not generic style preferences. In STE they are a **system** tied to:
1. safety,
2. translatability,
3. non-native-reader comprehension,
4. and document standardization. ([asd-ste100.org](https://www.asd-ste100.org/about_STE.html?utm_source=openai))

## B3. Where controlled language should and should not dominate

The official STE site warns that software tools can support checking but do not themselves “write STE” or reliably convert arbitrary prose into compliant STE. It also says writers who aim to use STE correctly should rely on the official ASD-STE100 document. ([asd-ste100.org](https://www.asd-ste100.org/STEsoftware.html?utm_source=openai))

That matters because controlled language is highly useful in:
- maintenance procedures,
- safety notices,
- operational instructions,
- technical docs requiring consistent terminology,
- multilingual workflows,
- and documentation with high cost of misreading. ([asd-ste100.org](https://www.asd-ste100.org/about_STE.html?utm_source=openai))

But it is a weaker fit for:
- exploratory essays,
- persuasive blog posts,
- nuanced argument,
- or genres where voice, rhetorical variation, or evidential nuance matter more than lexical restriction.

**Implication:** best practice is not “apply STE everywhere technical.” It is “apply STE where controlled language’s benefits outweigh its expressive cost.” That nuance is visible in the standard’s purpose, even if not always explicit in simplified summaries. ([asd-ste100.org](https://www.asd-ste100.org/about_STE.html?utm_source=openai))

---

## C. Plain-language guidance

## C1. Plain language is broader than simplification

The Federal Plain Language Guidelines define the outcome in user terms: readers should be able to find, understand, and use what they need. That makes plain language broader than “short words and short sentences.” It includes:
- audience identification,
- information architecture,
- topic-first organization,
- concise and precise wording,
- meaningful headings,
- lists/tables when useful,
- illustrations where they help,
- and testing. ([nces.ed.gov](https://nces.ed.gov/sites/default/files/rel-central/document/2024/10/Federal%20Plain%20Language%20Guidelines.pdf))

WHO’s guidance similarly frames plain language as helping target audiences understand information, guidance, and advice, and as a way to move audiences to action. ([who.int](https://www.who.int/about/communications/understandable/plain-language?utm_source=openai))

## C2. Plain language is context-sensitive, not anti-technical

Plain-language guidance generally advises replacing jargon when everyday words preserve the same meaning, not eliminating precision. The Federal Guidelines say not to use jargon or technical terms when everyday words have the same meaning, implying that technical language remains appropriate when it is the precise term. ([nces.ed.gov](https://nces.ed.gov/sites/default/files/rel-central/document/2024/10/Federal%20Plain%20Language%20Guidelines.pdf))

That is consistent with CDC health-literacy guidance and with the scientific-communication literature: clarity does not mean distortion. ([cdc.gov](https://www.cdc.gov/health-literacy/php/develop-materials/develop-test-materials.html?utm_source=openai))

## C3. Evidence for plain language improving understanding

In health communication, evidence is stronger than in many other domains. A randomized trial found that plain-language versions improved adults’ understanding of health recommendations. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/38008266/?utm_source=openai))

CDC and related health-literacy guidance also reflect the accumulated finding that much health information is written in ways that many readers cannot use effectively, and that plain-language methods improve accessibility and actionability. ([cdc.gov](https://www.cdc.gov/health-literacy/php/develop-materials/develop-test-materials.html?utm_source=openai))

**Uncertainty:** the supplied evidence here is strongest for health and public-facing guidance, not for every domain equally. It is still reasonable to generalize the principle that user-centered clarity aids comprehension, but the degree of effect varies by genre and audience.

---

## D. General style and rhetoric standards

## D1. Point-first organization is often right, but not universal

The Pyramid Principle and related business-writing advice support leading with the answer, especially for decision-making contexts. That matches web/plain-language findings that users scan and decide quickly. ([nces.ed.gov](https://nces.ed.gov/sites/default/files/rel-central/document/2024/10/Federal%20Plain%20Language%20Guidelines.pdf))

But research-backed scientific-writing guidance complicates this. Gopen and Swan do not simply say “lead with the conclusion”; they emphasize **reader expectation**:
- put familiar context early,
- put stress-worthy new information late,
- keep subject and verb close,
- and create old-to-new flow across sentences. ([plantscience.psu.edu](https://plantscience.psu.edu/research/labs/guiltinan/resources/readings-in-scientific-method-and-writing/the-science-of-scientific-writing/view?utm_source=openai))

So “answer first” is best for many executive, service, and advisory contexts, but not all genres. In methods, legal reasoning, and technical explanation, orientation and sequencing can matter as much as directness.

## D2. Active voice is usually better, but not always

Plain-language and STE both prefer active voice because it makes agency clearer. ([nces.ed.gov](https://nces.ed.gov/sites/default/files/rel-central/document/2024/10/Federal%20Plain%20Language%20Guidelines.pdf))

But genre matters. Scientific and technical prose sometimes uses passive strategically when the agent is irrelevant or the process is the focus; the repo itself notes this for papers, and that is consistent with mainstream scientific-writing instruction. ([plantscience.psu.edu](https://plantscience.psu.edu/research/labs/guiltinan/resources/readings-in-scientific-method-and-writing/the-science-of-scientific-writing/view?utm_source=openai))

**Implication:** “active by default, passive by reason” is more defensible than a blanket ban.

## D3. Concision is usually good, but brevity can overshoot

The Federal Guidelines recommend concision and cutting unnecessary words. ([nces.ed.gov](https://nces.ed.gov/sites/default/files/rel-central/document/2024/10/Federal%20Plain%20Language%20Guidelines.pdf))

But readability research and scientific rhetoric both suggest that clarity is not reducible to shorter text. Gopen and Swan show that sentence structure and information placement matter; recent readability work also critiques purely surface-level metrics. ([plantscience.psu.edu](https://plantscience.psu.edu/research/labs/guiltinan/resources/readings-in-scientific-method-and-writing/the-science-of-scientific-writing/view?utm_source=openai))

So “cut filler” is good advice; “shorter is always clearer” is not.

---

## E. Readability research: what it supports, and what it does not

## E1. Readability is multidimensional

Traditional readability formulas focus on surface proxies such as word and sentence length. Those proxies can correlate with reading difficulty, but they are incomplete. Readability research is interdisciplinary and includes typography, structure, prior knowledge, and task context. ([arxiv.org](https://arxiv.org/abs/2107.09615?utm_source=openai))

Recent human-centered readability work argues that common NLP metrics miss dimensions like trustworthiness, tone, cultural relevance, and actionability. ([arxiv.org](https://arxiv.org/abs/2510.10801?utm_source=openai))

## E2. Sentence length caps are useful heuristics, not universal quality markers

STE’s sentence limits are part of a specialized controlled-language regime. They are valid **inside STE’s operational context**, not universal evidence-based thresholds for all writing. ([asd-ste100.org](https://www.asd-ste100.org/about_STE.html?utm_source=openai))

Outside that context, readability depends heavily on structure, coherence, and terminology choice. A longer but well-structured sentence can be easier than a short but contextless sentence. Gopen and Swan’s subject-verb proximity and stress-position principles support this view. ([plantscience.psu.edu](https://plantscience.psu.edu/research/labs/guiltinan/resources/readings-in-scientific-method-and-writing/the-science-of-scientific-writing/view?utm_source=openai))

## E3. Jargon is not categorically bad

A recent study on plain-language summaries of health research examines jargon and readability directly, and commentary in Nature notes the tradeoff: jargon can impair understanding for lay readers but can also signal precision and authority. The practical rule is audience-relative: avoid unnecessary jargon, but keep technical terms when they are the most accurate label and the audience can use them. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/39805102/?utm_source=openai))

---

## F. AI-generated, AI-disclosed, and “humanized” text

## F1. Detection is real but unstable

There is active work on detecting AI-generated text, but the literature also shows instability. A 2025 Scientific Reports paper notes that detectors trained on earlier outputs perform worse on newer, more sophisticated models, and that data diversity and model evolution remain major challenges. ([nature.com](https://www.nature.com/articles/s41598-025-27377-z))

NIST’s GenAI pilot includes a text-to-text detection task, which itself underscores that this is an open evaluation problem rather than a solved capability. ([nvlpubs.nist.gov](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.700-1.pdf))

**Implication:** advice based on a fixed list of “AI tells” is, at best, heuristic. It may catch stereotyped generated prose, but it cannot be treated as robust detection science.

## F2. “AI tells” often overlap with generic bad writing

Many so-called AI tells are also features of weak human writing: filler, generic abstraction, stacked hedges, ungrounded superlatives, scene-setting openers, and repetitive formatting. The repo’s `tells.md` is strongest when it treats these as signals for editorial review rather than deterministic evidence of machine authorship. That stance is more consistent with the evidence than claiming a stable detection rule.

## F3. Disclosure norms are strengthening in scholarly and high-accountability contexts

ICMJE now says authors, editors, publishers, and reviewers should be transparent about AI use, including which tool was used and for what purpose. It also indicates that nondisclosure can require corrective action and may amount to misconduct in some cases. ([icmje.org](https://www.icmje.org/recommendations/browse/artificial-intelligence/?utm_source=openai))

Other publisher guidance reflects a similar pattern: AI may assist, but humans remain responsible, AI is not an author, and disclosure is required when AI materially contributes beyond light polishing. ([journals.aps.org](https://journals.aps.org/authors/appropriate-use-ai-tools?utm_source=openai))

Anthropic’s own materials include an “AI diligence statement” tutorial that frames disclosure as a transparency practice. ([claude.com](https://claude.com/resources/tutorials/writing-an-ai-diligence-statement?utm_source=openai))

## F4. Disclosure and trust are not simple

The social evidence is unsettled. A recent vignette study found readers often see disclosure as more necessary than writers do, and view disclosure as more necessary when AI’s contribution is direct, irreplaceable, or not intentionally steered by the writer. ([arxiv.org](https://arxiv.org/abs/2604.27129?utm_source=openai))

Another recent study reports that disclosed AI use can trigger penalties from both human and LLM raters. ([arxiv.org](https://arxiv.org/abs/2507.01418?utm_source=openai))

So there is a real tradeoff:
- **transparency may support integrity norms**, especially in science and regulated contexts;
- **disclosure may also lower perceived quality or authenticity** in some evaluative settings.

**Uncertainty:** this literature is early, socially contingent, and likely to shift quickly.

## F5. The main risk is false humanization, not merely detectability

The most defensible practitioner position is:
- use AI to improve clarity, structure, and fit to audience;
- do not use it to fabricate human idiosyncrasy or conceal material authorship in contexts where provenance matters;
- and do not “roughen up” text with fake mistakes to simulate humanity.

That aligns with disclosure norms in publishing and with the repo’s own warning not to introduce errors intentionally. ([icmje.org](https://www.icmje.org/recommendations/browse/artificial-intelligence/?utm_source=openai))

---

## G. Context matrix: how best practice changes by purpose and genre

## G1. Procedures, maintenance docs, safety text
Best fit:
- controlled terminology,
- short imperative instructions,
- one action per sentence,
- explicit conditions,
- warning/caution structure,
- strong consistency. ([asd-ste100.org](https://www.asd-ste100.org/about_STE.html?utm_source=openai))

## G2. Public-facing service content and health information
Best fit:
- plain-language organization,
- clear headings,
- task orientation,
- familiar words where possible,
- visuals/lists where helpful,
- usability testing,
- actionability. ([nces.ed.gov](https://nces.ed.gov/sites/default/files/rel-central/document/2024/10/Federal%20Plain%20Language%20Guidelines.pdf))

## G3. Scientific papers
Best fit:
- evidential calibration,
- citations for non-obvious claims,
- reader-expectation structure,
- strategic use of technical terms,
- no forced certainty,
- passive by reason, not by reflex. ([plantscience.psu.edu](https://plantscience.psu.edu/research/labs/guiltinan/resources/readings-in-scientific-method-and-writing/the-science-of-scientific-writing/view?utm_source=openai))

## G4. Advisory chat / executive recommendation
Best fit:
- answer first,
- make the recommendation,
- state assumptions,
- avoid throat-clearing,
- calibrate detail to stakes. This is more practitioner consensus than formal standard, but it coheres with plain-language and task-oriented guidance. ([nces.ed.gov](https://nces.ed.gov/sites/default/files/rel-central/document/2024/10/Federal%20Plain%20Language%20Guidelines.pdf))

## G5. Essays, blogs, opinion writing
Best fit:
- distinct voice,
- concrete claims,
- rhythm and emphasis,
- anti-filler editing,
- but not necessarily controlled language or extreme anti-symmetry rules. Evidence here is less standardized and more rhetorical than formal.

---

# 2) TOOL EVALUATION SECOND — assessing `ste`, `plainspoken`, and `humanize`

## Overall verdict

The repo is strongest when read as **three aggressive editorial modes**:
- `ste` for controlled technical prose,
- `plainspoken` for answer-first chat,
- `humanize` for anti-filler, anti-generic revision.

That maps to real bodies of practice. But all three skills tend to **compress context-sensitive guidance into universal-sounding rules**. The biggest issue is not that they are wrong in spirit; it is that they are often **too absolute for the evidence base they borrow from**. The repo would be stronger if it made genre boundaries, disclosure norms, and evaluation criteria more explicit. ([asd-ste100.org](https://www.asd-ste100.org/STEsoftware.html?utm_source=openai))

---

## A. `ste`

## Where it fits the synthesis well

`ste` correctly captures many core STE features:
- active voice preference,
- imperative instructions,
- sentence caps,
- one meaning per word,
- terminology consistency,
- limited noun clusters,
- caution about ambiguity,
- procedural vs descriptive distinctions,
- and safety text conventions. ([asd-ste100.org](https://www.asd-ste100.org/about_STE.html?utm_source=openai))

It also explicitly limits strictness in chat and code identifiers, which is sensible.

## Where it diverges or oversimplifies

### 1. It implies compressibility that the official STE body itself cautions against
The README claims it “compresses the full standard” into one skill. But the official STE site says no tool can simply write STE for you or reliably convert arbitrary prose into STE; correct use depends on the official document. ([asd-ste100.org](https://www.asd-ste100.org/STEsoftware.html?utm_source=openai))

That does not make the skill invalid. It does mean the repo should position `ste` as an **operational approximation / coaching aid**, not as a faithful portable substitute for Issue 9.

### 2. It overextends STE to genres where controlled language is not clearly best
The README scopes `ste` to docs, procedures, READMEs, reports, UI text. Some of those fit better than others. Procedures and safety text are clear fits. Reports and some READMEs may require nuance or rhetorical flexibility that strict STE can flatten. The evidence supports contextual deployment, not universal use across “technical prose.” ([asd-ste100.org](https://www.asd-ste100.org/about_STE.html?utm_source=openai))

### 3. It risks confusing “clarity” with “compliance”
Sentence caps and verb restrictions are legitimate within STE, but not a general readability science. Without caveats, users may mislearn these as universal good-writing laws. ([asd-ste100.org](https://www.asd-ste100.org/about_STE.html?utm_source=openai))

## Net assessment
Good as a **controlled-language mode**. Weaker as a generalized clarity engine. It needs clearer boundary-setting and stronger disclaimers about approximation.

---

## B. `plainspoken`

## Where it fits the synthesis well

`plainspoken`’s “answer first” rule aligns with task-oriented communication and scan-heavy contexts, especially chat, support, and advisory use. Its emphasis on cutting preamble, making assumptions explicit, quantifying comparisons, and recommending a default also matches effective service communication. ([nces.ed.gov](https://nces.ed.gov/sites/default/files/rel-central/document/2024/10/Federal%20Plain%20Language%20Guidelines.pdf))

Its scope note—“chat prose, not deliverables”—is one of the repo’s best design choices because it acknowledges genre differences.

## Where it diverges or oversimplifies

### 1. “Decide, don’t survey” is useful but not universally best
For many user requests, giving a recommendation is better than dumping options. But in high-stakes, ambiguous, or preference-sensitive contexts, over-decisiveness can suppress legitimate tradeoffs. The evidence base supports task orientation, not a blanket anti-options norm. This is especially risky where user values, constraints, or harms vary materially.

### 2. “One idea per sentence” is more slogan than research-grounded rule
It pushes concision in a useful direction, but the scientific-writing literature shows that good sentences can coordinate orientation and payoff when structured well. The sharper evidence-backed principle is not “one idea per sentence”; it is “make sentence structure match reader expectation.” ([plantscience.psu.edu](https://plantscience.psu.edu/research/labs/guiltinan/resources/readings-in-scientific-method-and-writing/the-science-of-scientific-writing/view?utm_source=openai))

### 3. Some “AI tell” bans are stylistic taste disguised as detection
Bans on em dashes, triads, or “isn’t X, it’s Y” can help avoid overused LLM cadences. But they are not inherently signs of AI authorship, and good human prose uses them. The repo partly admits this in `humanize/references/tells.md`; `plainspoken` is more rigid. ([nature.com](https://www.nature.com/articles/s41598-025-27377-z))

## Net assessment
Strong mode for chat efficiency. Needs more explicit carve-outs for uncertainty, high-stakes advice, and cases where surfacing options is part of honest help.

---

## C. `humanize`

## Where it fits the synthesis well

This is the most interesting and the most problematic skill.

Its strongest features are not really “humanization”; they are **good editing**:
- cut filler,
- replace generic abstractions with specifics,
- distinguish calibrated from empty hedging,
- avoid empty scene-setting and redundant conclusions,
- keep technical terms when they are the precise term,
- and calibrate to a real writer’s voice using samples. ([nces.ed.gov](https://nces.ed.gov/sites/default/files/rel-central/document/2024/10/Federal%20Plain%20Language%20Guidelines.pdf))

The scientific-paper override is notably better than the generic mode. It correctly protects calibrated hedging, related-work balance, technical vocabulary, and conventional structure. It also imports Gopen & Swan in a way that is more evidence-based than the rest of the repo. ([plantscience.psu.edu](https://plantscience.psu.edu/research/labs/guiltinan/resources/readings-in-scientific-method-and-writing/the-science-of-scientific-writing/view?utm_source=openai))

The voice-profile mechanism is also a serious design choice: it shifts the goal from “generic human” to “this author’s documented habits,” which is more honest and produces better stylistic fit.

## Where it diverges or oversimplifies

### 1. The framing is ethically and evidentially overreaching
The description says “rewrite drafts so a person appears to have written them.” That frames the task as **appearance management**, not clarity or audience fit. In contexts where disclosure matters, that runs against current scholarly norms. ([icmje.org](https://www.icmje.org/recommendations/browse/artificial-intelligence/?utm_source=openai))

### 2. It leans too hard on folk detection
The `tells.md` catalog is useful as an editorial checklist, but the current research does not support treating these features as stable indicators of AI text across models and genres. Detection systems degrade as models change. ([nature.com](https://www.nature.com/articles/s41598-025-27377-z))

### 3. Some acceptance criteria are not evidence-grounded
The requirement that sentence-length coefficient of variation exceed 0.4, and that a piece must take at least one arguable position, are house heuristics, not established writing standards. They may improve some essays, but they are poor universal criteria. They are especially weak for explanatory docs, neutral summaries, and genres where overt stance is inappropriate.

### 4. It conflates genericity with machine-likeness
A lot of the “disease” it identifies—hedging, unnamed specifics, throat-clearing—is real. But those are also widespread human drafting habits. The most defensible claim is that the skill fights **bland, generic prose**, not that it reliably transforms “machine” prose into “human” prose.

## Net assessment
As an anti-filler editor with voice calibration, `humanize` is promising. As a “make this appear human-written” system, it is too close to concealment and too dependent on unstable AI-tell folklore.

---

# 3) GAP ANALYSIS — strengths, weaknesses, product gaps

## Strengths

### 1. Clear mode separation
The repo distinguishes chat mode (`plainspoken`), controlled technical writing (`ste`), and revision mode (`humanize`). That is good product architecture because the research base is also context-specific.

### 2. Strong anti-filler orientation
All three skills push against abstraction, hedging, and boilerplate. That aligns with plain-language and usability traditions. ([nces.ed.gov](https://nces.ed.gov/sites/default/files/rel-central/document/2024/10/Federal%20Plain%20Language%20Guidelines.pdf))

### 3. Good appreciation of genre conflict
The scientific-paper overrides in `humanize` show the maintainer understands that one style rule cannot span all writing.

### 4. Voice calibration as documented evidence
The blank voice profile is better than most generic “write like me” prompting because it asks for observable evidence, not invented persona traits.

## Weaknesses

### 1. Too many universal-sounding rules
The repo often presents local heuristics as if they were broad writing laws.

### 2. Thin treatment of audience and purpose
The literature starts with audience/task analysis; the repo starts with stylistic transformation. That is backwards from the strongest evidence. ([nces.ed.gov](https://nces.ed.gov/sites/default/files/rel-central/document/2024/10/Federal%20Plain%20Language%20Guidelines.pdf))

### 3. Weak disclosure/provenance stance
The repo says the skills make output read like a human wrote it. It does not distinguish:
- editing for clarity,
- adapting to a real authorial voice,
- and concealing substantive AI involvement.

That omission matters more now that disclosure norms are emerging. ([icmje.org](https://www.icmje.org/recommendations/browse/artificial-intelligence/?utm_source=openai))

### 4. Overreliance on AI-tell mechanics
The audit concept is useful, but the epistemic status of the flags is not strong enough in the current framing.

## Product gaps

### 1. No audience/purpose classifier or preflight
There is no skill that asks: Who is this for? What must the reader do? What is the consequence of misunderstanding? That is the missing top layer.

### 2. No plain-language deliverable mode
`plainspoken` is chat-only, while `ste` is technical and strict. There is no middle mode for public-facing docs, health-style explainers, product docs for mixed audiences, or executive summaries.

### 3. No disclosure/provenance support
There is no skill for drafting AI-use disclosures, diligence statements, or provenance notes for scholarly or professional contexts. This is a notable omission given the repo’s interest in “humanize.” ([icmje.org](https://www.icmje.org/recommendations/browse/artificial-intelligence/?utm_source=openai))

### 4. No evidence calibration mode
The scientific override exists inside `humanize`, but there is no standalone mode for evidence-calibrated writing that protects uncertainty, citations, and claim strength outside formal papers.

---

# 4) PROPOSED EXTENSIONS — prioritized collaborative pitch to the maintainer

Below is the extension set I would pitch first.

## Priority 1 — Add an `audience-purpose` preflight skill

### What it would do
Before any writing mode fires, ask or infer:
- audience expertise,
- purpose,
- top reader task,
- cost of misunderstanding,
- required tone,
- disclosure/provenance constraints,
- and whether the text is scanned, followed as procedure, or read as argument.

Then route to `ste`, `plainspoken`, `humanize`, or another mode with context-specific defaults.

### Why this is first
It aligns the repo with the strongest common finding across plain-language guidance: start from audience and use, not sentence tricks. ([nces.ed.gov](https://nces.ed.gov/sites/default/files/rel-central/document/2024/10/Federal%20Plain%20Language%20Guidelines.pdf))

### Suggested maintainer framing
“Right now the repo has style modes. Add a decision layer so the right mode is chosen for the right communicative job.”

---

## Priority 2 — Add a true `plain-language-docs` skill

### What it would do
A middle-ground document mode for:
- public-facing explainers,
- internal memos for mixed audiences,
- onboarding docs,
- customer support articles,
- health-style summaries,
- product overviews.

Rules should emphasize:
- find/understand/use,
- familiar words where meaning is preserved,
- task-first organization,
- clear headings,
- one topic per paragraph,
- lists and visuals when helpful,
- and testing assumptions against likely user questions. ([nces.ed.gov](https://nces.ed.gov/sites/default/files/rel-central/document/2024/10/Federal%20Plain%20Language%20Guidelines.pdf))

### Why it matters
The current repo jumps from conversational advice (`plainspoken`) to strict controlled language (`ste`). The literature says there is a large and important middle category.

---

## Priority 3 — Reframe `humanize` as `de-genericize` or `voice-calibrate`, and split ethics from style

### What to change
Rename or re-scope the skill from “make it appear a person wrote it” to:
- clarify,
- remove generic AI-ish smoothing,
- preserve genre-appropriate uncertainty,
- and match a documented house or personal voice.

### Add explicit guardrails
- Do not use to conceal AI involvement where disclosure is required by policy, publisher, employer, or contract.
- Do not fabricate human quirks or intentional mistakes.
- If provenance matters, suggest a disclosure block instead of hiding assistance. ([icmje.org](https://www.icmje.org/recommendations/browse/artificial-intelligence/?utm_source=openai))

### Why this is high priority
This is the repo’s biggest trust risk. The underlying editing logic is good; the current framing is the problem.

---

## Priority 4 — Replace hard “AI tell” bans with confidence-graded editorial flags

### What to change
Turn `tells.md` and `audit.py` into a triage system:
- **high-confidence genericity/filler flags**: stacked hedges, attribution to nobody, empty scene-setting, redundant close;
- **context-dependent style flags**: em dashes, triads, bold-colon lists, “framework,” “leverage,” etc.;
- **genre exemptions**: scientific writing, reference docs, legal text, UI copy.

### Why
Current detection research shows model-sensitive instability, so the repo should present these as editorial heuristics, not signatures of machine authorship. ([nature.com](https://www.nature.com/articles/s41598-025-27377-z))

### Concrete pitch
“Keep the audit, but downgrade its certainty claims. Make it a better editor and a weaker detector.”

---

## Priority 5 — Add a `scholarly-integrity` or `evidence-calibrated` skill

### What it would do
For papers, reports, analyses, grant text, and technical argument:
- preserve calibrated hedging,
- require attribution for non-obvious claims,
- distinguish evidence from inference,
- keep technical terms where precise,
- block overclaiming,
- encourage Gopen & Swan sentence design,
- and optionally produce an AI-use disclosure note when needed. ([plantscience.psu.edu](https://plantscience.psu.edu/research/labs/guiltinan/resources/readings-in-scientific-method-and-writing/the-science-of-scientific-writing/view?utm_source=openai))

### Why
The current scientific override is buried inside `humanize`; it deserves to be a first-class mode.

---

## Priority 6 — Soften `plainspoken` with an “uncertainty protocol”

### What to change
Retain answer-first, but add:
- when stakes are high or user preferences dominate, briefly surface the decision variable;
- if evidence is uncertain, say so in the first sentence;
- if a fork is irreversible, ask before committing.

### Why
This preserves the mode’s speed while reducing the risk of false decisiveness. It fits both honest communication and user-centered guidance.

---

## Priority 7 — Reposition `ste` as “STE-assisted,” not “STE-complete”

### What to change
In README and skill text:
- say it is a working compression/assistant for STE-aligned drafting,
- recommend checking against the official ASD-STE100 document for true compliance,
- and emphasize best-fit contexts: procedures, maintenance, safety, and controlled technical docs. ([asd-ste100.org](https://www.asd-ste100.org/STEsoftware.html?utm_source=openai))

### Why
This is more accurate to the official standard’s own stance and lowers compliance overclaim risk.

---

## Priority 8 — Add evaluation rubrics tied to purpose, not universal style metrics

### Replace current universal acceptance criteria with mode-specific ones

Examples:
- **plain-language-docs:** can target users find the action, understand terms, and complete the task? ([nces.ed.gov](https://nces.ed.gov/sites/default/files/rel-central/document/2024/10/Federal%20Plain%20Language%20Guidelines.pdf))
- **STE-assisted:** terminology consistency, imperative procedures, sentence/paragraph constraints, safety labeling. ([asd-ste100.org](https://www.asd-ste100.org/about_STE.html?utm_source=openai))
- **voice-calibrate:** reduced filler, preserved authorial habits, no fake quirks, provenance policy respected.
- **scholarly-integrity:** claims calibrated to evidence, citations present, no unsupported generalizations. ([icmje.org](https://www.icmje.org/recommendations/browse/artificial-intelligence/?utm_source=openai))

### Why
A single CV threshold or “must take a position” criterion is not evidence-grounded across genres.

---

# Bottom line

My opinionated read is:

1. The repo already contains the core of something useful.  
2. Its best ideas are **contextual writing modes**, **anti-filler revision**, and **voice calibration from evidence**.  
3. Its weakest point is the current “humanize” framing and the tendency to present house heuristics as universal research-backed rules.  
4. The most valuable collaboration pitch to the maintainer is not “add more anti-AI tricks.” It is: **add an audience/purpose layer, a plain-language docs mode, a scholarly-integrity mode, and stronger provenance guardrails.**

If you want, I can turn this into a **maintainer-facing memo** or a **GitHub issue / proposal draft** next.