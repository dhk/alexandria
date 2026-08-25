# Retrieval probe — single-source, hand-run

**What this is.** A cheap retrieval pass run in a Claude Code session to test
whether the open web can answer the retrieval-shaped questions in the two
briefs, before paying for a multi-model commission. It is one source, not
graded, not cross-checked. It is **not** an answer to either brief.

**Citation marking.** The briefs require every citation be marked FETCHED
(retrieved and read during the run) or RECALLED (training data, unverified).
This run needs a third marker the briefs do not have:

- **FETCHED** — the document was retrieved and its text read in this session.
- **SEARCH-SUMMARY** — a search engine returned a summary; the underlying
  page was *not* read. Weaker than FETCHED, stronger than RECALLED.
- **RECALLED** — training data, unverified here.

**Page references.** The document's printed page numbers run two behind the
PDF page index (printed p.34 is PDF page 36), verified against its own page
footers. Both are given below so a citation resolves whichever way the reader
opens it.

## Capability finding: the egress allowlist decides what is FETCHABLE

Page retrieval in this environment is governed by a domain allowlist, not an
open connection. Blocked on attempt: `theeastcut.org`, `sfist.com`,
`en.wikipedia.org`, `www.sfgate.com`. Reachable: `sfplanning.s3.amazonaws.com`.

This is a live constraint on any plan that relies on hand retrieval: news and
reference sites were unreachable, while the agency archive was not. It is also
the reason the East Cut section below is markedly weaker than the survey-grid
section — not because less exists, but because what exists sits on hosts this
session cannot open.

## Primary source obtained

**Historic Context Statement, South of the Market Area**, prepared by Page &
Turnbull, Inc. for the City and County of San Francisco Planning Department.
FINAL, 30 June 2009. 118 pp. Retrieved from SF Planning's archive:
`https://sfplanning.s3.amazonaws.com/archives/documents/372-SOMA_Historic_Context_Statement_06-30-2009.pdf`
sha256 `c5b3e1c26d315ce1e6c586ca074afa2a19cd19958605425a41521a9177e20268`
**FETCHED** — full text extracted and searched in this session.

Source class: primary administrative (an agency-commissioned historic resource
survey, which the brief's hierarchy ranks in tier 2). It is simultaneously a
2009 synthesis, so its own claims about the 1850s are retrospective commentary
and inherit whatever its footnotes rest on. Both facts matter per §3.5.

## Findings against the briefs

### 100 Vara Survey — extent, and a conflict worth registering

> "The name '100 Vara Survey' was bestowed on the blocks south of Market
> because O'Farrell laid out each block as six equal lots measuring 100 varas
> square." — printed p.2, note 3 (PDF page 4). A vara is given as approximately 33 inches. **FETCHED**

> "From Yerba Buena Cove west to 1st Street, the street grid replicated the
> 50 Vara Survey north of Market Street but from 1st Street west to 5th
> Street, O'Farrell adhered to the larger blocks of the 100-Vara Survey. This
> map shows that the grid initially ended at 5th Street, where it encountered
> vast tidal marshes." — printed p.18 (PDF page 20), citing *The Original and Authentic Plan of San
> Francisco* (1847). **FETCHED**

**CONFLICT.** A web search summary reports, on the authority of "city
documents from 1945", that the 100 Vara District runs "from the south side of
Market Street to the Ferry", and that the South of Market area is "officially
known as 100 Vara" (**SEARCH-SUMMARY**, page not read). Page & Turnbull place
50 Vara blocks between Yerba Buena Cove and 1st Street, with 100 Vara only
from 1st to 5th. These are materially different extents for the same name.

Unadjudicated. Resolving it needs the 1847 plan itself and the 1945 city
document, neither read here. This is exactly the disagreement §3.4 says to
preserve rather than resolve, and it appeared on the first pass.

### Second Street Cut, 1869

> "The fate of the South of Market Area as an industrial district was further
> solidified by the completion of the Second Street Cut in 1869. Constructed
> by private investors to ostensibly improve access from Market Street to the
> Pacific Mail Wharf at 1st and Brannan streets, the cut was crudely blasted
> through the center of Rincon Hill, transforming what had been a semi-rural
> lane over the top of the hill into a wide thoroughfare suitable for teams of
> horses at street grade. The cut physically damaged several properties and
> significantly impaired its desirability to the remaining residents who lived
> on Rincon Hill, the lone upper-class enclave in the South of Market Area."
> — printed p.34 (PDF page 36). **FETCHED**

On why Rincon Hill's wealthy did not stop it, the document quotes a **1928**
San Francisco Chronicle article: an 1867-68 State Legislature act authorised
the supervisors to modify the grade of Second Street, while the same session
granted 30 acres of submerged Mission Bay land to the Western and Southern
Pacific; the Chronicle suggests "wheels within wheels" and that some nominal
opponents may have been quietly assisting. — printed p.35 (PDF page 37). **FETCHED**

Note the evidence class: a 2009 document quoting a 1928 newspaper
speculating about 1868. Page & Turnbull hedge it themselves ("may shed some
light on what may have really happened"). Retrospective commentary at two
removes; usable as testimony about the 1928 understanding, not as evidence of
1868 intent.

### Happy Valley — a datable extent in named streets

> "A protected valley in the middle of the sand dunes bounded by Market,
> Howard, 1st, and 2nd streets soon became known as 'Happy Valley' among
> pioneer miners who erected tents and temporary wood houses in the area."
> — printed p.20 (PDF page 22). **FETCHED**

Four named bounding streets. Precision: approximate polygon (the source gives
edges but the name was colloquial). Register: pioneer miners — vernacular, not
official.

### Pleasant Valley — attested, and the brief's conditional is satisfied

> "Just south of Happy Valley was another valley later called Pleasant
> Valley." — printed p.17 (PDF page 19). **FETCHED**

Brief A listed this conditionally ("if attested alongside it"). It is. Note
"**later** called" — the document marks this as retrospective naming, so it
should not be given an 1849 attestation on this evidence.

### Steamboat Point — 1851

> "As early as 1851, the beach at the foot of 1st Street, which had deep water
> access, became the location of several boatyards, giving the area the name
> Steamboat Point." — printed p.20 (PDF page 22). **FETCHED**

### Tar Flat — a name that supersedes two others

> "The increasing dominance of heavy industry in the South of Market Area
> gradually displaced the bucolic Gold Rush-era neighborhoods of Happy Valley
> and Pleasant Valley. Increasingly, the neighborhood became known by another
> name: 'Tar Flat,' the result of by-products generated by the Donahue
> Brothers' gas works located at the corner of 1st and Howard streets. Built
> in 1854, the plant manufactured illuminating gas…" — printed p.30 (PDF page 32). **FETCHED**

This is a directional relationship the brief's schema wants:
Tar Flat `superseded_by`-inverse of Happy Valley and Pleasant Valley, with a
stated physical cause and a dated plant (1854).

### Rincon Point — distinct from Rincon Hill

Appears in the pre-1835 context as one of two headlands sheltering Yerba Buena
Cove, alongside Clark's Point. — **FETCHED**. Supports treating Rincon Point
as a `waterfront_or_shoreline_feature` separate from Rincon Hill's
`topographic_feature`, which Brief A asked to be kept apart.

### "South of the Slot" — the document has a section, not a date

The document uses "South of the Slot" as a section heading and dates the
*reputation* it describes: "By the 1870s and 1880s, the South of Market Area's
reputation as an immigrant and working-class district was firmly established."
— printed p.43 (PDF page 45). **FETCHED**

It does **not** date the term's first use. Its supporting citation for the
earlier period is Charles Lockwood, "South of the Slot," *San Francisco Sunday
Examiner and Chronicle*, 10 June 1979, p.75 — printed p.23, note 51 (PDF page 25). **FETCHED (as a
citation; the 1979 article itself was not read.)** That is a 1979 retrospective
being used for 1850s conditions.

Jack London's story of the same title is **RECALLED** as first published 1909
and collected in *The Strength of the Strong* (1914); a search summary
conflated the two. Neither was verified here. The brief's question — whether
London created, popularised, or recorded the term — remains open.

### "SoMa" — the leading agency document does not date the name

"SoMa" appears 10 times in the 118 pages, and **every occurrence is a modern
planning label**, chiefly "Western SoMa Light Industrial and Residential
Historic District". The document never discusses SoMa as a name event, gives
no origin, and gives no first use. **FETCHED (by absence — searched, not
found.)**

Open-web search was worse: the result set was AcronymFinder, Wikivoyage, a
Fandom wiki, Nextdoor, a towing company's blog, a realtor's blog and Quora,
and the search backend conceded it had nothing on first print use or who
coined it. The SoHo-imitation story circulates sourced to nobody.
**SEARCH-SUMMARY.**

**Conclusion for the commission:** this question is not answerable by
retrieval, at any price, by any tool that reads the open web. It needs a
newspaper database.

### The East Cut — recent, covered, but hosted where this session cannot read

All **SEARCH-SUMMARY**; every underlying page was blocked.

- Body was originally the **Greater Rincon Hill CBD**, renamed the East Cut
  CBD roughly two years in, reported as **2017**. A Chronicle item dated
  **2018-09-30** appears in results.
  **This contradicts the "2018" I wrote into Brief B's task text.** The
  adoption year must be pinned before either is cited.
- Stated derivation matches the brief's premise: the Second Street Cut, the
  levelling of Rincon Hill's high point to move goods to the water.
- Scale: ~4,500 constituents; "months of outreach"; ~6,000 units added in the
  prior decade.
- Reception: a 2018 survey reportedly found ~90% of residents thought the name
  was "dumb" — instrument, N and author all unknown. Not citable as it stands.
- By **September 2024** the name had reportedly disappeared from Google and
  Apple Maps — which speaks directly to Brief B's question of whether anyone
  beyond the coining body adopted it.

## What this changes about the commission

1. **Case Five (The East Cut) is mostly a retrieval problem, not a reasoning
   problem.** It does not need three frontier models. It needs an operator who
   can open `theeastcut.org` and the Chronicle, plus one archive check on the
   adoption year.
2. **Case One (SoMa's first print use) cannot be retrieved.** Neither the
   agency's own context statement nor the open web has it. Commissioning
   models to search for it will produce a confident wrong date. It should be
   specified as a gap and routed to a newspaper database.
3. **The survey-grid and Second Street Cut material is already largely in
   hand** from one document, and that document's footnotes name the next
   sources to pull.
4. **A conflict register has content before any commission has run** — the
   100 Vara extent disagreement above.

The judgment-heavy work the briefs ask for — place-class assignment, extent
precision, adjudicating the 100 Vara disagreement, keeping survey meaning
apart from social meaning — is untouched by this probe and remains the real
case for a commission.

## Gaps this probe could not close

Ranked by how much the gazetteer's integrity depends on them:

1. First print attestation of "SoMa" and of "South of the Slot" — needs a
   digitised newspaper database with full-text search over the SF dailies.
2. The 100 Vara extent conflict — needs *The Original and Authentic Plan of
   San Francisco* (1847) and the 1945 city document.
3. The East Cut adoption record — CBD formation and renaming documents, and
   the Chronicle coverage, all on hosts unreachable here.
4. The 1979 Lockwood article, used by Page & Turnbull for 1850s conditions and
   not read here.
5. Sanborn sheets, block books and city directories — not attempted; not
   text-indexed and largely not on the open web.

## What would change this answer

Reading the sources named in the gaps list. In particular, a single
full-text newspaper search could move Case One from "unanswerable" to
"answered", and would invalidate this document's central negative claim —
which is the outcome to hope for.

---

# Second pass — the SF Planning S3 archive

Added after the first pass, same session, same markers.

## Capability finding, corrected

The first pass concluded from five domains that news and reference hosts are
blocked and agency archives are not. That was half right and the reasoning was
wrong. **The allowlist is by host, not by content class.** Newly tested:

- `www.sfheritage.org` — BLOCKED (a preservation organisation, not news)
- `archives.sfplanning.org` — BLOCKED (SF Planning's *own* archive host)
- `sfplanning.s3.amazonaws.com` — REACHABLE

SF Planning is both blocked and reachable depending on which host serves the
file. What is reachable is the S3 bucket, and the entire SF Planning document
archive appears to sit in it — EIRs, area plans, historic context statements,
Historic Preservation Commission packets. That is a large, citable corpus
available to this session, and it was found only by testing rather than
inferring.

## Second source obtained

**Central SoMa Plan Draft EIR**, Section IV.C, Cultural and Paleontological
Resources. San Francisco Planning Department, Case No. 2011.1356E, December
2016. 70 pp.
`https://sfplanning.s3.amazonaws.com/sfmea/CentralSoMaPlanDEIR_09-iv-c-cultural.pdf`
**FETCHED** — full text extracted and searched in this session.

## New evidence

### The 50 Vara Survey is older than O'Farrell, and has a named author

> "On the north side of Market Street, O'Farrell laid out blocks which measured
> 50 varas on a side (a vara is a Spanish unit of measurement that
> approximately corresponds to 33 inches), consistent with Swiss sailor and
> surveyor Jean Jacques Vioget's original 1839 '50-Vara survey' of the area
> around Portsmouth Square. South of Market Street, O'Farrell created the
> '100-Vara Survey,' with blocks that were twice as long and twice as wide as
> those to the north." — p. IV.C-5 (PDF page 5). **FETCHED**

This dates the 50 Vara name to **Vioget, 1839** — eight years before
O'Farrell, and attached to a different surveyor and a different part of the
city. Page & Turnbull do not give this. It matters for Brief A, which listed
the 50 Vara Survey only "where it bounds the 100 Vara": on this evidence it is
a separate name event with its own author and date, not a boundary condition.

Also here: O'Farrell's Market Street was laid out **120 feet wide**, on a
diagonal connecting Yerba Buena Cove to Mission Dolores.

### CONFLICT 2 — Happy Valley's extent

> "During the Gold Rush, the majority of development south of Market Street
> was concentrated in 'Happy Valley,' located along the shoreline —
> approximately First Street — between Market and Mission Streets, and
> 'Pleasant Valley' to the south. Both of these areas were framed on the west
> by a ridge of sand dunes located east of what is today Second Street."
> — p. IV.C-5 (PDF page 5). **FETCHED**

Set against Page & Turnbull (2009), printed p.20: Happy Valley was "bounded by
Market, Howard, 1st, and 2nd streets".

The two official documents give different southern edges — **Mission Street**
(2016) versus **Howard Street** (2009). Mission lies north of Howard, so the
2009 extent reaches roughly a block further south. The western framing also
differs in kind: 2009 gives a street edge (2nd), 2016 gives a landform (a dune
ridge east of present-day 2nd).

Unadjudicated. Neither is a contemporaneous source; both are modern syntheses,
so this is a disagreement between two retrospective readings and resolving it
means going to whatever each rests on. It is exactly the case §3.4 exists for,
and it is the second such conflict found without any commission having run.

### Rincon Hill's height — a precision difference, not a conflict

Central SoMa DEIR: Rincon Hill rose "to more than 100 feet near the
intersection of Second and Harrison Streets" (p. IV.C-5). Page & Turnbull:
"the 150-foot outcropping of Rincon Hill" and "over 150' above San Francisco
Bay". These are not inconsistent — 150 satisfies "more than 100" — but only
one gives a figure precise enough to use. Recorded so a later reader does not
mistake the pair for a contradiction.

### "South of the Slot" — a second absence

The term appears **zero times** in 70 pages of cultural-resources analysis.
"SoMa" appears 147 times, all as the modern plan label. **FETCHED (by
absence.)**

Two independent agency documents now use "SoMa" freely as a designation and
neither treats it as a name with a history. That strengthens the first pass's
conclusion: the agency record will not date this name, and the question should
be routed to a newspaper database rather than commissioned.

### A named archaeological source for Tar Flat and Rincon Hill

Cited at note 106: Praetzellis, Mary and Adrian Praetzellis (eds.), *Tar Flat,
Rincon Hill, and the Shore of Mission Bay: Archaeological Research Design and
Treatment Plan for SF-480 Terminal Separation Rebuild*, 1992. **FETCHED (as a
citation; not read.)**

A whole volume named for two of the pilot's places. Highest-value unread lead
found so far.

## Revised gaps

Unchanged at the top: the first print use of "SoMa" and of "South of the Slot"
still need a newspaper database, and two agency documents failing to date them
is now positive evidence that no amount of agency material will.

Added:

- **Praetzellis & Praetzellis 1992** — named for Tar Flat and Rincon Hill; not
  located or read.
- **Vioget's 1839 50-Vara survey** — now dated and attributed, but the survey
  itself is unread; its extent is asserted here only as "the area around
  Portsmouth Square".
- **The Happy Valley extent conflict** — needs whatever the 2009 and 2016
  documents each rest on.
- **The rest of the S3 archive** — Historic Preservation Commission packets,
  the Central SoMa historic context statement adopted 16 March 2016, area
  plans for East SoMa, Rincon Hill and Transbay. Reachable, unexamined, and
  the cheapest remaining source of evidence for this project.
