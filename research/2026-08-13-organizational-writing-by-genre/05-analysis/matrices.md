# The matrices

**What this is.** Two matrices synthesised from the three research outputs of
run `r-2026-0813-03`, plus the cells where those outputs disagree. Matrix A is
about the *situation* — what a genre requires, independent of any tool. Matrix
B is about the *tools* — what each technique does to that quality. The
selection rule is to match a genre's column in A against the technique columns
in B, rather than to trust a recommendation.

**How it was built.** Each model produced its own tables on its own scale:
0–3 for demand in all three; −2..+2 for supply in two, and a five-letter scale
(`S`/`s`/`N`/`d`/`D`) in the third, which maps onto the same five points. Those
were normalised and the **median** of the three is shown. No model's numbers
were overridden and nothing was rounded toward agreement.

**Read the contested cells first.** Where the three models differ by two points
or more, the cell is marked `!` and every vote is listed below the table. A
median across a genuine disagreement is an artifact, not a finding.


### Matrix A — the demand

What each genre requires, independent of any tool. Scale 0–3: 0 irrelevant, 1 minor, 2 important, 3 critical. Median of three independent models.

| Consideration | Info brief | Investigation summary | Research proposal | Recommendation | Incident notification | Postmortem | Status update | Decision record | Dissent | Reference docs |
|---|---|---|---|---|---|---|---|---|---|---|
| Precision | +3 | +3 | +3 | +2 | +3 | +3 | +2 | +3 | +3 | +3 |
| Brevity | +2 | +2 | +1 | +2 | +3 | +1 | +3 | +1 | +1 | +1 |
| Scannability | +2 | +2 | +2 | +3 | +3 | +2 | +3 | +2 | +2 | +3 |
| Actionability | 0 | +2 | +2 | +3 | +3 | +2 | +2 | +1 | +2 | +2 |
| Confidence calibration | +2 | +3 | +3 | +2 | +3 | +2 | +3 | +2 | +2 | +1 |
| Empathy | +1 | +1 | +2 | +2 | +3 | +3 | +1 | +1 | +3 | +2 |
| Persuasive force | 0 | +1 | +3 | +3 | +1 | +1 | +0 | +1 | +3 | 0 |
| Accountability | +1 | +2 | +2 | +2 | +2 | +3 | +2 | +3 | +2 | +1 |
| Accessibility | +2 | +2 | +2 | +2 | +3 | +2 | +2 | +2 | +2 | +3 |
| Durability | +1 | +2 | +2 | +2 | +1 | +3 | +1 | +3 | +2 | +3 |

`†` = one model declined to score this cell. `·` = no model scored it.

### Matrix B — the supply

What each technique does to that quality. Scale −2 to +2: +2 serves it strongly, 0 neutral, −2 actively damages it. Median of three independent models.

| Consideration | ASD-STE100 | BLUF/Army | Minto | Amazon memo | ISO 24495-1 | Blameless PM | Toulmin | Hemingway | Hotaling | repo skills |
|---|---|---|---|---|---|---|---|---|---|---|
| Precision | +2 | +1 | +1 | +2 | +1† | **+1!** | +2 | **0!** | +1 | +2† |
| Brevity | +2 | +2 | +1 | -1 | +1† | 0 | -1† | +2 | +2 | +2 |
| Scannability | +1 | +2 | +2 | -2† | +2† | +1 | 0 | **+1!** | +1 | +2† |
| Actionability | +2 | +2 | +1 | +1 | +2† | +1 | +1 | 0 | 0 | +2 |
| Confidence calibration | -2 | -1 | -0† | **+1!** | +1† | +2 | +2 | -2 | 0 | -1† |
| Empathy | -1† | 0 | 0 | +1 | +2† | +2 | +1 | 0 | 0 | **0!** |
| Persuasive force | -2 | +1 | +2 | +2 | +0† | 0 | +2 | -1 | 0 | **-0!** |
| Accountability | +1 | +1 | 0 | +1 | +1† | +2† | +1 | **0!** | **0!** | +2† |
| Accessibility | +2 | +1 | +1 | 0† | +2† | +1 | 0 | +2† | +1 | +2† |
| Durability | +1 | 0 | +1 | +2 | +1† | +2 | +2 | **-1!** | 0 | **0!** |

**Contested cells** — the three models differ  by two points or more, so the median is not a consensus and should not be read as one:

- **Precision × Blameless PM** — +1, +0, +2
- **Precision × Hemingway** — -1, +0, +1
- **Scannability × Hemingway** — +0, +2, +1
- **Confidence calibration × Amazon memo** — +2, +0, +1
- **Empathy × repo skills** — -1, +1
- **Persuasive force × repo skills** — -2, +1
- **Accountability × Hemingway** — +0, -1, +2
- **Accountability × Hotaling** — +0, +0, +2
- **Durability × Hemingway** — +0, -2, -1
- **Durability × repo skills** — +1, -1

`†` = one model declined to score this cell. `·` = no model scored it.

---

## What the disagreements say

The claim landscape for this run records **25 consensus claims and zero
disagreements**. At cell level the same three outputs disagree in **ten
places**. Both statements are true, and the gap between them is a property of
the instrument: claims are extracted as propositions and scored by whether
models support or dispute them, so a disagreement about *how much* a technique
serves a quality never becomes a disputed claim. Read the group counts as
"nobody contradicted anybody", not as "the models agreed".

Four of the ten contested cells concern the **Hemingway Editor** — precision,
scannability, accountability, durability. That is the one technique in the set
with no published methodology, and the spread reflects it: the models are
scoring different guesses about what it actually implements.

Three concern the **repo's own skills**, on empathy, persuasive force, and
durability — driven by whether a model treated the three skills as one toolkit
or scored them separately. That ambiguity is itself a finding about the repo.

The **Amazon memo on confidence calibration** splits +2 / +1 / 0, which is the
live question of whether narrative prose genuinely forces calibrated claims or
merely provides room for them.

## What no cell in either matrix rests on

Outcome evidence. No technique here has been shown to improve organizational
decision quality, trust calibration, incident recurrence, or the durability of
reasoning. Every score is a judgement about mechanism, and the strongest
claims in Matrix B — Amazon's prose-over-bullets in particular — remain
unproven outside the institution that practises them.
