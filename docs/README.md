# Alexandria documentation index

This index distinguishes normative corpus documentation from cross-repository
interfaces and historical design. A document's category is part of its status.

## Current corpus contracts

- [Corpus design](DESIGN.md) — ownership, lifecycle, integrity, and governance.
- [Confidence calibration](confidence-calibration.md) — score semantics and
  evidence requirements used by stored claim artifacts.
- [Instrument record](instrument.md) — what apparatus produced a run's claim
  landscape, and why conformance is derived rather than stored.
- [Normalization](normalization.md) — stage `04-normalized`, why a matrix cell
  is derived from stored votes rather than stored itself, and the signed-zero
  rendering convention.
- [`schemas/`](../schemas) — normative machine-readable corpus contracts,
  applied to the artifacts they govern by `scripts/validate.py`.
- [Contributing](../CONTRIBUTING.md) and [agent rules](../AGENTS.md) — review,
  correction, public-data, and cross-repository coordination rules.

## Cross-repository contracts

- `ALEXANDRIA_REPO` points Minority Report at an Alexandria checkout.
- Alexandria schemas define promoted artifact meaning; Minority Report tests
  compatibility with the schemas it reads or drafts.
- Promotion from a local Minority Report run into `research/` is deliberate and
  reviewed; Minority Report does not automatically commit to this repository.
- Executable setup and operational manuals are authoritative in
  [Minority Report's docs](https://github.com/dhk/minority-report/tree/main/docs).

## Historical design and inbound-link pointers

These paths remain to preserve context and inbound links, but are not operational
authority: [MCP server](MCP-SERVER.md), [commission surface](COMMISSION-SURFACE.md),
[packaging](PACKAGING.md), [orchestration harness](orchestration-harness.md), and
[host service registry](RFC-0006-host-service-registry.md). The UX RFCs and
prototype under [`ux/`](ux/) are historical product-design records; current
executable behavior is documented with Minority Report.

## Research outputs

Each directory under [`research/`](../research) is a reviewed investigation with
its own status and limitations. [`generated/`](../generated) is rebuildable and
must not be treated as primary evidence.
