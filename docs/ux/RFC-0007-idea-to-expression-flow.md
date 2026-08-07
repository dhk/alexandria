# RFC-0007 — The idea-to-expression flow

Design v1.0 · Historical draft · 4 August 2026 · Implements issue #34

This document is the design handoff required by issue #34's first acceptance criterion. It is
preserved as product-design history. Current implementation and operator guidance
are owned by [Minority Report](https://github.com/dhk/minority-report); paths below
refer to that repository unless explicitly described as corpus paths.

One left-to-right rail carrying an idea from conception to a finished piece, collapsed to
headlines by default and openable stage by stage. The flow reads the artifact trail. It
summarises nothing the record does not already contain.

| | |
|---|---|
| Surface | One page · six lanes |
| Levels | 0 headline · 1 lanes · 2 prose |
| Viewport | 1280 full · 768 stacked |
| Export | Markdown · mirrors state |

> A stage that was never reached and a stage that produced nothing look identical in a
> scattered trail. The flow exists to keep them apart — which is why every lane renders a
> stated absence rather than an empty cell.

---

## 01 — Goals and non-goals

**Goals**

- See the whole arc of one idea at a glance, in the order it happened.
- Open any single stage without losing the shape of the rest.
- Learn what a stage covers before deciding to read it.
- Reach the canonical artifact from every stage in one action.
- Export what is on screen as Markdown, or the finished piece when one exists.
- Show an idea that stalled as plainly as one that shipped.

**Non-goals (v1)**

- No editing. Nothing on this surface writes to the record.
- No level 3. Full artifacts open in their own view, not inside a lane.
- No cross-idea comparison, portfolio board, or timeline scrubber.
- No summarisation by the UI. Lane text is written upstream or absent.
- No resolution taxonomy. That contract belongs to issue #35.
- No animation of the run. The flow is post-hoc inspection.

---

## 02 — Anatomy of the rail

Six lanes in a border-gap grid: a bordered parent with a 1px gap, so the dividers between
stages are the grid itself. Direction is carried by the numbering and by a single cobalt
progress hairline under the rail — **no arrow glyphs between lanes**, which would not survive
the mobile rotation. The rail is the whole page above the fold; there is no header chrome
beyond the idea line and the export control.

### One lane, collapsed

- **Stage key** — mono uppercase, cobalt when the stage has content, `--text-dim` when not reached.
- **Headline** — 16px/600, up to three lines, clamped at a word. The only prose at level 0.
- **Meta line** — mono 11.5px, stage-specific identifiers and counts. Never a duration estimate.
- **Level control** — mono text button naming the next action: `EXPAND` → `MORE` → `COLLAPSE`.

### The expansion model

Levels are per stage and independent — this is the requirement that decides the layout. Six
lanes cannot each hold prose at 1440px, so an expanded stage **takes the width and its siblings
give it up**, compressing to a 64px rail with a vertically-set mono key. Nothing is hidden: a
compressed lane is still a click target that expands it and releases the others.

| Level | Shows | Grid behaviour |
|---|---|---|
| 0 | Stage key, headline, meta line. | `repeat(6, 1fr)`, equal height, min 148px. Default on load. |
| 1 | Level 0 plus the four lanes describing what this stage's content covers. | Expanded column `minmax(420px, 2.4fr)`; unexpanded siblings `64px`. |
| 2 | Level 1 plus the opening paragraphs of the stage's own artifact. Additive — the lanes stay. | Expanded column `minmax(560px, 3fr)`. Two stages at level 2 split the remainder equally. |

Rules:

- Multiple stages may be open at once. Beyond two at level 2 the rail scrolls horizontally rather than shrinking prose below 420px.
- Width transitions run 0.15s on `grid-template-columns`; content cross-fades with no vertical movement and no shimmer.
- Level state is in the URL — `?open=03:1,04:2` — so a view is linkable and an export is reproducible.
- Keyboard: `←` `→` move focus along the rail, `↓` raises the focused stage a level, `↑` lowers it, `Esc` collapses all.
- A stage with no content cannot be expanded. Its control reads `NOT REACHED` and is inert, not disabled-looking-clickable.

---

## 03 — The six stages and their four lanes

Four lanes is a fixed contract, so the eye learns one shape and reuses it across the rail. The
labels differ per stage and are supplied by the record — the UI never invents a lane. Stage 02's
lanes are the four brief fields from RFC-0005; the rest follow the same principle of naming what
the reader would otherwise have to open the artifact to find out.

| Stage | Four lanes | Level 2 reads |
|---|---|---|
| 01 Idea | Origin · Claim under test · Why now · Scope | `00-topic/` topic.yaml note |
| 02 Research brief | Task · Context · Constraints · Output needs | `01-brief/` brief.md, as sent |
| 03 Engine run | Models dispatched · Inputs as sent · Spend · Failures | `03-runs/` manifest excerpt |
| 04 Results | Consensus · Disagreement · Novel · Coverage | `05-analysis/` report.md |
| 05 Synthesis | Findings · Evidence base · Not established · Open questions | `06-synthesis/` synthesis.md |
| 06 Resolution | Outcome · Expression · Decided by & when · Rationale | `08-published/` or the rationale note |

- **Coverage** is one lane, not three: it carries thin coverage, unaddressed claims, and failed
  calls together, because each is a statement about what the run did not establish. Silence and
  failure stay lexically distinct inside it — `—` is an observation, `✕` is a missing one
  (RFC-0005 §04).
- **Resolution** renders whatever outcome value the record holds, styled by a token map it does
  not own. Any unmapped value renders as its verbatim string in neutral `--bg3`. An absent value
  reads `UNRESOLVED` — a state, not a gap.
- A lane with no value in the record renders its label plus `NOT RECORDED` at `--text-dim`. Four
  lanes always render.

---

## 04 — Wireframes

Rendered wireframes for level 0, level 1 (stage 04 open, siblings compressed), level 2 (lanes
plus prose), and the stacked mobile state are in the companion design component,
`AlexandriaFlowSpec.dc.html`. The written rules in §02, §03, §06, and §10 are normative; the
wireframes show the intended proportions and density.

Level 0, for reference, is one header line (idea title, slug, opened/resolved dates) with the
export control on the right, then the six-lane grid, then the progress hairline with a
`n of 6` count.

---

## 05 — Export

Export mirrors the screen. What is expanded is what is written, so the file is a record of a
reading rather than a dump of the trail — and the operator is never surprised by content they
had not opened. Two placements, no floating control.

**Flow level — header, right.** Ghost button `Export Markdown` with a mono scope line beneath
it: `6 stages · 2 expanded · level 2`. Front matter carries the idea slug, the level state, and
the artifact shas.

**Stage level — expanded footer.** Ghost button `Export stage` beside the artifact link. Writes
that stage alone at its current level. Absent at level 0 — there is nothing to export but a
headline.

Rules:

- When Resolution names a finished piece, the flow-level control becomes a two-item menu:
  **Finished piece** (the published artifact, verbatim) or **Full trace** (the expanded flow).
  The finished piece is listed first.
- Level-2 exports include the paragraphs as shown plus a line naming the paragraphs omitted and
  the path to the full artifact. An excerpt must never read as a complete document.
- Filename `<idea-slug>-flow-L<max-level>.md`. Headings are the stage names at H2, lane labels
  at H3. No UI chrome, counts, or state pills reach the file as prose.
- Export is client-side and writes nothing back to the repository. Promotion into `research/`
  stays a deliberate operator action.

---

## 06 — Responsive behaviour

Left-to-right is how the arc reads on a desktop, not a property worth defending on a phone.
Below 768px the rail rotates: stages stack top-to-bottom, the progress hairline moves to the
left edge, and expansion becomes an ordinary accordion. The reading order, the four lanes, and
the three levels are identical.

- **≥ 1280 · full rail.** Six lanes visible, 1440 max width, 32px gutter. Expansion compresses siblings as specified in §02.
- **768–1279 · scrolling rail.** Lanes hold a 168px floor and the rail scrolls horizontally with `scroll-snap` per lane. The expanded lane pins to the left edge so its content is never half off-screen. Compressed siblings stay 64px and scroll with the rail.
- **< 768 · stacked.** One column. Stage key, headline, meta, and a full-width 44px control per stage. Only one stage open at a time — opening a second closes the first, because a stacked accordion cannot show two prose blocks in context. The header export control becomes sticky at the bottom.

---

## 07 — Honesty states

An arc view invites a false reading: that the trace is complete because it is continuous. Build
these in the same pass as the happy path.

| State | Behaviour |
|---|---|
| Not reached | Lane renders at full height with a dimmed key and the words `Not reached`. The progress hairline stops at the previous stage. Never a blank column, never a skipped column. |
| Stage abandoned | Reached, produced nothing, and later stages exist. Orange left-rule on the lane with one sentence naming what is missing. Distinct from Not reached. |
| Run failure | Stage 03's meta line carries the failed-call count in orange at level 0 — failure is visible before anything is expanded. Stage 04's Coverage lane keeps `✕` distinct from `—`. |
| Unresolved | Stage 06 with no outcome value reads `UNRESOLVED` in a neutral pill, with the date of the last activity. An idea in flight is not a failed idea. |
| Unmapped outcome | An outcome value this UI has no tint for renders verbatim in neutral. The taxonomy may grow in #35 without a change here. |
| Excerpt | Level 2 always states what it omitted — `2 of 9 paragraphs` — on screen and in the export. |
| Superseded stage | Where a stage was rerun, the lane shows the current artifact and a mono line naming the count of superseded predecessors. Corrections are new artifacts, so the flow shows the latest and says so. |

---

## 08 — Data the flow reads

One document per idea, assembled by the analysis layer from the lifecycle directory. The UI
formats and orders; it does not summarise. A missing field renders a stated absence.

| Field | Use |
|---|---|
| `idea_slug`, `title` | Header line and export filename. |
| `stages[].key` | `idea \| brief \| run \| results \| synthesis \| resolution`. Fixed order, exactly six. |
| `stages[].state` | `present \| abandoned \| not_reached`. Drives expandability and the progress hairline. |
| `stages[].headline` | One clause, written upstream. Level 0's only prose. Never generated here. |
| `stages[].meta[]` | Mono chrome tokens — ids, counts, spend, dates. An orange flag if the record marks one. |
| `stages[].lanes[4]` | `label, summary, count?, accent?`. Exactly four, always rendered. Missing summary reads `Not recorded`. |
| `stages[].excerpt` | `paragraphs[], shown_of_total, artifact_path, sha256`. Paragraph array, not a character budget — the UI must not cut prose itself. |
| `stages[].superseded_count` | Rendered when non-zero. Absence means one artifact, not an unknown history. |
| `resolution.outcome` | Verbatim string from issue #35's taxonomy. Null renders `UNRESOLVED`. |
| `resolution.expression` | Path or URL of the finished piece. Its presence is what turns flow-level export into a two-item menu. |

---

## 09 — Acceptance criteria

Not done until each is demonstrably true against two fixtures: one resolved idea with a failed
call and a superseded stage, and one idea that stopped after stage 03.

- **AC-01** All six stages render left-to-right in fixed order at level 0 on load, with no stage omitted for lack of content.
- **AC-02** Each stage's level changes independently; raising one to level 1 or 2 does not change another stage's level.
- **AC-03** Level 1 shows exactly four lanes for every stage, including lanes whose summary is absent.
- **AC-04** Level 2 keeps the four lanes visible and adds the opening paragraphs, with the shown-of-total count on screen.
- **AC-05** No excerpt ends mid-sentence, and no excerpt exceeds the paragraph count the record supplies.
- **AC-06** Markdown export contains exactly the stages and levels expanded on screen, and names the omitted paragraphs and artifact path for every excerpt.
- **AC-07** With a finished piece present, export offers it as a first-class choice beside the trace; with none, the single trace export remains.
- **AC-08** A stage in `not_reached` cannot be expanded, states so in words, and stops the progress hairline at the previous stage.
- **AC-09** An abandoned stage is visually distinct from a not-reached one, and names what is missing.
- **AC-10** Stage 06 renders any outcome string the record holds, including one this UI has no tint for, and reads `UNRESOLVED` when the value is absent.
- **AC-11** A failed call is visible at level 0 on stage 03, before any expansion.
- **AC-12** Reloading a URL with `?open=` restores the same levels, and exporting from it produces an identical file.
- **AC-13** At 375px width the flow stacks vertically, every control is at least 44px tall, and one stage is open at a time.
- **AC-14** The rail is fully operable by keyboard, with a visible cobalt focus ring on every lane and control.
- **AC-15** Nothing on the surface writes to the repository, and no control implies it does.
- **AC-16** Every colour, radius, and font is a DHK token. No hex literal anywhere in the flow.

---

## 10 — Visual system

DHK Electric Cobalt, light only. Structure is carried by hairlines and the three-step grey
ladder; the border-gap grid does the dividing work. One radius: 4px. No gradients, no shadows,
no icon set.

| Token | Use in the flow |
|---|---|
| `--bg` / `--bg2` / `--bg3` | Page · lane surface and lane bodies · lane hover and neutral pills. |
| `--accent` | Stage keys with content, progress hairline, consensus lane, focus ring, primary action. |
| `--accent-orange` | Disagreement, failure, abandonment, not-established. Never decorative. |
| `--accent-purple` | Novel claims only, matching RFC-0005. |
| `--accent-teal` | Coverage lane only. |
| `--border` | The 1px grid gap between lanes, lane edges, and every internal divider. |

- `system-ui` for headlines and prose; DM Mono strictly for chrome — stage keys, counts, shas, paths, level controls. Never mono for a sentence.
- Headline 16px/600 at level 0, 17–18px/600 when expanded. Lane summary 14px/1.6. Excerpt prose 15px/1.75 at 62ch. Mono chrome 10.5–12px uppercase at 0.08em. Nothing below 10.5px.
- Transitions 0.15s on colour, background, border-colour, and grid width. No bounce, no parallax, no shimmer. Under `prefers-reduced-motion` the width change is instant.
- Spacing via flex and grid `gap` on the 4px scale. Never sibling margins.
- Copy register: declarative, compressed, sentence case. Uppercase in mono chrome only. State the limit and trust the reader.

---

## 11 — Build order

1. **Level 0 rail against a fixture.** Six lanes, fixed order, the two absence states, and the progress hairline. This is the whole claim of the feature; everything else is depth.
2. **The expansion mechanic.** Level 1 with sibling compression, URL state, and keyboard control — with lane content stubbed. Get the geometry right before the content lands.
3. **Four-lane content.** Real lanes for all six stages, including every stated absence. Stage 04 first — it is the one with a colour vocabulary to inherit.
4. **Level 2 excerpts.** Paragraph arrays, shown-of-total, artifact links, and the sha line.
5. **Export.** Stage-level first, then flow-level, then the finished-piece branch. Last, because it depends on every level being correct.
6. **Stacked layout.** The mobile rotation and the single-open rule. A layout change only, no new content.

---

## 12 — Decisions and open questions

### Decided — 4 August 2026

Normative, and reflected in the sections above.

1. **Level 2 is additive.** Prose is added beneath the four lanes rather than replacing them, so the reader keeps the map while reading the territory.
2. **Expanding compresses siblings.** Six equal columns cannot hold prose. Compressed lanes stay visible at 64px and remain click targets — the arc is never hidden to read a part of it.
3. **Export mirrors state.** The file contains what is expanded, and nothing else. A trace export of collapsed stages would be a different feature and is a non-goal.
4. **Excerpts are paragraph arrays.** The record supplies whole paragraphs; the UI never counts characters and never truncates prose. "The first couple of paragraphs" means two, or one where only one exists.
5. **Mobile rotates.** Left-to-right is a desktop affordance. Below 768px the same six stages stack, one open at a time.
6. **Lane labels come from the record.** Four lanes is the contract; their names are data. The UI ships fallback labels for the six known stages and renders unknown labels verbatim.

### Still open

Per AGENTS.md, the pull request carrying this spec must state these. Do not resolve them
silently in code.

- **Who writes the headlines and lane summaries.** They are prose that must not be generated by the UI, but no upstream artifact holds them today. Either the analysis layer emits them or an idea-level front matter block does.
- **Multiple runs per idea.** A retry creates a new run id. Whether stage 03 shows the latest run with a superseded count, or splits into parallel sub-lanes, is undecided. The spec assumes the former.
- **Where the flow lives.** A route on the local commission surface, or a generated static page per idea under `generated/`. Decides whether level state can live in the URL as specified.
- **Ideas with no run.** An idea killed at the brief stage has four of six lanes empty and reads as mostly absence. Whether that is acceptable or wants a compact variant needs a real fixture to judge.

### Resolved during implementation — 4 August 2026

Not part of the original design pass; decided while building against real fixtures, per the
same discipline of stating rather than silently resolving.

- **Where the flow lives:** a route on the local commission surface (`GET /flow/{slug}`,
  [`src/alexandria/web.py`](https://github.com/dhk/minority-report/blob/main/src/alexandria/web.py)), not a generated static page. The commission surface already exists
  and already owns the token stylesheets and Starlette routing this needed; a static-site
  generator would have been new infrastructure the RFC never asked for.
- **Who writes the headlines and lane summaries:** an analysis layer
  ([`src/alexandria/flow.py`](https://github.com/dhk/minority-report/blob/main/src/alexandria/flow.py))
  reads them directly from upstream artifacts — `topic.yaml`'s four new fields (`origin`,
  `claim_under_test`, `why_now`, `scope`) for stage 01, `01-brief/brief.md`'s existing verbatim
  format for stage 02, and new `manifest.json` / `summary.yaml` conventions for stages 03–05 —
  never generated by the UI. A field with nothing upstream renders "Not recorded"; this is
  itself a new, small artifact contract, not a workaround.
  **Known gap:** this contract is not retroactive. The one pre-existing investigation in
  `research/` (`2026-07-29-supersimple-custom-apps`) predates it and uses different filenames
  (`analysis.md`, `run-metadata.yaml`); the flow correctly reads its later stages as
  `not_reached` rather than silently inventing content, but no migration exists yet to backfill
  it into the new shape.
- **Multiple runs per idea:** implemented as the spec assumed — stage 03 reads
  `manifest.json`'s `superseded_count` field and shows the latest run only.
- **Ideas with no run:** not specially cased. An idea killed at the brief stage renders stages
  03–06 as `not_reached` via the same reach-state rule as any other trailing gap (present only
  where there is trailing content after it; `not_reached` otherwise). No compact variant was
  built — this should be judged against a real example if one arises, per the original question.
- **Resolution's `morphed` outcome requires a forward pointer**, per issue #35's "no dead ends"
  principle (decided in that issue, not here): `resolution.yaml`'s `expression` field is
  mandatory when `outcome: morphed`, rendered as a clickable link rather than a status label.
  Issue #35 owns validating this at write time; this view only renders what it's given.

---

## Companion artifacts

- Design component with wireframes for every level and the stacked layout: `AlexandriaFlowSpec.dc.html`
- Resolution taxonomy: issue #35
- Implementation: [`src/alexandria/flow.py`](https://github.com/dhk/minority-report/blob/main/src/alexandria/flow.py) (data assembly), [`src/alexandria/flow_view.py`](https://github.com/dhk/minority-report/blob/main/src/alexandria/flow_view.py) (rendering), `GET /flow/{slug}` in [`src/alexandria/web.py`](https://github.com/dhk/minority-report/blob/main/src/alexandria/web.py)
- Tests: [`tests/unit/test_flow.py`](https://github.com/dhk/minority-report/blob/main/tests/unit/test_flow.py), fixtures under [`tests/unit/fixtures/flow/`](https://github.com/dhk/minority-report/tree/main/tests/unit/fixtures/flow)
