# Findings: Portfolio-website brand-interview pipeline

Raw findings for [`../../01-brief/brief.md`](../../01-brief/brief.md)'s
Q1–Q6, from two single-source passes (2026-08-08 web search; 2026-08-09
verification). Preserved as received — interpretation and the Q7
synthesis verdict live in
[`../../05-analysis/analysis.md`](../../05-analysis/analysis.md), kept
separate per `AGENTS.md` rule 7.

## Q1 — Landscape by pipeline step

**Step 1+5 — resume/LinkedIn-to-site parsers, one-shot.** Butternut AI
(parses a resume upload or free-text bio into a responsive site with a
visual editor and an AI agent for further edits); SpaceLoom (free, no
signup, resume PDF to site); Artfolio (PDF/DOCX/text into one of 8 fixed
designs); FolioGenerator; QuickCV (generates a site from its own built-in
resume builder); Kleap, MakeMyAISite, Xelta, Seekario (LinkedIn URL to
portfolio, largely interchangeable long tail). All one-shot: input once,
template out. None loop back for clarification or ask who the site is
for. [Sources: resumly.ai, spaceloom.co, artfolio.tech, foliogenerator.com,
quickcv.io, kleap.co, makemyaisite.com]

**Step 1-2 — personal brand voice/discovery AI, for ongoing content.**
Bloomberry (learns voice from existing writing, not tone sliders);
SelfBrand AI (research-first: tracks Reddit/LinkedIn/Quora for the user's
niche, voice-trained writer plus engagement assistant); Junia, Hoppy
Copy (analyze sample content into a style profile for future marketing
copy). None hand a defined brief to a design or build step — the loop
ends at "write more content like this." [Sources: bloomberry.ai,
selfbrand.app, junia.ai, hoppycopy.co]

**Step 3 — audience definition.** Only generic marketing-persona
templates found (Miro, Freshworks) — background, goals, pain points,
communication preferences — none portfolio-specific, none software (see
Q3 for the verification-pass follow-up on this). [Sources: miro.com,
freshworks.com]

**Step 4 — palette, brand identity, AI-themed site builders.** Two
sub-tiers. Dedicated colour/identity tools: Khroma (rates 50 colours the
user likes, learns taste, generates unlimited combinations); Coolors
(fast generation, extracts a palette from an uploaded reference image);
Huemint (full brand colour systems, previewed on real UI components, not
just swatches); Looka (logo + brand kit, 300+ collateral templates);
Tailor Brands (algorithm matches fonts/colours/icon style to design
trends). AI site generators that auto-theme from onboarding: B12
(~10 theme options from a questionnaire), 10Web, Dora, Durable, Framer
AI, Wix ADI — all theme from style prompts/reference URLs, not from a
biographical interview. Recommended manual workflow found repeatedly:
Khroma to explore → Coolors to refine → Huemint to build the full system
→ an accessibility checker (Stark) before shipping. [Sources: khroma.co,
coolors.co, huemint.com, looka.com, tailorbrands.com, various 2026
AI-website-builder roundups]

**Step 5 — build, commodity hosting/editor.** Squarespace (~$16/mo,
widest gallery-layout variety, automatic image optimization); Wix
(~$17/mo, maximum flexibility, large app market); Framer ($5–15/mo,
Figma-like editor, design-led); Carrd ($9–19/yr, single page, cheapest);
Webflow (usage-tiered, CMS-grade control); Notion + Super.so (cheapest
no-code path with a real theme editor, lower customization ceiling than
Webflow/Framer). [Sources: squarespace.com, wix.com, framer.com,
carrd.co, webflow.com, super.so]

## Q2 — Does anything chain all five steps?

**Verdict: refuted (no counter-example found).**

Scanned Product Hunt's 2025–2026 AI-software and AI-designer categories,
Y Combinator's Spring/Summer/Fall 2025 batches, and stealth-startup
directories directly, not through SEO listicles. No product was found
that runs a real discovery interview, defines an audience, and proposes
a traceable palette/layout before building.

Nearest miss: **Cactus** (Y Combinator S25) — an AI copilot for
solopreneurs (private chefs, caterers, personal trainers) bundling brand
maintenance, website creation, lead qualification, proposal generation,
and invoicing. $200K+ revenue in 3 months, 40+ paying customers per its
YC launch page. Website creation is one line item in an admin-automation
bundle; there is no discovery interview preceding it and no audience or
palette-reasoning step. Not a counter-example by mechanism, only by
name-adjacency. [Sources: ycombinator.com/launches/NSp-cactus-ai-copilot-for-solopreneurs,
tryfondo.com/blog/cactus-launches]

Also re-checked specifically: Dora AI and Framer AI, for whether either
added biographical/conversational onboarding in 2026 updates. Both still
theme from style prompts and reference images/URLs, not from a discovery
interview — no change from Q1's categorization. [Sources: tooljunction.io,
framer.com/agents]

## Q3 — Is the audience-definition gap real, or mislabeled?

**Verdict: partially confirmed** — the gap for portfolio sites
specifically is real; two adjacent labels exist and neither closes it.

**ICP-generator tools** define a company's target *customer* for B2B
sales outreach — the "ICP – Ideal Customer Profile Generator" custom GPT
builds a profile from a URL; Lemlist's free ICP generator does the same.
Wrong audience type: this is who a business should sell to, not who
should read someone's personal portfolio. [Sources: lemlist.com, custom
GPT store listings]

**Web-design-agency intake questionnaires** (Elementor's, Webfume's)
include "who is your target audience" as one of 12–40 client-onboarding
questions — the right question, asked by human designers, in a manual
form, not a software step that feeds a content or palette decision.
[Sources: elementor.com/blog/website-design-questionnaire,
webfume.com/blogs/development-articles/web-design-client-onboarding-questionnaire]

No tool was found that defines an audience specifically for a personal
portfolio site and then uses that definition to shape site content or
design.

## Q4 — Stealth or emerging competitive threats

**Verdict: no equivalent found.** No team beyond Cactus (Q2, not a real
match) surfaced across the same Product Hunt / YC / stealth-directory
scan claiming to build this combined pipeline, in any stage from launched
to stealth.

## Q5 — LLM-orchestrated interview-pipeline economics

Current flagship API pricing (GPT-4.1-tier: $2.00 / $8.00 per million
input/output tokens) reframes the generic build-vs-buy benchmarks
(custom site $1,500–$10,000+; starter kit $199–$499 cutting MVP time
50–80%; custom build 12–24 weeks minimum vs. SaaS live in 2–4 weeks;
>80% of SaaS startups fail on product-market fit, not tech — all still
directionally useful as an outer bound, but not specific to this
pipeline's shape). [Sources: appinventiv.com/blog/build-vs-buy-software,
designrevision.com/blog/custom-saas-development]

A structured multi-turn interview accumulates context each turn — a
10–15 exchange interview plausibly reaches 15–25K cumulative tokens —
putting that stage at roughly $0.05–$0.15 per user at current flagship
pricing. A single larger call for the palette/layout proposal (full
brief as context, structured output) adds roughly $0.02–$0.05. Total:
roughly $0.10–$0.30 per completed pipeline run, likely toward the low end
if a cheaper model handles interview turns and only the synthesis step
calls a flagship model. [Source: cloudzero.com/blog/gpt-4-api-cost]

Timeline: because this scope deliberately excludes hosting, parsing, and
colour infrastructure (bought, not built — see Q6 and the analysis), a
working prototype of just the interview → brief → proposal chain is
realistically 2–5 weeks for one engineer, well inside the 12–24-week
figure that assumes building the whole stack.

## Q6 — LinkedIn data: legal/ToS risk for the parsing step

**What the User Agreement says.** Section 8.2 bars members from
developing, supporting, or using "software, devices, scripts, robots, or
any other means or processes... to scrape the Services or otherwise copy
profiles and other data from the Services," and separately from using
"bots or other automated methods to access the Services." No carve-out
for scraping one's own profile. [Source: magicalapi.com/blog/linkedin-tools-insights/is-it-legal-to-scrape-linkedin]

**hiQ Labs v. LinkedIn.** The Ninth Circuit held (twice — once before and
once after a Supreme Court remand for reconsideration in light of *Van
Buren*) that scraping publicly accessible pages (no login required) does
not violate the Computer Fraud and Abuse Act's "without authorization"
provision, because that provision targets circumventing something like a
password wall, not violating a platform's stated wishes. This closes off
LinkedIn's ability to use the CFAA as a blanket weapon against scraping
public data — it does not make scraping ToS-compliant. [Sources:
fenwick.com/insights/publications/hiq-labs-scrapes-by-again...,
calawyers.org/privacy-law/ninth-circuit-holds-data-scraping-is-legal-in-hiq-v-linkedin]

**What's still live risk.** Breach of contract (LinkedIn can still sue
under ordinary contract law, separate from CFAA, for a ToS violation);
account restriction or ban (the practical, near-certain consequence of
detected automation); and in some cases DMCA/trespass-adjacent claims,
though these are less commonly the actual enforcement lever.

**Risk gradient.** Enforcement in practice tracks scale and commercial
intent: highest for services that scrape and resell/redistribute LinkedIn
data at scale (hiQ itself was a commercial data broker); lowest for an
individual accessing their own visible data at normal browsing speed.
2026 enforcement posture: same policy, more aggressive detection, per
multiple 2026 scraping-legality roundups. [Sources: nubela.co/blog/is-scraping-linkedin-legal-in-2026,
connectsafely.ai/articles/is-linkedin-automation-safe-tos-scraping-guide-2026]

## Open gaps

- Q2/Q4's scan did not extend to non-English-language markets or
  accelerators outside YC (Techstars, on-deck, etc.) — out of scope per
  the brief, but worth flagging if this research is revisited.
- Q5's cost estimate assumes current (2026) flagship pricing; token
  costs have historically dropped over time and this figure should be
  re-run before being used in a financial model rather than a rough
  feasibility check.
- No hands-on testing of any tool in the comparison set — all findings
  are sourced from public marketing pages, documentation, and
  third-party reviews, consistent with this being a Bronze single-source
  pass (see `topic.yaml`).
