# Is ASD-STE100 the right tool for clear, concise, persuasive writing?

**Question.** ASD-STE100 (Simplified Technical English) is circulating as a
general standard for good writing. Test the claim rather than assume it:
establish what STE was built for and by whom, what the evidence says it does
well and badly, how it compares with the other techniques and tools people
actually use, and how a writer should choose between them.

**Material examined.** The claim stated verbatim, plus the whole of
`github.com/nonatofabio/claude-writing-skills` (7 files) — its `ste`,
`plainspoken` and `humanize` skills and their reference material. Two further
artifacts named in the brief for the models to retrieve: the Hemingway Editor,
and Hotaling, S. (2020), *Simple rules for concise scientific writing*,
Limnology & Oceanography Letters 5:379–383.

**Answered by** `openai/gpt-5.4` · `anthropic/claude-opus-4.7` ·
`x-ai/grok-4.5`. **Graded by** `anthropic/claude-sonnet-4.6`.
**Web search** on — the models read live sources, so this run is not
reproducible from its inputs.
**Run** `r-2026-0813-02`, 2026-08-13, $2.16, 34 claims.

## The verdict

All three models reject the claim, for the same reason: STE removes by design
the devices persuasion depends on — varied rhythm, synonymy, figurative
language, voice, narrative. Virtues in a maintenance procedure read under
operational pressure by a second-language technician; liabilities in anything
meant to change a mind.

STEMG says so itself. Its own training material states that **STE is not a
simplified version of English for the writers, only for the readers** — the
cleanest refutation of the general-writing-standard claim available, in the
standard body's own words.

On **why the enthusiasm exists now**: STE is popular in AI and writing-tool
circles because it is *machine-operable* — rule-based, checkable, legible to a
tool — not for any reason connected to what it was built for.

## The finding that generalises

All three independently identified one assumption shared by the Hemingway
Editor, STE, Hotaling's rules, and the Claude skills: **that surface features
proxy quality, and that shorter is generally better.** All three reached the
same verdict — valid as a *diagnostic*, invalid as an *optimization target* —
and all three reached for Goodhart's Law unprompted.

Two consequences worth carrying:

- The `humanize` skill's AI-tell catalogue traces to community-maintained
  sources (Wikipedia's *Signs of AI writing*). It is practitioner folklore,
  not validated research, and should be labelled as such.
- Hemingway's own materials concede that grade level does not define the
  target audience, while its interface trains users to lower the number.

## Provenance, settled — and a correction

The earlier run answered this from recall and its models contradicted each
other. This run answered it from sources, and **retracted one of the earlier
claims**: all three could find no authoritative source for Douglas /
McDonnell Douglas involvement in STE's founding, and all three declined to
assert it.

| | |
|---|---|
| Late 1970s | AECMA originates STE, with AIA collaboration |
| 1983 | SEWG formally constituted, at a meeting associated with Fokker in Amsterdam |
| 1985 / 1986 | Issue 0 pre-release; first public guide as PSC-85-16598. Sources conflict; the ambiguity is real and is not flattened here |
| 2004 | Rename to ASD; maintenance passes to STEMG |
| 2005 | First issue under the ASD-STE100 title |
| 2006, 2018 | EU Trade Mark granted |
| 15 Jan 2025 | Issue 9 — current; 53 rules, ~900 approved words |
| Jan 2028 | Issue 10 scheduled |

Issue 9 grants **irrevocable, free-of-charge usage rights** to specific
categories including ASD and AIA members and universities — directly material
to whether a tool may ship the approved-word dictionary.

## Read order

1. [`01-brief/brief.md`](01-brief/brief.md) — the commission, verbatim.
2. [`05-analysis/analysis.md`](05-analysis/analysis.md) — where the three
   outputs converge and diverge, and what the run does not establish.
3. [`05-analysis/scores.csv`](05-analysis/scores.csv) — 34 claims scored
   against every model, with the quote each score rests on.
4. [`03-runs/r-2026-0813-01/`](03-runs/r-2026-0813-01/) — the superseded run,
   kept in full. The correction is only legible next to what it corrected.

## How far to trust it

**Silver: three lineages, claims scored, quotes attached, no source audit.**
The citations here are far better than the earlier run's — specific editions,
dates, and documents — but *no human has opened them*. That check is what
would make this Gold, and it is now cheap: the claims are specific enough to
verify one by one.

**The landscape records zero disagreements** (27 consensus, 7 novel) while the
analysis prose describes several real divergences — 1985 vs 1986, the ATA
requirement date, whether Hemingway uses ARI or Flesch–Kincaid, and a
three-way split on how far to trust Chiarello (2013) for the Fokker
attribution. Those are disagreements about *sourcing confidence*, and the
claim classifier only registers disagreement when score signs oppose. Read the
analysis, not the group counts.

**Where sources could not settle it**, the run says so rather than choosing:
the 1985/1986 release ambiguity and the Fokker attribution both remain open,
the latter resting on a STEMG-affiliated practitioner history that one model
could not access at all.
