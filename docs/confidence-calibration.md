# Confidence Calibration Spec — Claim Agreement Score

**Status:** Draft v1
**Owner:** Dave Holmes-Kinsella
**Last updated:** July 27, 2026
**Depends on:** [Orchestration Harness Design](./orchestration-harness.md), §9–10

---

## 1. Purpose & scope

This spec answers the open question left in the harness design: exactly how the signed integer **−3 to +3** score in `claim_scores.score` is derived from a research model's raw output, so that the value is reproducible, auditable, and traceable to a specific span of text — not a holistic vibe. The scale is normative in [`schemas/claim-score.schema.json`](../schemas/claim-score.schema.json).

## 2. What the score means

For a given `(claim, model)` pair:

| Score | Meaning |
|---|---|
| +3 | Strong support: the model states the claim directly and without hedging |
| +2 | Moderate support: qualified, partial, or conditional |
| +1 | Weak support: implied, passing, or heavily hedged |
| 0 | Graded-silent: the model responded but made no statement bearing on the claim |
| −1 | Weak contradiction: implied, passing, or heavily hedged |
| −2 | Moderate contradiction: qualified, partial, or conditional |
| −3 | Strong contradiction: direct and unhedged |

The score is a **derived integer**, not something an LLM is asked to output directly. Direct numeric self-rating from LLMs is a known source of miscalibration — models tend to be systematically overconfident and inconsistent across phrasings of the same request. Instead, the pipeline below produces the score deterministically from two categorical judgments plus a required evidence quote.

## 3. Two-stage pipeline

Claim identity and claim scoring are deliberately separated into two passes, so a change in one doesn't silently corrupt the other.

### 3.1 Extraction (upstream, unchanged from the harness design)

The synthesis call reads the union of all research models' raw outputs and produces a deduplicated canonical claim list (`claim_id`, `claim_text`). Extraction is intentionally permissive: if even one model treats something as a distinct claim, it gets its own `claim_id` — novelty is signal, not noise to be merged away. This stage is unchanged from §9 of the harness design and is not re-litigated here.

### 3.2 Grading (new — this spec's subject)

One grading call per **research model** (not per claim, and not per claim-model pair) — i.e. 3–4 calls total per run, matching your model count, not multiplying against the claim count.

Each grading call receives:
- the full canonical claim list from §3.1
- that one model's complete raw output, and *only that model's output* (no cross-contamination from other sources, no visibility into what other models said)

And returns, for every claim in the list, a `(stance, strength, evidence_quote)` triple — never a bare number.

This keeps grading blind and independent per source (avoiding anchoring on other models' framing) while keeping the call count linear in model count rather than quadratic in claim count.

## 4. Stance + strength rubric

**Stance** ∈ `{supports, disputes, silent}` — is the model's output can be found to bear on the claim, and in which direction.

**Strength** ∈ `{strong, moderate, weak}` — assigned only when stance ≠ silent, based on explicit linguistic markers:

| Strength | Markers |
|---|---|
| Strong | Unqualified assertion; no hedging language; often accompanied by explicit evidence/reasoning in the source text |
| Moderate | Qualified language ("generally," "in most cases," "likely") or the claim is supported/disputed only in part or under stated conditions |
| Weak | Passing, incidental, or heavily hedged mention; the claim is touched on but not a focal point of the model's output |

**Deterministic mapping** (stance, strength) → numeric score:

| Stance | Strong | Moderate | Weak |
|---|---|---|---|
| Supports | +3 | +2 | +1 |
| Silent | — | — | 0 |
| Disputes | −3 | −2 | −1 |

The grader outputs only the categorical pair; the integer score is computed by a fixed lookup, not by the model. This makes the mapping auditable. A later mapping change would require a new score-contract version, but the stored categorical labels allow derived scores to be recomputed without re-running model calls.

## 5. Evidence requirement (the silent/non-silent boundary)

A stance other than `silent` requires a directly quotable span from the model's raw output that a human reviewer can locate verbatim. This is the operational test for silence, removing ambiguity about implicit inference:

- **If a quotable span exists** that bears on the claim → classify stance + strength from it, and store the quote.
- **If no quotable span exists** → `stance = silent`, `score = 0`, `evidence_quote = null`.

The grader is explicitly instructed not to infer a stance the model never stated, even if it seems logically implied. This matches the repository's provenance-first principle: every non-zero score must be traceable to specific source text, not to the grader's own reasoning about what the model "must have meant."

A failed research call is not graded because no output exists. Its claim/model row carries `score = null`, with no stance, strength, quote, or grader call. This missing observation renders as `✕`; it must never be coerced to `0`, which would fabricate graded silence.

## 6. Grader model and configuration

Grading is a bounded classification task, not creative synthesis, so it doesn't need a flagship-tier model. Add a fourth config slot alongside the existing ones:

```yaml
research_models: [...]      # unchanged
synthesis_model: {...}      # unchanged
grader_model:
  provider: openai
  model: openai/gpt-5.4-mini
  temperature: 0
```

Running the grader at temperature 0 (or the lowest available setting) is required for reproducibility — the same run's raw outputs should produce the same grading result if re-run.

## 7. Reliability check (not per-run, periodic)

Per-run re-grading for consistency would double grading cost for no benefit on a healthy system. Instead: periodically (e.g., monthly, or after changing the grader model/prompt) re-run grading on a small sample of past runs and diff the categorical outputs against the stored ones. A calibration health-check, not a per-run gate.

**Known limitation to flag, not solve now:** a single grader model has its own biases — it may systematically read certain phrasing styles (e.g., a particular provider's characteristic hedging language) as weaker or stronger than another model's equivalent statement. Cross-checking with a second, different grader model is the natural mitigation, but adds cost proportional to model count again — worth revisiting only if the visualization output is ever found to systematically favor or penalize a specific provider's writing style.

## 8. Schema changes to the harness design

Extends §8 of the harness design doc. `claim_scores` gains the categorical/evidentiary columns; `model_calls.role` gains a `grading` value so grading calls are logged exactly like research and synthesis calls (cost, tokens, generation ID, latency — all preserved).

```sql
CREATE TABLE claim_scores (
    claim_id        TEXT NOT NULL REFERENCES claims(claim_id),
    model_id        TEXT NOT NULL,           -- the research model being graded
    stance          TEXT CHECK (stance IN ('supports','disputes','silent')),  -- null when call failed
    strength        TEXT CHECK (strength IN ('strong','moderate','weak')),  -- null when silent
    score           INTEGER,                 -- derived via §4; null only when the research call failed
    evidence_quote  TEXT,                    -- null when silent
    grader_call_id  TEXT REFERENCES model_calls(call_id),  -- which grading call produced this row
    PRIMARY KEY (claim_id, model_id)
);

-- model_calls.role CHECK constraint updated to:
-- CHECK (role IN ('research','synthesis','grading'))
```

## 9. Worked example

Claim: *"Migration cost estimate under $50k."*

Grading Model A's raw output → finds: *"Based on comparable migrations, total cost should land between $35,000 and $45,000."* → `stance=supports`, `strength=strong` (unqualified range, under $50k) → `score = +3`.

Grading Model B's raw output → finds: *"Cost could exceed $50k if the legacy schema requires custom tooling, which seems plausible given the described constraints."* → `stance=disputes`, `strength=moderate` (conditional, hedged) → `score = −2`.

Grading Model C's raw output → no quotable span bearing on migration cost anywhere in the text → `stance=silent` → `score = 0`.

This single claim's row now reads strong support under Model A, moderate contradiction under Model B, and graded silence under Model C — a disagreement pattern, with both underlying quotes stored and reviewable, not just inferred.
