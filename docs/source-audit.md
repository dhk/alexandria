# Source audit

**Status:** Normative
**Depends on:** [`schemas/source-audit.schema.json`](../schemas/source-audit.schema.json),
[Confidence calibration](confidence-calibration.md)

---

## 1. The gap this closes

A claim score records that a model *stated* something, and quotes the span it
stated it in. That is a fact about the model. Nothing anywhere in a run
establishes that a cited source says what the run says it says.

Every investigation in the corpus notes this in prose — "no human has opened
them" — and then carries on citing the claims. The source audit is the artifact
that closes it, and `assurance_level: gold` now requires one.

## 2. Two verdicts, because two things fail separately

Each entry carries **`citation_accuracy`** and **`claim_support`**, and they are
independent:

- **Citation accuracy** — does the work exist as cited? Title, venue, year,
  volume, pages.
- **Claim support** — does the work actually say what the investigation claims
  from it? `supports`, `partially-supports`, `contradicts`, `absent`,
  `unresolved`, or `unchecked`.

A real paper, cited perfectly, can still fail to support the claim drawn from
it. That second failure is the one worth auditing for, and it is invisible to
anyone checking bibliographies.

## 3. Only reading the source settles what it argues

Every verdict records a `method`: `primary-source`, `search-metadata`, or
`secondary`. Validation enforces one rule about it:

> A substantive `claim_support` verdict requires `method: primary-source`.

A catalogue record, a database entry, or a search summary establishes that a
work exists. It never establishes what the work argues. Accepting the second as
the first would rebuild the Silver gap inside the artifact built to close it —
substituting one unread layer for another and calling it verification.

`search-metadata` remains fully sufficient for `citation_accuracy`, which is
exactly the kind of question a catalogue answers.

## 4. Gold is checkable now

`scripts/validate.py` fails any investigation marked `gold` that has no
`05-analysis/source-audit.json`, or whose audit still holds `unchecked` claim
support. Assurance stops being a word typed into `topic.yaml` and becomes a
property the repository can demonstrate.

Silver is unaffected. An investigation may sit at Silver indefinitely with no
audit at all, which is the honest state for most of the corpus today.

## 5. Coverage today

`2026-08-13-is-ste100-the-right-tool` has the first audit file, and it is a
**worklist, not an audit**. Two entries have confirmed citation accuracy from
catalogue metadata — Hotaling 2020 and Kuhn 2014, both matching their citations
exactly. Every `claim_support` verdict is `unchecked`.

The session that started it had no outbound network beyond server-side search:
every publisher, index, DOI resolver and reference host tested was unreachable
under the environment's egress policy. Bibliographic facts were confirmable;
no source could be opened. Under §3 that permits no support verdict at all, so
the investigation stays Silver.

Two entries are flagged for whoever finishes it:

- **`kuhn-2014`** carries a load-bearing empirical claim — that the survey
  summarises studies finding Simplified English improves maintenance-procedure
  comprehension. Kuhn 2014 is a classification survey of controlled natural
  languages, and whether it carries outcome studies at all is precisely what
  the paper must be opened to settle.
- **`stemg-training`** is quoted as the standard body's own refutation of the
  general-writing claim, and the published quotation may be a compression of
  two separate sentences rather than a verbatim one. A compressed quotation
  presented as verbatim is a different defect from a wrong one, and harder to
  notice.
