# DHK Design System

The design language of **DHK** — an independent studio publishing essays, small tools,
and data studies at the intersection of **data, thinking, and AI**. This system captures
the *Electric Cobalt* light theme that powers [dhk.io](https://dhk.io) as of May 2026, its
core components, and recreations of its product surfaces.

Consumers link **one** file: `styles.css`.

---

## Sources

Built by reading the real product source. Explore these to go deeper:

- **GitHub — `dhk/DHK-website`** (private, Astro 4.x): https://github.com/dhk/DHK-website
  - Ground truth: `src/styles/global.css`, `public/design-system.md` (Electric Cobalt, May 2026), `CLAUDE.md`
  - Product surfaces: `src/content/{writing,work,signal}`

> **Two palettes exist in the repo.** `src/styles/global.css` + `public/design-system.md`
> define the current **Electric Cobalt** system and are treated as ground truth here. An
> older `design-system.md` at the repo root (green accent, Barlow fonts) is **stale**. This
> design system tracks **only** the Electric Cobalt language; legacy green/Barlow surfaces
> (e.g. the standalone Twine product page) are intentionally excluded.

---

## Content Fundamentals

**Voice.** Declarative, compressed, confident. Short sentences that often land as a claim
then a turn: *"Demos are impressive. Equipping is impactful."* · *"Working, not finished."*
· *"The symptom looks like forgetting. The mechanism is dilution."* Copy states the idea and
trusts the reader to keep up — no hedging, no throat-clearing.

**Person & address.** Mostly third-person and imperative. Addresses "you" directly on
product pages ("You're hired. You have a brief."). First person is rare and never chatty.

**Casing.** Sentence case for all prose and headings. **UPPERCASE only in mono chrome** —
tags, nav, dates, section-divider labels, step numbers. Never uppercase a headline.

**Structure.** Problem → mechanism → implication. Essays open by naming a hidden assumption,
then dismantle it. Tools open with *"## The problem"* before *"## What it is / does."*

**Registers.** Two honesty tells recur: capabilities are described as *"working, not
finished,"* and hype is deflated ("It mostly doesn't"). Prefers *equipping* over *showing*.

**Emoji:** none. **Exclamation marks:** effectively none. **Punctuation flourish:** the em
dash and the mid-sentence period-for-emphasis do the heavy lifting.

**Titles** are either a plain noun phrase ("The Hidden Structure of Policy Networks") or a
crisp opposition ("Showing vs. Shipping", "From Nouns to Verbs").

---

## Visual Foundations

**Palette.** Light theme only — no dark mode. Page is a near-white blue-grey (`--bg #f5f6fa`)
that steps up through `--bg2` / `--bg3` for elevation and hover. The single brand colour is
**Electric Cobalt** (`--accent #2b50e8`), darkening to `#1a3bd4` on hover. Three secondary
accents are **semantic, not decorative**: purple = commentary/tools/graphs, orange =
projects/time-series, teal = studies/data-viz. A separate six-country `--viz-*` set exists
purely for multi-series charts.

**Type.** No custom font, no serif, no condensed. Headings and body both use the native
`system-ui` stack; **DM Mono** (Google Fonts) is reserved strictly for UI chrome — tags,
dates, nav, code, labels — and **never** body prose. h1 is a `clamp(42–64px)` 700 with tight
`-0.02em` tracking; body is 16px / weight 400 (never 300) / line-height 1.75. No UI text
below 11px.

**Spacing.** A 4px-based scale, `--sp1`…`--sp11`. Spacing is expressed with flex/grid `gap`,
**never** sibling margins.

**Backgrounds.** Flat colour only. No gradients, no photography, no illustration, no texture.
Depth comes from the three-step grey ladder and hairline borders — not shadow. The **only**
"imagery" is functional data-viz (line charts, force graphs) drawn in accent colours.

**Borders & radius.** Hairline 1px borders (`--border #c8cde0`) do the structural work:
card bottom-rules, section dividers, the "border-gap" feature grid (a 1px grid gap over a
bordered parent). One corner radius everywhere: **4px**. Corners are never fully round except
the small brand dot and legend pills.

**Shadows.** Essentially none — the system is shadow-free and flat. Elevation is signalled by
`--bg2` surfaces and borders, not drop shadows or blur (the only blur is the sticky header's
`backdrop-filter`).

**Cards.** No shadow, no heavy container. A content card is a flat surface with a bottom
hairline that simply lifts to `--bg3` on hover. Feature cards sit in the border-gap grid.

**Motion.** Restrained and quick. Standard transition is `0.15s` on `color` / `background` /
`border-color`. Longer, expressive easing (`cubic-bezier(0.22,1,0.36,1)`, ~1s) is reserved
for data reveals — warmth bars filling, graph edges drawing in. No bounce, no parallax.
Everything respects `prefers-reduced-motion`.

**Hover / focus / press.** Hover: surfaces → `--bg3`; primary buttons → 0.85 opacity; ghost
buttons and nav → accent border / darker text. Active state on nav is accent colour + a 2px
underline. Focus-visible is a 2px cobalt outline. No dedicated press-shrink.

**Imagery vibe.** There is none in the classic sense — the aesthetic is editorial,
type-forward, and monochrome-plus-cobalt. Cool blue-grey neutrals throughout; warmth only
enters via the semantic orange accent.

---

## Iconography

DHK is **near-iconless by design** — the aesthetic is type- and rule-driven, not icon-driven.

- **No icon library** is installed or linked. There is no icon font, no sprite, no Lucide/
  Heroicons dependency.
- The few glyphs that appear are **inline SVG drawn ad-hoc**: the tiny play/pause triangles in
  the podcast rows (8×8 `polygon`/`rect`), and the Twine hero's force-graph (circles + lines).
  These are illustrative, not a reusable set.
- **Unicode arrows** stand in for icons in links and buttons — `↗` for external/"Follow",
  `→` in step numbers ("01 — Upload"). This is the house convention; keep using `↗` / `→`
  rather than importing an icon set.
- The **brand dot** (a 7px filled circle before the wordmark) is the closest thing to a logo
  mark. The **favicon** is a single mono letter **D** (`assets/favicon.svg`, legacy green fill).
- **No emoji**, anywhere.

**If you need an icon** the source doesn't provide: prefer a Unicode arrow/dot, or a minimal
inline SVG at 1–1.5px stroke matching the hairline weight. If a real set is unavoidable, use
a thin-stroke CDN set (e.g. Lucide) and **flag the substitution** — it is not part of the
native system.

> **Logo caveat:** DHK has no pictorial logo. The brand is a **text wordmark** ("DHK" with a
> cobalt dot). No mark was invented here. The only supplied asset is the favicon `D` glyph,
> which still carries the *legacy* green fill (`#16a34a`) — flagged below.

---

## Components

Reusable primitives (namespace `DHKDesignSystem_c5bcb5`), in `components/core/`:

- **Button** — mono-uppercase action; `primary` (solid cobalt) / `ghost` (outlined).
- **Tag** — content-type pill, tinted by `kind` (essay/commentary/tool/study/project).
- **Card** — shared content-list surface; hover-lifts to `--bg3`, optional tag/date/title/excerpt.
- **SectionDivider** — mono label + hairline rule; opens every section.
- **NavLink** — sticky-header nav item; dim → dark → cobalt-underline when active.
- **FeatureGrid** / **FeatureCard** — the border-gap grid with hairline dividers.
- **Meta** — mono metadata line (dates, breadcrumbs, counts).
- **PostHeader** — article/product-page header: breadcrumb, title, excerpt, bottom hairline.
- **PullQuote** — accent-left-border quotation, italic and muted.

Each directory has a `.d.ts` (props + adherence), a `.prompt.md` (usage), and a `@dsCard`
showcase HTML.

*Component inventory note:* the DHK site is content-first and defines these patterns in CSS
rather than a formal component library. This set is a faithful extraction of the real,
recurring patterns in `global.css` — no speculative primitives were added.

---

## UI Kits

- **`ui_kits/dhk-website/`** — interactive recreation of dhk.io: Home, Writing, Lab, Listen,
  Signal, About, Article. Composes the core components; content mirrors the real collections.

---

## Repository Index

- `styles.css` — **the** entry point (imports only).
- `tokens/` — `colors.css`, `typography.css`, `spacing.css`, `layout.css`, `fonts.css`, `base.css`.
- `components/core/` — Button, Tag, Card, SectionDivider, NavLink, FeatureGrid, Meta.
- `guidelines/` — foundation specimen cards (Colors, Type, Spacing, Brand).
- `ui_kits/` — `dhk-website/`.
- `assets/` — `favicon.svg`.
- `SKILL.md` — Agent-Skill wrapper for downloadable use.

---

## Caveats / Substitutions

- **Fonts are loaded from Google Fonts CDN**, not bundled binaries: **DM Mono** (real site
  dependency) and **Barlow / Barlow Condensed** (for the legacy Twine kit). Headings/body use
  the native `system-ui` stack, so no webfont is needed for them. If you want self-hosted font
  files instead of the CDN, provide them and they'll be wired into `tokens/fonts.css`.
- **Favicon** is the only supplied brand asset and still uses the **legacy green** fill; it
  predates the Electric Cobalt migration. Provide an updated cobalt favicon if desired.
- **Twine (excluded).** The standalone Twine product page ships in its own legacy green/
  Barlow palette, which is off-system; it is intentionally omitted from this design system.
