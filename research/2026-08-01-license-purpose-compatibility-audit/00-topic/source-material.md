# Source material

## The feature idea, as given by the operator

> On the license — you must never implement. You can call out the absence,
> or contradiction, but you must never implement.
>
> Add a feature request: look at the remote docs/libraries/plugins/pip
> install/includes etc — and based on that, advise on whether the current
> license structure allows for that, where the poisonous components are
> (those that make adaptability and/or IP protection more restrictive than
> you want, or disallow you from the apparent purpose).
>
> This may be a cool feature all by itself. In and for this issue, do some
> lightweight research to see what other tools are out there, and spec out
> what a useful tool for this might look like.

## Lightweight research pass (single-agent, free, 2026-08-01)

Findings from a fast web-search pass, prior to any Alexandria dispatch —
included here verbatim as the raw material this brief's research questions
are meant to verify, extend, and stress-test:

### 1. Existing tools — landscape survey

- **ORT (OSS Review Toolkit)** — free/Apache-2.0, CI-oriented. Does true
  compatibility reasoning via a Kotlin-based policy engine
  (`evaluator.rules.kts`) plus a built-in ruleset derived from the OSADL
  License Compatibility Matrix; orgs still write their own rules for what's
  "acceptable."
- **ScanCode Toolkit** (nexB) — free/Apache-2.0 detection engine (900+
  licenses via ScanCode LicenseDB). Inventory/detection only, not a
  compatibility reasoner — other tools (flict, ORT) build reasoning on top
  of it.
- **`license-checker` (npm)** and **`pip-licenses` (Python)** — free,
  single-ecosystem, list-only. Report declared license per package; no
  cross-license reasoning.
- **`cargo-deny`** (Rust) and **`go-licenses`** (Go) — free, CI-oriented
  allow/deny lists per ecosystem. Compatibility is manual: declare an
  allow-list, anything else fails — no automatic "is X compatible with Y."
- **`licensee`** (GitHub's Ruby gem) — detects what license a repo *itself*
  declares via fuzzy LICENSE-text matching (powers GitHub's license badge);
  doesn't inspect dependencies. Sibling gem **`licensed`** caches/verifies
  dependency licenses but is inventory-only.
- **GitHub dependency graph** — surfaces each dependency's detected license
  in the UI; inventory only.
- **FOSSA** — commercial/enterprise SaaS (free tier for small projects).
  Real compatibility + policy reasoning: multi-layer detection plus "policy
  stacks" so the same GPL dependency can be flagged in a customer-facing
  product but allowed internally. Both CI enforcement and one-off audits.
- **Snyk, Mend (WhiteSource), Black Duck** — enterprise SCA suites,
  per-developer pricing (Snyk ~$25–98/dev/mo published, Mend up to
  ~$1000/dev/yr, Black Duck custom-quoted). Policy-based conflict detection
  at CI/compliance-team level.
- **REUSE (FSFE)** — a compliance specification/linter for tagging every
  file's license (SPDX headers). Not a dependency-compatibility tool.

### 2. How compatibility reasoning actually works

- No single universal authority. The **FSF's "Various Licenses and
  Comments" chart** gives a canonical (if GPL-centric) view of GPL
  compatibility. The **SPDX License List** standardizes identifiers/
  exceptions but doesn't encode compatibility itself. The **OSADL License
  Compatibility Matrix** is the most reused machine-readable compatibility
  dataset (pairwise leading/subordinate license lookups, JSON/CSV).
- Real tools encode it as a **static base ruleset (OSADL/SPDX) plus
  mandatory per-org policy layered on top** — ORT's `rules.kts` and FOSSA's
  "policy stacks" both work this way. Nobody ships a policy that "just
  knows" your intent — that's always a config step.
- **`flict`** (vinland-technology, GPL-3, free) explicitly computes
  license-expression compatibility and can check outbound licenses "against
  a policy," using ScanCode's license DB.
- Academic work (**LiDetector**, ACM TOSEM 2022, and follow-up
  **LiResolver**) shows the field is unsettled even for pairwise
  compatibility of arbitrary/custom license text — PCFG-based NLP,
  91% accuracy on right/obligation inference. Research-grade, not
  production.

### 3. The gap

- The space splits almost exactly in two: **(a)** enterprise SCA platforms
  (FOSSA, Mend, Black Duck, Snyk) with real compatibility/policy engines
  but paid/org-oriented, and **(b)** free single-ecosystem inventory tools
  that list but don't reason. **ORT and flict are free/open exceptions
  that do real reasoning**, but both require config/rule authoring — not
  "just point and get English"; ORT especially is a heavyweight
  multi-tool suite meant for CI pipelines. Newer entrants (LicenseGuard,
  LicenseWatch) are lightweight free web checkers aimed at solo devs/small
  projects, but appear to be inventory + basic risk flags, not deep
  purpose-aware reasoning — unverified beyond marketing copy, flagged here
  as needing a hands-on check rather than being cited as settled prior art.

### 4. Purpose-aware reasoning (the novel angle)

- **FOSSA's "policy stacks"** are the closest existing concept — different
  rules for "internal tool" vs. "customer-facing product" contexts — but
  still manually configured per-policy, not inferred from repo signals
  (e.g. presence of a SaaS Dockerfile, a pricing page, absence of a
  LICENSE = closed intent). No surveyed tool auto-infers "commercial/SaaS/
  closed-redistribution intent" from repo content and cross-checks it
  against dependency license terms (e.g. a non-commercial-only or
  SSPL/BSL dependency in an apparent SaaS product) — **this appears to be
  genuinely unclaimed territory**, which is the claim this brief exists to
  pressure-test.

Sources cited by the lightweight pass: oss-review-toolkit.org, ORT
evaluator-rules docs, nexB FOSDEM 2023 recap, license-checker (GitHub),
pip-licenses (PyPI), cargo-deny config docs, licensee (GitHub), FOSSA
blog, gnu.org license list, OSADL compatibility matrix, flict (GitHub),
LiDetector (arXiv), Snyk pricing writeup, Mend/Black Duck comparison
writeup. None independently re-verified for this brief — a deeper pass
should re-check the load-bearing ones (ORT's actual rule-authoring
requirement, FOSSA's actual policy-stack behavior, and whether
LicenseGuard/LicenseWatch-type tools do anything closer to purpose
inference than they appear to from marketing copy alone).
