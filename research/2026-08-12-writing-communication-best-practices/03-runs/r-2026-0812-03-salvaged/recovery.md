# How r-2026-0812-03 was recovered

This run is recorded `partial`. Every model call succeeded and was billed
(`failed_call_count: 0`), and the grading model returned a complete response —
`finish_reason: stop`, `native_finish_reason: end_turn`, 38,782 characters,
closing fence intact. Nothing was truncated.

The JSON inside it would not parse:

```
Expecting ',' delimiter: line 634 column 83 (char 27683)
```

The grading prompt demands verbatim quotes, and verbatim spans of writing
*about writing* contain quotation marks. The grader had quoted source text
without escaping them:

```
"quote": "acknowledges 'if the honest answer is "it depends"' here"
```

**Six** such characters in 38,782. With no repair or retry step, the pipeline
wrote an empty `claims.json`, a header-only `scores.csv`, and an 84-byte stub
report — discarding a grading pass that had already been paid for.

## What was done to it

One structural rule, applied to the preserved raw response: inside a JSON
string, a double quote can only be a terminator when the next non-whitespace
character is one of `,}]:`; anything else means the model was quoting, so the
quote was escaped. That made exactly six substitutions and changed nothing
else. No content was rewritten, reordered, or summarised.

`model_index` was mapped to models by matching each score's quote back to the
output containing it, rather than by assuming dispatch order. Each index's
quotes appear in exactly one model's text, with no cross-contamination.

The run directory on the host was left exactly as the pipeline wrote it. This
is the recovered copy; the run keeps its honest `partial` record.

The underlying defect is filed as dhk/minority-report#51, and a repair step is
proposed in dhk/minority-report#53.

## What it is worth

This run had web search on, so its outputs rest on live pages read on
2026-08-12 and it is **not reproducible from its inputs**. The canonical run
for this investigation is `r-2026-0812-04`, which asked the identical brief
(same `brief_sha256`) with search off.

Read them against each other rather than choosing one. The searching run
produced 37 claims to the offline run's 26, and its citations name specific
papers, dates, and venues that the offline models could not supply. Whether
those citations are accurate is exactly what nobody has checked — no source
audit has been done on either run.

It also cost $3.03 against the offline run's $0.75, for the same question.
