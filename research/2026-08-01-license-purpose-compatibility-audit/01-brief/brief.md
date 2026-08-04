# Research brief: License & dependency purpose-compatibility auditing — prior art and feasibility

Revision: 1 (2026-08-01).

## Background

While scoping a repo-documentation-standard tool (a tiered doc checklist +
audit tool for personal/OSS repos), the operator proposed an adjacent
feature: audit a repo's dependencies (package manifests, vendored code,
submodules) against both its own declared LICENSE and its *apparent
purpose* (closed-source product, SaaS offering, OSS redistribution,
internal-only tool), flagging "poisonous" dependencies whose license
terms are more restrictive than the project wants, or outright
incompatible with that apparent purpose. A fast, single-source, free
research pass (full text in
[`../00-topic/source-material.md`](../00-topic/source-material.md)) found
a bifurcated existing landscape — heavy paid compliance platforms with
real reasoning (FOSSA, Mend, Black Duck, Snyk) vs. free tools that only
inventory licenses (`pip-licenses`, `license-checker`) or that do real
reasoning but require manual policy authoring (ORT, `flict`) — and
concluded that *purpose-aware, zero-config* auditing appears genuinely
unclaimed. This brief exists to verify that conclusion properly (a
single fast pass is exactly the kind of research that overstates a gap)
and to scope what a real build would need.

**Hard constraint, non-negotiable, applies regardless of what this
research finds**: any resulting tool only detects and reports. It must
never author, choose, or edit a LICENSE file on the repo owner's behalf.
This is a product requirement carried in from the operator directly, not
a research question — do not treat any finding below as license to
relax it.

## Scope

In scope: whether existing tools (free or paid) do purpose-aware license
reasoning, how the tools that do real compatibility reasoning encode that
reasoning, and what a genuinely lightweight (no compliance-team,
no-config, solo-developer-usable) version of this would need
architecturally.

Out of scope: legal correctness of any specific license-compatibility
claim (this is a tooling-landscape and feasibility brief, not a legal
opinion); pricing negotiation detail beyond what's needed to characterize
"paid vs. free"; building or prototyping anything — this is prior-art and
feasibility only.

## Comparison set

FOSSA, OSS Review Toolkit (ORT), ScanCode Toolkit, `flict`, `pip-licenses`,
`license-checker` (npm), `cargo-deny`, `go-licenses`, `licensee`/`licensed`,
REUSE (FSFE), Snyk License Compliance, Mend (WhiteSource), Black Duck.

A source may flag additional relevant tools not in this set (e.g.
FOSSology, ClearlyDefined, Debian's `licensecheck`, LicenseGuard/
LicenseWatch-style newer web checkers referenced in the lightweight pass
but not independently verified) in its findings' "Open gaps" section
rather than silently ignoring them — the lightweight pass explicitly
flagged that its newer-entrant claims are unverified.

## Research questions

Each question traces to a specific claim in the lightweight pass
(quoted inline) that a deeper, multi-model, source-audited pass should
either confirm, correct, or sharpen.

### Q1 — Compatibility reasoning depth
The lightweight pass claims most free tools are "inventory only" (list
licenses, no cross-license reasoning) while ORT/flict/FOSSA/enterprise
suites do "true compatibility reasoning." For each comparison-set tool:
does it actually reason about license compatibility, or only detect/list?
What specifically does "reasoning" consist of (a static ruleset lookup,
a configurable policy engine, something else)?

### Q2 — Purpose/intent awareness
Core claim under test: "no surveyed tool auto-infers commercial/SaaS/
closed-redistribution intent from repo content and cross-checks it
against dependency license terms... this appears to be genuinely
unclaimed territory." Verify or refute this directly. Does any tool,
anywhere (including outside the comparison set), accept or infer a
*purpose*/intent signal and reason about license compatibility against
it, rather than doing purely pairwise license-vs-license comparison?

### Q3 — Automation vs. required configuration
The pass claims FOSSA's "policy stacks" and ORT's `rules.kts` both
require manual policy authoring before they'll flag a purpose-related
conflict. How much configuration does each real-reasoning tool actually
require before first useful output — is there a sensible default policy,
or is a blank slate genuinely unusable out of the box?

### Q4 — Free/OSS vs. paid, and target user
The pass characterizes the market as bifurcated: paid enterprise tools
with real reasoning vs. free tools that are inventory-only, with ORT and
flict as the free exceptions that do reason (but need config). Confirm
current pricing/tiers for FOSSA, Snyk, Mend, Black Duck, and assess: is
there anything free *and* usable by a solo developer with zero setup that
does real reasoning?

### Q5 — Underlying compatibility data
The pass names the OSADL License Compatibility Matrix as "the most reused
machine-readable compatibility dataset" and the FSF chart as the
canonical (GPL-centric) reference. Confirm current maintenance status,
coverage (how many licenses/pairs), and whether any tool relies on a
different or more comprehensive dataset not mentioned.

### Q6 — Detection accuracy for edge cases
Vendored code with no manifest entry, custom/non-SPDX license text,
dual-licensed dependencies. How well does each tool's *detection* layer
(not compatibility layer) handle these — this determines whether a
"purpose-aware" layer would even have reliable inputs to reason over.

### Q7 — Closest adjacent prior art for zero-config, purpose-aware auditing
If Q2 confirms the gap is real: what is the *closest* existing pattern to
build from — e.g. `repo_signature`-style heuristic classifiers (used
elsewhere for repo archetype classification), FOSSA's policy-stack
schema repurposed as an inferred-not-configured input, or something from
outside the license-tooling space entirely (SBOM tooling, supply-chain
risk scoring)?

### Q8 (synthesis question — answer in analysis, not a findings file)
Given Q1–Q7: is "purpose-aware, zero-config license-compatibility
auditing for a solo maintainer's repo" a real, buildable gap, or does it
collapse into "FOSSA's free tier plus five minutes of policy setup" once
examined closely? If real, what's the minimal viable architecture
(detection layer + compatibility dataset + purpose-inference heuristics)
— and can it be built by composing existing free components (e.g.
OSADL matrix data + `flict` logic + a small heuristic classifier) rather
than reimplementing detection or compatibility reasoning from scratch?

## Output format for a findings submission

One section per question (Q1–Q7), each with a table:

| Entry | What it is | Purpose-aware / zero-config overlap | Verdict |
|---|---|---|---|

Verdict is a closed set: `matches` / `partially matches` / `no
equivalent` — no invented labels; rationale goes in a Notes block under
the table, not in the verdict cell. No empty tables — a "no equivalent
found" result gets a `no equivalent` row naming the tool, with the reason
in Notes. End with an `## Open gaps` section for anything the question
set missed, including explicit note of any claim in the lightweight pass
(`00-topic/source-material.md`) that a source could not verify.

Q8 is answered only in `05-analysis/analysis.md` if this investigation is
promoted to a dispatched run — it requires comparing across questions and
sources, which is synthesis work, not independent findings.
