# Research perspectives preliminary design review

Status: completed  
Assessment: cross-provider single-model design-review assessment  
Disposition: `revise_and_re_review`

This is a defect-finding assessment, not independent verification, consensus, or
approval to implement.

## Provenance

| Field | Value |
| --- | --- |
| Review date | 2026-07-28 |
| Creator provider family | OpenAI |
| Reviewer provider family | Anthropic |
| Requested reviewer | `opus` |
| Resolved reviewer | `claude-opus-5` |
| Dispatch path | Claude Code, first-party Anthropic provider |
| Tools | Read only |
| Repository customizations | Disabled with safe mode |
| Session persistence | Disabled |
| First-pass cost | $0.661106 |
| Preserved concise-pass cost | $0.53153375 |
| Total review cost | $1.19263975 |

The user explicitly approved sending the subject and authority contract to
Anthropic. No other repository content was authorized as subject material.

## Frozen input checksums

| Artifact | SHA-256 |
| --- | --- |
| `docs/PRELIMINARY-RESEARCH-PERSPECTIVES.md` | `59ce940a6a694c544568068a455c071ddf4b1fa4c8afea31d71fc2d0a3371680` |
| `templates/reviews/software-design-review-v1.yaml` | `5a79d949530d001c9eb78b4b2c1c7db7a88b3ee9b42149b72d63dde8d48eb51a` |
| Preserved raw response | `ff162810dd2ef68665de537ca470236581d67d19b2fe335d2dc57f0722b7b5b4` |

The raw concise review response, including provider usage and cost metadata, is
preserved in
[`2026-07-28-research-perspectives-opus-raw.json`](2026-07-28-research-perspectives-opus-raw.json).
The earlier, longer pass returned before its response was durably captured; its
cost and top-level conclusions are recorded here, but it is not treated as durable
raw evidence.

## Blocking findings

1. **B-01 — Independence enforcement is undecided.** The design does not choose
   whether missing or same-family provenance blocks, warns, or escalates, and does
   not define code risk tiers.
2. **B-02 — Stable locator representation is undecided.** Findings require durable
   document and code locators, but no locator union or stale-locator behavior is
   specified.
3. **B-03 — Third-party data egress is uncontrolled.** The design lacks asset and
   trust-boundary analysis, secret scanning, provider egress disclosure, retention
   controls, and an approved-provider rule.
4. **B-04 — Failure behavior is absent.** Timeouts, retries, partial ensembles,
   relabelling, idempotency, checksum failure, and spend behavior are unspecified.

## Material non-blocking findings

- Major decisions lack alternatives and recorded rationale.
- Components, ownership, and data flow are not specified.
- Retention, redaction, deletion, and recovery are not specified.
- Operability and safety-control metrics are absent.
- Acceptance criteria test artifact shape but not finding usefulness or false
  positives.
- Actors, permissions, and the system boundary are not declared.
- Requirements are not traceable to acceptance criteria and implementation steps.
- Durable artifact schema versioning and migration rollback are incomplete.
- Version and criterion-ID formats are inconsistent.
- Open decisions lack owners and implementation gates.

## Remediation order

1. Resolve independence enforcement, risk tiers, override authority, and owners.
2. Add security/privacy boundaries, provider-egress disclosure, secret scanning,
   and specialist gates.
3. Define revision-bound document and code locator schemas plus staleness behavior.
4. Define timeouts, retries, partial failure, relabelling, idempotency, spend
   accounting, and rollback.
5. Add actors, permissions, component ownership, and the commission data flow.
6. Add decision records and requirements traceability.
7. Add outcome measures, retention/redaction, and artifact schema versions.
8. Add operability requirements and normalize format conventions.

After items 1–4 are incorporated, the design should receive another review using
the same frozen-contract procedure before implementation begins.
