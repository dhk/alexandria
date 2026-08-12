# Provenance — run r-2026-0812-03

## What was run

| | |
|---|---|
| Run | `r-2026-0812-03` |
| Dispatched | 2026-08-12T15:31Z, from draft `d-a5463f9f1cc8` |
| Brief revision | `A`, sha256 `2f4b3fc840ed` |
| Research models | `openai/gpt-5.4`, `anthropic/claude-opus-4.7`, `x-ai/grok-4.5` |
| Grading model | `anthropic/claude-sonnet-4.6` |
| Web search | on |
| Status as recorded | `partial` |
| Elapsed | 458s |

Inputs were the seven files of `github.com/nonatofabio/claude-writing-skills`
listed in the run's own `run.json`, each with a recorded sha256.

## Why this is a recovery, not a clean run

Every model call succeeded and was billed (`failed_call_count: 0`). The
grading model returned a complete response — `finish_reason: stop`, 38,782
characters, closing fence intact — but the JSON inside it did not parse:

```
Expecting ',' delimiter: line 634 column 83 (char 27683)
```

The grader had quoted source text containing raw double quotes, e.g.
`'if the honest answer is "it depends"'`, without escaping them. **Six**
such characters in 38,782 made the whole response unparseable, and the
pipeline has no repair or retry step, so it wrote an empty `claims.json`,
a header-only `scores.csv` and an 84-byte stub `report.md` — discarding a
grading pass that had already been paid for.

The material here was recovered by re-escaping only those double quotes
that cannot be string terminators (a quote is a terminator only when the
next non-whitespace character is one of `,}]:`). Nothing else was altered:
no content was rewritten, reordered, or summarised. The run directory
itself was left exactly as the pipeline wrote it.

`model_index` values were mapped to models by matching each score's quote
back to the model output containing it, not by assuming dispatch order.

## Cost

| | Estimated | Actual |
|---|---|---|
| Total | $0.2873 | **$3.0321** |
| Research | $0.1925 | $2.8011 |
| Grading | $0.0797 | $0.2310 |

The run cost **10.6x its estimate and
overran the $1.00 ceiling the commission review called "the only bound that
is enforced"**. Cause: research prompt tokens came to
529,883 against an estimate built on
10,583
input tokens — web-search results are billed as prompt tokens, and the
estimator adds only a flat per-search charge. Filed as a defect against the
tooling repo (`dhk/minority-report`).

An earlier attempt at the same brief, `r-2026-0812-02`, failed differently:
`anthropic/claude-opus-4.7` and the grading call both returned HTTP 402
because the OpenRouter key's weekly limit could not cover a reservation of
`max_tokens x completion price`, with `max_tokens` defaulted to 65,536 by
OpenRouter because the client never sets it.

## Score distribution

`+3`: 22 · `+2`: 38 · `+1`: 7 · `+0`: 20 · `-1`: 5 · `-2`: 19

Across 37 claims and 111 model scores.
