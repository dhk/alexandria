# San Francisco Historical Place Names Atlas
## Multi-Phase Research Brief

**Project type:** Historical gazetteer and evidence-backed spatial-temporal research

**Primary objective:** Create a version-controlled research corpus that documents how San Francisco place names, neighborhood names, boundaries, and geographic concepts have emerged, overlapped, changed, declined, and been revived over time.

**Intended future product:** A map with a time slider and name search. This brief covers research and data production only; it does not require building the visualization.

**Core operating principle:** A neighborhood is not a timeless, authoritative polygon. It is a historical claim, made by a particular source at a particular time, with a degree of geographic precision and social or administrative authority.

---

## 1. Research questions

The research should answer the following questions for every place-name record:

1. What exact name or spelling was used?
2. When is its earliest and latest dated evidence of use?
3. Who used the name, and in what context?
4. Was it an official district, survey area, planning designation, common neighborhood, cultural district, corridor, topographic feature, real-estate label, or retrospective historical term?
5. What spatial extent did the source support at that moment in time?
6. Is the boundary exact, approximate, corridor-based, point-based, or unknown?
7. Which other names did it overlap, contain, succeed, replace, or compete with?
8. What physical, institutional, demographic, or political events changed the name’s meaning or extent?
9. What uncertainty, disagreement, or evidentiary gap must be visible to downstream users?

---

## 2. Scope and definitions

### Geographic scope

The full project concerns the City and County of San Francisco. Begin with a high-documentation pilot centered on downtown and South of Market:

- Financial District
- Transbay
- South of Market / SoMa
- East SoMa
- South Park
- Rincon Hill
- South Beach
- Yerba Buena
- Yerba Buena Gardens
- 100 Vara District
- Happy Valley
- South of the Slot
- The East Cut
- Embarcadero waterfront and historic shoreline

### Temporal scope

- **Full target period:** 1835–present
- **Pilot target period:** 1847–present
- **Default display granularity:** decade
- **Evidence granularity:** exact dates or years whenever supported

Do not manufacture exact start or end dates. Use ranges and confidence levels when evidence is partial.

### Unit of analysis

The primary unit is a **place-name assertion**, not a contemporary neighborhood polygon.

A place may have:

- Multiple names at the same time
- Multiple geometries at different times
- Different boundaries depending on source type
- Names that persist as historical references after common use fades
- Ambiguous or purely cultural boundaries

---

## 3. Required research principles

### 3.1 Separate name use from spatial extent

Store name usage and geometry as independent, versioned facts. A name can stay in use while its understood boundary shifts.

### 3.2 Preserve source provenance

Every factual claim must be traceable to a specific source record and a location within that source, such as page number, map sheet, archive identifier, stable URL, or quoted passage.

### 3.3 Do not force false precision

A cultural, colloquial, or informal name should not receive a crisp parcel-level polygon unless evidence supports one. Use approximate polygons, corridors, points, or `unknown` as appropriate.

### 3.4 Represent disagreement

Conflicting sources are research results, not errors to erase. Preserve competing spatial interpretations and attach source-specific evidence.

### 3.5 Distinguish historical evidence from retrospective commentary

A 1900 map labeling an area is different from a 2020 article describing what people called the area in 1900. Both may be useful, but they need different source classes and confidence.

### 3.6 Avoid presentism

Do not back-project current neighborhood boundaries into historical periods without dated evidence. Do not assume today’s name or boundary existed in earlier decades.

---

## 4. Multi-phase execution plan

## Phase 0 — Repository, standards, and source registry

### Goal

Create the durable GitHub-native research environment before collecting claims.

### Tasks

1. Create the repository structure described in Section 8.
2. Adopt the schemas in Section 7 as versioned Markdown and JSON specifications.
3. Create a controlled vocabulary for:
   - Place classes
   - Name status
   - Boundary precision
   - Boundary basis
   - Source type
   - Confidence level
   - Relationship type
4. Establish a source registry with stable `source_id` values.
5. Define citation rules and contribution rules.
6. Create issue templates for:
   - New candidate place name
   - New source
   - Boundary dispute
   - Source correction
   - Geometry review
   - Research gap
7. Set up lightweight validation for required fields and invalid dates.

### Deliverables

- `README.md` explaining the project and research model
- `docs/data-model.md`
- `docs/editorial-standards.md`
- `docs/controlled-vocabularies.md`
- `data/sources/sources.jsonl`
- GitHub issue and pull-request templates
- Initial project board or GitHub Milestones

### Acceptance criteria

- Every assertion can reference a source ID.
- Every source can be retrieved or described sufficiently for a future researcher to locate it.
- Required terminology is defined before entries are added.

---

## Phase 1 — Pilot candidate-name inventory

### Goal

Compile a broad, non-authoritative inventory of candidate names for the downtown/SoMa pilot.

### Tasks

1. Gather names from historical maps, planning documents, gazetteers, directories, local histories, newspapers, archival finding aids, and community organizations.
2. Record all spelling variants, abbreviations, and aliases.
3. Classify each candidate as one or more of:
   - Official jurisdiction or survey district
   - Common neighborhood
   - Sub-neighborhood
   - Topographic feature
   - Cultural or ethnic district
   - Industrial, occupational, or social district
   - Corridor
   - Planning or redevelopment area
   - Real-estate or branding overlay
   - Historical or retrospective label
4. Add a preliminary earliest and latest attestation where possible.
5. Open a research issue for every ambiguous candidate or likely duplicate.

### Minimum pilot seed list

- Yerba Buena
- San Francisco
- 100 Vara District / 100 Vara Survey
- South of Market
- South of the Slot
- SoMa / SOMA
- East SoMa
- Rincon Hill
- Rincon
- Happy Valley
- South Beach
- South Park
- Transbay
- Financial District
- Yerba Buena
- Yerba Buena Gardens
- Embarcadero
- The East Cut
- Second Street Cut

### Deliverables

- `data/places/candidate-names.csv` or `.jsonl`
- One GitHub issue per unresolved name, duplicate, or ambiguity
- A short research memo summarizing candidate-name coverage and gaps

### Acceptance criteria

- The candidate list includes aliases rather than silently collapsing them.
- No candidate is treated as an established boundary without evidence.
- Every candidate has an initial research status: `unreviewed`, `in_research`, `verified`, `disputed`, or `insufficient_evidence`.

---

## Phase 2 — Evidence acquisition and source extraction

### Goal

Collect structured evidence for name usage, date ranges, and spatial descriptions.

### Priority source hierarchy

1. **Primary cartographic evidence**
   - Survey maps
   - Subdivision maps
   - Official city maps
   - Sanborn Fire Insurance maps
   - Block Books and assessor materials
   - Topographic maps
   - Historic aerial imagery

2. **Primary administrative evidence**
   - Ordinances
   - Planning area plans
   - Redevelopment plans
   - Historic-resource surveys
   - Landmark nominations
   - Environmental review documents
   - Public-agency reports

3. **Primary contemporaneous textual evidence**
   - Newspapers
   - City directories
   - Business directories
   - Census and property records
   - Community organization publications
   - Oral histories, tagged appropriately

4. **Secondary interpretive evidence**
   - Academic scholarship
   - Local historical organizations
   - Curated archives
   - Established local journalism
   - Reputable books and institutional histories

### Key initial source institutions

- San Francisco Public Library, San Francisco History Center
- San Francisco Planning
- San Francisco Assessor-Recorder and historical Block Books
- San Francisco Municipal Transportation Agency archives where transit naming is relevant
- OpenSF / DataSF and planning GIS portals
- Bancroft Library, University of California, Berkeley
- California Historical Society collections
- University of San Francisco Library map collections
- Library of Congress map collections
- David Rumsey Map Collection
- National Archives where federal maps or census materials are relevant

### Tasks

1. Register every source in the source registry before using it in a claim.
2. Extract exact quotations, map labels, sheet references, page numbers, and dates.
3. For map evidence, capture:
   - Map title
   - Publisher or agency
   - Publication date
   - Sheet identifier
   - Scale, if supplied
   - Legend or boundary notation
   - Map label transcription
   - Georeferencing potential and restrictions
4. Separate direct evidence from interpretation.
5. Add a source-quality assessment and rights/licensing note.

### Deliverables

- Expanded `data/sources/sources.jsonl`
- Source-note Markdown files under `sources/`
- Extracted evidence linked to candidate names
- A source coverage matrix by period and pilot subarea

### Acceptance criteria

- Every quoted phrase is exact and locatable.
- Every map claim identifies the map sheet or region.
- Secondary sources never overwrite contrary primary evidence without an editorial note.

---

## Phase 3 — Gazetteer and chronology construction

### Goal

Convert raw evidence into versioned place-name records and dated name events.

### Tasks

1. Create one canonical place record per underlying geographic concept where appropriate.
2. Create separate name events for each alias, spelling, rebrand, revival, or observed usage interval.
3. Record the source-specific extent of each claim.
4. Link related names using explicit relationship records.
5. Build a chronology of physical and institutional events that plausibly affect place meaning or boundaries.

### Required relationship types

- `alias_of`
- `former_name_of`
- `renamed_as`
- `revived_as`
- `part_of`
- `contains`
- `overlaps`
- `adjacent_to`
- `superseded_by`
- `marketing_overlay_of`
- `planning_overlay_of`
- `named_after`
- `derived_from`

### Core pilot chronology topics

- Yerba Buena to San Francisco naming change
- 1847 survey/planning framework and the 100 Vara grid
- Gold Rush growth and Rincon Hill residential development
- Shoreline filling and changes to bays, coves, and wharves
- 1869 Second Street Cut through Rincon Hill
- Industrialization of the South of Market and waterfront zones
- 1906 earthquake/fire and rebuilding
- Bay Bridge and Transbay Terminal development
- Mid-century freeway, redevelopment, and urban-renewal periods
- Late-20th-century SoMa usage and East SoMa planning
- Post-1989 waterfront/freeway transformation
- 21st-century Transbay, CBD, and branding overlays including The East Cut

### Deliverables

- `data/places/*.json` canonical place records
- `data/name-events/*.jsonl` time-bounded name-use assertions
- `data/events/chronology.jsonl`
- `docs/pilot-chronology.md`

### Acceptance criteria

- A researcher can distinguish name history from physical-history context.
- Every relationship is directional and has evidence.
- Date uncertainty is explicitly represented.

---

## Phase 4 — Historical geometry and boundary interpretation

### Goal

Create time-versioned, evidence-backed spatial representations without overstating certainty.

### Geometry rules

- Use an **exact polygon** only when an official or cartographically explicit boundary supports it.
- Use an **approximate polygon** when a source describes a coherent area but does not set exact edges.
- Use a **corridor** for street-based or linear identities.
- Use a **point plus radius/notes** for centers of activity with uncertain extent.
- Use **no geometry** when only name usage is evidenced.
- Keep competing geometries if two credible sources differ.

### Tasks

1. Choose a coordinate reference system and geometry format.
2. Store geometries as GeoJSON with versioned metadata.
3. Record source-specific geometry events rather than one definitive boundary.
4. Georeference historic map sheets when rights, quality, and labor permit.
5. Preserve georeferencing control points, transformation method, residual/error data, and operator notes.
6. Publish an uncertainty-friendly display intent for each geometry.
7. Review all approximate boundaries manually.

### Geometry metadata requirements

- `geometry_id`
- `place_id`
- `valid_from`
- `valid_to`
- `geometry_type`
- `precision`
- `boundary_basis`
- `source_id`
- `source_locator`
- `method`
- `confidence`
- `editorial_note`
- `created_by`
- `created_at`
- `review_status`

### Deliverables

- `data/geometries/*.geojson`
- `data/geometry-events/*.jsonl`
- `docs/geometry-methodology.md`
- Georeferencing logs and control-point files when applicable

### Acceptance criteria

- No geometry is detached from dated evidence.
- Approximate and disputed boundaries remain distinguishable from official ones.
- Modern GIS boundaries are never used to assert a historic boundary without explicit documentation.

---

## Phase 5 — Editorial review, conflict resolution, and publication readiness

### Goal

Make the pilot auditable, internally consistent, and ready for a future map consumer.

### Tasks

1. Audit every pilot record for required citations, dates, classification, and uncertainty.
2. Review source conflicts and maintain a conflict register.
3. Check alias handling and duplicate place records.
4. Confirm all external links, archive identifiers, and file references.
5. Validate machine-readable data using schema checks.
6. Write short human-readable place dossiers for the most complex pilot entries.
7. Tag a versioned release.

### Required dossier subjects

- South of Market / SoMa
- South of the Slot
- 100 Vara District
- Rincon Hill
- Happy Valley
- South Beach
- East SoMa
- The East Cut

### Deliverables

- `docs/conflict-register.md`
- `docs/research-gaps.md`
- `docs/place-dossiers/`
- Validated data release
- Changelog and release notes

### Acceptance criteria

- A reviewer can reproduce every major claim from repository contents.
- The project clearly identifies disputed, unverified, and incomplete material.
- The data can be consumed by a future timeline-map application without reinterpreting prose.

---

## 5. Research outputs and quality bar

The agent should produce the following, in order:

1. A GitHub-native repository with documented standards.
2. A source registry with stable source identifiers.
3. A pilot candidate-name inventory.
4. Structured source notes and evidence extracts.
5. A machine-readable historical gazetteer.
6. Time-bounded geometry records where support exists.
7. A chronology of contextual city changes.
8. An evidence/conflict register.
9. Human-readable dossiers for complex and contested names.
10. A tagged pilot release with changelog.

A successful pilot is not one that has the most polygons. It is one where every meaningful assertion has traceable provenance and where uncertainty is visible rather than hidden.

---

## 6. Source and evidence model

### Source record

```json
{
  "source_id": "sfpl-map-1899-sanborn-vol-01-sheet-04",
  "title": "Sanborn Fire Insurance Map, Volume 1, Sheet 4",
  "source_type": "primary_map",
  "creator": "Sanborn Map Company",
  "publication_date": "1899",
  "repository": "San Francisco Public Library",
  "repository_identifier": "REPLACE_WITH_ARCHIVE_ID",
  "stable_url": "REPLACE_WITH_URL",
  "accessed_date": "YYYY-MM-DD",
  "rights_note": "REPLACE_WITH_RIGHTS_INFORMATION",
  "coverage_note": "REPLACE_WITH_GEOGRAPHIC_COVERAGE",
  "reliability_note": "Primary cartographic source; labels and drawn boundaries should be interpreted sheet by sheet."
}
```

### Evidence assertion

```json
{
  "assertion_id": "assertion-south-of-the-slot-001",
  "subject_id": "place-south-of-market-001",
  "predicate": "name_used_for",
  "object": "South of the Slot",
  "asserted_from": "1890",
  "asserted_to": "1935",
  "date_precision": "range",
  "evidence_type": "secondary_historical_account",
  "source_id": "sf-heritage-south-of-market-month-001",
  "source_locator": "paragraph 3",
  "quotation": "REPLACE_WITH_EXACT_QUOTATION",
  "interpretation": "The term is described as a colloquial designation for the district south of Market Street.",
  "confidence": "medium",
  "review_status": "needs_primary_confirmation"
}
```

### Place record

```json
{
  "place_id": "place-rincon-hill-001",
  "canonical_name": "Rincon Hill",
  "place_classes": ["topographic_feature", "neighborhood"],
  "description": "A historic hill and later neighborhood identity near the southeastern edge of downtown San Francisco.",
  "status": "active_with_historical_layers",
  "aliases": ["Rincon"],
  "notes": "Do not equate all historic uses with the current neighborhood extent.",
  "created_at": "YYYY-MM-DD",
  "updated_at": "YYYY-MM-DD"
}
```

### Name-event record

```json
{
  "name_event_id": "name-event-rincon-hill-1848",
  "place_id": "place-rincon-hill-001",
  "name": "Rincon Hill",
  "name_normalized": "rincon hill",
  "name_status": "active",
  "valid_from": "1848",
  "valid_to": null,
  "date_precision": "year",
  "usage_context": "topographic_and_neighborhood",
  "source_id": "REPLACE_WITH_SOURCE_ID",
  "source_locator": "REPLACE_WITH_LOCATOR",
  "confidence": "medium",
  "editorial_note": "The name’s geographical meaning varies by period and source."
}
```

### Geometry-event record

```json
{
  "geometry_id": "geometry-rincon-hill-pre-1869-001",
  "place_id": "place-rincon-hill-001",
  "valid_from": "1848",
  "valid_to": "1868",
  "geometry_type": "approximate_polygon",
  "precision": "approximate",
  "boundary_basis": "historic_map_and_secondary_synthesis",
  "source_id": "REPLACE_WITH_SOURCE_ID",
  "source_locator": "REPLACE_WITH_LOCATOR",
  "method": "Digitized from historically georeferenced cartographic evidence; boundary remains interpretive.",
  "confidence": "medium",
  "editorial_note": "Represents a historical interpretation, not a statutory neighborhood boundary.",
  "geojson_path": "data/geometries/rincon-hill-pre-1869.geojson",
  "review_status": "draft"
}
```

---

## 7. Controlled vocabularies

### Place classes

- `official_jurisdiction`
- `survey_district`
- `planning_area`
- `redevelopment_area`
- `neighborhood`
- `sub_neighborhood`
- `topographic_feature`
- `cultural_district`
- `ethnic_district`
- `industrial_district`
- `commercial_district`
- `social_district`
- `corridor`
- `waterfront_or_shoreline_feature`
- `real_estate_or_branding_overlay`
- `historical_or_retrospective_label`
- `landmark_or_locality`

### Name status

- `active`
- `former`
- `declining`
- `revived`
- `historical_reference_only`
- `proposed`
- `disputed`
- `unknown`

### Geometry type

- `exact_polygon`
- `approximate_polygon`
- `line_or_corridor`
- `point`
- `point_with_radius`
- `multi_geometry`
- `unknown`

### Boundary basis

- `statute_or_ordinance`
- `official_map`
- `planning_document`
- `redevelopment_document`
- `historic_map_label`
- `survey_or_assessor_record`
- `newspaper_or_directory_usage`
- `oral_history`
- `community_organization`
- `scholarly_synthesis`
- `editorial_synthesis`

### Confidence levels

- `high`: Direct, dated, specific source support with unambiguous interpretation.
- `medium`: Credible support, but geography/date requires interpretation or is corroborated indirectly.
- `low`: Limited, conflicting, retrospective, or weakly specific support.
- `unassessed`: Not yet reviewed.

---

## 8. GitHub-native repository structure

```text
sf-historical-place-names/
├── README.md
├── LICENSE
├── CITATION.cff
├── CONTRIBUTING.md
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── new-place-name.md
│   │   ├── new-source.md
│   │   ├── boundary-dispute.md
│   │   ├── research-gap.md
│   │   └── data-correction.md
│   ├── pull_request_template.md
│   └── workflows/
│       └── validate-data.yml
├── docs/
│   ├── data-model.md
│   ├── editorial-standards.md
│   ├── controlled-vocabularies.md
│   ├── geometry-methodology.md
│   ├── research-workflow.md
│   ├── pilot-chronology.md
│   ├── conflict-register.md
│   ├── research-gaps.md
│   └── place-dossiers/
├── data/
│   ├── sources/
│   │   └── sources.jsonl
│   ├── places/
│   │   ├── candidate-names.jsonl
│   │   └── canonical/
│   ├── name-events/
│   ├── assertions/
│   ├── geometries/
│   ├── geometry-events/
│   ├── relationships/
│   ├── events/
│   └── vocabularies/
├── sources/
│   ├── primary-maps/
│   ├── primary-documents/
│   ├── newspapers-and-directories/
│   └── secondary/
├── research/
│   ├── inbox/
│   ├── working-notes/
│   └── completed-memos/
├── schemas/
│   ├── source.schema.json
│   ├── place.schema.json
│   ├── name-event.schema.json
│   ├── assertion.schema.json
│   ├── geometry-event.schema.json
│   └── relationship.schema.json
└── scripts/
    └── validate_data.py
```

### Repository rules

- Markdown is the human-readable canonical research layer.
- JSON/JSONL and GeoJSON are the machine-readable data layers.
- Never embed unlicensed high-resolution source scans in the repository unless rights clearly permit it.
- Store metadata, citations, and derivative geometries even when original scans must remain externally hosted.
- Use pull requests for all changes to verified data.
- Use issues to track ambiguity, missing sources, disputes, and research questions.
- Every release must include a changelog describing added, changed, deprecated, and corrected records.

---

## 9. Provenance, attribution, and evolution

### Provenance requirements

Each record must make it possible to answer:

- Who created the record?
- When was it created and last revised?
- Which sources support it?
- What exact part of each source is being interpreted?
- What transformation was performed, particularly for geometry?
- What uncertainty remains?
- What changed between repository versions?

### Git workflow

- Use a protected `main` branch.
- Create topic branches such as `research/rincon-hill-1869-cut` or `source/sanborn-1899-vol-1`.
- Write commits that name the research action, not just the file action.
  - Good: `Add 1869 evidence for Second Street Cut and Rincon Hill geometry`
  - Weak: `Update data`
- Link commits and pull requests to issue IDs.
- Require review for new verified claims and geometry changes.
- Tag releases using semantic or date-based versioning, for example `v0.1.0-pilot`.

### Change policy

Never delete a superseded research claim merely because it was corrected. Preserve it with:

- `status: superseded` or `status: withdrawn`
- An explanation of why it changed
- The commit or pull request that introduced the correction
- Links to the new preferred assertion

This supports scholarly auditability and allows the project’s own interpretation to evolve transparently.

---

## 10. Research workflow for each name

For each candidate name, follow this exact sequence:

1. Create or locate the candidate-name issue.
2. Search for primary and reputable secondary references.
3. Add every source to the source registry.
4. Extract exact, dated evidence of usage.
5. Determine whether the evidence supports a place, a name event, a geometry, or only a historical interpretation.
6. Add machine-readable records and a concise Markdown research note.
7. Add relationships to related place records.
8. Record uncertainty and conflicts explicitly.
9. Submit the record for review.
10. Close the issue only when the entry has a source-backed status; use `insufficient_evidence` where needed rather than forcing a conclusion.

---

## 11. Pilot-specific research notes

### South of Market / SoMa

Treat `South of Market` as a broad directional-geographic term whose practical extent may differ by period and source. Treat `SoMa` as a separate name event and investigate its emergence, adoption, and changing usage rather than assuming it is simply equivalent at all times.

### South of the Slot

Treat this as a historically situated colloquial/social designation. The term refers to the cable-car conduit or “slot” on Market Street and should not be represented as an official district unless a specific official source establishes that usage.

### 100 Vara District

Treat this primarily as a land-survey or property-grid designation. Do not collapse it into SoMa. Its geometry may be comparatively well defined in survey materials, but its social or neighborhood meaning must be researched separately.

### Rincon Hill and the Second Street Cut

Model the 1869 Second Street Cut as a physical transformation event. Research pre-cut and post-cut usage and extent separately. The name may refer to topography, an elite residential district, later industrial context, and current redevelopment-era neighborhood identity.

### The East Cut

Treat this as a recent, source-datable naming/branding or community-benefit-district-led identity. Document its stated historical reference to the Second Street Cut, its adoption process, its stated boundaries, and its relationship to older names such as Rincon Hill, South Beach, Transbay, and SoMa.

---

## 12. Out-of-scope items

The execution agent should not:

- Build the public map, time-slider UI, search UI, or consumer application.
- Represent the research corpus as an official city neighborhood map unless an official source specifically supports a given layer.
- Infer historical boundaries from present-day real-estate listings.
- Treat marketing language as neutral historical fact.
- Replace ambiguous historical evidence with a single clean modern polygon.
- Copy copyrighted maps or text into the repository beyond legally permissible metadata, quotations, thumbnails, or derived research outputs.

---

## 13. Definition of done for the pilot

The downtown/SoMa pilot is complete when it includes:

- At least 15–20 candidate or canonical place names.
- At least 40 source records across primary and secondary source classes.
- A documented chronology from 1847 to the present.
- Source-backed name events for every pilot place.
- At least one reviewed geometry event where credible spatial evidence exists for each major pilot concept.
- Explicit uncertainty/dispute notes for every non-exact boundary.
- Dossiers for the eight required complex names.
- Automated validation passing for all published machine-readable records.
- A tagged release, changelog, and open research-gap list.

---

## 14. Recommended first agent action

Start with Phase 0, then complete the Phase 1 candidate-name inventory before attempting historical GIS work. The first agent output should be a pull request containing repository standards, controlled vocabularies, a source registry seed, and the downtown/SoMa candidate-name list with research-status fields.

Do not begin drawing comprehensive boundaries until the source registry and assertion model are in place.
