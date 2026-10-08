# A corpus-wide sweep for historical place names

**Status:** analysis, single-analyst, not graded. Descriptive inventory only —
it records what eleven documents write down, and adjudicates nothing.
**Instrument:** `02-run-plan/quote.py`. Every printed page below is the page
`quote.py` computed from the manifest's recorded offset, or an explicit refusal
to compute one. **Every row is `FETCHED`.**

## What was swept, and what was not

The eleven documents that were in
`04-normalized/sources/manifest.json` when this sweep began:

`central-soma-deir-cultural`, `citywide-hcs-howto`, `corbett-heights-hcs-2017`,
`japantown-hcs-2008`, `market-octavia-context-2007`, `mission-district-context`,
`modern-architecture-context-2011`, `north-beach-hcs`, `parkside-statement-2008`,
`soma-context-2009`, `sunset-hcs`.

**Three more arrived while the sweep was running** — `wnp-richmond-district`,
`wnp-sea-cliff` and `soma-filipino-heritage-2013`, added by another session that
is live in the manifest. `quote.py --list` reported 11 documents at the start
and 14 at the end. Those three were **not swept**, and nothing below is
evidence about them.

## Method, in three steps

1. **Discover.** A throwaway script (written to scratch, not to the repo) read
   the local extractions, repaired the commonest extraction damage — a capital
   orphaned from its word, `W illiam` → `William` — and pulled capitalised
   phrases ending in a place-noun (`Valley`, `Flat`, `Hill`, `Heights`,
   `Homestead`, `Tract`, `Addition`, `Rancho`, `Cove`, `Point`, `Gulch`,
   `District`, `Lands`, …) plus phrases introduced by `known as` / `called` /
   `named`. That produced **1,163 raw candidate strings**. A second pass tested
   **130 seed names** a reader of San Francisco would expect; **19 of the 130
   appear nowhere in the corpus** (see below).
2. **Verify.** **165 queries** were then put through `quote.py` — of which 6
   were sentence probes rather than names, so **159 name candidates were
   verified against the documents**. Discovery output was never used as
   evidence; only `quote.py`'s output is quoted here.
3. **Discard.** Aggressively, and by category. See *What was thrown away*.

**No name below is dated by proximity to a number.** Dates appear only in the
separate *Dates the documents actually assert* section, and only where the
quoted sentence asserts the date itself.

---

## South of Market and the bay shore

Included as raw input to the SoMa work happening elsewhere. **No extent is
adjudicated here and no conflict is resolved here.**

| name | document | printed page (PDF page) | phrase |
|---|---|---|---|
| Yelamu | `soma-context-2009` | p.14 (PDF p.16) | "the northern part of the San Francisco Peninsula was located within the Yelamu tribal territory of the Ohlone" |
| Chutchui | `soma-context-2009` | p.14 (PDF p.16) | "The closest Ohlone village to what is now the South of Market Area was called Chutchui and it was located on Mission Creek" |
| Sitlintac | `soma-context-2009` | p.14 (PDF p.16) | "another village on San Francisco Bay called Sitlintac to harvest shellfish on the tidal flats of what is now the Mission Bay area" |
| Yerba Buena Cove | `soma-context-2009` | p.15 (PDF p.17) | "A traveler disembarking at Yerba Buena Cove would have initially encountered a pristine white pebble beach backed by towering sand dunes" |
| Rincon Point | `soma-context-2009` | p.16 (PDF p.18) | "an excellent natural anchorage protected from wind and storms by Rincon Point and Clark's Point" |
| Clark's Point | `soma-context-2009` | p.16 (PDF p.18) | *same sentence* |
| Happy Valley | `soma-context-2009` | p.15 (PDF p.17) | "a narrow lush valley filled with oaks and willows. Later called Happy Valley, this declivity was sheltered from the fierce afternoon winds" |
| Pleasant Valley | `soma-context-2009` | p.15 (PDF p.17) | "Just south of Happy Valley was another valley later called Pleasant Valley" |
| Tar Flat | `soma-context-2009` | p.30 (PDF p.32) | "\"Tar Flat\" The increasing dominance of heavy industry in the South of Market Area gradually displaced the bucolic Gold Rush-era neighborhoods of Happy Valley…" |
| Steamboat Point | `soma-context-2009` | p.20 (PDF p.22) | "the beach at the foot of 1st Street… became the location of several boatyards, giving the area the name Steamboat Point" |
| Rincon Hill | `soma-context-2009` | p.3 (PDF p.5) | "presently only the stump of Rincon Hill beneath the Bay Bridge adds any noticeable topographic relief" |
| Mission Bay | `soma-context-2009` | p.3 (PDF p.5) | "Similar to other \"made land\" such as the Marina District and Mission Bay, the South of Market Area is almost entirely manmade" |
| South Park | `soma-context-2009` | p.1 (PDF p.3) | "the high technology node of \"Multimedia Gulch\" near South Park" |
| Multimedia Gulch | `soma-context-2009` | p.1 (PDF p.3) | *same sentence* |
| South of the Slot | `market-octavia-context-2007` | p.39 (PDF p.39) | "The character of the South of Market area, or \"South of the Slot\" as it was then known, is reflected in the writings of Jack London" |
| Manilatown | `soma-context-2009` | p.60 (PDF p.62) | "Initially settled north of Market Street in an area called Manilatown, near the intersection of Washington and Kearny streets" |
| Manilatown | `central-soma-deir-cultural` | IV.C-12 (PDF p.12) | "demolition of numerous businesses and residential hotels along Kearny and adjacent streets, an area then known as Manilatown" |
| Greek Town | `soma-context-2009` | p.59 (PDF p.61) | "the presence of so many Greek businesses gave the area the name Greek Town" |
| Wholesale District | `soma-context-2009` | p.37 (PDF p.39) | "Outside of the \"Wholesale District\" (centered at the intersection of 2nd and Mission streets)" |
| Point San Quentin | `soma-context-2009` | p.33 (PDF p.35) | "Long Bridge from Steamboat Point, across Mission Bay, to Point San Quentin in the Potrero District" |
| Polk Gulch | `soma-context-2009` | p.73 (PDF p.75) | "Polk Gulch, the Haight-Ashbury, and the South of Market Area increasingly gained a visible gay and lesbian presence in the 1960s" |
| Happy Valley / Pleasant Valley | `central-soma-deir-cultural` | IV.C-5 (PDF p.5) | "concentrated in \"Happy Valley,\" located along the shoreline —approximately First Street—between Market and Mission Streets, and \"Pleasant Valley\" to the south" |
| Yerba Buena Cove | `central-soma-deir-cultural` | IV.C-5 (PDF p.5) | "connect the growing settlement at Yerba Buena Cove (today's Financial District) with Mission Dolores" |
| Steamboat Point / South Park | `central-soma-deir-cultural` | IV.C-6 (PDF p.6) | "the Second Street Cut in 1869, which sliced through Rincon Hill to create a direct route to the shipyards at Steamboat Point" |
| Yelamu | `central-soma-deir-cultural` | IV.C-44 (PDF p.44) | "The Ohlone tribe that occupied the northern end of the San Francisco peninsula in the late 18th century is known under the general term Yelamu" |

## North Beach and the northern waterfront

| name | document | printed page (PDF page) | phrase |
|---|---|---|---|
| Barbary Coast | `north-beach-hcs` | p.9 (PDF p.15) | "on the other side of Chinatown and beyond the Barbary Coast" |
| Sydney Town | `north-beach-hcs` | p.8 (PDF p.14) | "portions of the area along Broadway and on nearby blocks, especially on the north side, were called Sydney Town and Chile Town" |
| Chile Town | `north-beach-hcs` | p.8 (PDF p.14) | *same sentence* |
| Dago Town | `north-beach-hcs` | p.8 (PDF p.14) | "Montgomery Street was dago Town" |
| Little Italy | `north-beach-hcs` | p.8 (PDF p.14) | "By the late 1850s the community of duPont Street was known as little Italy" |
| Latin Quarter | `north-beach-hcs` | p.8 (PDF p.14) | "In 1890, the San Francisco Chronicle referred to the \"latin Quarter\" as the neighborhood from which children came to the North Cosmopolitan school" |
| Italian Quarter | `north-beach-hcs` | p.31 (PDF p.37) | "The busiest portion of the city today is the northern, or what was known as the Italian quarter" |
| Bohemian Quarter | `north-beach-hcs` | p.56 (PDF p.62) | "San Francisco's Historic Bohemian Quarter Succumbs To the Forces of Economics and Modernism" |
| Telegraph Hill | `north-beach-hcs` | p.11 (PDF p.17) | "this valley (not yet called Telegraph Hill) rose up out of the bay at the northeast corner of the peninsula" |
| North Point | `north-beach-hcs` | p.6 (PDF p.12) | "between North Point near the present-day corner of Kearny and Bay streets and Point San Jose" |
| Point San Jose / Black Point | `north-beach-hcs` | p.6 (PDF p.12) | "Point San Jose, later Black Point in Fort Mason" |
| Meiggs Wharf | `corbett-heights-hcs-2017` | p.237 (PDF p.244) | "The North Beach & Mission Railway ran horse cars between Meiggs Wharf in North Beach and Folsom Street" |

## Japantown, the Fillmore and the Western Addition

`japantown-hcs-2008` **has no established printed-to-PDF page offset**, so
`quote.py` declines to claim a printed page for any of its hits. Those rows say
so rather than guessing.

| name | document | printed page (PDF page) | phrase |
|---|---|---|---|
| Nihonmachi | `japantown-hcs-2008` | **printed page NOT CLAIMED** (PDF p.8) | "Japanese homes and businesses on Buchanan Street between Geary and Pine streets bloomed into a bustling Nihonmachi" |
| Nihonmachi | `modern-architecture-context-2011` | p.44 (PDF p.48) | "The A-1 area also included Nihonmachi (Japantown) and numerous Victorian houses" |
| Little Osaka | `japantown-hcs-2008` | **printed page NOT CLAIMED** (PDF p.33) | "this would prevent the reestablishment of \"Little Tokyos\" and \"Little Osakas\"" |
| Little Osaka | `modern-architecture-context-2011` | p.34 (PDF p.38) | "Defense workers also settled in the Little Osaka section of the Fillmore District" |
| Harlem of the West | `modern-architecture-context-2011` | p.44 (PDF p.48) | "These areas included the Fillmore District, noted as the \"Harlem of the West\" for its large black population" |
| Fillmore District | `modern-architecture-context-2011` | p.34 (PDF p.38) | *same sentence as Little Osaka* |
| Western Addition | `japantown-hcs-2008` | **printed page NOT CLAIMED** (PDF p.3) | "ultimately adding sections named Potrero Nuevo, Mission Dolores, Horner's Addition and the Western Addition" |
| Western Addition | `market-octavia-context-2007` | p.8 (PDF p.8) | "the Western Addition still technically encompasses a large swath of the city, including neighborhoods as disparate as Hayes Valley, Alamo Square, Japantown and Pacific Heights" |
| Japantown | `citywide-hcs-howto` | p.11 (PDF p.11) | "1698 Post Street Japantown 1979 … The property falls within the bounds of…" |

## Market and Octavia

| name | document | printed page (PDF page) | phrase |
|---|---|---|---|
| Duboce Triangle | `market-octavia-context-2007` | p.7 (PDF p.7) | "Duboce Triangle, historically known as Gaffney's Triangle, is located on the north side of Market Street, opposite Eureka Valley" |
| Gaffney's Triangle | `market-octavia-context-2007` | p.7 (PDF p.7) | *same sentence* |
| Lower Haight | `market-octavia-context-2007` | p.2 (PDF p.2) | "several distinct neighborhoods, including Duboce Triangle, the Lower Haight, Hayes Valley, the Western Addition, Civic Center, South of Market, Inner Mission, Eureka Valley, and the Market Street Corridor" |
| Hayes Valley | `market-octavia-context-2007` | p.2 (PDF p.2) | *same sentence* |
| Hayes Tract | `market-octavia-context-2007` | p.36 (PDF p.36) | "The railroad, which followed the route of MUNI's current 21-Hayes line, was initially completed in 1860, linking the Hayes Tract" |
| Mission Dolores Tract | `market-octavia-context-2007` | p.44 (PDF p.44) | "Duboce Triangle was not originally surveyed as part of the Western Addition. Rather, it was surveyed as part of the Mission Dolores Tract" |
| Reservoir Hill | `market-octavia-context-2007` | p.47 (PDF p.47) | "as well as Reservoir Hill (now Mint Hill), blocked the westward extension of Market Street" |
| Mint Hill | `market-octavia-context-2007` | p.6 (PDF p.6) | "Isolated, serpentine outcroppings exist within the Plan Area, especially Mint Hill, near the intersection of Hermann and Buchanan streets" |
| Bayshore Mound | `market-octavia-context-2007` | p.21 (PDF p.21) | "The most significant of these sites was a vast midden known as the Bayshore Mound" |
| Pueblo Lands | `market-octavia-context-2007` | p.28 (PDF p.28) | "the existence of squatters on Pueblo Lands (territory of the City of San Francisco inherited from the Mexican government)" |
| Outside Lands | `market-octavia-context-2007` | p.32 (PDF p.32) | "territories that were subject to the Third Consolidation Act of 1856, known as the Outside Lands of San Francisco" |
| Mission Addition | `market-octavia-context-2007` | p.31 (PDF p.31) | "further surveys and additions to the city, including Horner's Addition, Mission Dolores, the Mission Addition, and the Western Addition" |
| Horner's Addition | `market-octavia-context-2007` | p.31 (PDF p.31) | *same sentence* |
| Potrero Nuevo / Potrero Viejo | `market-octavia-context-2007` | p.23 (PDF p.23) | "Cattle were run on massive pastures called Potrero Nuevo (now Potrero Hill) and Potrero Viejo (now Bernal Heights)" |
| Mission Miracle Mile | `market-octavia-context-2007` | p.56 (PDF p.56) | "Later called the \"Mission Miracle Mile,\" the business district of the Mission became an alternative to the department stores of Market Street" |

## The Mission

| name | document | printed page (PDF page) | phrase |
|---|---|---|---|
| Laguna de Nuestra Señora de los Dolores | `mission-district-context` | p.15 (PDF p.18) | "the freshwater lagoon that de Anza had named Laguna de Nuestra Senora de los Dolores, \"Lake of our Lady of Sorrows\", near what is now the intersection of Camp and Albion Streets" |
| Bernal Gap | `mission-district-context` | p.15 (PDF p.18) | "entered the valley through a cleft in the hills bordering the valley to the south, now called the Bernal Gap" |
| Mission Bay | `mission-district-context` | p.15 (PDF p.18) | "a mill site at an outfall of the creek near the large cove, which was later named Mission Bay" |
| Potrero Viejo | `mission-district-context` | p.16 (PDF p.19) | "this wall demarcated the potrero viejo, or old pasture, to the south, located on present-day Bernal Heights" |
| Potrero Nuevo | `mission-district-context` | p.16 (PDF p.19) | "across the neck of the peninsula that is now Potrero Hill, but then was called potrero nuevo, or new pasture" |
| Precita Creek | `mission-district-context` | p.3 (PDF p.6) | "Cesar Chavez runs along the old alignment of Precita Creek, an under-grounded stream that marked the boundaries of early Spanish and Mexican land divisions" |
| Rancho San Miguel | `mission-district-context` | p.18 (PDF p.21) | "Jose Noe, a justice of the peace, obtained the Rancho San Miguel grant (4,443 acres), bounded on the northeast by the Old Mission Road, in 1845" |
| Horner's Addition | `mission-district-context` | p.22 (PDF p.25) | "The earliest subdivision was Horner's Addition, the easternmost slice of Rancho San Miguel, located between the Old Mission Road and present-day Church Street" |
| Mission Addition / Mission Dolores Addition | `mission-district-context` | p.23 (PDF p.26) | "an area that became known as the Mission Addition or the Mission Dolores Addition by the mid-1850s" |
| Treat Tract | `mission-district-context` | p.33 (PDF p.36) | "This grouping of buildings also coincided with a large parcel, the Treat Tract, upon which the Pioneer Race Course had operated until about 1863" |
| Perkins Tract | `mission-district-context` | p.33 (PDF p.36) | "This large area of buildings coincided neatly with the extent of the Perkins Tract, apparently a portion of the old Broderick property, which had contained the Union Race Course" |
| Butchertown | `mission-district-context` | p.47 (PDF p.50) | "a row of tanneries was strung between Army and Serpentine Streets, near the area to the east that was known as Butchertown" |
| Inner Mission | `mission-district-context` | p.1 (PDF p.4) | "The Mission District is also known as the \"Inner Mission,\" but is referred to herein simply as the Mission District" |
| Outer Mission | `mission-district-context` | p.1 (PDF p.4) | "The \"Outer Mission\" is a district of San Francisco with a different development history located some distance to the south" |
| Mission Terrace / Excelsior | `mission-district-context` | p.1 (PDF p.4) | "The Outer Mission area is also known as \"Mission Terrace\" and the \"Excelsior\"" |
| Outside Lands | `mission-district-context` | p.21 (PDF p.24) | "In the \"Outside Lands\", which included the Mission valley and the Mexican ranchos, settlers established themselves legally by acquiring land from ranchers or illegally by…" |
| Noe Valley / Bernal Heights / Potrero Hill | `mission-district-context` | p.20 (PDF p.23) | "other Californios are remembered in the names of areas and streets in the surrounding former rancho lands of Noe Valley (Noe and Sanchez Streets), Bernal Heights (Bernal Street), and Potrero Hill (de Haro Street)" |
| Showplace Square | `mission-district-context` | p.1 (PDF p.4) | "along with Showplace Square, an adjacent area that shares a similar and related history" |

## Corbett Heights, Eureka Valley and the central highlands

`corbett-heights-hcs-2017` records exception pages `1-7, 260-261` — its front
and back matter print numbers the offset does not explain. `quote.py` refuses a
printed page on those, so every dated plat below is cited from its **body**
section heading, not from the table of contents that first surfaced it.

| name | document | printed page (PDF page) | phrase |
|---|---|---|---|
| Corbett Heights | `corbett-heights-hcs-2017` | p.3 (PDF p.10) | "Corbett Heights is a collage of street plans and subdivisions from different eras" |
| Eureka Valley | `corbett-heights-hcs-2017` | p.7 (PDF p.14) | "It may also be that Eureka Valley is named for the Eureka Homestead Association or for the state motto, \"Eureka!\"" |
| Eureka Homestead Association | `corbett-heights-hcs-2017` | p.7 (PDF p.14) | "This stream crossed the area of the 1864 Eureka Homestead Association within the area bound by Seventeenth and Twentieth, Noe and Douglass Streets" |
| Eureka Valley Homestead Association | `corbett-heights-hcs-2017` | p.3 (PDF p.10) | "Douglass Street is the western boundary of the Eureka Valley Homestead Association" |
| Market Street Homestead Association | `corbett-heights-hcs-2017` | p.37 (PDF p.44) | "a new overlapping entity was established called the Market Street Homestead Association with the intention of purchasing a substantial part of the Pioche & Ro…" |
| Pioche & Robinson Subdivision | `corbett-heights-hcs-2017` | p.33 (PDF p.40) | "By far the largest of the primary subdivisions of Corbett Heights is that of Pioche & Robinson of 1867, consisting of over two-thirds of the land area of the neighborhood" |
| William R. McKee Subdivision | `corbett-heights-hcs-2017` | p.31 (PDF p.38) | "Among the new subdivisions west of Horner's Addition that would later be included in an enlarged version of Horner's Addition, one was in an area that would become part of Corbett Heights" |
| Park Lane Tract | `corbett-heights-hcs-2017` | p.39 (PDF p.46) | "The northwest corner of Corbett Heights (that area between Corbett Road and the north boundary of San Miguel Rancho, and west of what would become the McKee Subdivision) was sold by Pioche & Robin…" |
| Clover Heights | `corbett-heights-hcs-2017` | p.15 (PDF p.22) | "Corbett Heights is a neighborhood based on four primary surveys: the Pioche & Robinson Subdivision, the McKee Subdivision, the Park Lane Tract, and Clover Heights" |
| Ashbury Park | `corbett-heights-hcs-2017` | p.131 (PDF p.138) | "One part of the Simons-Fout land was developed by Edwards, Brewster & Clover, a real estate development firm, as Ashbury Park" |
| Ashbury Heights / Clarendon Heights | `corbett-heights-hcs-2017` | p.47 (PDF p.54) | "The new neighborhoods surveyed and developed by Adolph Sutro and others in and around the central highlands — Ashbury Heights, Clarendon Heights, and the Park Lane Tract among them" |
| San Miguel Rancho | `corbett-heights-hcs-2017` | p.3 (PDF p.10) | "history (the northern edge of Rancho San Miguel on the north)" |
| Noe Rancho | `corbett-heights-hcs-2017` | p.226 (PDF p.233) | "Noe received San Miguel Rancho, sometimes referred to as Noe Rancho (e.g., Gardiner 1854)" |
| Flint Tract | `corbett-heights-hcs-2017` | p.58 (PDF p.65) | "the Gray brothers purchased a site on Corona Heights in the Flint Tract, just north of the San Miguel Rancho boundary line" |
| College Homestead / University Extension | `corbett-heights-hcs-2017` | p.241 (PDF p.248) | "He adapted the Pioche & Robinson Subdivision for the Market Street Homestead Association and also developed the University Extension and College Homestead Associations in San Miguel Rancho" |
| Corona Heights / Buena Vista Peak / Mount Sutro / Twin Peaks | `corbett-heights-hcs-2017` | p.11 (PDF p.18) | "a partial ring of hills outside the study area around a sloping shelf of land: counterclockwise, these are Corona Heights, Buena Vista Peak, Mount Sutro, and Twin Peaks" |
| The Twin Peaks Group | `corbett-heights-hcs-2017` | p.11 (PDF p.18) | "Daniel Burnham and Edward Bennett described \"The Twin Peaks Group,\" meaning this ring of hills" |
| Mount Olympus | `corbett-heights-hcs-2017` | p.3 (PDF p.10) | "Popular sources have identified the geographical center of San Francisco as Mount Olympus, located in a portion of the Park Lane Tract" |
| Blue Mountain → Mount Parnassus → Mount Sutro | `corbett-heights-hcs-2017` | p.44 (PDF p.51) | "In the same spirit that he named Mount Olympus near Corbett Heights, he renamed Blue Mountain Mount Parnassus — today it is called Mount Sutro" |
| Eureka Peak / Noe Peak | `corbett-heights-hcs-2017` | p.7 (PDF p.14) | "Noe Peak on the south and Eureka Peak on the north drained into Noe Valley and Eureka Valley, respectively" |
| Kite Hill / Solari Hill | `corbett-heights-hcs-2017` | p.21 (PDF p.28) | "Kite Hill, on the south side of the Corbett Heights amphitheater, was known as Solari Hill for the Solari family dairy" |
| Tank Hill | `corbett-heights-hcs-2017` | p.52 (PDF p.59) | "The large steel tank built as part of the original reservoir complex gave Tank Hill its name" |
| Corbett Slope / Corbett Ord Triangle | `corbett-heights-hcs-2017` | p.170 (PDF p.177) | "Among voluntary gardens, Corbett Slope and the Corbett Ord Triangle, both owned by the San Francisco Department of Public…" |
| Merced Heights (second Kite Hill) | `corbett-heights-hcs-2017` | p.169 (PDF p.176) | "A second Kite Hill in San Francisco is at \"the western summit of Merced Heights at Shields and Ramsell\"" |

The Corbett statement also names, on printed p.5 (PDF p.12), two names it says
are **wrong** for this ground: "Some names have incorrectly referred to the area
or to parts of it, like Ashbury Park and Clarendon Heights." Both are in the
table above because the document writes them down; the document's own objection
travels with them.

## The Sunset, Parkside and the Outside Lands

| name | document | printed page (PDF page) | phrase |
|---|---|---|---|
| Outside Lands | `sunset-hcs` | p.19 (PDF p.19) | "much of the western half of what is now known as San Francisco was officially named the \"Outside Lands,\" a vast area of sand dunes that was outside of the City's boundaries" |
| Pueblo Lands | `parkside-statement-2008` | p.10 (PDF p.14) | "Ownership of these former Spanish/Mexican pueblo lands was disputed between the City of San Francisco and the federal government until May 1865" |
| Laguna de la Merced Rancho | `parkside-statement-2008` | p.9 (PDF p.13) | "South of the Parkside lay the 2,000-acre Laguna de la Merced Rancho, named after Lake Merced" |
| Rancho San Miguel | `parkside-statement-2008` | p.10 (PDF p.14) | "To the east of the Parkside was the 4,443-acre Rancho San Miguel, which extended from today's Forest Side Street in West Portal northeasterly to Mount Sutro" |
| Carville | `parkside-statement-2008` | p.17 (PDF p.21) | "Initially called \"Carville,\" the neighborhood grew, with more conventional houses constructed after the turn of the century, and became known as Oceanside" |
| Oceanside | `sunset-hcs` | p.20 (PDF p.20) | "Originally named \"Carville\" this area grew to include small-scale beach cottages and evolved into a permanent neighborhood, known as Oceanside" |
| Parkside District | `parkside-statement-2008` | **printed page NOT CLAIMED** (PDF p.1) | "San Francisco's Parkside District: 1905 - 1957" — offset +4 puts PDF p.1 in unnumbered front matter |
| Golden Gate Heights | `parkside-statement-2008` | p.7 (PDF p.11) | "all of the land south of Golden Gate Park, north of Sloat Boulevard, and west of the Golden Gate Heights ridge line is synonymous with the Sunset District" |
| Parkside / Oceanside / Inner Sunset / Outer Sunset / Golden Gate Heights / Parkway Terrace / West Portal | `sunset-hcs` | p.5 (PDF p.5) | "Within this large area are several smaller neighborhoods including the Parkside, Oceanside, Inner Sunset, Outer Sunset, Golden Gate Heights, Parkway Terrace, and portions of West Portal" |
| Forest Hill / St. Francis Wood / West Portal | `parkside-statement-2008` | p.10 (PDF p.14) | "It remained undeveloped until 1912 when the land was sold to become the neighborhoods of Forest Hill, St. Francis Wood, and West Portal" |
| Rivera Heights | `sunset-hcs` | p.30 (PDF p.30) | "Chris McKeon's 1936 \"Rivera Heights\" tract centered on 29th Avenue at Rivera Street" |
| Balboa Terrace / Merced Manor / Lakeside / Parkmerced / Ingleside Terraces / St. Francis Wood | `sunset-hcs` | p.43 (PDF p.43) | "curvilinear streets (St. Francis Wood), uniform picket fences or specific tree species (Lakeside), alleys with fronting attached garages (Merced Manor and Balboa Terrace), purposeful landscape design (Parkmerced and Balboa Terrace), or street furniture such as gates, pillars, or other entry markers (Ingleside Terraces)" |
| Lakeside District | `sunset-hcs` | p.60 (PDF p.60) | "constructed a large-scale residential tract in what is now the Lakeside District at a reported rate of one house a day" |
| Laurel Heights | `sunset-hcs` | p.19 (PDF p.19) | "opened up large tracts of land for residential development and a few public parks, primarily in the Inner Richmond and Laurel Heights neighborhoods" |
| Forest Knolls / Country Club Acres | `sunset-hcs` | p.53 (PDF p.53) | "tracts in Forest Knolls, Country Club Acres, Forest Hill, Lake Merced and Mount Sutro" |
| Sherwood Forest | `sunset-hcs` | p.62 (PDF p.62) | "two local branch offices near Sherwood Forest (200 Casitas Avenue) and West Portal (850 Ulloa Street)" |
| Mission Terrace | `sunset-hcs` | p.52 (PDF p.52) | "working from their home at 164 Otsego Avenue in San Francisco's Mission Terrace neighborhood" |
| Pine Lake / Lake Merced | `sunset-hcs` | p.23 (PDF p.23) | "Several creeks blocked by the dunes formed ponds and tidal lagoons, the largest of which were located to the southwest (Lake Merced) and southeast (Pine Lake in Stern Grove)" |
| Sunnyside / Outer Mission / Richmond | `parkside-statement-2008` | p.23 (PDF p.27) | "the districts beyond the fire line that catered to these buyers and had reliable mass transportation, such as the Richmond, Sunnyside and Outer Mission, experienced a population boom" |
| Presidio Terrace | `parkside-statement-2008` | p.28 (PDF p.32) | "Borrowing some of the popular restrictions residence park communities such as Presidio Terrace and St. Francis Wood required" |
| Sunset District | `sunset-hcs` | p.19 (PDF p.19) | "Sunset District In the mid-1850s, much of the western half of what is now known as San Francisco was officially named the \"Outside Lands\"" |

## Names that only the modern-architecture statement carries

| name | document | printed page (PDF page) | phrase |
|---|---|---|---|
| Diamond Heights | `modern-architecture-context-2011` | p.3 (PDF p.7) | "Modern architects and landscape architects designed iconic skyscrapers, urban landscapes, and master-planned developments such as Diamond Heights" |
| Red Rock Hill | `modern-architecture-context-2011` | p.47 (PDF p.51) | "Parts of Diamond Heights earned critical acclaim, including B. Clyde Cohen and James K. Leverson's Red Rock Hill design… Red Rock Hill was the first development phase (1962)" |
| Gold Mine Hill | `modern-architecture-context-2011` | p.29 (PDF p.33) | "steeper areas such as Diamond Heights, Twin Peaks, Gold Mine Hill, and the upper slopes of Bernal Heights" |
| Midtown Terrace | `modern-architecture-context-2011` | p.30 (PDF p.34) | "One example is Midtown Terrace, jointly developed by Standard Building Company and the Panorama Development Company in 1956-57" |
| Anza Vista | `modern-architecture-context-2011` | p.31 (PDF p.35) | "(1948) Anza Vista None listed Streamline Moderne $11,500 Single-family and unusual Moderne duplexes" |
| Stonestown | `sunset-hcs` | p.31 (PDF p.31) | "builders Henry and Ellis Stoneson developed Stonestown, consisting of residential towers, townhouses, and a commercial development" |
| Visitacion Valley / Silver Terrace / Excelsior | `modern-architecture-context-2011` | p.17 (PDF p.21) | "neighborhoods to the south with high concentrations of construction during the Modern Age such as Visitacion Valley, the eastern slopes of Bernal Heights, Silver Terrace, and the Excelsior" |
| Parnassus Heights | `modern-architecture-context-2011` | p.67 (PDF p.71) | "as did the UCSF campus located at Parnassus Heights" |
| Clarendon Heights / Lakeside / Twin Peaks | `modern-architecture-context-2011` | p.122 (PDF p.126) | "Residential enclaves that feature significant concentrations of the style include Clarendon Heights, Diamond Heights, Midtown Terrace, Lakeside, Twin Peaks, and eastern Bernal Heights" |
| Dogpatch / Uptown Tenderloin | `corbett-heights-hcs-2017` | p.180 (PDF p.187) | "In San Francisco, the Uptown Tenderloin, Chinatown, and Dogpatch are three examples" |
| Islais Creek | `soma-context-2009` | p.33 (PDF p.35) | "then onward across Islais Creek to Hunters Point" |
| Mission Creek | `corbett-heights-hcs-2017` | p.12 (PDF p.19) | "drained into Mission Creek and flowed easterly more or less along the later alignments of Caselli and Eighteenth Streets to a lagoon near the edge of Mission Bay" |

---

## Dates the documents actually assert

The only dates recorded anywhere in this file. Each is quoted from the sentence
that asserts it — **none is inferred from a nearby number.**

| name | date asserted | document | printed page (PDF page) | the sentence |
|---|---|---|---|---|
| Rancho Potrero Nuevo | 1835 grant, confirmed 1841 | `mission-district-context` | p.18 (PDF p.21) | "The de Haro twins… received confirmation of an earlier grant (1835) of Rancho Potrero Nuevo (approximately 1,000 acres) in 1841" |
| Laguna de la Merced Rancho | 1835 | `parkside-statement-2008` | p.9 (PDF p.13) | "It was granted to Jose Antonio Galindo in 1835 but he sold it two years later to Don Francisco de Haro" |
| Rancho San Miguel | 1845 | `mission-district-context` | p.18 (PDF p.21) | "Jose Noe… obtained the Rancho San Miguel grant (4,443 acres), bounded on the northeast by the Old Mission Road, in 1845" |
| South Park | 1852 (purchase), 1854 (plan) | `central-soma-deir-cultural` / `corbett-heights-hcs-2017` | IV.C-6 (PDF p.6) / p.34 (PDF p.41) | "Englishman George Gordon in 1852 began purchasing lots" · "the elongated circular plan of South Park in 1854" |
| Mission Addition | "by the mid-1850s" | `mission-district-context` | p.23 (PDF p.26) | "an area that became known as the Mission Addition or the Mission Dolores Addition by the mid-1850s" |
| Outside Lands | 1856 | `market-octavia-context-2007` | p.32 (PDF p.32) | "territories that were subject to the Third Consolidation Act of 1856, known as the Outside Lands of San Francisco" |
| Eureka Homestead Association | 1864 | `corbett-heights-hcs-2017` | p.7 (PDF p.14) | "This stream crossed the area of the 1864 Eureka Homestead Association within the area bound by Seventeenth and Twentieth, Noe and Douglass Streets" |
| William R. McKee Subdivision | 1864 | `corbett-heights-hcs-2017` | p.31 (PDF p.38) | section heading "William R. McKee Subdivision, 1864" on the body page |
| Pioche & Robinson Subdivision | 1867 | `corbett-heights-hcs-2017` | p.33 (PDF p.40) | "the primary subdivisions of Corbett Heights is that of Pioche & Robinson of 1867, consisting of over two-thirds of the land area of the neighborhood" |
| Market Street Homestead Association | 1868 | `corbett-heights-hcs-2017` | p.37 (PDF p.44) | section heading "Market Street Homestead Association, 1868", followed by "Two months after the first auction of properties in the Pioche & Robinson Subdivision, a new overlapping entity was established called the Market Street Homestead Association" |
| Park Lane Tract | 1885–1891 | `corbett-heights-hcs-2017` | p.40 (PDF p.47) | "Between 1885 and 1891, he subdivided the tract in sections and sold lots" |
| Ashbury Park | 1911 / 1913 | `corbett-heights-hcs-2017` | p.131 (PDF p.138) | "The first residents were there by the end of 1911, but it was not actively marketed until mid 1913" |
| Forest Hill · St. Francis Wood · West Portal | 1912 | `parkside-statement-2008` | p.10 (PDF p.14) | "It remained undeveloped until 1912 when the land was sold to become the neighborhoods of Forest Hill, St. Francis Wood, and West Portal" |
| Rivera Heights | 1936 | `sunset-hcs` | p.30 (PDF p.30) | "Chris McKeon's 1936 \"Rivera Heights\" tract centered on 29th Avenue at Rivera Street" |
| Midtown Terrace | 1956–57 | `modern-architecture-context-2011` | p.30 (PDF p.34) | "jointly developed by Standard Building Company and the Panorama Development Company in 1956-57" |
| Red Rock Hill | 1962 | `modern-architecture-context-2011` | p.47 (PDF p.51) | "Red Rock Hill was the first development phase (1962)" |

Sixteen dated names, against **136 inventory rows** in the tables above (a few
rows carry several names from one sentence; a few names appear twice because two
documents carry them). That ratio is the finding.
The earlier bulk extraction dated 47 of 131 by taking the nearest four-digit
year and produced a man's birth year as a plat date; reading the sentence
instead yields a third as many dates and every one of them survivable.

---

## What was thrown away, and why

Roughly **1,000 of the 1,163 raw candidate strings** never reached `quote.py`,
and about **30 of the 159 verified candidates** were dropped after reading the
passage. The categories, each with a real example:

**Not a place — a person.** `Henry Hill` scored 14 discovery hits and is an
architect: "Henry Hill and Ernest Kump, Second Bay Tradition Modern architects,
studied under Gropius at Harvard" (`modern-architecture-context-2011`, printed
p.79, PDF p.83). Likewise `Albert Henry Hill`, `Williams Henry Hill`,
`McGraw Hill`, `Donald Beach`, `James Beach`, `L. Dale`.

**Not a place — a building type.** `Romeo Flats` scored 112 seed hits across
four documents and is a form of apartment building: "A few had the look on the
map of what were later called Romeo Flats — six-flat buildings with two tiers of
three flats" (`north-beach-hcs`, printed p.18, PDF p.24). `Standard Flats`,
`Alley Flats`, `Cuneo Flats`, `Morosin Flats` and `Type V. Alley Flats` are the
same North Beach typology chapter.

**Not a place — an architectural period.** `First Bay`, `Second Bay` (105 hits)
and `Third Bay` are the Bay Tradition style sequence.

**Not in San Francisco.** `Berkeley Property Tract` is the most tempting: it
reads exactly like a Corbett Heights plat and appears in that document, but it
is in Berkeley — "he prepared a plan for property adjacent to the College site
for a small residential subdivision called the Berkeley Property Tract"
(printed p.30, PDF p.37). Also discarded: `Napa Valley`, `Sacramento Valley`,
`Santa Clara Valley`, `Mill Valley`, `Scotts Valley`, `Yosemite Valley`,
`Monterey Bay`, `Morro Bay`, `Stinson Beach`, `Pebble Beach`, `Long Beach`,
`Bloomfield Hills`, `Beverly Hills`, `Los Altos Hills`, `Menlo Park`,
`Rohnert Park`, `Walnut Creek`, `Llewellyn Park`, `Central Park`.

**A modern administrative or regulatory designation, not a historical name.**
`South End Historic District`, `Townsend Warehouse Historic District`,
`Sixth Street Lodginghouse Historic District`, `SoMa Light Industrial Historic
District`, `Transit Center District`, `Second Street Conservation District`,
`Filipino Cultural Heritage District`, `Japantown Cultural District`,
`Underground Utility District`, `Zoning District`, `Caltrans District`.

**A park, square, plaza or institution rather than a district.**
`Golden Gate Park`, `McLaren Park`, `Duboce Park`, `Dolores Park`, `Larsen
Park`, `Pinelake Park`, `Alamo Square`, `Hamilton Square`, `Columbia Square`,
`Union Square`, `Portsmouth Square`, `Washington Square`, `Jackson Square`,
`St. Francis Square`, `Ghirardelli Square`, `Maritime Plaza`, `Fox Plaza`,
`Mint Plaza`, `United Nations Plaza`, `Valencia Gardens`, `Woodward's Gardens`,
`Sigmund Stern Grove`. South Park is the exception and is kept, because the
documents treat it as a residential enclave and a neighbourhood, not a garden.

**A street.** `Uranus Terrace`, `Loma Vista Terrace`, `Clifford Terrace`,
`Lower Terrace`, `Cottage Row`, `Columbus Avenue`, `Aladdin Terrace`,
`Calhoun Terrace`, `Montclair Terrace`, `Normandie Terrace`.

**A false positive the extraction manufactured.** `Old City` in
`market-octavia-context-2007` printed p.9 is "old City Hall" with a line break
in the wrong place. `Sunset Tract` in `sunset-hcs` printed p.38 is "most Sunset
tract houses" — a house form, not a tract name. `Flats Flats Flats Flats
Flats`, `Type VI. Flats`, `BUI LT ENVIRONMENT Corbett Heights`, `Interior.
National Park`, `DC. National Park`, `Melanie Simo. Invisible Gardens` and
`Mel. The San Francisco Bay` are table-of-contents leader dots and bibliography
runs read as prose.

**A grammatical accident of the pattern.** `In North Beach`, `Among North
Beach`, `For North Beach`, `Although Corbett Heights`, `Within Corbett Heights`,
`Compare Corbett Heights`, `Wants Flats`, `Eliminate Romeo Flats`,
`Known Tract`. The discovery regex allowed up to four leading capitalised
words; sentence-initial capitals slip in.

**Nineteen of the 130 seeded names appear nowhere in the corpus at all**,
including `Washerwoman's Lagoon`, `Loma Alta`, `Westwood Park`, `Monterey
Heights`, `Pipesville`, `Mooneysville` and `Precita Valley`. That is a fact
about these documents, not about San Francisco.

---

## What this is not

**It is a concordance of eleven documents, not a gazetteer.** Every name here
is a name written down in one of eleven San Francisco Planning-adjacent
documents fetched on 27 August 2026. **Absence from this table is not absence
from the record.** `Washerwoman's Lagoon` is a real place name; it is missing
here because none of these eleven papers happens to mention it. The corpus was
assembled to answer other questions — SoMa, Corbett Heights, Japantown, the
Sunset — and its silences are the shape of that assembly, not the shape of the
city.

**The coverage is lopsided by construction.** Corbett Heights has a 261-page
statement and contributes 24 names; the Richmond has no statement in this corpus
at all, which `richmond-seacliff.md` establishes separately. A name's absence
correlates with which neighbourhoods commissioned a context statement, which is
a fact about municipal preservation budgets.

**It does not adjudicate extent.** Several names here are given incompatible
bounds by different documents — that is expected and is being handled elsewhere.
Nothing in this file resolves a boundary, ranks two claims, or prefers one
document's account over another's. Where a document disputes a name, the dispute
is quoted, not settled.

**It does not date what the sentence does not date.** Sixteen names carry a
date. The other 120 rows do not, and their appearance beside dated ones must not
be read as dating them. This is the trap the earlier bulk extraction fell into.

**Some names are contemporary usage, not historical.** `Multimedia Gulch`,
`Uptown Tenderloin`, `Dogpatch`, `Mission Terrace` and the Diamond Heights
sub-hills are twentieth- or twenty-first-century coinages the documents record.
They are kept because they are named districts and hills, not because they are
old.

**One document's printed pages are unavailable.** `japantown-hcs-2008` has no
established printed-to-PDF offset, so every Japantown row cites a PDF page and
says so. `parkside-statement-2008` PDF p.1 and `corbett-heights-hcs-2017` PDF
pp.1–7 and 260–261 are similarly refused. Not one printed page in this file was
invented.

**The extraction is not the page.** `quote.py` tolerates broken words, but
pypdf reads two-column layouts and tables in the PDF's own order. A quoted
phrase that reads as slightly disjointed prose — the `Anza Vista` row is one —
is a table row, and the context around it is not adjacent on the printed page.

**Marker discipline.** Every row is `FETCHED` — retrieved, read, and cited from
`quote.py`'s output. There is nothing `SEARCH-SUMMARY` and nothing `RECALLED` in
this file. Seed names were chosen from recall; **recall selected the queries,
and the documents supplied every answer.** The 19 seeds that found nothing are
reported as finding nothing.

## Reproducing this

```
cd research/2026-08-21-sf-downtown-place-names/02-run-plan
uv run --no-project python quote.py --list
uv run --no-project python quote.py "Eureka Homestead Association" --id corbett-heights-hcs-2017
```

The extractions are gitignored and are not in this repository. Re-fetch them
with `acquire-documents.py` on a host with open egress; the manifest carries the
sha256 of every document as fetched.
