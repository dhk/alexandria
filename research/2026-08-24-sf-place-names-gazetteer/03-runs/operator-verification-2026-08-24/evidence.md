# Operator verification pass — primary sources retrieved and read first-hand

Run 2026-08-24 by the operator's session (Claude Code, direct retrieval), **not**
through a commissioned model. No provider generated any claim in this file; each
entry below was fetched, opened and transcribed.

This pass exists because the commissioned instrument reported failure on Q3's
central document (see
[`../perplexity-2026-08-24/response-q3b-1945-document.md`](../perplexity-2026-08-24/response-q3b-1945-document.md))
while a different response
([`response-q3c-block-books.md`](../perplexity-2026-08-24/response-q3c-block-books.md))
attributed the disputed wording to Wikipedia. Following that attribution to the
Wikipedia article's own footnote located the document the first response could
not find.

## Rights and why the artifacts are not committed here

Per CONTRIBUTING's rule that safe publication may displace exact preservation:
retrieved files are held **outside** this public repository, and their SHA-256
checksums are recorded below so a later reader can confirm they are looking at
the same bytes.

- **SF Board of Supervisors *Journal of Proceedings*, 1945** — a public record;
  the Internet Archive copy is freely retrievable. Quoted at length below.
- **SF Assessor's block maps** — each sheet bears "© COPYRIGHT SAN FRANCISCO
  CITY & COUNTY ASSESSOR". **Not committed.** Described and quoted only to the
  extent needed for the finding; every sheet is retrievable at the URL given.
- **Los Angeles Times, 1988** — copyrighted. One sentence quoted as evidence of
  the usage under investigation; the retrieved HTML is not committed.
- **Wikipedia** — CC BY-SA. Quoted with attribution.

| File retrieved | SHA-256 |
|---|---|
| `journalofproceed40sanfrich_djvu.txt` | `4211cb20565da4ddee267b72b5f4e1ed2f56834793b9a381d7549fe2b30605b4` |
| `block3775.pdf` (2011 web.archive.org capture) | `622e96d2d9468733cb350a1fa6134129333417ed65bb10d232f7bfe7996e377e` |
| `AssessorBlock3717.pdf` | `7289c5f789b0b197384e363be66732dd47f24f6be05b48f554677ed47ff5a7aa` |
| `AssessorBlock3746.pdf` | `294ebdf41e11221c673ad7c8cbe9967ba6b8770434555833cfe348bd430c7ca6` |
| `AssessorBlock3708.pdf` | `8b662910ff1ab63ea75db0a8382a56478bf1d564f34c9afd61b446b5e516cea7` |
| LA Times 1988 article HTML | `0d24db1638e39992e92d44e2732a3db2ab2cecd285158134413939a8e9645ee9` |
| Wikipedia revision 2647532 wikitext | `e85e1e8956897f9326a8c4b8a5d44d176b12f6e09345aca155135876aff13dea` |
| Wikipedia current wikitext (2026-08-24) | `9eaaab4f63a9ad03e65bfb97c0f064cc34e5857e48cce2abb469448a2b800012` |

---

## 1. The 1945 document — located, read, and narrower than reported

**Contemporaneous. READ.** *Journal of Proceedings, Board of Supervisors, City
and County of San Francisco*, Volume 40, No. 1, **Tuesday, January 2, 1945**,
**page 46**, in the **Assessor's Office** annual report (Assessor **Russell L.
Wolden**). Internet Archive item `journalofproceed40sanfrich`; full OCR text
retrieved and read in context.

> "The land valuation division accomplished another step toward the completion
> of Assessor Wolden's program for a complete scientific land revaluation of the
> entire City. In addition to the districts already surveyed, the revaluation
> studies this year included Western Addition, **50 Vara Section north of Lower
> Market Street** and the **100 Vara District on the south side of Market Street
> to the Ferry**. Various minor surveys were made in the Sunset and Richmond
> districts."

**Settles:** "100 Vara District" was live administrative usage in 1945, by the
Assessor's Office, in a document of record, paired symmetrically with "50 Vara
Section."

**Does not settle, and the secondhand report overreached:** this is a list of
revaluation study areas, not a boundary definition, and it nowhere says South of
Market is "officially known as 100 Vara." The phrase is ambiguous between a
strip along Market's south side running to the Ferry Building and a district
whose northern edge is Market. **No polygon should be derived from it.**

## 2. Where the secondhand version came from

**READ.** Current wikitext of "South of Market, San Francisco", retrieved
2026-08-24. Two adjacent sentences, differently sourced:

> "Since 1847,{{Citation needed|date=September 2019}} the official name of the
> South of Market area has been the '100 Vara Survey' (alternately '100 Vara
> District')…"

> "According to city documents from 1945,\<ref name=\"BOS\"/\> the '100 Vara
> District' goes from the south side of Market Street to the Ferry."

The `BOS` footnote is the Journal page above, correctly cited. The **"official
name since 1847"** claim is a separate, unsourced assertion tagged since
September 2019. The brief's Account B fused the two.

## 3. The block book — an independent test of extent

All four sheets retrieved as PDFs from `sfplanninggis.org/blockbooks/` (3775 via
a 2011 `web.archive.org` capture of `gispub02.sfgov.org`), rendered to images,
and read.

| Sheet | Bounded by | Header | vs 1st St | Dimensions shown |
|---|---|---|---|---|
| AB 3775 | 2nd / Brannan / 3rd / Bryant (South Park) | "100 VARA BLK. 359" | west | — |
| AB 3708 | Market / 1st / Mission / 2nd | "100 VARA BLK. 346" | west, abuts Market | irregular; alleys |
| **AB 3717** | Mission / Spear / Howard / Main | "100 VARA BLK. 325" | **EAST** | 275 ft (Main–Spear) |
| **AB 3746** | Folsom / Main / Harrison / Beale | "100 VARA BLK. 332" | **EAST** | **275.00 × 275.00 ft** |

**Settles:** the 100 Vara block series extends **east of 1st Street** to the
waterfront, and "100 VARA BLK. *N*" is a standing cross-reference printed on
current Assessor's maps alongside the modern Assessor's Block number. AB 3746's
275.00 × 275.00 ft is exactly 100 varas square (100 × 33 in = 275 ft); a 50-vara
module would be 137.5 ft.

**Does not settle:** 1847 geometry. These are modern sheets, and much of the
land east of 1st Street was under Yerba Buena Cove in 1847. Four sheets were
sampled; the series was not walked to its limits, so no boundary is claimed.

## 4. The 1988 *Los Angeles Times* usage

**Contemporaneous. READ.** "Warehouse District Caters to Budget-Minded", *Los
Angeles Times*, 6 November 1988. Embedded schema.org metadata gives
`"datePublished":"1988-11-06T08:00:00.000Z"`. No byline exposed.

> "The warehouse district, nicknamed SoMa (for south of Market), is an area of
> factory buildings bordered by Market, 1st, Townsend and 12th streets."

**Settles:** the earliest verified print use in this investigation, its register
(anonymous travel/retail feature), and — the substantive part — that at first
verified use **SoMa excluded everything east of 1st Street** and was therefore
not a synonym for South of Market.

## 5. Provenance of the SoHo-derivation claim

**READ.** Retrieved the article's revision history via the MediaWiki API. The
**first revision**, 5 March 2004, revid 2647532, already carried it:

> "Many people shorten the name to SOMA or SoMa, **probably in reference to SoHo
> (South of Houston) in New York City.**"

The hedge "probably" is the original author's. No source was given then; the
claim has carried a `{{Citation needed}}` tag since **July 2013** and remains
unsourced.

**Settles:** the derivation is not a sourced etymology but a 2004 Wikipedia
editor's explicitly hedged speculation, unsourced for thirteen years and copied
outward from there.

**Does not settle:** whether the derivation is true. SoHo did precede SoMa. The
finding is that nobody has produced evidence, and that the claim's ubiquity is a
citation-laundering artifact.
