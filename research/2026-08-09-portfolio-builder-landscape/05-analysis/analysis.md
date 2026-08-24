# Analysis: Portfolio-website brand-interview pipeline — differentiation and build recommendation

Interpretation built on
[`../03-runs/claude-2026-08-09/response.md`](../03-runs/claude-2026-08-09/response.md)
(Q1–Q6 raw findings) and the source material. This is judgment, not
additional evidence — kept in a separate file per `AGENTS.md` rule 7.
Single-source: treat every claim below as one model's read of the
findings, not a graded consensus.

## Answering Q7: does the build-vs-buy recommendation hold up?

**Yes, and the verification pass sharpens it rather than overturning
it.** The recommendation drafted before this investigation was: buy or
integrate resume/LinkedIn parsing, colour math, and hosting/page
rendering as commodity; build the adaptive interview logic, the
audience-definition step, and the reasoning layer that turns a brand and
audience brief into a palette/layout proposal with a stated rationale.
Every question in this pass either confirms a piece of that or adds a
constraint to it, none contradict it:

- **Q2 confirms the core gap.** A direct hunt for a product that chains
  all five steps — not a re-read of the same listicles a first pass
  already covered — turned up nothing. The nearest miss, Cactus, is
  admin automation with a website as a line item, not a brand-interview
  pipeline. This is the strongest evidence in the whole investigation
  that the reasoning layer is genuinely unclaimed territory, because the
  search was adversarial by design (see `01-brief/brief.md` Q2).
- **Q3 sharpens "build the audience step" into "build it from
  scratch."** The gap isn't just unsearched, it's structurally
  mislabeled everywhere it's adjacent to: B2B ICP tools answer a
  different question (who should a business sell to) and human
  web-design questionnaires ask the right question but produce a form a
  person reads, not a software artifact that shapes a palette or content
  decision. There's no existing pattern to adapt — this has to be
  designed, not borrowed.
- **Q5 lowers the bar to validate the reasoning layer specifically.**
  Roughly $0.10–$0.30 in LLM cost and 2–5 weeks of one engineer's time
  to prototype interview → brief → proposal, once hosting/parsing/colour
  are treated as bought rather than built. That's a materially smaller
  and faster bet than the generic "12–24 weeks minimum" custom-build
  figure implies, because that figure assumes building the whole stack.
  The practical implication: there's no reason to wait for more
  certainty before prototyping this piece — it's cheap enough to build
  the smallest version and see if the chain holds together end to end
  before investing in anything downstream.
- **Q6 adds a constraint to "buy/integrate parsing," not a
  contradiction.** "Buy commodity resume/LinkedIn parsing" was framed
  generically enough to cover a live-scrape implementation. It shouldn't
  be. See below.

## LinkedIn data — legal/ToS risk, and the resulting hard constraint

LinkedIn's User Agreement (§8.2) bars scraping, crawling, or any
automated means of accessing the platform or copying profile data,
without exception for scraping one's own profile. Historically this got
framed as a criminal-exposure question via the Computer Fraud and Abuse
Act, but hiQ Labs v. LinkedIn closes most of that off: the Ninth Circuit
held — twice, including after a Supreme Court remand — that scraping
publicly accessible pages (no login required) doesn't violate the
CFAA's "without authorization" provision, because that provision targets
circumventing something like a password wall, not violating a platform's
stated wishes.

That doesn't make scraping ToS-compliant. It shifts what's actually at
stake: LinkedIn can still enforce the clause as an ordinary contract
breach, and — the practically certain consequence — restrict or ban the
account doing the scraping. Enforcement in practice tracks scale and
commercial intent: heaviest against services scraping and reselling data
at scale (hiQ itself was a commercial data broker), lightest for an
individual accessing their own visible data at normal browsing speed.
2026 enforcement is the same policy, applied more aggressively.

None of that risk is necessary for this product. The interview step
needs the *content* of a user's own LinkedIn profile, not the ability to
fetch arbitrary profiles at scale — and getting that content doesn't
require touching LinkedIn's systems at all.

**Hard constraint, recorded here and in `topic.yaml`'s `notes`, carried
into any downstream build from this research:** the interview step must
never scrape LinkedIn. It must require the user to supply their own
profile data directly — pasted text, a one-time fetch of a URL the user
themselves provides interactively (not a background/bulk crawl), or
LinkedIn's own official "Get a copy of your data" export. Any of those
gets the same interview-seeding content with none of the ToS exposure,
and is more reliable besides, since LinkedIn actively fights automated
access.

This is a product requirement, not a prior-art finding, so it doesn't
carry a Q2–Q6-style verdict — but it's the one piece of this
investigation with a direct, immediate implication for how step 1 gets
built, which is why it's promoted out of the findings and into the
constraint the whole investigation is now scoped around.

## Open questions this single-source pass cannot resolve

- Whether a Silver-tier dispatch through Alexandria's own multi-model
  commission flow would surface a genuine counter-example to Q2 that a
  single search pass missed — the whole reason for wanting that dispatch
  in the first place. Blocked on
  [dhk/minority-report#33](https://github.com/dhk/minority-report/issues/33)
  being fixed, not on anything this pass could resolve directly.
- Q5's cost estimate is a rough order-of-magnitude figure from current
  list pricing, not a costed technical design — it should be re-derived
  against an actual prompt design once one exists, not treated as a
  budget.
- Whether LinkedIn's official data-export flow (recommended in the hard
  constraint above) is actually usable inside a product's onboarding —
  i.e. whether the export completes fast enough, and in a format easy
  enough to parse, for a first-session interview flow. Not researched
  here; a concrete blocker if the export takes hours/days as LinkedIn's
  exports sometimes do.

A Silver-tier upgrade of this investigation — dispatching
`01-brief/brief.md` through Alexandria's own `begin_research`/
`run_research` commission flow once it can complete — would meaningfully
de-risk Q2 and Q4 in particular, since a single search pass (even an
adversarial one) is a weaker check for "nothing exists" than three
independent models with live web search and a grading pass. That
dispatch was attempted three times here and failed each time; see
`topic.yaml`'s `notes` and the linked issue.
