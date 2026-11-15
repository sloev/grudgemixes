# Formal candidate-record audit — 2026-11-15

Scope: all four Markdown files currently under `candidates/`, checked against `README.md` and the adopted `METHODOLOGY.md`. This is a research/editorial audit, not a unilateral editorial rewrite. Historical status labels are retained in the source files; proposed crosswalks below are audit findings.

## Repository-level finding

The formal candidate directory contains four records only. The README's “Current research snapshot” lists ten items, but six of those are held only in `research/` dossiers or screening/re-audit notes, not in `candidates/`. This is not necessarily an error: the README describes a mixed snapshot of candidate records and leads. It should, however, say explicitly that the table spans both directories and link every row to its canonical file. The four formal files also retain legacy “PARTIALLY VERIFIED” labels rather than the adopted A/B/C evidence vocabulary. Preserve the legacy label but add a visible mapping on the next editorial pass.

## File-by-file audit

### 1. `candidates/GM-AM-001-pamp-vorodan-1916.md`
- Existing status: “PARTIALLY VERIFIED / NOT CLEARED.”
- Recording identity: strong. LOC item jukebox-19711 gives Victor 69102, matrix B-18462 take 3, date 1916-10-11, New York, performer Torcom Bézazian and arranger H. Sinanian.
- Text/composition: strong historical witness. Alishan poem published 1850; Utidjian identifies Bianchini's celebrated setting. The dossier correctly distinguishes Sinanian's arrangement credit from Bianchini's composer attribution and records the unresolved musical-version question.
- Thematic case: strong on the poem's explicit vengeance/collective retaliation frame, but exact 1916 performed text has not yet been collated with the poem. Avoid saying the Victor take contains every quoted stanza until heard/transcribed.
- Date: CORE DATE — VERIFIED for fixation (LOC item-specific date and matrix/take).
- Audio: access derivative exists; collection-level LOC workflow is documented, but item-specific transfer chain and preservation master availability remain open. Raw status not established.
- Rights: NOT CLEARED, correctly separated.
- Proposed evidence crosswalk: **B — PROBABLE CANDIDATE** until exact performed text/version is checked. This is not a failure of the recording date; it is a text-to-master linkage gap.
- Highest-value next step: listen to the exact LOC take, collate all audible text against Alishan/Sinanian witnesses, and request item-specific preservation-master/transfer metadata.

### 2. `candidates/GM-FR-001-saint-saens-vengeance-at-last-1908.md`
- Existing status: “PARTIALLY VERIFIED — exact archival item located; direct audio file and transfer/rights review still open.”
- Recording identity: strong triangulation. UCSB Victor Red Seal Discography and HRS give Victor 87501, matrix B-6227-2, 1908-05-25, Camden; FAU RSA item 57310 is an exact catalogue/performer item. Contemporary November 1908 trade advertisement confirms the selection and says English.
- Thematic case: clear fictional revenge/conspiracy scene; however, the actual words and completeness on the disc have not been verified from listening. The dossier properly distinguishes the staged plot from historical testimony.
- Date: CORE DATE — VERIFIED for fixation and contemporary issue advertisement.
- Audio: FAU player is discovery/listening access, not a direct source file; FAU policy and transfer metadata remain open.
- Rights: NOT CLEARED, correctly separated.
- Proposed evidence crosswalk: **B — PROBABLE CANDIDATE** pending actual audio/text confirmation and item-level transfer details. The thematic plot is unusually strong, but do not infer the recorded English wording from French libretto or title alone.
- Highest-value next step: inspect/listen to FAU track; obtain label/runout and FAU item-level transfer notes; compare the English text to the libretto/score.

### 3. `candidates/GM-IT-001-caruso-vesti-la-giubba-1904.md`
- Existing status: “PARTIALLY VERIFIED — strong archival candidate; not commercially cleared.”
- Recording identity: strong LOC metadata for Victor 930, matrix B-1002 take 1, 1904-02-01, New York; issue date still not independently documented in the file.
- Composition: Leoncavallo's *Pagliacci* and aria chronology are well established.
- Thematic problem: the dossier itself accurately says the recorded aria is Canio's betrayal lament and explicitly says it is **not** an act of revenge; the murder/retaliation occurs later in the opera, outside this aria. Under current METHODOLOGY.md §3, conditional lament/betrayal must itself include an accusation, demand, threat, vow, refusal, answer or intention to retaliate/resist. The current dossier has not demonstrated such a mechanism in the recorded aria. A plot event elsewhere in the opera cannot be imported into the recorded excerpt.
- Date: recording date is pre-cutoff and item-specific; issue/publication date still needs contemporary evidence for strict “published or fixed” determination, although fixation date itself is documented.
- Audio/rights: LOC access audio and general preservation workflow are described; item-specific source/processing and territory clearance remain open.
- Proposed thematic decision: **REJECTED / OUTSIDE THEMATIC CORE as currently documented**, or retain only as a non-counting comparative control about grievance without retaliation. This is a scope decision under the adopted rule, not a claim the recording is historically unimportant. Reconsider only if listening/transcription demonstrates an in-aria accusation or responsive intention not represented in the current note.
- Highest-value next step: no further rights/audio work is justified for core selection until the thematic gate is resolved. If retained as control, document why the excerpt fails while the larger opera contains later retaliatory violence.

### 4. `candidates/GM-IT-002-verdi-si-vendetta-vocalion-1921.md`
- Existing status: “PARTIALLY VERIFIED — exact archive item and issue identification located; exact recording date/matrix and direct audio/transfer details unresolved.”
- Recording identity: FAU item 54400 identifies Vocalion 60019, Scotney and Rimini, and the track title; specialist Vocalion sessionography associates 60019/30146 with session 7176, tentatively March 1921. The date is explicitly tentative; matrix/take absent.
- Thematic case: strong fictional revenge declaration and plot context, but the actual recording's text/language and completeness have not yet been heard/verified. The dossier correctly cautions against collapsing Gilda's and Rigoletto's agency.
- Date: PROBABLE DATE, not verified; catalogue/session linkage is good but the session date has a question mark.
- Audio: FAU player exists; no direct audio file or item-specific transfer details; public stream is not a commercial licence.
- Rights: NOT CLEARED.
- Proposed evidence crosswalk: **B — PROBABLE CANDIDATE** (not A) because the exact archive item and catalogue linkage are substantial, but session date, matrix and performed text remain open. If the sessionography linkage cannot be independently corroborated, downgrade to C.
- Highest-value next step: obtain Vocalion 60019/30146 label/runout, identify matrix/take and session ledger, then listen to FAU track 2 and verify singers/text.

## Cross-record consistency findings

1. The four records all contain recording identity, taxonomy, audio and rights discussions, but only the Armenian record has a deeply developed text/arrangement genealogy. This is appropriate to evidence availability, but the README's required-record checklist should be interpreted as aspirational for C leads and progressively complete for B/A.
2. “PARTIALLY VERIFIED” is not one of the current evidence levels. The next maintenance pass should add a compact field such as “Current evidence level: B — PROBABLE” while preserving historical wording.
3. Rights and transfer caveats are consistently not confused with thematic eligibility; this is good and should be retained.
4. Caruso is the material mismatch: its own text says the selected aria is only lament, but the record was retained because of retaliation later in the opera. That does not meet current methodology unless the aria itself contains a qualifying response mechanism.
5. Candidate filenames use country/region IDs (AM/FR/IT), while the README does not publish a schema for ID assignment. No duplicate IDs are visible in the four-file set.
6. Formal candidate records are not a substitute for research dossiers; many substantial leads remain under `research/`. The README should distinguish “formal candidate records” from “research leads” more clearly.

## Priority order for subsequent work

1. Resolve Caruso's thematic eligibility or mark it non-core; do not spend clearance effort first.
2. Verify the performed text on Victor 69102 / B-18462 take 3.
3. Verify the performed text and archive transfer on Victor 87501 / B-6227-2.
4. Resolve Vocalion 60019/30146 matrix/session and listen to track 2.
5. Add README cross-links/status mapping after the dossier inventory and editorial review.

## Audit limitations

This pass inspected repository text and linked metadata as recorded by contributors. It did not listen to any embedded audio, inspect physical carriers, independently request archival files, or issue legal opinions. All four records remain NOT CLEARED for commercial use.


## 2026-11-15 follow-up: strongest operatic pair for first mix

The two strongest existing candidates for an initial tightly themed mix are Saint-Saëns, “Vengeance at Last” (Victor 87501, matrix B-6227-2, Camden, 25 May 1908) and Verdi, “Sì, vendetta” (Vocalion 60019 / 30146, session 7176, ca. March 1921). Both are now explicitly crosswalked as **B — PROBABLE**, not A. Their exact recording identities and strong revenge narratives are well supported, but the actual archive access copies have not been listened to or transcribed in this research run. A mix may be developed editorially, but not called release-ready or “rock solid” until audio/content, transfer provenance and rights are separately checked.

The Saint-Saëns item has an especially strong date and matrix chain: Victor 87501, B-6227-2 take 2, Camden, 25 May 1908, plus a contemporary November 1908 trade advertisement specifying English. A conflicting secondary entry gives 89501; retain that discrepancy but prefer 87501, corroborated by contemporary advertising, UCSB and FAU. Its full libretto places the recorded selection in Act II, Scene II, where Dalila and the High Priest conspire to defeat Samson and explicitly call it vengeance. The English recording itself still needs collation.

Verdi's FAU item 54400 confirms the exact catalogue item and performers; Mintzer's specialist Rimini discography links it to Vocalion session 7176 and catalogue 30146 / 60019, ca. March 1921. The session date is tentative and the matrix/take unresolved. Read the duet as Rigoletto's revenge plan and Gilda's participation/complication, not as a simple shared motive.
