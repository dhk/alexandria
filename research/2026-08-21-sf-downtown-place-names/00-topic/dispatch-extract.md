# San Francisco Historical Place Names — research-bearing extract

This is an extract from a longer project brief, prepared for a research
commission. The omitted material (Phases 0-5 execution plan, GitHub
repository structure, JSON record schemas, Git workflow, and the
definition-of-done checklist) tells an execution agent how to build and
govern a repository. It is being handled separately and is not what this
commission is asking for. What remains below is the part that states a
research question: the questions themselves, the geographic and temporal
scope, the principles that govern how evidence must be handled, the
controlled vocabularies whose closed sets the answer must use, the
name-specific research notes, and the explicit out-of-scope list.

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

