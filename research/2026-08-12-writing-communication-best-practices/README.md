# Written-communication best practices, and `claude-writing-skills` measured against them

Literature synthesis then tool evaluation, opened 2026-08-12. Assurance
level: **Silver (graded multi-model)** — three independent research
outputs, claims extracted and scored across all three by a fourth model.

## What this is

The brief asks a deliberately ordered question: *first* establish what the
research and practitioner literature says are best practices for written
communication — and how they vary by context, purpose, audience, and
content type — and only *then* turn to the three skills in
`github.com/nonatofabio/claude-writing-skills` (`ste`, `plainspoken`,
`humanize`) and assess them against it.

The ordering is the point. The synthesis is intended to stand on its own
as a citable literature review, independent of the tool, because the
output is meant as a collaborative proposal to that repo's maintainer —
and a critique is only worth reading if its standard was established
before the thing being judged.

Bodies of knowledge in scope: controlled-language standards (ASD-STE100
and comparable controlled Englishes), plain-language guidelines,
style/rhetoric standards, readability research, and the emerging
literature on clearly-AI-generated or AI-disclosed text — detectability,
reader trust, and the risks of over-smoothing or false humanization.

## Read order

1. [`01-brief/brief.md`](01-brief/brief.md) — the commission, verbatim as
   sent to every model.
2. [`03-runs/r-2026-0812-03/report.md`](03-runs/r-2026-0812-03/report.md) —
   the comparative analysis across the three outputs: where they converge,
   where they diverge, and what that implies about confidence.
3. [`03-runs/r-2026-0812-03/claim-landscape.md`](03-runs/r-2026-0812-03/claim-landscape.md) —
   37 extracted claims, each scored against all three models with the
   quote the score rests on. The rows where one model states a claim and
   another contradicts it are the ones worth reading first.
4. [`03-runs/r-2026-0812-03/outputs/`](03-runs/r-2026-0812-03/outputs/) —
   the three research outputs verbatim, unedited.

## Status and how far to trust it

Silver: three models, claims scored, quotes attached — but **no source
audit has been done**. The scores record whether a model *stated and
sourced* a claim, not whether the source says what the model says it
says. Web search was on, so the outputs rest on live pages read on
2026-08-12 and are not reproducible from the inputs alone.

The grading pass reached this repo by recovery, not cleanly: the run is
recorded `partial` because the grader's JSON was malformed, and the
material here was salvaged from the complete-but-unparseable response.
[`provenance.md`](03-runs/r-2026-0812-03/provenance.md) states exactly
what was repaired and what was left untouched. Read it before citing
anything here.

Stages `00-topic`, `02-run-plan`, and `04-`…`08-published` are absent.
The commission came from the operator directly rather than from a prior
topic pass, and nothing here has been through synthesis or publication.

## Known gap

A web-search-off companion run — same brief, reproducible from its inputs
— is intended and not yet possible: three concurrent research calls
reserve more OpenRouter credit than the key has left this week, because
the tooling never sets `max_tokens` and OpenRouter defaults it to 65,536.
Tracked against the tooling repo, `dhk/minority-report`.
