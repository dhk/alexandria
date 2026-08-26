# How a brief becomes a checkable record

![How a brief becomes a checkable record: a research brief is priced by begin_research, which calls no model; it crosses an explicit review gate the operator must confirm before any spend; past the gate the work runs either as a commissioned multi-model run with a grader, or as a single-source read; both produce marked evidence, promoted deliberately into Alexandria.](assets/commission-flow.svg)

[`assets/commission-flow.svg`](assets/commission-flow.svg) ·
[`assets/commission-flow.png`](assets/commission-flow.png)

Companion to [`assets/alexandria-architecture.svg`](assets/alexandria-architecture.svg),
which draws the boundary between the two repositories. This one draws what
happens to a single brief as it crosses that boundary — the same structure,
seen as a sequence rather than a map.

## What it shows

**The gate is the load-bearing part.** `begin_research` resolves inputs, prices
the run against live rates, and calls no model at all. It returns an estimate
and a confirmation phrase. Dispatch requires that phrase, supplied by the
operator, so a brief cannot spend money by accident and an edited brief cannot
inherit an earlier approval.

**Two ways to answer, both first-class.** A commissioned run puts one brief to
several models independently and has a grader compare them — agreement is
evidence of convergence, not proof, and the grader's own topology is a recorded
limitation rather than an assumption (see
[`instrument.md`](instrument.md)). A single-source read has one session fetch
and read the documents itself. Neither is a fallback for the other; they answer
different shapes of question, and a brief that turns on a specific document is
usually better served by the second.

**Provenance travels with the evidence, not with the run.** Each claim carries
how it was obtained, so a reader can tell a document that was retrieved and
read from one that a model remembered. See
[`source-audit.md`](source-audit.md).

**Promotion is deliberate.** Nothing crosses into the corpus automatically. A
successful local run is a candidate artifact, not a reviewed one.

## Using this as a primitive

The file is a standalone SVG with no external references, no embedded raster,
and no script. It follows the drawing conventions shared by the other assets in
this directory, so the three read as a set:

| | |
|---|---|
| Frame | `1600 × 900`, `viewBox="0 0 1600 900"` |
| Accessibility | `role="img"` with `aria-labelledby="title desc"`; the `desc` states the claim in full |
| Classes | `bg` `panel` `accent` `gate` `h` `hsmall` `t` `s` `line` — defined in one `<style>` block in `<defs>` |
| Palette | slate neutrals, `#155eef` for flow, `#ea580c` reserved for the review gate |
| Type | `system-ui` for prose, `ui-monospace` for the `s` annotations |

To add a diagram to this set, copy the `<defs>` block verbatim and reuse those
class names rather than introducing new ones. The reserved orange means
*a human decides here* and should not be spent on anything else.

Regenerate the PNG after editing the SVG:

```bash
uv run --no-project --with cairosvg python -c \
  "import cairosvg; cairosvg.svg2png(url='docs/assets/commission-flow.svg', \
   write_to='docs/assets/commission-flow.png', output_width=1600, output_height=900)"
```
