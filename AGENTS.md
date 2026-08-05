# AGENTS.md

## Repository purpose

Alexandria manages the artifacts and review process for multi-model research. The repository—not any orchestration service—is the authoritative record. The orchestration service itself (MCP server, commission dispatch, deploy tooling) lives separately in [dhk/minority-report](https://github.com/dhk/minority-report); see [issue #33](https://github.com/dhk/alexandria/issues/33).

## Working rules

1. Never commit substantive work directly to `main`.
2. Create a branch named `agent/<short-description>` or `research/<short-description>`.
3. Keep each pull request focused on one coherent change.
4. Preserve raw model outputs exactly as received.
5. Never rewrite or delete merged raw evidence. Add a correction or superseding artifact instead.
6. Record provider, model, prompt, brief revision, execution time, tool access, and checksums for every run.
7. Keep generated interpretation separate from source evidence.
8. Do not treat model agreement as factual validation.
9. Do not commit API keys, credentials, private session data, hidden reasoning, or copyrighted source corpora without permission.
10. Update schemas and documentation together when changing an artifact contract. If the contract change affects how Minority Report reads or writes artifacts, coordinate that change there too.
11. **Verify the claim before you make it.** Any assertion that something is absent, identical, complete, current, or the only copy — in a handoff, a pull-request body, a commit message, or a report — must be checked by a command before it is written, and the check named alongside it. Report what the command returned, not what you expected it to return. An unverified "this exists only here" nearly cost merged work; a diff that compared a tree against itself was reported as a passing verification gate. Both were internally consistent and externally wrong, and in both cases the falsifying command was one line away.

## Cross-repository handoff

Work moves between repositories and between sessions as a **branch**, never as an archive of loose files. A branch carries its base commit, so a reviewer can see what it was written against; an archive carries nothing, and reconciling one has already cost more than the work inside it — and concealed a regression against current `main`.

More than one session may be working across this repository and Minority Report at once. Before changing shared paths, check what is already in flight: open pull requests in both repositories, and recent commits on `main`. Rule 11 applies with particular force to anything you are about to tell another session is done, absent, or current.

## Pull-request expectations

Every pull request should state:

- what changed;
- why it changed;
- which artifacts or contracts are affected;
- how it was validated;
- whether existing analyses become stale;
- any unresolved design decisions.

## Research changes

A substantive change to an approved research brief creates a new brief version and normally a new batch. Runs must point to the exact brief revision and checksum they used.

## Generated files

Generated indexes may be rebuilt. Raw research evidence may not.
