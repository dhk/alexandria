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
