# Normalization

**Status:** Normative
**Depends on:** [`schemas/normalized-matrix.schema.json`](../schemas/normalized-matrix.schema.json)

---

## 1. Why the stage exists

The research lifecycle has always listed `04-normalized/` — *derived,
non-destructive normalization* — and until now no investigation had ever used
it. Normalization still happened; it just happened inside hand-written analysis
prose, where nothing could check it.

That is where [#62](https://github.com/dhk/alexandria/issues/62) came from. A
matrix brief asks each model to score a grid, and models answer on whatever
scale they like: two on the requested `-2..+2`, one on a five-letter
`S`/`s`/`N`/`d`/`D`, one — in a control run — on the `0..3` scale belonging to a
different matrix entirely. Collapsing those onto one scale and taking a median
is a derivation. One run performed it correctly and said so in a preamble; the
control run silently did not, and published a supply matrix holding votes from
another scale. Both artifacts looked equally finished.

A derivation belongs in an artifact with a contract, not in prose.

## 2. Cell values are not stored

The normalized artifact records **votes**, and the cell value is computed from
them. There is no field holding the median.

This is the same rule the corpus applies to a claim score, which is derived from
`(stance, strength)` rather than chosen by a model, and to instrument
conformance, which is derived from recorded facts rather than asserted. In each
case the reason is identical: a stored derived value can drift from what it was
derived from, and once it has, nothing can tell you which one is wrong.

With votes as the only stored quantity, a matrix that disagrees with its
evidence is not a thing that can exist.

## 3. What validation enforces

`scripts/validate.py` checks every `04-normalized/matrices.json`:

- **Every vote lies inside the matrix's declared scale.** This is the #62 check.
  A vote from another scale is not a datum, and the run fails rather than
  producing a median nobody can interpret.
- **The derivation still reproduces the published analysis.** Where a cell
  records `published_value`, the median computed from its votes must render to
  exactly that. This is a cross-reference to a separate artifact, checked like a
  checksum — not a duplicate of derived data.
- **Coverage is honest.** `complete` requires the full row and column
  vocabulary, and every pair must carry votes. Partial coverage is legitimate
  and must be declared; what is forbidden is a matrix that looks complete.
- **Attribution is real.** A cell claiming `votes_attributed` must name a model
  per vote. Where the source analysis published an unattributed list, the
  multiset is all that may be claimed, and the artifact says so.

## 4. Rendering, and the signed zero

Published matrices print a derived median with **sign-preserving truncation
toward zero**. A half-step between two votes therefore appears as a signed zero:
`-0` is −0.5, `+0` is +0.5, and a true zero is unsigned.

This convention was in the corpus before it was written down anywhere, which
made it unreadable — `-0` looks like a typo, and a consumer that parses it as
`0` silently loses the distinction between "the models split" and "the models
agreed on neutral". `_render_median` in `validate.py` is now the single
definition, and the checked `published_value` keeps prose and derivation from
diverging.

## 5. Coverage today

`2026-08-13-organizational-writing-by-genre` is the first investigation with a
`04-normalized/` stage, at coverage `contested-cells-only`. Only the cells whose
votes the published analysis actually listed can be recorded; the rest exist in
the per-model raw responses preserved on the host, which are not promoted into
the corpus. Completing it to `complete` is host-side work.

The control run `r-2026-0814-01` has no normalized artifact deliberately. Its
votes are known to be on mixed scales, so promoting them would land a set that
fails validation by design. Re-deriving it is
[#62](https://github.com/dhk/alexandria/issues/62), and needs the same host
access.

## 5a. The published table has a producer now

`05-analysis/matrices.md` is hand-written, and its digits were connected to
nothing: `published_value` in this stage is a hand-copied claim *about* a
hand-written table, so the two could drift together and neither would notice.
Two things close that.

`scripts/generate_matrices.py` derives a table from recorded votes and prints
it. Where a cell has no votes it prints `·`, reports how many cells that was,
and exits non-zero — a partial emission is never something to paste over a
published table. At `complete` coverage the same command emits the table in
full and exits zero, which is the point at which the digits stop being typed.

`scripts/validate.py` checks the direction that matters today: every cell whose
votes are recorded must print in `matrices.md` as the value those votes derive.
That is ten of two hundred cells for the run described in §5, and the validator
prints the count rather than leaving it to be assumed. Both use
`scripts/matrices.py`, so the rendering rule in §4 has one implementation
rather than one per caller.

What blocks full generation is not the tooling. It is that most cells' votes
were never promoted, and — as `04-normalized/corrections.md` records for the
2026-08-13 genre run — the published columns are a collapse of the columns the
models actually answered on, a step no artifact describes. A generator cannot
invent that rule; it can only stop it being applied silently once it is written
down.

## 6. Every responding model must be accounted for

A cell records a vote per model that scored it. It must also record, as
`unrecorded_model_count`, every responding model whose vote is *not* in that
list — and say why, because "the model declined to score" and "the analysis did
not publish the vote" are different facts with different repairs.

Without that accounting a two-model interpolation is indistinguishable from a
three-model median once it reaches the page. Both print as a single number in
the same column, and the reader has no way to tell that one of them rests on
two thirds of the panel.

A third reason, `off-scale`, was added on 2026-08-21. It covers a model that
scored the cell but not with a value on the declared scale — a range like `0–1`,
or a compound answer naming several sub-columns. That is neither a decline (a
missing observation) nor `not-published` (a missing record): the observation
exists and is not a scale value. Resolving it to a point needs a stated rule,
and a cell carrying this reason is evidence that no such rule was written down.

This is not hypothetical in the current corpus. Of the ten contested cells in
`r-2026-0813-03`, three list only two votes — and none of those three carries
the declined marker the table uses elsewhere. So the corpus alone cannot say
whether the third model declined or the analysis simply omitted its vote. They
are recorded as `not-published` rather than inferred to be declines; the raw
responses on the host would settle it.

### 6a. The cell that needed the third reason

`Persuasive force × Status update` in the demand matrix of `r-2026-0813-03`
publishes `+0`. A median of three votes is always one of those votes, so a
half-step in a matrix documented as three-votes-everywhere-none-contested is
arithmetically impossible. The raw responses say why: `opus-4.7` scored `0`,
`gpt-5.4` scored `1`, and `grok-4.5` answered `0–1`. Two usable votes, median
0.5, printed as a signed zero.

It is recorded as a cell now — `votes: [0, 1]`, one model `off-scale` — so the
matrix states its own exception instead of the exception hiding inside a
rendering convention. Under §7 the cell loses its point value.
## 7. The quorum rule (adopted 2026-08-20)

A published cell value must be a value some model actually assigned.

The scales are ordinal. `+2 serves strongly / 0 neutral / −2 damages` fixes an
order, not equal intervals, and the median is admissible precisely because it is
a rank statistic: it returns an observed category. The even-*n* convention of
averaging the two middle votes is not a rank statistic. It is arithmetic on
category labels, and it produces values outside the measurement system — which
is what the signed zero of §4 has been all along.

**The rule, by case.**

| Votes | Publish |
|---|---|
| n = 3 | the median, at any range — flagged strongly when the votes are contested |
| n = 2, agreeing | that value |
| n = 2, differing | **no point value** |
| n = 1 | no point value |

The n = 3 line is a decision rather than a derivation, and the panel commissioned
on this question (`r-2026-0818-01`) split three ways on it: withhold at range ≥ 3,
withhold at range ≥ 3 but publish range 2 with a flag, or publish at any range
with a strong flag. The third was adopted. At n = 3 the median is always a value
a model assigned, so the rule above is already satisfied; what a wide spread
calls for is a louder flag, not a withheld number. Refusing to print a legitimate
observed value costs the reader a cell they can act on and buys no honesty the
flag does not already supply.

**Why n = 2 differs.** With two differing votes there is no observed middle. Any
number printed there is one no model chose, and on the diverging supply scale it
is worse than that: `{−1, +1}` published as `0` asserts the named category
*neutral*, when one model said mildly damages and the other said mildly helps.
The cell reports agreement where there was a two-way split.

**What this changes.** Six cells, and up to twenty-three.

- Four cells print a signed zero, which is a half-step wearing a scale value's
  clothes: `Confidence calibration × Minto`, `Persuasive force × ISO 24495-1`,
  `Persuasive force × repo skills` in the supply matrix, and
  `Persuasive force × Status update` in the demand matrix. That last one sits in
  a matrix described as carrying three votes on every cell with none contested,
  which makes a half-step impossible — see §6a.
- **Two more print a plain `0`**, and these are the ones worth the rule.
  `Empathy × repo skills` and `Durability × repo skills` each hold `{−1, +1}`.
  Zero is a legal scale value, so nothing looks wrong; but no model said zero.
  One said mildly damages, the other mildly helps, and the cell reports neutral
  agreement where there was a two-way split. The signed zeros advertise
  themselves. These do not, which is why an eye count of the published table
  finds four and running the rule finds six.
- The upper bound is the 22 daggered supply cells: each rests on two votes, and
  any whose votes differ loses its number. Which ones cannot be told from the
  corpus, so the range stays open until coverage does.

**What a withheld cell prints: `·`.** The token the published tables already
use for a cell nobody scored, and `scripts/generate_matrices.py` already emits
for a cell it cannot derive. Reusing it is deliberate — to a reader scanning the
grid, "no number here" is the same fact whichever reason produced it, and a
third glyph would buy a distinction the markers already carry. The reason stays
visible in the annotation: `·†` is a declined vote, `**·!**` a split, bare `·`
a cell no model scored.

**This section is enforced.** `scripts/validate.py` checks it two ways. Where
votes are recorded it derives what §7 permits and compares; where they are not
— which is most cells — it refuses any signed zero outright, since a signed zero
is by construction the midpoint of two differing votes. That second check is
what reaches `Confidence calibration × Minto` and `Persuasive force × ISO
24495-1`, whose votes were never promoted.

§4 describes the signed-zero convention this supersedes. It is kept as the
record of what the corpus did, not as instruction.

