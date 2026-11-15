# Research dossier and repository architecture audit — 2026-11-15

Scope: all 24 files under `research/`, the four formal candidate records, root README and methodology. This audit records information architecture, status/evidence consistency and handoff risks; it does not claim independent re-verification of every external source.

## 1. Repository architecture and data flow

The repository is document-first, with no application source, package manifest, build configuration, test suite or CI workflow in the root inventory. Its effective architecture is:

1. `README.md` — project charter, editorial taxonomy, archive routes, required candidate fields, contribution protocol and a snapshot of current leads.
2. `METHODOLOGY.md` — normative eligibility/evidence rules. Adopted 2026-11-15; should override older screening notes where they conflict.
3. `candidates/` — four relatively formal item dossiers with stable IDs.
4. `research/` — 24 mixed-purpose documents: regional discovery screens, item-specific leads, multi-item research clusters, global map, re-audit crosswalk and the formal-candidate audit.
5. `coop.log.md` — append-only multi-agent research and decision ledger.
6. `research_method.md` — autonomous execution state and module audit handoff.

Logical research flow: local narrative/genre discovery → printed/oral/contextual witnesses → discography/catalogue/session evidence → exact recording/master linkage → performed-text/audio inspection → separate transfer and rights assessment → A/B/C evidence classification → editorial consideration. The files document these stages unevenly; they are not a normalized database.

## 2. Global map, crosswalk and first-pass control documents

### `research/global-early-recording-map.md`
- Living global discovery map; sections for search principles, gateways and regional routes, initial discovery evidence and dated additions across Egypt, Mexico, Japan, Bengal and Anlo-Ewe.
- Correctly states it is a discovery map, not a list of eligible recordings. Strong emphasis on regional archive routes and not conflating a broad tradition with a specific master.
- It accumulates dated additions and sometimes repeats the same item in several sections. This preserves provenance but makes a canonical per-item status difficult to find. The README should direct readers to the detailed dossier, not treat the map as a registry.
- Japan/Naramaru and Anlo-Ewe/Nathaniels appear in several cross-linked documents; keep one detailed source-of-truth dossier per item and make map entries concise pointers.
- No A-level status should be inferred from map inclusion.

### `research/re-audit-existing-leads-2026-11-15.md`
- Most useful current crosswalk: explicitly says no A-level candidates; 8 provisional B and 18 C, plus one Greek outside-core false positive. It states this is not a full re-examination and rights clearance is not inferred.
- It contains a broad reclassification table covering Gene Greene, Armenian Victor, Handel, Wagner, Saint-Saëns, Verdi, Naramaru, Takamine, Kumoemon, Papus, Mexican corridos, Kolkata, Nathaniels, Solanke, Boyajian, Helen Paul, Armenian Tashjian leads, Plaatje, Caruso, Egypt and other leads.
- The table is a provisional status register, not a formal candidate inventory. Keep its B/C values as the current crosswalk unless a later evidence pass changes them.
- **Markdown defect:** a free-standing “Catalogue caution added 2026-11-15” paragraph appears inside the Markdown table after the Heraclio Bernal row and before Macario Romero. It interrupts the table and can cause subsequent rows to render as prose. Move that paragraph below the table under its own heading on a formatting-only maintenance commit.
- Caruso is already explicitly labelled C — thematically outside on current evidence. This agrees with the formal-candidate audit's substantive finding; do not present it as an active revenge candidate.

### `research/first-pass-screening.md`
- Historical first-pass record. Its original rejection of Gene Greene is based on the now-superseded author-death cutoff; a dated follow-up correctly maps the item to B under the revised methodology and adds a performed-text witness.
- Keep the historical rejection as audit trail. Current status comes from the re-audit, not the old opening paragraph.
- The original “5–8 track batch” language is a prior production target and should not override current evidence quality.

## 3. Regional and item dossier inventory

### Africa
- `research/african-early-recording-leads-1923-1925.md`: Plaatje (1923), Nathaniels (1925), Solanke (1925); separates three performers and recording sides, distinguishes contextual tradition from the actual audio/text, and has substantial archive/rights handoffs. Plaatje is explicitly contextual/not thematically admitted; Nathaniels remains C; Solanke's tonal ambiguity is unresolved.
- *haló* is context only, not a matched recording. The 1925 Nathaniels “Ewe Battle Hymn” is not proven to be a haló performance.

### Middle East / Arabic / Egypt / Ottoman
- `research/arabic-early-recording-screening-2026-11-15.md`: no candidate admitted; AMAR/Harvard discovery routes and controls only.
- `research/egypt-dinshaway-mawwal-1906.md`: Dinshaway oral/printed mawwāl and “Mawwal Zahran” textual leads; no eligible recording. 1908 topical disc is a control, not a match.
- `research/global-search-note-arabic-corridos-2026-11-14.md`: reconnaissance across Harvard Arabic 78s and Frontera/Mexican corridos; records later-dated false positives and catalogue routes.
- `research/ottoman-eastern-mediterranean-diaspora-2026-11-14.md`: matrix chronology and diaspora collection routes; no admitted recording.
- `research/eastern-mediterranean-greek-armenian-title-search-2026-11-14.md`: discography route and Armenian diaspora screening; no admitted recording. These documents should remain regional search logs, not duplicate candidate records.

### East Asia / Japan / Korea / Bengal
- `research/east-asian-early-recording-screening-2026-11-15.md` (67,891 characters): large multi-stage dossier on Korean Fletcher cylinders, Cantonese/Chinese infrastructure, Japanese Chūshingura/Rōkyoku records, Kumoemon, Naramaru, Takamine, Royal 1651 and Bengal *Bande Mataram*. It contains valuable item-level distinctions but is the largest and most duplication-prone research file. Its internal sections are dated and detailed; future work should add a table of contents and canonical links rather than duplicate long blocks.
- `research/japan-ako-gishi-yoshida-naramaru-royal-record.md`: detailed Naramaru item dossier; correctly distinguishes Toiri, Denchū Ninjō, Royal 1651, Royal 1723, Taihei later-generation issues and other recordings. Royal 1651 remains B only conditionally on physical label confirmation; exact date/audio still open.
- `research/india-vande-mataram-recordings-1905-1908.md`: distinct H. Bose cylinder, Pathé–H. Bose disc, National Grand spoken-word disc and Binapani advertisement. C — LEAD cluster; public singing/anti-partition defiance is conditional, and the lyric itself is mainly invocation/praise.
- `research/south-asia-early-recording-research-2026-11-14.md`: regional infrastructure/negative-result note; no item-level candidate.
- Korea Fletcher cylinders and 1920s+ items are treated as controls or outside core where appropriate; do not infer a 1896 grievance song from the mere existence of Korean recordings.

### Latin America
- `research/latin-american-corridos-screening-2026-11-15.md`: Mexico City Edison 1904 campaign; Ignacio Parra, Heraclio Bernal and Macario Romero remain C leads; Pancho Villa 1924 title is rejected for taxonomy. It carefully separates printed corrido witnesses from cylinder text and preserves the 18638/18634 catalogue discrepancy.
- `research/global-search-note-arabic-corridos-2026-11-14.md` also contains Frontera controls and later dated rejections. Avoid duplicating the full corrido history in the global map.

### Armenian / diaspora
- `research/lead-dalvorig-mihran-damadian-tashjian-columbia-1909-1910.md`: strong thematic textual lead with 1924 and 1962 printed witnesses and 1909/1910 recording branches; exact lyric-to-recording identity remains unresolved.
- `research/lead-mardiros-tashjian-columbia-1909.md`: two 1909 titles; one appears patriotic/commemorative, another protest-oriented, but translation and taxonomy are provisional.
- `research/lead-tashjian-1910-dalvorig-grvetsek-dgherk.md`: separate 1910 Tashjian Brothers titles; contextual patriotic repertoire only until lyrics are checked.
- `research/lead-dalvorig...` and `research/lead-tashjian-1910...` overlap on “Dalvorig.” They must not be merged without title/lyric/matrix identity evidence; add cross-links and a variant/recording-branch table.
- `research/lead-vahan-boyajian-derzor-dastaanaci-bilbil-2.md`: date unresolved near cutoff; lament/memory lead, thematic response not established.
- `research/lead-helen-paul-tzain-ma-hunchetz-columbia-e4661-1918.md`: strong collective-resistance/protest lead, but matrix/date, composition provenance, exact text and audio remain open.
- `research/eastern-mediterranean-greek-armenian-title-search-2026-11-14.md` and `research/ottoman-eastern-mediterranean-diaspora-2026-11-14.md` provide regional context and should link to these item files.

### European / theatrical / opera leads
- `research/candidate-papus-rache-bar-kochba.md`: extensive Yiddish theatre/Goldfaden score and Homocord 1118 discographic research; remains C because exact carrier, matrix/date code, audio and performed-version link are missing. Distinguishes Papus Rache from other Homokord/Beka titles.
- `research/lead-handel-alexanders-feast-revenge-timotheus.md`: strong explicit text but performer/matrix take disputed; HMV D589 and Vocalion X-9560 are distinct recording paths; C/LEAD in the dossier while re-audit lists B for the reported early issues. This discrepancy must be resolved in the canonical crosswalk: B is defensible only if the exact issue/session identity is sufficiently linked; keep each recording branch separate.
- `research/lead-wagner-hagen-meditates-revenge-1922.md`: strong discography/title lead; exact audio and rights open; C/LEAD in dossier while re-audit assigns B. Add explicit provisional B mapping or downgrade the re-audit after checking matrix and session source.
- `research/greek-early-recording-screening-2026-11-15.md`: *Fonias tha gino* is correctly rejected as post-cutoff (1927/1929) and current text is not revenge; retain as negative control, not candidate.
- Saint-Saëns and Verdi are formal candidate files, not separate research files; see formal-candidate audit.

### South Asia / Kolkata theatre
- `research/lead-kolkata-khune-nahak-corinthian-1902.md`: C/lead only. The play *Khun-e-Nahaq* and revenge plot do not prove the 1902 chorus side is from that scene or even that it is revenge content. Correctly warns against assigning play plot to song from title alone.

## 4. Cross-module integrity issues and risks

1. **Status drift:** formal candidate files use “PARTIALLY VERIFIED”; research dossiers use “LEAD,” “STRONG LEAD,” “PARTIALLY VERIFIED,” while the re-audit uses A/B/C. The README snapshot uses older terms such as “HIGH-PRIORITY LEAD” and “LEAD ONLY.” One canonical status crosswalk is needed.
2. **B-level drift:** Handel and Wagner are marked LEAD in their dossiers but B in the re-audit. Add a transparent rationale or reconcile.
3. **Caruso scope:** the formal record retains it as a candidate while the re-audit says C — thematically outside. The new methodology supports the latter unless exact in-aria text proves a response mechanism.
4. **Candidate-vs-lead ambiguity:** the README table mixes formal candidate files, research dossiers and textual clusters. Add a “record type” column and canonical file link for each row.
5. **Duplicate research branches:** Japanese Chūshingura/Naramaru content spans the East Asian screen, Japan dossier, global map and re-audit; Armenian Dalvorig spans at least two separate recording branches. These are not necessarily duplicate facts, but they need cross-links and explicit branch identities.
6. **No normalized rights register:** rights are described individually and correctly marked unresolved, but there is no central rights matrix by recording, master, composition, transfer, territory and intended use.
7. **No archive-contact ledger:** archive request targets are described in handoffs, but no shared request status, contact date, response or authorization register exists.
8. **No release-ready A-level candidates:** re-audit explicitly assigns none. The current repo is still a research discovery set, not a verified track batch.
9. **No source-code/test architecture:** repository is currently entirely documentary research. There are no code modules or tests to execute; validation must be editorial/data-integrity validation.

## 5. Recommended maintenance architecture (non-destructive)

- Keep each detailed candidate/lead dossier as source of truth.
- Keep the global map as short regional discovery pointers and archive routes, not a duplicate dossier.
- Keep the re-audit as a dated status crosswalk, with links to canonical files.
- Add a compact root or `research/` index later: item ID/title, canonical dossier, evidence level, date assessment, theme, audio status, rights status, next action.
- Create separate append-only `research/archive-requests.md` and `research/rights-register.md` only when actual contact/rights work begins; do not populate imagined contacts or clearances.
- Add a table of contents to the East Asian mega-dossier and cross-links for duplicate/related Armenian titles.
- Use a stable lead identifier only when a specific recording object exists; keep multi-item oral/text traditions as research clusters.

## 6. Immediate next work

1. Fix the broken Markdown table boundary in `research/re-audit-existing-leads-2026-11-15.md`.
2. Reconcile B vs C for Handel and Wagner, and update README's current snapshot with canonical links/status vocabulary after the full audit.
3. Add explicit cross-links between the Dalvorig dossier branches and the Japan/Naramaru source files.
4. Continue high-value evidence work on exact performed text/audio for the best B candidates; do not spend rights effort before thematic and recording identity are firm.
5. Inspect companion `sloev/grudgebook` repository for conceptual framework and editorial voice as README instructs, if repository access is available.

## Audit limitation

All file content was inspected through repository text. No embedded audio was played, no physical records inspected, no archive staff contacted, and no external source independently re-opened in this audit.
