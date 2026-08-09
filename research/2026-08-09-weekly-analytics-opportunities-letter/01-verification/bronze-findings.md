# Bronze verification pass

Single-source (Claude, this session), 9 August 2026. Live web search
against the brief's seven named competitors, plus an open scan for other
close analogs the brief's "Sources consulted" list doesn't name. Not
dispatched through Alexandria's multi-model commission pipeline
(`begin_research`/`run_research`) — that remains a spend-gated action for
the operator to trigger separately if this pass makes it worth a Silver
upgrade.

**Method note / limitation:** `WebFetch` was blocked by this session's
network egress proxy for every Substack domain and for
`analyticsengineeringjobs.com` — direct-fetch verification of those pages
wasn't possible. Everything below is sourced from `WebSearch` result
snippets only, which is weaker evidence than a direct fetch would be.
Anything below marked *(search-snippet only)* should be treated as
plausible, not confirmed, and is carried into `02-brief/brief.md` as a
question a Silver pass should close by actually opening the page.

## 1. The seven named competitors, checked

All seven are real, currently operating, and the brief's characterization
of each held up against what a live search returns:

| Competitor | Confirmed | Notes |
|---|---|---|
| [Analytics Engineering Jobs](https://analyticsengineeringjobs.com/) | Yes | Curated board with salary-range, dbt, Snowflake, SQL, remote landing pages; has a weekly newsletter. *(search-snippet only — could not confirm whether the newsletter carries per-listing personal commentary or is purely structured/tagged listings, which is the brief's actual claim. See open question below.)* |
| [DataAnalyst.com](https://www.dataanalyst.com/) | Yes | Career-level-segmented board (entry through lead), monthly newsletter, 7,500+ subscribers, market-insights content. Matches the brief's "segments alerts by career level" claim. |
| [Data Elixir](https://dataelixir.com/) | Yes | Weekly curated data-science newsletter, ~29,000 subscribers, plus a separate [job board](https://jobs.dataelixir.com/) (listings run 45 days, featured twice in the newsletter). Confirms the brief's claim: content is industry/learning links, and the jobs product is a paid-listing board bolted on, not network-sourced personal curation. |
| [Locally Optimistic](https://locallyoptimistic.com/community/) | Yes | Slack community, ~9,000 members, analytics-leadership and strategy focus. Notably: community guidelines **explicitly exclude vendors, recruiters, and other commercial users "to generate leads."** Worth flagging for the operator directly — if the letter is ever promoted inside LO's Slack, framing it as personal editorial practice rather than a recruiting channel matters for staying welcome there. |
| [Never Search Alone](https://www.phyl.org/the-book) | Yes | Phyl Terry's book/methodology + volunteer-led "Job Search Council" peer-support groups; candidate-market-fit framework. Confirms it's a support methodology, not a content publication — no overlap with a curated-opportunities letter. |
| [Welcome to the Jungle](https://www.welcometothejungle.com/) | Yes | French-origin platform, ~2M candidate profiles, AI-driven culture/mission matching at platform scale. Confirms the brief's claim that "values are categories rather than personal judgment." |
| [Tech Jobs for Good](https://techjobsforgood.com/) | Yes | Mission-driven board (nonprofits, government, climate, education), employer + job-seeker profiles, 12 named impact areas. Confirms the brief's characterization. |

## 2. Close analogs the brief's source list didn't name

The brief's "unclaimed territory" argument is about a *specific
combination* — network-sourced, mid-career-analytics-specific, editorially
interrogated, trust-disclaimed. That combination held up. But three of its
individual *components* already exist elsewhere, separately, and the brief
should say so rather than read as if the whole mechanism is novel:

- **[Saturday Data Drop](https://vizmasters.substack.com/)** (VizMasters,
  Substack) *(search-snippet only)* — an already-running **weekly "Hot
  Data & Analytics Job Openings"** digest, i.e. it occupies the exact
  surface-level positioning ("weekly + data/analytics + jobs newsletter")
  the brief is aiming for. The mechanism is different and weaker than
  what's proposed: it's pulled from a LinkedIn feed (aggregated, not
  network-sourced) and nothing in the search results suggests per-role
  personal commentary or a "why this caught my eye / what I'd ask"
  layer — it reads as a volume digest with a Poland-market slant, not an
  interrogative one. This is the single closest **name-and-cadence**
  collision worth knowing about before launch, even though the actual
  editorial mechanism doesn't compete.

- **["odd jobs" by imagined](https://imaginedhq.substack.com/)** (run by
  Ritvik Varghese/Arora, India-oriented) *(search-snippet only)* — this is
  the closest **mechanism** match found anywhere in this pass. Its own
  stated thesis is nearly identical to the brief's core insight: *"the
  best jobs on the internet are never really published — they're
  whispered in corridors and DMs"* — curated from the creator's own
  WhatsApp groups and network, weekly, no-fluff. It is **not**
  analytics-specific, has no visible mid-career framing, and (as far as
  search results show) doesn't carry a structured
  interrogation/disclaimer vocabulary comparable to "why it caught my
  eye / what I know / what I would ask." Its existence is still an
  important data point: **the network-sourced-weekly-curation mechanism
  itself is not novel or defensible IP — it's already been built, just
  not for this audience.** The brief's "no shortage of X, but nobody
  does Y" framing should rest on the audience + editorial-interrogation
  layer specifically, not imply the format itself is unclaimed.

- **[D+P Jobs](https://dpluspjobs.substack.com/)** *(search-snippet
  only)* — design/product roles sourced directly from hiring managers via
  a referral posting method. Same shape again, different vertical.
  Reinforces the same point: the mechanism travels across niches easily;
  it hasn't yet landed on analytics/analytics-engineering specifically.

- **dbt Labs' own community newsletter** — dbt Labs runs an "Analytics
  Engineering Roundup" newsletter/podcast on Substack and a Slack/
  Discourse community reported at 50,000–100,000+ members, aimed at
  exactly this audience. It does not currently appear to run a
  network-sourced curated-opportunities feature. It is, however, the
  single most-resourced incumbent already holding this audience's
  attention — worth watching, not competing with head-on, since dbt Labs
  (recently merging with Fivetran per search results) could add a
  curated-jobs feature to existing infrastructure faster than an
  independent letter could build reach.

## 3. Net assessment of the "unclaimed territory" claim

The brief's central claim holds, but should be stated more precisely than
"there is no shortage of X... the defensible opportunity is..." implies.
Three things are true simultaneously:

1. **The audience is not unclaimed.** Data Elixir, Analytics Engineering
   Jobs, Locally Optimistic, and dbt Labs' own newsletter all already
   reach mid-career analytics practitioners.
2. **The mechanism is not unclaimed.** Odd Jobs and D+P Jobs already run
   network-sourced, personally-curated, weekly opportunity digests — just
   for different audiences.
3. **The surface format is not unclaimed.** Saturday Data Drop already
   publishes a weekly data/analytics jobs digest, even though its
   sourcing and editorial depth don't match what's proposed here.

What appears genuinely open, based on this pass, is the **specific
combination** of all three — plus the editorial-interrogation layer (the
seven-question lens, the "why it caught my eye / what I know / what I
would ask / connection available" annotation vocabulary) and the explicit
provenance discipline (never confusing "shared with me" with "endorsed by
me"). No newsletter found in this pass combines audience + mechanism +
editorial-interrogation + provenance discipline the way the brief
proposes. That's a narrower, more defensible claim than "nobody does
this," and it's the version worth putting in front of the operator and,
eventually, readers.

## 4. A risk the brief doesn't name: network concentration

Every "durable moat" argument in the brief (network, judgment, trust)
assumes the initial 15–20 trusted forwarders are a reasonably diverse
sample of the field. The brief doesn't ask whether that group is skewed
toward one company, one era of Dave's career, or one flavor of analytics
work (e.g. heavy on ex-colleagues from a single employer). A skewed
seed group would bias early coverage in a way attentive readers — the
exact audience this letter is trying to earn trust with — would likely
notice quickly. Carried forward as an open question in `02-brief/brief.md`.
