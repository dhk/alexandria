# The browser viewer for this investigation

`index.html` is the whole investigation as one page: both matrices, the ranked
selection rule, a review prompt, and what each technique is with its reference.
It is a single self-contained file — open it, no server and no build step.

## It is generated, and that is the point

`index.html` is **derived, not authored**. Rebuild it with:

```
python scripts/build_viewer.py 2026-08-13-organizational-writing-by-genre
```

The page's two hundred cell values come from
[`../05-analysis/matrices.md`](../05-analysis/matrices.md), read through
`scripts/matrices.py` — the same parser `validate.py` uses to cross-check the
published tables against the recorded votes. Before this the page carried its
own transcription of those cells, which made it a fourth copy of the numbers
and the only one nothing compared against the original. That is the shape
[#62](https://github.com/dhk/alexandria/issues/62) took, one layer out from
where it was found.

`validate.py` rebuilds the page on every CI run and fails if the committed file
differs, so a corrected analysis and a stale page cannot both pass.

## Why not build from `04-normalized/`

It would be the better source and is not yet a usable one. Coverage there is
`contested-cells-only`: eleven of two hundred cells have promoted votes, and a
page built from them would be almost entirely gaps. When coverage reaches
`complete`, `generate_matrices.py` regenerates the analysis from those votes
and this keeps building from the analysis — the chain closes without
`build_viewer.py` changing.

## What lives where

| File | Authored? | Contains |
|---|---|---|
| `template.html` | yes | layout, styles, behaviour, and the prose describing each technique |
| `index.html` | no | `template.html` with the cell values substituted in |

Anything that is not a cell value belongs in `template.html`. The technique
records there carry each technique's description and reference; a reference
link appears only where the URL could be verified, and the rest print their
citation in full instead.
