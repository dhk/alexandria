# RFC-0005 — The commission surface

Design v1.0 · Historical · 28 July 2026

This is the preserved design record for the original commission surface. Current
executable behavior and operational guidance are authoritative in
[Minority Report](https://github.com/dhk/minority-report/blob/main/docs/COMMISSION-SURFACE.md).
The artifact and honesty rationale below remains useful history, but this file no
longer governs implementation.

A single-operator web UI that commissions one research brief to several models, then
presents the result as a claim landscape with evidence one click away. The UI reads the
run record. It produces no interpretation of its own.

| | |
|---|---|
| Surface | Desktop web · 5 screens · min viewport 1280px |
| Deploy | Local · single operator |
| Record | Git repo · immutable |
| Assurance | Bronze — exploratory |

> Agreement is model agreement. It is not verification. Every screen exists to keep that
> distinction legible — which is why silence, failure, and single-source claims are
> rendered as first-class states rather than gaps.

---

## 01 — Goals and non-goals

**Goals**

- Assemble an input set and a brief, and see exactly what will be dispatched before anything is sent.
- Commit to spend as an explicit, priced decision with a hard ceiling.
- Read a run's outcome as canonical claims × models, grouped by epistemic status.
- Reach the verbatim span behind any score in one action.
- Make failure, exclusion, and silence visible inside the result — never in a log the operator must find.

**Non-goals (V0.1)**

- No accounts, sharing, or multi-user review. One operator, one machine.
- No editing of claims or scores in the UI. Corrections are superseding artifacts (AGENTS.md §5).
- No streaming token view. The harness consumes complete responses.
- No Silver or Gold review workflow. No adjudication UI, no approval gates.
- No OCR, no re-extraction retry, no per-file extraction settings.
- No mobile layout.

---

## 02 — Surface map

Persistent sticky header on all screens. A numbered lifecycle rail on every screen except
History. Screen body max-width 1440px, gutter 32px. A 620px right drawer overlays the body
and never navigates away.

The sequence is a lifecycle, not a wizard: once a run exists, the rail permits free navigation.

| Screen | Does | Leaves via |
|---|---|---|
| History | Lists every run — completed, partial, draft — with inputs, model set, cost, status. | Row → Result · New → 01 |
| 01 Commission | Left: input set (paste + files, extraction state each). Right: four brief fields, sent verbatim. | Review → 02 |
| 02 Review | Model selection, warnings, priced summary against a ceiling. Last screen before dispatch. | Run → 03 · Back → 01 |
| 03 Run | Stage list and per-call state. Elapsed and completed calls only. | Open result → 04 · Cancel |
| 04 Result | Four tabs over one run: claim landscape, report, raw outputs, provenance. | Drawer · Revise → 01 |

---

## 03 — Screen specs

### Screen 00 — History (single column, 1440 max)

Opens with the thesis stated plainly, then the run table. A run is never deleted;
archiving hides it. Draft rows resume into Commission rather than opening a result.

Build:
- Hero: h1 clamp(38–52px)/700, one positioning paragraph, primary "Start a commission →" + ghost "Open the last result".
- Section divider "Run history" — mono uppercase label + hairline rule.
- Grid (not `<table>`): run id (mono), brief title, inputs, model set, cost, status pill.
- Status pill tints: Completed cobalt, Partial orange, Draft neutral `--bg3`.
- Row hover lifts to `--bg3`; whole row is the hit target.

Rules:
- Cost is actual recorded spend when it exists. Until then the estimate, labelled "estimated" in mono.
- Draft rows are local scratch state, not artifacts. No cost, no model set, and they resume into Commission.
- A Partial run is openable and reads as a result, not an error page.
- Footer states that archived runs are hidden, never deleted.

### Screen 01 — Commission (two equal columns, gap 56)

The operator must be able to answer "what exactly will the models see?" before leaving.
Extraction is where research quietly fails, so extraction state is surfaced per file with
the consequence spelled out.

Build:
- Paste panel: bordered card, mono header with live char/token count, footer confirming the draft is local and undispatched.
- Dropzone: dashed border, hard limits stated inline (8 files, 20 MB, 400k chars).
- File rows: name, state pill (Extracted / Warning / Excluded), mono metadata line — format, size, char count, encoding, checksum.
- A warning file gets an orange left-rule line naming the **consequence**, not the cause.
- Input summary strip: inputs kept, extracted chars, tokens per model, excluded count (orange when non-zero).
- Brief: four labelled textareas — Task, Context, Constraints, Output needs — each with a one-line hint.
- Footer: brief revision letter, content sha, autosave state, primary "Review commission →".

Rules:
- Never rewrite, summarise, or normalise brief text. The screen states it is sent verbatim.
- An excluded file stays visible with a restore affordance. Silent dropping is forbidden.
- Checksums are computed on original bytes; derived text is a separate artifact.
- A revision letter is cut at dispatch, from the text as sent. An undispatched draft has no revision — the footer shows autosave state alone.
- Editing the brief after a run starts a new run at the next revision letter. It never mutates the existing one.

### Screen 02 — Review (content 1.25fr + sticky rail 1fr, 1180 max)

The spend gate. Dispatch is an explicit decision made once, against a ceiling the operator
set. Estimates are conservative and labelled as maxima.

Build:
- Model list: checkbox, name, provider slug, context window, per-model estimate. Named default set as a mono token.
- Line stating models research independently and never see each other's output.
- Warnings section repeating each input warning, plus one that content leaves the machine.
- Sticky rail: estimate at 46px/700, fill bar against the ceiling, keyed summary (inputs, brief rev, models, grading model, retention, artifacts).
- Primary button is the commitment and carries the price in its label.

Rules:
- Over ceiling: estimate and bar turn orange, button disables, label states why. Never dispatch and warn afterwards.
- Fewer than two models selected also disables — a single model produces no landscape.
- Estimate colour is the only signal; no alert box.
- Keys are never displayed or entered here. The rail states keys are not exposed to the interface.
- Pricing is fetched at Review time. If the fetch fails the rail reads "Estimate unavailable", names the provider-side key limit as the active ceiling, and the run stays dispatchable.

### Screen 03 — Run (two columns, 1180 max)

Honest progress. Duration is unknowable, so nothing pretends to know it.

Build:
- Header: run id, headline that changes on completion, elapsed clock in mono at 40px, completed-call count.
- Left: six stages with ✓ / ▸ / · marks and Done / Running / Queued labels. Active stage 600 weight, cobalt.
- Right: one row per dispatched model — name, slug, state pill, detail (cost when done, attempt count when retrying).
- A failing model transitions Queued → Retrying → Failed with the status code visible in the detail column.
- Footer button: Cancel while running, "Open result →" when complete, with an explanatory line beside it.

Rules:
- No progress bar and no percentage anywhere on this screen.
- State the page is leaveable and the record is retained either way.
- Cancel copy must state that issued calls may still complete, may still cost, and their output is retained.
- A failed call reaches the Result screen as evidence, never as a discarded row.

### Screen 04 — Result (full 1440, tabbed)

One run, four readings of it. The claim landscape is the default because it is the only
view that shows disagreement structurally. The report is generated and explicitly
subordinate to the evidence.

Build:
- Header: run id + brief rev + completion qualifier, h2 restating the question, one line of what was extracted from what.
- Four stat figures: consensus, disagreement, novel counts, and cost · elapsed — coloured by group token.
- Failure banner: orange left-rule, one sentence, "See limitations →" opening the drawer.
- Tabs: Claim landscape / Report / Raw outputs / Provenance — mono, 2px cobalt underline when active.
- Report tab: prose column at 74ch beside an Artifact card (Copy Markdown, Download bundle).
- Raw tab: one row per call — name, slug, token and cost metadata, "Open raw".
- Provenance tab: manifest key/value list beside limitations, plus revise-and-rerun.
- Drawer: claim detail with per-model stance, score, verbatim quote in an accent-bordered blockquote, locator line; "Open raw output →" swaps the drawer with a back link.

Rules:
- Report copy must name what the run does not establish. A section, not fine print.
- The drawer never navigates away — the landscape stays behind it and scroll position survives.
- A silent model in the drawer reads "No bearing statement found" with nothing to quote. Do not synthesise a quote.
- The completion qualifier names the failure ("completed with one failed call"). Never just "completed".
- Every quote is a verbatim span with a grading-call locator. No paraphrase reaches the UI.

---

## 04 — The claim landscape

The core object. One row per canonical claim, one column per dispatched model, grouped by
epistemic status. Build this before the report tab.

Grid: `1fr repeat(N, 78px) 148px`, gap `0 8px`. Column header sticky at 68px. Row click
opens the claim drawer; row hover lifts to `--bg3`.

### Cell states

Sign is stance, magnitude is strength. Tint alpha encodes strength: `0.20` at ±3, `0.13`
at ±2, `0.07` at ±1. Cobalt `rgba(43,80,232,α)` for support, orange `rgba(224,92,42,α)`
for contradiction. Nothing else carries colour.

| Cell | Meaning |
|---|---|
| `+3` | Supports, strong — stated directly and unhedged |
| `+2` | Supports, moderate |
| `+1` | Supports, weak — implied or in passing |
| `−1…−3` | Contradicts, same strength ladder |
| `—` | Silent. The model responded; the blind grading pass found no bearing statement. **This is an observation.** |
| `✕` | Call failed. No output exists to grade. **A missing observation — never render as silence.** |

The distinction between `—` and `✕` is the single most important detail in this spec.
Collapsing them fabricates coverage.

### Group taxonomy

Assigned by the analysis layer, not the UI. Order is fixed. The five keys and
their precedence are normative in
[`schemas/claim-group.schema.json`](../../schemas/claim-group.schema.json) —
this table is the design rationale for them, not their definition.

| Key | Label | Meaning |
|---|---|---|
| `consensus` | Consensus | Every responding model took the same side. |
| `disagreement` | Disagreement | Models split. Operator judgment required — so it sorts second, not last. |
| `novel` | Novel | Raised by exactly one model, unreviewed by others. A lead, not a finding. |
| `thin` | Thin coverage | Fewer than half the responding models had a bearing statement. |
| `silent` | Unaddressed | No model produced a bearing statement. Absence is not disagreement. |

When a claim qualifies for two groups the **disagreement label wins** — split beats coverage. A claim answered by two of five models that contradict each other therefore reads as Disagreement, which is why the classification cell should carry the responding fraction (see §10).

Filter chips above the grid carry live counts, are single-select, with `All` as default and reset.

---

## 05 — Honesty states

Not error handling. These are the product's argument, each with a defined home in the
layout. Build them in the same pass as the happy path.

| State | Behaviour | Home |
|---|---|---|
| Failed call | Cells read `✕` on every claim; raw entry preserves the attempt log with status codes and timings. Retry creates a new call record, never overwrites. | Result banner, every landscape cell, claim drawer, raw tab, limitations |
| Silence | Graded `—` by the blind pass. Drawer says so in words and offers nothing to quote. | Landscape cell, claim drawer row |
| Excluded input | Stays listed, states why, restorable. Excluded count in the input summary. | Commission file row, input summary, Review warnings |
| Partial extraction | Scanned pages carry no text; no OCR. Copy states those pages reach the models effectively empty. | Commission file warning, Review warnings, limitations |
| Budget | Over ceiling: estimate and bar orange, run button disabled with reason in label. Refusal precedes spend. | Review rail |
| Framing | "Agreement is not verification" appears on History, in the claim drawer, in the report, and in limitations. Four placements is deliberate. | Four surfaces |
| Unpriced run | Pricing fetch failed: rail reads "Estimate unavailable" and names the OpenRouter key limit as the active ceiling. Run proceeds with no price in the button label. An advisory ceiling must not look enforced. | Review rail |
| Retry | Re-dispatches only the failed model into a new run inheriting brief, inputs, and successful outputs by reference. States that it creates a new run id and costs money. | Limitations drawer |

---

## 06 — Data the UI reads

The UI is a reader. Every rendered value comes from the run record on disk; it derives
nothing beyond formatting and the cost estimate. If a field does not exist, the
corresponding element renders a **stated absence** — never a zero, never a blank.

### `run.json` — one per run, immutable

| Field | Use |
|---|---|
| `run_id` | Header and history. Format `r-YYYY-MMDD-NN`. |
| `brief_revision`, `brief_sha256` | Rendered together everywhere the run is identified. |
| `status` | `completed \| partial \| failed \| draft` — drives history pill and header qualifier. |
| `cost_actual`, `elapsed_seconds` | Read from the aggregator response, per call. Absent until the run completes — History then shows the labelled estimate. |
| `inputs[]` | `name, format, bytes, extracted_chars, encoding, sha256, state (extracted \| warning \| excluded), warning` |

### `claims.json` — canonical claims from the union of outputs

| Field | Use |
|---|---|
| `claim_id` | Stable within the run. Drawer deep-link target. |
| `text` | One declarative proposition. Never truncated with an ellipsis. |
| `group` | `consensus \| disagreement \| novel \| thin \| silent`. Assigned upstream. |
| `responding_model_count` | Denominator for "n of m responding models". Excludes failed calls. |

### `scores.csv` — one row per claim × model

| Field | Use |
|---|---|
| `claim_id`, `model_id` | Composite key. A missing row is an error — silence is an explicit `0`. |
| `score` | Integer −3…+3, `0` for graded-silent, null only when the call failed. |
| `quote` | Verbatim span. Required whenever `score ≠ 0`. |
| `grading_call_id` | Locator shown under each quote. |

### `raw/<model>.json`, `manifest.json`

| Field | Use |
|---|---|
| `raw[].body` | Exactly as received. Mono, pre-wrapped, never reformatted or highlighted. |
| `raw[].attempts[]` | Failed calls: attempt number, status, error class, offset. The `✕` drawer content. |
| `resolved_model_id` | Upstream revision the aggregator actually served. Required for reproducibility. |
| `generation_ids[]` | Provider-side call ids, listed for audit. |
| `source_run_id` | On a raw entry inherited by reference into a retry run. Absence means this run dispatched the call itself. |
| `redispatched_models[]` | Manifest field naming which models a retry run actually called. Everything else is inherited evidence. |
| `extraction_method` | Library and version per format. Rendered verbatim. |

---

## 07 — Acceptance criteria

Not done until each is demonstrably true against a run record containing at least one
failed call, one excluded input, one single-source claim, and one unaddressed claim.

- **AC-01** A run with one failed call renders `✕` in that column on every claim row, and `—` never appears in that column.
- **AC-02** Opening a claim shows one row per dispatched model, including silent and failed, with the responding-model denominator excluding failures.
- **AC-03** Every non-zero score in the drawer displays a verbatim quote and a grading-call locator. A score without a quote is a validation failure, not a blank row.
- **AC-04** From any landscape cell, the raw output is at most two clicks away, and returning preserves scroll position.
- **AC-05** Group filter chips show live counts that sum to the total claim count.
- **AC-06** An estimate above the ceiling disables the run button, turns estimate and bar orange, and states the reason in the button label.
- **AC-07** Fewer than two models selected disables the run button with its own reason.
- **AC-08** Excluded inputs remain listed with reason and restore action; the excluded count appears in the input summary.
- **AC-09** The Run screen contains no progress bar, no percentage, no ETA. Elapsed time and completed-call count are present.
- **AC-10** Cancel copy states that issued calls may complete, may cost, and are retained.
- **AC-11** The result header names the failure in its completion qualifier; a partial run never reads as "completed".
- **AC-12** The report contains a section naming what the run does not establish, at body size.
- **AC-13** Provenance shows brief revision and checksum, extraction method and version, grading model, resolved model ids, generation ids, and artifact list.
- **AC-14** Editing the brief creates a new revision and a new run. No screen mutates an existing run record.
- **AC-15** No screen shows or accepts a raw provider key.
- **AC-16** Every colour, radius, and font is a DHK token. No hex literal outside the tint alphas in §04.
- **AC-17** A claim qualifying for both disagreement and thin coverage renders as Disagreement. Split beats coverage.
- **AC-18** When per-model pricing cannot be fetched, the Review rail states the estimate is unavailable, names the provider-side key limit as the active ceiling, and the run remains dispatchable.
- **AC-19** Retry re-dispatches only failed models, creates a new run id, and every inherited raw entry carries `source_run_id`.
- **AC-20** A brief revision letter is cut at dispatch from the text as sent. No revision exists for an undispatched draft.
- **AC-21** Draft rows appear in History with no cost and no model set, and resume into Commission rather than opening a result.

---

## 08 — Visual system

DHK Electric Cobalt, light only. No new colours, no gradients, no shadows, no icon
library. Depth is the three-step grey ladder plus hairline borders. One radius: 4px.

| Token | Use |
|---|---|
| `--bg` | Page |
| `--bg2` | Cards, panels, sticky rail |
| `--bg3` | Row hover, neutral pills |
| `--border` | Structural hairlines, card edges |
| `--accent` | Support, primary action, active tab, consensus |
| `--accent-orange` | Contradiction, failure, warning, over-ceiling |
| `--accent-purple` | Novel claims, drawer chrome |
| `--accent-teal` | Thin coverage only |

Type and motion:
- `system-ui` for all prose. DM Mono strictly for chrome — ids, counts, labels, dates, code, status. Never mono for a sentence.
- h1 clamp(38–52px)/700/−0.02em · h2 34px · h3 20px/600 · body 15–16px at 1.6–1.75.
- Mono chrome 10.5–12px uppercase at 0.08em tracking. Nothing below 10.5px.
- Weight-carrying numbers (estimate, elapsed) large and mono; table numbers 11.5–12px mono.
- Transitions 0.15s on colour, background, border-colour. No bounce, parallax, or skeleton shimmer.
- Spacing via flex/grid `gap` only. Never sibling margins.

Copy register: declarative and compressed. State the limit, then trust the reader — *"No
time remaining is shown, because none is known."* Never hedge, apologise, or use an
exclamation mark or emoji. Uppercase belongs in mono chrome only, never in a heading.

---

## 09 — Build order

1. **Result screen against a fixture.** Landscape, drawer, and raw tab from a hand-written run record containing a failure, a silence, a single-source claim, and an unaddressed claim. This is the product; everything else feeds it.
2. **History and navigation.** Run table, header, rail. Makes the fixture reachable and establishes the lifecycle model.
3. **Commission screen.** Input assembly with extraction states and brief fields — read-only against fixtures first, then wired to real extraction.
4. **Review gate.** Model selection, estimate, ceiling refusal. Nothing dispatches until this screen refuses correctly.
5. **Run screen and dispatch.** Stage and per-call state from the real harness. Last, because it is the only part that spends money.

---

## 10 — Decisions and open questions

### Decided — 28 July 2026

Normative. Reflected in the sections above.

1. **Score scale.** Integer −3…+3, with `0` meaning graded-silent. The contract lives in `schemas/`; the grading prompt and the UI both validate against it.
2. **Group assignment.** The analysis layer writes `group` into `claims.json`. Thin coverage is fewer than half the responding models. When a claim qualifies for two groups, disagreement wins.
3. **Retry semantics.** Retry creates a new run inheriting the brief and inputs, re-dispatches only the failed model, and copies successful outputs by reference. The action lives in the limitations drawer.
4. **Cost source.** Actual cost is read from the aggregator response per call; no vendor price tables in the repo. The Review estimate is fetched at review time. History shows a labelled estimate until actual cost exists. If the pricing fetch fails, the run still dispatches — the OpenRouter key limit is the real ceiling and the UI says so.
5. **Draft persistence.** Drafts are local scratch state, never committed. They appear as History rows that resume into Commission. A brief revision is cut at dispatch, from the text as sent.

### Still open

Per AGENTS.md, the PR carrying this spec must state these. Do not resolve them silently in code.

- **Claim de-duplication.** Who merges near-identical propositions from different models into one canonical claim, and whether the UI ever shows that a claim was merged. Affects the claim count in every stat block.
- **Grading-model failure.** There is an honest state for a failed research call but none for a failed grading pass, which would blank the landscape entirely. Needs a defined surface before the Result screen ships.
- **Coverage on the classification cell.** *Recommended, awaiting confirmation:* render the responding fraction beside the label (`Disagreement · 2/5`) so a thin-coverage split does not overstate its evidence. Follows directly from decision 2.
- **Run record shape.** Whether a run is a git commit or a directory on disk. Does not block the UI, but decides whether History reads the filesystem or the git log.

---

## Companion artifacts

- Interactive prototype: `Alexandria.dc.html` (all five screens, seeded with the wingman provider-layer commission as example data)
- Rendered spec: `docs/ux/RFC-0005-commission-surface.html`
