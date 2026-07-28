# Alexandria MCP server

Alexandria's tools as a first-class MCP surface — the same stdio/`--http`
shape proven out by `dhk/wingman`'s MCP server, forked via
`templates/mcp-server/` (see that directory's README for the generic
version of everything below).

## What it exposes today

Every MCP tool is **read-only and deterministic**: no model call, no network,
no write. The separate local commission web surface described in
[`docs/COMMISSION-SURFACE.md`](COMMISSION-SURFACE.md) owns the first guarded
OpenRouter write path; it does not change the MCP tool contract.

| Tool | What it does |
|---|---|
| `status()` | Investigation counts by lifecycle stage and assurance level. |
| `list_research(assurance="", stage="")` | List investigations under `research/`, optionally filtered. |
| `show_research(slug)` | One investigation's `topic.yaml` fields, README, and lifecycle-stage checklist. |
| `search_research(query, limit=10)` | Case-insensitive substring search across `research/`'s text files, with file/line citations. |

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
  never inside the repository), rotatable with `--rotate-token`.
- **Host config** follows the "wingman.env" pattern: `~/.config/
  alexandria.env` is the one canonical file a systemd `EnvironmentFile=`
  or a bare shell points at.
- **The admin installations page** (`/admin/<token>/installations`) shows
  every instance listed in `<data-dir>/installations.toml` — name,
  version, running/stopped, and a link in. Read-only and launcher-only, by
  design.

Full deployment instructions (systemd units, tunneling, multi-instance)
are in `templates/mcp-server/docs/SERVER.md` — the `<service>` placeholder
there is `alexandria` and the entry point is `alexandria-mcp`.

## Design note: why read-only

This server's tools answer "what does the repository already know" — the
recall step before anyone proposes new research work — not "generate a
report" or "dispatch a model." Once the orchestration harness in
`docs/orchestration-harness.md` is actually built, its `estimate_cost()` /
`run_research()` tools belong on this same server, gated the same way
wingman gates its own first external write (RFC-025 there: preview the
exact action, require explicit confirmation, keep the destination and
credential the user's own). That is future work, not part of this surface
yet.
