# San Francisco downtown/SoMa historical place names

**State: two briefs, plus one single-source retrieval probe.** No
commission has answered either brief. The probe under
`03-runs/claude-probe-2026-08-25/` is one source, ungraded, and is not an
answer to either brief — but it did obtain a substantive primary
administrative source and open the conflict register, so it is evidence
and is citable as such, with its markers respected.

## Read order

1. `00-topic/source-material.md` — the operator's full multi-phase project
   brief, as supplied.
2. `00-topic/dispatch-extract.md` — the research-bearing sections of it
   (§1, §2, §3, §7, §11, §12), which is what the commissions were built on.
3. `01-brief/brief-a-gazetteer.md` — commission A, breadth.
4. `01-brief/brief-b-cases-chronology.md` — commission B, depth.
5. `03-runs/claude-probe-2026-08-25/findings.md` — the retrieval probe,
   and the only evidence here so far.

## What the source brief asked for, and what was commissioned

The source brief is a project execution plan: it specifies a repository
layout, JSON record schemas, controlled vocabularies, a Git workflow, and
a five-phase build sequence, wrapped around a historical research
question. Research models can answer the question; they cannot build the
repository. So the execution material was stripped and only the
research-bearing sections were sent — the questions themselves, the
geographic and temporal scope, the evidence-handling principles, the
controlled vocabularies whose closed sets an answer must use, the
name-specific research notes, and the out-of-scope list.

That extract was then split into two independent commissions rather than
one, to protect depth: a single brief asking for 23 gazetteer entries,
five extended cases, a chronology and three registers would likely have
truncated. The split is breadth versus depth, not deliverable versus
deliverable — each commission carries its own source registry and
conflict register, because a registry can only document sources that run
actually read. The intended benefit is that the overlap between the two
registries becomes a cross-check: two independent runs citing the same
map sheet for the same fact either agree or expose a disagreement that a
single synthesis would have hidden.

## Why there are no findings

Commission A was dispatched on 2026-08-21 as run `r-2026-0821-01`, with
three research models and web search enabled. It never returned. The run
record stopped updating and the server itself eventually reported that
the run had been open far longer than a commission takes and that the
record would not update itself — consistent with the orchestration
service restarting mid-run. The MCP channel is the only route to that
service from a session container, and it exposes no way to recover a
partial or completed response from an orphaned run, so the output (if any
was produced) is not retrievable from the corpus side.

Actual spend is unknown. The run's cost field never settled.

Commission B was drafted and deliberately **not** dispatched. Sending a
second thirty-to-forty-minute searching run into a service with a
demonstrated restart problem risks orphaning the same way, and the
exposure here is duration as much as price.

The run record itself is not committed here. Local run records belong to
Minority Report, not to this corpus (`CONTRIBUTING.md`, "Route changes by
owner").

## Checksum note on the dispatch extract

`00-topic/dispatch-extract.md` is the extract as generated from
`source-material.md`: 7,574 bytes, sha256 `3252ef60a88b…`.

The copy actually sent to the models differed slightly — the server
recorded it as 7,557 bytes / 7,551 characters, sha256 `d70574336fe7…`.
The difference is smart-quote normalisation introduced when the extract
was transcribed into the dispatch call. The two are not byte-identical
and are recorded separately here rather than asserted to be the same
file. The exact dispatched bytes live only in the orphaned run record on
the host.

## Cost calibration observed while this ran

Worth carrying forward if these briefs are dispatched later: across the
six prior runs whose records are committed in this repository, **every
run cost more than its estimate**, searching runs by up to 10.6×.

| Run | Search | Estimate | Actual | Ratio |
|---|---|---|---|---|
| r-2026-0812-03 | on | $0.287 | $3.032 | 10.6× |
| r-2026-0813-02 | on | $0.299 | $2.160 | 7.2× |
| r-2026-0813-03 | on | $0.304 | $0.970 | 3.2× |
| r-2026-0814-01 | on | $0.294 | $0.846 | 2.9× |
| r-2026-0812-04 | off | $0.272 | $0.752 | 2.8× |
| r-2026-0813-01 | off | $0.180 | $0.640 | 3.6× |

The commission review's "this run cannot exceed $X" figure models
completion tokens at the 16,000-token cap. Web-search results bill as
*prompt* tokens, which that arithmetic does not bound, so the stated
worst case is meaningful for an offline run and misleading for a
searching one. Note also that `r-2026-0812-03` settled at $3.03 against a
default $1.00 ceiling, which suggests the ceiling is a pre-dispatch
admission check rather than a runtime cap. That is an inference from the
committed records, not a reading of the enforcement code.

## What the probe established

Run 2026-08-25, single source, ungraded. In short:

- SF Planning's **Historic Context Statement, South of the Market Area**
  (Page & Turnbull, 30 June 2009, 118 pp.) was retrieved and read in full.
  It answers, with quotable passages, the 100 Vara / 50 Vara survey extent,
  the 1869 Second Street Cut, Happy Valley's street-bounded extent, Pleasant
  Valley, Steamboat Point (1851), Tar Flat and its supersession of the two
  valleys, and Rincon Point as distinct from Rincon Hill.
- **Neither that document nor the open web dates the first print use of
  "SoMa".** The name appears in it ten times, always as a modern planning
  label. This question is not answerable by retrieval and should be
  specified as a gap, not commissioned.
- **One conflict is already open**: Page & Turnbull put 50 Vara blocks
  between Yerba Buena Cove and 1st Street with 100 Vara only from 1st to
  5th, while a 1945 city document is reported to run the 100 Vara District
  from Market to the Ferry. Unadjudicated.
- **Brief B's task text says The East Cut was adopted in 2018; reporting
  points at 2017.** The year must be pinned before either is cited. The
  briefs are left unedited — the correction belongs in findings, not in a
  silent rewrite of a brief that a run was already dispatched against.
- Page retrieval is governed by an **egress domain allowlist**. Every news
  and reference host attempted was blocked; the agency archive was not.
  Any plan that depends on hand retrieval has to account for that.

## Modern geometry

[`02-run-plan/acquire-geo.md`](02-run-plan/acquire-geo.md) covers acquiring
street and boundary geometry from Overture Maps for all of San Francisco, not
just the pilot — the source brief's scope was always the whole city, with
downtown/SoMa as a high-documentation starting point. Acquisition runs on a
host with open egress and commits derived GeoJSON plus a provenance sidecar;
the licence question (ODbL versus public-domain TIGER) is settled there rather
than at publication time.

## What a later session would need to decide

1. Whether the host is stable enough for a long searching run.
2. Whether to keep web search on. The argument for it is that this
   deliverable is a source registry and unverifiable citations are worse
   than none; the argument against is cost, non-reproducibility, and the
   restart exposure that a long run carries.
3. Whether to dispatch A and B at all, or research the pilot by hand
   against the same briefs.
4. Whether to re-scope the commission in light of the probe: Case Five is
   mostly retrieval and does not need three frontier models; Case One
   cannot be retrieved at any price and should be declared a gap. What is
   left for a commission is the judgment-heavy work — place-class
   assignment, extent precision, adjudicating the 100 Vara disagreement,
   and holding survey meaning apart from social meaning.
