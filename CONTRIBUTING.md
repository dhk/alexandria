# Contributing

Alexandria uses GitHub branches and pull requests for all substantive work.

## Workflow

1. Open or reference an issue describing the change.
2. Branch from the appropriate reviewed base.
3. Make one coherent change.
4. Run `python scripts/validate.py`.
5. Open a pull request with the validation result and any known limitations.
6. Obtain the review required by the affected research level.
7. Merge only after required checks pass.

## Branch naming

- `agent/<description>` for repository and tooling changes
- `research/<topic-or-stage>` for investigation artifacts
- `fix/<description>` for corrections
- `docs/<description>` for documentation-only changes

## Commit policy

Commits should be intentional and describe the artifact-level change. Do not mix raw evidence import with synthesis edits in the same commit.

## Corrections

Merged raw outputs are immutable. To correct metadata or interpretation:

- add a correction record;
- preserve the original artifact;
- explain the reason;
- identify the superseding artifact where applicable.

## Public repository safety

Do not commit secrets, personal data, confidential documents, provider credentials, or full copyrighted works without authorization.
