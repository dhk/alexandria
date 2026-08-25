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

<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:970c3bf2 -->
## Beads Issue Tracker

This project uses **bd (beads)** for issue tracking. Run `bd prime` to see full workflow context and commands.

### Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work
bd close <id>         # Complete work
```

### Rules

- Use `bd` for ALL task tracking — do NOT use TodoWrite, TaskCreate, or markdown TODO lists
- Run `bd prime` for detailed command reference and session close protocol
- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files

**Architecture in one line:** issues live in a local Dolt DB; sync uses `refs/dolt/data` on your git remote; `.beads/issues.jsonl` is a passive export. See https://github.com/gastownhall/beads/blob/main/docs/SYNC_CONCEPTS.md for details and anti-patterns.

## Agent Context Profiles

The managed Beads block is task-tracking guidance, not permission to override repository, user, or orchestrator instructions.

- **Conservative (default)**: Use `bd` for task tracking. Do not run git commits, git pushes, or Dolt remote sync unless explicitly asked. At handoff, report changed files, validation, and suggested next commands.
- **Minimal**: Keep tool instruction files as pointers to `bd prime`; use the same conservative git policy unless active instructions say otherwise.
- **Team-maintainer**: Only when the repository explicitly opts in, agents may close beads, run quality gates, commit, and push as part of session close. A current "do not commit" or "do not push" instruction still wins.

## Session Completion

This protocol applies when ending a Beads implementation workflow. It is subordinate to explicit user, repository, and orchestrator instructions.

1. **File issues for remaining work** - Create beads for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **Handle git/sync by active profile**:
   ```bash
   # Conservative/minimal/default: report status and proposed commands; wait for approval.
   git status

   # Team-maintainer opt-in only, unless current instructions forbid it:
   git pull --rebase
   bd dolt push
   git push
   git status
   ```
5. **Hand off** - Summarize changes, validation, issue status, and any blocked sync/commit/push step

**Critical rules:**
- Explicit user or orchestrator instructions override this Beads block.
- Do not commit or push without clear authority from the active profile or the current user request.
- If a required sync or push is blocked, stop and report the exact command and error.
<!-- END BEADS INTEGRATION -->

<!-- BEGIN BEADS CODEX SETUP: generated by bd setup codex -->
## Beads Issue Tracker

Use Beads (`bd`) for durable task tracking in repositories that include it. Use the `beads` skill at `.agents/skills/beads/SKILL.md` (project install) or `~/.agents/skills/beads/SKILL.md` (global install) for Beads workflow guidance, then use the `bd` CLI for issue operations.

### Quick Reference

```bash
bd ready                # Find available work
bd show <id>            # View issue details
bd update <id> --claim  # Claim work
bd close <id>           # Complete work
bd prime                # Refresh Beads context
```

### Rules

- Use `bd` for all task tracking; do not create markdown TODO lists.
- Run `bd prime` when Beads context is missing or stale. Codex 0.129.0+ can load Beads context automatically through native hooks; use `/hooks` to inspect or toggle them.
- Keep persistent project memory in Beads via `bd remember`; do not create ad hoc memory files.

**Architecture in one line:** issues live in a local Dolt DB; sync uses `refs/dolt/data` on your git remote; `.beads/issues.jsonl` is a passive export. See https://github.com/gastownhall/beads/blob/main/docs/SYNC_CONCEPTS.md for details and anti-patterns.
<!-- END BEADS CODEX SETUP -->
