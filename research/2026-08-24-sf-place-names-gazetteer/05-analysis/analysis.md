<!--
Provenance: generated interpretation. This is Alexandria's analysis artifact,
not raw provider output. Raw provider responses are under 03-runs/.
-->

# San Francisco place names — three unresolved questions: research results

Date of research: 2026-08-24
Method: three Perplexity deep-research passes (`sonar` deep-research preset), plus
direct first-hand retrieval of primary sources by Claude Code where the research
passes left a gap.

## How to read the provenance marks

This report distinguishes **three** evidence tiers, not two. The brief asked for
read / not-read; running the work through a research agent adds a middle tier that
must not be collapsed into either.

- **READ (first-hand)** — I retrieved the document or image in this session and
  read it myself. Quotes are transcribed from the retrieved text or image.
- **AGENT-REPORTED** — the Perplexity research pass says it read the page. I did
  **not** open it. Treat as a lead with a locator, not as verified.
- **NOT READ** — known only from a search snippet or a catalog record.

Contemporaneous vs retrospective is marked per claim.

---

# Q1. When does "SoMa" first appear in print?

## Verdict

**Unsettled, with a firm floor.** The earliest use I verified first-hand is
**6 November 1988**, in the *Los Angeles Times* — and it is a genuinely useful
data point, because at that first verified use **"SoMa" was not a synonym for
"South of Market."** The *Times* defines it as a warehouse district "bordered by
Market, 1st, Townsend and 12th streets" — a boundary that **excludes everything
east of 1st Street**, i.e. excludes Rincon Hill, South Beach and Steamboat Point.
So the acronym enters the verified record as a name for a *sub-area* with an
industrial/retail character, not for the whole 1847 survey district. The register
is journalistic and commercial: a travel-section piece on discount clothing
outlets, using "nicknamed" — the writer is reporting a name in circulation, not
minting one, which pushes actual first use earlier than 1988 by an unknown margin.
The SoHo-imitation claim is, as the brief suspected, **unattributed** — and I can
now say something sharper than that: I traced its mass-circulation vector.
The strongest earlier candidate, *SOMA* magazine (founded 1986 or 1987), remains
**unverified** — no first issue, masthead or library holding was located.

## Evidence

### The earliest verified use — 6 November 1988

**Contemporaneous. READ (first-hand).** "Warehouse District Caters to
Budget-Minded," *Los Angeles Times*, 6 November 1988. I retrieved the article and
transcribed the passage verbatim:

> "The warehouse district, nicknamed **SoMa (for south of Market)**, is an area of
> factory buildings bordered by Market, 1st, Townsend and 12th streets. The
> district is unglamorous and off the beaten tourist path."

Embedded schema.org metadata in the page gives `"datePublished":
"1988-11-06T08:00:00.000Z"` and `"headline":"Warehouse District Caters to
Budget-Minded"`. **No byline is exposed** in the archive page. URL:
https://www.latimes.com/archives/la-xpm-1988-11-06-tr-170-story.html

Three things this settles, and one it does not:

1. **Register (a).** Anonymous journalist, travel/shopping feature. Not a
   developer, planner, gallery or resident. The word "nicknamed" is doing real
   work — it frames SoMa as vernacular already in use, and as informal.
2. **Extent (c).** Market / 1st / Townsend / 12th. This is *not* South of Market.
   It stops at 1st Street on the east. **Do not treat SoMa and South of Market as
   coextensive at 1988.**
3. It does **not** establish priority. An LA paper reporting an SF nickname is
   evidence the name was already current in San Francisco.

### Currency by 1989

**Contemporaneous. AGENT-REPORTED — I did not open this.** *San Francisco Bay
Guardian*, vol. 24, no. 8, 29 November 1989, used "SOMA nightspots/restaurants" in
a Potrero Court Apartments advertisement while the editorial matter elsewhere in
the issue still used "South of Market." Internet Archive identifier `Issue24.08`,
reported at pp. 87 and 33–36.
https://archive.org/stream/Issue24.08/Issue24.08_djvu.txt

Note the register split, if it holds up on inspection: **advertising adopted the
short form before the editorial voice did.** That is a pattern worth testing
against more issues — it would make SoMa's early currency commercial rather than
journalistic. Per rule 6, the advertisement is evidence of what the advertiser
wanted "SOMA" to connote (nightlife, desirability), not of a boundary.

### The *SOMA* magazine candidate — 1986–1987, unverified

**Retrospective. AGENT-REPORTED.** Ali Ghanbarian's biography page (dated
1 October 2023, https://alighanbarian.com/about-2/) says he began publishing *SOMA*
in **1986** and claims he "coined the term SoMa." A 21 May 2009 *Magazine Rack*
piece reproduced on the magazine's press page says it was first published
"22 years ago," implying **1987**.

**Weight: low, and self-interested.** No first issue, volume/number, masthead
scan or library holding was located. The research pass checked the *Subject
Catalog of Periodicals, Including Selected Serials*, San Francisco Public Library,
1987 (Internet Archive `subjectcatalogof1987sanf`) and found **no OCR entry for
*SOMA***, which fails to corroborate the magazine's existence at that date. A
2023 self-published coinage claim with no contemporary document behind it cannot
carry an origin question. The defensible statement is: *SOMA* magazine is a
plausible earlier candidate bounded 1986–1987, unproven.

### (b) The SoHo-imitation claim — unattributed, and I traced its vector

This is the most substantive new finding on Q1.

**READ (first-hand).** The claim circulates unattributed, and its principal
vector of mass circulation is **Wikipedia, unsourced from the article's first
day.** I pulled the article's revision history via the MediaWiki API. The
**very first revision** of "South of Market, San Francisco" —
**5 March 2004, revid 2647532** — already contained it:

> "Many people shorten the name to SOMA or SoMa, **probably in reference to SoHo
> (South of Houston) in New York City.**"

https://en.wikipedia.org/w/index.php?oldid=2647532

The hedge "probably" is the original author's own. No source was given then.
The current article still carries the claim and has carried a
`{{Citation needed}}` tag on it **since July 2013**:

> "there is a trend to shorten the name to SOMA or SoMa,
> probably{{Citation needed|date=July 2013}} in reference to SoHo (South of
> Houston) in New York City, and, in turn, Soho in London."

(Current wikitext, retrieved 2026-08-24 via `action=raw`.)

**Conclusion for the gazetteer:** the SoHo derivation is not a sourced etymology.
It is a 2004 Wikipedia editor's speculation, explicitly hedged, never sourced,
flagged as unsourced for thirteen years, and copied outward from there. It should
be recorded as **a widely repeated conjecture of known origin and no authority** —
which is a stronger and more useful finding than "unattributed."

This does not prove the derivation false. SoHo (1960s–70s) plainly preceded SoMa,
and the acronym-coining fashion is real. It proves only that **nobody has produced
evidence for it**, and that its ubiquity is a citation-laundering artifact.

## What I could not verify for Q1

- **San Francisco Chronicle, 1975–1995** — no issue-level archive search was
  possible. This is the single most likely home of an earlier use and it is
  **unsearched**.
- **San Francisco Examiner, 1975–1995** — Newspapers.com states coverage
  1865–2024, but automated retrieval of historical pages was blocked. Unsearched.
- **San Francisco Bay Guardian, 1975–1988** — the 48hills scanning project states
  not all issues are online. Only vol. 24 no. 8 (1989) was reached, and that by
  the agent, not by me.
- **SF Weekly and San Francisco Sentinel, 1975–1995** — no complete searchable run
  retrieved. The Sentinel's LC catalog record (sn92019400) shows 1986 holdings but
  no searchable text.
- **California Digital Newspaper Collection** — no native OCR search across all
  titles and spelling variants (SoMa / SOMA / So-Ma / So. of Market) was completed.
- ***SOMA* magazine vol. 1 no. 1** — not located in any library catalog.
- **Gallery and club ephemera** — flyers, listings and calendars from South of
  Market venues 1979–1988 were not searched at all. Given that the 1989 Guardian
  hit is an advertisement and the 1988 LAT hit says "nicknamed," ephemera is where
  an earlier use most plausibly sits.

---

# Q2. The East Cut — the adoption record

**Provenance caveat: this section is almost entirely AGENT-REPORTED.** I did not
independently open the East Cut CBD pages, the NYT article, the CBD management
plan or the Board of Supervisors files. Locators are given so each can be checked.

## Verdict

**The year is 2017, and the "2017 vs 2018" confusion is now explainable.** The
name was public by **1 June 2017** and formally launched by the CBD on
**8 June 2017**. The mechanism was **not** a City action and **not** a CBD
renewal — it was a privately commissioned naming-and-branding exercise by the
then Greater Rincon Hill CBD, whose 2015 management plan already ran a 15-year
assessment term to FY2029–30 and was untouched by the rebrand. The recurrent
**2018** date comes from **Google Maps adopting the label in spring 2018**, which
is when most people first encountered it. The **legal** district name changed
later still: the City styled the body "Greater Rincon Hill CBD (dba The East Cut
CBD)" through 2018 and did not change the assessment district's name until
**Board of Supervisors Resolution 492-19, 19 November 2019**. So there are three
defensible dates for three different events, and conflating them is the source of
the disagreement. What remains **unproved** is the exact board vote: no agenda,
minutes or resolution was retrieved, and one December 2017 report says the name
was created "in May."

## Evidence

### Adoption: year and mechanism

- **1 June 2017 — contemporaneous. AGENT-REPORTED.** SFist reported the CBD was
  spending assessment revenue on a branding campaign — new name, logo, website,
  branded clothing. Executive Director Andrew Robinson called The East Cut "a 21st
  century idea of what a neighborhood should be."
  https://sfist.com/2017/06/01/now_theyre_trying_to_rebrand_rincon/
- **8 June 2017 — contemporaneous, primary as to intent. AGENT-REPORTED.**
  "Introducing The East Cut," East Cut CBD: "In selecting The East Cut we have
  created a confident name layered with both heritage and potential." Describes a
  "community effort" of meetings, interviews and public board meetings. **Contains
  no resolution, motion, vote date or tally.**
  https://www.theeastcut.org/introducing-the-east-cut/
- **4 August 2017 — contemporaneous, primary as to intent. AGENT-REPORTED.** "About
  The East Cut Name" lists the process: historical and planning-document review, a
  community meeting, walking tours, stakeholder interviews, street interviews,
  review of MLS listing names, and "numerous publicly-accessible Committee and
  Board meetings." Then this, which matters:

  > "Our process specifically was to determine a name for the CBD itself, and not
  > change the name of any existing neighborhoods within the district's larger
  > boundaries."

  **This contradicts the June launch page**, which repeatedly presents The East Cut
  as a neighborhood. Per rule 6: the August page is the CBD narrowing its claim
  under criticism. Both are evidence of what the CBD wanted at each moment.
  https://www.theeastcut.org/east-cut-name/
- **14 December 2017 — contemporaneous. NOT READ (snippet only).** *San Francisco
  Business Times* reports the name was created "in May." Bounds the vote to
  roughly May 2017; does not date it.
- **2–5 August 2018 — retrospective. AGENT-REPORTED.** The *New York Times*
  reports the board rejected **"Grand Narrows"** and **"Central Hub"** before
  choosing The East Cut, and that Google added the name in spring 2018 at the
  CBD's request.
  https://www.nytimes.com/2018/08/02/technology/google-maps-neighborhood-names.html
- **19 June 2018 — contemporaneous administrative. NOT READ (official search
  summary).** BOS File 180665 still styles the body "Greater Rincon Hill Community
  Benefit District (dba The East Cut Community Benefit District)."
- **19 November 2019 — contemporaneous City action. AGENT-REPORTED via a
  reconstructed legislative record; the signed PDF was not retrieved.** Resolution
  492-19 changed the assessment district's name to The East Cut Community Benefit
  District. **This is a district name change, not the creation of an official City
  neighborhood polygon.**
- **Not a renewal.** The Greater Rincon Hill CBD Management Plan (June/July 2015)
  set a 15-year term to FY2029–30. The 2017 rebrand redrew nothing.
  https://sfelections.sfgov.org/ftp/uploadedfiles/elections/ElectionsArchives/2015/RinconHillCBD/RinconHillCBD_Management_Plan.pdf

### Stated boundaries — and the CBD contradicts itself

Three different geographies from the same organisation:

1. **2015 assessment district (legal, parcel-based).** An irregular perimeter:
   east side of Second from Jessie south to Harrison; Harrison east to Main (with
   parcel exclusions); Main south to Bryant; Bryant east to The Embarcadero; west
   side of the Embarcadero back to Harrison; Steuart from Harrison to Howard;
   Howard to Spear; Spear to Mission; Mission to First; then an irregular return
   through First, Stevenson, Ecker and specified parcel lines to Second.
   (Management Plan p. 25; Engineer's Report p. 13.) **Controlling for assessed
   parcels only.**
2. **Current CBD "District Map" page (undated).** "Market Street to Harrison
   Street" north–south, "Second Street to Steuart Street" east–west. A clean
   rectangle that **extends further north than the assessment perimeter**.
   https://www.theeastcut.org/district-map/
3. **Current CBD FAQ (undated).** "the east side of 2nd Street to The Embarcadero,
   and the North side of Mission to Harrison streets" — then says boundaries are
   set by which parcels pay the assessment. **This does not match (2).**
   https://www.theeastcut.org/faq/

**Gazetteer note:** the coining body has never published one consistent boundary
for the name it coined. Record all three as separate dated claims. Do not
synthesise them into a polygon.

### Stated historical derivation — the CBD's own words

- **8 June 2017. AGENT-REPORTED.**
  > "The name, The East Cut is inspired by the Second Street Cut, a defining
  > moment in our history. But, the name also points to our role as the epicenter
  > of the bustling eastern side of the city."

  and

  > "The name was inspired by the Second Street Cut, the leveling of Rincon Hill
  > which both created out current southern border and defined the character of
  > the neighborhood for almost 100 years."

  ("out" for "our" is in the original as reported.)
- **4 August 2017. AGENT-REPORTED.** The name refers to "the district's
  geographical location east of the Second Street Cut."
- **Current history page. AGENT-REPORTED.**
  > "Then in 1869, city planners decided to flatten the center of Rincon Hill along
  > 2nd Street, creating the 2nd Street Cut. While the Cut facilitated commerce
  > between downtown and the docks at South Beach, the change scarred the
  > neighborhood and it lost its cachet."

**Note the divergence from the established record.** Page & Turnbull (2009,
printed p.34) has the Cut built by **private investors** and "crudely blasted
through the center of Rincon Hill." The CBD's current page attributes it to
"city planners" and omits the private promoters. **No CBD wording using
"private," "blasted," or naming the Pacific Mail Wharf was found.** Per rule 6,
this is branding language: a name derived from an act of civic planning reads
better than one derived from a speculator wrecking a hill.

Also note the internal tension: 2017 says the Cut "created our current southern
border"; the same paragraph elsewhere places the district *east* of the Cut. The
derivation is decorative rather than geographic.

### Reaction, and the "90% said dumb" survey

**The survey exists but the "dumb" figure does not, as usually quoted.**

- The *New York Times* (2 August 2018) reports only that **Tad Bogdan**, a 14-year
  resident, organised a survey of **271 neighbours**, and — the NYT's words —
  **"he said, 90 percent disliked the name."**
- **"Thought the name was dumb" is later paraphrase, not the reported result, and
  not a documented question.**
- **The instrument was not found.** The research pass searched the South
  Beach/Rincon/Mission Bay Neighborhood Association's Surveys page
  (https://sbrmbna.com/surveys/) and its indexed 2017–18 meeting materials, the
  Rincon Hill neighborhood blog's 2018 archive, the CBD's own 2017 response, and
  the NYT and CNBC versions. No form, export or publication surfaced.
- **The date is not securely 2018.** The CBD's 4 August 2017 page already
  acknowledges a non-board-sanctioned "survey" circulating, unnamed and without a
  sample size. The NYT called Bogdan's survey "recent" in August 2018. These may
  be the same survey. **Field date is bounded only between June 2017 and
  2 August 2018.**
- **Authority:** 271 respondents, recruitment undocumented, self-selected as far
  as anyone can tell, result reported by the organiser rather than published.
  This evidences strong opposition among Bogdan's respondents. It does **not**
  establish a 90% neighbourhood consensus, and should never be cited as one.

Named contemporaneous reactions (all AGENT-REPORTED):
- Lauri Mashoian, Rincon Hill resident, June 2017: "I don't know why they want to
  rebrand Rincon Hill, which is real and historic and accurate… If you have to
  explain something, maybe it's not right."
- Jamie Whitaker, longtime Rincon Hill resident, June 2017: residents were only
  beginning to distinguish Rincon Hill from South Beach; hoped Rincon Hill would
  survive south of Folsom; called East Cut "okay" but doubted it would outlast its
  sponsor.
- ABC7, August 2018: mixed/confused street interviews. Illustrative only.

### Did anyone beyond the coining body adopt it?

| Body | Evidence | Weight |
|---|---|---|
| **Google Maps** | Added spring 2018 at the CBD's request; a Google spokesperson said staff inserted it manually after checking public sources. Label observed **absent** by 26 September 2024. | Real platform adoption ~2018–2024. **Correction to the brief: "disappeared around September 2024" should read "first observed absent 26 September 2024"** — no removal date was published. |
| **Apple Maps** | 26–27 Sept 2024: SFGate and SFist report it no longer appears as a browsing label, though direct search could still surface it. Neither addition nor demotion date established. | Demotion, not deletion. |
| **SF Planning** | Uses "The East Cut Community Benefit District" as the *partner organisation's* name; its planning geography is "South Downtown — the Transit Center District and Rincon Hill." | Recognises the org, **not** the neighborhood. |
| **SF.gov** | An undated "Perfect Day in The East Cut" promo page, itinerary curated by the CBD. | City-hosted marketing. Not a planning designation. |
| **USPS** | No East Cut locality, station or preferred-city record found in indexed USPS/PostalPro material. | **No adoption.** (Absence of search result ≠ proof of absence.) |
| **Zillow / Redfin / MLS** | "East Cut" appears in listing prose; Zillow's **structured neighborhood field** for several properties still reads **Rincon Hill**. | Marketing use; no evidence of a taxonomy change. |
| **Wikipedia** | "A marketing effort, started in 2017, attempts to give Rincon Hill and parts of South Beach / SOMA a new neighborhood name: The East Cut." | Explicitly declines to treat it as a neighborhood. |
| **News** | Divided. NYT and Business Insider used it as a label; SFist and SFGate consistently framed it as contested or failed branding. | Recognisable referent; did not displace older names. |

## What I could not verify for Q2

1. **The decisive 2017 board record** — no agenda, minutes, resolution or roll-call
   vote saying "the board adopts The East Cut." The CBD's Public Meetings archive
   did not expose 2017 documents.
2. **An exact May 2017 date** — the SF Business Times article behind the "created
   in May" line was not read in full.
3. **Bogdan's survey instrument** — see the named searches above.
4. **Exact Google/Apple add and remove dates** — press observation only; no
   platform change log or company statement.
5. **Any formal MLS neighborhood-code decision.**
6. **The signed Resolution 492-19 PDF and full File 190983 packet** — retrieval
   blocked; the action is known via a reconstructed legislative record.

---

# Q3. The 100 Vara District's extent — a live conflict

**This section is the strongest in the report: I retrieved and read the primary
sources myself.** Both accounts in the brief turned out to be checkable, and both
turned out to be partly wrong in interesting ways.

## Verdict

**Adjudicated on the naming question; not adjudicated on the 1847 geometry
question — and the two were never the same question.** The conflict in the brief
is largely a **category error between an administrative designation and a
surveying description**, and it dissolves once they are separated.

On **naming and administrative extent, Account B is right and Account A's
implication is wrong.** I verified the 1945 document — it is real, and it is the
San Francisco Board of Supervisors' *Journal of Proceedings*, in the **Assessor's
Office** annual report. And I then tested its extent independently against the
Assessor's own block book, which still cross-references every South of Market
block to a "100 VARA BLK." number. Blocks **east of 1st Street** — Mission/Spear/
Howard/Main (AB 3717 = 100 Vara Blk. 325) and Folsom/Main/Harrison/Beale
(AB 3746 = 100 Vara Blk. 332) — carry 100 Vara numbers. **The 100 Vara series
therefore runs east of 1st Street to the waterfront**, exactly as the 1945
Assessor implies, and contrary to any reading of Page & Turnbull that puts the
waterfront-to-1st strip outside it.

On **1847 block geometry, I could not adjudicate**, because I could not view the
1847 plan. But I can report that Page & Turnbull's specific wording is **not
supported by the modern block record**: AB 3746 measures **275.00 × 275.00 feet** —
a full 100-vara square (100 varas × 33 in = 275 ft) — and it sits east of 1st
Street. A 50-vara module would be 137.5 ft. What *is* true is that blocks east of
1st are **smaller overall**, because extra streets (Main, Spear, Beale, Fremont)
subdivide them. P&T appear to have compressed "smaller blocks east of 1st" into
"replicated the 50 Vara Survey," which the dimensions do not bear out.

**Crucially, the secondhand version of Account B in the brief overstates its
source.** The 1945 document does **not** say South of Market is "officially known
as 100 Vara." That gloss is Wikipedia's, and Wikipedia's own "Since 1847… official
name" sentence has carried a `{{Citation needed}}` tag since September 2019.

## Evidence

### The 1945 document — found, read, and narrower than reported

**Contemporaneous. READ (first-hand).** *Journal of Proceedings, Board of
Supervisors, City and County of San Francisco*, Volume 40, No. 1, **Tuesday,
January 2, 1945**, **page 46**, within the **Assessor's Office** annual report
(Assessor **Russell L. Wolden**). Internet Archive item
`journalofproceed40sanfrich`; I downloaded the full OCR text
(`journalofproceed40sanfrich_djvu.txt`) and read the passage in context. Verbatim:

> "The land valuation division accomplished another step toward the completion of
> Assessor Wolden's program for a complete scientific land revaluation of the
> entire City. In addition to the districts already surveyed, the revaluation
> studies this year included Western Addition, **50 Vara Section north of Lower
> Market Street** and the **100 Vara District on the south side of Market Street
> to the Ferry**. Various minor surveys were made in the Sunset and Richmond
> districts."

https://archive.org/details/journalofproceed40sanfrich

**What this settles:**
- **"100 Vara District" was in live administrative use in 1945**, by the
  Assessor's Office, in a document of record, paired symmetrically with
  "50 Vara Section." Account B's document is genuine.
- It locates that district **south of Market and running to the Ferry**.

**What this does NOT settle, and where the secondhand report overreached:**
- It is a **list of revaluation study areas**, not a boundary definition. "on the
  south side of Market Street to the Ferry" is a locating phrase in a sentence
  about which areas got studied that year. It is not a survey call.
- It **nowhere says** South of Market is "officially known as 100 Vara." That
  sentence is Wikipedia's synthesis, footnoted to this same page.
- The phrase is genuinely ambiguous: it can be read as the strip along Market's
  south side running northeast to the Ferry Building, or as the whole district
  whose northern edge is Market and whose eastern reach is the Ferry. **Do not
  give this a polygon.** Per rule 5, "extent as stated: south of Market, reaching
  to the Ferry; precision low" is the correct gazetteer entry.

### The Wikipedia layer — where the secondhand version came from

**READ (first-hand).** Current wikitext of "South of Market, San Francisco",
retrieved 2026-08-24. Two adjacent sentences, differently sourced:

> "Since 1847,{{Citation needed|date=September 2019}} the official name of the
> South of Market area has been the '100 Vara Survey' (alternately '100 Vara
> District')…"

> "According to city documents from 1945,<ref name="BOS"/> the '100 Vara District'
> goes from the south side of Market Street to the Ferry. The name is found mainly
> in history books, legal documents, title deeds, and civil engineering reports."

The `BOS` ref is the Journal of Proceedings page 46 above — correctly cited. The
**"official name since 1847"** claim is a **separate, unsourced** assertion tagged
since September 2019. The brief's Account B fused the two. Record them separately.

### The block book — an independent test, and it is decisive on extent

The Wikipedia article also cites an Assessor's block book sheet as evidence of
legal use. I followed that up and then extended it into a deliberate test of the
Account A / Account B disagreement, by pulling sheets **east of 1st Street**.

All four **READ (first-hand)** — retrieved as PDFs from
`sfplanninggis.org/blockbooks/`, rendered to images, and read:

| Sheet | Bounded by | Header | Position vs 1st St | Block dimensions shown |
|---|---|---|---|---|
| **AB 3775** | 2nd / Brannan / 3rd / Bryant (South Park) | **"100 VARA BLK. 359"** | west of 1st | — |
| **AB 3708** | Market / 1st / Mission / 2nd | **"100 VARA BLK. 346"** | west of 1st, abuts Market | irregular; alleys (Stevenson, Jessie, Ecker, Anthony) |
| **AB 3717** | Mission / Spear / Howard / Main | **"100 VARA BLK. 325"** | **EAST of 1st** | 275 ft wide (Main–Spear) |
| **AB 3746** | Folsom / Main / Harrison / Beale | **"100 VARA BLK. 332"** | **EAST of 1st** | **275.00 × 275.00 ft** |

- **AB 3775** confirms Wikipedia's example: South Park is 100 Vara Blk. 359.
  Sheet carries revision dates from the 1960s through 2008 — i.e. **still
  maintained**, not a historical artifact.
- **AB 3717** and **AB 3746** are the decisive ones. Both lie **east of 1st
  Street**, in the zone Page & Turnbull assign to a 50-vara-style grid. Both are
  numbered in the **100 Vara** series.
- **AB 3746 measures 275.00 × 275.00 ft**, which is exactly 100 varas square
  (100 × 33 in = 3,300 in = 275 ft). A 50-vara block would be 137.5 ft.
  Sheet bears "© COPYRIGHT SAN FRANCISCO CITY & COUNTY ASSESSOR 1995" and
  revisions 2009, 2016, 2017.

**Retrospective caveat, stated plainly:** these are **modern** Assessor sheets.
They record the survey system as the Assessor administers it **today**, after a
century and a half of bay fill, resurvey and renumbering. Much of the land east
of 1st Street **did not exist in 1847** — it was Yerba Buena Cove. So this
evidence is strong on the question *"what does the 100 Vara series cover as an
administrative designation"* and **weak** on the question *"what did O'Farrell
draw in 1847."* Those are the two questions the brief's conflict conflates.

### "100 Vara Block N" as a legal description

**Confirmed. READ (first-hand)** via the four sheets above — the form
"100 VARA BLK. *N*" is printed as a standing cross-reference on current
San Francisco Assessor's block maps, alongside the modern Assessor's Block number.
So the modern AB/lot system did not abolish it; it carries it as a parallel
identifier.

**AGENT-REPORTED corroboration** (not opened by me): *The San Francisco Original
Handy Block Book: comprising fifty vara survey, one hundred vara survey, South
Beach, Mission, Horner's Addition, Potrero, Western Addition, Richmond District,
Sunset District, Flint Tract, etc.*, Hicks-Judd Company, 1909–10, Internet Archive
`sanfranciscoorig3190910bloc`; and the 1901 edition, `sanfranciscobloc1901hick`.
Note what the title itself demonstrates: the vara surveys were **two named series
among many**, sitting alongside Horner's Addition, the Potrero, the Western
Addition and so on. That is the correct frame — a **land-description series**, not
a neighborhood.

### A third extent, and it disagrees with both

**NOT READ (snippet only).** SF Memory's description of the Handy Block Books
says the "One Hundred Vara Survey" volume covers South-of-Market blocks **"from
Ninth Street to the Bay."** https://sfmemory.org/listHandyBlockBooks.php

This is a **third** stated extent, and it is not the same as either account in the
brief. It gives a western limit at 9th Street — where Page & Turnbull say 5th.
**Do not reconcile these.** Record three dated claims:
- 1847 plan, per P&T (2009): 1st to 5th Streets is 100-vara; cove to 1st is not.
- 1945 Assessor: south of Market, to the Ferry.
- Handy Block Book, per SF Memory: 9th Street to the Bay.

### On Account A's underlying source — not verified

I could **not** confirm a catalogued 1847 map titled "The Original and Authentic
Plan of San Francisco" in the David Rumsey, Library of Congress or Bancroft
collections. What the research pass found instead (all **NOT READ**, snippet
level):
- David Rumsey holds *Official Map of San Francisco*, **William M. Eddy**, **1849**
  (catalog id given as DR2321.001), described as **enlarging** O'Farrell's 1847
  plan. So the Eddy association attaches to an **1849** map, not the 1847 sheet.
- The LC record surfaced (`G4364.S5A35 1847 .B6`, LCCN 74693207) is a **Bosqui
  Eng. & Print. Co. panorama view**, catalogued 1884 — **not** the survey plan.
- OAC holds *Jasper O'Farrell correspondence, 1846–1848* (`ark:/13030/c8dr336w`),
  with no associated map catalog record surfaced.

**The 1847 map image was not viewed by anyone in this research — not by me, not by
the agent.** Page & Turnbull's citation therefore stands unchecked at its source.
Secondary descriptions (SF Planning centennial brochure; SPUR) describe O'Farrell
as laying out "a separate, larger grid" south of Market with lots roughly twice
the northern width — and **none of them** describes a small-block/large-block
transition at 1st Street. That is absence of corroboration for P&T's specific
sentence, not disproof of it.

## What I could not verify for Q3

- **The 1847 plan itself.** Not located under the cited title, not viewed. Until
  someone opens it, P&T's sentence cannot be checked against its own source. This
  is the single highest-value remaining task in the whole brief.
- **Whether the 1847 plan drew the cove-to-1st area at all.** In 1847 most of it
  was under water. If O'Farrell drew paper blocks over the cove, their module is
  the crux; if he did not, P&T's sentence describes a later survey and is
  misattributed to 1847.
- **The full extent of the 100 Vara block series.** I sampled **four** sheets. I
  did not walk the series to its western, southern or northern limits, so I cannot
  state its boundaries — only that it demonstrably includes blocks east of 1st.
  The 5th-vs-9th-Street disagreement is untested.
- **Whether "100 Vara District" ever had a boundary defined in an ordinance**, as
  opposed to being an inherited land-description series used loosely. The 1945
  text does not define one. No defining instrument was found.
- **Deeds.** I verified the form on Assessor's *maps*. I did not open a recorded
  deed or title document using "100 Vara Block N" in its legal description.
- The research pass searched **Internet Archive, HathiTrust, SFPL/SF History
  Center catalogs, sfplanning.org archives and BOS materials** for a *different*
  1945 document (a Planning Commission or Master Plan item) and found none — the
  1945 source is the Assessor's report in the Supervisors' Journal, and there is
  no evidence of a second 1945 document.

---

# Source list

## Read first-hand in this session

| Source | Creator | Date | Locator | What it settles / cannot settle |
|---|---|---|---|---|
| "Warehouse District Caters to Budget-Minded" | *Los Angeles Times* (no byline exposed) | 6 Nov 1988 | https://www.latimes.com/archives/la-xpm-1988-11-06-tr-170-story.html | **Settles:** earliest verified "SoMa" in print, its register, and its 1988 extent (Market/1st/Townsend/12th). **Cannot settle:** priority — "nicknamed" implies earlier currency. |
| *Journal of Proceedings, Board of Supervisors, City and County of San Francisco*, Vol. 40, No. 1, p. 46 (Assessor's Office report) | City and County of San Francisco | 2 Jan 1945 | IA `journalofproceed40sanfrich`; https://archive.org/details/journalofproceed40sanfrich | **Settles:** "100 Vara District" was live administrative usage in 1945, located south of Market to the Ferry. **Cannot settle:** its boundaries; and it does **not** say SoMa is "officially known as 100 Vara." |
| Assessor's Block Map, Block **3775** ("100 VARA BLK. 359", South Park) | SF City & County Assessor | rev. 1960s–2008 | web.archive.org 2011 capture of `gispub02.sfgov.org/assessorblocks/block3775.pdf` | **Settles:** 100 Vara block numbers are current cross-references on official maps. |
| Assessor's Block Map, Block **3717** ("100 VARA BLK. 325"; Mission/Spear/Howard/Main) | SF City & County Assessor | © 1995, rev. '77–'92 | http://sfplanninggis.org/blockbooks/AssessorBlock3717.pdf | **Settles:** the 100 Vara series extends **east of 1st Street**. |
| Assessor's Block Map, Block **3746** ("100 VARA BLK. 332"; Folsom/Main/Harrison/Beale) | SF City & County Assessor | © 1995, rev. 2009–2017 | http://sfplanninggis.org/blockbooks/AssessorBlock3746.pdf | **Settles:** a **275.00 × 275.00 ft** (100-vara square) block **east of 1st Street**. Contradicts P&T's "replicated the 50 Vara Survey." **Cannot settle:** 1847 geometry — this is a modern sheet over filled land. |
| Assessor's Block Map, Block **3708** ("100 VARA BLK. 346"; Market/1st/Mission/2nd) | SF City & County Assessor | rev. 2019 | http://sfplanninggis.org/blockbooks/AssessorBlock3708.pdf | **Settles:** 100 Vara numbering runs up to Market St; shows irregular alley-cut lots. |
| "South of Market, San Francisco" — current wikitext | Wikipedia contributors | retrieved 24 Aug 2026 | `?action=raw` | **Settles:** the exact wording, and the `{{Citation needed}}` tags (SoHo claim, July 2013; "official name since 1847", Sept 2019). |
| "South of Market, San Francisco" — **first revision** | Wikipedia contributors | 5 Mar 2004, revid 2647532 | https://en.wikipedia.org/w/index.php?oldid=2647532 | **Settles:** the SoHo-imitation claim is present, hedged ("probably"), and **unsourced from day one**. **Cannot settle:** whether the derivation is true. |

## Agent-reported (locator given; I did not open these)

- "Introducing The East Cut", East Cut CBD, 8 Jun 2017 — https://www.theeastcut.org/introducing-the-east-cut/ — launch date and derivation wording; no vote record.
- "About The East Cut Name", East Cut CBD, 4 Aug 2017 — https://www.theeastcut.org/east-cut-name/ — stated process; the "name for the CBD itself" retreat.
- "History" / "District Map" / "FAQ", East Cut CBD, undated — theeastcut.org — three mutually inconsistent boundary/derivation claims.
- SFist, 1 Jun 2017 — https://sfist.com/2017/06/01/now_theyre_trying_to_rebrand_rincon/ — name public by 1 June; early opposition.
- Curbed SF, 5 Jun 2017 — https://sf.curbed.com/2017/6/5/15730564/rincon-hill-east-cut-san-francisco — proposed geography; Whitaker quote.
- Jack Nicas, "As Google Maps Renames Neighborhoods, Residents Fume", *NYT*, 2 Aug 2018 — the Bogdan survey (271 neighbours, "90 percent disliked"); Google spring-2018 insertion; rejected names.
- Greater Rincon Hill CBD Management Plan, Jun/Jul 2015 — sfelections.sfgov.org (…/RinconHillCBD_Management_Plan.pdf) — controlling assessment boundaries; 15-yr term to FY2029–30.
- BOS Resolution 492-19, 19 Nov 2019 — legal district name change (signed PDF not retrieved).
- BOS File 180665, 19 Jun 2018 — "Greater Rincon Hill CBD (dba The East Cut CBD)".
- SFGate, 26 Sep 2024 / SFist, 27 Sep 2024 — first observation of the map label's absence.
- *SF Bay Guardian* vol. 24 no. 8, 29 Nov 1989 — IA `Issue24.08` — "SOMA nightspots" in an advertisement.
- Ali Ghanbarian, "About", 1 Oct 2023 — alighanbarian.com/about-2/ — 1986 founding and coinage claim; self-published, uncorroborated.
- *Subject Catalog of Periodicals*, SFPL, 1987 — IA `subjectcatalogof1987sanf` — **no** *SOMA* entry.

## Not read (snippet / catalog only)

- *SF Business Times*, 14 Dec 2017 — "created the name in May."
- SF Memory, Handy Block Books listing — "One Hundred Vara Survey… Ninth Street to the Bay" — the third extent.
- Hicks-Judd, *San Francisco Original Handy Block Book*, 1909–10 (IA `sanfranciscoorig3190910bloc`) and 1901 (`sanfranciscobloc1901hick`).
- David Rumsey, *Official Map of San Francisco*, W. M. Eddy, **1849** — described as enlarging O'Farrell's 1847 plan.
- LC `G4364.S5A35 1847 .B6` / LCCN 74693207 — a Bosqui panorama **view**, not the survey plan.
- OAC, *Jasper O'Farrell correspondence, 1846–1848*, `ark:/13030/c8dr336w`.

---

# What would change this answer

**Q1 — highest value first**
1. A **San Francisco Chronicle or Examiner** full-text search, 1975–1990, for
   SoMa / SOMA / So-Ma. This is the obvious gap and it is entirely unsearched.
2. A scan of ***SOMA* magazine vol. 1, no. 1** with masthead and date. It would
   either substantiate or kill the 1986–87 claim and the Ghanbarian coinage claim
   in one move.
3. **Gallery, club and performance ephemera, 1979–1988** — SF Public Library, GLBT
   Historical Society, Bay Area arts collections. The 1988 "nicknamed" phrasing and
   the 1989 advertisement both point at vernacular/commercial print running ahead
   of newspapers.
4. For the SoHo claim: any **pre-2004** printed assertion of the derivation. That
   would move it from "2004 Wikipedia speculation" to a real, if still unevidenced,
   claim with an author.

**Q2**
5. **2017 East Cut CBD board agenda and approved minutes** with the motion and
   vote — would replace "public by 1 June, launched 8 June" with an exact date.
6. **Bogdan's original survey form or response export** — would give the actual
   question, choices, recruitment and denominator, and settle whether "dumb" was
   ever asked.
7. **Google/Apple place-data change logs** — would replace "first observed absent"
   with real add/remove dates.

**Q3**
8. **View the 1847 O'Farrell plan.** Everything about Account A turns on it and
   nobody in this research has seen it. Start with David Rumsey and the Bancroft
   under O'Farrell rather than under the "Original and Authentic Plan" title,
   which did not resolve.
9. **Walk the 100 Vara block series to its limits** in the Assessor's block maps —
   find the highest and lowest numbered sheets and their streets. This would
   convert my four-sheet sample into an actual boundary and settle the
   5th-vs-9th-Street disagreement empirically.
10. **A recorded deed** using "100 Vara Block N" as its legal description, to
    confirm the form in title records and not only on Assessor's maps.
11. **An ordinance or Assessor's instruction defining the 100 Vara District's
    boundary**, if one exists. Its absence, if confirmed, is itself a finding:
    the name would then be an inherited land-description series that never had an
    administrative boundary at all — which is exactly the kind of thing this
    gazetteer should record.
