# Research brief: Supersimple Custom Apps vs. the agent/BI dashboard landscape

Revision: 1 (2026-07-29). Checksum of this revision is recorded in
[`../03-runs/claude-2026-07-29/run-metadata.yaml`](../03-runs/claude-2026-07-29/run-metadata.yaml).

## Background

Supersimple, an AI-native BI/dashboard product, is preparing to launch
"Custom Apps": a way to embed custom code, components, and visualizations
into the Supersimple environment, share them company-wide, wire them into
the same variables/filters as native charts, and — the differentiating
claim — let them both read from Supersimple's governed, permissioned data
models **and** write to (take action in) external back-end systems, under
admin-controlled connection and access permissions. The product team
frames this partly as a response to "shadow AI-coding": individual
employees already using tools like Claude Code to build one-off local
reports and mini-apps, ungoverned and unshared.

Full source material: [`../00-topic/source-material.md`](../00-topic/source-material.md).

## Scope

In scope: how "bring custom code/apps into a governed BI platform" is
solved today by comparable products, and what specifically differs about
Supersimple's framing (integration depth, write-back/action capability,
governance model, and the shadow-IT positioning).

Out of scope: Supersimple's pricing, go-to-market, or non-Custom-Apps
product surface; a security audit of any vendor's implementation;
anything requiring access to Supersimple's actual product (this is a
pre-launch transcript, not a hands-on review).

## Comparison set

The operator named a comparison set that a speech-to-text transcript
garbled ("hex on the light – space – Tableau, meta base and Sigma"). It
is read as **Hex, Lightdash, Tableau, Metabase, Sigma** — the five most
plausible product names given context (all are BI/analytics tools; all
five appear as a natural single breath-group).

Two adjacent tools are added because the transcript's own claims point at
them more directly than at some of the named five:

- **Looker (Extension Framework)** — the closest structural analog: build
  React apps that run inside Looker, hit Looker's governed semantic layer
  (LookML) *and* arbitrary external APIs, distributed and permissioned
  through Looker's platform. Any brief that skips this understates how
  differentiated Supersimple's pitch actually is.
- **Retool** (with Superblocks noted as a peer) — not a BI tool, but the
  named target of the "take action in your core systems" and "internal
  tools onto one governed platform" framing. If Supersimple's real
  competitive threat is teams building bespoke internal tools elsewhere,
  Retool-class tools are the elsewhere.

A source may flag additional relevant tools not in this set (e.g. Mode,
Domo, Superset/Preset, ThoughtSpot Everywhere) in its findings' "Open
gaps" section rather than silently ignoring them.

## Research questions

Each question traces to a specific line in the source transcript or
product notes (quoted inline).

### Q1 — Custom code/component embedding
"Bring any kind of custom logic, components or visualizations... with
rich interactions, animations." Does each comparison tool let a user
embed arbitrary custom code (not just configure a chart type) into the
BI surface? What language/runtime, and what's the distribution unit (a
cell, a plugin, a standalone app)?

### Q2 — Ecosystem integration depth
"These aren't isolated little apps... fully integrated with the rest of
your ecosystem" — specifically, a shared date-range variable applies to
both native charts and the embedded custom app simultaneously. Which
tools let a custom/embedded component subscribe to the same
filter/parameter state as native visualizations, versus treating it as a
sandboxed iframe with its own state?

### Q3 — Read vs. write: taking action in core systems
"Tools where you don't just read data but you can even take action in
your core systems." Which tools support write-back or side-effecting
actions from an embedded app/extension (not just read-only
visualization), and against what kinds of backends (the tool's own
semantic layer vs. arbitrary external systems)?

### Q4 — Dual data access: governed model + external backends
"Custom apps can access data through Supersimple's governed and
permissioned data models, but they can also connect to other external
back-end systems." Does each tool allow a single embedded
app/extension to combine (a) the platform's own governed semantic layer
and (b) arbitrary external API/backend calls, or does it confine
extensions to one or the other?

### Q5 — Governance and permissioning of connections
"As admins, you have full control over what can connect to what and who
can access what." What admin-side controls exist over which
extensions/apps may reach which backends, and who may install, publish,
or view them? Row/column-level permission inheritance vs. a separate
permission model for extensions?

### Q6 — Distribution and reuse
"Collaborate and share with your entire company"; "I copied this exact
account growth app into a bigger dashboard." Is there a gallery/catalog
for publishing and reusing custom apps org-wide, and can one be
copied/embedded into a different dashboard while keeping it wired to
shared context?

### Q7 — The "shadow AI-coding" framing
"Every team out there right now has a bunch of people Claude Coding up a
bunch of local one-off reports... their own personalised mini apps." Do
any comparison tools explicitly position a feature as the governed home
for AI-generated one-off artifacts (vs. positioning custom
apps/extensions purely as a developer/admin feature)? Is this framing
novel, or is another vendor already making the same pitch?

### Q8 (synthesis question, answer in analysis not findings)
Given Q1–Q7, what — if anything — is genuinely differentiated about
Supersimple's Custom Apps versus the nearest existing pattern, and what
is table-stakes the pitch is merely repackaging?

## Output format for a findings submission

One section per question (Q1–Q7), each with a table:

| Entry | What it is | Supersimple Custom Apps concept overlap | Verdict |
|---|---|---|---|

Verdict is a closed set: `matches` / `partially matches` / `no
equivalent` — no invented labels; put rationale in a Notes block under
the table, not in the verdict cell. No empty tables — a "no equivalent
found" result gets a `no equivalent` row naming the tool, with the reason
in Notes. End with an `## Open gaps` section for anything the question
set missed.

Q8 is answered only in `05-analysis/analysis.md`, not in a findings
file — it requires comparing across questions and sources, which is
synthesis work, not independent findings.
