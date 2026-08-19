# Corrections — 04-normalized

## 2026-08-19 — `native_scales` understated how far the models diverged

**What it said.** The supply matrix recorded two native scales: two models on
`integer -2..2` mapped by identity, one on the five-letter `S/s/N/d/D`. The
demand matrix recorded one: `integer 0..3`, "identity — all three models
answered on the requested scale."

**What the raw responses show.** Three scales on the supply side, not two, and
only one of them integers:

| model | supply scale as emitted |
|---|---|
| `anthropic/claude-opus-4.7` | integers `+2 / +1 / 0 / −1 / −2`, with `‡` for effects asserted but unsupported |
| `x-ai/grok-4.5` | letters `S / s / N / d / D`, with `*` for the same caveat |
| `openai/gpt-5.4` | symbols `++ / + / 0 / − / −−`, mapping declared by the model itself, with `?` for a technique it declined |

`gpt-5.4`'s symbolic scale is unambiguous — the model supplied its own
conversion — but it is not the requested scale, and "identity" is not what
happened. Several of its cells are not points on any scale: `0 / −`,
`mixed / often −`, and per-skill splits such as `` `humanize` + ; `ste` − ``.
Its entire `ISO 24495-1` column is `?`.

On the demand side, `grok-4.5` returned five range-valued cells — `0–1` in
Actionability, `0–1`, `1–2`, `0–1` in Persuasive force, and `2–3*` in
Accountability — so "all three models answered on the requested scale" is not
true of that matrix either. The published integer for those cells was chosen
during analysis rather than stated by a model.

**The larger finding, which is not corrected here because it needs a decision.**
The published supply matrix has ten technique columns. Two of the three models
answered on twelve, splitting the repo skills into `ste`, `plainspoken` and
`humanize`; the third returned one bundled column. Somewhere between the raw
responses and the published matrix, twelve columns became one `repo skills`
column. No artifact records that step or which sub-column any published vote
came from.

That is the step the three unresolved two-vote cells sit in. For
`Empathy × repo skills` the corpus records votes `{−1, +1}`. In the raw
responses `opus` gives `‡ / 0 / 0` across its three skill columns, `grok` gives
`+1 / +1 / 0`, and `gpt` gives `+1` and `−1` inside a single cell. The recorded
pair is reproducible as gpt's own compound answer, or as gpt's `−1` with grok's
`+1`. Both fit, and nothing distinguishes them.

**Consequence.** The handoff that scheduled this work expected the raw responses
to settle whether the third model declined or its vote was merely unpublished.
They do not. `unrecorded_reason: "not-published"` stands, and the bound on how
many supply cells a quorum rule would change can be narrowed but not closed from
the corpus plus the raw responses alone. What is missing is not data — it is the
record of a normalization step that was performed in prose.

This is the same failure mode as dhk/alexandria#62, in a different run, and it
is the strongest available argument for generating `matrices.md` from this stage
rather than hand-writing it: a generated matrix cannot collapse columns without
declaring the rule it used.

**What changed in the artifact.** `native_scales` on both matrices, and
`coverage_note`. No cell value and no vote was altered.
