# anthropic/claude-opus-4.7 — research output

Run `r-2026-0812-03`, dispatched 2026-08-12. Web search: on (this output rests on live sources read that day).

Completion tokens 16,408; prompt tokens 355,942; billed $2.290.

Verbatim model output, unedited.

---

I'll research the external literature first, then evaluate the repo against it. Let me gather evidence across the domains the brief specifies.I have enough material to write a strong brief. Let me do one more targeted search on the ethics/risks of "humanizing" AI text and detector evasion, which is directly relevant to the `humanize` skill.I have a strong evidence base. Now I'll write the brief.

---

# A Research Brief on Written-Communication Best Practices, with Application to `claude-writing-skills`

**Prepared for:** DHK, Head of Data, Infinitus Systems
**Purpose:** Independent literature synthesis to serve as the evidence base for a collaborative proposal of extensions to `github.com/nonatofabio/claude-writing-skills`.
**Method note:** This brief is written by one model in a multi-model commission; where the evidence is thin or contested I say so. All external claims are cited to sources returned by web search on 12 Aug 2026.

---

## Part 1 — Synthesis: what the literature says about good writing

The literature on written-communication best practices does not converge on a single "good writing." It converges on a stronger claim: **best practice is a function of purpose, audience, and genre**, and the same feature (a hedge, a passive verb, a heading, a triadic list) can be a virtue in one context and a defect in another. This section organizes the evidence along that axis.

### 1.1 The context-dependence of "good writing" — the genre frame

The dominant modern account of how written communication should be evaluated is rhetorical genre theory, most influentially Carolyn Miller's 1984 "Genre as Social Action." A rhetorical approach to genre should focus not on form or content but on recurrent rhetorical action. Genre is reconceived as social action in response to recurrent rhetorical situations perceived as a combination of purpose, audience, and occasion. Practically, this means: awareness of audience and purpose influences both what and how a writer writes.

The corollary matters for any general-purpose writing tool: rules that are appropriate for procedural aerospace maintenance documentation are not appropriate for a personal essay, and rules that are appropriate for a personal essay are not appropriate for a scientific paper. Every subsection that follows should be read against this frame.

### 1.2 Controlled-language / technical-writing standards

**ASD-STE100 Simplified Technical English (STE).** STE is the reference standard for high-stakes technical documentation. It is a controlled natural language designed to simplify and clarify technical documentation, originally developed in the 1980s by the European Association of Aerospace Industries (AECMA) at the request of the European Airline industry, which wanted a standardized form of English for aircraft maintenance documentation that could be easily understood by non-native English-speakers. The current edition, published in January 2025, consists of 53 writing rules and a dictionary of approximately 900 approved words.

The design intent is safety-critical and translation-oriented, not aesthetic: complex technical instructions can be misunderstood, and misunderstandings can lead to accidents; STE helps operators understand maintenance instructions correctly, removes linguistic barriers, and reduces Human Factor risks. The core mechanisms are one meaning per word, active voice, simple tenses, one instruction per sentence, short sentences, no dropped words and the writing rules differentiate between two types of texts: procedures and descriptions.

**Scope caveats from the standard's own maintainers and adjacent literature.**

1. STE is a technical-documentation standard, not a general prose standard. The STE guide was never meant to become a general writing standard; nevertheless, it was successfully adopted by many industries. STE is more strictly controlled — while plain English aims for general clarity, STE follows precise rules tailored for technical writing.
2. Even inside its scope, STE cannot be fully automated. No language checker can guarantee full compliance with STE, because the goal of STE is clarity — only human writers can judge whether a sentence or paragraph makes good sense.
3. Mastery is non-trivial. Despite its name, STE is not an easy language to learn through self-study; authors can spend their entire careers writing technical documents in STE and never fully grasp it. With its stringent rules, mastering STE is similar to learning a new language in some ways.

**Comparable controlled Englishes.** STE has cousins. Caterpillar Fundamental English (CFE) was an influential controlled language developed at Caterpillar, officially introduced in 1971, based on Basic English, and reported to be the earliest industry-based CNL. Its history contains a warning relevant to any rule-driven tool: CFE was discontinued by Caterpillar in 1982 because (among other reasons) the basic guidelines of CFE were not enforceable in the English documents produced. Caterpillar Technical English was developed following a different approach: the restrictions on the language should be enforceable. **Enforceability, not elegance, is what makes a controlled language survive in production.**

Kuhn's 2014 survey names dozens of industry controlled Englishes (Nortel Standard English, IBM EasyEnglish, PACE, KANT, GM Global English, and others), which suggests STE is one point on a design space, not the only serious answer for "clear technical prose."

### 1.3 Plain-language guidelines

Plain language is a broader tradition than STE, targeting general public-facing government and civic writing rather than machine-parseable safety documentation. In the US the anchor is the Plain Writing Act of 2010: the broadest, clearest, and most well-known plain language law is the Plain Writing Act of 2010, signed into law on October 13, 2010. It aims to make government information easier for people to access and understand, and requires federal agencies to use clear language that the public can understand.

The Federal Plain Language Guidelines (PLAIN / plainlanguage.gov) codify the operational advice: avoid jargon, redundancy, ambiguity, and complex words; write briefly and clearly; use definite, concrete, everyday language; write in short sentences; use active voice; use bullet lists for complex material; avoid legal, business, and medical jargon; avoid double negatives.

Two nuances are widely under-appreciated:

- **Audience, not simplicity, is the first principle.** The first rule of plain language is: write for your audience. One of the most common plain language myths is that you have to "dumb down" your content so that everyone can read it. That's not true. Use language your audience understands and feels comfortable with.
- **Plain language is testable, not just prescribed.** The Federal Plain Language Guidelines stress the importance of understanding the audience, organizing content logically, using plain language techniques, and testing documents for clarity to ensure information is easy to find, understand, and use.

### 1.4 Structure / rhetoric standards for business and technical prose

For decision-oriented prose (memos, reports, briefings, executive email), the dominant standard is Barbara Minto's Pyramid Principle. Barbara Minto's pyramid principle is a communication method that structures ideas with the main conclusion first, followed by supporting arguments organized in logical groups to create clear, compelling business documents. This structure aligns with how executives process information — top-down and outcome-focused. The Minto Pyramid enforces logical, MECE thinking: by organizing arguments in a mutually exclusive, collectively exhaustive way, it ensures that ideas are structured, non-overlapping, and collectively complete.

Crucially — and this is often lost in one-line summaries — the Pyramid Principle is genre-scoped. Its own literature names when *not* to use it: avoid the Pyramid Principle when your audience needs to be emotionally engaged before hearing your conclusion, when you're delivering bad news that requires context first, or when you genuinely don't have a recommendation yet. It's designed for situations where you have a clear answer and a decision-making audience.

For scientific and technical prose, the standard reference is Gopen & Swan's "The Science of Scientific Writing" (American Scientist, 1990). Its central claim is reader-expectation, not rule-based: the meaning of any prose is not that which the writer intends, but that which readers interpret. Readers interpret prose more easily and more uniformly if information is placed where they expect it. When readers' expectations are met, they are more likely to get the "correct" interpretation. The two operational moves most cited from it are:

- "Save the best for last" (stress position) and "First things first" (topic position). In the stress position the reader needs and expects closure and fulfillment; in the topic position the reader needs and expects perspective and context.
- Put in the topic position the old information that links backward; put in the stress position the new information you want the reader to emphasize.

Gopen and Swan explicitly frame these as principles, not laws: Gopen and Swan also make clear that these are "principles" not "rules."

### 1.5 Readability research

Readability formulas (Flesch, Flesch-Kincaid, Dale-Chall, SMOG, Fog, Fry) are the oldest quantitative writing-quality literature and remain the default in most editing tools. The earliest works focused on the construction of readability formulae; these measures rely on shallow textual characteristics such as the number of sentences, average length of sentences and average word length. For example, one of the most well known readability scores is the Flesch-Kincaid score, which takes the average number of words per sentence as well as the average number of syllables as a proxy for syntactic and semantic difficulty.

The modern consensus is that these formulas are useful but limited. The Flesch-Kincaid readability assessment tool along with other traditional metrics remains widely used to measure text complexity yet fails to accurately measure text difficulty because it only evaluates quantifiable characteristics of word length and sentence structure (DuBay, 2004). The formulas concentrate on surface-level characteristics while neglecting complex linguistic elements that affect comprehension, especially in online texts, together with technical documentation and domain-specific content. There are multiple limitations to readability formulae. Firstly, these formulae are based on surface characteristics of text, and ignore deeper levels of text processing known to be important factors of readability. DuBay emphasizes the reader side: prior knowledge and reading skills might impact how easy a text is.

The takeaway for a writing tool: **surface metrics (sentence length caps, syllable counts, coefficient-of-variation targets) are usable proxies but should be presented as diagnostics, not acceptance tests, and never applied uniformly across genres.**

### 1.6 Signs-of-AI-writing and the "humanize" literature

This is the newest and most volatile body of practitioner discourse. Its most-referenced artefact is Wikipedia's community-maintained "Signs of AI writing" page. TechCrunch's characterization: the group's public guide to "Signs of AI writing" is the best resource I've found for nailing down whether your suspicions are warranted.

The identifiable patterns cluster into families:

- **Vocabulary drift.** 2023 to mid-2024 (GPT-4): Additionally, boasts, bolstered, crucial, delve, emphasizing, enduring, garner, intricate/intricacies, interplay, key, landscape, meticulous/meticulously, pivotal, underscore, tapestry, testament, valuable, vibrant. Mid-2024 to mid-2025 (GPT-4o): align with, bolstered, crucial, emphasizing, enhance, enduring, fostering, highlighting, pivotal, showcasing, underscore, vibrant.
- **Structural tells.** Negative parallelisms: "It's not X, it's Y." Rule of threes: AI defaults to triplets when listing anything: adjectives, benefits, takeaways. Em dash overkill: deployed for punchy emphasis where a comma would do. Formatting overkill: excessive bolding of key terms. AI vocabulary: delve, intricate, tapestry, pivotal, underscore, landscape, foster, testament, enhance, crucial.
- **Compulsive closure.** Compulsive summaries: "Overall," "In conclusion" — the tendency to restate what was just said, even when the passage is too short to require it. Human writers sometimes do this in long documents, but AI does it reflexively.

Two important caveats sit inside this literature, both under-cited in the practitioner discussion:

1. **The tells are volatile and shift with model releases.** For a few months last year, everyone became convinced that specific words like "delve" or "underscore" could give models away, but the evidence is thin, and as models have grown more sophisticated, the telltale words have become harder to trace. The signs of AI use vary between models and are constantly changing over time. There was indeed a time where ChatGPT in particular loved to use the em dash. But that was one model at one particular point in time. In all the mass of AI text I've seen on Wikipedia over the past 8 months or so, the em-dash isn't even something I bother to look for at this point.
2. **Human and AI language are converging.** Human speech and writing is being influenced by LLMs, and thus they are becoming more similar. This was already evident in 2024, as shown by a study that detected a significant LLM influence in spoken content (e.g. conversational podcasts). Further studies seem to confirm this influence on language, including semantics and word choices.

### 1.7 Detectability, reader trust, and the ethics of "humanizing"

The literature on AI-text detection and reader response is unstable but converges on three findings:

**a) Humans cannot reliably detect AI text.** People are increasingly unable to distinguish AI-generated text from human writing without explicit disclosure, a finding that holds true even for those knowledgeable about large language models. Clark et al. (2021) found that even trained annotators performed only marginally above chance when distinguishing AI outputs from human writing, particularly for shorter texts.

**b) Automated detection is unreliable and biased.** Perkins et al. evaluated six major detectors and found their average accuracy (already a modest 39.5%) dropped to 17.4% when faced with texts lightly modified to evade detection. Vanderbilt University disabled Turnitin's AI detection in August 2023, noting that even 1% false positives applied to 75,000 papers yields ~750 wrongful accusations annually. Studies also demonstrated systematic bias against non-native English speakers, with seven detectors showing 61.3% false positive rates on TOEFL essays compared to near-zero on native English writing. This occurs because perplexity-based detection systematically penalizes simpler vocabulary and grammatical structures commonly used by English language learners. False positives are particularly common for non-native English speakers and for technical or formulaic academic writing.

**c) Disclosure has a "transparency penalty," but effects are context-dependent.** Research on AI disclosure highlights its paradoxical effect on interpersonal trust. Several studies show that when readers learn AI contributed to a text, their trust in the human author declines even if the quality of the text is unchanged. This "transparency penalty" challenges the conventional assumption that openness builds trust. The more AI was stated to be present, the less trustworthy participants perceived the email. But: AI disclosure significantly reduced the perceived credibility of correct information while unexpectedly increasing the perceived credibility of misinformation. Negative attitudes towards AI significantly moderated these effects. And the magnitude of this trust erosion is not uniform and appears to be moderated by individual differences. People with more positive attitudes toward AI show a smaller decline in trust upon disclosure. A user's AI literacy plays a significant role in shaping their perceptions — AI-literate individuals tend to view its use as pragmatic, whereas less knowledgeable readers may interpret it as a sign of incompetence or laziness.

**d) The ethics of "humanizing" divide sharply by context.** In academic and scholarly contexts the practitioner consensus is that active detector-evasion is misuse: institutional guidelines on AI use increasingly emphasise transparency, academic integrity, and responsible disclosure of AI assistance. So using AI content humanizers to deliberately mask AI authorship is seen as cheating and dishonest, even if it helps you pass initial AI detection checks. More generally: while humanizers can enhance productivity, misuse could blur the lines between assistance and deception. Institutions emphasize integrity, viewing over-reliance on AI as a form of academic dishonesty. Ethically, users should treat humanizers as editing aids rather than substitutes for original thought. Transparency is key — disclosing AI involvement where required fosters trust and upholds scholarly standards.

The academic-integrity literature has increasingly concluded that detection is a losing arms race and the appropriate response is disclosure norms, not detector-hardening: this study examines the methodological challenges of detecting AI-generated content in neurosurgical literature through a two-fold approach: first, by applying current detection methods to quantify potentially AI-generated content, and second, by using these results to illustrate the fundamental limitations of detection-based approaches. Rather than claiming definitive identification of AI-generated text, we aim to demonstrate why the academic community should shift focus from detection to transparency and ethical guidelines.

**Synthesis of Section 1.7:** removing AI tells to sound like a human is a legitimate editorial goal *when the tells themselves signify low-information, safe, generic prose* — i.e. when they mark bad writing rather than merely non-human writing. Removing tells to evade detection while masking undisclosed AI authorship is a different activity with a different ethical status, and the two must be kept apart at the tool level.

### 1.8 What varies across content types — a consolidated view

Pulling the strands together, the following table is defensible from the sources above:

| Genre | Primary standard(s) | What "good" prizes | What kills the piece |
|---|---|---|---|
| Aircraft/industrial procedures | ASD-STE100 | Unambiguous action; one meaning per word | Ambiguity in a step; synonyms |
| Government/public info | Plain-language guidelines, Plain Writing Act | Reader can act on it | Jargon, buried lede |
| Executive memo, consulting deck | Minto Pyramid Principle | Answer-first, MECE support | Building to conclusion; menu of options with no recommendation |
| Scientific paper | Gopen & Swan; IMRaD conventions | Calibrated claims; topic/stress position; citations | Overclaiming; broken old-to-new flow |
| Blog / essay / launch post | Practitioner consensus + "signs of AI writing" | Specificity, position, cadence variation | Generic vocabulary; both-sidesing; compulsive summary |
| Chat / conversational reply | BLUF / answer-first | Meaning in the first token | Preamble; menu of options |

The genre literature (§1.1) is the discipline that says: pick the row before you pick the rules.

---

## Part 2 — Evaluation of the `claude-writing-skills` repo against the synthesis

I evaluate each skill on three dimensions: **fidelity to its cited source**, **coverage of the relevant literature**, and **context/audience sensitivity**.

### 2.1 `ste` — Simplified Technical English

**Fidelity.** High. The skill correctly identifies the standard, the current issue (Issue 9, January 2025), the two-part structure (writing rules + dictionary), the procedure/description distinction, the 20/25-word sentence caps, and the one-meaning-per-word principle. All of these match the source material (§1.2). The 900-approved-word dictionary, six-sentence paragraph cap, and no-semicolon rule reflect the standard as documented.

**Coverage.** Adequate for the standard itself, but the skill inherits a scope confusion that the standard's own maintainers warn against. The SKILL.md says its scope is "technical prose deliverables (docs, procedures, READMEs, reports, UI text)." Two problems:

1. **STE was designed for aircraft maintenance manuals with non-native readers and potentially fatal consequences of misreading**, not general-purpose software READMEs. The key driver for the creation of a controlled and simplified form of English was a request from the airlines (80% of which were not from English-speaking countries) to ensure accurate maintenance practices and guarantee aircraft availability and safety. Complex technical instructions can be misunderstood, and misunderstandings can lead to accidents. The STE guide was never meant to become a general writing standard. The repo's framing does not warn the user that they are applying an aerospace-safety controlled language to a blog-adjacent artefact, which will strip legitimate voice from a README that has no safety exposure.
2. **The skill treats STE as mechanically enforceable, but the standard's implementers explicitly say it is not.** No language checker can guarantee full compliance with STE, because the goal of STE is clarity. Only human writers can judge whether a sentence or paragraph makes good sense.

**Context sensitivity.** Weak. The skill has one persistence mode ("on until off") and no branching for procedures vs. descriptions vs. safety-critical text at the invocation layer, even though the standard itself treats these as different genres with different rules (Sections 5, 6, 7 of the standard, all of which the SKILL correctly lists but does not gate on).

### 2.2 `plainspoken` — talking-register mode

**Fidelity.** The skill is a fair distillation of the Pyramid Principle for chat register: "answer first," "decide, don't survey," own the voice, cut preamble. All of this matches Minto (§1.4). Putting the "answer first" offers instant clarity and helps your audience grasp your message immediately. This top-down method also lowers the chance that crucial insights will be hidden.

**Coverage.** Good on Minto, thin on the counter-cases. Minto's own literature is explicit that answer-first is not universal. Avoid the Pyramid Principle when your audience needs to be emotionally engaged before hearing your conclusion, when you're delivering bad news that requires context first, or when you genuinely don't have a recommendation yet. The `plainspoken` SKILL.md acknowledges "if the honest answer is 'it depends'" and "if you don't know," but does not address the two harder cases: emotional-context-first and bad-news delivery.

**Context sensitivity.** Reasonable at the register level — it correctly scopes itself to chat prose ("this governs chat prose, not deliverables"). This is the right move; the failure of many practitioner guides is that they apply BLUF/answer-first universally, ignoring §1.1's genre point.

**A small technical note.** The AI-tells list inside `plainspoken` (em dashes as crutch, hype adverbs, triads for rhythm, "isn't X, it's Y") is well-supported by the current practitioner literature (§1.6). But the ban on em dashes and hype adverbs at the register level risks the same problem the Wikipedia editors flag: this kind of thing only worsens the problem, because not only is it not a reliable sign which therefore can lead you to wrongly accuse people of using AI, but it also means that people stop trusting those of us who actually take the effort to learn how to identify AI properly, because they get used to random people going "pfft, that has to be AI!" because they saw an em dash or the word "delve."

### 2.3 `humanize` — draft-rewriter

**Fidelity.** The skill is unusually self-aware among tools in this space. It correctly (a) diagnoses the underlying problem as "picks the likeliest next word … the safest choice in its slot," (b) names Orwell's rules in order, (c) invokes Gopen & Swan by name for the scientific-paper override section (stress position, topic position, old-to-new flow, subject-verb proximity), and (d) explicitly warns against overcorrection ("Aggressive de-slopping has its own tells").

All four of these move it well ahead of most practitioner tooling. In particular, the stress/topic position content is a direct and correct import of Gopen & Swan (§1.4): to summarize the principles connected with the stress position, we have the proverbial wisdom, "Save the best for last." To summarize the principles connected with the topic position, we have its proverbial contradiction, "First things first." In the stress position the reader needs and expects closure and fulfillment; in the topic position the reader needs and expects perspective and context. Put in the topic position the old information that links backward; put in the stress position the new information you want the reader to emphasize.

**Coverage — three gaps.**

1. **The literature on human/AI language convergence isn't reflected.** The tells catalog (`tells.md`) reads as timeless, but as models have grown more sophisticated, the telltale words have become harder to trace and the tell vocabulary is model-generation-specific: 2023 to mid-2024 (GPT-4) vs Mid-2024 to mid-2025 (GPT-4o) have measurably different tell sets. A durable audit needs to timestamp its wordlist and version it.

2. **The disclosure/ethics dimension is absent.** The skill's job description ("Rewrite drafts so a person appears to have written them") is ambiguous between two goals — improving prose whose *tells* are the problem, and making AI-written prose harder to attribute. The literature (§1.7) is emphatic that these are ethically distinct activities and that the second, when undisclosed, is treated as academic misconduct. Institutional guidelines on AI use increasingly emphasise transparency, academic integrity, and responsible disclosure of AI assistance. So using AI content humanizers to deliberately mask AI authorship is seen as cheating and dishonest. The current SKILL.md's scientific-paper override handles the linguistic side but not the disclosure norm.

3. **The audience side of plain language is under-represented.** The `humanize` skill is heavily *style*-focused. It does not include a "who is this for?" step, whereas the plain-language literature makes that the first principle: the first rule of plain language is: write for your audience. A rewrite that removes hedges to sound committed can degrade a piece written *for* a lay/regulatory audience where calibrated hedge is part of the contract.

**Context sensitivity.** The scientific/academic override is the strongest genre-branching feature in the whole repo, and its content is correct: the guidance to keep calibrated hedges, not force claims past evidence, treat "significant" and "robust" as technical terms in a paper, and skip cadence targets in IMRaD-conventional sections all track §1.4 and §1.7. But the branching is binary (papers vs everything else) where the genre literature (§1.1) suggests at least four or five distinct contexts.

**The acceptance-criteria design is the single most opinionated choice in the repo.** Criterion 3 ("Sentence-length coefficient of variation is above 0.4, and no four consecutive paragraphs share the same sentence count") is a defensible operationalization of the practitioner claim that uniform sentence length is one of the strongest signs of AI writing in any text. But it inherits the readability-formula critique from §1.5: it is a surface metric, and the literature warns explicitly against treating surface metrics as acceptance tests. The SKILL.md acknowledges this in the papers override; the general case deserves the same acknowledgement.

---

## Part 3 — Gap analysis

### Strengths (keep these)

1. **Genre-aware overrides in `humanize`.** The scientific-paper override is best-in-class among practitioner tools I found — it correctly imports Gopen & Swan and correctly relaxes cadence, structure-symmetry, and vocabulary-tell rules for IMRaD. Ground truth: §1.4, §1.7.
2. **Voice-profile design in `humanize`.** Requiring three-to-five unedited samples and letting the profile override generic rules is well-aligned with plain-language theory's "write for your audience" and with the rhetorical-genre insight that a wide range of variation can and does exist because different rhetors respond differently to the same situation. The AGENTS.md's insistence on evidence-quoted `Observed patterns` lines is a strong pattern.
3. **Skill-as-mode framing.** The persistent-mode design (on/off) matches how professional writers move between registers (technical manual mode vs email mode vs paper mode). Consistent with §1.1.
4. **Correct disavowal of surface-only fixes in `humanize`.** The SKILL.md explicitly warns "Ban them and the model reaches for the second-most-average word. The draft still reads like a press release, now with a smaller vocabulary." This directly tracks §1.6's evidence on vocabulary drift and model-generation-specific tells.

### Weaknesses

1. **`ste`'s scope creep is not warned.** The skill applies an aerospace safety-critical language to READMEs and reports without flagging that the source standard's maintainers explicitly say it was not designed for that. Ground: §1.2.
2. **`humanize`'s tells catalog is time-frozen.** It reads as if AI tells are fixed. The evidence says they shift with each major model generation. Ground: §1.6.
3. **No disclosure/ethics scaffolding anywhere.** The strongest finding in the trust literature is the "transparency penalty" but also that undisclosed use of humanizers is treated as misconduct in academic contexts. A tool called `humanize` should have an opinion. Ground: §1.7.
4. **Detector-evasion vs style-improvement is not separated.** The literature is explicit that these are distinct goals with distinct ethics. Ground: §1.7.
5. **Audience/purpose specification is not a first-class input.** The plain-language literature (§1.3) and rhetorical-genre theory (§1.1) both put audience/purpose *before* rules. The repo puts rules first.
6. **`plainspoken` doesn't handle bad-news/emotional-context-first cases** that Minto's own literature calls out.
7. **`ste` doesn't gate procedures vs descriptions vs safety-critical** at the invocation layer, even though the standard treats these as genre-distinct.
8. **The `audit.py` acceptance criteria are surface metrics presented as pass/fail.** The readability-research consensus (§1.5) is that surface metrics are diagnostics, not adjudicators.

### Product gaps (missing skills)

- **A `plainlang` skill.** The repo has an aerospace-standard skill (`ste`) and a de-slop skill (`humanize`) but not a plain-language skill aligned with the Federal Plain Language Guidelines / PLAIN. This is a real genre — public-facing regulatory, benefits, health, legal-summary writing — with a distinct standard (§1.3). Ground: §1.3.
- **A `pyramid` / `brief` skill.** `plainspoken` covers chat; there is no dedicated skill for the artefact side of Minto (executive summary, one-pager, recommendation memo). Ground: §1.4.
- **An audience-brief upstream skill.** Nothing in the repo captures "who is this for, what will they do with it, in what genre" *before* choosing which style skill to invoke. Ground: §1.1, §1.3.
- **A disclosure/citation-of-AI-assistance helper.** Given the trust-and-ethics literature, this is arguably the most under-served real need. Ground: §1.7.

---

## Part 4 — Proposed extensions (prioritized)

Framed as a collaborative pitch to the maintainer. Each proposal cites its supporting finding.

### P0 — Add an audience/purpose preamble as a shared upstream

**Change:** All three skills read a shared `PURPOSE.md` header (or accept a one-line invocation like `/humanize --audience=regulators --purpose=inform`) that captures audience, purpose, genre, and disclosure posture *before* rules fire.

**Why:** Genre is reconceived as social action in response to recurrent rhetorical situations perceived as a combination of purpose, audience, and occasion. The first rule of plain language is: write for your audience. Every style rule in the repo is conditional on this input, and today the tools have to guess.

**Effort:** Low. It's a data structure and a prompt-level convention.

### P1 — Add a `plainlang` skill

**Change:** A fourth skill implementing the Federal Plain Language Guidelines (audience-first, short sentences, active voice, everyday words, bullet lists for complex material, testable outcomes).

**Why:** To comply with the Plain Writing Act, avoid jargon, redundancy, ambiguity, and complex words; write briefly and clearly; and organize writing well. Use definite, concrete, everyday language. Write in short sentences. Use active voice. Use bullet lists for complex material. This is a distinct standard from STE (STE is more strictly controlled — while plain English aims for general clarity, STE follows precise rules tailored for technical writing.) and from `humanize` (which is style/voice-focused, not audience-focused).

**Effort:** Medium. The guidelines are well-documented and public.

### P2 — Split `humanize` along the ethics/goal axis

**Change:** Two modes (or two skills):
- `humanize --improve` (default): remove tells because they mark generic, low-information prose. Never targets a detector.
- `humanize --attribution=human` (opt-in, warns on invocation): the current behavior, plus a required companion disclosure block if the user's use context is academic or journalistic.

**Why:** Institutional guidelines on AI use increasingly emphasise transparency, academic integrity, and responsible disclosure of AI assistance. So using AI content humanizers to deliberately mask AI authorship is seen as cheating and dishonest. The literature says these are ethically distinct activities. The current tool conflates them by default.

**Effort:** Low-medium. It is a framing change plus a warning message plus an optional block.

### P3 — Version the tells catalog and add a "model-generation" field

**Change:** `references/tells.md` gains a `since:` and `models:` tag per entry, and the audit prints the catalog version. Older tells (e.g. "delve") are downweighted, not deleted.

**Why:** The evidence is thin, and as models have grown more sophisticated, the telltale words have become harder to trace. The tell vocabulary is measurably different between GPT-4 (2023 to mid-2024) and GPT-4o (mid-2024 to mid-2025) eras. A tell catalog without a timestamp will start producing false positives faster than the maintainer can update it.

**Effort:** Low. Metadata change plus a script tweak.

### P4 — Reframe `audit.py` acceptance criteria as diagnostics, not pass/fail

**Change:** The CV-of-sentence-length criterion (0.4), the "no four consecutive paragraphs share the same sentence count" rule, and similar surface metrics become *diagnostics with genre-aware thresholds*, not hard pass/fail. Papers already get an override; add overrides for legal, regulatory, API-reference-docs (where uniform structure is a feature, not a bug).

**Why:** Traditional readability metrics fail to accurately measure text difficulty because they only evaluate quantifiable characteristics of word length and sentence structure. The formulas concentrate on surface-level characteristics while neglecting complex linguistic elements that affect comprehension, especially in online texts, together with technical documentation and domain-specific content. Gopen and Swan also make clear that these are "principles" not "rules." The `tells.md` "Things wrongly flagged as AI" section already contains the seed of this move — extend it to the numeric criteria.

**Effort:** Medium. Script change plus documentation.

### P5 — Add procedure/description/safety branching to `ste`

**Change:** Invocation supports `/ste procedure`, `/ste description`, `/ste warning` and applies the 20-word cap only to procedures (per Rule 5.1), the 25-word cap to descriptions (per Rule 6.3), and the safety-command-first structure to warnings (per Section 7). Default to a mixed-mode with a warning when ambiguous.

**Why:** The standard itself distinguishes these. The rules also differentiate between two types of texts: procedures and descriptions. The current SKILL.md correctly *lists* the rules but does not gate on which set is active.

**Effort:** Low. It is a routing change in one skill.

### P6 — Add a scope warning to `ste`

**Change:** When invoked on a file that isn't a procedure, technical description, or safety-critical text, print a one-line notice: "STE was designed for safety-critical maintenance documentation. Applying it to blog posts, essays, or general READMEs may strip legitimate voice. Consider `/plainlang` or `/plainspoken`."

**Why:** The STE guide was never meant to become a general writing standard. Nevertheless, it was successfully adopted by many industries. The key driver for the creation of STE was a request from the airlines to ensure accurate maintenance practices and guarantee aircraft availability and safety. Complex technical instructions can be misunderstood, and misunderstandings can lead to accidents. Users applying an aerospace safety-standard to a personal blog should at least be told.

**Effort:** Trivial.

### P7 — Add a `brief` (Minto) skill for artefacts

**Change:** A dedicated skill for one-pagers, executive summaries, recommendation memos, and consulting-style decks. Enforces answer-first, MECE grouping, and the situation-complication-question-answer (SCQA) opening pattern.

**Why:** Barbara Minto's pyramid principle is a communication method that structures ideas with the main conclusion first, followed by supporting arguments organized in logical groups to create clear, compelling business documents. This is a real genre with a real standard, and `plainspoken` currently absorbs its philosophy but scopes to chat only.

**Effort:** Medium.

### P8 — Add the bad-news / emotional-context override to `plainspoken`

**Change:** When the invocation signals bad news (layoff communication, apology, condolence, incident postmortem to affected users), `plainspoken` softens "answer first" to "acknowledge first, answer second."

**Why:** Avoid the Pyramid Principle when your audience needs to be emotionally engaged before hearing your conclusion, when you're delivering bad news that requires context first, or when you genuinely don't have a recommendation yet.

**Effort:** Low.

### P9 — Add non-native-writer defense to `humanize`

**Change:** The audit gets a `--assume-non-native` flag (and the voice profile gets a language-background field) that suppresses tells commonly produced by ESL writers rather than by models — repeated-word avoidance, formal-register carryover, certain determiner patterns.

**Why:** Studies demonstrated systematic bias against non-native English speakers, with seven detectors showing 61.3% false positive rates on TOEFL essays compared to near-zero on native English writing. This occurs because perplexity-based detection systematically penalizes simpler vocabulary and grammatical structures commonly used by English language learners. It must be noticed however that editors who are not native English speakers might prefer to avoid repeated words as well. For example Italian schools often teach to avoid repeating words. The `voice-profile.md` already has an "Overrides" section and mentions "non-native constructions" — this proposal formalizes it as a first-class flag.

**Effort:** Low.

---

## Uncertainties and limitations of this brief

1. **The `humanize` literature is the most volatile input.** Between the knowledge cutoff and the search date, the practitioner discourse on AI tells has shifted twice; treat any specific tell in `tells.md` as time-decaying.
2. **The trust literature is mixed on effect size.** Attempts at transparency are used and can be a valuable contribution to the safe and responsible use of AI, [but] their actual impact on user perceptions remains inconclusive. The disclosure recommendation in P2 is grounded in the ethics literature more than in a proven trust benefit.
3. **I did not evaluate the actual `audit.py` code**, only the SKILL.md description of what it does. Any claim about its behavior is inferred from documentation.
4. **The repo's target user is described in context as one senior data leader.** Several of my proposals (P0, P1, P2, P7) assume the repo is being pitched as a broader public writing toolkit; if the maintainer's intent is narrower, some proposals may be out of scope.
5. **The "signs of AI writing" evidence base leans on Wikipedia and practitioner blogs rather than peer-reviewed studies.** This is a limitation of the field, not of the search — the peer-reviewed literature on detector reliability and disclosure exists, but the tell-catalog itself is community-maintained.
6. **I have not independently searched the repo's commit history or the maintainer's Substack.** Per the brief, I started from the external evidence.

The strongest single move, if only one is taken, is **P0 (audience/purpose preamble)** — it is the change most consistently supported across every body of literature in Part 1, from Miller's genre theory (§1.1) through STE's audience design (§1.2) through plain language's first principle (§1.3) through Minto's "know your decision-maker" (§1.4) through Gopen & Swan's reader-expectations (§1.4) through the trust literature's audience-moderation findings (§1.7). Everything else in the repo works better once that input is explicit.