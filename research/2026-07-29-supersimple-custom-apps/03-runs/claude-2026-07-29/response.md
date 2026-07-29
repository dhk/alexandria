# Findings: claude-2026-07-29

Raw findings from a single-source research pass answering
[`../../01-brief/brief.md`](../../01-brief/brief.md) Q1–Q7. Preserved as
returned — see [`../../05-analysis/analysis.md`](../../05-analysis/analysis.md)
for interpretation, differentiation judgment, and Q8.

Sources are cited inline per entry. Supersimple's own Custom Apps feature
is unreleased; its characterization throughout comes only from
[`../../00-topic/source-material.md`](../../00-topic/source-material.md),
not independent verification — Supersimple's public site does not yet
document it (confirmed via search 2026-07-29).

## Q1 — Custom code/component embedding

| Entry | What it is | Supersimple Custom Apps concept overlap | Verdict |
|---|---|---|---|
| Hex | Apps are published from curated notebook cells (Python/SQL); an Embed API also exports an individual cell as a link or raw HTML/iframe for insertion into an external front-end. | Publishing custom logic/visuals for org sharing, yes; but the unit is "curated notebook cells," not an arbitrary standalone app dropped onto a canvas. | partially matches |
| Sigma | Plugin SDK (JS or React Hooks), developer-hosted, rendered in an iframe inside a workbook; pulls data from Sigma and renders with any library (D3, Recharts, etc.). | Close: arbitrary custom code/visualization, published for reuse. | matches |
| Tableau | Dashboard Extensions API / Viz Extensions: web apps (arbitrary JS) run as an object inside a dashboard, with a published Extensions API and a public Exchange marketplace. | Close: arbitrary custom UI with rich interaction, shared via marketplace. | matches |
| Metabase | `@metabase/custom-viz` plugin SDK: React/TS chart type, admin-uploaded as a `.tgz` bundle, then available in the visualization picker for anyone. | Custom code, yes; scope is visualization types only, not general interactive apps. | partially matches |
| Lightdash | No plugin/extension surface for embedding custom code inside the Lightdash UI itself; instead exposes a REST API, Python client, and MCP server so *external* apps can be built against its semantic layer. | Inverted pattern: build your own app outside Lightdash against its data, rather than embed custom code inside Lightdash. | no equivalent |
| Looker (Extension Framework) | Full custom React/TypeScript apps, built with the Looker Extension SDK, running inside the Looker product itself. | Strongest match: arbitrary custom logic/UI, first-class citizen of the platform, not a bolted-on iframe widget. | matches |
| Retool | The entire product is a custom-app builder (drag-and-drop UI + arbitrary JS/Python), not an extension *within* a BI tool. | Overlaps on "arbitrary custom app," but it's a separate standalone platform, not something embedded inside a governed BI dashboard alongside native charts. | partially matches |

Notes: Sigma and Tableau are the two products where "arbitrary developer
code as a first-class, published, reusable object inside the BI canvas"
is most literally true today. Looker's Extension Framework is closer in
spirit (whole apps, not just viz widgets) but is scoped as a full-page
app rather than a droppable dashboard object.

## Q2 — Ecosystem integration depth (shared filter/variable state)

| Entry | What it is | Supersimple Custom Apps concept overlap | Verdict |
|---|---|---|---|
| Hex | Within one Hex project, app-level input parameters can drive every cell (including display cells) in that same document. | Matches for content native to the same Hex app; unclear whether an *externally embedded* HTML cell (Embed API) auto-subscribes to the host app's filters the way Supersimple describes a date range hitting both native charts and the custom app. | partially matches |
| Tableau | Extensions API exposes methods for extensions to read dashboard filter/parameter/selection changes and to fire dashboard actions — two-way event subscription. | Matches: an extension can react live to the same filter changes native worksheets see. | matches |
| Sigma | Plugins receive the data/config bound to their element; native controls (e.g. a date range control) that feed that element's underlying query do propagate to the plugin. | Matches, contingent on binding the plugin's data source to the same controlled element as native charts. | matches |
| Metabase | Custom-viz types work "like any other interactive Metabase chart," with drill-through, inside questions/dashboards — implying standard dashboard-filter propagation since it sits in the normal query pipeline. | Matches for the visualization-only scope. | matches |
| Lightdash | No embedded-extension surface exists to test this against. | N/A. | no equivalent |
| Looker | Depends on the integration pattern: a "visualization extension" bound to an explore's query does receive filter-driven data; a general nav-level Extension Framework app is a standalone page that must explicitly call the SDK to read dashboard state — it does not automatically inherit host filters. | Partial: the platform *can* do this, but it's two different mechanisms depending on which kind of extension you build, not one unified story. | partially matches |
| Retool | Standalone app platform; not embedded inside another product's dashboard canvas at all. | No equivalent — different product category entirely. | no equivalent |

Notes: this question is where Supersimple's pitch is most testable and
most differentiated *if* true as described — "one variable, one update,
both native charts and the custom app move together" with zero extra
wiring is not the default behavior of any tool above; it is either
opt-in (Sigma/Tableau, bind to the right element/subscribe to the right
event) or scoped narrowly (Hex, Metabase — same-document or same-pipeline
only).

## Q3 — Read vs. write: taking action in core systems

| Entry | What it is | Supersimple Custom Apps concept overlap | Verdict |
|---|---|---|---|
| Hex | Python cells can call arbitrary external APIs (including POST/PUT), so a Hex app *can* take action, but this is a general-purpose code capability, not a marketed/governed write-back feature. | Technically possible, not productized the way Supersimple frames it. | partially matches |
| Sigma | Input Tables / Write-Back Tables: governed write-back into the warehouse (BigQuery GA, Snowflake documented), used for planning/budgeting/forecasting inputs. | Matches for writing back to the *data warehouse*; narrower than "take action in your core systems" if "core systems" means arbitrary external backends (CRM, ticketing, etc.), not just the warehouse. | matches |
| Tableau | Dashboard Extensions with write-back: a dedicated Write-Back Server/Cloud product plus community extensions that POST to arbitrary REST endpoints from inside a dashboard. | Matches, including the "arbitrary external system," not just the warehouse. | matches |
| Metabase | No write-back or action capability found; custom-viz plugin contract is rendering-only. | No equivalent. | no equivalent |
| Lightdash | Read-only BI layer over dbt; no write-back feature found. | No equivalent. | no equivalent |
| Looker | Extensions can call `external_api_urls` (arbitrary external APIs, entitlement-gated) and Looker's own write-capable SDK endpoints. | Matches. | matches |
| Retool | Write to databases and POST/PUT to any REST API is core, headline functionality. | Matches — the most general-purpose action capability in this set. | matches |

Notes: Sigma's write-back is warehouse-only; Tableau, Looker, and Retool
all support writing to arbitrary external backends, which is the closer
analog to Supersimple's "take action in your core systems" framing.

## Q4 — Dual data access: governed model + external backends, one component

| Entry | What it is | Supersimple Custom Apps concept overlap | Verdict |
|---|---|---|---|
| Hex | A single notebook/app can both query the governed warehouse and call external APIs from Python cells — dual access is possible, but as general code, not a permissioned dual-connector object. | Partially matches. | partially matches |
| Sigma | Plugins read the governed workbook data; whether a plugin also reaches arbitrary external APIs is technically possible (it's developer-hosted iframe JS) but not a documented, marketed capability. | Thinly documented. | partially matches |
| Tableau | Extensions can read the dashboard's governed data context (Data/Viz Extensions APIs) *and* make arbitrary external HTTP calls in the same extension. | Matches. | matches |
| Metabase | Custom-viz plugins receive only the query result Metabase hands them; no documented external-call contract. | No equivalent. | no equivalent |
| Lightdash | N/A — no embedded extension surface. | No equivalent. | no equivalent |
| Looker | Best-documented split: entitlements separately list which Looker (governed) resources and which `external_api_urls` an extension may reach, both usable in one app. | Matches — closest documented analog to Supersimple's "governed model + external backend, admin-controlled" framing. | matches |
| Retool | Connects to internal databases/warehouses and 50+ external APIs/SaaS within one app — but typically against raw data sources, not necessarily the same governed semantic/metric layer analysts already use in BI dashboards. | Partially matches. | partially matches |

## Q5 — Governance and permissioning of connections

| Entry | What it is | Supersimple Custom Apps concept overlap | Verdict |
|---|---|---|---|
| Hex | Row-level security and pass-through auth for embeds; workspace/project-level sharing permissions. No distinct "which app may reach which external backend" control found. | Partially matches. | partially matches |
| Sigma | Admins enable/manage plugins and iframe embeds at the org level; workbook-level access control applies to who sees a plugin. | Partially matches — org-level plugin allow-listing, not per-connection granularity. | partially matches |
| Tableau | Server/Cloud admins explicitly allow-list which extensions may run, and can restrict extensions to "sandboxed" (no network access) vs. full network-enabled — a genuine per-extension connectivity control. | Matches. | matches |
| Metabase | Admins gate who can install a plugin; no granular per-plugin "may connect to backend X" control documented. | Partially matches. | partially matches |
| Lightdash | N/A. | No equivalent. | no equivalent |
| Looker | Project manifest entitlements (`oauth2_urls`, `external_api_urls`, named Looker models) are explicitly reviewed and enabled per extension by an admin; extensions also inherit the instance's model-level permission set for any user running them. | Matches — the most granular "what can connect to what and who can access what" control found in this set. | matches |
| Retool | RBAC, audit logs, and admin-defined approved data connections that business-builder-authored apps must operate inside of. | Matches. | matches |

## Q6 — Distribution and reuse

| Entry | What it is | Supersimple Custom Apps concept overlap | Verdict |
|---|---|---|---|
| Hex | Apps can be published and shared org-wide; the reuse unit is the app/notebook itself. No evidence found of "copy this exact app into a different, larger dashboard" as a first-class pattern — Hex apps are not droppable widgets. | Partially matches. | partially matches |
| Sigma | Once published, a plugin is selectable from any workbook by any authorized user — a de facto shared gallery. | Matches. | matches |
| Tableau | Tableau Exchange is a public extension marketplace; any dashboard can add a published extension as an object, closely matching "copy this app into a bigger dashboard." | Matches. | matches |
| Metabase | Installed custom-viz types are available as a chart option across all questions/dashboards org-wide once an admin uploads them. | Matches, for the visualization-only scope. | matches |
| Lightdash | N/A. | No equivalent. | no equivalent |
| Looker | Extensions are listed per project/instance and can be embedded in multiple places, but each is closer to a standalone app users navigate to than a widget copied between arbitrary dashboards. | Partially matches. | partially matches |
| Retool | Apps can be shared/cloned within a workspace, but remain standalone apps — not droppable into someone else's BI dashboard alongside native charts. | No equivalent — different product surface. | no equivalent |

## Q7 — The "shadow AI-coding" framing

| Entry | What it is | Supersimple Custom Apps concept overlap | Verdict |
|---|---|---|---|
| Industry-wide (all six tools' public marketing, as searched) | None of Hex, Lightdash, Tableau, Metabase, Sigma, or Looker's public materials found in this pass explicitly pitch their extension/plugin/embed feature as "the governed home for the one-off AI-agent-generated artifacts your employees are already building." | No equivalent found as a *productized feature pitch* tied to a specific embed/extension capability. | no equivalent |
| Retool ("State of AI Governance" 2026 report) and the broader "shadow AI" vendor category (governance/observability platforms, per multiple 2026 sources) | Live 2026 industry narrative: "shadow IT becomes shadow AI" — ungoverned, agent-built tools as an enterprise risk category, with a growing set of dedicated AI-governance vendors (visibility/policy/access tooling) addressing it. | The *problem framing* Supersimple invokes is a real and current 2026 narrative other vendors also reference — but as thought-leadership/governance-platform positioning, not as "publish your AI-generated artifact into our BI tool with permissions" the way Supersimple's product notes describe. | partially matches |

## Open gaps

This pass covered the brief's seven named/added tools (Hex, Lightdash,
Tableau, Metabase, Sigma, Looker, Retool) but not other plausible
analogs the questions surfaced along the way:

- **Domo** — has an "App Framework" / App Store for publishing custom
  data apps inside its governed platform, which on its face sounds like
  a close structural analog to Supersimple's pitch; not researched here.
- **Apache Superset / Preset** — has a plugin architecture for custom
  chart types (open-source, similar shape to Metabase's), not researched
  for write-back or external-API capability.
- **Mode Analytics** — notebook-and-app model similar to Hex; not
  researched here.
- **ThoughtSpot Everywhere** — embedding SDK; not researched for a
  custom-app/plugin surface distinct from embedding.
- **Superblocks** — named in the brief as a Retool peer; not
  independently researched, findings above rely on Retool alone.

None of these gaps were investigated due to the brief's named scope;
flagged here rather than silently omitted, per the brief's own
"no silent gaps" instruction.
