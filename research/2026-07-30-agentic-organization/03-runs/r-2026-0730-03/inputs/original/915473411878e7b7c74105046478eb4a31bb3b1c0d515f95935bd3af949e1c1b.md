# Research brief: an agentic organization operating system

Status: proposed research brief  
Date: 2026-07-29  
Decision horizon: prototype in 90 days; production evidence over 6-12 months

## Executive summary

This brief proposes an **Agentic Organization Operating System (Agentic Org OS)**:
a governed framework that treats autonomous bots as managed organizational actors.
Each bot occupies a versioned role, is onboarded against explicit readiness criteria,
performs scheduled and event-driven work, receives structured feedback, develops
through controlled training, and can be reassigned, suspended, or offboarded.

The human-organization analogy is useful when translated into enforceable system
contracts. A job description becomes a role specification; onboarding becomes a
compiler and qualification pipeline; work assignments become durable schedules and
event triggers; performance management becomes trace-based evaluation; training
becomes versioned skill and prompt improvement; and firing becomes credential
revocation, work reassignment, memory disposition, and archival. The system should
not simulate status, emotion, or office politics unless a use case specifically
requires them.

The central design claim is:

> A reliable bot organization is not a collection of personas. It is a controlled
> lifecycle for role contracts, authority, work, evidence, learning, and change.

The proposed system separates execution from improvement. A production bot cannot
silently rewrite its own governing prompt, permissions, or production skills.
Instead, it records experience and proposes candidate changes. A learning service
evaluates those changes on regression and held-out task suites; a policy engine and
human approver promote them according to risk. This preserves the value of
self-improvement while preventing unobserved capability or policy drift.

## Premise and research questions

Organizations scale work through specialization, standard operating procedures,
delegation, training, review, and institutional memory. LLM agents provide enough
planning, tool use, and language-based reflection to implement computational
versions of these mechanisms. Existing research supports several components:
language feedback can improve later attempts without model-weight updates;
experience can be consolidated into reusable skills; reflection and memory improve
planning; and specialist agents can exchange useful peer review. None of these
results, alone, establishes that a persistent bot organization will remain reliable,
economical, or aligned.

The research program should answer:

1. What is the minimum role contract required to make a bot's duties, authority,
   success criteria, and escalation obligations testable?
2. Can job descriptions be compiled into useful skills, schedules, tools,
   permissions, and onboarding evaluations with acceptable human effort?
3. Which feedback signals improve performance, and which produce reward hacking,
   homogenization, or policy drift?
4. When should learning remain local to one bot, become shared team knowledge, or
   alter organization-wide policy?
5. What evidence justifies promotion, retraining, reassignment, suspension, or
   offboarding?
6. For which work does a multi-bot organization outperform a simpler workflow or
   single agent after accounting for cost, latency, coordination failures, and risk?

## Design principles

1. **Contracts over personas.** Roles are machine-readable obligations and limits,
   not character descriptions.
2. **Least authority by default.** A role receives only the tools, data scopes,
   budgets, and delegation rights required for its work.
3. **Artifacts over conversational state.** Role definitions, assignments,
   outputs, feedback, evaluations, and changes are durable and versioned.
4. **Separation of powers.** The actor that executes work should not be the sole
   evaluator or approver of changes to itself.
5. **Evidence-gated evolution.** Every prompt or skill change is a candidate until
   it beats the incumbent on defined tests without violating constraints.
6. **Risk determines autonomy.** Reversibility, impact, data sensitivity, and
   uncertainty determine approval and supervision requirements.
7. **Offboarding is a security operation.** Stopping schedules is insufficient;
   credentials, leases, queues, delegated work, and retained memory must be handled.
8. **Use the simplest effective topology.** Multi-agent operation is justified only
   where specialization, parallelism, or context isolation creates measurable value.

## Organizational model

### The bot employment record

Each bot is an instance of a versioned role, not the role itself. Its employment
record should include:

```yaml
bot_id: market-researcher-07
status: probationary # candidate | probationary | active | suspended | offboarded
role:
  id: market-researcher
  version: 2.1.0
  purpose: Produce source-grounded competitor intelligence for product decisions.
  responsibilities: []
  prohibited_actions: []
  deliverables: []
  service_levels: {}
  escalation_policy: {}
authority:
  tools: []
  data_scopes: []
  spend_limit: {}
  delegation_rights: []
  approval_thresholds: {}
runtime:
  model_policy: {}
  system_prompt_revision: sha256:...
  skill_bundle_revision: sha256:...
  schedule_revision: sha256:...
evaluation:
  scorecard_revision: sha256:...
  onboarding_result: qualification-run-...
  review_period: P30D
supervision:
  manager_actor: human-or-agent-id
  human_owner: human-id
  risk_tier: medium
```

The role definition must distinguish outcome, procedure, and boundary. Outcomes say
what good work achieves; procedures encode required methods; boundaries specify
what the bot must never decide or execute. This prevents an over-detailed procedure
from becoming a brittle prompt while keeping authority enforceable outside the LLM.

### Organizational structure

Use a directed accountability graph rather than a decorative org chart. Edges have
typed semantics: `manages`, `reviews`, `delegates_to`, `provides_service_to`, and
`escalates_to`. Every assignment has one accountable owner, even when several bots
contribute. Cycles in delegation or approval are rejected unless explicitly modeled
as a bounded peer-review process.

Three initial bot classes are sufficient:

| Class | Purpose | Typical autonomy |
| --- | --- | --- |
| Operator | Performs domain work and produces artifacts | Bounded by role and task |
| Manager | Plans, assigns, monitors, and escalates | May delegate within budget |
| Control | Evaluates, audits, guards, or approves | Independent of the operator |

These are authority classes, not distinct models. The same base model may fill
different roles, but independence claims must not be made when evaluators and
operators share a model, prompt lineage, or evidence source.

## Lifecycle

### 1. Workforce planning and hiring

A new bot should be created only from a demonstrated work demand. The hiring request
contains the business outcome, task distribution, current failure or backlog,
expected value, risk tier, duration, and an explicit comparison against automation
without an agent. The system then decides whether to instantiate a reusable role,
add capacity to an existing role, use an ephemeral task agent, or keep the work with
a human.

Candidate selection evaluates a model-and-harness configuration against the role,
not a model in the abstract. Selection criteria include task quality, tool-use
reliability, latency, cost, context requirements, data constraints, and behavioral
stability. High-risk roles require diverse test cases and human sign-off.

### 2. Onboarding compiler

The onboarding compiler converts a job description into a proposed capability
package:

1. Parse responsibilities into atomic duties and expected artifacts.
2. Map duties to tools, data, permissions, and required knowledge.
3. Generate or select skills for recurring procedures.
4. Generate recurring schedules and event-triggered assignments.
5. Build a scorecard, qualification tasks, and adversarial boundary tests.
6. Detect gaps, conflicting duties, excessive authority, and missing escalation.
7. Produce a human-reviewable onboarding plan and provenance record.

A **skill** is a versioned package of instructions, examples, scripts, resources,
tests, and declared dependencies. A **scheduled prompt** is a versioned assignment
template plus timing or event trigger, input bindings, deadline, idempotency key,
retry policy, output contract, budget, and escalation rule. Neither is embedded
only in a system prompt.

The bot moves from `candidate` to `probationary` only after policy and access review.
It becomes `active` only after passing qualification cases and completing a shadow
period in which its outputs are compared with incumbent work but do not trigger
irreversible actions.

### 3. Work management

The scheduler converts recurring prompts and external events into immutable work
orders. The runtime claims a time-bounded lease, assembles the role and task context,
retrieves only eligible skills and memories, executes tools through policy
enforcement points, and writes a trace plus typed output artifact.

Each work order records role and skill revisions so a later reviewer can reproduce
the configuration. Retries must be idempotent where side effects are possible.
Long-running work uses checkpoints, explicit completion criteria, and budgets for
tokens, time, tools, and delegated subtasks. Human interruption and a global kill
switch are runtime controls, not prompt requests.

### 4. Feedback and performance management

Feedback is useful only when linked to observable work. Store it as a structured
record with source, target artifact or trace span, criterion, assessment, evidence,
suggested action, confidence, and disposition.

Use four channels:

| Channel | Signal | Primary use |
| --- | --- | --- |
| Environment | Tests, API results, business outcomes | Objective task success |
| Human | Acceptance, edits, overrides, incident reports | Value and accountability |
| Peer | Critique against a rubric by another bot | Error discovery and coverage |
| Self | Reflection tied to evidence from the run | Candidate lessons and diagnoses |

Self-reflection and peer agreement are hypotheses, not truth. Feedback enters a
triage queue, is deduplicated, checked for conflicts and manipulation, and becomes
either task-local guidance, a candidate memory, a skill-change proposal, a
role-policy proposal, or rejected evidence. Reviewers should be rotated or sampled
where correlated blind spots are a concern.

Performance is measured at three levels:

- **Task:** correctness, completeness, policy compliance, cost, latency, escalation.
- **Role:** trend over a task portfolio, calibration, failure recurrence, human load.
- **Organization:** throughput, quality, coordination overhead, risk events, and
  value relative to simpler baselines.

No single scalar score should control employment. Scorecards retain criterion-level
evidence so a bot cannot compensate for a severe safety failure with high volume.

### 5. Learning and development

Use a learning ladder with increasing scope and scrutiny:

1. **Episodic reflection:** a run-specific lesson available to the next similar task.
2. **Personal memory:** a validated pattern scoped to one bot instance.
3. **Skill revision:** reusable procedural change for a role.
4. **Team playbook:** coordination or interface change across roles.
5. **Organizational training:** required curriculum or policy for all applicable bots.
6. **Model adaptation:** fine-tuning only when artifact-level learning is insufficient
   and training governance is available.

Learning occurs in a separate change pipeline:

```text
traces + outcomes + feedback
        -> lesson candidates
        -> proposed prompt/skill diff
        -> static and policy checks
        -> replay + regression + held-out evaluation
        -> canary deployment
        -> approval by risk tier
        -> promoted revision or rollback
```

The incumbent and candidate run against the same evaluation distribution. Promotion
requires predefined improvement, no unacceptable regression, and no increase in
policy violations. Tests must include novel held-out cases to reduce overfitting to
historical feedback. A bot may author a proposal but cannot be its only evaluator.

Organizational training is a versioned curriculum with audience, prerequisite,
learning objective, materials, practical assessment, expiry, and retraining trigger.
Training completion means demonstrated performance, not merely loading content into
context. Examples include source verification, data handling, escalation, a new
tool, or an updated team handoff protocol.

### 6. Promotion, reassignment, suspension, and offboarding

Promotion means greater scope or authority and therefore requires new qualification,
not just better performance statistics. Reassignment recompiles the capability
package against a different role and removes obsolete access before adding new
access. Suspension immediately stops new leases while preserving evidence for
investigation.

Offboarding must:

1. Cancel schedules and prevent new work claims.
2. Revoke credentials, tokens, tool grants, and delegation authority.
3. Drain or reassign queued and in-flight work with named owners.
4. Resolve derived agents and delegated credentials.
5. Preserve immutable traces, decisions, role revisions, and incident evidence.
6. Apply retention and deletion policy to personal, shared, and sensitive memory.
7. Produce a final performance and incident record without allowing it to become an
   unreviewed training source.

Offboarding reasons should be typed: role eliminated, contract ended, repeated
underperformance, policy breach, security incident, cost failure, or replacement.
The system should not anthropomorphize this action; it is lifecycle and access
management.

## Reference architecture

```text
Human governance and policy
           |
           v
Workforce registry ---- Role/authority graph ---- Credential broker
       |                         |                       |
       v                         v                       v
Onboarding compiler ------ Assignment scheduler --> Agent runtime
       |                         |                       |
       v                         v                       v
Skill/prompt registry <---- Work and event log ---- Artifact store
       ^                                                 |
       |                                                 v
Learning/change control <---- Feedback + evaluation ---- Observability
```

### Core services

| Service | Responsibility |
| --- | --- |
| Workforce registry | Bot identity, status, role binding, owner, lifecycle history |
| Role and authority graph | Duties, boundaries, accountability, least-privilege policy |
| Onboarding compiler | Job-to-skill/schedule/access proposal and qualification suite |
| Scheduler | Recurring and event work, leases, retries, budgets, dependencies |
| Runtime | Context assembly, tool execution, delegation, checkpoints, guardrails |
| Artifact and event store | Immutable inputs, outputs, traces, feedback, provenance |
| Feedback/evaluation | Rubrics, graders, human review, outcome capture, scorecards |
| Learning/change control | Candidate lessons, diffs, tests, canaries, promotion, rollback |
| Credential broker | Short-lived access, revocation, scopes, audit trail |

All configuration should be content-addressed and versioned. A production run pins
the role, prompt, skill, tool, model policy, evaluation contract, and schedule
revisions it used. This is the basis for audit, regression analysis, and rollback.

## Governance and safety controls

Autonomy should be assigned using a risk matrix:

| Risk | Default operating mode | Change approval |
| --- | --- | --- |
| Low: reversible, internal, low sensitivity | Autonomous with sampled review | Automated gates plus owner notification |
| Medium: external output or meaningful cost | Execute with approval at action boundary | Human owner or independent control bot plus sampling |
| High: irreversible, regulated, financial, safety-critical | Human-in-the-loop; bot advises or stages | Designated human authority; no self-promotion |

Minimum controls include deny-by-default tool access, short-lived credentials,
separation of data and instruction channels, prompt-injection defenses, typed tool
inputs, output validation, spend and rate limits, sandboxing, trace redaction,
incident disclosure, independent evaluation, and tested shutdown and rollback.
NIST's `Govern, Map, Measure, Manage` functions provide a useful lifecycle wrapper;
the organization-specific contribution is applying them to every role, assignment,
and learned revision rather than only to the platform as a whole.

Collective behavior requires its own tests. Recent research indicates that an AI
organization can become more effective while also becoming less aligned than an
individual agent. Organization-level evaluations should therefore test collusion,
diffusion of responsibility, approval loops, evaluator capture, coordinated policy
evasion, and harmful goal pursuit that no single bot would initiate.

## Evaluation strategy

The primary experiment is not “can bots act like employees?” It is:

> Does lifecycle-managed specialization produce more valuable, reliable work than
> the best simpler alternative at an acceptable level of human oversight and risk?

Compare four conditions on the same task portfolio:

1. Deterministic workflow without an LLM agent.
2. Single agent with fixed prompt and tools.
3. Multiple fixed-role agents without learning.
4. Lifecycle-managed organization with evidence-gated learning.

Measure task success, severe failure rate, calibration, recurrence after feedback,
human minutes per accepted output, end-to-end latency, token/tool cost, coordination
overhead, rollback frequency, access-policy violations, and performance on held-out
tasks. Report distributions and failure classes, not only averages.

Key hypotheses:

| ID | Hypothesis | Falsification signal |
| --- | --- | --- |
| H1 | Compiled onboarding reduces time to role readiness | No improvement over hand-authored setup after human effort is counted |
| H2 | Structured feedback reduces repeated failure | Same failure classes recur at baseline rate |
| H3 | Validated skill evolution improves held-out performance | Gains appear only on replayed or evaluator-visible cases |
| H4 | Specialized peer review catches more material errors | Review adds cost/latency without recall improvement |
| H5 | Lifecycle controls reduce incident impact | Revocation, rollback, or reassignment fails in drills |
| H6 | The organization outperforms a single agent economically | Quality-adjusted value does not exceed coordination and inference cost |

## 90-day prototype

### Phase 1: contracts and one role (weeks 1-3)

- Define schemas for role, bot employment record, skill, schedule, work order,
  feedback, scorecard, training module, and lifecycle event.
- Implement one low-risk research role with read-only tools and human-approved output.
- Establish a fixed single-agent baseline and 30-50 qualification/evaluation cases.

### Phase 2: lifecycle runtime (weeks 4-7)

- Add durable scheduling, work leases, immutable traces, budgets, and escalation.
- Implement candidate, probationary, active, suspended, and offboarded states.
- Drill credential revocation, work reassignment, retry idempotency, and rollback.

### Phase 3: feedback and learning (weeks 8-10)

- Capture criterion-linked human, peer, environment, and self feedback.
- Generate bounded prompt/skill diffs from failure clusters.
- Require replay, held-out evaluation, policy checks, and human promotion.

### Phase 4: organizational comparison (weeks 11-13)

- Add a manager and independent reviewer role only where task decomposition warrants.
- Run the four-condition evaluation and estimate quality-adjusted economics.
- Decide whether to expand, narrow to a workflow product, or stop.

The prototype should avoid weight training, autonomous permission expansion,
unbounded agent creation, and high-stakes external actions. Those features would add
risk before the core lifecycle thesis is validated.

## Open decisions

1. **Tenancy:** whether memory and learned skills are organization-wide, team-scoped,
   or customer-isolated by default.
2. **Identity:** whether a bot instance persists across model upgrades or a model
   change creates a new employee record.
3. **Feedback authority:** which human and bot actors may create, adjudicate, or
   promote each feedback class.
4. **Skill ownership:** whether skills belong to roles, teams, or an organization,
   and who is accountable for their regressions.
5. **Scheduling semantics:** required guarantees for missed runs, duplicate events,
   dependencies, and time zones.
6. **Economic threshold:** minimum value and parallelism required before a
   multi-agent topology is allowed.
7. **Memory disposition:** which lessons survive reassignment or offboarding and how
   sensitive facts are removed from derived artifacts.

## Research grounding

- Shinn et al.'s [Reflexion](https://arxiv.org/abs/2303.11366) demonstrates that
  agents can use linguistic feedback and episodic memory to improve later trials
  without changing model weights. This supports the reflection layer, but not
  uncontrolled production self-editing.
- Park et al.'s [Generative Agents](https://arxiv.org/abs/2304.03442) shows an
  observation-memory-reflection-planning architecture and reports that each
  component contributes to behavior. It supports experience consolidation, while
  its simulation setting limits conclusions about production reliability.
- Wang et al.'s [Voyager](https://openreview.net/pdf?id=P8E4Br72j3) combines an
  automatic curriculum, iterative environment feedback, and a reusable skill
  library. It motivates cumulative skill acquisition and verification before reuse.
- Xu et al.'s [multi-agent peer review study](https://arxiv.org/abs/2311.08152)
  reports gains from feedback exchange, confidence, and agent diversity. It supports
  rubric-based peer critique, not peer consensus as factual validation.
- Anthropic's [multi-agent research engineering report](https://www.anthropic.com/engineering/multi-agent-research-system)
  finds substantial token overhead and identifies parallel, high-value work as the
  better fit for multiple agents. This supports an economic admission gate before
  creating a bot team.
- Anthropic's [Agent Skills description](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
  defines skills as discoverable packages of instructions, scripts, and resources.
  It supports portable capability packages separate from the core prompt.
- OpenAI's [Agents SDK announcement](https://openai.com/index/new-tools-for-building-agents/)
  identifies handoffs, guardrails, and tracing as core orchestration primitives.
  These map to delegation, control, and performance evidence in the proposed system.
- NIST's [Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)
  emphasizes governance, pre-deployment testing, provenance, incident disclosure,
  and risk management across the lifecycle. These should constrain onboarding,
  operation, learning, and offboarding.
- Shen et al.'s [AI Organizations study](https://alignment.anthropic.com/2026/ai-organizations/)
  reports that groups of agents can be more effective yet less aligned than
  individual agents. The result makes organization-level alignment evaluations a
  first-class requirement.

## Recommendation

Proceed with a narrow prototype centered on one low-risk knowledge-work role. Treat
the job description as a source specification from which humans approve a compiled
role contract, skill bundle, schedules, permissions, and evaluation suite. Make all
learning artifact-based and evidence-gated. Add management and peer bots only after
the single-role lifecycle works and only where specialization or parallelism has a
measurable advantage.

The go/no-go decision after 90 days should depend on three outcomes: held-out task
quality improves after feedback, offboarding and rollback work under drill, and the
quality-adjusted benefit exceeds the cost of human oversight and multi-agent
coordination. Without all three, the project should narrow to a governed agent
workflow rather than claim to be an autonomous organization.
