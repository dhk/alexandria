# Brief — San Francisco place names: three unresolved questions

Commissioned 2026-08-24 by the operator, from
[`00-topic/source-material.md`](../00-topic/source-material.md), which the
operator wrote as a standalone handoff prompt. This brief records the
commission **as actually dispatched**, including the two scope reductions
forced by provider timeouts.

## The governing principle carried into every dispatch

Taken verbatim from the operator's brief, because it shapes what counts as an
answer:

> A neighborhood is not a timeless polygon. It is a claim, made by a particular
> source, at a particular date, with a particular degree of geographic precision
> and social or administrative authority. Every answer should be shaped that way
> — not "where is X", but "who said X was where, when, and how much weight does
> that carry".

## The three questions

- **Q1.** Earliest datable published use of "SoMa"/"SOMA" for the San Francisco
  district. Who put it into print and in what register; whether it was coined in
  imitation of SoHo in New York (and if that claim is sourced to anyone at all);
  and whether its extent at first use matched "South of Market".
- **Q2.** The East Cut — exact year and mechanism of adoption by the community
  benefit district; the boundaries as the CBD itself published them; the CBD's
  own wording on deriving the name from the 1869 Second Street Cut; the
  reaction, including the reported ~90%-disapproval survey; and whether anyone
  beyond the coining body ever adopted it.
- **Q3.** The 100 Vara District's extent, where two accounts conflict — Page &
  Turnbull (2009) citing an 1847 plan, against a 1945 city document reported
  secondhand. Both to be checked, neither to be resolved by popularity.

## Standing instructions given to every model call

Passed as a system prompt on each dispatch, condensed from the operator's rules:

1. Every factual claim carries a locator — title, creator/publisher, date, URL
   or archive identifier. A claim with no locator is unusable.
2. Mark each source READ (page retrieved and read) or NOT READ (search snippet
   or memory). Never blur the two.
3. Separate contemporaneous evidence from retrospective commentary, marked per
   claim rather than once at the end.
4. Do not manufacture dates; give ranges and say what bounds them.
5. Do not give a colloquial name a precise boundary it has no evidence for.
   "Unknown extent" is a correct answer.
6. Treat branding and real-estate language as evidence of what its author
   wanted, never as neutral fact.
7. Report what could not be found, specifically enough to act on — which
   database, which years, which publication.

Output shape required per question: **Verdict** (one paragraph, with the
unsettledness stated up front rather than buried), **Evidence** (locators
inline), **What you could not verify**, then a **Source list** and **What would
change this answer**.

Explicitly stated as already established and not to be re-derived: the seven
findings the operator's prior pass took from SF Planning's *Historic Context
Statement, South of the Market Area* (Page & Turnbull, 30 June 2009).

## Scope reductions forced during dispatch

Not planned. Recorded because they changed what was asked, not merely how long
it took — see [`../03-runs/manifest.json`](../03-runs/manifest.json).

- **Q1 and Q3 were each re-issued in a shortened form** after the full-length
  prompt timed out. The rewrite dropped elaboration and added "Be CONCISE",
  keeping every substantive sub-question.
- **Q3 was then split in two** — the 1847 map, and the 1945 document plus the
  land-records question — after the shortened single prompt also timed out.
  Both halves timed out again at the deep-research preset and were re-issued
  against the fast preset, which is a weaker instrument on an archival question.
- **Q2 alone ran once, at full length, as written.**

## What the commission did not ask for

No visual or map-reading task was dispatched: no model was asked to read an
1847 map image, because none of these tools can. That gap was closed outside
the commission by direct operator-side retrieval, recorded in
[`../03-runs/operator-verification-2026-08-24/`](../03-runs/operator-verification-2026-08-24/).
