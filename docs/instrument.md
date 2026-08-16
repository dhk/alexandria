# Instrument record

**Status:** Normative
**Depends on:** [Confidence calibration](confidence-calibration.md),
[`schemas/run-record.schema.json`](../schemas/run-record.schema.json)

---

## 1. Why a run must state its apparatus

Alexandria's premise is that model agreement is not verification, and that the
way to see through it is to dispatch models independently and score them blind.
The claim landscape — `claims.json` and `scores.csv` — is where that premise
either holds or fails.

So a claim landscape is a *measurement*, and a measurement is uninterpretable
without knowing the instrument that produced it. Two runs with identical group
counts are not comparable evidence if one was graded per-model-blind and the
other by a single pass that read every output first. Nothing in the corpus
recorded that distinction until now, which meant every run's counts read as
though they came from the same apparatus.

The `instrument` block on each run record fixes that. It is required by
[`run-record.schema.json`](../schemas/run-record.schema.json); a run record
without one does not validate.

## 2. The four fields

| Field | Values | Meaning |
|---|---|---|
| `spec_version` | `confidence-calibration/draft-v1` | Which spec revision this run is measured against |
| `grader_topology` | `per-model-blind` · `single-call-all-models` | How grading calls were partitioned across research outputs |
| `score_derivation` | `derived-lookup` · `model-assigned` | How the signed integer in `scores.csv` was produced |
| `extraction_pass` | `separate` · `fused` | Whether claim identity was fixed before claim scoring |

The first value listed for each field is the one the spec requires.

**`grader_topology`** is the load-bearing one. `per-model-blind` is spec §3.2:
one grading call per research model, each receiving that model's output *and
only that model's output*, explicitly to avoid anchoring on another model's
framing. `single-call-all-models` concatenates every output into one prompt.
That is author-anonymised — the grader is told not to identify or rank authors —
but it is not source-isolated, and those are different properties. Under
`single-call-all-models` the grader has read every output before scoring any of
them, and is asked to produce the union of claims and the per-model scores in
the same pass.

Independence at dispatch does not survive a grader that sees everything.

## 3. Conformance is derived, never stored

The block records **facts only**. Whether a run conforms to the spec is computed
from those facts at read time, and is deliberately not a stored field.

This is the same principle the calibration spec applies to scores: §4 derives the
integer from `(stance, strength)` by fixed lookup precisely so the mapping is
auditable and can change without re-running anything. A stored `conforming: true`
would be a number a writer chose — exactly the thing the spec refuses.

```
conforming ⟺ grader_topology  == "per-model-blind"
           ∧ score_derivation == "derived-lookup"
           ∧ extraction_pass  == "separate"
```

`scripts/validate.py` derives and reports this per run. It does not fail a run
for non-conformance: the block's job is to state what a run *is*, and a
non-conforming run that says so is behaving correctly. What fails is a run that
declines to say.

## 4. The corpus as it stands

Every run currently in `research/` was produced by an implementation that
diverges from the spec on all three axes — `single-call-all-models`,
`model-assigned`, `fused`. This is tracked as
[dhk/minority-report#59](https://github.com/dhk/minority-report/issues/59).

Two consequences follow, and both are corpus-visible rather than merely internal:

1. **Group counts are not independent per-model agreement.** `consensus` /
   `disagreement` / `novel` counts across every published investigation were
   assigned by a grader that had read all outputs. They should not be cited as
   though three isolated passes converged. Two investigations already report the
   symptom in prose — one grading model volunteered, unprompted, that
   *"the degree of agreement on individual claims is unusually high"* — and the
   size of the effect is unmeasured.
2. **Existing scores cannot be recomputed.** §4 promises that stored categorical
   labels allow rescoring without new model calls. No categorical labels were
   stored, so that property does not hold for any existing run. A mapping change
   requires re-dispatch.

Neither is repaired by editing history. Raw provider responses are preserved per
model on the host, so the honest repair is a re-grade published as a new,
linked artifact — which also measures consequence 1 rather than asserting it.

## 5. Adding a value

The enumerations are closed on purpose: an open string field would let a new
topology enter the corpus without anyone deciding it exists. A new value is a
schema change, reviewed, with this document updated in the same pull request.
