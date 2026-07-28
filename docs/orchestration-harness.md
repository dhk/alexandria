# Orchestration Harness Design

**Status:** Draft v1
**Owner:** Dave Holmes-Kinsella
**Last updated:** July 27, 2026

---

> This document describes the orchestration harness that dispatches briefs to multiple model providers, estimates and logs cost, and produces the runs and comparative artifacts consumed by [`research/`](../research). It is deliberately kept separate from [`docs/DESIGN.md`](DESIGN.md), per this repository's principle that "the repository is the durable system of record" while "provider adapters, orchestration services, user interfaces, and analysis engines are replaceable components around it."

## 1. Overview & Goals

Commission the same research brief or document to multiple frontier LLMs in parallel, then synthesize the results into a report that explicitly preserves disagreement and novelty rather than collapsing everything into a single averaged voice — a "minority report" style output, not a majority-vote consensus.

**Primary use case:** roughly 5 research commissions per week, run by a small trusted team (the operator plus a few colleagues), against the operator's own shared model-provider balance for now.

**Success looks like:** a self-contained markdown report per commission, with a companion visualization showing exactly where the models agreed, disagreed, or each raised something unique — traceable back to the person, session, and exact models involved, at a cost low enough to be a rounding error.

## 2. Non-Goals (v1)

- No public or external user support, no self-serve signup
- No real payment collection — cost estimation and logging only, no wallet or Stripe integration yet
- No automated NotebookLM participation in the fan-out (see §6)
- No multi-machine deployment — all three integration surfaces run on the operator's machine, so a single local SQLite ledger is sufficient

## 3. Economics

Using [OpenRouter](https://openrouter.ai/pricing) as the unified gateway rather than separate provider accounts, at 5 commissions/week with a 3-model fan-out + 1 synthesis call:

| Scenario | Per commission | Per week | Per month | Per year |
|---|---|---|---|---|
| Light brief, mid-tier models (GPT-5.4 / Sonnet / Sonar Pro) | ~$0.17 | ~$0.85 | ~$3.65 | ~$44 |
| Full document, flagship models (GPT-5.4 / Opus / Sonar Reasoning Pro) | ~$0.32 | ~$1.60 | ~$6.90 | ~$83 |

OpenRouter itself charges no markup on inference (same per-token rate as going direct to a provider), plus a 5.5% fee only on credit *purchases*, not per request ([OpenRouter pricing](https://openrouter.ai/pricing)). At this volume there's no off-the-shelf "multi-model consensus" product that pencils out against building this directly — the cheapest comparable subscription tools run $299+/month.

## 4. Architecture Overview

```
 ┌───────────────┐   ┌───────────────┐   ┌──────────────────────┐
 │ Claude Desktop │   │ Claude Code    │   │  Web services / n8n   │
 │  (MCP client)  │   │ CLI (MCP)      │   │  (plain HTTP trigger)  │
 └───────┬────────┘   └───────┬────────┘   └───────────┬───────────┘
         └────────────┬───────┘                        │
                       ▼                                ▼
             ┌──────────────────┐             ┌──────────────────┐
             │  mcp_server.py    │             │   api_server.py    │
             │ (stdio adapter)   │             │ (FastAPI adapter)   │
             └─────────┬─────────┘             └─────────┬──────────┘
                       └────────────┬──────────────────────┘
                                    ▼
                     ┌────────────────────────────────┐
                     │      research_synthesis/ core     │
                     │ resolver · dispatcher · estimator │
                     │ synthesis · visualizer · ledger    │
                     └─────────────────┬────────────────┘
                                       ▼
                            OpenRouter (unified API)
                   OpenAI · Anthropic · Gemini · Perplexity
```

Everything below the two adapters is a single mode-agnostic core library. The adapters only translate between a transport (MCP tool call vs. HTTP POST) and the same underlying function calls.

## 5. Credential & Cost Management

### 5.1 Credential resolver abstraction

A single interface: `get_key(user_id) -> api_key`.

- **Today:** `SharedKeyProvider` — one OpenRouter key provisioned per person via the [Management API](https://openrouter.ai/docs/guides/overview/auth/management-api-keys) (`POST /api/v1/keys`), all funded from the operator's balance, each carrying a per-key spend `limit` with a daily/weekly reset ([OpenRouter limits](https://openrouter.ai/docs/api_reference/limits)). This gives per-user attribution and a safety cap even while the operator is footing the bill.
- **Future:** `UserKeyProvider` — same interface, same per-key mechanics, but the key is funded by the person who owns it instead of the operator. Migrating to BYOK is a funding-source change, not a code change.

### 5.2 Pre-flight cost estimator

Token-counts the document and brief, multiplies by live per-model rates pulled from OpenRouter's `/models` endpoint, and produces a dollar estimate before dispatch.

- **Desktop / CLI mode:** the MCP server exposes two tools, `estimate_cost()` and `run_research()`. The model naturally calls the estimator first, shows the number in chat, and only calls the dispatcher after the user confirms — a human-in-the-loop gate with no custom UI required.
- **Web-service mode:** no chat loop to confirm in, so runs auto-execute as long as the estimate is under a configured per-run budget ceiling. No async approval step.

### 5.3 Settlement and ledger

After each run, the exact cost is pulled via OpenRouter's per-generation lookup (`GET /api/v1/generation?id=`) and reconciled against the estimate, then logged (§7). No real billing is collected yet — this is the foundation for later metered billing or BYOK migration, not a live payment path.

## 6. Model Provider Coverage & Configuration

| Provider | On OpenRouter? | Notes |
|---|---|---|
| OpenAI | Yes | [openrouter.ai/openai](https://openrouter.ai/openai) |
| Anthropic | Yes | [openrouter.ai/anthropic](https://openrouter.ai/anthropic) |
| Google (Gemini) | Yes | [openrouter.ai/providers](https://openrouter.ai/providers) |
| Perplexity | Yes | [openrouter.ai/perplexity](https://openrouter.ai/perplexity) |
| NotebookLM | **No** | Not a model API — a Google product built on Gemini. Only official surface is the enterprise-gated [NotebookLM Enterprise API](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks) (requires a Gemini Enterprise license); no public consumer API exists yet ([Goldcoast Labs](https://web-clipper-for-notebooklm.com/blog/gemini-notebook-api)). Excluded from the automated fan-out for v1 — treated as a manual input if its perspective is wanted. |

Model selection is config-driven rather than hardcoded, so swapping models is a one-line edit, and each provider is called through the identical OpenRouter request shape:

```yaml
research_models:
  - provider: openai
    model: openai/gpt-5.4
  - provider: anthropic
    model: anthropic/claude-opus-4.7
  - provider: google
    model: google/gemini-3.1-pro-preview
  - provider: perplexity
    model: perplexity/sonar-reasoning-pro
synthesis_model:
  provider: anthropic
  model: anthropic/claude-sonnet-4.6
budget:
  desktop_cli_mode: confirm
  web_service_mode: auto_ceiling
  web_service_ceiling_usd: 1.00
retry:
  max_retries_per_call: 1
  on_exhausted: proceed_partial
```

Overrides can also be passed per-run (e.g., from the MCP tool call itself) rather than only at this default level.

## 7. Integration Surfaces

**Claude Desktop** — add to `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "research-synthesis": {
      "command": "python",
      "args": ["/path/to/research_synthesis/mcp_server.py"],
      "env": { "OPENROUTER_MANAGEMENT_KEY": "..." }
    }
  }
}
```

**Claude Code CLI** — one command, same underlying server:
```bash
claude mcp add research-synthesis --scope user -- python /path/to/research_synthesis/mcp_server.py
```

**Small web services** — a thin FastAPI wrapper exposing the same two operations as HTTP routes for n8n workflows, cron jobs, or an internal web UI:
```python
@app.post("/estimate")
def estimate(req: ResearchRequest): ...

@app.post("/run")
def run(req: ResearchRequest): ...
```

## 8. Data Model & Instrumentation

Single local SQLite database, since all three surfaces run on the operator's machine. Documents and prompts are stored verbatim for full traceability (per decision — revisit if sensitive content ever flows through this).

```sql
CREATE TABLE users (
    user_id     TEXT PRIMARY KEY,
    name        TEXT NOT NULL,
    key_ref     TEXT NOT NULL,       -- resolved by the credential resolver (§5.1)
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE sessions (
    session_id  TEXT PRIMARY KEY,
    user_id     TEXT NOT NULL REFERENCES users(user_id),
    source      TEXT NOT NULL CHECK (source IN ('desktop','cli','web')),
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE runs (
    run_id          TEXT PRIMARY KEY,
    session_id      TEXT NOT NULL REFERENCES sessions(session_id),
    document_ref    TEXT,            -- verbatim document (path or inline blob)
    brief           TEXT NOT NULL,   -- verbatim prompt/brief
    status          TEXT NOT NULL CHECK (status IN ('pending','estimated','running','completed','failed','partial')),
    cost_estimated  REAL,
    cost_actual     REAL,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at    TIMESTAMP
);

CREATE TABLE model_calls (
    call_id                     TEXT PRIMARY KEY,
    run_id                      TEXT NOT NULL REFERENCES runs(run_id),
    provider                    TEXT NOT NULL,   -- openai | anthropic | google | perplexity
    model_id                    TEXT NOT NULL,   -- exact OpenRouter model string
    role                        TEXT NOT NULL CHECK (role IN ('research','synthesis','grading')),
    input_tokens                INTEGER,
    output_tokens                INTEGER,
    cost                        REAL,
    openrouter_generation_id    TEXT,
    latency_ms                  INTEGER,
    status                      TEXT NOT NULL CHECK (status IN ('success','retried','failed')),
    error                       TEXT,
    created_at                  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE claims (
    claim_id    TEXT PRIMARY KEY,
    run_id      TEXT NOT NULL REFERENCES runs(run_id),
    claim_text  TEXT NOT NULL,
    group_key   TEXT CHECK (group_key IN ('consensus','disagreement','novel','thin','silent')),
    responding_model_count INTEGER NOT NULL
);

CREATE TABLE claim_scores (
    claim_id        TEXT NOT NULL REFERENCES claims(claim_id),
    model_id        TEXT NOT NULL,
    stance          TEXT CHECK (stance IN ('supports','disputes','silent')),
    strength        TEXT CHECK (strength IN ('strong','moderate','weak')),
    score           INTEGER,   -- -3..+3; 0 is graded-silent; null only when the call failed
    evidence_quote  TEXT,      -- required for every non-zero score
    grader_call_id  TEXT REFERENCES model_calls(call_id),
    PRIMARY KEY (claim_id, model_id)
);
```

`model_calls.model_id` stores the literal OpenRouter model string, so any run can always be traced back to exactly which model, which user, which session, and what it cost, and reconciled against OpenRouter's own generation record via `openrouter_generation_id`.

## 9. Synthesis Engine

1. Each research model produces its raw output independently.
2. The synthesis call atomizes the combined outputs into a discrete canonical claim list.
3. One blind grading call per successful research model classifies every claim using the fixed stance/strength rubric in [Confidence Calibration Spec](confidence-calibration.md). The application maps those categories to integer −3…+3 scores; `0` means graded-silent.
4. The analysis layer assigns each claim's `group` (`consensus | disagreement | novel | thin | silent`). Disagreement wins when a claim also has thin coverage.
5. The synthesis output is **hybrid**: the structured claim/score data above is the canonical artifact, and a prose report (following the usual Task → Context → Constraints → Output Format structure) is rendered from it for reading.
6. **Failure handling:** if a research call errors or times out, it is retried once; if it still fails, the run proceeds with the remaining models' outputs. The failed model's score is null—a missing observation rendered `✕`—never `0`, which is reserved for graded silence.

## 10. Visualization Layer

A companion file, separate from the prose report, built from the same claim/score data — no separate data model needed.

- **Encoding:** the integer −3…+3 score carries stance and strength for each `(claim, model)` pair. The analysis layer writes the claim's group explicitly; the UI does not infer taxonomy from colour or recompute it from the matrix.
- **Two-tier rendering**, both generated from the identical score matrix so they can never drift apart:
  1. A portable text table using color-coded block/emoji buckets (🟩🟢⬜🟠🟥) — renders identically in Desktop chat, CLI output, and any web response, with no dependencies.
  2. A rendered heatmap image (diverging colormap, green–gray–red) embedded via a normal markdown image link — the "whizzy" layer, for viewers that render images.

## 11. Output & Delivery

Every run always saves two files (prose report + visualization companion) to disk, **and** returns the same content inline to whichever mode triggered it — a chat reply for Desktop/CLI, a response payload for the web-service call. Nothing is file-only or chat-only.

## 12. Future Work / Open Items

- **NotebookLM integration path** — pending a decision on whether to pursue Enterprise API access, or continue treating it as a manual input
- **Real payment collection** — Stripe charge or internal wallet debit, deferred until external (non-trusted) users exist; the ledger built in §8 already carries the exact cost needed to bolt this on later
- **BYOK rollout** — swap the funding source on already-provisioned per-user keys; no schema or dispatcher change required
- **Confidence calibration** — resolved. See [Confidence Calibration Spec](confidence-calibration.md) for the stance/strength rubric, per-model blind grading pass, and evidence-quote requirement used to derive the integer −3…+3 score.
- **Multi-machine deployment** — if the web-service mode ever moves off the operator's machine, the SQLite ledger needs to become a small hosted Postgres reachable by all three surfaces

## References

- [OpenRouter Management API Keys](https://openrouter.ai/docs/guides/overview/auth/management-api-keys)
- [OpenRouter per-key limits](https://openrouter.ai/docs/api_reference/limits)
- [OpenRouter guardrails](https://openrouter.ai/docs/guides/features/guardrails)
- [OpenRouter workspace budgets](https://openrouter.ai/docs/guides/features/workspaces/workspace-budgets)
- [OpenRouter providers directory](https://openrouter.ai/providers)
- [OpenRouter pricing](https://openrouter.ai/pricing)
- [OpenRouter — Anthropic models](https://openrouter.ai/anthropic)
- [OpenRouter — OpenAI models](https://openrouter.ai/openai)
- [OpenRouter — Perplexity models](https://openrouter.ai/perplexity)
- [Google NotebookLM Enterprise API docs](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks)
- [NotebookLM API status, 2026](https://web-clipper-for-notebooklm.com/blog/gemini-notebook-api)
