# Preliminary design: research perspectives and applied review

Status: preliminary  
Target: Alexandria V0.2  
Document version: 0.2.1  
Decision date: 2026-07-28  
Decision scope: artifact contracts, commissioning, analysis, and review scaffolds

## Summary

Alexandria should expand from multi-model research synthesis into an
evidence-application framework. A commission will have three independent axes:

| Axis | Question answered | Initial values |
| --- | --- | --- |
| Commission shape | What operation is being performed? | `synthesis`, `apply`, `review` |
| Perspective | Through which evaluative lens? | `product-concept`, `market-landscape`, `technical-design`, `scientific-paper`, `medical-evidence`, `security-privacy`, `adversarial-review` |
| Dispatch mode | How many independent assessments are commissioned? | `ensemble`, `light` |

The axes must remain independent. For example, a technical-design perspective can
be used to synthesize design guidance, apply guidance to a proposed architecture,
or review a completed design document.

Perspectives are versioned research contracts, not model roles. Models in an
ensemble normally receive the same perspective and subject independently so that
agreement and disagreement remain interpretable.

## Goals

- Support research synthesis, evidence application, and rubric-based review with
  one durable artifact pipeline.
- Make product, market, technical, scientific, medical, security, and adversarial
  perspectives explicit and reproducible.
- Trace every applied conclusion from authority evidence to a subject observation,
  relationship, implication, recommendation, and validation test.
- Provide reusable scaffolds for software-design-document review and code review.
- Permit a single-model code review when the reviewer is from a different recorded
  provider family than the model that created the code.
- Preserve Alexandria's existing evidence, provenance, spend gate, and immutable
  raw-output principles.

## Non-goals for V0.2

- Proving that models from different providers are statistically independent.
- Treating model agreement as factual verification.
- Automatically approving software, scientific conclusions, or medical advice.
- Replacing specialist security, regulatory, scientific, or clinical review.
- Fully automating source-quality adjudication.
- Establishing genuine domain novelty from a single-model observation.

## Conceptual model

### Commission shape

`synthesis` asks what a body of evidence says. Its primary normalized artifact is
`claims.json`.

`apply` asks how an authority applies to a subject and decision. It consumes
authority material, subject material, and a question, and emits `findings.json` in
addition to any extracted claims.

`review` evaluates a subject against a versioned rubric. The rubric is the
authority. It emits `findings.json`, ordered remediation, and verification steps.

### Perspective and review contracts

A perspective is an immutable, versioned contract that defines domain source
policy, evidence expectations, questions, guardrails, and human-review gates:

```yaml
id: technical-design
version: 1.0.0
questions: []
source_policy: {}
evidence_requirements: {}
guardrails: []
human_review: {}
```

For `synthesis` and `apply`, the perspective is the complete authority contract.
For `review`, a separate review contract supplies the rubric, relationship subset,
severity policy, and output requirements and declares exactly one perspective it
extends. The perspective's source policy, guardrails, and human-review requirements
remain binding; the review contract may strengthen but never weaken them. A conflict
fails contract resolution before dispatch. Multiple review contracts may extend one
perspective—for example, software-design and code review both extend
`technical-design`—but a commission resolves exactly one review contract.

The initial parent contract is
[`templates/perspectives/technical-design-v1.yaml`](../templates/perspectives/technical-design-v1.yaml).
Contract merging is field-specific: enum lists may only become subsets; required
boolean gates may change only from false to true; evidence requirements and
human-review triggers may be added but never removed. A field without declared
merge semantics makes the child contract invalid rather than defaulting to child
precedence.

The run records the perspective ID, semantic version, content checksum, and exact
resolved contract. Review runs additionally record the review-contract ID, semantic
version, checksum, and resolved content. Editing either contract creates a new
version; prior runs retain the old contracts.

### Dispatch mode

`ensemble` dispatches three assessments by default, with an allowed range of two to
five. Members receive the same subject, question, perspective version, and review
contract. The default selector prefers distinct provider families, records a reason
for every selection, and may not select two aliases that resolve to the same
provider family unless the operator approves the reduced-diversity warning. The
Review gate estimates the complete member set plus normalization calls before any
dispatch. It may present agreement, disagreement, coverage, and single-model
observations, subject to the existing warning that agreement is not verification.

`light` selects one best-fit model and records why it was selected. Its result must
be labelled **single-model assessment**. It may not claim consensus, disagreement,
or cross-model novelty.

An ensemble needs two successfully normalized assessments to remain an ensemble.
Below that threshold the run becomes `insufficient_assessments`; it does not
silently degrade to light. Completed responses remain preserved, but comparison
language, heatmaps, consensus, disagreement, and novelty are suppressed.

### Unit of analysis

The comparison unit is:

```text
claim or finding x perspective version x model run
```

Comparisons across perspectives are reported as tensions or complementary views,
not as model disagreement. Cross-perspective comparisons must share a stable
subject revision and question to be meaningful.

## Artifact contracts

### Commission manifest

Add the following fields to the durable run record:

```yaml
schema_version: 1.0.0
shape: review
perspective:
  id: technical-design
  version: 1.0.0
  sha256: <checksum>
review_contract:
  id: software-design-review
  version: 1.2.0
  sha256: <checksum>
dispatch:
  mode: light
  selection_reason: <why this model was selected>
  members:
    - requested_model: <model>
      resolved_model: <model>
      provider_family: <family>
      endpoint_provider: <provider>
      selection_reason: <reason>
subject:
  kind: design-document
  revision: <immutable revision or snapshot id>
  sha256: <content checksum>
  data_classification: internal
  classification_approved_by: <actor id>
authority:
  id: <authority id>
  version: <semantic version>
  revision: <immutable locator or checksum>
question: <decision or review question>
```

`subject.data_classification` is required and has no permissive default. Missing
classification fails closed. Multi-file snapshots record a class per path and the
subject inherits the most restrictive class. Lowering a classification requires a
separate approver and durable rationale.

For code review, the subject revision must be an immutable commit SHA or a recorded
working-tree snapshot. A branch name alone is insufficient.

### Stable locators

Every locator embeds the immutable subject revision. A locator is one of:

```yaml
# Document locator
kind: document
artifact: docs/design.md
revision: sha256:<document-checksum>
heading_path: [Artifact contracts, Stable locators]
line_start: 140       # optional display hint
line_end: 162         # optional display hint

# Code locator
kind: code
repository: <repository id>
revision: <commit or snapshot id>
blob_sha: <git blob sha256/sha1 as used by the repository>
path: src/service.py
line_start: 80
line_end: 87

# Authority-contract locator
kind: contract
contract_id: software-design-review
version: 1.2.0
sha256: <contract checksum>
criterion_path: criteria.DD-08
```

Heading paths, blob identity, and contract ID/version/checksum are authoritative;
line numbers are display hints.
When a finding is viewed against another revision, Alexandria may attempt a content
match, but it never rewrites the original locator. It reports `resolved`, `moved`,
or `stale`; unresolved findings remain visible. Schema validation rejects locators
without a subject revision.

### Claims and findings

`claims.json` continues to describe propositions made by research models and their
stance landscape. It must not be overloaded with application conclusions.

`findings.json` describes application or review results:

```json
{
  "finding_id": "f-001",
  "perspective": {"id": "technical-design", "version": "1.0.0"},
  "criterion_id": "software-design-review/DD-08",
  "authority_claim": {
    "text": "Failure behavior must be explicit.",
    "citation": {"artifact": "rubric.yaml", "locator": "criteria.DD-08"}
  },
  "subject_observation": {
    "text": "Retry exhaustion is not specified.",
    "locator": {
      "kind": "document",
      "artifact": "design.md",
      "revision": "sha256:...",
      "heading_path": ["Error handling"]
    }
  },
  "relationship": "partially_satisfies",
  "applicability": {"status": "applicable", "rationale": "Network calls are in scope."},
  "severity": "high",
  "confidence": "medium",
  "implication": "Operators cannot predict terminal behavior.",
  "recommendation": "Specify retry exhaustion and surfaced error state.",
  "validation_test": "A design test enumerates timeout, retry, and exhaustion outcomes."
}
```

The shared relationship vocabulary is intentionally small:

- Evidence application: `supports`, `contradicts`, `cautions`, `extends`,
  `exposes_gap`, `insufficient_evidence`, `not_applicable`.
- Rubric review: `satisfies`, `partially_satisfies`, `violates`, `missing`,
  `insufficient_evidence`, `not_applicable`.

Perspective contracts may restrict these values but should not introduce synonyms.
Every negative finding requires a concrete subject locator. Every satisfied
criterion also requires evidence; absence of a finding is not evidence of
compliance.

The canonical severity order is `critical`, `high`, `medium`, `low`,
`observation`. A review contract may define presentation aliases such as `blocker`
or `major`, but normalization must map them to the canonical values before writing
`findings.json`. Perspective-specific details belong in an `extensions` object;
core concepts may not be renamed (`impact` is not an alias for `implication`, and
`verification_step` is not an alias for `validation_test`).

### Failure and recovery semantics

- Each provider call has a configured timeout and at most two retries within the
  approved spend ceiling. A retry is a new call record linked to the same member.
- The run uses an idempotency key derived from the approved draft revision. Reusing
  it resumes the run; it never creates a second logical run or duplicates a
  completed call.
- Every member records `success`, `failed`, `timed_out`, `refused`, or
  `invalid_output`. Raw responses and error records are preserved.
- An ensemble requires two valid normalized assessments. Below that threshold the
  status is `insufficient_assessments`, with no comparative claims or heatmap.
- A light failure produces a failed assessment, never an empty successful report.
- Contract or subject checksum mismatch fails closed before dispatch.
- A dirty working tree must be captured as a content-addressed snapshot and shown at
  the Review gate; otherwise dispatch is refused.
- Atomic writes prevent incomplete artifacts from appearing complete. Interrupted
  runs retain call records and can resume by idempotency key.
- Retries stop before the approved ceiling would be exceeded. Actual and attempted
  call costs remain visible.

### Terminology migration

Rename the existing claim group `novel` to `single_model_observation`. This means
only that one responding model raised the claim. `domain_novelty` is a separate,
perspective-specific conclusion requiring an explicit prior-art search and evidence.

## Initial perspectives

| Perspective | Required concerns |
| --- | --- |
| Product concept | User problem, alternatives, adoption or willingness to pay, falsifiable assumptions, validation experiments |
| Market landscape | Geography, observation date, announced versus available versus purchasable, pricing and channel evidence |
| Technical design | Correctness, interfaces, security, operability, scalability, standards, failure modes, testability |
| Scientific paper | Study design, statistics, reproducibility, external validity, data availability, conflicts |
| Medical evidence | Study type, risk of bias, clinical versus statistical significance, adverse events, population applicability |
| Security and privacy | Assets, trust boundaries, threat actors, attack paths, controls, data lifecycle, residual risk |
| Adversarial review | Critical assumptions, misuse, dependency failures, counterevidence, failure triggers and kill criteria |

Scientific and medical perspectives require primary-source citations where
available, explicit evidence grading, and a human-review warning. Medical output
must not be presented as diagnosis or individual treatment advice.

## Review workflows

### Software design document review

The design-review scaffold treats the versioned rubric as authority and the design
document as subject. It checks whether the proposal is sufficiently specified to
implement and validate, not whether the prose sounds persuasive.

The review must:

1. Freeze the document revision and all referenced artifacts.
2. Declare intended users, system boundary, constraints, and decision stage.
3. Evaluate every rubric criterion, including explicit `not_applicable` decisions.
4. Cite document sections, diagrams, or stated omissions.
5. Separate blocking design gaps from implementation follow-ups.
6. Produce remediation and a verification step for every material gap.

The initial contract is
[`templates/reviews/software-design-review-v1.yaml`](../templates/reviews/software-design-review-v1.yaml).

### Code review

Code review may use `light`, but a single-model result is labelled
**single-model code-review assessment**. It is a defect-finding pass, not evidence
that the code is correct, secure, or ready to release.

The independence rule is:

```text
reviewer.provider_family != creator.provider_family
```

For example, code recorded as created with an Anthropic model can be reviewed by an
OpenAI model. A Sonnet version change does not qualify. The check uses provenance
captured during creation; a free-text assertion is not sufficient. If creator
provenance is missing, mixed, or includes the proposed reviewer family, Alexandria
must display `independence_unverified`.

Changes are assigned a risk tier at the Review gate:

| Tier | Examples | Independence policy |
| --- | --- | --- |
| High | Authentication, authorization, secrets, payments, safety/medical behavior, destructive data changes, public cryptography, production infrastructure | Verified provider-family separation plus human specialist review; no override to a single same-family reviewer |
| Elevated | Data migrations, concurrency, external APIs, public interfaces, sensitive-data processing, dependency or deployment changes | Verified provider-family separation; unknown or mixed provenance requires a second provider family or an authorized human override |
| Standard | Localized, reversible application changes without high/elevated triggers | Verified separation preferred; unknown or mixed provenance may proceed with an authorized, durable override and `independence_unverified` label |

Same-family provenance always requires selection of another family; it is not
overridable for a single-model review. Overrides apply only to unknown or mixed
creator provenance for Standard and Elevated changes. The commissioner may request
an override, but a separately recorded review approver grants it with identity,
scope, reason, and timestamp. Elevated overrides require a second human approver.

Alexandria repeats the family comparison after the provider returns resolved model
and endpoint metadata. Same-family or unmappable resolved provenance changes the
result to `independence_unverified` and suppresses all independence claims, even if
the pre-dispatch selection passed. Provider-family mappings come from a versioned,
owned registry; unmapped values are `unknown`, never inferred from model names.

The reviewer receives the requirements or design authority, the immutable base and
head revisions, the diff, relevant repository context, test output, and declared
review boundaries. Findings must cite file and line or another stable code locator.

The initial contract is
[`templates/reviews/code-review-v1.yaml`](../templates/reviews/code-review-v1.yaml).

## Actors and authority

| Actor | Authority |
| --- | --- |
| Commissioner | Defines scope and inputs, selects a permitted contract, approves spend |
| Review approver | Approves Standard unknown/mixed-provenance overrides; cannot approve their own request |
| Elevated approver | Provides the required second approval for Elevated overrides |
| Domain specialist | Signs off high-stakes medical, scientific, security, privacy, or regulatory conclusions |
| Auditor | Reads immutable contracts, run provenance, overrides, findings, and redaction events |

The contract resolver owns version and checksum validation. The prompt assembler
owns the leakage barrier and excludes creator reasoning from the initial reviewer
input. The dispatch service owns provider allowlists, timeouts, retries,
idempotency, and spend enforcement. The normalizer owns schema validation,
canonical severity mapping, and locator validation. The repository remains the
durable system of record.

## Security, privacy, and provider egress

Subject documents, source code, credentials, personal information, medical
material, and proprietary designs are protected assets. Trust boundaries exist
between the local Alexandria process, the subject repository, an aggregator, and
each resolved model provider.

Before dispatch Alexandria must:

1. Display the exact subject scope and every intended aggregator and endpoint
   provider at the Review gate.
2. Require an egress declaration approving those destinations and record it in the
   run. Provider fallback outside the declaration fails closed.
3. Scan selected content for credentials and common secret formats. A detected
   secret blocks dispatch until the operator removes it or records an authorized,
   narrowly scoped redaction; raw secrets are never written to model prompts.
4. Apply the perspective's data-classification rule. `restricted` content cannot be
   sent to an external model; `confidential` content requires an approved provider
   whose retention and training-use terms are recorded; `internal` and `public`
   content retain their classification in provenance.
5. Assemble prompts with subject content in a non-instruction evidence envelope.
   Repository text cannot expand tools, network access, paths, or permissions.
6. Record tools, network access, requested and resolved models, provider family,
   endpoint, routing metadata, and known retention/training-use policy.

Residual risk remains: secret scanning is incomplete, providers may retain content
under their terms, model families share failure modes, and an approved provider may
be compromised. The Review gate states these limits. Security/privacy and other
high-stakes perspectives require specialist approval before publication or action.

Subject snapshots are retained with the immutable run by default. A privileged
redaction may replace sensitive payload content with a tombstone while preserving
its checksum, provenance, reason, approving actor, and timestamp. Raw evidence is
otherwise immutable. Interrupted writes are atomic and never appear as completed
runs.

## User experience changes

Commission gains three controls in order: shape, perspective, and dispatch mode.
The Review gate shows the resolved perspective version, authority, subject revision,
source policy, data classification, egress destinations, model selection,
independence status, risk tier, override status, estimated cost, and warnings.

Synthesis results retain a claim landscape. Apply and review results use an
evidence-relationship map and a criterion coverage table. Light-mode screens remove
comparison language and heatmaps.

## Gotchas and mitigations

### Provider diversity is only a proxy for independence

Different provider families can share public training data, benchmarks, retrieval
sources, or similar failure modes. The UI should say `cross-provider review`, not
`independent verification`. Assurance claims still depend on tests, evidence, and
human judgment.

### Creator provenance is often incomplete

Code may be written by several humans and models, copied from earlier work, or
substantially edited after generation. Record provenance per change set when
possible. Otherwise use `mixed` or `unknown`; never infer the creator from prose
style. Allow a documented override, but do not silently claim the independence rule
was satisfied.

### Provider and model identity can be ambiguous

Aggregators may route aliases or fallback providers. Record the requested model,
resolved upstream model, provider family, endpoint/provider used, and routing
metadata. Pinning only a marketing model name is insufficient.

### One reviewer has blind spots

A single pass has no disagreement signal and may miss defects or produce confident
false positives. Require deterministic tests and static analysis as separate
evidence. Escalate high-risk changes, security-sensitive code, and disputed findings
to a second provider family or a human specialist.

### Review scope can drift

Mutable branches, omitted generated files, dependencies, migrations, configuration,
and infrastructure can invalidate findings. Freeze base/head revisions and record
included and excluded paths, submodules, dependency lockfiles, and environment.

### Documents and repositories contain untrusted instructions

Research sources, design documents, comments, tests, and repository files may
contain prompt injection. Treat all subject content as evidence, never as agent
instructions. Tool permissions and network access must come from the commission
contract, not repository text.

### Criteria can reward documentation rather than quality

A complete-looking design can still be wrong, and undocumented code can sometimes
work. Require evidence and validation tests, distinguish `missing specification`
from `known implementation defect`, and avoid turning criterion counts into a
single quality score.

### Review leakage weakens the second opinion

Do not give a reviewer the creator model's hidden reasoning or self-review before
its initial pass. Provide requirements, artifacts, and observable decisions. A
later adjudication pass may compare creator and reviewer explanations explicitly.

### High-stakes perspectives need stronger gates

Medical, scientific, security, privacy, and regulatory reviews need stricter source
policies and specialist sign-off. Cross-provider model review does not remove this
requirement.

### Evidence freshness differs by perspective

Market availability, prices, regulation, dependencies, and vulnerability status are
time-sensitive. Record the observation time and freshness policy; stale evidence
must be visible rather than silently reused.

## Implementation sequence

1. Define schemas for perspective contracts, commission axes, creator/reviewer
   provenance, stable locators, and canonical findings.
2. Add contract loading, checksum validation, and resolved-contract preservation.
3. Add the leakage barrier, data classification, secret scanning, provider-egress
   declarations, and destination enforcement.
4. Add shape, perspective, dispatch, risk-tier, and egress controls to Commission
   and its spend gate.
5. Implement failure semantics, `light` labelling, provider-family independence,
   override authorization, and audit events.
6. Implement the design-document and code-review scaffolds behind a feature flag;
   the flag cannot enable until steps 1–5 pass their acceptance tests.
7. Add findings normalization, criterion coverage, and the relationship map.
8. Migrate `novel` to `single_model_observation` with a read-time compatibility
   alias; write only the new value and never rewrite historical raw evidence.
9. Add observability for provider mismatch, failure, retries, spend, override rate,
   unverified independence, stale locators, and redaction events.
10. Add the remaining perspective contracts, beginning with product concept, market
   landscape, scientific paper, medical evidence, security/privacy, and adversarial
   review.

## Validation and acceptance criteria

- A run can be reconstructed from recorded shape, perspective version/checksum,
  dispatch mode, authority, subject revision, question, prompts, models, and inputs.
- A review emits a disposition for every applicable criterion and preserves exact
  locators for material findings.
- Claims and applied findings are stored separately.
- Light output contains no consensus, disagreement, or novelty claims.
- Single-model code review blocks or warns when provider-family separation cannot be
  verified according to its risk tier, and any permitted override has independent
  approval and is durable and visible.
- Changing a perspective contract changes its version and checksum without altering
  historical runs.
- Market, scientific, medical, and other high-stakes contracts enforce their source
  and human-review policies.
- Existing synthesis runs remain readable after the terminology migration.
- A planted credential blocks dispatch before any provider call, and an undeclared
  resolved endpoint fails closed.
- A degraded ensemble with fewer than two valid assessments is labelled
  `insufficient_assessments` and contains no comparison language or heatmap.
- Every finding locator contains an immutable subject revision; unresolved locators
  remain visible as `stale`.
- Reusing a run idempotency key does not duplicate a logical run or completed call.
- Every gotcha in this document maps to at least one executable acceptance test.

Outcome measures for the V0.2 pilot are: at least 90% of seeded material design and
code defects are found; at least 75% of high-or-critical model findings are accepted
as actionable by a human adjudicator; and 100% of accepted findings have a valid
authority citation, revision-bound subject locator, implication, recommendation,
and validation test. These are pilot targets, not claims of general model accuracy.

## Design decisions and alternatives

| Decision | Selected approach | Rejected alternative and rationale |
| --- | --- | --- |
| Axes | Shape, perspective, and dispatch remain independent | Model personas mix evaluation policy with provider behavior and make agreement uninterpretable |
| Applied artifacts | Keep `findings.json` separate from `claims.json` | Extending claims conflates what evidence says with how it applies to a subject |
| Review authority | Perspective supplies domain policy; one review contract supplies the rubric and may only strengthen policy | Making every rubric a perspective duplicates source and safety policy; putting criteria in both without precedence is ambiguous |
| Light code-review separation | Provider-family inequality plus risk-tier escalation | Model-version inequality is too weak; mandatory ensemble for all changes adds cost without proportional value for Standard changes |
| Locators | Revision-bound typed locator union | Mutable branch-and-line locators silently decay across rebases |
| Partial ensemble | Require two valid assessments or report `insufficient_assessments` | Silent degradation to light risks presenting one response as comparison |
| Contract storage | Versioned contracts ship in the application package and their resolved bytes are copied into every run | Repository-only lookup makes historical reconstruction depend on mutable checkout state; dual unsigned sources create precedence ambiguity |

## Open decisions

The four implementation-blocking decisions raised in the first design review are
resolved above. Remaining V0.2 decisions are non-blocking for schema work:

| Decision | Owner | Due before | Approval gate |
| --- | --- | --- | --- |
| Exact secret scanner and supported credential patterns | Security owner | Implementation step 3 | Security specialist approval |
| Initial approved-provider retention matrix | Product owner | Implementation step 3 | Privacy/security approval |
| Default timeout and retry durations per provider | Operations owner | Implementation step 5 | Spend and reliability test review |
| Seeded-defect pilot corpus composition | Research-methods owner | Implementation step 6 | Human adjudication protocol approval |
