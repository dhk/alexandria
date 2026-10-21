# San Francisco place names — SoMa, The East Cut, and the 100 Vara District

**Question.** Three that survived a prior pass, for a version-controlled
gazetteer of San Francisco place names: when does "SoMa" first appear in print
and was it really copied from SoHo; what is the actual adoption record for "The
East Cut"; and how wide was the 100 Vara District, where a 2009 planning
document and a 1945 city document describe materially different areas under the
same name.

**Material examined.** Newspaper and magazine archives, the East Cut CBD's own
publications, SF Board of Supervisors proceedings, San Francisco Assessor's
block maps, and Wikipedia's revision history. Carried in as already settled and
not re-derived: seven findings from SF Planning's *Historic Context Statement,
South of the Market Area* (Page & Turnbull, 30 June 2009).

**Answered by** the Perplexity Agent API via MCP — deep-research preset, with a
fast preset substituted on three calls after repeated timeouts. **Not graded**,
not cross-checked, no claim scoring. **Run** `perplexity-2026-08-24`, 10 calls,
5 usable responses — followed by `operator-verification-2026-08-24`, a
no-model pass that read the primary sources directly and produced most of what
this investigation actually establishes.

## The verdict

**Q1 — unsettled, with a firm floor and a better answer than expected on the
SoHo question.** The earliest verified print use is the *Los Angeles Times*,
6 November 1988. The substantive finding is what it says: SoMa is "bordered by
Market, 1st, Townsend and 12th streets" — **excluding everything east of 1st**.
At its earliest verified use the acronym named a sub-area, not the survey
district, so SoMa and South of Market should not be treated as synonyms at any
date without evidence for that date.

**Q2 — resolved into three events that were being conflated.** Branding launch
**8 June 2017**; Google Maps adoption **spring 2018**; legal district-name
change by **Resolution 492-19, 19 November 2019**. The exact board vote was
never found.

**Q3 — adjudicated on naming, not on geometry, and the two were never the same
question.**

## The finding that generalises

The SoHo-imitation claim is not merely unattributed. It is traceable:

> It is in the **first revision** of Wikipedia's *South of Market* article,
> **5 March 2004**, hedged by its own author as "probably", unsourced then,
> tagged `{{Citation needed}}` since **July 2013**, and unsourced still.

That is a different and more useful class of finding than "circulates
unattributed" — it names the vector. The same shape appears twice more in this
investigation. The "1945 document" that says South of Market is "officially
known as 100 Vara" does not say that; a Wikipedia sentence adjacent to the
correctly-cited one does, and it is itself tagged Citation-needed. The "90%
thought it was dumb" survey is a paraphrase of the *NYT*'s "90 percent disliked
the name", which is itself the organiser's own account of an instrument nobody
has produced.

**Three of this investigation's four headline claims turned out to be citation
laundering.** For a gazetteer whose governing principle is that a name is a
claim by a source at a date, that is the result worth keeping.

## What the block book settles

The 100 Vara extent dispute is largely a **category error** between an
administrative designation and a surveying description.

On **administrative extent**, the 1945 reading holds. Assessor's sheets
**3717** (Mission/Spear/Howard/Main) and **3746** (Folsom/Main/Harrison/Beale)
lie **east of 1st Street** and are headed "100 VARA BLK. 325" and "332". AB 3746
measures **275.00 × 275.00 ft** — exactly 100 varas square, where a 50-vara
module would be 137.5 ft.

On **1847 geometry**, nothing is adjudicated, because **nobody in this
investigation ever saw the 1847 plan.** The block sheets are modern, and much of
the land east of 1st Street was under Yerba Buena Cove in 1847.

## Read order

1. [`05-analysis/analysis.md`](05-analysis/analysis.md) — **start here.** All
   three questions, with a three-tier provenance mark on every source.
2. [`03-runs/operator-verification-2026-08-24/evidence.md`](03-runs/operator-verification-2026-08-24/evidence.md)
   — the primary sources, quoted verbatim, with rights notes and checksums.
3. [`00-topic/source-material.md`](00-topic/source-material.md) — the operator's
   brief, verbatim.
4. [`01-brief/brief.md`](01-brief/brief.md) — the commission as dispatched,
   including the scope reductions the timeouts forced.
5. [`03-runs/perplexity-2026-08-24/`](03-runs/perplexity-2026-08-24/) — the raw
   provider responses, including
   [the one that is a false negative](03-runs/perplexity-2026-08-24/response-q3b-1945-document.md).

## How far to trust it

**Bronze. Single provider, not graded, no second reader.**

**The provenance marks are three-tier, not two.** The operator's brief asked for
read / not-read. Routing the work through a research agent creates a third
state — *the agent says it read it, nobody else opened it* — and collapsing it
into either of the other two would be dishonest. The analysis marks every source
**READ (first-hand)**, **AGENT-REPORTED**, or **NOT READ**. That split is what
makes the quality gradient visible, and it is uneven on purpose.

**Q2 is the weak section and says so at the top.** It rests almost entirely on
agent-reported sources; not one was independently opened. Q1 and Q3 carry
first-hand verification and are correspondingly stronger. Do not cite Q2's
details at the same confidence as Q3's.

**The instrument failed on the material that mattered most.** Five of seven
deep-research calls timed out at the client's 300s ceiling — accepted
server-side, so in all likelihood billed while returning nothing. Three Q3 calls
were downgraded to a weaker preset, and one of those returned a **confident
false negative**, reporting the 1945 document unfindable across five named
archives. It is retrievable, and a footnote chase found it in minutes. That
response is preserved unedited because a provider failure is an observation to
record, not a reason to retry quietly into a better-looking result.

**No cost is recorded.** The provider returned no usage metadata on any call.
Estimating it would have been easy and wrong, so the field is empty.

**The four-sheet sample is a sample.** The 100 Vara series was not walked to its
limits, so no boundary is claimed for it — only that it demonstrably includes
blocks east of 1st Street. Three mutually inconsistent extents now sit in the
record (Page & Turnbull's 1st-to-5th, the 1945 Assessor's to-the-Ferry, SF
Memory's Ninth-Street-to-the-Bay) and are carried as three dated claims rather
than reconciled.

## What a Silver upgrade would need

- **The 1847 O'Farrell plan, actually viewed.** Everything about the Page &
  Turnbull account turns on it. Search the David Rumsey and Bancroft catalogs
  under O'Farrell rather than under "The Original and Authentic Plan of San
  Francisco", which did not resolve in any catalog searched.
- **A *Chronicle* or *Examiner* full-text run, 1975–1990**, for SoMa / SOMA /
  So-Ma. The single most likely home of an earlier use, and entirely unsearched.
- **A second model on Q2**, whose sources are all agent-reported.
- **The 100 Vara series walked to its limits** in the Assessor's block maps,
  which would convert a four-sheet sample into an actual boundary and settle the
  5th-versus-9th-Street disagreement empirically.
