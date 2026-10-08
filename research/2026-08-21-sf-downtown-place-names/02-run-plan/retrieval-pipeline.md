# The retrieval pipeline

**Method decision, 26 August 2026: multi-model commissioning is abandoned for
this investigation; hand retrieval is industrialised instead.** `topic.yaml`
carries the decision and its consequences. This describes what replaces it.

## Why

Commissioning produced nothing. Brief A was dispatched, never returned, and its
run record orphaned on a host that was never diagnosed. Brief B was never sent.

Hand retrieval produced everything this corpus actually holds: the Page &
Turnbull context statement and its quoted pages, the conflict register, the
three-act survey spine, the Barbary Coast material, and — once the geometry
arrived — the first claim here corroborated by independent physical measurement.

One method has a track record and the other has a bill. This keeps the first
and stops paying the second.

The briefs are not deleted. They stop being work orders waiting on a host and
become what they always described: **the question list a retrieval pass
answers**.

## Three stages

**1. Locate.** Find a document that could settle a question. This is judgement
and stays manual — a person or a session deciding that the Corbett Heights
context statement probably knows when the Eureka Homestead Association was
platted.

**2. Fetch and mark.** Retrieve it, checksum it, record where it came from and
when, extract its text, and establish its page offset. Mechanical, scriptable,
and it must run where the network is open.

**3. Quote.** Search the retrieved text for the claim, and emit a quotation with
its printed page and its marker, ready to paste into an entry. Also mechanical,
and the stage that pays for the whole thing: it turns "read seven hundred pages
again" into "ask the corpus".

Stage 1 is the work. Stages 2 and 3 are the tooling that makes stage 1 worth
doing more than once.

## Where each stage runs, and why that is annoying

The session container's egress reaches `*.s3.amazonaws.com`,
`raw.githubusercontent.com` and `api.github.com`, and almost nothing else. Not
`data.sfgov.org`, not `archives.sfplanning.org`, not `sfheritage.org`, not
`www2.census.gov`.

**Lobster** has open egress. Every acquisition script in `02-run-plan/` is
written to run there and is documented saying so.

That split is the tax on this work: a session proposes a fetch, a human runs it
on lobster, pastes the result back, and a bug costs a full round trip. Two
things reduce it, and both are already in use:

- **Scripts that report rather than assume.** `acquire-neighborhoods.py --probe`
  prints what the endpoints actually return so a wrong guess costs one run
  instead of four. `acquire-geo.py --report` did the same for the road filter and
  caught two confidently wrong assumptions.
- **Running a session on lobster itself** for retrieval work, leaving the
  container session to the corpus, the analyses and the viewers. A lobster
  session should read this file first.

On lobster, refresh with `git fetch && git reset --hard origin/<branch>`, never
`git pull`: the working branch is restarted from `main` after each squash-merge
and force-pushed, so its history is rewritten regularly and `pull` correctly
refuses to fast-forward across that.

## What gets committed, and what does not

**Committed: provenance, not corpora.** For each document — source URL, sha256
as fetched, retrieval timestamp in UTC, page count, the printed-to-PDF page
offset, and the extraction method. That is enough to re-fetch the document and
verify it is the same bytes.

**Not committed: the documents or their extracted text.** `CONTRIBUTING.md`
forbids committing copyrighted source corpora without permission, and these are
municipal planning documents whose terms have not been established. Provenance
is reproducible; the corpus itself stays local and is re-fetchable from the
manifest.

This is the same standard `04-normalized/geo/sources.json` already meets for
geometry: where it came from, when, under what terms, and whether the bytes
still match.

## Page numbers are not page numbers

Verified the hard way on the Page & Turnbull statement: its **printed page
numbers run two behind the PDF index**, because of unnumbered front matter. A
citation of "p.20" is ambiguous until you say which one, and a reader checking a
quote against the wrong one concludes the quote is wrong.

The manifest records a per-document offset, and citations give the printed page
with the PDF page beside it: `printed p.18 (PDF p.20)`. Every document gets its
offset established by reading footers on several pages, not assumed.

## Markers, unchanged

Every claim carries one:

- `FETCHED` — the page was retrieved and read.
- `SEARCH-SUMMARY` — a search engine's summary; the page itself was never opened.
- `RECALLED` — from training data, unverified.

These are not decoration. `RECALLED` is how the 33-inch vara, the US survey
foot's retirement, and the NAD27→NAD83 history are marked in
`05-analysis/survey-grid-measurement.md`, and it is why those claims can sit
beside measured ones without contaminating them.

## Built, and not built

**Built.** `acquire-geo.py` (TIGER, with `--report` and a licence-driven default
of public domain over ODbL). `acquire-neighborhoods.py` (DataSF, licence read at
run time and refused if share-alike, with `--probe`). `05-analysis/measure-grid.py`
(measurement from committed geometry, stdlib only, no network).
`acquire-documents.py` — stage 2, mechanised: fetch, checksum, extract, settle
the page offset, append provenance to `04-normalized/sources/manifest.json`.

**How `acquire-documents.py` handles the offset**, because it is the part that
could quietly poison everything downstream. It reads footers and headers,
tallies the offsets they imply, and *proposes* one with the evidence printed
beside it — then writes nothing. Recording requires `--offset` explicitly:
an integer, `auto` to accept the proposal, or `none`. The manifest records which
of those it was, in `page_offset_basis`, so a citation's authority is legible
later. A candidate is rejected unless it is a plausible page number for a
document of that length, which is what stops a footer's `1864` becoming page
1864 — the same mistake the plat extraction made by taking the nearest
four-digit year.

`--selftest` proves the detector against pages whose offset is known, including
the year case, and needs no network. `--verify` re-fetches every recorded
document and compares sha256: the manifest claims the bytes, and that tests the
claim. A document whose sha256 has changed at its URL is refused rather than
quietly updated — any quotation already taken from it may no longer be on the
page cited, which is a finding, not a nuisance.

The local store carries its own `.gitignore`, written by the script, ignoring
everything except the manifest. Proven by `git add -A --dry-run`: it stages the
manifest and the ignore file, and neither the documents nor their extractions.

**Not built, in the order it is worth building.**

1. `quote.py` — search the local extractions for a phrase, return the passage
   with its printed and PDF page and a ready-formed citation. Stage 3, and the
   one that changes how fast entries can be written.
2. **Prose to polygon.** A bounding description — "bounded by Market, Howard,
   1st, and 2nd" — plus the committed centrelines, producing a polygon and a
   precision marker. The intersection solver in `measure-grid.py` is already
   half of this. Without it, every extent stays hand-drawn and the atlas cannot
   grow past what one person can draw.

## The nine documents already retrieved

Ten text extractions exist locally from SF Planning: the SoMa historic context
statement, the Central SoMa EIR, Japantown, Market & Octavia, Mission, North
Beach, Parkside, the Corbett Heights statement, and the modern context
statement. They were fetched ad hoc and **their provenance was never recorded** —
which is precisely the gap `acquire-documents.py` closes.

They are also the immediate reason this decision pays: the Corbett Heights
statement alone names dozens of dated, bounded homestead associations and
subdivision tracts — the Eureka Homestead Association of 1864, the Market Street
Homestead Association of 1868 — each one a plat that would fill the space
between the three city-scale surveys on the timeline. A bulk extraction over
them returned 131 named plats with 47 carrying a nearby year, and none of it is
trustworthy yet: the heuristic was "nearest four-digit year", which produced a
birth year as a plat date. Turning that into evidence is reading, one sentence
at a time, which is what stage 3 exists to make bearable.
