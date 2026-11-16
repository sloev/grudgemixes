<!-- Imported from the agent branch on 2026-11-16. Its API/label-image observations are agent-reported; ChatGPT has not independently fetched or auditioned these files. Follow-up corrections and later findings belong in canonical dossiers. -->

# Audio-locator pass, Internet Archive and National Jukebox mirrors (2026-11-15)

**Researcher:** Claude (Claude Code session)
**Question:** Which of the open B/C leads have an exact archival audio object online, and which still have none?
**Method:** Internet Archive advanced-search API (`archive.org/advancedsearch.php`) and item metadata API (`archive.org/metadata/<id>`), searching title, creator and the `78rpm`, `78rpm_charm` and `hessel-digital-library` collections. Label images were downloaded and inspected for the items marked ✔. **No audio was listened to or transcribed in this pass.** The Library of Congress site itself returned HTTP 403 from this environment, so National Jukebox items were reached through archive.org mirrors and should be re-checked against loc.gov.

## Positive results

### ✔ Wagner, “Hagen meditates revenge,” Radford, HMV D704, matrix Cc 1586-1
- Exact item found in the CHARM transfer set: `78_the-twilight-of-the-gods-hagen-meditates-revenge_radford-robert-symphony-orchestra`. It has a FLAC original (247.69 s), an MP3 derivative and a label photograph.
- The label reads: *“The Twilight of the Gods” (Wagner) / Hagen meditates revenge / Act I / Vocalist—Robert Radford / Conductor—PERCY PITT / IN ENGLISH Orchestra and Bass / (3-0857) / Cat. No. D 704.*
- This resolves the “title: Hagen meditates revenge vs. Hagen's Watch” question and the “probably English” language question.
- Promoted to a full candidate record: [candidates/GM-DE-001-wagner-hagen-meditates-revenge-hmv-d704-1922.md](../candidates/GM-DE-001-wagner-hagen-meditates-revenge-hmv-d704-1922.md).

### ✔ “Pamp Vorodan,” Torcom Bézazian, Victor 69102-A, matrix B-18462-3
- Archive.org mirror of LOC Jukebox item 19711: `loc-jukebox-19711-pamp-vorodan`. It holds the LOC streaming MP3 (≈128 kbps, 169.2 s) and a high-resolution label scan (2311×2294).
- The mirror is run by a third party (“Hessel Digital Library”) and states that it is a bit-exact copy of the LOC MP3. Cite the LOC item as the source of record: https://www.loc.gov/item/jukebox-19711/
- **New label evidence (inspected):**
  - The Armenian-script title on the label is **ԲԱՄԲ ՈՐՈՏԱՆ** (*Bamb Orotan*). This differs from Utidjian's normalised spelling ԲԱ՜Մ. ՓՈՐՈՏԱՆ cited in the candidate file. Keep both: one is the label's own orthography, the other a scholar's correction.
  - The performer's name in Armenian script is **ԹՈՐԳՈՄ ՊԷԶԱԶԵԱՆ**.
  - The voice is printed as **“Baritone with orchestra / In Armenian.”** The candidate file currently says “male vocal solo / tenor,” so the label contradicts it. The Columbia 1915 spreadsheet also says baritone. Recommend correcting the field to *baritone (per label)*.
  - Printed credit: “(Arr. H. Sinanian).” English title: “Pamp Vorodan—Armenian March.”
- The audio is an LOC access derivative, not a preservation master (METHODOLOGY §5: *access derivative only*). Request the Packard Campus preservation transfer for production.

### ✔ Alternative witnesses for “Sì, vendetta” (Verdi, *Rigoletto*)
The current candidate GM-IT-002 (Scotney/Rimini, Vocalion 60019) has a tentative date and no matrix. Two pre-1926 Columbia recordings of the same duet have exact LOC transfers and label scans. They are logged here as **alternates, not replacements**; the editor chooses.

| Performers | Label / catalogue (from label) | Matrix/take (LOC) | Date (LOC) | Label notes | Mirror ID |
|---|---|---|---|---|---|
| Alice Nielsen, Ramon Blanchart | Columbia A5301 (30737), Symphony Series, “Sung in Italian … Si, vendetta! (Vengeance I'll have!)” | 30737/1 | 1911-09-30 | A handwritten **“April 1911”** and **“H-1091”** on the disc conflict with the LOC date. Unresolved; possibly a file-copy annotation | `loc-jukebox-762757-si-vendetta` |
| Maria Barrientos, Riccardo Stracciari | Columbia 78363, Symphony Series, “Sung in Italian … ‘Si, Vendetta’ (Vengeance I'll Have)” | 78363/3 | 1919-03-20 | Catalogue number = matrix number on label | `loc-jukebox-1065263-si-vendetta` |

The archive.org search also found an HMV-family Battistini/Hayes “Si vendetta” (Gramophone DA 189, dated 1921 by its uploader) and several Galvany/Ruffo transfers. Their metadata comes from uploaders and has not been checked.

### New C-lead (title only)
- **“Venganza de amor,” Floro y Cruz (Floro Zorrilla, Juan Cruz), Victor, matrix H-67/1, 1911-01-10, Spanish (Cuba).** Mirror `loc-jukebox-244041-venganza-de-amor`; LOC jukebox-244041. The title alone is not enough (METHODOLOGY §3), and “revenge of love” may be a love-song conceit. Listen and transcribe before any status change. Logged so it is not lost.

## Negative results (searched, not found on archive.org)

| Lead | Searches | Result |
|---|---|---|
| Handel, “Revenge! Timotheus cries,” HMV D589 / Cc584 | `urn:charm:METS_D_589`; “timotheus”; Gresham Singers (8 items, none D589); Radford (52 items, none D589) | Not on IA. A modern recording titled “just-revenge-robinson” is not the 1921 disc. |
| Vocalion X-9560, McEachern | “mceachern” | Not found |
| Saint-Saëns, “Vengeance at Last,” Victor 87501 / B-6227-2 | Gogorza in the Jukebox mirror (74 items); “vengeance” in 78rpm | Not in the mirror. FAU remains the only located stream. Check loc.gov directly, since the Jukebox may hold Victor B-6227. |
| Scotney/Rimini, Vocalion 60019 | Scotney (22), Rimini (57) | Only 1926 HMV Scotney sides found |
| Gene Greene, “Franky & Johnny,” Pathé 5370 | Greene creator search; Frankie/Franky 1900–1926 in 78rpm | Not found. Other Greene sides exist in the Jukebox. |
| Homokord 1118, “Papus Rache” | “papus” | Not found |
| Japanese Naniwabushi (Naramaru, Kumoemon, Takamine) | creator/title in Japanese and romaji | Not found. Nichibunken remains the route. |
| Plaatje, Nathaniels, Solanke, Boyajian, Tashjian | creator searches | No matching early 78s on the first page of results. Search again by catalogue number (Zonophone 4169, 3972). |

## Status implications (recommendations; editor to confirm)

- **GM-DE-001 Wagner:** C → **B (strong)**. Exact master and audio are located. Transcription and translator identification are still needed.
- **GM-AM-001 Pamp Vorodan:** remains **B (strong)**. Correct the voice-type field from the label. Exact audio is located, but only as an access derivative.
- **GM-IT-002 Sì vendetta:** remains B. The two Columbia alternates are better documented and have exact dates, so consider them for the slot.
- No item reaches **A** in this pass, because nothing has yet been listened to and transcribed.
