# Contributing

Alexandria uses branches and pull requests for every substantive corpus change.

## Route changes by owner

Make the change here when it concerns research artifacts, lifecycle, schemas,
policy, provenance, source handling, assurance, publication, or governance.

Make it in [dhk/minority-report](https://github.com/dhk/minority-report) when it
concerns executable orchestration, MCP or web behavior, provider integration,
local run records, packaging, deployment, services, tunnels, or host operation.
Coordinate one PR in each repository when an artifact contract and its reader or
writer change together; cross-link them and state the safe merge order.

## Workflow

1. Open or reference an issue and branch from the reviewed base.
2. Make one coherent change. Do not mix evidence import with synthesis edits.
3. Run `uv run --frozen python scripts/validate.py`.
4. Open a PR naming affected artifacts/contracts, validation, stale analyses,
   limits, and unresolved decisions.
5. Obtain the review required by the affected assurance level.
6. Merge only after required checks pass.

Use `agent/<description>` for repository changes, `research/<topic-or-stage>` for
investigations, `fix/<description>` for corrections, and `docs/<description>` for
documentation-only changes.

## Evidence, corrections, and public safety

Raw provider outputs and source evidence are immutable after merge. Correct them
with a linked correction or superseding artifact; never silently edit history.

Before committing public research material:

- confirm the source may be used and record attribution, retrieval, and rights;
- minimize personal data and exclude confidential or user-specific inputs;
- keep secrets, credentials, capability paths, account identifiers, local run
  records, and host details out of Git;
- separate quotations and raw evidence from generated interpretation;
- state access, citation, provider, and verification limitations honestly.

If safe publication conflicts with exact preservation, keep the sensitive raw
record outside this public repository and commit a provenance note or checksum
that does not disclose the protected content.
