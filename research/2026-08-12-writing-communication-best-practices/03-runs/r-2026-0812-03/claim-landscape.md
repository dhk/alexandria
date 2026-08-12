# Claim landscape

37 claims extracted from the three research outputs by
`anthropic/claude-sonnet-4.6`, each scored against every model.

Model index, verified by matching each score's quote back to the
output it was taken from (each index's quotes appear in exactly one
model's text):

| Index | Model |
|---|---|
| 1 | `openai/gpt-5.4` |
| 2 | `anthropic/claude-opus-4.7` |
| 3 | `x-ai/grok-4.5` |

Score scale, from [`docs/confidence-calibration.md`](../../../../docs/confidence-calibration.md) §4 —
a (stance, strength) pair maps to a signed integer:

| | Strong | Moderate | Weak |
|---|---|---|---|
| Supports | `+3` | `+2` | `+1` |
| Silent | — | — | `0` |
| Disputes | `-3` | `-2` | `-1` |

Two caveats on reading these numbers. The spec has the grader emit the
categorical pair and derive the integer by fixed lookup, precisely
because direct numeric self-rating from a model is badly calibrated;
the implemented prompt asks for the integer directly, so these are
model-assigned numbers, not derived ones. And a score records what a
model *stated*, not whether the cited source bears it out — no source
audit has been done.

A claim supported by one model and disputed by another is a real
disagreement, not a formatting artifact — those rows are worth reading
first.

## 1. ASD-STE100 Issue 9 was published in January 2025.

- **`openai/gpt-5.4`** — `+2` (supports, moderate)
  > The official STE site states that the current version is **Issue 9, January 15, 2025**
- **`anthropic/claude-opus-4.7`** — `+2` (supports, moderate)
  > The current edition, published in January 2025, consists of 53 writing rules and a dictionary of approximately 900 approved words.
- **`x-ai/grok-4.5`** — `+2` (supports, moderate)
  > Issue 9 (January 2025) comprises ~53 writing rules plus a dictionary of ~900 approved words

## 2. ASD-STE100 was originally developed for aircraft maintenance documentation to serve non-native English-speaking airlines.

- **`openai/gpt-5.4`** — `+2` (supports, moderate)
  > ASD-STE100 is a controlled language standard originally developed for maintenance documentation
- **`anthropic/claude-opus-4.7`** — `+3` (supports, strong)
  > originally developed in the 1980s by the European Association of Aerospace Industries (AECMA) at the request of the European Airline industry, which wanted a standardized form of English for aircraft maintenance documentation that could be easily understood by non-native English-speakers
- **`x-ai/grok-4.5`** — `+2` (supports, moderate)
  > STE is optimized for **procedures and safety-critical description**, not for persuasive essays, literary voice, or open scientific argumentation

## 3. STE's official maintainers state that no software tool can guarantee full STE compliance because only human writers can judge whether a sentence makes good sense.

- **`openai/gpt-5.4`** — `+2` (supports, moderate)
  > The official STE site warns that software tools can support checking but do not themselves 'write STE' or reliably convert arbitrary prose into compliant STE.
- **`anthropic/claude-opus-4.7`** — `+3` (supports, strong)
  > No language checker can guarantee full compliance with STE, because the goal of STE is clarity — only human writers can judge whether a sentence or paragraph makes good sense.
- **`x-ai/grok-4.5`** — `+0` (silent — no bearing statement)

## 4. STE was never intended to become a general writing standard, though it has been adopted beyond aerospace.

- **`openai/gpt-5.4`** — `+2` (supports, moderate)
  > controlled language is highly useful in: maintenance procedures, safety notices, operational instructions… But it is a weaker fit for: exploratory essays, persuasive blog posts, nuanced argument
- **`anthropic/claude-opus-4.7`** — `+3` (supports, strong)
  > The STE guide was never meant to become a general writing standard; nevertheless, it was successfully adopted by many industries.
- **`x-ai/grok-4.5`** — `+2` (supports, moderate)
  > Official guidance stresses STE is **not a standalone style guide**—it must sit with domain specs and professional judgment. Over-application outside maintenance/procedure genres is a known misapplication risk.

## 5. Caterpillar Fundamental English was discontinued in 1982 partly because its guidelines were not enforceable in practice.

- **`openai/gpt-5.4`** — `+0` (silent — no bearing statement)
- **`anthropic/claude-opus-4.7`** — `+3` (supports, strong)
  > CFE was discontinued by Caterpillar in 1982 because (among other reasons) the basic guidelines of CFE were not enforceable in the English documents produced.
- **`x-ai/grok-4.5`** — `+0` (silent — no bearing statement)

## 6. The U.S. Plain Writing Act of 2010 requires federal agencies to use clear language that the public can understand.

- **`openai/gpt-5.4`** — `+1` (supports, weak)
  > The Federal Plain Language Guidelines define the outcome in user terms: readers should be able to find, understand, and use what they need.
- **`anthropic/claude-opus-4.7`** — `+3` (supports, strong)
  > the broadest, clearest, and most well-known plain language law is the Plain Writing Act of 2010, signed into law on October 13, 2010. It aims to make government information easier for people to access and understand, and requires federal agencies to use clear language that the public can understand.
- **`x-ai/grok-4.5`** — `+2` (supports, moderate)
  > U.S. Federal Plain Language Guidelines (implementing the Plain Writing Act of 2010)

## 7. ISO 24495-1:2023 defines four plain-language principles: content is relevant, findable, understandable, and usable for the intended reader.

- **`openai/gpt-5.4`** — `+0` (silent — no bearing statement)
- **`anthropic/claude-opus-4.7`** — `+0` (silent — no bearing statement)
- **`x-ai/grok-4.5`** — `+3` (supports, strong)
  > **ISO 24495-1:2023** frames four governing principles: content is **relevant**, **findable**, **understandable**, and **usable** for the intended reader.

## 8. Plain language is not about dumbing down content but about using language the intended audience understands.

- **`openai/gpt-5.4`** — `+2` (supports, moderate)
  > Plain-language guidance generally advises replacing jargon when everyday words preserve the same meaning, not eliminating precision.
- **`anthropic/claude-opus-4.7`** — `+3` (supports, strong)
  > One of the most common plain language myths is that you have to 'dumb down' your content so that everyone can read it. That's not true. Use language your audience understands and feels comfortable with.
- **`x-ai/grok-4.5`** — `+2` (supports, moderate)
  > "Plain" is audience-relative. A term that is plain to a senior engineer is jargon to a citizen.

## 9. Gopen and Swan's reader-expectation principles hold that readers interpret prose more easily when information is placed where they expect it, with old information in the topic position and new/important information in the stress position.

- **`openai/gpt-5.4`** — `+2` (supports, moderate)
  > Gopen and Swan argue that clarity depends heavily on placing information where readers expect it, especially using sentence openings to orient readers and sentence endings to carry emphasis.
- **`anthropic/claude-opus-4.7`** — `+3` (supports, strong)
  > Put in the topic position the old information that links backward; put in the stress position the new information you want the reader to emphasize.
- **`x-ai/grok-4.5`** — `+2` (supports, moderate)
  > Gopen–Swan flow, evidence-calibrated hedges, genre structure

## 10. Gopen and Swan explicitly frame their guidance as principles, not rules.

- **`openai/gpt-5.4`** — `+0` (silent — no bearing statement)
- **`anthropic/claude-opus-4.7`** — `+3` (supports, strong)
  > Gopen and Swan also make clear that these are 'principles' not 'rules.'
- **`x-ai/grok-4.5`** — `+0` (silent — no bearing statement)

## 11. Barbara Minto's Pyramid Principle is not universally applicable and should be avoided when the audience needs emotional engagement before the conclusion, when delivering bad news requiring context first, or when no recommendation yet exists.

- **`openai/gpt-5.4`** — `+1` (supports, weak)
  > the Pyramid Principle and related business-writing advice support leading with the answer, especially for decision-making contexts
- **`anthropic/claude-opus-4.7`** — `+3` (supports, strong)
  > avoid the Pyramid Principle when your audience needs to be emotionally engaged before hearing your conclusion, when you're delivering bad news that requires context first, or when you genuinely don't have a recommendation yet.
- **`x-ai/grok-4.5`** — `+1` (supports, weak)
  > Pyramid answer-first, decide-don't-survey, owned voice

## 12. Traditional readability formulas such as Flesch-Kincaid rely on surface characteristics like sentence length and syllable count while ignoring deeper linguistic factors that affect comprehension.

- **`openai/gpt-5.4`** — `+2` (supports, moderate)
  > Traditional readability formulas focus on surface proxies such as word and sentence length. Those proxies can correlate with reading difficulty, but they are incomplete.
- **`anthropic/claude-opus-4.7`** — `+3` (supports, strong)
  > The Flesch-Kincaid readability assessment tool along with other traditional metrics remains widely used to measure text complexity yet fails to accurately measure text difficulty because it only evaluates quantifiable characteristics of word length and sentence structure
- **`x-ai/grok-4.5`** — `+2` (supports, moderate)
  > Formulas ignore content difficulty, prior knowledge, layout, cohesion, and retrieval aids.

## 13. AI text detectors show unstable and declining accuracy, with paraphrasing or light editing sharply degrading detector performance.

- **`openai/gpt-5.4`** — `+2` (supports, moderate)
  > detectors trained on earlier outputs perform worse on newer, more sophisticated models, and that data diversity and model evolution remain major challenges
- **`anthropic/claude-opus-4.7`** — `+2` (supports, moderate)
  > Perkins et al. evaluated six major detectors and found their average accuracy (already a modest 39.5%) dropped to 17.4% when faced with texts lightly modified to evade detection.
- **`x-ai/grok-4.5`** — `+2` (supports, moderate)
  > Paraphrasing and light editing sharply degrade detector accuracy (e.g., DIPPER paraphrases collapsing DetectGPT-style performance while preserving semantics). OpenAI retired its own classifier citing low accuracy.

## 14. AI text detectors show systematic bias against non-native English speakers, with false positive rates as high as 61.3% on TOEFL essays compared to near-zero on native English writing.

- **`openai/gpt-5.4`** — `+0` (silent — no bearing statement)
- **`anthropic/claude-opus-4.7`** — `+3` (supports, strong)
  > Studies also demonstrated systematic bias against non-native English speakers, with seven detectors showing 61.3% false positive rates on TOEFL essays compared to near-zero on native English writing.
- **`x-ai/grok-4.5`** — `+2` (supports, moderate)
  > false positives have harmed non-native writers in academic settings

## 15. Vanderbilt University disabled Turnitin's AI detection feature, noting that even a 1% false positive rate applied to 75,000 papers would yield approximately 750 wrongful accusations annually.

- **`openai/gpt-5.4`** — `+0` (silent — no bearing statement)
- **`anthropic/claude-opus-4.7`** — `+3` (supports, strong)
  > Vanderbilt University disabled Turnitin's AI detection in August 2023, noting that even 1% false positives applied to 75,000 papers yields ~750 wrongful accusations annually.
- **`x-ai/grok-4.5`** — `+0` (silent — no bearing statement)

## 16. Disclosing AI use can reduce reader trust in the human author even when text quality is unchanged, a phenomenon described as a 'transparency penalty.'

- **`openai/gpt-5.4`** — `+2` (supports, moderate)
  > disclosure may also lower perceived quality or authenticity in some evaluative settings
- **`anthropic/claude-opus-4.7`** — `+3` (supports, strong)
  > Several studies show that when readers learn AI contributed to a text, their trust in the human author declines even if the quality of the text is unchanged. This 'transparency penalty' challenges the conventional assumption that openness builds trust.
- **`x-ai/grok-4.5`** — `+2` (supports, moderate)
  > Multiple experiments find **disclosing AI use can reduce trust** in the actor ('transparency dilemma').

## 17. The trust penalty from AI disclosure is moderated by individual differences, with AI-literate individuals showing a smaller decline in trust upon disclosure.

- **`openai/gpt-5.4`** — `+0` (silent — no bearing statement)
- **`anthropic/claude-opus-4.7`** — `+3` (supports, strong)
  > People with more positive attitudes toward AI show a smaller decline in trust upon disclosure. A user's AI literacy plays a significant role in shaping their perceptions — AI-literate individuals tend to view its use as pragmatic, whereas less knowledgeable readers may interpret it as a sign of incompetence or laziness.
- **`x-ai/grok-4.5`** — `+0` (silent — no bearing statement)

## 18. Readers generally perceive AI disclosure as more necessary than writers do, and view it as more necessary when AI's contribution is direct, irreplaceable, or not intentionally steered by the writer.

- **`openai/gpt-5.4`** — `+2` (supports, moderate)
  > a recent vignette study found readers often see disclosure as more necessary than writers do, and view disclosure as more necessary when AI's contribution is direct, irreplaceable, or not intentionally steered by the writer
- **`anthropic/claude-opus-4.7`** — `+0` (silent — no bearing statement)
- **`x-ai/grok-4.5`** — `+2` (supports, moderate)
  > Readers often want disclosure more than writers do; necessity judgments depend on how central/irreplaceable AI contribution was.

## 19. Using AI humanizers to deliberately mask AI authorship is considered academic misconduct in scholarly contexts.

- **`openai/gpt-5.4`** — `+2` (supports, moderate)
  > nondisclosure can require corrective action and may amount to misconduct in some cases
- **`anthropic/claude-opus-4.7`** — `+3` (supports, strong)
  > using AI content humanizers to deliberately mask AI authorship is seen as cheating and dishonest, even if it helps you pass initial AI detection checks
- **`x-ai/grok-4.5`** — `+2` (supports, moderate)
  > Integrity risk: tools that maximize 'undetectable' output facilitate undisclosed AI use in academic/professional contexts where disclosure or human authorship is required.

## 20. AI vocabulary tells are model-generation-specific and shift with each major model release, making static tell catalogs time-decaying.

- **`openai/gpt-5.4`** — `+2` (supports, moderate)
  > advice based on a fixed list of 'AI tells' is, at best, heuristic. It may catch stereotyped generated prose, but it cannot be treated as robust detection science.
- **`anthropic/claude-opus-4.7`** — `+3` (supports, strong)
  > 2023 to mid-2024 (GPT-4): Additionally, boasts, bolstered, crucial, delve… Mid-2024 to mid-2025 (GPT-4o): align with, bolstered, crucial… The signs of AI use vary between models and are constantly changing over time.
- **`x-ai/grok-4.5`** — `+2` (supports, moderate)
  > These are **probabilistic style markers**, not proof.

## 21. Human language is converging with AI language as LLMs influence human speech and writing, making AI tells harder to distinguish.

- **`openai/gpt-5.4`** — `+0` (silent — no bearing statement)
- **`anthropic/claude-opus-4.7`** — `+3` (supports, strong)
  > Human speech and writing is being influenced by LLMs, and thus they are becoming more similar. This was already evident in 2024, as shown by a study that detected a significant LLM influence in spoken content (e.g. conversational podcasts).
- **`x-ai/grok-4.5`** — `+0` (silent — no bearing statement)

## 22. ICMJE requires authors, editors, publishers, and reviewers to be transparent about AI use, and states that nondisclosure can require corrective action and may constitute misconduct.

- **`openai/gpt-5.4`** — `+3` (supports, strong)
  > ICMJE now says authors, editors, publishers, and reviewers should be transparent about AI use, including which tool was used and for what purpose. It also indicates that nondisclosure can require corrective action and may amount to misconduct in some cases.
- **`anthropic/claude-opus-4.7`** — `+0` (silent — no bearing statement)
- **`x-ai/grok-4.5`** — `+1` (supports, weak)
  > Scholarly norms increasingly push disclosure of material AI assistance; undisclosed use risks retraction and reputational harm.

## 23. The academic community should shift focus from AI detection to transparency and ethical guidelines, because detection-based approaches have fundamental limitations.

- **`openai/gpt-5.4`** — `+1` (supports, weak)
  > Detection remains unstable and model-contingent, while disclosure norms are strengthening
- **`anthropic/claude-opus-4.7`** — `+3` (supports, strong)
  > we aim to demonstrate why the academic community should shift focus from detection to transparency and ethical guidelines
- **`x-ai/grok-4.5`** — `+2` (supports, moderate)
  > Cat-and-mouse: humanizers exist largely to evade detectors; detection and evasion co-evolve and neither is reliable.

## 24. The repo's `humanize` skill correctly imports Gopen and Swan's stress-position and topic-position principles for its scientific-paper override.

- **`openai/gpt-5.4`** — `+2` (supports, moderate)
  > The scientific-paper override is notably better than the generic mode. It correctly protects calibrated hedging, related-work balance, technical vocabulary, and conventional structure. It also imports Gopen & Swan in a way that is more evidence-based than the rest of the repo.
- **`anthropic/claude-opus-4.7`** — `+3` (supports, strong)
  > invokes Gopen & Swan by name for the scientific-paper override section (stress position, topic position, old-to-new flow, subject-verb proximity)
- **`x-ai/grok-4.5`** — `+2` (supports, moderate)
  > Academic overrides (calibrated hedges, IMRaD, passive-as-tool, Gopen–Swan positive moves, don't flag precise technical vocabulary) are unusually well aligned with scientific writing research.

## 25. The repo's `humanize` skill frames its goal as making drafts appear to have been written by a person, which risks conflating quality editing with concealment of AI authorship.

- **`openai/gpt-5.4`** — `-2` (disputes, moderate)
  > The description says 'rewrite drafts so a person appears to have written them.' That frames the task as **appearance management**, not clarity or audience fit.
- **`anthropic/claude-opus-4.7`** — `-2` (disputes, moderate)
  > The skill's job description ('Rewrite drafts so a person appears to have written them') is ambiguous between two goals — improving prose whose *tells* are the problem, and making AI-written prose harder to attribute.
- **`x-ai/grok-4.5`** — `-2` (disputes, moderate)
  > **Primary framing ('so a person appears to have written them')** sits on the detectability/evasion axis.

## 26. The repo lacks a dedicated plain-language document skill aligned with Federal or ISO plain-language standards.

- **`openai/gpt-5.4`** — `-2` (disputes, moderate)
  > There is no middle mode for public-facing docs, health-style explainers, product docs for mixed audiences, or executive summaries.
- **`anthropic/claude-opus-4.7`** — `-2` (disputes, moderate)
  > A `plainlang` skill. The repo has an aerospace-standard skill (`ste`) and a de-slop skill (`humanize`) but not a plain-language skill aligned with the Federal Plain Language Guidelines / PLAIN.
- **`x-ai/grok-4.5`** — `-2` (disputes, moderate)
  > **Plain-language-as-document-standard is missing** as a first-class skill; plainspoken ≠ Federal/ISO plain language for public docs.

## 27. The repo lacks an audience/purpose analysis step before applying style rules, which is the first principle in plain-language and rhetorical-genre guidance.

- **`openai/gpt-5.4`** — `-2` (disputes, moderate)
  > The literature starts with audience/task analysis; the repo starts with stylistic transformation. That is backwards from the strongest evidence.
- **`anthropic/claude-opus-4.7`** — `-2` (disputes, moderate)
  > Audience/purpose specification is not a first-class input. The plain-language literature (§1.3) and rhetorical-genre theory (§1.1) both put audience/purpose *before* rules. The repo puts rules first.
- **`x-ai/grok-4.5`** — `-2` (disputes, moderate)
  > **Audience model is implicit**, not operationalized (no lightweight audience/purpose/risk preamble before applying rules).

## 28. The repo's `ste` skill ships an approved-verb list but not the full ~900-word STE dictionary, limiting its claim to full STE compliance.

- **`openai/gpt-5.4`** — `-1` (disputes, weak)
  > The README claims it 'compresses the full standard' into one skill. But the official STE site says no tool can simply write STE for you or reliably convert arbitrary prose into STE
- **`anthropic/claude-opus-4.7`** — `-2` (disputes, moderate)
  > The skill correctly identifies the standard… but the skill inherits a scope confusion that the standard's own maintainers warn against.
- **`x-ai/grok-4.5`** — `-2` (disputes, moderate)
  > **STE dictionary gap** (verbs ≠ full dictionary) limits claim of full STE compliance.

## 29. The repo contains no disclosure or provenance support for contexts where AI-use transparency is required.

- **`openai/gpt-5.4`** — `-2` (disputes, moderate)
  > There is no skill for drafting AI-use disclosures, diligence statements, or provenance notes for scholarly or professional contexts.
- **`anthropic/claude-opus-4.7`** — `-2` (disputes, moderate)
  > The disclosure/ethics dimension is absent.
- **`x-ai/grok-4.5`** — `-2` (disputes, moderate)
  > **Disclosure / provenance / appropriate-use policy** absent despite material trust literature.

## 30. The `humanize` skill's sentence-length coefficient-of-variation threshold of 0.4 is a house heuristic, not a validated writing standard from the academic literature.

- **`openai/gpt-5.4`** — `-2` (disputes, moderate)
  > The requirement that sentence-length coefficient of variation exceed 0.4, and that a piece must take at least one arguable position, are house heuristics, not established writing standards.
- **`anthropic/claude-opus-4.7`** — `-1` (disputes, weak)
  > Criterion 3 ('Sentence-length coefficient of variation is above 0.4…') is a defensible operationalization of the practitioner claim that uniform sentence length is one of the strongest signs of AI writing in any text. But it inherits the readability-formula critique from §1.5: it is a surface metric
- **`x-ai/grok-4.5`** — `-2` (disputes, moderate)
  > **Cadence CV > 0.4** is a reasonable anti-metronome heuristic but **not** a validated readability or 'humanness' standard in the academic literature; risk of cargo-cult variation.

## 31. The repo's `ste` skill applies STE to READMEs and reports without warning users that the standard was designed for safety-critical maintenance documentation, not general software documentation.

- **`openai/gpt-5.4`** — `-1` (disputes, weak)
  > It overextends STE to genres where controlled language is not clearly best. The README scopes `ste` to docs, procedures, READMEs, reports, UI text. Some of those fit better than others.
- **`anthropic/claude-opus-4.7`** — `-2` (disputes, moderate)
  > The repo's framing does not warn the user that they are applying an aerospace-safety controlled language to a blog-adjacent artefact, which will strip legitimate voice from a README that has no safety exposure.
- **`x-ai/grok-4.5`** — `-1` (disputes, weak)
  > Persistence default ON when unsure is operationally aggressive; STE misapplied to persuasive or narrative chat can harm register fit

## 32. The `plainspoken` skill's scope note limiting it to chat prose rather than deliverables is a sound design choice that acknowledges genre differences.

- **`openai/gpt-5.4`** — `+2` (supports, moderate)
  > Its scope note—'chat prose, not deliverables'—is one of the repo's best design choices because it acknowledges genre differences.
- **`anthropic/claude-opus-4.7`** — `+2` (supports, moderate)
  > `plainspoken` SKILL.md acknowledges 'if the honest answer is "it depends"' and 'if you don't know,' but does not address the two harder cases: emotional-context-first and bad-news delivery.
- **`x-ai/grok-4.5`** — `+1` (supports, weak)
  > Excellent for assistant chat. Not a document plain-language skill

## 33. The `humanize` skill's voice-profile mechanism, which calibrates to a real author's documented habits rather than a generic human style, is a stronger design choice than generic humanization.

- **`openai/gpt-5.4`** — `+2` (supports, moderate)
  > The voice-profile mechanism is also a serious design choice: it shifts the goal from 'generic human' to 'this author's documented habits,' which is more honest and produces better stylistic fit.
- **`anthropic/claude-opus-4.7`** — `+2` (supports, moderate)
  > Voice-profile design in `humanize`. Requiring three-to-five unedited samples and letting the profile override generic rules is well-aligned with plain-language theory's 'write for your audience'
- **`x-ai/grok-4.5`** — `+2` (supports, moderate)
  > Voice-profile calibration outranking generic rules—addresses 'generic human' failure mode.

## 34. A plain-language randomized trial found that plain-language versions improved adults' understanding of health recommendations.

- **`openai/gpt-5.4`** — `+2` (supports, moderate)
  > A randomized trial found that plain-language versions improved adults' understanding of health recommendations.
- **`anthropic/claude-opus-4.7`** — `+0` (silent — no bearing statement)
- **`x-ai/grok-4.5`** — `+0` (silent — no bearing statement)

## 35. The `humanize` skill's anti-overcorrection warning against staccato fragments, forced slang, and fake typos reflects sound editorial practice.

- **`openai/gpt-5.4`** — `+1` (supports, weak)
  > The repo's own warning not to introduce errors intentionally
- **`anthropic/claude-opus-4.7`** — `+2` (supports, moderate)
  > explicitly warns against overcorrection ('Aggressive de-slopping has its own tells')
- **`x-ai/grok-4.5`** — `+2` (supports, moderate)
  > **Anti-overcorrection** section shows editorial maturity beyond typical 'humanizer' products.

## 36. The `ste` skill does not gate its procedure, description, and safety-critical rules at the invocation layer, even though the STE standard treats these as genre-distinct with different sentence-length caps.

- **`openai/gpt-5.4`** — `-1` (disputes, weak)
  > It risks confusing 'clarity' with 'compliance.' Sentence caps and verb restrictions are legitimate within STE, but not a general readability science.
- **`anthropic/claude-opus-4.7`** — `-2` (disputes, moderate)
  > `ste` doesn't gate procedures vs descriptions vs safety-critical at the invocation layer, even though the standard treats these as genre-distinct.
- **`x-ai/grok-4.5`** — `-2` (disputes, moderate)
  > No built-in usability-test reminder (plain-language literature's closing loop).

## 37. Rhetorical genre theory holds that genre should be understood as social action in response to recurrent rhetorical situations defined by purpose, audience, and occasion.

- **`openai/gpt-5.4`** — `+0` (silent — no bearing statement)
- **`anthropic/claude-opus-4.7`** — `+3` (supports, strong)
  > A rhetorical approach to genre should focus not on form or content but on recurrent rhetorical action. Genre is reconceived as social action in response to recurrent rhetorical situations perceived as a combination of purpose, audience, and occasion.
- **`x-ai/grok-4.5`** — `+0` (silent — no bearing statement)
