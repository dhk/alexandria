# Written-communication best practices, and `claude-writing-skills` measured against them

Literature synthesis then tool evaluation, opened 2026-08-12. Assurance level:
**Silver (graded multi-model)** — three independent research outputs, claims
extracted and scored across all three by a fourth model. No source audit.

## What this is

The brief asks a deliberately ordered question: *first* establish what the
research and practitioner literature says are best practices for written
communication — and how they vary by context, purpose, audience, and content
type — and only *then* turn to the three skills in
`github.com/nonatofabio/claude-writing-skills` (`ste`, `plainspoken`,
`humanize`) and assess them against it.

The ordering is the point. The synthesis has to stand on its own as a citable
literature review, independent of the tool, because the output is meant as a
collaborative proposal to that repo's maintainer — and a critique is only worth
reading if its standard was set before the thing being judged.

## Two runs, one brief

Both runs answer the **identical brief** (`brief_sha256` `2f4b3fc840ed85b1`).
They differ in one variable: whether the models could read the live web.

| | `r-2026-0812-04` | `r-2026-0812-03` |
|---|---|---|
| Web search | off | on |
| Status | completed | partial, recovered |
| Claims | 26 | 37 |
| Cost | $0.75 | $3.03 |
| Reproducible from inputs | yes | no — rests on pages read 2026-08-12 |

`-04` is canonical. `-03` is kept because live sources produced citations —
specific papers, dates, venues — that the offline models could not supply, and
because the pair is itself a finding: what four times the money buys is more
claims and more citation specificity, on a question where nobody has yet
checked whether those citations are accurate.

## Read order

1. [`01-brief/brief.md`](01-brief/brief.md) — the commission, verbatim as sent
   to every model.
2. [`05-analysis/analysis.md`](05-analysis/analysis.md) — the comparative
   analysis for `-04`: where the three outputs converge, where they diverge.
3. [`05-analysis/scores.csv`](05-analysis/scores.csv) and
   [`claims.json`](05-analysis/claims.json) — 26 claims, each scored against
   every model with the quote the score rests on.
4. [`03-runs/r-2026-0812-03-salvaged/`](03-runs/r-2026-0812-03-salvaged/) — the
   same shapes for the searching run, plus
   [`recovery.md`](03-runs/r-2026-0812-03-salvaged/recovery.md), which states
   exactly what was repaired to get them.

The rows where one model supports a claim and another disputes it are the ones
worth reading first. That disagreement is the product.

## How far to trust it

Silver: three lineages, claims scored, quotes attached — and **no source
audit**. A score records whether a model *stated* a claim and quotes the span
it stated it in. Nobody has checked that the cited sources say what the models
say they say. That check is the difference between Silver and Gold here, and it
has not been done.

Scores are also model-assigned integers rather than derived ones.
[`docs/confidence-calibration.md`](../../docs/confidence-calibration.md) §4
specifies that the grader emits a `(stance, strength)` pair and the integer
comes from a fixed lookup, precisely because direct numeric self-rating from a
model is badly calibrated; the implemented prompt asks for the number directly.
Filed as dhk/minority-report#51.

Raw provider responses are not published — the corpus is public. Each run's
JSON records that they exist, with sizes and sha256s, so the omission is
visible and the bodies remain checkable on the host.

Stages `00-topic`, `02-run-plan`, `04-`, and `06-`…`08-published` are absent.
The commission came from the operator directly rather than from a prior topic
pass, and nothing here has been through synthesis or publication.
