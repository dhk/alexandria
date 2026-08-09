# Source material

Preserved verbatim as provided by the operator, across two sessions. This is
input evidence for the investigation, not analysis — see
[`../05-analysis/analysis.md`](../05-analysis/analysis.md) for interpretation.

## Original request (2026-08-08, unrelated Claude Code session)

> I want you to do some research. The Tusk hand is to help people design
> portfolio website websites that are congruent with their brand.
>
> So step one is an interview process to help them understand what their
> brand is use things like resumes, LinkedIn profiles and so forth to help.
> Also, any questions.
>
> Step two is to ask them whatever else makes sense
>
> Step three is to figure out who the audience is Foran what they will
> populate their content with
>
> Step four is to propose some cour schemes and then design layouts
>
> Step five is to build
>
> So the research activity is to go out and find out what tools are out
> there. Look at the build versus by decision. Also, any best practices or
> guidelines that are out there

Read literally as dictated/transcribed rather than corrected: "The Tusk
hand is" is almost certainly a speech-to-text artifact for "The task at
hand is"; "cour schemes" for "colour schemes"; "Foran" for "for and". Not
corrected in the quote above, per this file's own rule (preserved
verbatim) — the five-step process itself is unambiguous and is what
[`../01-brief/brief.md`](../01-brief/brief.md) operationalizes.

## Follow-up: commission the verification pass to Alexandria (same session)

> Create a research brief for this and give it to Alexandria.

Operationalized as `begin_research`'s `task`/`pasted_content`/
`constraints`/`output_needs` fields — see
[`../01-brief/brief.md`](../01-brief/brief.md) for the brief text sent
verbatim to the commission draft.

## Follow-up: after three failed dispatch attempts (same session)

> Write an issue to Alexandria with the research brief.
>
> Do the deep research yourself

Filed as [dhk/minority-report#33](https://github.com/dhk/minority-report/issues/33)
(routed there per `dhk/alexandria`'s own `CONTRIBUTING.md` — MCP/
orchestration bugs are out of scope for this repo). The "do the deep
research yourself" half produced
[`../03-runs/claude-2026-08-09/`](../03-runs/claude-2026-08-09/).

## Follow-up: the LinkedIn hard constraint (this session)

> Update the Alexandria research repo to require user-supplied LinkedIn
> input.

Following a chat exchange (not reproduced here) working through LinkedIn's
User Agreement, the hiQ Labs v. LinkedIn Ninth Circuit rulings, and the
practical risk gradient between individual and commercial-scale scraping.
Recorded as the hard constraint in `topic.yaml`'s `notes` field and
justified in
[`../05-analysis/analysis.md`](../05-analysis/analysis.md#linkedin-data--legaltos-risk).
