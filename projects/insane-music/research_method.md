# Persistent research state

## Highest-priority standing direction — global non-Anglo research and the small web

The genuinely global, non-Anglo perspective is the **highest research priority**, above the inherited archive queue and above convenience. Deliberately rotate Africa, Asia, Latin America/Caribbean, the Pacific, the Middle East, and eastern/southeastern Europe. Begin with local languages, scripts, regional archives, community collections, personal sites, local historians, independent labels and oral histories. Do not allow North American or western European cases to dominate because they are easier to search. English-language visibility is not a measure of significance. Preserve original titles, scripts, names and context.

The small/smol web is a primary discovery territory. Search old private homepages/domains, GeoCities/Angelfire-era survivors and mirrors, Blogspot, WordPress, LiveJournal, Tumblr, forums, zines, webrings, blogrolls, guestbooks, link directories, cassette blogs, micro-labels and regional collector sites. Use Wiby, Marginalia, Weirdnet, Old'aVista, Neocities/Nekoweb directories and web archives/Wayback snapshots; follow link trails outward. Treat abandoned or archived pages as potential first-hand evidence, then verify independently. Record the region, language and small-web route used in each discovery pass.


**Repository:** `sloev/insanemusic` (default branch: `main`)
**Project reality check:** This repository is an editorial research compendium, not (on current inspection) a conventional software codebase. Its principal artefacts are Markdown methodology, candidate/environment leads, and a collaboration/research log. Do not invent modules, runtime architecture, or code paths. If executable code, data schemas, workflows, or site-generation logic are discovered in the tree, inspect them file-by-file and document exact paths and control/data flows.

## Operating method
1. At the beginning of every run, read this file first, then `method.md`, `environment-leads.md`, and `coop.log.md`; inspect the current repository tree and latest commits before editing.
2. Preserve the project's editorial standard: environment-first discovery; extant recording required for main entries; distinguish resident-made recordings from visiting performances, broadcast/playback, later reconstruction, and merely found media; assess obscurity separately from provenance; no sensationalism or diagnosis-by-sound.
3. Research internationally and in local languages. Search independent music blogs, cassette blogs, zines, personal sites, small-web directories, micro-labels, radio archives, national libraries, finding aids, local newspapers, oral histories and primary catalogues. Treat blogs as discovery leads, not proof. Verify against original/archival sources.
4. For every lead, capture exact item identity, date(s), medium, performers/roles, recording location, institution/community relationship, archive/shelfmark, provenance chain, circulation/reissue, evidence status, obscurity rating, ethical/rights constraints, source URLs, uncertainties and next actions.
5. Keep negative findings and false positives, but state their scope precisely. Never claim to have listened, contacted, accessed restricted material, or obtained permission unless actually done.
6. Before each milestone, update this file with phase, work completed, findings, blockers and next exact task. Update `environment-leads.md` and `coop.log.md` after substantive evidence-based work. Fetch the current blob SHA immediately before each write; never write the same path concurrently; verify resulting commits.
7. This is a research compendium, not a software engineering task unless the tree proves otherwise. The user's request for module-by-module technical inspection is interpreted as a file-by-file audit of the actual repository artefacts. If code is present, additionally document imports, entry points, data flow, state, dependencies, side effects, and tests.

## Current phase (2026-11-15)
**Phase 0 — Repository reconnaissance and research-state bootstrap.**
- Checked for this file first: it did not exist.
- Confirmed `README.md` is absent at repository root.
- Confirmed `method.md`, `environment-leads.md`, and `coop.log.md` exist.
- Existing research compendium already contains 35 numbered leads and extensive editorial/methodological notes (see the files themselves; do not duplicate them).
- Immediate next tasks:
  1. Create this persistent state file.
  2. Inspect the repository's complete root/tree and all tracked files; classify each as methodology, candidate data, log, code, media, or ancillary.
  3. Audit cross-file structure and references (lead numbering, source URLs, status vocabulary, duplicated/contradictory entries, stale next steps).
  4. Identify the highest-value unresolved archive/blog trails and continue evidence-based research.
  5. Record any substantive results in the canonical lead/log files and verify commits.

## Continuation checkpoint
Last known research state from previous runs is summarised in conversation context: lead #35 is Harry Urata / holehole bushi; current priority trails include Soledad CTF / Jack Bowers and Waupun prison newspapers; other recent screens include Tule Lake and psychiatric-hospital archives. Verify all current file contents and commits rather than trusting this summary as the live repository state.


## Milestone 1 — repository artefact and structure audit (2026-11-15)
**Current phase:** editorial/data-structure audit completed at a first pass; move to source-level follow-up and controlled cleanup.

### Confirmed file inventory
The GitHub connector exposes these tracked root artefacts:
- `method.md` — 226 lines, about 23.6 KB, 25 Markdown headings. Defines mission, inclusion pathways, recording threshold, environment-first search, obscurity ratings, evidence vocabulary, metadata, ethics, rights, collaboration, contextual register and small-web discovery.
- `environment-leads.md` — 509 lines, about 133.3 KB, 57 headings, 204 URL occurrences. Main working register; contains the first nine priority leads, a calibration/exclusion area, older preliminary lead notes, detailed archive audits and later unnumbered updates.
- `coop.log.md` — 629 lines, about 105.0 KB, 96 headings, 171 URL occurrences. Chronological session log with 24 dated top-level entries (all dated 2026-11-15 in the current file).
- `research_method.md` — this newly created persistent checkpoint.
- Root `README.md` is absent. Repository search for `package.json`, HTML entry points and common source-code signatures found no evidence of a software application. Search results for code-like words only matched prose in the Markdown files. This is not proof of every possible file in the Git tree; continue checking tree/file discovery if a supported listing endpoint becomes available.

### Architecture / data flow as actually represented
There is no observed executable runtime, build system, package/dependency manifest, test suite, or application entry point. The current repository is a human-maintained Markdown knowledge base:
- `method.md` is the normative editorial schema and research protocol.
- `environment-leads.md` is the semi-structured candidate/source register; it contains both candidate records and contextual/source-audit notes.
- `coop.log.md` is the append-only narrative provenance of research sessions and decisions.
- `research_method.md` is the run-state/checkpoint file and should point back to the canonical files rather than duplicate their contents.

### Structural findings / cleanup risks
1. `environment-leads.md` has duplicated numbered headings: numbers 14 and 15 each occur twice. The first 14/15 are preliminary entries for Prussian POW recordings and David Boder; the later detailed sections are Indiana State Prison (#14), Prussian Phonographic Commission (#15), and Hénonville (#16). The early entries appear to be superseded/duplicated summaries, but do not delete or renumber them without comparing full text and preserving all unique evidence.
2. The register's numbered headings continue through #31, while later substantial items (Soledad CTF, CELL(R), Harry Urata) are unnumbered. Several numbered sections are follow-up/correction/context notes rather than independent recording candidates (e.g. Uzuakoli, Culion, Liberation). Therefore heading numbers are not a reliable count of distinct candidates; do not equate the current count with 35 independent recordings.
3. The first nine leads sit under `## Priority leads`; subsequent records and audit notes use a mixture of `##` and `###`, and later updates are appended without a consistent heading depth. This is readable Markdown but weak as a machine-maintainable catalogue.
4. `method.md` places section 3C (small-web discovery) after section 11 (contextual register). The content is coherent, but the numeric order is not sequential.
5. The log is chronological but contains old action items that have since been superseded by later scope decisions and completed research. Treat later dated decisions as authoritative; do not erase historical context.
6. Repeated URLs are often legitimate source reuse across related notes. A simple duplicate-URL count is not a defect signal; inspect context before deduplication.
7. Status vocabulary appears in both candidate and evidence dimensions (e.g. VERIFIED vs PROMISING/HIGH PRIORITY). Preserve the distinction: evidence status is not the same as editorial priority.

### Exact current blob SHAs at audit
- `research_method.md`: `1fdfb6086bc3609228f4022674f2dbbaba17e458` before this milestone update.
- `method.md`: `67bd38531d9e6a5741a1bd6d2a8dd89a718fe502`.
- `environment-leads.md`: `32e4130638abaa97ab20c264381b3e2f033ca22f`.
- `coop.log.md`: `2614ca23bd07260e05ee55b63cfb94da1d7b32df`.

### Next work, in order
1. Build a safe candidate index that distinguishes true recording candidates from context-only archive audits, follow-up notes and discovery conduits; avoid renumbering until a cross-reference map is complete.
2. Inspect the two duplicated early Prussian/David Boder summaries against the later expanded sections and decide whether to mark them as historical preliminary notes or merge them without loss.
3. Audit candidate records for required fields (recording existence, provenance category, date, medium, maker/performer, archive/source, rights/consent, obscurity and next step). Report missing fields, do not fill them by guess.
4. Resume source research with the highest-value open trails: Soledad CTF (LOC digital files, cassette-liner photos, Jack Bowers interview); Waupun prison newspaper issues; then a fresh independent blog/smolweb sweep in underrepresented regions/languages.
5. Only after the audit is stable, consider a durable structured index/table in a separate file; do not convert the current prose register wholesale without owner approval.


### Milestone 1 completion / continuation point
- Repository audit was also appended to `coop.log.md`; commit: `84e200ab03972c4fbeb24c44e3bc4ba22ec70b63`.
- Persistent checkpoint audit commit: `c68c7b45d13569307ca2cd21534ccf1e4dac01d0`.
- No changes were made to `environment-leads.md`; structural issues are recorded for deliberate treatment.
- **Next active task:** construct a cross-reference map of numbered headings, true recording candidates, contextual archive audits, duplicate/follow-up notes, and unnumbered late additions. Compare the preliminary Prussian/David Boder notes to their later expanded records. Do not change lead numbering until the mapping is complete.
- **Then:** run a metadata completeness audit (recording existence, maker/performer, location, date, medium, provenance category, archive identifier, rights/consent, visibility rating, evidence status, source and next action). Log gaps as gaps, not inferred facts.


## Milestone 2 — lead-heading cross-reference (2026-11-15)
**Current phase:** candidate/notes taxonomy mapped; next perform field-level metadata completeness audit.

### Canonical candidate / archive-route headings
- **1–9:** ARSCH; Holy Church of Yahweh (music content still needs item-level verification); Grand Valley Institution for Women; Parchman; Kalaupapa; Partheni; Drapchi (context-only visibility); Clifton Hill (context/secondary route); Carville.
- **10–13:** Svenskt visarkiv prison-song reels; Anders Enevig field recordings; Margaret Valiant FSA migrant-camp recordings; Benjamin J. Harbert prison-music collection.
- **14:** Indiana State Prison / Bruce Jackson source tapes (detailed entry at line 187).
- **15:** Prussian Phonographic Commission wax-cylinder music corpus (detailed entry at line 196).
- **16:** Hénonville DP-centre / David Boder wire recordings (detailed entry at line 206).
- **17:** Texas prison farms / Huntsville recordings.
- **19:** Ericson Acosta / *Prison Sessions* (campaign/public-circulation context; distinguish visiting collaborator).
- **21:** Ohio Penitentiary 511 Jazz Ensemble / *Hard Luck Soul* (reissued; context-only for obscurity).
- **22:** Uzuakoli / Choir of the Leprosy Colony and Harcourt Whyte recordings (original vinyl still unresolved).
- **29:** *Liberation* Massachusetts prison recording (facility attribution is disputed/corrected later).
- **Unnumbered substantial recording/archive leads:** RISK (Kentucky State Penitentiary); Upheaval (Waupun; surviving single/video); Soledad CTF / Jack Bowers corpus; CELL(R) / *Every Day*; Harry Urata / *holehole bushi* field recordings.
- **Conditional / verify music content:** Holy Church of Yahweh; Svenskt visarkiv individual reel/song mapping; Uzuakoli original choir vinyl; Soledad CTF performers and tape-to-programme links; RISK original prison-cassette vs reunion rerecordings.

### Contextual records, follow-ups, conduits and exclusions — not separate candidates
- Preliminary heading at line 166 (“14. Prussian Phonographic Commission / Berlin Phonogramm-Archiv”) is a short early summary duplicated by the expanded detailed #15 at line 196.
- Preliminary heading at line 176 (“15. David Boder”) is a broad early summary expanded into Hénonville #16 at line 206. These two early headings cause the duplicate 14/15 numbering. They should be preserved as historical notes until a safe merge is made.
- #18 Anders Enevig's wider archive expands #11; it is a related collection-level route, not a separate artist/candidate.
- #20 independent blogs/small-web is a discovery-source register, not a recording.
- #23, #25 and #27 are Uzuakoli / Harcourt Whyte discographic clarification and track-level follow-ups to #22.
- #24 is a historical Culion band with no identified surviving audio; #26, #28 and #30 add photo, silent-film and radio-infrastructure context, not audio evidence.
- #31 is a correction/contact-route note for #29 *Liberation*.
- Massachusetts prison arts-programme/Northeastern archive sections contextualise #29 and the uncertain facility; they are not additional audio candidates.
- Smithsonian Anacostia sections are collection audits with no track-level provenance; Buffalo State Hospital *The Language of Schizophrenia* is screened out as spoken interviews, not music.
- Waupun institutional history, prison newspapers and historic band photographs are context/archive routes; do not count as surviving recordings. The Waupun newspaper trail may yet identify specific music items.
- Soledad/Waupun research-update sections summarise existing trails; Harry Urata follow-up is item-level refinement of the same collection.

### Consequence for future maintenance
The current numbering is a mixture of candidate IDs, source-register sections and follow-up notes. It is not a stable unique key. Avoid citing “lead #N” alone in future work; use a descriptive title plus location/date/archive ID. Before any renumbering, create a stable index with separate identifiers for (a) recording/release, (b) archive collection, and (c) contextual environment. No automatic deduplication based only on matching URLs or names.

### Next exact task
Audit the canonical candidate/archive-route records against the metadata schema in `method.md` §7 and the ethical/rights requirements in §§8–9. Build a gap list by descriptive title; do not fill missing dates, performers, shelfmarks, listening notes or permissions by inference.


### Milestone 2 completion / continuation point
- Candidate-heading crosswalk committed in `research_method.md`: `6cd22de1d126cf735200ca78127fcf7aa31660ac`.
- Cross-reference analysis appended to `coop.log.md`: `335d1269542a6b17cf251a155b5ca654b05628ff`.
- No candidate facts were rewritten and no numbering was changed.
- **Next active phase:** field-level completeness audit against `method.md` §7 (metadata) and §§8–9 (ethics and rights). Prioritise the verified/partially verified archive leads and the unnumbered Soledad/RISK/Upheaval/CELL(R)/Urata records. Identify missing evidence fields and conflicting claims; do not fill them without sources.


## Milestone 3 — metadata and ethics completeness audit (started 2026-11-15)
**Active phase:** inspect candidate records against `method.md` §7 and §§8–9. This is a gap audit, not an invitation to fabricate missing data or rewrite uncertain claims.

Audit dimensions:
- item existence and exact identity (title, version, medium, date, catalogue/archive ID);
- maker/performer and roles, with identity confidence;
- place and relationship to institution/community (resident-made, visiting, staff, broadcast, found/recovered, later reconstruction);
- source and provenance chain, including original vs copy/reissue;
- evidence status vs editorial visibility rating;
- access, rights, consent, privacy, coercion and community terminology;
- what has not been verified (audio not auditioned, restricted access not requested, no contact made).

**Working rule:** an archival finding aid can verify the existence of a described object, but not necessarily its musical contents, authorship, exact recording circumstances or reuse rights. Do not treat a catalogue description as an audition.

First-pass priorities: records with extant sound objects and significant ethical/provenance risks (Parchman, Kalaupapa, Partheni, Carville, Svenskt visarkiv, Margaret Valiant, Harbert/LOC, Indiana/Texas prison tapes, Prussian cylinders, Hénonville, Soledad CTF, RISK, Upheaval, CELL(R), Urata). Then check conditional/context-only records. Record exact gaps in the next milestone; no changes to candidate claims until evidence is sourced.


## Milestone 3 — metadata / ethics completeness audit: first-pass gap register (2026-11-15)
**Audit scope:** canonical recording/archive leads inspected against `method.md` §7 metadata and §§8–9 ethics/rights. This is a gap map, not a claim that the underlying recordings have been audited or heard. Existing notes already contain useful cautions; the gaps below are the next evidence tasks.

### A. Recording identity and provenance gaps
- **ARSCH (Bitsch, 2020):** release title/date/format and collective context are documented. Missing: exact track-to-source-tape chronology, original reel dates/formats, individual performer/recorder roles, label catalogue/edition identifiers, and independent corroboration of the 2019 fire/archive-loss account. Confirm whether all album tracks are from pre-fire surviving tapes.
- **Holy Church of Yahweh (Quezon City, 1978–91):** several dozen cassettes are documented, but no discrete music item is established. Missing: item IDs, exact date/title/track, whether content is music/chant vs spoken ritual, recordist/performer roles, current custodian and community-authorised access. Remain LEAD until a specific musical recording is confirmed.
- **Grand Valley / Pros and Cons (2017–20):** album titles, song counts and participant anonymity are documented. Missing: complete item/track metadata for *Undisclosed Location*, physical/digital release identifiers, recording dates per song, full participant-role/production credits, and explicit current reuse/consent conditions. Do not seek identities.
- **Parchman women (1936/1939):** collection and named singers are documented. Missing: per-song AFS/field-disc/matrix IDs, mapping of named singers to exact sides/sessions, recording dates and recordists for each candidate, and rights/access conditions for each source object. Prioritise LOC catalogue crosswalk rather than general Parchman claims.
- **Kalaupapa (1952):** cassette, sides, choir names, two patient recordists and several credits are documented. Missing: complete item accession/shelfmark, full 11-song tracklist and exact titles, exact singer/choir membership and patient status by performer, full recording chain, and community/archive publication permissions. Distinguish the separate 1958 DePauw reel.
- **Partheni / *Songs of Exile* (c.1970–71):** 16-song cassette and named roles/recording circumstances are described. Missing: present custodian and stable item identifier, original cassette vs later copy/CD genealogy, exact recording date, complete track order/durations, current authorised transfer, and rights/consent position. Reconcile the claim of a later CD with the 2018 account that it was unpublished at that time.
- **Drapchi 14 (1993):** cassette and variant track counts are documented. Missing: original carrier/accession, exact track sequence and edition lineage, identity/voice-protection edits per copy, and permission/access conditions. It remains CONTEXT ONLY; do not attempt to reverse anonymity.
- **Clifton Hill (1976–83):** archive corpus and recordist are known. Missing: selected item IDs for unknown/under-documented performers, original cassette IDs, recording/performer role per event, and rights/consent for any proposed item-level entry.
- **Carville cantatas:** finding-aid cassette entries are cited. Missing: stable item IDs beyond series/box/folder, exact dates and durations for items 5–8, full tracklists, patient/staff performer credits, whether Christmas entries are duplicates, and archive permission/reproduction conditions.
- **Svenskt visarkiv:** reel references and corpus counts are documented. Missing: item-level song-to-reel and singer-to-reel mapping, individual dates/venues, exact Hinseberg date (1973 vs 1975), digitisation/access status and restrictions. Preserve confidential status/anonymity; no inference from archive logs alone.
- **Anders Enevig:** archive size and one Sambleben audio lead are documented. Missing: Royal Danish Library call numbers, exact recording date/location for Sambleben, which items contain music vs speech, the 205-tape vs ~400-hour corpus relationship, recordist/performer roles per item and access/consent restrictions. Do not assign Sambleben to Blushøj without evidence.
- **Margaret Valiant:** three strong LOC examples have AFS identifiers. Missing: exact session dates and recordist metadata for each, source-disc/matrix and preservation identifiers, broader camp-item inventory, performer biography/context, and rights/access terms. Keep camp performances separate from arranged radio/pageant events and outside entertainers.
- **Harbert / AFC 2024/014 (Louisiana/California):** collection scale, file names and selected recording dates are known. Missing: item-level IDs/timecodes/tracklists for priority LCIW and New Folsom files, participant-role mapping, distinction between original field recording and derivative/edit, and rights/consent for third-party performers. Do not assume Harbert's CC licence covers all contributors.
- **Indiana State Prison / Bruce Jackson (1962):** IU accession numbers and tape ranges are known, but no crosswalk to item/track, singer, date and released/unreleased status exists. Need original logs and compare IU accessions against Smithsonian/Folk-Legacy copies; establish which audio is genuinely recorded inside vs Hank Ferguson's 1963 home rerecordings.
- **Prussian Phonographic Commission (1915–18):** corpus count and media distinction are strong. Missing: individual cylinder signatures, performer identities, nationality/language/camp/date mapping, specific access/audio conditions and item-level later publication status. Critical ethical gap: coercion/selection/consent cannot be assumed; catalogue classifications and colonial research conditions need item-level contextualisation.
- **Hénonville / Boder (1946):** USHMM accession is known and six-song session/performers are described. Missing: exact wire spool ID and original Akron archive cross-reference, precise date, track sequence/durations, spelling reconciliation from original notes, recording vs song-origin place per track, and rights/access conditions.
- **Texas prison farms / Bruce Jackson (1964–66):** several LOC reel IDs, dates, song titles and singers are documented. Missing: source-reel crosswalk for second-generation samplers, precise facility and work-action mapping for every song, uncertain name/title spellings, relation to AFC 1965/011 and AFC 1967/009, and rights/access terms. Do not treat dubs as independent performances.
- **Enevig wider archive (#18):** collection-level duplicate of #11, not a new candidate. Same item-level gaps as Enevig above; use one stable collection record if a structured index is later approved.
- **Ericson Acosta (2011):** two dates, tracklists and in-jail setting are documented. Missing: exact master/carrier/recording engineer and chain, exact credits per track, distinction between raw session recordings and CD compilation sequence, current authorised access and rights. State clearly that Reyes was an outside collaborator and this is not an inmate-only recording.
- **Ohio Penitentiary 511 (1971):** four-track release and player credits are documented. Missing: original label/catno/matrix, exact session date, full engineer/producer credits, original LP object provenance and payment/credit claims independently verified. Reissue makes it CONTEXT ONLY; don't infer all band members were equally credited/composers.
- **Uzuakoli / Harcourt Whyte:** existence of original choir vinyl is attested, but the actual release remains unidentified. Missing: title, label, catalogue/matrix, exact date, tracklist, venue, singer roster, patient/resident status, relation to posthumous 1977 recording vs pre-1977 commercial choir records. Do not attribute ARC 1059/1106 to the colony choir without primary evidence.
- **Liberation (Massachusetts, c.1981):** five reference mixes and first-person production account are unusually strong. Missing: exact facility (Norfolk vs Shirley conflict), session date, names or consented aliases, producer/engineer role verification, original cassette/multitrack survival, rights owner and performer consent. Streaming MP3s are not permission. Do not name musicians without their agreement.
- **RISK (Kentucky State Penitentiary, c.1984):** first-person history and reported ~50 prison-cassette songs exist. Missing: tape count/sequence, exact dates, equipment/recordist, complete original tracklist, track-by-track identification of prison-original vs reunion rerecording, stable carrier/digital file identifiers, rights ownership and consent. Preserve public pseudonyms.
- **Smithsonian Anacostia AV003511-2:** archive item exists but does not yet establish a prison-made recording. Missing: tracklist, source reel genealogy, cue sheet, precise facilities, original recording dates and whether it is a compilation of earlier sources. Keep CONTEXT / SOURCE AUDIT, not candidate.
- **Upheaval (Waupun, 1974–75):** 45 and 1975 video evidence are documented. Missing: exact single label/catalogue/matrix and session date, full video accession/item ID and track/timecode list, radio/TV station and broadcast master evidence, personnel by session, rights and consent for audiovisual publication. Do not promote other Waupun bands without surviving audio.
- **Soledad CTF / Jack Bowers (1983–96):** LOC digital ID and set-level track counts/titles are documented. Missing: performer/inmate status and role for each set, original cassette IDs and liner-photo crosswalk, exact session dates, tape-to-AIFF transfer chain, whether “Oscar's Tune” belongs to Soledad, interview correlation, rights/consent. Keep Rusty Smith separate from the unrelated Santa Cruz copyright record until proven.
- **CELL(R), Leuven (2023):** release date, tracklist, venue, eight incarcerated contributors and some credits are documented. Missing: CD catalogue/label/imprint and physical metadata, track-by-track contributor mapping, confirmation of preferred public aliases/credits, recording date(s), current rights/reuse permissions. Do not identify aliases.
- **Harry Urata / holehole bushi (1960–80; CD 2000):** collection and several tape IDs are documented. Missing: track-level contents and exact song titles, date/location/performer for each side, Japanese-language label transcription, mapping between tapes and MHCD2000, identification of which items are music vs oral history, performer biography/consent, rights per item. Do not interpret “1885” as recording date.

### B. Cross-cutting ethics / rights findings
- Many records correctly say “no audio auditioned,” “no contact made,” or “permission unknown.” Keep these statements explicit and update only after the action occurs.
- A catalogue description or accessible stream verifies neither informed consent nor reuse permission. Separate **access**, **listening**, **quotation**, **reproduction**, and **redistribution** rights.
- Highest sensitivity: anonymous incarcerated women at Grand Valley; Drapchi nuns and identity-protection edits; patients/residents at Kalaupapa, Carville and Uzuakoli; detainees at Partheni; coerced/colonially collected POW recordings; displaced Holocaust survivors; named prison singers in historical archives; living or recently living contributors in Harbert, Soledad, RISK and CELL(R).
- Use aliases/anonymity exactly as the source and participants authorise. Do not identify pseudonyms, reverse anonymisation, infer diagnosis or legal identity, or expose sensitive medical/prison details beyond what is necessary.
- For coercive settings, document power imbalance and institutional control. Do not imply consent simply because someone sang or a recording was catalogued.
- Community language requires special review for Uzuakoli, Kalaupapa, Culion, Romani/traveller collections, Japanese plantation workers and Indigenous/Hawaiian materials. Historical titles can be preserved as metadata with explanation, not adopted as editorial voice.
- No archive contact, participant contact, listening session or rights request was made during this audit.

### C. Audit disposition
No candidate metadata was silently filled and no recording was upgraded or downgraded in `environment-leads.md`. The register already captures many of these uncertainties; this milestone consolidates the open fields in one place so later research can close them systematically.

### Next active work
1. Highest-value next: item-level follow-up on **Soledad CTF** (LOC cassette liner photographs, AIFF files, Jack Bowers MiniDV MV031) and **Waupun** (specific *Waupun World* issues), but only if public sources can resolve metadata without claiming private archive access.
2. Parallel priority: identify the actual **Uzuakoli colony-choir vinyl** and obtain a source-item crosswalk for **Kalaupapa** and **Carville**.
3. Then tackle **Parchman/Valiant/Jackson** source-tape crosswalks and **Urata** Japanese-language tape notes.
4. Add a stable index only after owner approval; do not renumber or convert the prose register.


### Milestone 3 completion / next research pass
- First-pass metadata and ethics gap register committed in `research_method.md`: `2e45024a32a389e8dc28fef1571946ffb40614fe`.
- Audit log appended to `coop.log.md`: `38888ac735a88d34e7c23b98e751c92ed7ad5cbd`.
- `environment-leads.md` and `method.md` were not changed; no factual upgrade or rights assumption was made.
- **Next active research pass:** public-source follow-up on (1) Soledad CTF / Jack Bowers item-level records and the interview/liner photos; (2) Waupun newspaper holdings and any accessible issue excerpts; (3) Uzuakoli colony-choir vinyl identity. If sources cannot resolve these, prepare precise archival request targets but do not claim requests were sent.


### Milestone 4 — public-source follow-up completed (2026-11-15)
- Soledad: reconfirmed LOC subseries and precise digital ID `afc2024014_dc001`; Jack Bowers interview MV031 is separately described (2003–04). No performer identities/inmate status resolved from public finding aid.
- Waupun: confirmed digitised newspaper availability and exact WHS holdings; post-1928 *Waupun World* access requires Waupun Public Library local access. No new recording verified.
- Uzuakoli: still no identified original posthumous choir vinyl. Added a low-confidence forum clue naming two albums/Nnamdi Olebara, but it is not evidence and must not be promoted without sleeve/label/primary testimony.
- Upheaval: added “Vampire Lady” as a reported surviving song and clarified that Hayes reportedly held a CD's worth of recordings while Rudd's tapes' whereabouts are unknown. Provenance of these copies remains unresolved.
- `environment-leads.md` update: `8e3948341d37c30d27b93d68dc46992be6937fb3`.
- `coop.log.md` update: `55ef20e2ca9b82e10fb0afe6e18100d1d4b5b9c3`.
- No new independent candidate verified; no archive/participant contact, listening, access request or reuse permission occurred.

**Next active phase:** widen small-web discovery outside the already-covered North American/Western European cassette blogs, targeting local-language independent blogs and archive finding aids in West Africa, Southeast Asia, Latin America and Eastern Europe. Use local-language variants for prison, commune, psychiatric hospital, colony, residential institution and cassette/private pressing; admit only candidates with an extant recording and corroborated environment connection. Then revisit exact unresolved archive requests.


## Milestone 5 — international small-web discovery sweep (started 2026-11-15)
**Active phase:** expand beyond existing English-language cassette blogs and North American/Western European archives. Search in regional languages for prison-made music, community/commune recordings, institutional choirs, patient/resident recordings, and private-press/cassette documentation. Blog posts are discovery leads only; require primary/archival corroboration before adding candidates.


### Milestone 5 — international small-web sweep: first results (2026-11-15)
- **Argentina:** added *Rimas de Alto Calibre* (Unidad Penal 48, 2010–12) as a well-documented CONTEXT ONLY regional comparator; added *El rock en la cárcel* (Carabanchel, 1993) as CONTEXT ONLY due to its 20,000-copy launch and prominent collaborators.
- **Brazil:** added Impacto Real / *Mundos dos Muros* (Presídio Santa Augusta, 2011) as VERIFIED recording / PROMISING. The original Comunicasom blog was cited as hosting audio but is inaccessible in the current web route; no audio auditioned. Added Danila Alves / *A Voz da Liberdade* as CONTEXT pending proof of recording location.
- **Small-web method:** found contemporaneous Blogger reposts but several repeat the same source text; they are not independent corroboration. The original project blog and institutional records remain the verification targets.
- Lead-register update: `environment-leads.md` commit `0cb0fe7bdfe035537ee213aceeefaaa9e1c414f9`.
- Log update: `coop.log.md` commit `d4d0adcc9bda7934a1d211843798e459beb32c1d`.
- No permissions, listening, contact or access were claimed.

**Next:** broaden the Portuguese-language search to Chilean and Argentine clandestine/camp recordings and Brazilian prison music, then move to Eastern European and African local-language archive/blog routes. Maintain the distinction between prisoner-made audio, outside collaborations, broadcasts and music merely played in prison.


### Milestone 5 — international small-web sweep: Brazil, Costa Rica and Chile
- **Brazil:** Impacto Real / *Mundos dos Muros* added as a PROMISING 2011 prison-made 9-track CD (three incarcerated contributors at Presídio Santa Augusta). Original project-blog audio was not accessible; title spelling and full tracklist remain open. Danila Alves / *A Voz da Liberdade* remains context-only until recording location is proven.
- **Costa Rica:** Sufferras Crew added as a PROMISING in-prison recording lead (La Reforma, c.2012); Rootstico gives five public stage names and a download link but not the release identity. A 2013 newspaper corroborates a group formed inside the prison, without mapping the public aliases to individuals.
- **Chile:** Chacabuco clandestine camp cassette/LP documented as CONTEXT ONLY due to later publication/reissue; useful for provenance distinctions (original cassette vs LP vs later rerecording and reconstruction).
- **Argentina/Spain:** Rimas de Alto Calibre and *El rock en la cárcel* retained as CONTEXT ONLY comparators due to public promotion and circulation.
- `environment-leads.md`: `ef6e186544eb1845c726a6bcb8a7b22f56de010f` (Chile/Costa Rica addendum; Brazil addendum earlier `0cb0fe7`).
- `coop.log.md`: `f5e3b8f79e90a04cce3d8bea3e03ff8f7105a79a`.
- No audio auditioned, no archive/participant contact made, and no rights or reuse permissions inferred.

**Next active task:** pursue Costa Rica's Rootstico/Sufferras file and producers; search African and Eastern European local-language small-web sources for similarly small, place-specific prison/commune/institution recordings. Preserve the source hierarchy: a copied blog post is discovery, not independent corroboration.


### Milestone 5 — additional regional screens / false positives
- **Es lo que hay (Argentina, 2008):** band formed in prison, but recording was planned for an outside studio; no prison-made recording verified.
- **Ivan Kuchin (Russia, 1985–87):** claimed prison-era tape and later commercial chanson releases; artist is now well-known and dates/provenance are inconsistent. CONTEXT ONLY.
- **Atrofia Cerebral / *Matanza Extrema* (Peru):** prison massacre cover image only; no inmate-made music evidence. False positive.
- **Studio du Temps / Saint-Maur (France):** incarcerated workers digitised INA archive recordings, not their own music. Context only.
- Lead register: `environment-leads.md` commit `beec17dc3f6b2acecd066d25fb7e3dff81c9c38a`.
- Log: `coop.log.md` commit `ee7f0cfe33332cd232dffd17b6094c91f65eb12e`.

**Next active task:** pursue the Costa Rican Sufferras Crew in-prison source tape/download and identify the exact file/recording session; continue African/Eastern European local-language search. No contact has yet been made; any contact would require a separate deliberate step and should not be implied by the research.


### Milestone 5 — African small-web screening
- Re-surfaced Zomba Prison Project, already recorded and CONTEXT ONLY due to Grammy nomination and substantial coverage.
- Screened TID / *Prison Voice* (Tanzania), Gemann / *14* (Ghana), Lamboginny's Kirikiri concerts (Nigeria), and Yaw Sarpong's planned Ghana prison music programme. None establish a new extant recording made by inmates inside prison.
- `environment-leads.md`: `cdb6bcadb5294c98b5c61c200fc65ba526a3da12`.
- `coop.log.md`: `f33d72a842c2c3886897627e0203bc3a75ccd33a`.
- No candidate added; no audio auditioned/contact made.

**Next:** continue with the strongest unresolved lead from the small-web sweep: Sufferras Crew / La Reforma (Costa Rica), where a 2012 independent reggae blog links a download and explicitly states that five incarcerated members recorded inside. Resolve the linked file's identity and session provenance without redistributing unauthorised material. If that route stalls, move to archive-level searches for other Latin American and African prison music collections.


### Milestone 6 — Sufferras Crew track-level follow-up
- Identified **“La Vida En El Penal (Automatic Riddim)”** as a specific track attributed to The Sufferras / Sufferras Crew. A Videos Luis upload is dated 7 March 2010; ReggaeTico's official riddim-pack listing corroborates the track title.
- The Rootstico post (2012) says the five-member group recorded inside La Reforma, and a 2013 *Diario Extra* report confirms the group formed and made music inside. Neither source links this specific track to the prison session. Upload date is not recording date.
- Rootstico's 2012 MediaFire link returns 404. Its two embedded videos were not resolved. Do not replace the original prison source with third-party rips.
- Lead register update: `environment-leads.md` commit `ffdd019b18f847fbf98b51e531a1051c025343fe`.
- Log update: `coop.log.md` commit `7f5deff2b98b7a891988789a0ad393c1b5667863`.
- No audio auditioned, no contact made, no permissions inferred.

**Next:** continue public-source research for original 2010 session credits, recording date and track-to-prison crosswalk. If no primary evidence is publicly available, retain PROMISING / PARTIALLY VERIFIED and note that a direct archive/producer enquiry would be required; do not contact anyone without separate user authorisation.


### Milestone 6 — producer/source search result
- Further public searches for E.G.V. Records, Cultura Roots, DJ Zion, the Rootstico MediaFire ID and the exact track found no primary session log, sleeve, or statement connecting the 2010 “La Vida En El Penal” upload to the in-prison recording session.
- Status remains PARTIALLY VERIFIED / PROMISING at group/session level; track-specific prison provenance unresolved.
- Log commit: `2c418f5b45f771d3fa32290e73ca48e812818eee`.
- No contact made and no candidate facts changed.

**Continuation point:** do not repeat the same public search. Next, either (a) locate a primary local archive/press source for the 2010 Sufferras recording or (b) move to other under-documented Latin American prison projects. Any direct email/contact to the blog author or producer requires separate user authorisation.


## Milestone 7 — expand beyond prisons: residential schools, refugee settlements and liberation-front recording infrastructure (started 2026-11-15)
**Research question:** identify extant, under-catalogued recordings made by residents/members in environments not yet adequately represented in the register. This pass prioritises residential-school audio archives, refugee-camp resident compositions, and mobile/frontline recording archives. Do not promote professionally publicised collaborative projects simply because they were made in a camp.

**Sources opened / current findings:**
- Presbyterian Church in Canada Archives guide: audio tape file **2011-7001**, titled “Cecilia Jeffrey Residential School and Birtle Residential School Choir,” 30 songs, undated, no recording location indicated on the tape. Original tape digitised in early 2011 into two side-master WAV files and 30 individual CDA files. This establishes an extant sound object and school-choir association in the archive title, but not date, venue, student membership or whether the recording was made during school operation. Treat as PARTIALLY VERIFIED archive lead, with strict survivor/community and child-protection ethics.
- Eritrean EPLF / Dmtsi Hafash: 2026 open-access scholarship documents master cassettes, lyric books and a digitisation project at Eritrea's Ministry of Information; travelling field recordings in remote front-line settings; an entire show recorded with fighters and patients in a field-hospital unit; songs named “Bdho,” “Salina,” “Filmawit Ade,” and “Weledi.” This is a substantial archival route but the collection was strategically curated for national liberation messaging and some songs are widely known. Do not treat the collection as outsider music or assume all recordings are obscure. Context-only at collection level; specific unidentified hospital/frontline masters remain an archival research lead.
- Za’atari, Jordan: Oxford 2024 thesis documents residents composing songs about displacement and camp life; a 2015 Recording Earth project documented refugee musicians and produced a film/recording trail; a 2023–26 NGO music programme created a camp studio and a 2026 “Hope/Amal” album by Syrian children. These projects are public, collaborative and professionally promoted, so currently context-only; search for resident-made, independent recordings outside the programme before adding candidates.
- Calais “Jungle”: *The Calais Sessions* (2016) is a 13-track collaborative album recorded in a makeshift camp studio with refugee musicians and UK visitors. Bandcamp Daily selected it in its 2016 best-albums list; context-only for obscurity. Distinguish camp residents' songs/performances from visiting musicians' contributions.


### Milestone 7 — expanded environment sweep: current disposition
- **Residential-school audio:** added Presbyterian Church in Canada Archives file 2011-7001, an undated 30-song tape titled “Cecilia Jeffrey Residential School and Birtle Residential School Choir.” PARTIALLY VERIFIED / PROMISING archive lead; no date, venue or performer identity is given. Treat with survivor/community-led permissions and do not identify child performers.
- **Eritrean frontline studio:** added Dmtsi Hafash / EPLF travelling studio and master-cassette archive as a CONTEXT-only collection-level route. A 2026 article documents frontline recording and a complete field-hospital show with fighters/patients present; exact item metadata remains absent and the collection is politically curated.
- **Refugee settlements:** Za’atari 2015–26 recordings and the 2026 Amal/Hope album are documented as context-only due to NGO collaboration/publicity. Calais The Calais Sessions (2016) is also context-only due to public release and visiting-musician collaboration.
- **Leprosy-mission archive:** added TLM Canada / Effect:Hope multinational audiovisual archive as a context-only route. Its listing names audio tapes made on Purulia, Chandraghona, Bhutan, Irian Jaya, Papua New Guinea and Thailand, but no sound contents or resident-music provenance. Do not call these music tapes until item descriptions establish it.
- **Remote-setting false positives:** Great Lakes Lighthouse Keepers oral-history cassette; Casey Antarctic favourite-music cassette; Percy Riley USSR coal-mining visit tape with incidental music. None is evidence of resident-created music.
- environment-leads.md additions: b860cb3426c0a034f6cce1b63a22f2cf82552533 (residential-school/Eritrea/refugee routes), 4a290c30316651bcbaa6f04743dbd01e7b21ba6c (TLM and remote-setting screens).
- coop.log.md additions: 7f37c4a26efcdb5b56316d460966226b91192512 and 10c08813b14097786805e2221716eff2d82684b1.
- No new high-confidence obscure recording was admitted. One new partially verified archive sound-object lead (2011-7001) is worth follow-up; the other findings are contextual archive routes or publicised collaborations.

**Next active phase:** search the TLM/Effect:Hope audiovisual inventory and other national leprosy mission archives for specific resident-made music; investigate whether 2011-7001 has an associated donor or accession file and any public, non-restricted provenance note; then extend the same method to refugee-camp personal cassette circulation and field-hospital/guerrilla archives in underrepresented regions. Keep each search bounded and record null results, not merely candidate finds.


## Milestone 8 — West Papuan refugee-camp recordings and cassette networks (started 2026-11-15)
**Major new lead:** Concertzender's 2026 West Papua programme identifies an unpublished 4:15 track titled **“Papua Barat”**, recorded in a Papua New Guinea refugee camp on a cassette labelled “refugee camp”; the programme compiler says copies of these recordings are held by West Papuan refugees/exiles in the Netherlands. Performer, camp, date, original tape custodian and recording chain are unknown. This is a high-priority item-level lead because the recording is explicitly tied to a refugee camp and remains unpublished.
**Related scene:** ANU Press scholarship documents the formation of Sampari in Blackwater camp, Vanimo, in August 1984, after West Papuan refugees fled Jayapura; the group arranged and recorded “songs of the struggle,” including “Blue 7 White 6.” PACE's Papua Collecties inventory documents a Sampari self-published CD-R of 24 traditional Wor songs sold at performances, and a cassette containing a 26 June 1986 live performance at the End of the World, Amsterdam, plus an unidentified album-side string-band recording. Do not assume these two PACE items are the same as the Blackwater-camp recordings.
**Mambesak / archive context:** ANU Press research confirms five cassette volumes of folksongs recorded 1978–83, widely marketed in West Papua, and documents that after Arnold Ap's death the University stopped selling the series and copies circulated through refugees and activists. PACE identifies original cassettes for volumes 2–4, homemade copies for 1 and 5, and three original Arnold Ap reels with songs, field recordings and radio material. The published Mambesak series is CONTEXT ONLY for obscurity (locally popular and culturally iconic); the less-circulated original reels, prison recordings, and refugee-camp cassettes are the stronger item-level research targets.
**Expanded scene:** PACE's archive inventory lists multiple additional West Papuan groups and original cassettes (Yanero, Apuse, Tune Manaa, Kurana Mambesak, Eyuser, Beyuser Byak, etc.). These are discovery leads for a local cassette scene under Indonesian rule; exact recording locations, dates and performers require item-level verification. Do not label all local-language Christian/gospel string-band cassettes as outsider music; assess the specific political/social context and local circulation.


## Milestone 9 — Southeast Asian refugee-camp cassette cultures (started 2026-11-15)
New regional sweep beyond West Papua:
- **Cambodia / Thai refugee camps:** independent Cambodian Cassette Archives research by Mark Gergis identifies Kieng Yuthhan's “Blue Basket” (also “Sronos Kantong Khiev”), recorded in November 1986 inside SITE 2 refugee camp in Thailand. Kieng and his group built a bamboo studio and recorded to cassette using borrowed instruments and two microphones. The tapes were sent to Cambodian companies in the United States for duplication/distribution. The song was reissued on *Cambodian Cassette Archives* (2004 CD; 2016 double LP/CD), so the known track is CONTEXT ONLY for obscurity; the full original cassette-album and other camp-made tapes remain discovery targets.
- **Karen / Mae La and other Thai border camps:** 2015 Manoch Chummuangpak research documents Karen refugee pop albums on cassette since the 1990s and names early artists Hsar Gay Doh Htee, Danny, Kaw Law La and Tha Kolo. Charlotte Hill's 2021/2022 ethnography documents three recording studios in Mae La, including Saw Ka Lu's studio begun in 2008 with borrowed church equipment and a bamboo-walled room; residents record original music and distribute through YouTube/Spotify and diaspora networks. Specific public songs include Pu Dah's “Refugee” (2020), Hser's “We Need Unity” (2020), Tempered Family's “Revolution” (2020), TNKG's “Who are you?” (2017), and NUCELER/OBED 7's “Life in MRM refugee camp” (2020). These are context-only due to public digital visibility; early 1990s cassette albums and less-circulated camp recordings remain promising item-level targets.
- **Karenni / Nai Soi camp:** PAN Records' *Karenni: Music from the Border Areas of Thailand and Burma* (1994) contains three tracks by singers from Nai Soi refugee camp. Fred Gales's Concertzender programme identifies “The Journey” (4:55; ten named singers/performers, vocals and flutes) as recorded at Nai Soi in April 1993. Commercially issued field recording, so context-only for obscurity, but exact track-level documentation is valuable.
- **Other refugee audio archives:** AUB's Palestinian Oral History Archive holds around 1,000 hours of interviews, folktales and songs from Palestinian refugees in Lebanon, including 172 hours of folktales/song recordings and 36 hours of women's video from Ein el-Helwe. This is an archive route, not automatically a music candidate; distinguish songs embedded in oral histories from stand-alone resident-made recordings.


### Milestone 8–10 — refugee-camp and exile research: completed first sweep (2026-11-15)
**West Papua / PNG**
- Added unpublished “Papua Barat” (4:15) on a cassette titled “refugee camp,” described by Concertzender as recorded in a PNG refugee camp and held in refugee/exile collections in the Netherlands. HIGH PRIORITY; exact performer/camp/date/custodian unresolved.
- Added Sampari: formed in Blackwater camp (1984), later exile in the Netherlands; 24-track self-published CD-R (PACE Band 169) and 26 June 1986 Amsterdam live cassette (Band 189). PROMISING; do not assume either object is the original Blackwater recording.
- Added Arnold Ap's “Mystery of Life” / “Misteri Hidup” prison cassette, reportedly recorded in his cell and sent to his wife in a PNG refugee camp. HIGH PRIORITY to locate original cassette; later Eyuser/Strange Birds versions are rerecordings.
- Added East Awin field-tape corpus: Diana Glazebrook explicitly says she tape-recorded songs but never speech (1998–99). HIGH PRIORITY archive-tracing lead; song titles in the book are not yet crosswalked to tape.
- Mambesak published five-volume series is CONTEXT ONLY for obscurity; original Arnold Ap reels, radio tapes and unissued prison recordings remain stronger item-level targets.
**Cambodia / Karen / Karenni**
- Added Kieng Yuthhan's “Blue Basket” from SITE 2 camp (1986); bamboo studio and cassette circulation documented; track reissued in 2004/2016, so CONTEXT ONLY, but original cassette-album remains a target.
- Added Karen refugee cassette culture since the 1990s and Mae La studio network (Saw Ka Lu, Kaw Koh, etc.); early cassette albums remain PROMISING. Public 2017–20 songs are context examples.
- Added PAN Records *Karenni* (1994), including Nai Soi refugee-camp tracks and Fred Gales's April 1993 recording of “The Journey”; CONTEXT ONLY due commercial issue.
**Afghanistan / Liberia**
- Added Haikal's 1985 Peshawar cassette (40-minute Mujahideen epic) and an unidentified second war cassette; PROMISING, but these are exile-city recordings, not proven camp recordings.
- Added six-disc Afghan Music Preservation project (2001) as a LOC/VOA archive route; session venues and catalogue IDs remain unknown.
- Added Buduburam's 16-group *Giving Voice to Hope* (2009) as CONTEXT ONLY; underlying S-Man/Shadow camp-studio masters and demos are the promising target.
**Palestine / Dadaab**
- Added Ettijah's *The Journey* (2017) and “Ana Qawiya” (2020) as PROMISING group discography; protect the members who were minors at formation.
- Added Palestine Street's Dheisheh camp rap corpus as PARTIALLY VERIFIED / PROMISING; exact masters and full discography unresolved.
- Added Dadaab Allstars' “Dear Mr. Peace” (2012), Refugeenius (2016), Dadaab Stories and the Refugee Cultural Heritage Archive as context/route entries. Refugeenius project produced 48 songs but released 18; trace artist-held unreleased masters.
- Screened Sierra Leone Refugee All Stars as CONTEXT ONLY: camp-formed band, but later commercial albums recorded after leaving the camps.
**Repository changes**
- West Papuan entries: `environment-leads.md` commits `4a1804a12b2f9a5584f502f800202c4e4194847b`, `7aff1276ef0c3250535d5dda1fdd1589bc5a54d4`, `e24ecd2b71f8998647bd33e272308cfebb8a4744`.
- Cambodia/Karen/Karenni: `ef0a0f3945bea7f20bcca11be2f9d4b4ca59219c`.
- Afghanistan/Liberia: `7371c102c90e75f9e8afc4715cf4e64bcbd860be`.
- Palestine/Dadaab: `99654e5f4ac52ef8ff41cc759b79e7c5a8bb233d`; Sierra Leone context screen: `3aeacc8ed10e89a62aeb9bdb38a21641e50fcf5a`.
- `coop.log.md` contains corresponding research entries and null-result notes; most recent log commit: `3c6bfc9adfa15d163bfc72c93dafc2e7c0d698d9`.
- No audio audition, participant/archive contact or rights request was made during these passes.

**Next active phase:** item-level archive crosswalks for (1) the West Papuan “refugee camp” cassette / Arnold Ap prison tape / East Awin song tapes; (2) Afghan LOC six-disc deposit and Haikal cassette; (3) Karen 1990s cassette releases and Buduburam 48-track masters; (4) Palestinian camp archive sound items and Ettijah/Palestine Street original releases. In parallel, continue language-specific small-web search across other refugee settlements and displacement settings (e.g. Sahrawi camps, Sudanese/Eritrean settlements, Burmese/Karenni diaspora, Afghan/Pakistani exile, Palestinian camps). Search original blogs, local labels, community radio, and resident-run archive platforms; record no-result screens as well as new candidates.


## Milestone 11–12 — Sahrawi and northern Greek refugee-camp archives (2026-11-15)
**Sahrawi camps / Algeria**
- Added the British Library's 133-item *Portraits of Saharawi Music* (2013–14), a collaborative archive of traditional, medeh, revolutionary/nidal and modern music from camps; local copies were left in camp institutions.
- Identified specific camp recordings: Salwan's “Bismilah” (Smara; recorded in Faknash Abeid's house), ElHafed's self-composed “Your Objective” (Dakhla; recorded for the BL project), and Tarba Bueibu's “Saharawi Revolution” (Al Aaiun; later on a 2015 Songlines CD). The first two remain promising item-level recordings; Tarba's released version is context-only.
- Nubenegra's 1998 production diary reveals three pre-mix CDs from camp sessions: traditional, modern, and an unissued/“discarded” disc. The first two were turned into the 1998 albums; the third is a HIGH PRIORITY archive target. Separate the 1982 *Polisario Vencerá* reissue, recorded in Barcelona.
- Radio Nacional Saharaui / Ministry of Information archive: c.2,500 reels and digital recordings, including music, cultural programmes and performances. Public access/reuse and item-level metadata require Ministry review. Added Badawi Sahrawi Music Archives as a diaspora-run cassette preservation route.
- Lead-register commit: `447536d814d37a5d4aa11bd608524735ea95d0fa`.
**Northern Greece / Thessaloniki (2016)**
- Added Oreokastro's resident-run “Refugees Got Talent” contest; an 11 Aug. 2016 rap performance by two young women is described in MMRC podcast as an audio extract from a Refugee TV Facebook video.
- Added field recordings of an unnamed Syrian refugee singing his own song about the revolution (21 July 2016), “Janna, Janna” protest chant, and Nidal Karam's already-circulating “Safarna A'la Euroba” performed at a protest. The Softex adhan is religious recitation, not a main-discography music item.
- Protect minors/unnamed performers and distinguish original songs from covers, playback and religious recitation.
- Lead-register commit: `e317a76ca0b48b8828cbbcca2c62c94ab69a7b9a`.
- Latest log commit after both additions: `f09b436e13d9d99cb622fbc70a984842ddb4cf55`.
- No audio audition, archive contact or reuse request was made.

**Next active phase:** continue the refugee-settlement sweep in less-covered regions (Sahrawi radio item-level catalogue, Arbat/Iraq, Tibetan exile, Somali and Sudanese settlements, plus the original Palestinian camp archive items). Then return to the highest-priority item-level crosswalks: “Papua Barat” refugee cassette, Arnold Ap prison cassette, East Awin song tapes, Afghan LOC six-disc project, and the Nubenegra 1998 unissued pre-mix. Do not contact custodians or performers without a deliberate permission/consent step.


## Active phase 13 — user-led psychiatric survivor / peer-run creative spaces (started 2026-11-15)

**User-provided discovery seed:** Maskine Maskine Amager (MM Amager; https://mmamager.dk/om) and a 105-row list of Danish/international user-led, peer-run, clubhouse, outsider-art, lived-experience and creative-recovery organisations.

**Research question:** not “which organisations exist?” but “which of these spaces have produced, hosted, archived or circulated recordings made by members/participants, and can any discrete obscure recording be identified?” The organisations are discovery conduits, not automatic music candidates.

**Admission gates for this phase**
1. Establish the organisation's identity, operating dates, participant governance and actual creative/music activities from its own sources.
2. Look for concrete audio evidence: participant-made albums/singles, rehearsal/demo tapes, radio/podcast/music programmes, studio projects, event recordings, sound art, cassette/CD-R releases, archived files or item-level collection records.
3. Distinguish member/participant-created recordings from visiting artists, staff-led workshops, commissioned outside artists, general events, therapeutic music sessions, and music merely played at the venue.
4. Record maker/participant consent and anonymity concerns; do not infer diagnoses or identify private participants.
5. Apply obscurity threshold: a venue with music activity but no recording is a research route only; a famous outsider-art institution is not a priority merely because it is well known.
6. Search in local languages and small-web sources (Danish, Swedish, Norwegian, Dutch, French, German, Spanish, Japanese, Korean, etc.), including archived pages, blogs, local radio, newsletters, Bandcamp, SoundCloud, YouTube and archive catalogues.
7. Use user's 105 names as leads, not verified fact. Validate URLs, current/historic status, location, mission and whether the short description is accurate. Flag broken, duplicated, miscategorised or non-music-focused entries. Avoid the supplied generic directory's unverified claims.

**First sub-pass:** MM Amager and the Danish organisations (HJEM/Thorvaldsen, Galebevægelsen, LAP, Outsideren, Fountain House København, plus Danish clubhouse/peer-led networks). Then select international organisations only where primary evidence suggests music/audio.

**Current status:** methodology checkpoint written before external research. No organisation in the supplied list has yet been admitted as a recording candidate solely from the user's descriptions.


### Phase 13 milestone — first screen of peer-run creative spaces (2026-11-15)
**Verified/high-value**
- **Netværkstedet Thorvaldsen / Rooster Music / RadioTi (Copenhagen):** municipal evidence describes a professional sound studio and music publisher where members record and release music with professional producers; concerts/tours under “Thorvaldsens talrige talenter”; RadioTi is a local station for and with people with psychosocial problems. This is a HIGH PRIORITY catalogue/archive hunt, but no specific member release identified yet.
- **Frente de Artistas del Borda (Buenos Aires):** *Música/Canciones para la oreja izquierda*, 16-track CD, 1,000 copies, 2008; contemporary reporting says performed by inpatients; official grant description confirms songs performed by music-workshop members. PROMISING overlooked participant-made album. 2017 “La sangre borda” on *Épocas* is a separate later group track.
- **KAOS / Black Fuel Ensemble (Brussels):** documented in-house ensemble; EU report says KRANKLAND jammed with them and recorded sessions with people he met at the psychiatric-context residency, later sampling recordings in his own work. IME produced a 16-track international collaborative album with composers with lived experience, but external artist authorship and participant contributions must be separated. Public project = CONTEXT; raw sessions/ensemble = PROMISING archive route.
- **Maskine Maskine Amager (Copenhagen):** verified *MMusik* live video archive (El Ray 2020; Tudeprinsen, Love Against The Machine Allstars, A + band, Farmand 2024; further 2023/25 items), plus MMAfilm production unit and 2026 *Virelai* concert film. Not yet known whether acts are members or invited performers. CONTEXT/research route only until provenance is established.
**Not yet screened in depth:** the remainder of the user's 105-entry list. Do not treat the supplied descriptions as verified. Prioritise places that have music studios, member bands, radio stations, recording archives, cassette/CD-R releases or participant-owned catalogues; deprioritise purely visual-art centres unless they document sound works.
**Repository:** new entries in `environment-leads.md` commit `10394edb6d61e91d1b51017278ce9daebb0d1a68`; detailed log in `coop.log.md` commit `de8df8ace9ddc723ed02cdfc33538c36b78a7f3e`.
**Next active tasks:** (1) locate Rooster Music's actual catalogue and RadioTi audio archive; (2) recover the Borda 2008 CD tracklist/physical copy and trace the 2017 “La sangre borda” original; (3) identify Black Fuel Ensemble and IME track-by-track participants; (4) establish member/guest provenance for MMAmager's filmed bands; (5) screen the remaining Danish entries (LAP, Galebevægelsen, Outsideren, Fountain House CPH) and only then expand to other international names with evidence of sound production.
No audio audition, participant contact or rights clearance has occurred.


### Phase 13 milestone 2 — Danish peer-run organisations: media and sound-production screen (2026-11-15)
**Completed:** screened LAP, Galebevægelsen, Outsideren, Fountain House København, and an additional Danish lead, Nationalt Center for Kunst og Mental Sundhed (CKMS). Queries covered official sites, Danish-language music/sound terms, radio/video archives, press releases, newsletters, event listings, and participant-created audio.

**New concrete sound/music leads**
- **CKMS / Lydminder and sound workshops:** verified user-involved sound art, recording, soundscape and collective music-making. CKMS's “Lydminder” project used participant work with sound and memory; an online video documents the artist describing it. Its current “Lyden Ud” workshops explicitly record and process environmental sounds into participant-made soundscapes and music. “Det Åbne Ensemble” is a collaborative improvisation group of people using psychiatric services; it performed at Roskilde Festival on 4 July 2026. The Roskilde event description confirms participant musicians and process but not an archival recording. This is a PROMISING contemporary sound-art / music archive route, not yet an obscure release.
- **Galebevægelsen / Kanal 1:** official Kanal 1 page says the movement began in 1979 with current/former patients, relatives and staff; people associated with Netværkstedet Thorvaldsen have produced programmes for over a decade. The page names rapper Rytme-Hans (Hans Martin Hjortsø) among musicians and lists a 2014 portrait video plus “Chefen for det hele” programmes and a Kim Sonders music video. This is a real participant-adjacent community media/music route, but the individual makers' membership/lived-experience relationship and whether videos are original music recordings remain unverified. Do not assume identity links to commercial artist profiles without corroboration.
- **Fountain House København:** official sources confirm member music activity in Ungehuset Fontana and a member-assembled “Musik På Tværs” group active since 2024, with rehearsals and concerts at house events/TAMTAM. No sound recording, release or audio archive found in this pass. Context / archive route only.
- **LAP:** official archive identifies Natasha Ejskjær Thomassen/Natsang's “Linedans,” written by her, produced by Mads B. B. Krog and released by Gateway.dmf.dk as an iTunes single in 2011, in support of LAP's “Død i psykiatrien” campaign. LAP's 2010/2011 campaign event reports also describe live music by several performers. The song is a verified recording but no source establishes that Natasha was an LAP member or psychiatric-service user; do not admit as participant-made music on that basis. Context-only campaign music pending artist provenance. LAP Radio page lists reports/interviews and music at events, not a distinct member-created music archive.
- **Outsideren:** official activity calendar describes writing, editorial and graphic activities; historical magazine material invited text, image, sound and video submissions, but no specific participant-made music recording was located. No candidate admitted.

**Priority decisions**
1. CKMS is the strongest new recording-environment lead; seek exact workshop audio outputs and ownership/access terms.
2. Galebevægelsen/Kanal 1 is the strongest media/archive route; identify whether Rytme-Hans and Kim Sonders items are authored/performed by people connected to Thorvaldsen and locate any original audio releases.
3. Fountain House and LAP remain context-only until participant-created audio is identified.
4. Outsideren remains screened with no qualifying music object found in this pass.

**Sources searched:** CKMS official pages for “Lydminder,” “Lyden Ud,” sound groups, Recovery Radio, open stage and participant workshops; Roskilde Festival 2026 programme for Det Åbne Ensemble; Kanal 1 Galebevægelsen and video/music pages; LAP press releases, Radio, TV and publications archives; Fountain House official news/calendar; Outsideren activity calendar and historical magazine PDF. No participant, organisation or archive contact made; no audio auditioned.

**Next exact tasks:** (1) identify whether CKMS retains participant-generated Lydminder/Lyden Ud soundscape masters and whether any are publicly released; (2) find the recording/video embeds and producer credits for Kanal 1's Rytme-Hans and Kim Sonders items; (3) search Fountain House archive/social channels for “Musik På Tværs” event recordings; (4) complete the Danish list screen before moving into high-value international names (La Colifata, Bethel House, Workman Arts, Clubhouse Paris, etc.).


### Phase 13 checkpoint — Danish first screen saved; next shift to high-value international cases (2026-11-15)
The Danish first screen is now recorded in environment-leads.md and coop.log.md. The strongest result is CKMS's documented participant sound-making and soundscape production; Galebevægelsen/Kanal 1 provides a public-access music/video route; Fountain House has member music performances but no audio identified; LAP's campaign single is not proven participant-made; Outsideren yielded no specific recording in public sources.

**Further source-level CKMS detail:** official CKMS page embeds two YouTube items for “Lyden Ud” with video IDs VERqyrWMY8A (introduction) and XKU52gWaKRU (teaser). Fetching the embed pages was throttled; retain IDs as source links, not as proof of full workshop recordings. The “Grønne planter” article (lines 94–99) explicitly says participants collected environmental audio on phones, processed it and transferred it to plants with microchips. The current sound-group page says “Det Åbne Ensemble” and “Lyden UD” are interactive, user-involving workshops, with participants making music/sound art and recording/editing sources. Roskilde Festival describes the ensemble as an orchestra of people using psychiatric services and confirms a 4 July 2026 performance; no archival capture located.

**Next phase:** international high-yield entries from the user's list. Begin with La Colifata (Borda Hospital, Buenos Aires) because it is a patient-run radio platform with potential music recordings; then Bethel House (Urakawa, Japan), Workman Arts (Toronto), Fountain House / Gallery (New York) and Gugging (Austria). For each, look for specific audio objects and original participants, not merely visual-art collections, performances or commissioned projects. Do not infer music-making from an organisation's name or mission.


### Phase 13 milestone 3 — first international peer-run recording cases (2026-11-15)
**La Colifata (Buenos Aires):** official archive confirms *Viva La Colifata* (2005), 20 pieces of member-generated songs/poetry/improvisations mixed with Manu Chao's backing (CONTEXT due fame/publicity); the more promising less-visible *Spot Colifatos* is a separate set of jingles/radio-art pieces explicitly created by members. *Rompiendo Muros* is spoken microprogrammes, not automatically music; *Siempre fui loco* mixes La Colifata audio with music by twenty Barcelona street bands. Detailed entry in leads; no audio auditioned.
**Urakawa Bethel House (Japan):** high-priority participant-authored CD project by Papipupepo Orchestra, 22 tracks; 56 singers/players incl. 38 members with lived experience, most songs written by members. Recording completed Feb. 2013; release planned June 2013, but actual issue/title/label not verified. Official FY2012 report confirms original team-authored songs and weekly music team. Detailed entry in leads.
**Workman Arts (Toronto):** verified independent blog recordings of Bruised Years Choir live at Workman Arts Main Hall, Long Winter 7.5, 29 March 2019: “Trouble in Mind” and “We Are the Champions,” two MP3s linked from Mechanical Forest Sound; automated fetch returned 403. These are member-group arrangements/covers, not original compositions. Workman Arts also documents 2025 *Lingering Echoes* sound-art works from Sounding Spaces course; individual item playback and provenance require checking.
**Next exact tasks:** (1) confirm Papipupepo CD issue and locate physical/digital tracklist; (2) extract La Colifata Spot Colifatos SoundCloud set metadata; (3) identify other Workman Arts member recordings, not only choir covers; (4) continue through user list: Bethel House, Workman Arts, La Colifata now screened; next New York Fountain House/Gallery, Gugging, KAOS (already in leads), Creativity Explored/Creative Growth only if they have sound/audio outputs, then other countries. Maintain distinction between music and spoken audio, participant-made and visiting/collaborative production, and public events vs surviving recordings.
**Repository:** La Colifata leads commit `834de96705cf9216079ac2827ae4cafa737bc492`; Bethel + Workman leads commit `3a80ba7a43712cba30352f49723ee531df881ba9`; corresponding logs `10b438f23fc06fd8d8b4ae210b0ad4110eeaed60` and `b5443fe000fa12475648b4f366cfa983790da6eb`. Latest research_method checkpoint before this update `7013f0c4f3d6a1fd23f8cfefe23212f034618ddb`.
No audio audition, participant contact or rights clearance made.


### Phase 13 milestone 4 — Creedmoor and further visual-art studio screen (2026-11-15)
**Creedmoor / DSM5:** added Issa Ibrahim's 2004–2009 ward-recorded solo corpus and DSM5's *Insanity Never Sounded So Good!* (10 songs; recorded Creedmoor summer 2011; issued spring 2012). First-person press kit describes secret Fostex 16-track recordings in locked-ward bathrooms/bedrooms; NPR transcript corroborates a CD recorded in his room in 2004. His 2004/2007 CDs are likely direct ward artefacts; the 2012 *Asylum Years* compilation covers 2004–2011 and must be crosswalked rather than assumed wholly institutional. Latest lead commit `d81e2629c26f29a62bad6edf3038450220538d7f`.
**Creative Growth (Oakland):** found a concrete 2025 collaborative record, *Peace Makers in the Summer Time* by Creative Growth artist William Scott and BJ Armour of Studio Route 29, with facilitator/producer Hop Peternell. Scott's side contains four tracks; the record's credits state sessions at Creative Growth and Studio Route 29. The official 2026 *Stereo Dynamic* exhibition promoted Scott's original song live and linked to the Bandcamp album. PROMISING participant-authored collaborative recording; no audio auditioned. Need preserve co-composer/producer credits and distinguish William Scott's side from BJ Armour's.
**Bethlem Gallery:** official annual review documents “Bethlem Voices” (sound recording including voices from the Bethlem community) and “meet me where I am” (audio book of listening experiments co-created with nine contributors). These are spoken/listening works, not verified music; context/sound archive route only. No music candidate admitted.
**Hospital Rooms:** surfaced a “Sound and Colour” workshop at Walton Ward (five service users and four NHS staff) exploring music, sound, colour and emotion, but no recording or participant-authored track identified. Context only.
**Gugging:** searches surfaced musical homages and sound works by outside musicians inspired by Gugging artists (e.g. *The Gugging Album*, David Bowie/Eno's *Outside* influence, later site-specific compositions). No resident-created audio recording was identified in this pass. Do not conflate music inspired by artists with music made by them.
**Creative Growth additional note:** its public archive's audio descriptions are accessibility narrations, not music. Its 2026 “Stereo Dynamic” exhibition does include live music and collaborations; only William Scott's 2025 album has been admitted so far.
**Next:** locate William Scott/BJ Armour session tapes and any earlier Creative Growth music recordings; confirm whether the 2005/2007 Creedmoor solo CD tracklists can be recovered; extract La Colifata SoundCloud track metadata; continue remaining high-yield list entries (Dragon Café, Project Ability, Everybody Arts, Workman Arts already screened, KAOS already screened, Fountain House, etc.).

### Phase 13 milestone 5 — Creative Growth record identified; negative screens logged (2026-11-15)
**Creative Growth:** admitted *Peace Makers in the Summer Time* (2025), an eight-track collaborative album by Creative Growth artist William Scott and Studio Route 29 artist BJ Armour, produced with facilitator Hop Peternell. Scott's four-track side is co-composed with Peternell; Scott improvised vocals and gave sound direction. Sessions were at Creative Growth and Studio Route 29; preserve dual location and separate Side A/Side B credits. Status PROMISING, not obscure unknown: limited indie release and niche distribution. Lead commit `c16c02e363eafd1a2bd20b3da87a53c95a26cedb`.
**Negative/context screens:** Bethlem Gallery's “Bethlem Voices” and “meet me where I am” are sound/spoken/listening works, not music; Hospital Rooms' Sound and Colour workshop has no identified recording; Gugging searches surfaced outside musical homages, not resident-made recordings; Creative Growth audio descriptions are accessibility narration, not music. These null results are in coop.log.
**Repository:** Creedmoor / DSM5 lead commit `d81e2629c26f29a62bad6edf3038450220538d7f`; Creedmoor log `28a5e23cdfc640a475d24e3024c8a2dae8a1f9f4`; Creative Growth log `ba3c9931cf48e0d7a7b4f6ecbec66588708ae492`; current method checkpoint `4a8e8f4277dd467f4f8e37aa1d85b16eb1bd921e`.
**Next:** (1) confirm Papipupepo Orchestra 2013 CD issue/tracklist; (2) obtain *Square Roots* and *Cosmic Knockout* Creedmoor-era tracklists and map recording dates; (3) trace La Colifata *Spot Colifatos* track metadata; (4) investigate Dragon Café, Project Ability and Everybody Arts only for concrete member-made audio; (5) search Studio Route 29 for other disability-led releases and Creative Growth archive for older music works.


### Phase 13 milestone 6 — Dragon Café album; UK creative-space screen (2026-11-15)
**The Dragon Café / Mental Fight Club:** added *In This Circle Is My Heart* (July 2025), 12 original songs written collaboratively by The Dragon Café Singers between 2016–2025, recorded at 9M Studios. Vivien Ellis's first-person track notes identify patron contributions by Daniel O'Byrne and Sionie to “Roots,” “Finding Our Way,” “Ballad of The Dragon Café” and “At The Dragon Café”; separate attendee-authored “Windrush: The Story of Cordelia” is a further audio lead. The Café is open to all; don't infer that all singers/patrons have psychiatric histories. PROMISING collaborative community song corpus. Lead commit `51425404cf34b8886d4c56fad4b8d33b6e552dca`.
**Everybody Arts:** screened *Halifax: The Town That Is* (2026) vinyl; it is a sound-art commission by Andy Abbott and Michael Powell with local resident conversations, field recordings and original music by Abbott, but no evidence that contributors were Everybody Arts members or people with lived experience. CONTEXT only.
**Project Ability:** official programme is visual arts; no specific member-created music/audio object found, despite broad charity objects mentioning music/film/sound. Null result logged.
**Next:** identify Dragon Café album's full digital metadata and rights, seek the actual recording of “Windrush: The Story of Cordelia” and earlier CD mentioned in Vivien Ellis's 2019 blog; investigate Studio Route 29's wider catalogue (including earlier disability-led albums); continue list screening for Art4Space, Arty-Folks, Creative Start, Submit to Love Studios, Venture Arts, ActionSpace and Recovery Café projects only where audio evidence exists.


### Phase 13 milestone 7 — Studio Route 29 / Beauty Music catalogue expansion (2026-11-15)
**New release:** BJ Armour, *mooooons/aspirations* (29 Nov. 2023), six-track EP on Beauty Music. Track pages credit lyrics/vocals to Armour and production to Hop Peternell and Armour. This is a verified artist-led recording, PROMISING small-label release. Studio Route 29's official site describes Beauty Music as a music studio practice, collaborative recording project and label centering artists with intellectual/developmental disabilities. New lead commit `4add4ecb63dcac2a57c08ef16b7a0e69260de737`.
**Additional routes:** Beauty Radio is a live internet stream mainly of music selected by artists and staff, with plans for interviews and artist audio; not yet an archive of original songs. “Greenwood: The Musical” (24 Apr. 2026) by Ira Karp (performer with Down Syndrome) is an original musical performance hosted at SR29; no recording found. A 2023 report documents BJ Armour performing three pre-recorded original songs he wrote with audio assistance from Hop Peternell, not yet matched to EP tracks. A June 2026 flexi single “If My Love Is a Clock” is by facilitator Hop Peternell, so exclude as participant-made music.
**Next:** identify session locations/dates for each BJ Armour track; crosswalk 2023 performance songs; determine whether Beauty Radio has archived episodes; seek a recording of Greenwood; continue screening Art4Space, Arty-Folks, Creative Start, Submit to Love Studios, Venture Arts and ActionSpace. Keep all credits and participant provenance explicit.


## Phase 13 milestone 8 — Thorvaldsen / Rooster Music and peer-space screen (2026-11-15)

**Current phase:** peer-run / lived-experience creative environments; move from organisation discovery to item-level archive recovery.

### Completed this run
- Read this checkpoint first, then `method.md`, `environment-leads.md` and `coop.log.md`; continued Phase 13 rather than restarting earlier work.
- Identified the strongest new Danish archive route: Netværkstedet Thorvaldsen's Rooster Music is explicitly documented in a Copenhagen municipal record as a member recording studio and music publisher where members record and release music with professional producers. The same source documents member music instruction, studio-technique courses, concerts and tours. The centre's own site describes itself as 100% user-run and without therapeutic/pedagogical staff. No actual release or catalogue has yet been identified.
- Refined Maskine Maskine Amager: the official resources page divides its archive into MMANYT, MMAtalks, MMAfilm and MMusik; MMusik contains dated filmed performances from 2020 onward. The archive is verified, but participant/artist provenance is not; do not assume every act at the venue is member-created.
- Screened Fountain House Gallery, Submit to Love Studios, Arty-Folks, Art4Space and Creative Start. No qualifying music recording surfaced in the public material reviewed. Creative Start's Underdog Arts podcast is spoken discussion, not music. These are scoped null/context findings only.
- Added evidence and next steps to `environment-leads.md` (commit `3dd526facef52ca539983fcd451634c0681770ac`) and `coop.log.md` (commit `9b1d6371cd1108c0dc9cdbcea4e95a478144e33e`).

### Evidence boundaries
No audio was auditioned; no organisations or participants were contacted; no rights/consent permissions were obtained. Municipal/official descriptions prove the existence and stated purpose of a recording programme, not the identity or survival of any particular master. MMusik venue footage is not automatically participant-made music.

### Next exact work queue
1. Trace actual Rooster Music member releases: search historic site snapshots/publications, local library/municipal records, RadioTi schedules and Kanal 1 listings; seek catalogue/artist/title/format/date evidence.
2. Itemise MMusik videos, identify each act's own discography/biography and establish membership or participant relationship independently.
3. Resolve whether Papipupepepo Orchestra's planned 22-song 2013 Bethel House CD was issued; search Japanese-language local press, label catalogues and member/community sources.
4. Extract the official La Colifata Spot Colifatos SoundCloud set into exact item metadata; separate music/jingles from spoken spots.
5. Continue remaining peer-run studio list where there is a plausible audio trail, and maintain a country/language matrix. Do not add generic organisation records as music candidates absent a sound object.

**Continuation instruction:** read this file first on the next run, then the method and canonical lead/log files. Resume at task 1 above. Do not repeat the already completed screens unless new evidence appears.


### Phase 13 milestone 9 — Bethel and La Colifata item-level follow-up (2026-11-15)

- Exact Japanese searches for ぱぴぷぺぽ楽団 and the two reported song titles did not establish that the planned 22-song Bethel CD was actually issued. The 2013 report and FY2012 report confirm the member-led orchestra, original songwriting/performance and a recording project with 56 participants (38 members plus staff/supporters); no later catalogue, label or extant CD identified. Maintain as PROMISING / release archive hunt, not a confirmed released album.
- Opened La Colifata's official podcast page and followed the Spot Colifatos SoundCloud embed. The official page explicitly calls it member-created jingles, spots and radio-art; the official SoundCloud endpoint is https://soundcloud.com/radio-la-colifata/sets/spots-colifatos . The player yielded no item metadata. Exact tracklist, dates, duration, creator credits and music-vs-spoken classification remain unknown.
- Updated `environment-leads.md` (commit `d910062f37458d48880ddc459d503ee99e45a71f`) and `coop.log.md` (commit `b0b2562db80bc6b8b8b93d0af56dadabead2ea66`). No audio auditioned, contact or rights request made.
- Next work: recover the Rooster Music catalogue; identify Maskine Maskine performers' relationship to the centre; continue the remaining international peer-run studio list and preserve exact null-screen boundaries.


## Phase 13 milestone 10 — Thorvaldsen / RadioTi corpus scale and Rooster label audit (2026-11-15)

### Completed
- Read this checkpoint first and resumed from the exact Rooster Music / Maskine Maskine queue.
- **Major Thorvaldsen discovery:** Copenhagen Municipality's 2020 budget-process evaluation (describing c.2019–20) records c.120 members, a professional music studio, three employees sharing 1.5 FTE, about 15 music-production sessions per week across nine weekday studio hours, a long waiting list, and member-formed groups using the rehearsal room. A handful of members produced RadioTi programmes spanning reportage, music and debate, usually broadcast in evenings. This establishes a substantial sustained member music-production ecosystem, not merely an occasional workshop. Source: https://www.kk.dk/sites/default/files/agenda/9f0a4187-0249-41c3-9030-be87548163a2/7b989b43-bb70-4609-a131-4dabf22ecdac-bilag-6.pdf pp. 16–18.
- Historical evidence: 2006 municipal evaluation says music project and RadioTi were among the most popular activities; LAP memorial says RadioTi began broadcasting Aug. 1993 and Rooster studio was built after the 1996 expansion, with three professional producers; another municipal grant table says user-run RadioTi grew from 3 to 33 broadcast hours/week. Sources logged in `environment-leads.md` and `coop.log.md`.
- **Rooster Music label caution:** Presto lists Niels Andersen, *En Blandet Landhandel* (2014; cat. 484829) and The Copenhagen Jazzharmonics (2012; cat. 484831) under a label named Rooster Music; Amazon lists a 2011 Copenhagen Jazzharmonics single under tunecore / Rooster Music. No evidence links this label imprint to Thorvaldsen's studio. Treat as unresolved name collision, not a confirmed candidate.
- Maskine Maskine MMusik list expanded to eight dated venue recordings (2020–25). Still no member/performer relationship verified; venue archive is not automatically participant-made music.
- Dragon Café: Bloomsbury Festival listing confirms a new song “Isolation” was performed 10 Oct. 2026 alongside album tracks; no separate recording/release verified.
- Updated `environment-leads.md` (commit `72a254f246c31b2b3c259b5fc595057f616a30fd`) and `coop.log.md` (commit `829af730d8402f44f7588c733e59974cd366698a`).

### Evidence boundaries
No audio auditioned, no contacts made, no rights cleared. The municipal report is a programme description, not a catalogue. Label name similarity is not proof of common ownership. MMusik videos document venue events, not necessarily member-made work. Dragon Café “Isolation” is documented as a live performance only.

### Next exact queue
1. Prioritise RadioTi archive recovery: search programme schedules, radio station listings, broadcast tapes, playlists, old Radioator/Radio 10 documentation and station frequencies; investigate whether any sound archive is held by Thorvaldsen, volunteers, local-radio archives or municipal repositories.
2. Investigate Rooster Music label-owner, producer, ISRC/UPC and distributor metadata for catalogue 484829 / 484831; do not attach to Thorvaldsen until confirmed.
3. Search old Thorvaldsen newsletters / MMANYT-equivalent publications for named member artists, releases, concerts and tours by Thorvaldsens talrige talenter.
4. Identify MMusik acts' relationship to Maskine Maskine membership; distinguish invited acts, member acts and collaborative ensembles.
5. Verify whether Dragon Café's “Isolation” has a studio recording, and continue track-level metadata work on *In This Circle Is My Heart*.

**Continuation:** read this checkpoint first, then `method.md`, `environment-leads.md`, `coop.log.md`. Resume at task 1; don't repeat the completed screens.


## Milestone 11 — RadioTi broadcast-archive recovery (2026-11-15)
**Current phase:** Phase 13, peer-run music environments — Thorvaldsen / RadioTi archive research.

### Work completed
- Re-read the persistent checkpoint first, followed by the canonical method, candidate register and log. Continued the saved exact task: recover RadioTi programme/archive leads.
- Confirmed from RadioTi's official site that it is a non-commercial 92.9 MHz FM / online station started in 1993 by and for people with psychosocial disabilities, open to others. The site explicitly invites programme contributors and technical volunteers, and lists music production, multimedia and electronic communication among possible activities. Recent programme types include listener poems, songs and stories, radio drama and sound montages.
- Found the current programme grid, including “Det handler om musikken” (portraits of Danish underground musicians), “Sunlight” (Indian music, Punjabi folk and fusion), “Radio Uden Smag” and “Radio Guldkorn.” These are broadcast/discovery programmes; member authorship is not established.
- Found Frederiksberg association documentation and a Copenhagen municipal grant spreadsheet describing RadioTi as user-run / volunteer-run and giving 35 broadcast hours per week for 2023–24. This supports the scale of the station, not provenance of every broadcast.
- Identified Radioator as a related but distinct youth-radio programme that broadcast on RadioTi after an earlier period on Sokkelund Radio. Its website preserves 422 audio files, including 23 jingles and 33 “Musikupdate” segments. The latter are spoken music-news updates, not original music. No evidence links Radioator's output to RadioTi members; do not merge the two archives or treat Radioator as a qualifying participant-music candidate. Radioator's site prohibits reuse without permission.
- Identified Royal Danish Library radio/TV collection as a practical archive route: it holds DR, TV2 and selected periods of other Danish channels; pre-2006 material may survive on reel-to-reel tape/VHS, but locating a non-digitised programme requires broadcast date/time. DR-arkiv is for DR, not RadioTi. No RadioTi accession/holding has yet been confirmed.

### Evidence / editorial assessment
RadioTi remains a HIGH-PRIORITY archive hunt, not yet a verified recording candidate. It has a documented user-run history, a broadcast platform and explicit music-production / listener-song pathways. The crucial missing step is a dated, extant item whose creator, performance and relation to the community can be established. Separate original member compositions and jingles from licensed music, guest performances, syndicated content and spoken radio.

### Repository changes
- environment-leads.md appended with a dated RadioTi / Radioator archive-recovery note and sources. Commit: 76d73409e781f65cba7aa2fb647c50adfbf504d2.
- coop.log.md appended with the search process, findings, boundaries and next tasks. Commit: a167cb01a9ef4e004fe4c677a580953fe9d152e7.

### Next exact task
1. Inspect historical RadioTi programme grids and archived website snapshots for named member-produced programmes and dated broadcasts.
2. Establish which non-DR channel periods the Royal Danish Library collected and whether RadioTi is represented; use historic local-radio schedules to identify dates/times before requesting any specific item.
3. Search for surviving station tapes in Thorvaldsen, Galebevægelsen, LAP, volunteer and local-radio association collections, without contacting anyone unless authorised.
4. Keep Radioator as a separate contextual small-web archive.
5. Once this route is adequately exhausted, resume the other saved Phase 13 queue (Rooster Music label attribution, MMusik artist provenance, Dragon Café “Isolation”) and then international peer-run music spaces.
**No contact made, no audio auditioned, no restricted archive accessed, and no reuse permission obtained.**


## Milestone 12 — RadioTi / Rooster Music primary cross-link and broadcast archive boundaries (2026-11-15)
**Current phase:** Phase 13 — peer-run music environments; Thorvaldsen / RadioTi.

### Work completed
- Established a direct municipal record linking RadioTi with Thorvaldsen and Rooster Music: Copenhagen's 2013 grant record lists RadioTi, c.40 participants and 25 volunteers, and explicitly describes close collaboration with both the centre and studio.
- Located a 2015 first-person CV by co-founder Erik Olsen describing Rooster Music as a studio where service users produce their own music. The CV dates RadioTi's co-founding to 1992; RadioTi's official site and LAP memorial give 1993 as start/on-air date. Preserve the distinction as a possible founding vs first-broadcast discrepancy.
- Reconfirmed production scale in a 2019–20 municipal evaluation: c.15 studio production sessions weekly, nine weekday studio hours, three staff sharing 1.5 FTE, long waiting list and member rehearsal groups; some members also made RadioTi reportage, music and debate programmes.
- A 2020 municipal grant overview describes RadioTi as 100% volunteer-run, with c.40 participants and c.20 volunteers monthly, and says the project had existed for 27 years.
- Found a third-party programme directory listing Radio Kiks, Radio Dunst, Amalies Time, Sunlight, Mandags Salonen, Onkel Oles musikportrætter and other programme titles/presenters. Treat as search terms, not authoritative programme history.
- Found a 2009 Venice band blog advertising a guest interview and song premieres on Radio Kiks on 12 June 2009, 20:00–22:00. This is an external band's promotional broadcast, not participant-created music; the date is outside the Royal Danish Library's local-radio week-46 sample window.
- Clarified Royal Danish Library policy: it says it collected local-radio and local-TV broadcasts during week 46 each year from 1988, but its current detailed radio-channel list does not list RadioTi. An annual sample is a possible route, not proof of any RadioTi holding. No accession or item is confirmed.
- Rejected a 2017 “MonsterMix” co-production mention as evidence: the applicant was Radio Helsingør and the text was conditional on Radio Ti separately obtaining permission.

### Editorial conclusion
The **organisational link** between RadioTi and Thorvaldsen's Rooster Music is now documented by municipal evidence; the earlier concern about conflating two unrelated organisations with similar names is resolved at that level. However, the two Presto catalogue releases under the generic Rooster Music imprint remain unlinked to this studio. RadioTi / Rooster Music is a **HIGH-PRIORITY documented participant-led production and broadcast environment**, but still not a verified release-level candidate until a specific member-created recording is identified and its provenance recorded.

### Repository changes
- `environment-leads.md` expanded with the municipal cross-link, founder testimony/date discrepancy, production scale, programme leads, dated guest broadcast and national archive sampling caveat. Commit: `db86cd035b0f48fc8205732c4343c787e018de73`.
- `coop.log.md` appended with search scope, sources, exclusions and next steps. Commit: `a0fbfeecea00439d138e46dc0b22a2e4be0fd554`.

### Next exact task
1. Find historic RadioTi programme schedules, newsletters and annual reports, especially the programme titles listed by the third-party station directory.
2. Determine whether any Royal Danish Library week-46 local-radio sample contains RadioTi; the public channel list does not identify it.
3. Trace the studio's output through named artists, producers, catalogues, ISRC/UPC and old concert programmes; keep generic Presto label hits unassigned until corroborated.
4. After a bounded RadioTi archive pass, return to the remaining Phase 13 tasks: MMusik member provenance, Dragon Café “Isolation,” and further peer-run recording studios.
**No contact made, no audio auditioned, no restricted archive accessed, and no reuse rights obtained.**


## Milestone 13 — Maskine Maskine MMusik catalogue and provenance triage (2026-11-15)
**Current phase:** Phase 13 — peer-run music environments; next inspect MMANYT and Tudeprinsen/Fiskprinsen provenance.

### Work completed
- Opened the official MMusik resource page and the individual linked item pages. Confirmed that this is an extant venue-produced audiovisual archive with dated item pages, not merely a list of events.
- Verified individual MMAfilm records for Tudeprinsen (2 Feb. 2024); Love Against The Machine Allstars (same date); A + band performing “My Heart Will Go On” (2 July 2024); Farmand (same date); the 31 Jan. 2025 changeover/farewell event; Nicolaj Agerholm's Tudeprinsen cover (13 Oct. 2023); Nicolai Agerholm performing Tudeprinsen songs (6 June 2023); and El Ray at the official opening (4 Sept. 2020).
- Identified **Tudeprinsen / Fiskprinsen** as the highest-priority provenance lead: a 2025 Folkemødet listing names “Fiskprinsen (formerly Tudeprinsen), Maskine Maskine Amager.” This indicates an artist/centre association but does not yet prove member status, songwriting authorship, identity or whether other recordings exist. Preserve pseudonym/alias and do not attempt private identification.
- Established that El Ray is an already documented Copenhagen surf-rock band and Farmand a Copenhagen punk band with external appearances; no evidence links either to MMA membership. Treat their MMusik videos as visiting performances unless new evidence changes the attribution.
- Kept A + band anonymised; the recorded item is a cover of “My Heart Will Go On,” not evidence of original composition. Love Against The Machine Allstars remains unclassified pending performer credits.
- Identified MMANYT (2019–22, four seasons; first two seasons also published as MMApress books) as a potentially useful parallel source for member/band biographies. The official site says it was written by Søren Dixen and included material beyond MMA, so it cannot alone establish participant authorship.
- YouTube embedded pages were throttled; no audio/video was auditioned. Only official page metadata and item embeds were verified.

### Editorial assessment
MMusik is a VERIFIED venue-produced audiovisual corpus, but it is not automatically a participant-made music corpus. Tudeprinsen/Fiskprinsen is a HIGH-PRIORITY provenance lead, not yet a confirmed candidate recording. Guest bands and covers remain distinct categories.

### Repository changes
- `environment-leads.md` expanded with individual MMusik item pages, Tudeprinsen/Fiskprinsen provenance lead, visiting-act exclusions, MMANYT source route and audition/access caveat. Commit: `4cec8a35e10a337e9fa497355dc70326e54850de`.
- `coop.log.md` appended with the source review, evidence boundaries and next tasks. Commit: `1dbbe6324b652d7f20ac0996a7f570796a94e365`.

### Next exact task
1. Inspect MMANYT Seasons 1–4 (especially 2019–22) for Tudeprinsen/Fiskprinsen, Nicolai/Nicolaj Agerholm, Love Against The Machine and other named MMusik performers; capture exact issue/page citations and distinguish centre members from guests.
2. Search for original Tudeprinsen/Fiskprinsen releases, demos, home recordings and other live tapes, keeping artist alias and membership evidence separate.
3. If no specific member-created recording is established after a bounded pass, return to Dragon Café “Isolation” and other peer-run studios.
**No contact made, no audio/video auditioned, no restricted material accessed, and no reuse rights obtained.**


## Milestone 14 — MMANYT bounded audit and Dragon Café recording provenance (2026-11-15)
**Current phase:** Phase 13 — peer-run music environments. RadioTi archive work and MMusik catalogue triage have been bounded; Dragon Café recording corpus now has stronger item-level documentation.

### Work completed
- Attempted the saved MMANYT Seasons 1–4 search. Official page establishes fortnightly PDF issues from Jan. 2019 through part of 2022, three complete seasons plus half of Season 4, with Seasons 1–2 also issued as MMApress books. However, the web-extracted page exposes only the season descriptions, not the issue full text; searches for Tudeprinsen/Fiskprinsen, Agerholm and Love Against The Machine returned no indexed full-text matches. A national bibliography record confirms Season 1 was a 178-page 2019 volume (ISBN 978-87-93859-00-5). Mark as bounded but incomplete; full audit requires access to the books/issues.
- Found an independent RUST booking (17 Apr. 2025) listing Fiskprinsen as support, and a DDEA/Folkemødet listing calling Fiskprinsen “formerly Tudeprinsen” and associating the act with Maskine Maskine Amager. This strengthens the alias and external booking trail but does not prove member status, songwriting or a release. Lower obscurity priority; do not infer personal identity from profile aggregators.
- Advanced Dragon Café metadata: In This Circle Is My Heart – Songs from The Dragon Café is a 12-track, 50-minute album released 2 July 2025, with full tracklist and durations now recorded in environment-leads.md and coop.log.md.
- Identified “Southwark Rebel Women” as a discrete collaborative song written and recorded during lockdown in 2021. Resonance FM's contemporaneous credits name choir/leader Vivien Ellis and songwriter Daniel O'Byrne as collaborators, guest soloists Victoria Couper, Clemmie Franks, Frankie Armstrong, Sally Davies and Gina Foster, and Glenn Keiles as recording/arranging/producing/mixing engineer. The track is 7:02 on the 2025 album.
- Southwark Council documents a 16 Feb. 2026 live performance of “Southwark Rebel Women.” Bloomsbury Festival / Mental Fight Club document a new song “Isolation” performed on 10 Oct. 2026; no studio recording/release of “Isolation” found.
- Editorially, Dragon Café is a VERIFIED participant-collaborative recording corpus, but its 2025 album is publicly distributed; it is better treated as context / promising for collaborative authorship than as an undiscovered recording. Do not reduce singers to diagnostic identities. “Isolation” remains live-performance evidence only.

### Repository changes
- environment-leads.md appended with MMANYT bounded-search result and external Fiskprinsen booking. Commit: 5d19feef13f08c4c4331ff1a67a772a1a6013f63.
- coop.log.md appended with MMANYT search boundary, full Dragon Café tracklist, Southwark Rebel Women credits, 2026 performance and status. Commit: 3b2df650472f3a82bb1c56b859fbd1a25970dea0.

### Next exact task
1. If access to the MMANYT books / PDFs can be obtained without contacting anyone, inspect actual issue contents for artist/member status and music leads; otherwise treat the public-web pass as bounded and don't claim a full audit.
2. Search the Dragon Café Singers' earlier recording history (including the reported Finding Our Way album and the 2017 “Drive The Cold Winter Away” recording) for item-level metadata, exact dates, participants and provenance; keep album/track masters and permissions distinct.
3. Then continue to the next unexamined peer-run music environments from the user's supplied list, prioritising those with extant participant-created recordings or studio/radio archives, not visual-art-only spaces.
**No contact made, no audio auditioned, no restricted material accessed, and no reuse permission obtained.**


## Milestone 15 — Dragon Café first album and original-song chronology (2026-11-15)
**Current phase:** Phase 13 — peer-run music environments. MMANYT full-text access remains unresolved; Dragon Café archive history is now documented at album and song level.

### Work completed
- Charity Commission annual report for year ended 30 April 2020 confirms The Dragon Café Singers had already recorded a first album, *Finding Our Way*, with 10 professionally produced songs written and performed by the singers. Exact release date, tracklist, label, catalogue number and recording location remain unknown. This is distinct from the identically titled song on the 2025 album.
- Vivien Ellis's 2025 first-person account says the 12-track album *In This Circle Is My Heart* was recorded at 9M Studios in Southwark and that its songs were collaboratively written between 2016 and 2025. Song chronology now captured: “Finding Our Way” (first co-written song with café patron Daniel O'Byrne; performed 2016); “When Icicles Hang By The Wall” (2016); “Drive the Cold Winter Away” (2017, adapted Elizabethan carol melody); “Music to Hear” (2018 Shakespeare Sonnet 8 setting); “Roots” (2019, Daniel O'Byrne helped shape; Helen McDonald soloist); “Southwark Rebel Women” (written/recorded virtually during 2021 lockdown); “Here and Now” (2022, 10th anniversary); “Ballad of The Dragon Café” (2024, patrons Sionie and Daniel helped write; 100+ verses distilled).
- Cross-checked “Southwark Rebel Women” with Mental Fight Club's 2021 review and contemporaneous Resonance FM credits: group and Vivien Ellis wrote/recorded in March 2021 with Team London Bridge; Daniel O'Byrne collaborated; guest soloists named Victoria Couper, Clemmie Franks, Frankie Armstrong, Sally Davies and Gina Foster; Glenn Keiles recorded, arranged, produced and mixed. Track duration on 2025 album: 7:02.
- Mental Fight Club's 2024 report describes the second song in an anniversary trilogy as a 100+ verse, two-act history of the café from participants' points of view; Ellis identifies it as “Ballad of The Dragon Café.” The report also documents a long-time attendee's self-written *Windrush: The Story of Cordelia* performance; no recording known.
- Status: Dragon Café is a VERIFIED participant-collaborative recording corpus, with at least two album projects and original song history dating to 2016. The material is publicly released, so it is context / collaborative-authorship documentation rather than a hidden-recording priority. Preserve distinction among patrons, choir lead, invited soloists and studio personnel. No audio auditioned and no reuse permission obtained.

### Repository changes
- `environment-leads.md` appended with first album, 2025 studio location, song chronology, production credits and Windrush performance lead. Commit: `42bbaba7a41f352f84ca441980cf89d285046e87`.
- `coop.log.md` appended with archive search, chronology, source comparison and status. Commit: `35193c0f213b92f78068a3e7e45119e60f4c3c0d`.

### Next exact task
1. Search for physical/catalogue metadata and tracklist of the first *Finding Our Way* album; distinguish it from the 2025 track with the same title.
2. Resume the supplied peer-run environments list, prioritising places with documented recording studios, radio stations, self-produced cassettes, albums or digital archives; do not treat art-only programmes as music candidates.
3. If practical, obtain MMANYT Seasons 1–4 or their underlying PDFs for a full-text artist/member search; the public web extraction did not expose their contents.
**No contact made, no audio auditioned, no restricted material accessed, and no reuse rights obtained.**


## Milestone 16 — Dragon Café first CD date and broadcast trace (2026-11-15)
**Current phase:** Phase 13 — peer-run music environments; Dragon Café recording chronology now extends to the first CD.

### Work completed
- Vivien Ellis's 27 Dec. 2019 first blog post says the Dragon Café Singers recorded a CD “last year,” narrowing the first *Finding Our Way* album's recording to 2018. This aligns with the 2019/20 Charity Commission report confirming the 10-song professionally produced first album. Exact release date, label, catalogue number and full tracklist remain unknown.
- The 2019 post identifies “Drive the Cold Winter Away” as the first track and links a SoundCloud stream. Ellis says it was written for the 2017 Globe Concert for Winter, adapting a sixteenth-century ballad melody with new lyrics about love, food and community and a samba rhythm. SoundCloud was not accessible to inspection; no audio audition claim. The relationship between this linked audio and the 2025 album version is unresolved.
- The 2020/21 Charity Commission report records a Great Get Together / Southwark Community Festival radio broadcast that included “Finding Our Way,” but gives no station, date or programme. Treat as a broadcast trace, not an identified archive object. The report separately notes “Southwark Rebel Women” on Resonance Radio on 8 March 2021.
- The 2025 album chronology, 2021 track production credits and 2024 participant-authored anniversary ballad remain as recorded in Milestone 15.

### Repository changes
- `environment-leads.md` appended with first CD recording year, SoundCloud track pointer and undated broadcast trace. Commit: `b435346f6adcbe4062cab93e6f40076b7c361a6d`.
- `coop.log.md` appended with source comparison, limitations and next steps. Commit: `040d1959c1c64a580f2fd0164781a0748c8c2ce9`.

### Next exact task
1. Find first-CD artwork/tracklist and any label or catalogue metadata for *Finding Our Way* (recorded 2018; confirmed by 2020 report).
2. Determine whether the SoundCloud “Drive the Cold Winter Away” item is the 2018 CD master or a later recording, without claiming to have listened.
3. Identify the station/date/programme for the Great Get Together broadcast of “Finding Our Way.”
4. After a bounded pass, continue through the remaining user-supplied peer-run music environments with verified audio outputs.
**No contact made, no audio auditioned, no restricted material accessed, and no reuse rights obtained.**


## Milestone 17 — Park Royal *Pine* album and La Colifata catalogue correction (2026-11-15)
**Current phase:** Phase 13 — peer-run / participant-led music environments, extending to documented institutional recording projects. New priority: Park Royal / Finding Rhythms; La Colifata short-form archive remains a separate item-level route.

### Work completed
- Identified *Pine*, a 19-track digital album credited to Finding Rhythms & Park Royal Mental Health Centre, released on Bandcamp 17 Apr. 2025. Bandcamp states every track was composed and recorded at Park Royal Mental Health Centre by participants on Finding Rhythms' 157th project; project musicians Fred Harper and Cleo Savva, mixing/mastering Fred Harper. Full tracklist/durations recorded in `environment-leads.md`.
- CNWL NHS Trust report (12 June 2025) independently establishes context: around 15 service users took part on Pine Ward in a flexible drop-in project during autumn 2024; participants wrote/composed original songs, recorded in a makeshift ward studio with professional musicians/producers; all participants feature on the album, plus a Christmas track including staff. It describes an on-ward listening party. This is VERIFIED participant-created institutional recording / PROMISING, not an unknown release. Preserve participant anonymity and do not infer individual credits.
- Clarified La Colifata's official catalogue. *Rompiendo Muros* is a 1996–97 compilation of 2–4 minute member-produced radio microprogrammes; *Rompiendo Muros II* is a second such compilation; *Viva La Colifata* comprises 20 items of member-generated songs, poetry and improvisations mixed with Manu Chao's musical bases; *Spot Colifatos* is a member-created archive of jingles, spots, “chichas” and radio art.
- Corrected a false-positive: *Siempre fui loco* is a Manu Chao assembly of music by 20 Barcelona street bands with La Colifata microprogramme audio, not an album of songs composed by Borda residents. Official source says about 3,000 copies were sold by the street musicians.
- Preserved the date conflict for *Viva La Colifata*: current official microsite says the two volumes were edited in 2005; contemporary 2009 press coverage dates the launch to July 2009 and says recording/workshops began in 2007. Do not harmonise without further evidence.
- La Colifata's famous Manu Chao collaboration is CONTEXT ONLY for obscurity; *Spot Colifatos* and *Rompiendo Muros* remain PROMISING item-level audio/archive leads. No audio auditioned.

### Repository changes
- `environment-leads.md` appended with verified *Pine* album, full 19-track metadata, NHS provenance and rights caution; La Colifata catalogue split, false-positive correction and date discrepancy. Commit: `60add125d7d86983c3ee28d61fd7a60bfcb3b8c4`.
- `coop.log.md` appended with sources, exact album tracklist pointer, La Colifata distinctions and assessment. Commit: `13f3cdc12f074bc113cf91d3b2579f925af7bd69`.

### Next exact task
1. Inspect Finding Rhythms' broader Bandcamp discography and project pages for other institution/community-made releases, keeping each participant population and setting separate; for *Pine*, record any item-level participant credits, dates and rights language without attempting to identify unnamed residents.
2. Return to La Colifata's SoundCloud/official audio embeds and see whether item-level titles, dates or creators are discoverable for *Spot Colifatos* and *Rompiendo Muros*. Preserve the separation between member speech/music and guest backing tracks.
3. Continue through the remaining user-supplied peer-run environments, prioritising actual audio outputs (e.g. recording studios, bands, radio archives) rather than visual-art-only organisations. Treat Chilli Studios as a promising independent recording-studio lead from the prior literature reference, but verify first-hand output and artist attribution before adding a candidate.
4. Keep the first Dragon Café CD tracklist and Great Get Together broadcast station/date as unresolved lower-priority follow-ups; do not spend further time repeating generic album searches.
**No contact made, no audio auditioned, no restricted material accessed, and no reuse rights obtained.**



## Milestone 18 — Finding Rhythms catalogue as a cross-environment recording archive (2026-11-15)
**Current phase:** Phase 13 — participant-led music environments. Finding Rhythms is now a significant institutional/community recording conduit identified through the Pine Ward lead.

### Work completed
- Expanded from *Pine* to the wider Finding Rhythms Bandcamp catalogue and 2025 annual report. The report (published 20 Oct. 2026) says 199 participants engaged during 2025; 25 group projects (14 custodial, 11 community) involved 151 participants and produced 22 original-music albums. The Peckham studio separately hosted 48 participants in 351 one-to-one sessions.
- Verified the 2023–24 Northwick Park Hospital trilogy (*Hotter Than Water*, *Every Effort Counts*, *Creative Energy*) through Bandcamp item pages and a peer-reviewed 2026 study. Across three projects, 27 Black men experiencing repeated contact with mental-health services created three original albums with professional musicians and NHS psychologists. Do not assume every participant was an inpatient.
- Captured album dates, credits and full tracklists for all three Northwick Park releases in `environment-leads.md`; the Bandcamp pages distinguish “recorded with Finding Rhythms musicians” (*Hotter Than Water*) from “composed and recorded by participants” (*Every Effort Counts*) and “recorded by participants” (*Creative Energy*).
- Logged further adjacent album leads: *Timeless* / *Timeless II* (YMCA Landaid House), *W11* (Rugby Portobello Trust), *Listen To Our Stories* (HMP Bristol), and 2026 releases from Westbourne House Approved Premises and prisons. These require individual item checks before separate candidate records.
- Editorial conclusion: Finding Rhythms is a research conduit / collection-level archive, not one artist or one homogeneous environment. Most albums are publicly released on Bandcamp and are not obscure in strict terms, but the collection provides a rare, unusually well-indexed map of resident- and participant-created music in settings with few recording opportunities. Preserve the distinction between participant composition, performance, recording, and professional production.

### Repository changes
- `environment-leads.md` appended with Finding Rhythms collection-level record, annual statistics, Northwick Park album trilogy and adjacent album leads. Commit: `69fb66d0ee6594e0741e189e3a77e3a212df4084`.
- `coop.log.md` appended with the catalogue search, source comparisons, three album details and editorial assessment. Commit: `4b3470222b271ef8a024e4f6eab10561a57aa62f`.

### Next exact task
1. Inspect other Finding Rhythms albums most relevant to the user's peer/community list, especially YMCA Landaid House (*Timeless* / *Timeless II*), Rugby Portobello Trust (*W11*), and post-release / approved-premises settings; preserve project and participant boundaries.
2. Inspect the La Colifata SoundCloud embeds for item-level titles/metadata in *Spot Colifatos* and *Rompiendo Muros*, using official catalogue descriptions as the classification authority.
3. Resume the original user-supplied peer-run environments list and prioritise actual recording outputs; Chilli Studios remains a literature-derived studio lead to verify.
4. Keep Dragon Café first-CD tracklist and Great Get Together radio station/date as unresolved lower-priority leads; no more generic album searches unless a new specific source appears.
**No contact made, no audio auditioned, no restricted material accessed, and no reuse permission obtained.**


## Milestone 19 — Finding Rhythms residential and probation-transition releases (2026-11-15)
**Current phase:** Phase 13 — participant-led music environments. Continued the Finding Rhythms cross-project archive audit.

### Work completed
- Verified *Timeless* (19 Nov. 2024, 11 tracks) and *Timeless II* (10 Sept. 2025, 12 tracks) by Finding Rhythms & YMCA LandAid House. Bandcamp states both were recorded by participants at the residence; it does not say all tracks were composed by them. YMCA's official site identifies LandAid House as accommodation for young people experiencing homelessness, opened May 2021. This is a community housing setting, not a psychiatric facility.
- Verified *Listen To Our Stories* (HMP Bristol, 17 Apr. 2025, 11 tracks): Bandcamp explicitly says all tracks were composed and recorded by participants at HMP Bristol on project 164, in partnership with Change Grow Live.
- Verified *Our Brighter Future* (Westbourne House Approved Premises, 7 Oct. 2026, 11 tracks): Bandcamp says participants composed and recorded all tracks on project 207. Finding Rhythms' project story says four participants took part over six days / 24 hours in July–August 2026. HM Inspectorate confirms Westbourne House is an Approved Premises, i.e. temporary supervised community accommodation for people on probation after prison release, not a prison or hospital.
- Verified *W11* (Rugby Portobello Trust, 10 Dec. 2024, 15 tracks): Bandcamp says participants recorded all tracks on project 144; page does not explicitly establish participant composition.
- Editorial conclusion: these albums show the Finding Rhythms model crossing custodial, acute mental-health, supported-housing and probation-transition settings. Preserve differences between “composed and recorded by participants” and “recorded by participants”; don't flatten the environments or attribute all production to residents. Public Bandcamp releases are contextual/promising, not obscure masters.

### Repository changes
- environment-leads.md appended with item-level residential/custodial release notes and institutional context. Commit: 686f5495885473b5a54f639d70546c05455fd894.
- coop.log.md appended with the sources and distinctions. Commit: 555910000b1d7c24efc7519b365a1620e5d84449.

### Next exact task
1. Inspect specific 2026 releases on the Finding Rhythms Bandcamp catalogue (e.g. HMP High Down, HMP Woodhill, HMP Channings Wood, London Pathways Partnership) only where the album page provides new setting/provenance information; do not duplicate the whole catalogue.
2. Return to the original peer-run environments list and investigate Chilli Studios as a literature-derived recording-studio lead: find primary project/artist pages and any specific releases, with participant authorship carefully verified.
3. Revisit La Colifata's official SoundCloud embeds for item-level *Spot Colifatos* and *Rompiendo Muros* metadata.
4. The first Dragon Café CD metadata and Great Get Together broadcast remain lower-priority unresolved leads.
**No contact made, no audio auditioned, no restricted archive accessed, and no reuse permission obtained.**


## Milestone 20 — Finding Rhythms prison release sweep and Chilli Studios verification (2026-11-15)
**Current phase:** Phase 13 — participant-led music environments. New archive paths: ten verified 2026 Finding Rhythms prison albums; Chilli Studios' music studio/radio archive and Found Sounds '26 project.

### Work completed
- Audited ten further 2026 Finding Rhythms Bandcamp albums: *The Progressive Regime* (HMP High Down, project 168); *Power Of The Outreach* (HMP High Down, 169); *Pick & Mix* (HMP Woodhill, 171); *Pain Called Life* (HMP Woodhill, 172); *Pros And Cons* (HMP Dovegate, 175); *Made In The Wok* (HMP Brixton, 181); *Locked In For The Summer* (HMP Brixton, 167); *The Memo* (HMP Bristol, 184); *Times Inside* (HMP Portland, 191); *Road To Riches* (HMP Channings Wood, 198). All ten album pages explicitly say tracks were composed and recorded at the named prison by participants. Release dates, track counts and project musician credits are in environment-leads.md.
- Catalogue page also exposes leads at Harrow Adult Mental Health Services, London Pathways Partnership, YMCA LandAid House, Katherine Price Hughes House and other prisons; these remain title-level until each page is checked.
- Chilli Studios is now confirmed as a genuine participant music-recording environment: a 2018 PhD thesis describes its music studio, equipment, professional facilitators, twice-weekly member-led songwriting/jamming and development of member songs into semi-professional recordings. The current official site lists Chilli Radio podcasts with member music and Heads & Tales, a participant-shaped heritage archive. A 2020/21 charity report documents music recording/technical support.
- Found Sounds '26 is a concrete current collaboration led by Chilli Studios with AF Sound Collective, Sound Rooms, Ouseburn Radio and SVP Newcastle. It plans field recording, electronic music creation, Ouseburn Radio broadcast and a short-run cassette. The project page does not yet prove the tape or broadcast has been released.
- Corrected a false positive: Simon Taylor's *Survival E.P* credits a bass part recorded at Chilli Studios, but Taylor wrote, performed, recorded and mixed the work himself. Not a Chilli member-made release.
- Editorial status: Finding Rhythms is a rich modern prison recording archive but mostly public Bandcamp material (contextual, not obscure); Chilli Studios is PROMISING, with its audio catalogue still to be itemised.

### Repository changes
- environment-leads.md appended with ten Finding Rhythms albums and Chilli Studios profile / Found Sounds project / false-positive correction. Commit: 9b03ab9ec181ca96928c297d9a0c50b81c1f454c.
- coop.log.md appended with the source audit and provenance distinctions. Commit: 089fdaaa99f9b3698838a339b3c7810fe324594a.

### Next exact task
1. Inspect Chilli Radio's embedded audio/podcast catalogue, identify actual music items and their makers, and verify whether Found Sounds '26 cassette/broadcast has materialised.
2. Check the remaining Finding Rhythms title-level leads most relevant to peer/community environments: *Stories From Section 2* (Harrow Adult Mental Health Services), *Higher Power* / *Nothing's Undone* (London Pathways Partnership), *Timeless III* (YMCA LandAid House), and *A.P Living 2* (Katherine Price Hughes House). Open only pages that establish useful new provenance; avoid repeating the prison catalogue sweep.
3. Resume La Colifata official SoundCloud *Spot Colifatos* and *Rompiendo Muros* item-level audit.
4. Return to the wider supplied peer-run list for additional documented recording infrastructures.
**No audio auditioned, no contact made, no restricted archive accessed, and no reuse rights obtained.**


## Milestone 21 — Chilli Studios 2016 annual report reveals an unidentified studio album (2026-11-15)
**Current phase:** Phase 13 — peer-led / participant music environments. Chilli Studios now has a verified unidentified album in addition to documented music studio and radio activity.

### New finding
- Opened the original Charity Commission annual report for year ended 31 March 2016. It explicitly lists “1 studio album” among Chilli Studios' achievements and separately records “Chilli Radio: numerous members podcasts” (report lines 339–379).
- The same report records 172 regular member participants and 4,269 workshop participations; it says members could work independently in the studio or join weekly structured workshops including music (lines 449–515).
- The album's title, medium, tracklist, participants, producer, date and authorship are not specified. Thus album existence is VERIFIED, but member authorship/content remain unresolved. Do not assume it was made by members or confuse it with the later Simon Taylor *Survival E.P* (which was his own work with one bass contribution recorded at Chilli).
- “Chilli Seed” in the report is a creative-enterprise start-up model, not a music album.
- Assessment upgraded to HIGH PRIORITY provenance chase: find the album title/copy, credits and participant authorship; also identify member podcast items.

### Repository changes
- environment-leads.md appended with 2015–16 report evidence and album verification status. Commit: 0d3b5d215e31c40bee2dd043060cdf887cf747e1.
- coop.log.md appended with the source audit and revised priority. Commit: 45237f18c83a3ab847493b8b0be77d93441da09b.

### Next exact task
1. Retrieve Chilli Studios Annual Report 2015–16 and contemporaneous Chilli Seed material from Issuu; search for album title, format, tracklist, producer, participants and member rights/consent. Search the report's referenced Chilli Radio podcast corpus and identify actual music items.
2. Verify whether Found Sounds '26 cassette and Ouseburn Radio broadcast have been produced; project page says these were intended outputs but does not establish delivery.
3. Inspect Finding Rhythms title-level leads *Stories From Section 2*, *Higher Power*, *Nothing's Undone*, *Timeless III* and *A.P Living 2* only for new provenance.
4. Continue La Colifata's *Spot Colifatos* / *Rompiendo Muros* item-level audit and wider peer-run list.
**No audio auditioned, no contact made, no restricted archive accessed, and no reuse rights obtained.**


## Milestone 22 — Finding Rhythms, La Colifata and Chilli follow-up (2026-11-15)
**Current phase:** Phase 13 — peer-run / participant-led music environments.

### Work completed
- Audited five Finding Rhythms releases: *Stories From Section 2* (Harrow Adult Mental Health Services credit; recording venue Harrow Arts Centre), *Nothing's Undone* and *Higher Power* (London Pathways Partnership), *Timeless III* (YMCA LandAid House), and *A.P Living 2* (Katherine Price Hughes House). Full tracklists, dates, project numbers and composition/recording distinctions appended to `environment-leads.md`.
- Key correction: *Stories From Section 2* is credited to Harrow Adult Mental Health Services, but its Bandcamp page says participants composed and recorded at Harrow Arts Centre. Do not describe it as ward recording. For *Timeless III* and *A.P Living 2*, pages say participants recorded the tracks but do not explicitly establish participant composition.
- La Colifata: found a 2017 collector's documentation of a physical 22-track *Rompiendo Muros* CD, each microprogramme 2–4 minutes, and official catalogue descriptions distinguishing spoken microprogramme compilations from member-created radio-art *Spot Colifatos*. Official SoundCloud embed yielded no track metadata; direct SoundCloud pages blocked. *Viva La Colifata* is hybrid member-generated songs/poetry/improvisations plus Manu Chao musical bases.
- Chilli Studios: exact Issuu URLs for its 2015–16 annual report and Chilli Seed programme were identified in an academic bibliography, but Issuu pages inaccessible. Official Chilli Radio page confirms podcasts include member music, but its link resolves to a static image, not audio. Found Sounds '26 continues to describe intended cassette/broadcast outputs but no evidence of completed output was located.
- No audio auditioned, no contact made, no restricted material accessed, and no reuse rights obtained.

### Repository changes
- `environment-leads.md` updated, commit `f3e5a52a44a0f610165f10be6334fc500730301f`.
- `coop.log.md` updated, commit `102ab5bbedc6fac7f1e56691f50046306712c7e5`.

### Next exact task
1. Return to the wider user-supplied peer-run environments list; prioritise named music groups, member-recording studios, community radio archives and actual release objects rather than generic arts activity. Search for original artist/member credits and surviving audio.
2. Continue Chilli Studios provenance only if a new route appears (archived Chilli Radio podcast pages, Chilli Collective member portfolio, cached/physical annual report or 2017 evaluation); do not repeat generic web searches.
3. La Colifata: use any newly available catalogue/physical scans to identify actual *Spot Colifatos* item names and distinguish jingles/music from speech. Current SoundCloud embed is a dead-end for text extraction.
4. Maintain exact composition/recording/production distinctions and rights/consent/anonymity cautions.



## Milestone 23 — Outsider Music Live and Om Music Sanctuary (2026-11-15)
**Current phase:** Phase 13 — peer-led / participant-created music environments.

### Work completed
- Identified Outsider Music Live as a self-organised peer group formed by people who took part in earlier Outsider Music projects. Its official page links individual member Bandcamp releases.
- Verified three releases:
  - Mary G, *The Wandering Star* (9 tracks, 3 Aug. 2023): artist credit explicitly says producer Jon Hall enabled her to write and perform her own songs.
  - Trav Man, *Rise Together* (9 tracks, 14 Aug. 2023): collaborative album with producer, backing singers and musicians explicitly credited; do not assume all tracks are solo-authored.
  - Victory Vibes / Victoria Lamb, *Hello* (17 tracks, 3 July 2023): artist says written and recorded alone on GarageBand between 2014–23; a member link on Outsider Music Live page confirms relationship, but this is home-recorded rather than Outsider studio output.
- Outsider Music's general page lists six original-song examples without artist/date credits; retained as unattributed examples. Lisa's linked Bandcamp page was inaccessible.
- Added Om Music Sanctuary, Edinburgh: a peer-led project with a verified recording studio, member songwriting, recording sessions and original-music events. Council and charity records document its earlier development and pandemic interruption; current official site confirms reopening and current activity. No specific member-made release identified yet.
- No audio auditioned, no contact made, and no reuse rights obtained.

### Repository changes
- `environment-leads.md` updated, commit `e5bd5075eec020bc0a3feae94819fdeebf934b5d`.
- `coop.log.md` updated, commit `7f21acb8ad86288b64585dd6fbe8ec445d0016f2`.

### Next exact task
1. Continue the user-supplied peer-run list, prioritising documented member bands, studio outputs, local radio and participant-run labels.
2. Inspect Outsider Music Originals and the member Bandcamp discographies for earlier/unreleased/less visible works, without reproducing sensitive biographies or ignoring all-rights-reserved licences.
3. For Om Music Sanctuary, search for specific member recordings and studio-band material; distinguish member composition from covers, visiting open-mic performers and volunteer-led demonstrations.
4. Revisit Gugging and Bethel House only through specific audio/release evidence; do not pad the compendium with visual-art-only centres.


## Audio retrieval handoff — 2026-11-15

### Current batch status
- Grok reports these three files already in the shared Drive: `AFC_Lonesome_Jailhouse_Blues_1937.mp3`, `Faust_Scene_de_Prison_Affre_Landouzy.mp3`, `Mille_et_un_jours_en_prison_a_Berlin_Chap1.mp3`. This assistant has not independently inspected Drive or file bytes.
- `TRACK_MAPPING.md` now distinguishes those reported files from new source-verified targets that have not been downloaded here.
- Corrected caution: `AFC_Lonesome_Jailhouse_Blues_1937.mp3` has no matching Parchman LOC item record established in this pass. Keep its provenance unresolved until the audio itself is matched.
- Verified Parchman 1939 LOC audio targets: “Early in the Mornin’” (AFS 02679a01; https://www.loc.gov/item/lomaxbib000368/), “Eaton Clan” (AFS 02675b02; https://www.loc.gov/item/lomaxbib000356/), and “Sick ’em Dogs On” (AFS 02678a02; https://www.loc.gov/item/lomaxbib000365/). LOC states 21 tracks were recorded at Parchman in 1939, 17 included online. “Dangerous Blues” AFS 03082 A03 search result is a digitised catalogue card, not the audio.
- Grand Valley target: official *Undisclosed Location* page exposes a ZIP link, https://prosandconsprogram.com/wp-content/uploads/2018/03/Undisclosed-Location.zip . It is ten anonymous participant-written/sung/recorded songs from Grand Valley, 2017–18. Direct binary retrieval failed in this workspace.
- Additional album routes: *Private Town* (Grand Valley, 11 tracks; https://prosandconsprogram.bandcamp.com/album/private-town) and *Paint in the Forest* (Joyceville, 12 tracks; https://prosandconsprogram.bandcamp.com/album/paint-in-the-forest). Bandcamp checkout advertises digital downloads. Do not conflate Joyceville with Grand Valley.
- No batch-2 audio bytes downloaded, no audio auditioned, and no upload performed. Never claim otherwise.

### Next exact execution
1. Resume audio retrieval from the three verified Parchman LOC item pages. Obtain actual audio bytes only where the source exposes a legitimate download route; record exact URL, filename, file size and checksum. If the current execution environment cannot fetch binary media, report that limitation and provide the verified source/download page rather than inventing a sandbox file.
2. Download the official *Undisclosed Location* ZIP if a working binary transfer route becomes available; preserve anonymity and the original filenames/track order. Verify archive contents and checksums.
3. For *Private Town* and *Paint in the Forest*, use the official Bandcamp digital download route; do not bypass checkout or claim free access unless the platform explicitly offers it.
4. Continue to Grand Valley / Pros & Cons related releases only after batch 2 has been logged. Keep the spoken-word Berlin memoir outside the music track batch.
5. After any actual retrieval, update `TRACK_MAPPING.md` with exact local filename, source URL, file size, checksum, download date, and verification status; append concise dated evidence to `coop.log.md`; update this checkpoint last. Use fresh SHA for each sequential file update and verify all three repository files.


## 2026-11-15 — Revised execution checkpoint: research-only / track-source discovery

**This section supersedes the previous “Next exact execution” download-retrieval queue above.** The project owner has explicitly shifted this assistant's role to research, candidate verification and track/source URL discovery. Grok handles downloading and Google Drive uploads. Do not spend scheduled sessions trying to download or upload audio.

### Current work mode
- Research-first: discover overlooked recordings; polish candidate records; verify environment, authorship, date, format and provenance; identify exact track/item pages and direct listening/download URLs.
- Update environment-leads.md, TRACK_MAPPING.md and coop.log.md with evidence. Maintain this checkpoint after each meaningful batch.
- Direct URLs must be verified from primary/official sources. Distinguish an item/catalogue page, embedded player, stream URL and actual downloadable file URL. Never invent media URLs from guessed slugs.
- No claim of listening, download, upload, archive contact or permission unless it happened.
- Private research is not a rights clearance. Keep access, consent, rights and publication/reuse status distinct.

### Latest completed research batch — Soledad / Kalaupapa / Carville (2026-11-15)

**Soledad CTF / Jack Bowers, AFC 2024/014**
- Audited LOC finding aid, Series 7 / Subseries 1, printed pp. 143–144: https://tile.loc.gov/storage-services/service/gdc/gdcfindingaidpdfs/af024007/af024007.pdf .
- Confirmed exact groupings and tracklists: Rusty Smith (1983, 10 AIFF), Sacred Ryche (1986, 7 AIFF), CTF Recording Project (July 1992, 13 AIFF), Anthology CTF (1996, 9 AIFF), Oscar's Tune (2 AIFF, undated/performer unknown). Five cassette-liner JPGs also catalogued.
- LOC shared digital ID afc2024014_dc001 is not a direct media URL. No public audio files exposed in finding aid. Research access by AFC request: https://hdl.loc.gov/loc.afc/folklife.contact .
- Copyright Office catalogue transcriptions reveal a possible related 1984 Joint Venture cassette *Pearls Before Swine*, performed as Rusty Smith and the Saddletramps, credited to George Lee Davidson; exact match to CTF 1983 grouping unproven. Do not merge or infer identity without liner confirmation.
- Sacred Ryche and Oscar's Tune are strongest obscurity leads; 1992/1996 compilations need track-level authorship/cover classification.

**Kalaupapa 1952 cassette**
- HCUCC public listening page: https://www.hcucc.org/kalaupapa-sunday ; 13 A-side and 8 B-side audio excerpts.
- HCUCC written description PDF: https://www.hcucc.org/_files/ugd/1c51b0_974ec3094c53448d93230effc8ebec64.pdf . One 60-minute cassette recorded in 1952 by Steve Dawson and Robert Kihe (both identified as patients); source made available by Nancy Chang Talino.
- Side 1 contains 11 songs by Kana‘ana Hou Boys Chorus / Kana‘ana Hou Choir; “E Nā Kini o ka ‘Āina” explicitly written by Ernest Kalā. “Moku Kakele o i ona” title/spelling uncertain. Side 2 has eight St. Francis of Assisi Church Choir excerpts; titles/personnel unverified.
- Do not infer all singers were patients. HCUCC player is public listening, not a verified full-cassette download.

**Carville patient cantatas**
- Daughters of Charity Archives finding aid: https://docarchivesblog.org/wp-content/uploads/2023/02/11-2-carville-la-national-hansens-disease-center-finding-aid.pdf .
- Exact inventory RG 11-2-8-4, Box 48: folder 7 Easter cantata performed by patients, narrated by Buddy Glacis, organ by Sr. Laura Stricker (undated); folder 8 generic Christmas cantata (undated); folder 9 Christmas cantata by Sr. Laura Stricker & patients (1981); folder 6 Carville organ music (undated).
- Archive-only cassette inventory; no public listening/download. Access/reproduction restrictions and permission required for publication. Patient performance does not prove patient composition.

**Repository commits**
- environment-leads.md: b1ad28e22646053a37da0c371a339224aacde318
- TRACK_MAPPING.md: 081714fc29622819d3a8a4e7805b6a3573e5f48a
- coop.log.md: 84f48de3935709b4d5542cc6a1c5ba70965e0376

### Latest completed research batch — Pros and Cons / Waupun source audit (2026-11-15)

**Pros and Cons official media map**
- *Undisclosed Location* (Grand Valley, 2017–18): official page confirms 10 original songs written, sung and recorded anonymously by incarcerated women. Verified official M4A links for all ten tracks and official ZIP: https://prosandconsprogram.com/wp-content/uploads/2018/03/Undisclosed-Location.zip . Exact links are in TRACK_MAPPING.md.
- *Postcards from the County* (Pittsburgh Institution, 2014): official page confirms 12 tracks, all notes sung/played inside jail, inmate songwriting/arranging in the prison chapel studio, and guest musician participation. Verified all 12 direct MP3 links and official ZIP: https://prosandconsprogram.com/wp-content/uploads/2015/04/PostcardsFromTheCountyArchive.zip . Page says P.I. marks indicate original inmate compositions, but text extraction did not preserve which track titles carry the marker. Do not infer track authorship until visually checked. The Pittsburgh Institution naming is retained as used by the original project page; later official copy refers to Joyceville Correctional Centre.
- *Private Town* (Grand Valley, released 15 May 2020): official page confirms songs written/performed by incarcerated women, producer Aimee Copping, mix Hugh Christopher Brown/Jake Bury; direct tracklist/media links remain unexposed in text extraction.
- *Paint in the Forest* (Joyceville, 2017–19): official page confirms recording period; official May 2020 announcement says 12 songs selected from over 100 recorded at on-site studio and identifies a traditional hymn rendition. Complete tracklist/direct media links not extracted.
- No files downloaded or auditioned; web preview rejected linked audio/ZIP MIME types, but exact official targets were captured.

**Waupun newspaper trail clarified**
- The digitised Waupun *Prison Press* is historical 1859–1898 material and is not the right source for Upheaval's 1970s music-era evidence.
- WHS prison-newspaper collection list identifies *Waupun World*, c.1969–Jan. 1983, with scattered holdings including 1970–75 and July 1980–Jan. 1983. This is the relevant title to search/request for band activity.
- Waupun Public Library's Newspapers.com announcement lists digitised Waupun papers including *Prison Press* but does not establish online *Waupun World* coverage.
- Sources: https://cdn.wisconsinhistory.org/cdm/Prison%20Newspaper%20CollectionSep2017.pdf ; https://waupunpioneer.com/2024/05/21/waupun-public-librarys-collection-of-historical-waupun-newspapers-digitized/ .

**Repository commits**
- environment-leads.md: 34b55d0e2a2f001ae9177688514077799854c103
- TRACK_MAPPING.md: 411439c726bd49998e5902b1d5eba0e2620480d7
- coop.log.md: 3474046dc46cde4db86be281c5e37c4f8ebf8cf6

### Next active research queue
1. **Waupun / Upheaval:** request/search Wisconsin Historical Society *Waupun World* holdings (especially 1974–75, then 1980–83) for music-program articles, band member names, events, photographs and source scans. Continue trying to resolve WHS Aviary media IDs 155112/155113; current public web fetch returns internal errors, so do not claim player access. Seek reliable video item/catalogue record, exact segmentation and song-to-reel mapping. Search other Waupun bands only if concrete surviving audio emerges.
2. **Pros and Cons embedded media:** inspect official embedded players for *Private Town* and *Paint in the Forest* to capture tracklists and exact official audio URLs; visually inspect *Postcards* page/liner to identify P.I. track markers without unmasking anonymous writers.
3. **International discovery:** continue environment-first research through specialist archives, small-web music blogs, cassette/zine sites, micro-labels and community radio; prioritise obscure, unissued or under-documented recordings.
4. **Finding Rhythms:** continue item-level audit only where institutional setting and participant authorship are explicit; score obscurity separately from provenance quality and avoid padding with recent commercial albums.
5. **Soledad CTF / Jack Bowers:** first-pass audit complete. Revisit only if cassette-liner images, performer/authorship evidence or an actual archive access route appears.
6. **Carville and Kalaupapa:** first-pass item-level inventories complete. Revisit only for new audio access, community/archivist clarification, complete Kalaupapa side-2 identification or new performer/composer evidence.

### Latest completed research batch — Upheaval / Waupun (2026-11-15)

- Rechecked Max Wilson's 2022 article and both embedded WHS Aviary links. Media IDs 155112 and 155113 are confirmed by article iframe targets, but both fail with redirect-loop errors in the web viewer. No direct media/download URL or full cue sheet found.
- Newly mapped archival/song leads: “Love Station,” “Broken Down Porch” (written by James Harris), “Ready Train,” “Happy Hooker,” and “Vampire Lady”; Hayes reportedly had a CD's worth of recordings. Rudd's reels/cassettes' current location remains unknown. No unlicensed copies or archive rips to be sought.
- Confirmed authorised digital retail routes:
  - Symphonical Records SYM001, *Come on with the Come on / TLC* (2016), Newtone Records Digital: https://www.newtone-records.com/product/9053925 . Two previously unreleased prison-recorded tracks, 3:18 and 3:05, sourced from surviving cassettes; digital formats offered. Added to TRACK_MAPPING.md as HIGH priority GROK DOWNLOAD REQUEST.
  - Now-Again Records, “Paradise Lost” official Bandcamp digital track: https://nowagainrecords.bandcamp.com/track/paradise-lost . Paid digital track; later reissue/context, added as MEDIUM priority Grok request.
- No media downloaded or auditioned. Track mapping contains exact official retailer pages, formats, track durations, rationale and transfer instructions.

### Next active research queue
1. **Waupun / Upheaval:** Grok can action the two authorised reissue download requests in TRACK_MAPPING.md if purchase is authorised. Continue source research for WHS Aviary IDs 155112/155113, *Waupun World* scans and exact video cue sheet; do not rip restricted video or private tapes. Search for authorised release/access routes for the unreleased song leads only.
2. **Pros and Cons embedded media:** use alternative source routes to extract tracklists/direct official audio for *Private Town* and *Paint in the Forest*; visually inspect *Postcards* P.I. track markers without identifying anonymous writers. WordPress REST API endpoint attempts failed; do not invent media URLs.
3. **International discovery:** continue environment-first research through specialist archives, small-web music blogs, cassette/zine sites, micro-labels and community radio; prioritise obscure, unissued or under-documented recordings.
4. **Finding Rhythms:** continue item-level audit only where institutional setting and participant authorship are explicit; score obscurity separately from provenance quality.
5. **Soledad CTF / Jack Bowers:** first-pass audit complete; revisit only for new liner/performer/access evidence.
6. **Carville and Kalaupapa:** first-pass inventories complete; revisit only for new audio access, community/archivist clarification or new attribution evidence.

### Per-run completion and repository workflow
- Begin every run by reading this file first, then method.md, environment-leads.md, coop.log.md and TRACK_MAPPING.md.
- Work the queue in order unless a stronger primary-source lead appears; mark completed items and carry forward unresolved questions.
- Fetch each file's current SHA immediately before its sequential update; never parallel-write the same file. Update candidate evidence, track map and concise log, then update this checkpoint last.
- Verify final file contents and commit hashes. Report only what was actually verified; state clearly when a source is identified but direct media retrieval/playback remains unresolved.
- Each scheduled run is approximately one hour and should produce a concise report even if no new candidate qualifies. No work continues between runs.


### Latest completed research batch — Langdon Hospital / Labyrinthe Des Esprits (2026-11-15)

- Verified *The Cosmic Hunt* (Labyrinthe Des Esprits), released 18 March 2025, through official artist Bandcamp and Devon Partnership NHS Trust.
- Six patients at Langdon Hospital, a medium-secure forensic service in Dawlish, recorded, edited and produced the album under Musical Technical Instructor Matt Smith. Trust confirms field recordings during approved Section 17 leave, guest ambient contributions by Nick Lesja, Anthony Tang and Ash Wednesday, and narration by Trust employee Peter.
- Official Bandcamp tracklist has 25 entries (23 shorter pieces plus two long-form sides), complete durations, 24-bit/44.1kHz digital download at £7+ and limited cassette+digital at £10 when inspected. Patient contributors credited by initials JPW, CN, NT, JLG, DS, AC. Licence: all rights reserved.
- Added detailed candidate record to environment-leads.md and a MEDIUM-priority GROK DOWNLOAD REQUEST to TRACK_MAPPING.md. Strong institutional provenance, but recent public release / The Wire and BBC coverage mean it is not a high-obscurity discovery. Do not infer track-by-track authorship or deanonymise contributors.
- Sources: https://www.dpt.nhs.uk/news/langdon-patients-release-therapeutic-ambient-album-831/ ; https://labyrinthedesesprits.bandcamp.com/album/the-cosmic-hunt ; https://www.bbc.com/news/articles/clydyxl1w65o .

### Next active queue (revised)
1. Pros and Cons: resolve direct track/media mapping for *Private Town* and *Paint in the Forest*; identify *Postcards from the County* P.I. markers using rendered page/liner without identifying anonymous writers.
2. Waupun / Upheaval: obtain primary *Waupun World* 1971 issue evidence for Eddie Quinn's music writing and named bands; pursue authorised WHS catalogue/access route for Aviary IDs 155112/155113 and exact cue sheet. Do not rip or bypass restricted video.
3. International discovery: continue small-web, local-language, micro-label, radio and national-archive research for older, less-circulated participant/resident-created recordings. Screen out contemporary, already-public examples unless they add a distinct environment or method.
4. Langdon: use as a comparative contemporary case; revisit only if track-level participant/guest credits, project documentation, or a less-public predecessor/related output emerges.
5. Finding Rhythms: continue only where specific institutional setting, participant authorship and item-level release evidence can be verified.
6. Soledad, Carville and Kalaupapa: first-pass audits complete; revisit only for genuinely new attribution, access or item evidence.



### Waupun archival refinement (2026-11-15)
- Exact target is now the **January 1971 Waupun World** issue: Max Wilson quotes Eddie Quinn's “Music Scene” essay from that issue. Wisconsin Historical Society holdings list covers 20 Jan–20 Nov 1971, plus specific issues in 1970, 1972–75 and July 1980–Jan 1983. Request January 1971 first, then 1974–75 issues for Upheaval material.
- Wilson also names QCR, Yusef & The Fellows, King Thomas and the Blue Flames, The Spiritual Five and The Sudanese; no separate surviving recordings for these groups are yet established.
- Sources: https://quillette.com/2022/07/28/lost-soul-behind-bars/ ; https://cdn.wisconsinhistory.org/cdm/Prison%20Newspaper%20CollectionSep2017.pdf .


### Latest research batch — Iowa State Penitentiary inmate radio / The Madisonians (2026-11-15)

- Contemporary 1959 trade-magazine article verifies “Prison on the Hill,” weekly Iowa State Penitentiary inmate-produced/engineered radio programme beginning 11 March 1956; music, vocals, quartets and interviews. Named prison orchestra The Madisonians led by incarcerated trumpeter Bob Frost; Bobby Mohr co-producer/performer; Duke Birr engineer. Article: https://www.worldradiohistory.com/Archive-All-Audio/Archive-Tape-Recording/50s/Tape-Recording-1959-08.pdf .
- *Daily Iowan* (23 May 1957) independently documents inmates recording an interview with Governor Loveless for the programme: https://dailyiowan.lib.uiowa.edu/DI/1957/di1957-05-23.pdf . KMA 1957/58 station guides list programme schedule.
- No extant programme tape/aircheck or direct audio URL found. Candidate entered as high-priority archive search, not verified extant recording and not a Grok download request. Next: Iowa State Archives/DOC, KXGI/KMA station archives, Fort Madison historical collections, participant papers.
- Screened Derby Leprosarium / Bungaran Orchestra: 1999 documentary *The Healing Sounds of the Bungaran Orchestra* is a later memory/return documentary; scholarship documents patient orchestra/choir but no extant historic recording established. Context only pending audiovisual item audit.
- Screened Texas “Thirty Minutes Behind the Walls” (Huntsville, 1938–44): historical radio programme and inmate performers verified, but reporting states no programme recordings have been found. Contextual negative finding; not an extant recording candidate.
- Sources: https://www.worldradiohistory.com/Archive-All-Audio/Archive-Tape-Recording/50s/Tape-Recording-1959-08.pdf ; https://dailyiowan.lib.uiowa.edu/DI/1957/di1957-05-23.pdf ; https://www.screenaustralia.gov.au/screen-guide/healing-sounds-of-the-bungaran-orchestra-the-14164/ ; https://www.themarshallproject.org/2016/05/16/a-peek-at-the-golden-age-of-prison-radio .

### Next active research queue
1. Iowa State Penitentiary: pursue named archive/station repositories for “Prison on the Hill” tapes/airchecks and The Madisonians recordings. Only add Grok request when an extant authorised audio source and exact item are verified.
2. Pros and Cons: obtain player tracklists/media for *Private Town* and *Paint in the Forest*; identify *Postcards* P.I. track markers without unmasking anonymous makers.
3. Waupun: seek January 1971 *Waupun World* and 1974–75 issues; resolve WHS Aviary IDs 155112/155113 via catalogue/access, not stream-ripping.
4. International environment-first discovery, especially historic participant-made recordings with actual surviving audio; prioritize local-language archives and independent micro-labels.
5. Texas “Thirty Minutes Behind the Walls” and Derby/Bungaran remain contextual unless new extant sound evidence appears.


### Latest completed research batch — Fort Madison 1952 WOI-TV prisoner-song film (2026-11-15)

- Verified WOI-TV *In Our Care*, Episode 10, “State Penitentiary at Fort Madison,” broadcast 11 July 1952, inventory K-155, 29:00. Iowa State University's WOI-TV 16mm film inventory lists the item and production credits (Ray Stewart, LaMar Smith, Hazel Allen, Ferne Bonomi, Charles Hawley).
- The Johnson County Justice Center's episode description says it includes a song conducted and performed by prisoners. This is a source description; song title, performers, authorship and timecode remain unidentified, and the film has not been auditioned in this research.
- Public streaming: Iowa State SCUA YouTube Part 1 https://www.youtube.com/watch?v=Ef6OTf8kTc8 and Part 3 https://www.youtube.com/watch?v=taqZqdE74Jw; episode page embeds Parts 1–3 https://jcjusticecenter.com/2015/01/11/in-our-care-fort-madison-penitentiary-documentary/ .
- Production papers: Ray Stewart Papers RS 5/6/22, Box 1/Folder 5, open for research; publication rights require consultation with SCUA. Finding aid https://findingaids.lib.iastate.edu/spcl/arch/rgrp/5-6-22.html .
- Added as a verified audiovisual document containing an unidentified prisoner-performed song, not a standalone release and not a Grok download request. It is distinct from *Prison on the Hill* / The Madisonians.
- Next: inspect the three public segments for the music timecode and song identity; use Box 1/Folder 5 production notes/scripts and ask SCUA about K-155 preservation masters, source sound elements and reuse permissions.
- Sources: https://specialcollections.lib.iastate.edu/files/documents/2023-04/WOI-TV-Films.pdf ; https://findingaids.lib.iastate.edu/spcl/arch/rgrp/5-6-22.html ; https://jcjusticecenter.com/2015/01/11/in-our-care-fort-madison-penitentiary-documentary/ .

### Next active research queue (revised)
1. **Fort Madison K-155 film:** inspect public parts 1–3 to locate and identify the prisoner-performed song; audit the Ray Stewart papers' Box 1/Folder 5 for script, cue sheet or music detail; establish authorised access/reuse route with SCUA before any acquisition request.
2. **Iowa State Penitentiary radio:** continue repository/station search for *Prison on the Hill* programme tapes/airchecks and The Madisonians recordings. KXGI/KMA and prison administration remain hypotheses, not known holdings.
3. **Pros and Cons:** obtain player tracklists/media for *Private Town* and *Paint in the Forest*; identify *Postcards* P.I. track markers without unmasking anonymous makers.
4. **Waupun:** seek January 1971 *Waupun World* and 1974–75 issues; resolve WHS Aviary IDs 155112/155113 through catalogue/access, not stream-ripping.
5. **International environment-first discovery:** prioritize older participant-made recordings with extant audio, local-language archives and independent micro-labels.
6. **Texas “Thirty Minutes Behind the Walls” and Derby/Bungaran:** contextual only unless new extant sound evidence appears.


### Fort Madison print-source follow-up — *The Presidio* (2026-11-15)

- Fort Madison Public Library's local-history guide lists *The Presidio* for 1939–1968: https://www.fortmadison-ia.com/DocumentCenter/View/33 . April 1956 *The Penal Press* notices the inmate-edited publication and names writers Hendrie, Runyon and Gagnan: https://penalpress.com/wp-content/uploads/KPT_Apr56.pdf . A 1958 *Freeman* article describes the magazine as monthly and discusses its November 1956 issue: https://cdn.mises.org/The%20Freeman%201958%2C%20Vol%20IV_2.pdf .
- This is a print-source route for *Prison on the Hill* context and contributor identification, not audio evidence. No music-specific content established in the secondary descriptions.
- **Queue update:** after K-155 song identification, seek 1956–59 *Presidio* issues via Fort Madison Public Library / State Historical Society of Iowa; search explicit references to the radio programme, The Madisonians, and music. Verify issue holdings before claiming coverage.


### Latest completed batch — Pros and Cons Bandcamp tracklists (2026-11-15)

- Completed primary Bandcamp tracklist audit for *Private Town* and *Paint in the Forest*.
- *Private Town*: Grand Valley Institution for Women, released 15 May 2020; 11 tracks, full titles/durations captured in environment-leads.md and TRACK_MAPPING.md. Bandcamp explicitly credits the songs as written and performed by incarcerated women; 16-bit/44.1 kHz MP3/FLAC/other download options; all rights reserved.
- *Paint in the Forest*: Joyceville Minimum Institution, recorded 2017–19, released 15 May 2020; 12 tracks and durations captured in both files. Bandcamp offers 24-bit/44.1 kHz MP3/FLAC/other downloads; all rights reserved. Official copy says 12 tracks selected from over 100 on-site studio recordings; “Lord Prepare Me” is a traditional Methodist hymn. Avoid claiming all tracks are participant-original compositions.
- Added MEDIUM-priority GROK DOWNLOAD REQUESTS for both releases with official checkout links, formats, filenames, tracklists, provenance and rights notes. Treat as public 2020 releases, not rare archival tapes.
- **Next exact tasks:** (1) identify *Postcards from the County* P.I. original-composition markers from rendered page/liner without identifying anonymous makers; (2) inspect K-155 public video parts to locate the prisoner song/timecode and consult Ray Stewart Papers Box 1/Folder 5 for script/cue notes; (3) resume Fort Madison *Presidio* issue-level search and Iowa radio archive search.


### Latest batch — global research balance correction; Chilean archive discovery (2026-11-15)

- Research balance instruction: deliberately expand beyond North American/western European archives; use local-language catalogues, community museums, regional universities, oral-history projects and independent labels across Africa, Asia, Latin America/Caribbean, Pacific, Middle East and eastern/southeastern Europe. Preserve original-language titles and assess significance independently of English-language visibility.
- **Highest-priority new lead: Chile / Cantos Cautivos.** “El Suertúo” is a cueca composed by Víctor Canto and Luis Cifuentes at Chacabuco camp between Nov 1973 and Feb 1974, clandestinely recorded by Alberto Corvalán Castillo with a recorder supplied by a camp captain. Los de Chacabuco, directed by Ángel Parra, performed it in the camp's weekly concert. The recording is part of the Cantos Cautivos archive. Archive: https://www.cantoscautivos.org/ ; contemporary reporting: https://radio.uchile.cl/2015/01/11/cantos-cautivos-la-musica-que-sono-en-los-centros-de-detencion-de-la-dictadura/ ; https://www.biobiochile.cl/noticias/2014/12/31/cantos-cautivos-canciones-al-interior-de-los-centros-de-torturas-de-pinochet.shtml .
- University of Chile says the archive had 168 testimonies by mid-2025, including 40 works created in prison and 12 works with lyrics written/altered in captivity over existing music. UNESCO's Sept 2026 resource adds a current educational/archive route. See environment-leads.md for URLs and provenance.
- Keep the lead HIGH PRIORITY for exact item audit, but do not add a Grok request until direct archive entry, media URL, item identity and access/reuse terms are confirmed. Distinguish in-camp original from later performance; keep composer, recordist, performers and ensemble director separate.
- **Malawi:** Zomba Prison Project's 2015/2016 albums verified from official artist/label pages; use as context/comparison, not obscure archival material.
- **POW multilingual archive:** Austrian Phonogrammarchiv's ~250 WWI POW recordings verified; next audit individual music items and communities, with critical attention to the researcher's wartime power and recording context.

### Revised next active queue
1. Chile: item-level Cantos Cautivos audit, starting with “El Suertúo” and Chacabuco; then cross-check La Serena and Ritoque thesis-index candidates against primary archive entries. No download request until authorised item/media route and rights are clear.
2. Austrian Phonogrammarchiv: identify musical (not speech-only) POW items by language/community and establish access to audio masters/source edition.
3. Broaden the international search through local-language repositories and independent labels, prioritising Africa, Asia, Latin America, Pacific, Middle East and eastern/southeastern Europe.
4. Resume outstanding Pros and Cons *Postcards* P.I. marker audit and Fort Madison K-155 song identification when appropriate; these remain active but do not dominate discovery batches.
5. Waupun *Waupun World* issue-level search and WHS Aviary item access.
6. Malawi Zomba Prison Project remains CONTEXT / comparative, not a novelty lead.


### Chile follow-up — exact MMDH radio archive item and corrected credits (2026-11-15)

- MMDH Archivo Radial search result identifies **“Centros de Detención”**, Radio Moscú / *Escucha Chile*, Chacabuco, 23:36; event marking prisoners' release; acts Punto 30, Jamarí, Hugo Peñaloza, Mario Céspedes, Coro Chacabuco; songs include “Libre,” “Oficina Chacabuco,” “Volver,” “Himno a la Alegría,” “Tonada del Viejo Amor,” “Amalia Rosa,” “Caliche,” “El Puntudo.” Public player/catalogue: https://archivoradial.museodelamemoria.cl/buscador_resultado.php?filtro=11&registros=0&tipo=1 .
- Chilean music-education thesis says “El Suertúo” appears in this 23:36 programme at 18:30–20:50; separately identifies a 2:03 clandestine Chacabuco recording item. Timecode is a lead, not an auditioned confirmation: https://openbiblio.museodelamemoria.cl/media/digitales/TESIS_EDUCACION%20MUSICAL.pdf .
- Song credit refined: lyrics Víctor Canto and Luis Cifuentes; music Roberto Parra; Fondo García Salas, MMDH conservation code 067-001-002: https://manager.mmdh.cl/uploads/L_Ibro_tesis_20212022_EDUCACION_MUSICAL_Vok_WEB_da5720b67c.pdf .
- Cantos Cautivos index says *Pasión según San Juan* by Ángel Parra is track 3 on the Chacabuco cassette recorded by Los de Chacabuco. Follow up for direct item/audio route and version provenance.
- Keep the 23:36 programme, 2:03 clandestine recording, and individual songs/cassette as distinct objects pending item-level record reconciliation. Player access is not direct download or reuse permission. No Grok request added.


### Further global leads — Nigeria and Japan (2026-11-15)

- **Nigeria / Uzuakoli:** LEPRA sources confirm Ikoli Harcourt Whyte's patient choir and that Dr. J.A.K. Brown / Frank Davey recorded traditional songs from outlying communities and played these recordings to Whyte as source material. John Manton's 2015 radio documentary confirms surviving original vinyl recordings of Whyte's choir were remastered into the broadcast, alongside contemporary arrangements, testimony and field recordings. Exact original pressing/discographic data still missing. Keep original choir sides, traditional field recordings, later arrangements and radio documentary excerpts distinct. Sources in environment-leads.md.
- TLM Canada archive catalogue notes audio tapes made in Purulia, Chandraghona, Bhutan, Irian Jaya, Papua New Guinea and Thailand; contents unverified. Worth item-level audit, not assumed musical.
- **Japan / Nagashima Aiseien:** Aoi-tori Gakudan / Bluebird Band, a resident-led harmonica ensemble founded in 1953 and led by Koichi Kondo, is documented by Japanese scholarship and the National Hansen's Disease Museum. No period recording yet located; archive hunt only. Search Japanese terms 楽団「あおいとり」, 青い鳥楽団, 長島愛生園, 近藤幸一, ハーモニカ. Do not substitute modern tribute performances.
- **Next queue:** (1) identify Uzuakoli original vinyl labels/catalogue numbers and access route via Manton broadcast credits / Whyte biographer / Nigerian church collections; (2) search National Hansen's Disease Museum and Nagashima Aiseien records for Aoi-tori historical recordings; (3) item-audit TLM audio tapes in non-Western field collections; (4) continue Chile Cantos Cautivos / MMDH exact item reconciliation; (5) Austrian POW musical item audit; then rotate back to pending Pros and Cons / Fort Madison / Waupun work.


### Latest research batch — Uzuakoli and Nagashima Aiseien source-history refinement (2026-11-15)

- **Uzuakoli correction:** Music In Africa reports that Ikoli Harcourt Whyte did not record an album; the Choir of the Leprosy Colony, Uzuakoli recorded his compositions after his death in 1977, while a separate St. Louis Missouri African Choir recording followed in 1999. John Manton's 2015 programme confirms original vinyl recordings of the Uzuakoli choir were used, but exact pressing/date/label/catalogue number remain unknown. Do not imply Whyte personally recorded the vinyl or that it is a lifetime recording.
- Identified key song-title search variants “Atulegwu” / “Atula Egwu” and “Umu gi emebiwo uwa gi” through International Leprosy Association sources. Located Achinivu Kanu Achinivu's 1979 two-volume monograph record in the International Library of African Music / AMIRA catalogue (DRE eaa-99-0243; identifier 1270); volume 2 includes music and texts, but this is a notation/text source, not audio or proof of vinyl custody.
- **Japan / Aoi-tori Gakudan:** Japanese-language National Diet Library research confirms the November 1953 formation and detailed ensemble activity. National Hansen's Disease Museum documentation identifies a May 1974 performance photograph and 1970 Zhao Gen-zai photographs B053/B054. A 2023 Ken Miyazaki video reuses 1982 footage of Kondo singing with Blind Association members; because the band had ceased activity by 1978, this is a later resident performance, not a Bluebird Band recording. A 2019 Asahi memorial concert is a modern professional tribute. Strong period documentation, but no historical band audio located.
- Sources are recorded in environment-leads.md and coop.log.md. TRACK_MAPPING.md unchanged; no new authorised acquisition URL.
- **Next active queue:**
  1. Uzuakoli: pursue original choir-vinyl discographic identity through Achinivu monograph bibliography, original broadcast production notes/credits, Nigerian Methodist/choir holdings and local-language/label catalogues; reconcile “Atulegwu” title variants. No download request until exact pressing and authorised route.
  2. Nagashima Aiseien: identify NHDM / Nagashima Aiseien History Museum audiovisual inventories and original 1970s photographer/broadcaster holdings; target 1974 performance footage or an original audio master, not modern tributes.
  3. TLM archive: item-level audit the tapes from Purulia, Chandraghona, Bhutan, Irian Jaya, Papua New Guinea and Thailand; establish whether any contain music before treating them as candidates.
  4. Chile Cantos Cautivos: reconcile exact item pages/media for “El Suertúo,” “Centros de Detención,” the separate 2:03 clandestine item and Chacabuco cassette / *Pasión según San Juan*.
  5. Austrian Phonogrammarchiv: identify music-bearing WWI POW recordings by language/community, not speech-only objects.
  6. Continue rotating globally through locally grounded sources; do not let English-language visibility or Western archive availability dictate priority.


### Latest research batch — Chacabuco item reconciliation, TLM inventory and Aoi-tori tour trail (2026-11-15)

- **Chile:** MMDH catalogue search exposes two separate Chacabuco objects: 23:36 “Centros de Detención” (release ceremony; listed ensembles and songs) and 2:03 “Grabación clandestina…” (Alberto Corvalán attribution; explicitly lists “Canción de la Despedida,” Ángel Parra, Coro Chacabuco/Iván Quezada and other acts). The thesis locates “El Suertúo” at 18:30–20:50 in the 23:36 programme, not the separate 2:03 item. A 2022 scholarly source uses ambiguous “this clandestine recording” wording for “El Suertúo” and “El Puntúo”; do not merge the objects. Song authorship is discrepant across manuscript appendix, testimony and secondary table: keep Luis Cifuentes / Víctor Canto lyric/composition claims distinct from the separate Roberto Parra music credit pending primary reconciliation. No direct download or rights route.
- **TLM Canada / Effect:Hope:** ILA archive entry confirms audio tapes made on Purulia, Chandraghona, Bhutan, Irian Jaya, Papua New Guinea and Thailand, but no item-level contents. It also lists 11 largely 16mm reels, numerous videotapes and a 1978 cassette accompanying slide group titled “More Than a Prophet” (content unknown). Contact route info@effecthope.org. Ask for tape IDs, titles, dates, subjects, language, recordists, whether music is present, formats/condition, restrictions and preservation copies. No assumption of music or copying rights.
- **Japan:** Aoi-tori Gakudan external performance history 1967–76 includes 15 outings and venues/events in Osaka, Tokyo, Nagoya and Kyoto. Search local host venue programmes, newspapers, amateur film and radio/TV archives; photographs are not audio evidence.
- Sources and detailed metadata are appended to environment-leads.md and coop.log.md.

### Next active queue
1. **TLM Canada / Effect:Hope:** obtain/locate item-level AV finding aid for six named audio-tape locations and identify the 1978 “More Than a Prophet” cassette. No blanket copying request; establish community, content and restrictions.
2. **Japan / Aoi-tori:** follow the 1967–76 touring circuit through local newspapers, venue/event programmes, broadcasters and amateur film collections in Osaka, Tokyo, Nagoya and Kyoto; seek original sound only, not tribute recordings.
3. **Chile / Chacabuco:** reconcile conflicting cueca credits with manuscript pages and testimony; identify whether the 23:36 programme includes the clandestine source recording and map the separate 2:03 item; seek direct media and rights metadata.
4. **Nigeria / Uzuakoli:** pursue the post-1977 Choir of the Leprosy Colony vinyl through Achinivu's 1979 bibliography, Manton's broadcast production records, Methodist/choir holdings and local Nigerian labels. Separate the choir vinyl from field recordings and 1999 St. Louis recording.
5. **Austria / Phonogrammarchiv:** isolate music-bearing WWI POW items by language/community; exclude speech-only records and document wartime power asymmetry.
6. Rotate international discovery across Africa, Asia, Latin America/Caribbean, Pacific, Middle East and eastern/southeastern Europe through local-language sources; then resume Pros and Cons *Postcards*, Fort Madison K-155 and Waupun.


### Latest research batch — Aoi-tori historic concert recordings verified as surviving (2026-11-15)

- **Priority upgrade:** Leprosy.jp's 2017 Japanese interview says former Aoi-tori vocalist Matsuo Sasaki played the interviewer concert recordings, including Koichi Kondo's original “鶴島哀歌” with Sasaki solo vocal; another concert recording featured Sasaki lead with nursing-school women's chorus. Sasaki died in 2019; the recordings are not publicly linked and their current custodian/date/format are unknown.
- A 1968-06-24 Osaka Kosei Kaikan concert programme lists “鶴島哀歌” as a Sasaki solo. This documents a specific performance but does not prove that the tape heard in 2017 is this particular 1968 recording.
- Umitaro Abe's 2025 lecture report says nearly all Aoi-tori concerts were recorded, source audio/materials were shown to him by an event organiser, and he planned a curated historic recording selection and audio collection (“近藤宏一の過去と現在”). A 2026 Nagi Museum page confirms Abe/Toyama's ongoing research, recording/digitisation and preservation project, but no public original audio release located.
- Distinguish historic Aoi-tori tapes from Abe/Toyama contemporary interpretations and the 2019 memorial concert. No Grok request until authorised public release or documented access and rights. Detailed evidence in environment-leads.md and coop.log.md.

### Next active queue
1. **Japan / Aoi-tori — top priority:** establish current status of Abe Umitaro's historic audio collection / “近藤宏一の過去と現在”; identify event organiser who supplied source audio; query Nagashima Aiseien History Museum, National Hansen's Disease Museum, FIWC Kansai / Musubi no Ie and the 1968 concert programme archive for original reel/cassette inventories, item dates, transfer history, access and rights. Keep 1968 “鶴島哀歌” Sasaki solo distinct from any unmatched recording. Respect participant/family wishes; no unsolicited family contact or publication of private audio.
2. **TLM Canada / Effect:Hope:** obtain item-level AV inventory for audio tapes made on Purulia, Chandraghona, Bhutan, Irian Jaya, Papua New Guinea and Thailand; identify 1978 “More Than a Prophet” cassette; establish whether music is present and restrictions. No assumptions.
3. **Chile / Chacabuco:** reconcile the 23:36 “Centros de Detención” and separate 2:03 “Grabación clandestina” objects; thesis places “El Suertúo” at 18:30–20:50 in the 23:36 player. Resolve conflicting song credits; seek direct media and rights metadata.
4. **Nigeria / Uzuakoli:** pursue post-1977 Choir of the Leprosy Colony vinyl through Achinivu bibliography, Manton broadcast production records, Methodist/choir holdings and local Nigerian labels; distinguish field recordings and 1999 St. Louis recording.
5. **Austria / Phonogrammarchiv:** isolate music-bearing WWI POW items by language/community; exclude speech-only records and document wartime power asymmetry.
6. Continue globally balanced discovery across Africa, Asia, Latin America/Caribbean, Pacific, Middle East and eastern/southeastern Europe; then return to Pros and Cons Postcards, Fort Madison K-155 and Waupun.


### Aoi-tori follow-up — two dated historic tape trails found (2026-11-15)

- Mami Tanaka's 2016 Ritsumeikan doctoral thesis, pp. 164–170, establishes two additional tape histories:
  1. **1963 Carville tape:** Mieko Kamiya carried an Aoi-tori tape to Carville Sanatorium in the United States during 25–30 July 1963; it was played to John Wick and senior staff. The account mentions Nagashima waves and the “Megumi no Kane” bell and says patients carried a recorder around for days to make the tape. This appears to be a composite island soundscape plus Aoi-tori musical context, not necessarily a clean concert master. No Carville accession/custody is known.
  2. **1967-05-12 Ibaraki Hospital concert:** after Aoi-tori's first off-island concert, Kondo sent Kamiya a tape. Her 21 May 1967 reply (quoted as previously unpublished correspondence) says she listened to it in full, intended to return it, and could not make a copy at home; she offered to copy it at Nagashima's Lighthouse. A Lighthouse duplicate is possible, not proven. The original may have been returned to Kondo.
- The same thesis refers to a Lighthouse tape library in 1976 correspondence. The 2024 Kamiya Library catalogue is a paper-library inventory, not proof of audio holdings.
- Keep these two tapes separate from the 2017 Sasaki-held “鶴島哀歌” / concert recordings. The 1968-06-24 programme lists Sasaki singing “鶴島哀歌,” but the tape he played the interviewer has not been matched to that event.
- **Sources:** https://ritsumei.repo.nii.ac.jp/record/10057/files/k_1115.pdf ; https://leprosy.jp/people/plus08/ ; https://kouhou.niigatakenjinkai.com/?p=17685 ; https://www.town.nagi.okayama.jp/moca/news/20260207.html ; https://libro-koseisha.co.jp/leprosy/9784774408392/ . Full provenance notes in environment-leads.md and coop.log.md.
- **Next exact steps:** (a) follow Tanaka's footnote/source trail for Kamiya's original 21 May 1967 letter and the 1963 Carville visit; (b) identify Carville's surviving audiovisual collections and any transfer/custody record; (c) locate the Lighthouse tape library in Nagashima residents' / History Museum records; (d) ask Umitaro Abe's “Aoi Tori no Harmonica” preservation project for item-level tape inventory, dates, formats, digitisation status and rights/access.
- No public audio URL or permission route verified; no Grok request.

### Revised immediate queue
1. Japan / Aoi-tori: pursue the 1963 Carville and 1967 Ibaraki tapes through Carville records, Kamiya correspondence, Nagashima Lighthouse tape library, History Museum, and Abe's preservation project. Do not merge tapes or infer a surviving accessible master.
2. TLM Canada / Effect:Hope: item-level AV inventory for tapes from Purulia, Chandraghona, Bhutan, Irian Jaya, Papua New Guinea and Thailand; identify “More Than a Prophet” cassette; establish content and restrictions.
3. Chile / Chacabuco: resolve the two MMDH audio objects and disputed cueca credits; direct media/access/rights.
4. Nigeria / Uzuakoli: post-1977 Choir of the Leprosy Colony vinyl discography and authorised source.
5. Austria / Phonogrammarchiv: music-bearing WWI POW records by language/community, with critical provenance.
6. Keep global regional balance; return to Pros and Cons Postcards, Fort Madison K-155 and Waupun after the above.


### Aoi-tori / Carville — US archival cross-check (2026-11-15)

- NLM's **Edgar B. Johnwick Daybooks, MS C 374 (1956–65)** are a direct contemporaneous source to check for Mieko Kamiya's 25–30 July 1963 Carville visit and playback of the Nagashima tape. Dr. Johnwick was Carville chief; the thesis's “John Wick” likely refers to him, but confirm in the daybook. Collection is unrestricted for research access onsite; finding aid status is an unverified partial draft. https://findingaids.nlm.nih.gov/repositories/ammp/resources/johnwick374 .
- Daughters of Charity Carville RG 11-2-8-4, Box 54 Folder 2 lists “16 mm reel to reel tape of patients, etc.” This is only a possible AV inventory lead; it is not linked to the Aoi-tori tape. Clarify format and provenance with archive staff. The finding aid imposes some restrictions and requires Daughters of Charity Communications Director permission for publication of archival audio/video/text/images. https://docarchivesblog.org/wp-content/uploads/2023/02/11-2-carville-la-national-hansens-disease-center-finding-aid.pdf .
- HRSA's National Hansen's Disease Museum holds Carville Daughters of Charity and USPHS collections and interprets patient culture/activities, but no published evidence says it holds the Nagashima tape: https://www.hrsa.gov/hansens-disease/museum .
- Next: inspect/request Johnwick's July 1963 daybook entries; clarify Box 54 Folder 2 with Daughters Archives; ask Carville Museum about any Japanese audio transfer. No assumption that any Carville item is the Aoi-tori tape.


### Aoi-tori / Carville — public-release and catalogue audit (2026-11-15)

- Abe's official NEWS archive (visible entries through Oct 2026) has no indexed “青い鳥”, “青い鳥のハモニカ” or “近藤宏一” announcement and no historic-audio collection link. This is a bounded negative search, not proof of no release. Nagi Museum's Feb 2026 page still documents ongoing research into Kondo's scores/recordings and work toward publication.
- NHDM's 2023 event page links a YouTube record of the “青い鳥のハモニカ” programme. The page identifies Abe, Takeo Toyama and Itoko Toma as contemporary performers/reader; classify this as modern interpretation, not an original Aoi-tori tape. NHDM event contact: event@nhdm.jp.
- NLM Directory of History of Medicine scope for Carville describes Daughters of Charity correspondence, publications, photographs, clippings and diaries, and USPHS Medical Officer daybooks. Edgar B. Johnwick Daybooks MS C 374 (1956–65) are daily hospital records, not an identified audio holding. NLM's later oral-history/video collections do not establish custody of the 1963 Japanese tape.
- Daughters of Charity Provincial Archives' public ILA description emphasises correspondence, publications, photos, clippings and Sisters' diaries; its public exhibit includes digitised cassette interviews, but not the Nagashima tape.
- Sources: https://www.umitaroabe.com/news/ ; https://www.town.nagi.okayama.jp/moca/news/20260207.html ; https://www.nhdm.jp/en/events/list/4899/ ; https://hmddirectory.nlm.nih.gov/hmddir/print_collection/223 ; https://findingaids.nlm.nih.gov/agents/corporate_entities/39 ; https://leprosyhistory.org/archive/archive853/ .
- **Next action:** ask Carville Museum / Daughters Archives whether Kamiya's July 1963 visit appears in Johnwick's daybook, Sisters' annals or visitor files, and whether a Japanese tape, accompanying correspondence or transfer/accession record survives. Keep the 1963 Carville soundscape, 1967 Ibaraki concert tape, Sasaki's later recording, and modern tribute performances distinct.


### New source development — Uzuakoli vinyl and Aoi-tori hand-off correction (2026-11-15)

- **Uzuakoli:** John Manton's 2015 programme page explicitly says it uses original vinyl as remastered recordings of the Uzuakoli Choir of Harcourt Whyte, alongside separate contemporary Achinivu arrangements, oral history and field recordings. This confirms original vinyl source access by 2015 but not label, date, tracklist, owner or rights. Follow production records through John Manton / Anthropologies of African Biosciences, The Arts & Culture Unit and engineer Vivien Jones; ask for source log, permissions, remaster files and owner metadata. The 2021–23 Achinivu-Harcourt Whyte Choral Association score project is a local network lead, not an audio reissue.
- **Aoi-tori correction:** Tanaka thesis pp.164–166 says Kamiya listened to Kondo's 12 May 1967 Ibaraki concert tape in full. She offered to make a copy at the Lighthouse if needed, but her letter closes by saying she would return the original to the Lighthouse and leave it with someone there the following Tuesday. A duplicate is not confirmed; planned hand-off of original is explicit, but completion/permanent deposit is unconfirmed. Search Lighthouse/Blind Association committee papers and resident tape collections, not just formal archive catalogues.
- Sources: https://africanbiosciences.wordpress.com/publications/radio-uzuakoli-in-music-and-medicine/ ; https://www.shf.or.jp/en/information/21652 ; https://ritsumei.repo.nii.ac.jp/record/10057/files/k_1115.pdf .
- No authorised vinyl/audio download link; no Grok request.

### Revised queue
1. Japan / Aoi-tori: trace 1963 Carville tape, 1967 Ibaraki concert original and Lighthouse hand-off; keep all source tapes distinct; locate Abe preservation project's item inventory.
2. Nigeria / Uzuakoli: follow 2015 radio production chain for the original post-1977 choir vinyl source, remaster source log and rights; consult Achinivu-Harcourt Whyte Choral Association about physical disc custody.
3. TLM Canada / Effect:Hope: item-level inventory for six named audio-tape locations and “More Than a Prophet” cassette.
4. Chile / Chacabuco: exact object/media/credit reconciliation.
5. Austria / Phonogrammarchiv: music-bearing WWI POW items, language/community-specific and critical provenance.
6. Continue global region rotation, then Pros and Cons Postcards, Fort Madison K-155 and Waupun.


### Uzuakoli follow-up — provisional LP discography and chronology conflict (2026-11-15)

- New catalogue leads: *Harcourt Whyte And Choir*, ARC 1059 (specialist record-market index says 1975); *Harcourt Whyte & Choir Vol 2*, ARC 1106 (index says 1974). An unlicensed metadata page for ARC 1059 supplies a provisional 12-track list, Arc Studio Lagos / Writers Workshop of East Central State attribution, Nnamdi Olebara leader/vocal credit, and says a Tabansi ARC 1059 copy is a 1977 reissue. This is not a verified official discography and must not be used as a download source.
- The 1974/75 listing conflicts with Music In Africa's claim that the Uzuakoli Leprosy Colony choir recorded Whyte compositions after his 1977 death. Possible explanations include inaccurate market dates, an earlier/other ensemble, or an original/reissue distinction. No ARC catalogue number is yet matched to Manton's 2015 original-vinyl sources. Preserve the discrepancy.
- Achinivu-Harcourt Whyte Choral Association / Arochukwu Incorporated has a current community-preservation pathway: two volumes of *Messages for Life and Living* (100 scores/translations, 2022–23) and a commemorative concert announced for 26 Nov 2023 on Aromouthpiece TV. Modern community choir, not historical Uzuakoli patient-choir audio. ILEP partner listing is a network lead.
- Next exact queue: verify ARC 1059/1106 from sleeve/label/matrix scans and Nigerian label catalogues; establish dates, personnel, original vs reissue; ask John Manton for 2015 source log and catalogue IDs; locate authorised archive of the 2023 association concert; then return to Japan Aoi-tori and TLM/Effect:Hope inventory. No unauthorised rip, no Grok request.


### Uzuakoli LP follow-up — ARC vs Tabansi lineage (2026-11-15)

- Refined label evidence: specialist listing attributes ARC 1059 (1975) and ARC 1106 (1974) to label entity “ARC (21)”; an unlicensed metadata page lists a 1977 Tabansi reissue version of ARC 1059. Treat a possible ARC original → Tabansi reissue as a working hypothesis only; no physical labels, sleeve scans or matrix evidence located.
- The provisional 12-track list and Nnamdi Olebara leader/vocal credit on ARC 1059 are not independently verified. A 2013 memorial-concert report documents Olebara performing at a Harcourt Whyte memorial, not his LP role. Do not assume ARC 1059/1106 are the posthumous Choir of the Leprosy Colony source used by John Manton in 2015. Separate 1974/75 ARC issues, alleged 1977 Tabansi reissue and Manton's unidentified original-vinyl source lineage until matched.
- Next: obtain physical label/sleeve/matrix evidence for both LPs and the alleged Tabansi reissue; request/locate Manton's source log; verify choir identity and recording date. No authorised acquisition route, no Grok request.

### Aoi-tori Gakudan — 2025 publication target / 2026 status check (2026-11-15)

- **New lead:** In a 2025-02-11 lecture (report published 2025-05-20), Umitaro Abe said almost all Aoi-tori concerts had been recorded; an event organiser had shown him historical sound sources and materials; and he aimed to prepare a public-listening selection and issue an audio collection titled 「近藤宏一の過去と現在」 during 2025. This verifies a stated publication target, not release.
- **Current check:** Nagi Museum of Contemporary Art's official February 2026 page still describes Abe/Toyama's ongoing research into Kondo's surviving scores and sound sources, recording toward audio production and contact with people connected to him. It does not announce a completed historical-audio release or provide item-level metadata. Targeted Japanese searches did not locate a release announcement. Record as **no public release verified**, not “not released.”
- **Important separation:** 2023 “青い鳥のハモニカ” and 2026 Abe/Toyama concerts are contemporary reinterpretations/new performances, not historical Aoi-tori masters. NHDM's 2018 exhibition lists instruments, scores, costumes, programmes and photographs, not sound carriers. Its 2007 exhibition shows a May 1974 performance photo and a Kondo event but no audio accession. NHDM photo list identifies Zhao Gen-zai images B053/B054 as 1970 Aiseien “waiting to perform” / “performance” photos.
- **Sources:** https://kouhou.niigatakenjinkai.com/?p=17685 ; https://www.town.nagi.okayama.jp/moca/news/20260207.html ; https://www.nhdm.jp/en/events/list/2241/ ; https://www.nhdm.jp/events/list/2327/ ; https://www.nhdm.jp/hansen/wp-content/uploads/2023/pdf/list_b.pdf ; https://www.nhdm.jp/en/events/list/4899/ .
- **Next exact task:** ask whether the planned collection was completed, delayed, renamed or privately circulated; identify the event organiser and source-item inventory; separate original concert masters from field/soundscape tapes, dubs, excerpts and new arrangements; query Aiseien History Museum/NHDM about sound-carrier holdings. Preserve separate 1963 Carville, 1967 Ibaraki/Lighthouse, 1968 “鶴島哀歌” and Sasaki-held tape identities until matched.



### TLM Canada / Effect:Hope — AV inventory and “More Than a Prophet” cross-archive check (2026-11-16)

- The ILA archive description for TLM Canada (later Effect:Hope) explicitly lists audio tapes made at Purulia, Chandraghona, Bhutan, Irian Jaya, Papua New Guinea and Thailand. No item-level IDs, titles, dates, recordists, languages, contents, formats, durations or access/rights are supplied. These remain AV leads, not music candidates.
- Boxed slide collection Box 14: 80 slides (1978) with cassette and pamphlet notes titled **“More Than a Prophet.”** Contents unknown; do not assume music or link it to the six tape groups.
- **New possible cross-archive match:** Wheaton College Billy Graham Center Archives' OMF CN215 finding aid independently lists an undated “More Than a Prophet” programme, described as work among Malay Muslims in Thailand: slide Box 28 title cards S1842–S1845; tapes T45 Cantonese, T46 Mandarin, T47 English; script Folder 17-5. This may be the same programme or a related distribution copy, but could also be a title collision. Keep separate until slides, cassette label/duration, script, language and producer credits are compared. Source: https://www2.wheaton.edu/bgc/archives/Guides/cn215%20slide-tape%20grid.pdf .
- ILA page lists Bob MacFarlane as Effect:Hope contact, but its archive entry dates to Jan 2016; no contact has been made. TLM International has paper files for Purulia (1908–87), Chandraghona (1921–87) and Bhutan (1964–72 onward), useful as contextual transfer/correspondence leads, not proof of audio custody.
- Sources: https://leprosyhistory.org/archive/archive714/ ; https://leprosyhistory.org/archive/archive718/ ; Wheaton CN215 PDF above.
- **Next exact steps:** item-level TLM tape inventory; Box 14 slide/cassette/script metadata and rights; compare the TLM and OMF “More Than a Prophet” productions; search TLM International regional paper files for AV references. If music appears, distinguish local participant/community music from missionary performance or incidental programme audio and assess consent/colonial power. No authorised music download URL; no Grok request.



### Austria / Phonogrammarchiv — POW series item-level music identification (2026-11-16)

- **Specific musical item:** Phonogrammarchiv **Ph 2647**, Psalm 126 / “Shirat tsiyon” (“Song of Zion”) plus a fragment of “Hatikvah” (“The Hope”), sung by Isaak Isaakon at Theresienstadt/Terezín POW camp, recorded by Rudolf Pöch on 6 Oct 1915. Identified in Benjamin Fox-Rosen's 2026 “Objects and the Archive”; official edition Series 17/1, CD 1, track 8 (2018). Historical protocol descriptors “Bergjude” and “Tatisch” require contextualising; Judeo-Tat is a qualified language interpretation, not a certain identity claim. Protocol reportedly includes Hebrew text, transliteration and German translation.
- The recording belongs to a racial-anthropological research project using POWs as subjects. Preserve coercive wartime context and power asymmetry; use Monique Scheer's “Captive Voices” and the Phonogrammarchiv's own critical commentary.
- Series 17/1–5: about 200 language/music recordings of former Tsarist army POWs, especially Eger/Cheb, Reichenberg/Liberec and Theresienstadt/Terezín. Official digitised CD editions include data CDs with protocol scans/transcriptions/commentary. Audit item-level musical tracks.
- Series 17/6 Italian POW recordings from Mauthausen/Marchtrenk, 1918, are described as spoken rural stories/language samples; Marchtrenk installation used seven speech recordings. No musical content identified; keep out of candidate list unless a music-bearing item is found.
- Catalogue covers ~85% holdings; research access varies by depositor agreement; archive notes limited services through Jan 2027 due to relocation. Copy enquiries pha@oeaw.ac.at. Series 17/1 is an authorised physical CD + data CD-ROM publication, ISBN 978-3-7001-8226-9, listed €25; no authorised digital download URL verified, no Grok request.
- Sources: https://www.researchcatalogue.net/view/3355133/4340708 ; https://www.oeaw.ac.at/en/phonogrammarchiv/phonogrammarchiv/detail/recordings-from-prisoner-of-war-camps-world-war-i-series-17/1-5-1 ; https://www.oeaw.ac.at/en/phonogrammarchiv/publications/audio-and-video-publications/the-complete-historical-collections-1899-1950/ ; https://catalog.phonogrammarchiv.at/ ; https://www.oeaw.ac.at/phonogrammarchiv/detail/recordings-from-prisoner-of-war-camps-world-war-i-series-17/6 ; https://www.basis-wien.at/de/events/99197 ; https://www.academia.edu/14483841/Captive_Voices_Phonographic_Recordings_in_the_German_and_Austrian_Prisoner_of_War_Camps_of_World_War_I .
- **Next:** item-level audit of Series 17/1–5 musical tracks and languages; confirm Ph 2647 access/playback and physical edition availability; then Chile Chacabuco two-object/credit reconciliation and balanced global discovery.



## Research checkpoint — 2026-11-16 continuation

**Completed this run**
- Read this checkpoint first, then method.md, environment-leads.md, coop.log.md and TRACK_MAPPING.md.
- Austria / Phonogrammarchiv: verified all five Series 17/1–5 language groupings and exact publication configuration/pricing from the Academy publisher catalogue. The sets are physical audio CDs plus data CD-ROMs; 17/1 has one audio CD, 17/2–5 two each, all listed €25. The five ebook catalogue links are not verified as direct audio downloads. No new song-level item beyond Ph 2647 identified in this pass. A complete item/protocol audit is still needed; no Grok request.
- Chile / Chacabuco: added first-person Luis Cifuentes account from Discoteca Nacional Chile. It clarifies clandestine tape and LP side-A provenance, distinguishes side B's later European re-recordings, names Los de Chacabuco and its members, and gives a first-person joint authorship credit for “El suertudo” / “El puntudo” (Víctor Canto + Luis Cifuentes; composed Nov 1973–Feb 1974). Kept the thesis's conflicting Roberto Parra music credit and “Luis Fuentes” typo visible. The MMDH 23:36 and 2:03 archive objects remain distinct; relation to the LP cassette master is not proven. No stable direct audio URL or authorised download/reuse route found. No Grok request.
- Updated environment-leads.md and coop.log.md; TRACK_MAPPING.md intentionally unchanged.

**Exact active queue**
1. **Austria / Phonogrammarchiv:** obtain/audit item-level Series 17/1–5 track lists and original protocols; map each music item to Ph call number, singer, language/community, camp and recording date. Prioritise local-language titles and current scholarly/community context. Check whether Ph 2647 is directly playable and whether ebook links contain only documentation or audio files. Keep coercive POW research context explicit; no audio audition claim.
2. **Chile / Chacabuco:** identify MMDH internal IDs and underlying media URLs for the 23:36 and 2:03 objects; compare track/timecodes and provenance with LP VPA 8344 and 2003 *Pisagua + Chacabuco*. Verify VPA 8344 from primary label/sleeve/matrix evidence. Locate the 2014 Cantos Cautivos testimony pages for “El suertúo” and “El puntúo”; reconcile credit discrepancy without erasing Cifuentes' first-person account. No unauthorised rip; no download request without an authorised acquisition route.
3. **Japan / Aoi-tori:** resume distinct 1963 Carville soundscape and 1967 Ibaraki/Lighthouse tape trails; query Abe project's item inventory and whether 「近藤宏一の過去と現在」 was completed, delayed, renamed or privately circulated.
4. **Nigeria / Uzuakoli:** pursue John Manton 2015 source log and original post-1977 Uzuakoli choir vinyl identity; keep ARC 1059/1106 chronology and personnel unresolved until label/matrix evidence.
5. **TLM Canada / Effect:Hope:** item-level inventory for six location audio groups and Box 14 “More Than a Prophet”; compare Wheaton OMF CN215 copies without assuming identity/music.
6. Maintain regional rotation and small-web/local-language discovery across Africa, Asia, Latin America/Caribbean, Pacific, Middle East and eastern/southeastern Europe. Then Pros and Cons Postcards from the County P.I. markers, Fort Madison K-155 and Waupun/Upheaval. Soledad first pass remains complete unless new liner/authorship/access evidence emerges.

**No transfer activity:** no audio downloaded or uploaded; no archive contacted; no permission claimed. TRACK_MAPPING.md unchanged because no authorised downloadable item was verified.


## 2026-11-16 — Global small-web discovery pass / Japan Ōshima Seishōen

- **New verified recording trail:** Ōshima Seishōen resident Takashi Tōjō (東條高) made three CDs with Tomoe Sawa: *生かされて* (2003), *この道* (Feb 2021; five songs), and *こころ* (Apr 2026). The 2026 disc includes at least “こころ” and “君といつまでも”; full tracklist and catalogue metadata remain to be obtained. Local KSB/RSK reporting documents his own singing and the eight-day final recording process over four weeks. Tōjō died 21 Sep 2026, aged 96.
- Sawa's official Como Esta order page lists *東條高 こころ* at ¥1,000. This is an authorised physical CD order route, not a download. TRACK_MAPPING.md now has a Grok acquisition request; the known track titles are listed and the missing complete tracklist is explicitly flagged. Do not treat purchase as reuse permission; rights for the 2026 master remain to be confirmed.
- **Discovery path:** local Japanese Blogger page 「明日への言葉」 (28 Jun 2025) → National Diet Library Reference Cooperative Database response by the National Hansen's Disease Museum Library → local KSB/RSK reporting → artist's official order page. The 23 sanatorium-song research corpus is contextual, not 23 confirmed extant recordings.
- **Small-web infrastructure:** Weirdnet, Marginalia, Wiby, Neocities archive/music tags and old-web directories/web-archive routes added to active practice. Small-web pages are discovery evidence, not automatic proof. Search false positives screened rather than promoted.
- Sources: https://asuhenokotoba.blogspot.com/2025/06/ ; https://crd.ndl.go.jp/reference/entry/reference/show?asc=desc&fi=3_%E6%96%87%E7%8C%AE%E7%B4%B9%E4%BB%8B%E3%80%80%E4%BA%8B%E5%AE%9F%E8%AA%BF%E6%9F%BB&id=1000358845&lsmp=1&mcbt=200&mcmd=200&mcup=200&oldasc=desc&oldmc=100&oldst=update&page=ref_view&rnk=1&st=update ; https://news.ksb.co.jp/article/16531366 ; https://newsdig.tbs.co.jp/articles/rsk/2727313 ; https://comoesta.co.jp/contact/ ; https://directory.weirdnet.org/ ; https://search.marginalia.nu/ ; https://wiby.me/ .

**Next exact tasks:** obtain *こころ* booklet/full tracklist and recording credits; confirm 2026 master/composition/performance rights; audit *この道* separately; investigate historical Ōshima Seishōen ensembles and any original resident-made tapes. Continue deliberate regional rotation, with local-language/small-web discovery before English-language aggregation.


## Repository collaboration rule — main branch only

All agent and owner collaboration must happen on `main`. No feature/agent/task branches. Verify main before writing, commit/push there, and re-fetch to confirm. If another branch appears, inspect its unique commits and integrate only useful material into main without overwriting newer main content. Close stale PRs and delete obsolete branches when available; never force-push shared history. If branch deletion is unavailable, say so clearly and leave the branch pointer aligned with main so it contains no unique work.


## 2026-11-16 — Brazil follow-up: Banda Cazuluz source triangulation

- Improved the Cuiabá Banda Cazuluz lead with a contemporary Mato Grosso state-government/Sejusp report dated 18 Sep 2010. It says the band was formed by incarcerated residents of Centro de Ressocialização de Cuiabá, had been rehearsing for about a year, and had produced one CD inside the unit; it explicitly says the CD included four compositions by band members alongside songs by Legião Urbana, Zé Ramalho and Paralamas do Sucesso. This is stronger local primary-adjacent evidence than the 2011 blog repost.
- The 27 Aug 2011 G1 report (preserved in a local Blogspot archive) says the group had recorded two CDs by then, with five incarcerated members and a makeshift studio in a disused bathroom. Diario de Cuiabá's same-day report describes eight members; preserve the discrepancy rather than choosing a headcount. A local radio-program Blogspot entry from Sep 2011 says SoulGuetto visited the group and accompanied its activities, providing another small-web path.
- The two-CD/one-CD sequence may reflect a second release between 2010 and 2011, but no catalogue, tracklist, disc image, current custodian or authorised acquisition route has been verified. 2010 official report names four original songs but does not title them. Keep as a strong historical recording lead, not an extant audio item until a disc/copy is found.
- Sources: Sejusp/Toque de Alerta, 18 Sep 2010, https://toquedealerta.com.br/noticia/22350/Musica_transforma_a_vida_de_reeducandos_do_Centro_de_Ressocializacao_de_Cuiaba ; G1 report preserved at https://liberalcuiaba.blogspot.com/2011_08_21_archive.html ; Diario de Cuiabá, 27 Aug 2011, https://www.diariodecuiaba.com.br/policia/reconstruindo-a-vida-com-musicalidade/398343 ; SoulGuetto blog, 30 Sep 2011, https://programasoulguetto.blogspot.com/ .

**Next:** find CD artwork/tracklists, identify who retained the discs, and search local broadcast/photographic collections. Do not request files from former band members without a consent-sensitive, project-owner-approved contact plan.


## 2026-11-16 — Brazil / Juliano Moreira source genealogy and MIS-PA lead

- The Portuguese Blogger story traces to Luiz Gonzaga de Freitas Filho, *Memórias de um Hospital Psiquiátrico: Contos sobre casos no interior de um hospício* (1st ed., 1999). Author confirms academic residency at former Hospital Público Juliano Moreira in Belém and explicitly says character names were changed. “Raul” is a pseudonym; no deanonymisation.
- The memoir reports five songs and three speeches recorded on cassette by a patient trio with nurse coordination. Tape survival/custody remains unknown.
- Pará Secult says MIS-PA holds cassettes, CDs and reel tapes (mis.para@gmail.com). Plausible local archive enquiry only; no custody claim. See environment-leads.md and coop.log.md for sources and exact caveats.
- Next: search MIS-PA catalogue and local library/archive records for the tape, without identifying pseudonymous patients; no Grok request.


## 2026-11-16 — India / Tinka Tinka Jail Radio corpus

- Added IM-037: Tinka Tinka Foundation's “Music in Jail” index documents more than a dozen inmate-created songs from Indian jails. Strong item-level leads include Jai Bhagwan (Jind, 2023–24), Suchit Narang (Dehradun signature tune, 2023), ten-inmate Karnal theme song (2021), Kashish (Panipat, 2021), Jitendra (Rohtak, 2021), Sheru (Ambala, 2021), and Shyam Bai (Bilaspur, 2017). See environment-leads for item URLs, exact credits and caveats.
- Distinguish original inmate composition/lyrics from externally supplied poems, institutional theme songs, reworkings and visiting production. Do not merge Jind original with Dehradun adaptation until audio comparison. Shyam Bai's track has no direct audio URL yet.
- Tinka Tinka's site explicitly reserves rights; official YouTube streams are not download/reuse permission. No Grok request.
- Next: audit individual official episodes and metadata, especially the women-led Bilaspur item; seek authorised catalogue/listening details, not file rips.


## 2026-11-16 — Tinka Tinka item-level credit audit

- Rechecked the Foundation's official “Jail Radio: Jind” page against its “Music in Jail” index and the episode 71–80 index. The official Jind page identifies Episode 81, “आए अवध में राम” / “Prayers from Jind Jail,” as a song written and sung by Jai Bhagwan, with four incarcerated instrumentalists: Ramroop (dholak), Shashi (harmonium), Sunil (matka) and Govind (matka). Official item URL: https://tinkatinka.org/jail-radio-jind/ ; official index: https://tinkatinka.org/jail-music-2/ .
- Keep Episode 81 distinct from Jai Bhagwan's earlier original song released 25 Dec 2023 (“गमे ज़िंदगी में मुस्कुराना सीख ले…”). The same Jind page says the earlier composition was shared with Dehradun, where Dr Suchit Narang, Arun and Rohit made a new composition for Episode 77. Do not call Episode 77 the same recording or assume it is a straight cover without audio comparison.
- The Foundation index lists Episode 81 with a 21 Jan 2024 date and Episode 77 with a 25 Dec 2023 release date. It also lists Episode 90, “World Music Day / Musical creations through jail radio,” dated 21 Jun 2024, and states that more than 105 podcast episodes had been released by Jan 2025. These establish a larger official podcast corpus, but Episode 90's index citation alone does not identify additional discrete songs or performers; do not inflate IM-037's item count from episode count.
- The Foundation describes Jai Bhagwan as an undertrial inmate and says the Jind song was released through Tinka Jail Radio. Preserve the published credit, avoid additional identity research, and treat official YouTube links as listening/viewing routes only. The site reserves rights; no download/reuse permission is implied.
- No new evidence for Shyam Bai's 2017 Bilaspur master, custody, track title or direct authorised audio URL was found in this pass. Her item remains a separate lead, not a newly verified downloadable recording.
- No archive contact, audio download, or listening session was made. No candidate status change. Next: ask Tinka Tinka for an item-level catalogue/tracklist and authorised listening details for Episode 81 and Episode 77, plus the current custodian and authorised stream for Shyam Bai's 2017 recording.


## Owner direction update — diversify beyond prisons (2026-11-16)

The owner has explicitly said that the tracks currently in the Insane Music Drive are overwhelmingly prison-related and that discovery must look in more directions. Treat this as a standing editorial correction, not a one-off exception.

- **Prisons are one environment, not the project's identity or default search lens.** Keep strong prison/camp records in the archive, but do not let them dominate the next discovery or curation passes.
- Prioritise non-prison discoveries until the shortlist and selected listening set are visibly more balanced. Do not impose a rigid numerical quota; make the balance a deliberate editorial check at the end of each run.
- Rotate across non-prison pathways: intentional communities/communes and DIY studios; home-recorded and private-press cassette networks; community mental-health groups and disability-led arts (without reducing artists to diagnoses); sanatoria and other health settings; refugee/diaspora and migrant communities; itinerant/rural/remote communities; community radio and peer-run studios; local-language vernacular scenes; outsider-art workshops; spiritual/ceremonial and local cultural groups; women's and other under-documented community music histories.
- Do not replace a prison-only bias with a psychiatric-institution-only bias. The next passes should include both institutional and non-institutional, self-organised music, and should deliberately move among regions, languages, genres and recording formats.
- Newly documented non-prison candidates from this pass: Mágicos do Som (CAPS Usina de Sonhos, Brazil; second CD Saúde Musical reported 2013; title lineage unresolved) and Harmonia Enlouquece (CPRJ, Brazil; five-album/66-song corpus, fifth album listed in 2026). See environment-leads.md and catalogue.md for evidence and cautions.
- Existing non-prison candidates to bring into the next curation pass include ARSCH (IM-011; commune/barn studio), Takashi Tōjō (IM-036; Ōshima Seishōen resident-led CDs), Anders Enevig (IM-022; itinerant-community field recordings), Ernie Althoff / Clifton Hill (IM-030; community music centre), Sampari and East Awin refugee/diaspora material, and Dragon Café / Thorvaldsen peer-run music environments. These are different histories and should not be collapsed into a generic marginal category.
- **Drive access limitation:** the Google Drive connector is currently disabled by the workspace administrator and cannot be installed by the user in this workspace. This run did not inspect, move, upload or alter any Drive tracks. Repository research and curation recommendations are not a claim that the Drive folder has been changed.

### Immediate non-prison queue

1. Trace the physical CD / authorised audio / full tracklist for Mágicos do Som; resolve the repeated Saúde Musical title between the 2000/first-CD and 2013/second-CD accounts.
2. Verify the authorised current listening route and full credits for Harmonia Enlouquece's 2026 fifth album; select tracks whose documented themes broaden the set beyond institutional narratives.
3. Identify the 1998 Cancioneiros do IPUB CD/songbook and tracklist; treat Black Confusion as context only until a specific extant recording is found.
4. Add at least one non-institutional discovery pass in DIY/private cassette culture, intentional communities, refugee/diaspora, rural/remote or local-language music before returning to prison-specific follow-ups.
5. Review the actual Drive selection once an authorised Drive connection is available; then recommend additions/removals by track, not merely by environment label.

No audio auditioned, no Drive files accessed, no contact made, and no rights cleared in this pass.


## 2026-11-16 — Mágicos do Som first-CD audio lead

- Found contemporaneous 2002 *Voices Resources* page naming “Preconceito” as a Mágicos do Som / *Saúde Musical* recording sung by composer Regina Lúcia Serrão; page says clip presented with composer/coordinator approval. Its linked MP3 now returns 404, so no listening/audition claim.
- UFF 2007 dissertation identifies the song as written and sung by Serrão in 2000 and says audio is on its annex CD-ROM. This narrows first-CD metadata and supports distinguishing the first disc from the 2013 ten-song second CD, despite the repeated title *Saúde Musical*.
- No download, audio audition, contact or rights clearance. Immediate next action: request authorised access to the dissertation annex / first-CD copy and 2013 sleeve/tracklist; then move to Harmonia Enlouquece or non-institutional DIY discovery rather than further prison-specific leads.


## 2026-11-16 — Harmonia Enlouquece fifth-album metadata checkpoint

- State Health Secretariat (2026-08-15) reports launch of fifth album *O Quinto dos Infernos*, 13 tracks, 11 previously unreleased Hamilton de Jesus Assunção compositions. Apple/Amazon list a 13-track album as *Esse 5° É Dos Infernos*, dated 2026-07-05. Retain title/date variation until sleeve or rights-holder confirmation.
- Official group site reports five albums/66 songs, mixed user/professional ensemble and broad everyday/social themes; it links to Spotify. No audio auditioned, no rights cleared.
- Next: audition via official route if accessible and select only tracks with verified themes; avoid making choices from titles alone. In parallel continue non-prison/non-institutional discovery.


## 2026-11-16 — completed non-institutional Brazilian cassette discovery pass

- Added two PARTIALLY VERIFIED, PROMISING recording-level entries from the Brazilian underground cassette archive Demo-Tapes Brasil: IM-040 G.D.E., No Art Pictures (1995), and IM-041 G.D.E., Synthetic Apocalypse (1996).
- The archive curator says both G.D.E. audio sources were supplied by the band and the covers came from his private collection. The 1996 demo is reported as recorded on four tracks in May 1996. A Portuguese-language academic study independently corroborates Demo-Tapes Brasil as a substantial archive of Brazilian demo tapes, with audio, artwork and production metadata; it does not independently authenticate these two individual cassettes.
- Added adjacent leads for Caustic (home-studio/industrial), Os Rochas (Brasília, 1989) and Tubaína do Demônio (four-track São Paulo demo, 1993), without promoting them to the catalogue.
- This is a genuinely different, non-prison and non-clinical research environment: home studios, four-track production, private cassette circulation, fanzines, postal swaps and collector digitisation. It is pathway 9 in method.md, not a psychiatric-history claim.
- No audio downloaded or auditioned, no physical carrier inspected, no contact made and no rights cleared. Blog downloads are not assumed to be licensed for reuse.
- Sources and item-level metadata are in research/brazil-demo-tapes-small-web-2026-11-16.md; the new section is in environment-leads.md and catalogue IDs IM-040–IM-041 are in catalogue.md.
- Next: verify the 1996/1997 Synthetic Apocalypse distinction, establish item-level carrier/artwork/transfer provenance and a permission route, then rotate to another under-documented region rather than over-mining one Brazilian scene.


### Follow-up check — G.D.E. 1997 reference

- Checked Demo-Tapes Brasil's all-posts index after the 1995 post pointed to a further Synthetic Apocalypse (1997). The visible index lists G.D.E. No Art Pictures (1995) and Synthetic Apocalypse (1996), but no standalone 1997 G.D.E. post. The 1997 reference remains unresolved; do not create a third ID or merge versions without a tape/cover/tracklist comparison.
- Source: https://demo-tapes-brasil.blogspot.com/p/todos-os-links.html .


## 2026-11-16 — Philippine Cordillera cassette / community-music pass

- Rotated from Brazilian underground rock to the Philippines, focusing on Cordillera local-language cassette culture, community cultural organisations and movement-linked music.
- Added IM-042, Salidummay / Dap-ayan ti Kultura iti Kordilyera (DKK), as PARTIALLY VERIFIED / PROMISING. The ten-song cassette is documented in Michiyo Yoneno-Reyes' ethnomusicological dissertation and the 2023 *Lakbayan* exhibition catalogue; a current Spotify listing also gives ten tracks.
- Preserved the unresolved first-cassette date discrepancy: 1987 in the exhibition catalogue and platform metadata; 1989 in the dissertation. No label/J-card or original carrier has been inspected, and the platform's digital object has not been linked to a specific cassette master.
- Context: DKK is a cultural alliance associated with the Cordillera Peoples Alliance; the cassette is situated in community cultural activism around Cordillera autonomy, land, dams and logging. Do not treat the collective as representative of every Cordillera community or salidummay as a uniform ancient regional genre.
- Additional 1992 and 1995 DKK cassette titles are leads only. No separate IDs assigned pending item-level audio/edition verification.
- No audio downloaded or auditioned, no physical carrier inspected, no archive/collective contacted and no rights cleared.
- Detailed dossier: research/philippines-cordillera-salidummay-2026-11-16.md. Environment and catalogue updated.
- Next: verify the original cassette/J-card and 1987/1989 discrepancy; then broaden the Philippines pass to local-language rural/community artists and non-movement cassette networks. Do not over-focus on protest music alone.


## 2026-11-16 — Cordillera vernacular-country / local-language recording pass

- Broadened Philippine research beyond DKK/Salidummay and movement music to local Kankana-ey, Ibaloi and Ilokano country/pop, community radio, regional studios and cassette circulation in Baguio/Benguet.
- Fong 2007 describes the 1970s Ibaloy 45rpm wave, 1990s local-language cassette resurgence, makeshift Baguio studios and named leads: RJ Mero's “Benguet Country”; Cesar Pasiw / *Ivadoy Jen Country Songs*; Rio Felimon Cariño and D' Friends Band / video CD *Kabenguet an*; and “Batawa” as a song recorded by several artists. The 2006 *From the Boondocks* post provides a small-web trail for Rio “Filemon” Cariño.
- Mangahas' study documents the 2006 MPBC “Magic Countryhan” search and Kinnoboyan, a five-member Kankana-ey/Ibaloi group with a twelve-song original repertoire. It names Junie Rey Bag-ayan and Heintje Pis-Oy, whose later duo album *Inlove With You* (2014) includes titles overlapping the study's Kinnoboyan song list. This is a research lead only: do not conflate the 2014 duo album with the Kinnoboyan band's earlier twelve-song corpus or a cassette edition.
- Added contextual archive routes: UP Center for Ethnomusicology (large published/unpublished audio holdings); LOC AFC 1996/028 cassette *The Mountains Ring Out Their Joy* (1987); UP Diliman DALFCT linguistic fieldwork cassette project. None is automatically an Insane Music item; require item-level evidence and meaningful project relevance.
- No new catalogue ID assigned: the local scene is documented, but exact carrier/edition and a sufficiently specific marginal/DIY pathway for a particular release still need verification.
- Detailed dossier: research/philippines-cordillera-country-cassette-ecology-2026-11-16.md. Updated environment-leads.md.
- No audio downloaded or auditioned, no physical carrier inspected, no archive or artist contacted, and no rights cleared.


## 2026-11-16 — UPCE Sagada community archive / ReCollection follow-up

- Identified UPCE's 2025 “Collection and ReCollection” project with Saint Mary's School of Sagada, Inc. as a community-controlled Kankana-ey sound archive: 37 participants, 200 recordings (167 audio, 33 video), including songs, chants, instrumentals, interviews and recordings at weddings, a funeral and a gubbaw. Community members determined recording and preservation decisions; originals remain with SMSSI, while UPCE's off-site copy is room-use only.
- Identified UPCE's ReCollection trail: Maceda Collection material dating from 1953 repatriated to Sagada/Mountain Province in 2013; 1950s recordings returned to Sagada in 2020; and Ramon P. Santos' 1987 Bendian Festival recordings from Kabayan, Benguet, repatriated in 2017. Elders recognised voices in excerpts.
- These are concrete archival corpora, but public descriptions lack item-level catalogue IDs, performers, titles and carrier data. They remain contextual/archive leads, not Insane Music entries; no outsider/DIY status or resident authorship is inferred.
- Added detailed archive route and access constraints to the Cordillera cassette dossier and environment-leads. No catalogue ID assigned.
- Sources: https://upethno.upd.edu.ph/collection-and-recollection-recording-the-traditional-vocal-and-instrumental-repertoire-in-sagada/ ; https://upethno.upd.edu.ph/the-recollection-project-connecting-the-past-with-the-present/ ; https://upethno.upd.edu.ph/facilities/ .
- No audio downloaded or auditioned, no carrier inspected, no archive/community partner contacted and no rights cleared.

### NEXT
- Make a catalogue-level reference enquiry to UPCE for the 1987 Kabayan recordings, 1950s Sagada corpus and any itemised Kankana-ey/Ibaloi field recordings; ask about community review and access.
- Keep the 2025 SMSSI archive under community control; no request for unrestricted copies or assumption that UPCE can authorise access to originals.
- Continue identifying specific release media for Kinnoboyan / Rio Cariño / Cesar Pasiw without conflating local-language country music with outsider music.


## 2026-11-17 — IM-046 Ata Kak source-copy lineage update

The official 2025 *Obaa Sima (Anniversary Remaster)* page adds a second cassette-source witness. Awesome Tapes From Africa founder Brian Shimkovitz says that a Berlin acquaintance offered him a clean copy in early 2024; the label describes the 2025 remaster as sourced from a new, cleaner / nearly pristine cassette. This is distinct from the Cape Coast cassette bought in 2002 and used for the 2015 reissue. The new copy's generation and connection to the approximately 50 cassettes issued in Ghana in 1994 are not stated. The master DAT remains reported as degraded; do not equate either cassette transfer with the original master.

Updated the IM-046 dossier and catalogue, and added the source lineage to environment-leads.md. The 2015/2025 track-duration metadata differs slightly; no conclusion about speed, edits or performance identity is possible without audio comparison. No new IM-ID; status remains WELL-SUPPORTED. No audio auditioned, carrier inspected, contact made or rights cleared. A bounded search of Ghanaian news domains returned no relevant local item-level source; no Twi-language source was located in this pass.

Sources: https://atakak.bandcamp.com/album/obaa-sima-anniversary-remaster ; https://atakak.bandcamp.com/album/obaa-sima ; https://medium.com/@martynpepperell/ata-kak-interview-originally-published-via-the-405-a2f23c98b1f4 ; https://ra.co/news/27656 .

### NEXT
- Establish the Berlin cassette's acquisition/duplication history and whether it is one of the original 1994 copies.
- Compare 2015 and 2025 transfers, including the 2015 speed alternatives and track boundaries.
- Keep recording, 1994 issue, 2015 transfer and 2025 transfer as separate events.


## 2026-11-17 — IM-046 2025 release-note clarification

A closer read of the official 2025 Bandcamp page adds two important qualifications to the source-copy update. First, Shimkovitz reports that during a later visit to Kumasi he learned that Ata Kak's brother had sold “quite a few” cassettes, and that people in Kejetia market remembered the songs at funerals and local dance parties. This conflicts with the artist's 2015 estimate that only about three of approximately 50 copies sold. The exact sales and circulation are unresolved; do not repeat the three-copy estimate as settled fact.

Second, the 2025 page states that the original recording was made at a slower speed and that a slow-version download is included. It credits all songs as written/composed by Yaw Atta-Owusu and says the reissue is under exclusive licence from him, while marking the page all rights reserved. The Berlin source cassette remains a separate, generation-unknown copy; no audio comparison was performed.

The bounded Ghanaian press searches were English-language site queries; no Twi-language query was run. Local-language documentation remains an open search gap.

Source: https://atakak.bandcamp.com/album/obaa-sima-anniversary-remaster ; 2015 comparison: https://atakak.bandcamp.com/album/obaa-sima .

### NEXT
- Reconcile the artist's 2015 sales estimate with the 2025 label-founder account, without assigning an exact sales number.
- Establish the Berlin cassette's generation and source history.
- Compare the 2015 and 2025 faster/slower transfers; no listening claim until actually auditioned.
- Run a separate Twi-language/local Ghana source search.


## 2026-11-18 — IM-039 fifth-album item-level reconciliation

The fifth Harmonia Enlouquece album has an exact Amazon Music item page under the platform title Esse 5° É Dos Infernos (13 tracks, 46 minutes, platform-listed 2026-07-05, ℗© Hamilton Assunção). The official state-health announcement of 2026-04-08 uses O Quinto dos Infernos and names “O Amor Chegou” as a forthcoming highlight; the 2026-08-15 Agência Brasil report describes the public launch at MuhCab, 13 tracks and 11 previously unreleased songs by Hamilton. Treat the platform date and public event as distinct. “O Amor Chegou” is absent from the platform tracklist; no mapping to Apple Music's 2022 “Hoje o Amor Chegou” is established. The official group site says 66 songs; the 15 August report says 65. Preserve both. The other two album tracks' authorship is not established by the cited report.

Created research/harmonia-enlouquece-im-039-2026-11-18.md and updated catalogue.md / environment-leads.md. IM-039 remains VERIFIED corpus / CONTEXT ONLY: no obscurity or authorship promotion. Amazon is a streaming page, not a direct download URL; ℗© is not a reuse licence. No audio auditioned/downloaded, no upload, no contact and no rights clearance. No TRACK_MAPPING or Grok queue change.

### NEXT — exact queue
1. Resolve whether “O Amor Chegou” was omitted, retitled or issued separately; compare the official April announcement with the platform list and the unrelated 2022 “Hoje o Amor Chegou” without merging them. Seek a complete artist/label release sheet and credits for the remaining two tracks.
2. Continue IM-040 GDE item-level verification (exact cassette issue, tracklist, performer/authorship, band-supplied transfer provenance and lawful access); do not use collector-blog download links as rights evidence.
3. Continue IM-046 Ata Kak source-copy lineage: identify the Berlin cassette generation and run a distinct Twi-language/local Ghana source search; keep the 2015 and 2025 transfers separate.
4. Do not repeat the completed IM-038 two-CD chronology or IM-049 Tardes Nuestras theme qualification without a new primary audio/access or authorship route.


## 2026-11-18 continuation checkpoint — IM-048

A bounded source pass advanced the canonical Insane Music lead IM-048 using two contemporaneous Portuguese reports. The lead now has a precise 23 Nov 2001 launch / Jan 2002 distribution-report chronology, a nine-track count, an approximately 500-copy free-distribution estimate and a clearer mixed participant/guest performance distinction. The surviving carrier, complete sleeve/credits and rights remain unresolved. Next exact task: locate a surviving CD or municipal/participant-held sleeve and preserve the 2001 and 2002 reports as separate evidence. No audio or physical media was accessed.



## 2026-11-19 — IM-052 discovery and IM-038 enrichment

### New qualified lead IM-052 — ZeN, *Bakırköy Akıl Hastanesi'nde* (Istanbul, 1998)

Added a distinct Turkish underground live album recorded at Bakırköy Psychiatric Hospital. A contemporary July 1998 *Roll* interview with Murat Ertel documents the invitation and the band's deliberate adaptation of its improvisational approach to the hospital hall; an August 1999 *Roll* article is indexed as contemporaneous coverage of the released concert album; the 2023 Zel Zele label page states that the recording was performed live at Bakırköy for an audience of patients, doctors and visitors and that the original cassette/CD appeared in 1999. The label's 2023 double-LP is limited to 300 copies. This is an A + F pathway candidate with extant recording, but it is a **visiting band performance, not resident-made or patient-composed music**. The exact 23 June 1998, 14:30 date/time is from specialist secondary metadata and a 2026 account citing a 1998 newspaper notice; it remains to be verified against that notice. A 1998 interview names nurse Nurten as caller, while Ertel's 2024 interview describes two nurses; preserve the discrepancy.

### Canonicalisation of IM-051

The previously added Caustic *Unrest* (São Paulo, 1995) dossier has been mirrored into the canonical projects/insane-music/research/ directory and registered in this catalogue. It is one eight-track cassette object, not eight leads. This is a path correction/migration of the existing lead, not a new lead for the programme count.

### Existing baseline IM-038 — Mágicos do Som

The UFF 2007 dissertation was reopened directly; it identifies Regina Lúcia Serrão as composer/singer of “Preconceito” (2000) and points to the first *Saúde Musical* CD on an annex CD-ROM. A 2016 peer-reviewed *Sociologias* article independently identifies the song as her composition performed by Mágicos do Som and interprets it as collective anti-discrimination protest. The 2013 Volta Redonda municipal notice confirms the second *Saúde Musical* CD, ten songs, group-authored compositions and named participants. The municipal notice dates the group's origin to March 1996, while the 2016 article says 1997; this remains unresolved. The recording and group history are now better distinguished from clinical narratives: this is participant-authored music with an explicit public anti-stigma voice. The first CD-ROM and second CD remain unaccessed; no audio was auditioned.

### Next exact tasks
1. Obtain owner-approved copies/sleeves of both *Saúde Musical* CDs and complete tracklists; resolve 1996/1997 formation date.
2. For IM-052, verify the 1998 event date/time and original 1999 edition; establish master custody and 2023 remaster source through owner-approved enquiry.
3. Continue non-Anglo regional rotation beyond Brazil and Türkiye in the next batch.


### IM-052 release-variant reconciliation (2026-11-19)

The Wire's November 2026 article ties the 23 June 1998 event date to a Hürriyet notice from 21 June 1998; the notice page itself remains un-retrieved. Readdork lists the 1999 Kod Müzik KOD 009 cassette/CD and a 2002 Ada Müzik CD reissue. Yerdeniz lists a 2023 Ada Müzik Turkish 2LP with “Dut Ali” before “Arkadaşım Ateş”; the 1999 Guts of Darkness sequence lists those tracks in the reverse order. Zel Zele's Bandcamp page describes a separate European 2023 2LP edition limited to 300 copies. Treat these as edition/sequence variants of one live recording, not separate performances. The 16-track analogue / Bill Macbeth mix claim remains secondary-reported.


## 2026-11-19 — Chile / Radio Estación del Paraíso screening checkpoint

A bounded Spanish-language source pass identified Radio Estación del Paraíso, a patient-run radio project at Hospital El Peral (1999 onward), and the documentary *La furia de los caballos sin patas* (CineChile: 2001, 67 minutes). The 2000–2001 civic-programme case study confirms pre-recorded and live songs/poems in a public broadcast, but no exact song or participant authorship. A 2011 first-person team account says the film soundtrack includes radio transmissions and unreleased tracks by Shogun, Tobías Alcayota and Joe Villablanca. A 2024 public upload spells the third name “Jeo” and labels the film 2004; preserve both conflicts. A 2023 thesis reports that the original cassettes/discs became inaccessible after a 2003 Barros Luco lockout and that microprogrammes could not be traced in Radio Tierra / Archivo Nacional records.

**Classification:** context-only C lead; no new core catalogue ID and no Grok request. Keep the radio masters, microprogrammes, 2001 documentary mix and external soundtrack contributions separate. No audio was played, downloaded or copied; no contact or rights enquiry was made.

### NEXT — exact queue
1. Seek a filmmaker/producer-approved cue sheet or original soundtrack listing and resolve the 2001/2004 version and Joe/Jeo credit.
2. Identify exact participant-authored/performed songs, if any, within the radio broadcasts or microprogrammes; do not infer authorship from broadcast participation.
3. Establish whether the original tapes/discs survive and whether any lawful access route exists; treat the 2023 thesis's negative search as a bounded result, not proof of destruction.
4. Continue the existing IM-038 CD-owner-approved copy route and IM-052 original 1999 edition / master-chain audit; rotate to another non-Anglo region after this Chile screen.

## 2026-11-20 research checkpoint

### Existing baseline advanced

- **IM-001 — Horace Flinders, Eloise Hospital piano recital:** baseline status advanced IN PROGRESS → RESEARCHED-OPEN. CSU's finding aid says undated, Box 45 Folder 9; DPLA metadata says 1948 and cassette digitized 2015-11-03. The DPLA label transcription says “Harold [sic] Flinders” and “Eliose Hospital,” conflicting with CSU's Horace/Eloise title. CSU copyright policy makes the user responsible for rights where CSU does not hold them. No file was opened or audio played in this run; the prior retrieval report was not repeated or independently verified.

### New qualified leads

- **IM-053 — “Selections from Eloise Symphony” (1948):** item-level CSU audio-tape record, Box 45 Folder 2. A 1948 UP report says a work co-composed by a former inpatient and Ira Altshuler was scheduled for Detroit Symphony performance. The archived recording's performer and link to that event remain unproven; classify as hospital co-composition / unidentified possibly professional performance, not resident-made performance.
- **IM-054 — 은평병원 아트브뤼트 뮤지크 audio corpus (2012–2019):** official Seoul and Newsis sources attest blog-hosted recordings of participant-created songs. The 2015 report names 13 songs, including “우리들의 약” and “소중한 삶으로.” Count one corpus only; Naver item-level access, rights and consent remain unresolved.

### Next exact tasks

1. Continue baseline IM-041 as the next existing-lead batch.
2. With owner approval, request the CSU digital objects for IM-001 and IM-053; reconcile names, dates, carrier generation, performer and rights.
3. Resolve IM-054's stable Naver post URLs and item-level audio, then document title, date, group credit, medium, consent and rights before splitting any tracks.
4. Rotate discovery beyond the current US/Korea cases to a different language and region; retain environment-first and resident-made / visiting-performance distinctions.


## 2026-11-20 continuation checkpoint — IM-054 Korean-language pass

Completed a bounded Korean-language verification pass on IM-054. Institutional/press sources now corroborate patient-created song practice and the intended hospital-blog audio corpus, but no stable item-level audio or preservation record was recovered. Keep the corpus-level lead PARTIALLY VERIFIED / PROMISING. Next exact task: locate an archived/exported copy of the Naver blog or an institutional catalogue while preserving participant privacy and consent uncertainty. No audio, archive contact or rights clearance.
