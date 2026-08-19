# Corrections

Corrections to this investigation's analysis, added rather than applied. Per
AGENTS.md rule 5 the original artifacts are not rewritten: `claims.json`,
`scores.csv` and `analysis.md` continue to say what the run produced, and this
file records where reading a source has since shown that to be wrong.

---

## 2026-08-19 — c-032 overstates the absence of outcome studies

**The claim as published**

> c-032 — No strong empirical outcome studies (e.g., RCTs showing STE improves
> comprehension, error reduction, or safety outcomes) were found in open
> sources.

Group `consensus`, three responding models. `analysis.md` states the same
position in prose under "What this run does not establish": *"All three outputs
note the absence of RCTs or strong quasi-experiments showing STE rules improve
comprehension, error reduction, or safety outcomes in open sources."*

**What opening the source showed**

Kuhn 2014, the survey already on this investigation's source list, summarises
exactly such studies. Section 5.5 "Evaluations", page 145:

> "For type C, two studies on AECMA-SE showed that the use of controlled English
> significantly improves text comprehension, with a particularly large effect
> for complex texts and non-native speakers (Shubert et al. 1995; Chervak,
> Drury, and Ouellette 1996). The results of other studies were similar but not
> significant (Stewart 1998)."

All three named works are aircraft-documentation studies, and one is on
maintenance procedures specifically:

- Shubert, Serena K., Jan H. Spyridakis, Heather K. Holmback and Mary B. Coney.
  1995. "The comprehensibility of simplified English in procedures." *Journal of
  Technical Writing and Communication* 25(4):347–369.
- Chervak, Steve, Colin G. Drury and James P. Ouellette. 1996. "Field evaluation
  of simplified English for aircraft workcards." *Proceedings of the Tenth
  Meeting on Human Factors Issues in Aircraft Maintenance and Inspection*,
  123–136.
- Stewart, Kathleen M. 1998. "Effect of AECMA simplified English on the
  comprehension of aircraft maintenance procedures by non-native English
  speakers." Master's thesis, University of British Columbia.

**What is corrected, and what is not**

Corrected: the assertion that no empirical outcome studies for Simplified
English were found in open sources. They are in open sources, and they were
reachable from a source the investigation itself cites. A reader should treat
c-032's absence claim as withdrawn.

Not corrected, because it is not settled: whether any of the three meets the bar
c-032 sets — an RCT or a strong quasi-experiment. Kuhn characterises the
results, not the designs, and describes Chervak as a *field evaluation*. Two of
the three report significant effects; that is a statement about outcomes, not
about randomisation. Settling this requires opening Shubert 1995, Chervak 1996
and Stewart 1998, none of which has been done. Until then the honest position is
that outcome studies exist and their strength is unassessed — not that strong
ones do, and not that none do.

**A second error, in the audit rather than the analysis**

The `source-audit.json` entry for `kuhn-2014` recorded, on 2026-08-16, that "the
analysis attributes to this survey a summary of studies finding Simplified
English improves maintenance-procedure comprehension." That is not so. The
string `kuhn` does not appear in `analysis.md`; the survey appears nowhere in
the investigation's prose, and the prose asserts the opposite of what the note
describes. The mapping of `kuhn-2014` to c-032 exists only inside the audit
worklist. Recorded here because an audit note that misdescribes the artifact it
audits will mislead the next reader in the same way a bad claim does.

**Effect on assurance**

None yet. This investigation is Silver. The correction removes one obstacle to a
Gold source audit — the highest-priority entry now has a substantive,
quote-backed verdict — and adds a different one: c-032 cannot stand as written,
and nine of ten entries remain `unchecked`.
