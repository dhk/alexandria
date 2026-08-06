# Research perspectives preliminary design re-review

Status: completed  
Assessment: cross-provider single-model design-review assessment  
Disposition: `ready_with_conditions`

This is not independent verification, consensus, or specialist security/privacy
approval.

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
| Cost | $0.66147425 |

## Frozen inputs and output

| Artifact | SHA-256 |
| --- | --- |
| `docs/PRELIMINARY-RESEARCH-PERSPECTIVES.md` v0.2.0 | `57e91d869c52956388d665de91c7a1024d50305fb82e1632ddd5175575ac5f63` |
| `templates/reviews/software-design-review-v1.yaml` v1.1.0 | `a8a1164948c08e88ffc01d044ce5a8b74c85edcade58d4ff38fc07c5e088f0d1` |
| Preserved re-review response | `93cad311878d4efececc3242037f012670bca67d238689c2ac075b1eaec15ed1` |

The exact provider response and usage metadata are preserved in
[`2026-07-28-research-perspectives-opus-rereview-raw.json`](2026-07-28-research-perspectives-opus-rereview-raw.json).

## Prior-blocker result

| Prior blocker | Result |
| --- | --- |
| Independence enforcement | Resolved in policy; post-resolution enforcement remains a condition |
| Stable locators | Resolved; add a typed authority-contract locator |
| Provider egress and security | Resolved in policy; classification must become a required fail-closed input |
| Failure and degradation | Resolved; retry detail remains implementation work |

## Conditions before external dispatch

1. Author and pin the `technical-design` parent perspective contract; review
   contracts must name its ID and version.
2. Re-evaluate provider-family separation after the actual reviewer model and
   endpoint resolve. A mismatch or unknown family becomes
   `independence_unverified` and suppresses independence claims.
3. Add required `subject.data_classification`, fail closed when absent, prevent
   external dispatch for `restricted`, and require authorization to lower a class.

These conditions do not block schema and contract work. They block sending real
subjects to external providers.

## Important follow-ups

- Define how a review contract may strengthen but not weaken a perspective.
- Add a workflow and acceptance criteria for the `apply` shape.
- Add a typed, revision-bound authority-contract locator.
- Specify retention and erasure policy for subject snapshots.
- Complete retryability, backoff, member replacement, and normalizer failure rules.
- Add a nonce so the same approved draft can intentionally create a fresh run.
- Add incident response and default cost/time ceilings.
- Pin every referenced contract and define migration rollback.
- Decide whether design-document review uses creator/reviewer family separation.

The next implementation gate is to close the three dispatch conditions above and
obtain specialist human security/privacy review before enabling real provider
dispatch.
