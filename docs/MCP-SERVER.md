# Alexandria MCP server

Alexandria's tools as a first-class MCP surface — the same stdio/`--http`
shape proven out by `dhk/wingman`'s MCP server, forked via
`templates/mcp-server/` (see that directory's README for the generic
version of everything below).

## What it exposes today

The repository recall tools are **read-only and deterministic**. The commission
tools reuse the local commission service and separate review from spend: beginning
a commission resolves inputs and creates a draft, while running it requires the
exact confirmation phrase returned with that draft.

| Tool | What it does |
|---|---|
| `status()` | Investigation counts by lifecycle stage and assurance level. |
| `list_research(assurance="", stage="")` | List investigations under `research/`, optionally filtered. |
| `show_research(slug)` | One investigation's `topic.yaml` fields, README, and lifecycle-stage checklist. |
| `search_research(query, limit=10)` | Case-insensitive substring search across `research/`'s text files, with file/line citations. |
| `begin_research(task, pasted_content="", url="", ...)` | Resolve pasted text and/or a supported GitHub URL, fetch a live estimate, and save a local review draft. No provider model calls are dispatched. |
| `run_research(draft_id, confirmation="")` | Dispatch a reviewed draft only when `confirmation` exactly matches `RUN <draft-id>`. This incurs OpenRouter spend. |

### Beginning research from an MCP client

Ask the client to begin research with either pasted material or a GitHub repository,
issue, pull-request, or blob URL. For example:

```text
Begin Alexandria research.
Task: Compare the proposed provider-layer designs and recommend a narrow interface.
URL: https://github.com/dhk/alexandria/issues/3
Hard ceiling: $1.00
```

The client calls `begin_research`, which returns the exact inputs, models, verbatim
brief, estimate, ceiling, draft ID, and a draft-specific confirmation phrase. No
research or grading model has run at this point. Review that response, then explicitly
approve it. Only then may the client call `run_research` with the returned phrase.

The same flow accepts pasted content through `pasted_content`; pasted content and a URL
may also be supplied together. URL resolution currently accepts HTTPS `github.com`
repository, issue, pull-request, and supported blob URLs.

`topic.yaml`'s shape is not yet formalized under `schemas/` (also not
built yet); `src/alexandria/infrastructure/research_repo.py` reads a
lenient, best-effort subset (`title`, `status`, `assurance_level`) until a
real schema exists — treat that module as following the schema, not
defining it.

## Running it

```bash
uv sync
uv run alexandria-mcp              # stdio, for Claude Desktop / Claude Code
uv run alexandria-mcp --http       # loopback HTTP at /mcp/<token>
```

## Upgrade and restart cycle

Install the local checkout as a uv tool once:

```bash
cd ~/Documents/dev/alexandria
uv tool install --reinstall .
```

Then the Wingman-style operator cycle is:

```bash
alexandria-ctl cycle
```

For a short command like Wingman's locally configured `wg` alias, add this to your
shell configuration:

```bash
alias ax='alexandria-ctl'
```

Then `ax cycle` performs `git pull --ff-only` → `uv tool install --reinstall .` →
stop every same-user `alexandria-mcp` process → start the HTTP server → print its
loopback `/health` result. Pull and reinstall happen before shutdown, so a failed
upgrade leaves the old servers running. Client-owned stdio processes cannot be
relaunched independently of their clients; the command names any it stopped and
tells you to restart Claude Desktop or the affected CLI sessions.

Other lifecycle commands:

```bash
alexandria-ctl status
alexandria-ctl --tunnel-path /alexandria url
alexandria-ctl start
alexandria-ctl stop-all
alexandria-ctl upgrade       # pull + reinstall, without process changes
```

`ALEXANDRIA_REPO` selects the checkout (default
`~/Documents/dev/alexandria`). `ALEXANDRIA_LOG` selects the background HTTP log.
On Ubuntu, if the user-level `alexandria-mcp.service` exists, lifecycle commands
use systemd to stop and start it rather than launching a competing unmanaged process.
Standalone `stop-all` asks before terminating client-owned stdio processes; invoking
`cycle` is itself the explicit instruction to replace them and does not prompt.

By default the server detects the repository root by walking up from the
current working directory looking for `docs/DESIGN.md` and `AGENTS.md`.
Set `ALEXANDRIA_REPO` (see `.env.example`) when running from elsewhere —
a systemd service, a different cwd, or a second checkout.

**Claude Code CLI:**

```bash
claude mcp add alexandria --scope user -- uv run --project /path/to/alexandria alexandria-mcp
```

**Claude Desktop** (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "alexandria": {
      "command": "uv",
      "args": ["run", "--project", "/path/to/alexandria", "alexandria-mcp"],
      "env": { "ALEXANDRIA_REPO": "/path/to/alexandria" }
    }
  }
}
```

## Auth, config, and the admin page

Same pattern as `templates/mcp-server/` — see that directory's README for
the full design rationale. Summary:

- **`--http` auth is the capability path token** at `/mcp/<token>`,
  generated into the server's own local state dir (`ALEXANDRIA_DATA_DIR`,
  never inside the repository), rotatable with `--rotate-token`. Anyone holding
  this URL can read repository research and can confirm a commission against the
  configured OpenRouter key; treat it as a spend-capable secret.
- **Host config** follows the "wingman.env" pattern: `~/.config/
  alexandria.env` is the one canonical file a systemd `EnvironmentFile=`
  or a bare shell points at.
- **Tailscale URL resolution** follows Wingman: the server auto-detects its
  `*.ts.net` DNS name, admits that Host without disabling DNS-rebinding protection,
  and separates the local bind port from the external HTTPS path/port. On Lobster,
  Tailscale Funnel mounts Alexandria at `/alexandria` and strips that prefix before
  forwarding to `127.0.0.1:8797`.
- **The admin installations page** (`/admin/<token>/installations`) shows
  every instance listed in `<data-dir>/installations.toml` — name,
  version, running/stopped, and a link in. Read-only and launcher-only, by
  design.

Full deployment instructions (systemd units, tunneling, multi-instance)
are in `templates/mcp-server/docs/SERVER.md` — the `<service>` placeholder
there is `alexandria` and the entry point is `alexandria-mcp`.

## Design note: recall and commission boundaries

The recall tools answer "what does the repository already know." Commission tools
are intentionally separate: `begin_research` may resolve a URL, look up live pricing,
and write local scratch state, but it cannot dispatch a model. `run_research` is the
only MCP spend boundary and requires the draft-specific phrase displayed during
review. Provider credentials remain local and user-owned in both paths.
