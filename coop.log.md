## 2026-11-16 — Grok — GM-US-001 retrieval attempt

### Task
Attempt retrieval of READY FOR GROK item GM-US-001 (Bentley Ball, “Jesse James”, Columbia A3085) from Wikimedia Commons into the grudgemixes Drive folder.

### Result
- Source URL: https://upload.wikimedia.org/wikipedia/commons/4/42/Jesse_James_%28Bentley_Ball%29.ogg
- Status: FAILED — HTTP 429 rate limit from Wikimedia (retry-after 600s). Small HTML error page received instead of the 2.23 MB Ogg.
- No file uploaded to Drive.
- Other READY items (FAU streaming-only, DAHR access barriers, etc.) not attempted this session due to known restrictions.

### Handoff
Retry Wikimedia download later or seek alternative archive transfer. Do not mark as downloaded.

---

## 2026-11-16 — ChatGPT — Royal 1645/1649 catalogue access-route follow-up

### DONE
- Followed the Royal 1645 handoff and checked the NDL's current guidance for 演芸レコード発売目録 (1990, KD1-E21).
- NDL Research Navi confirms the catalogue covers domestic entertainment records from 1909–1945 and includes publication month, title, performer, author, company and catalogue number. The NDL digital copy is on-site only.
- CiNii's bibliographic record lists the same book in about 30 libraries, including Cambridge University Library and Japanese university collections, providing an alternative physical consultation/enquiry route.
- A Kamigata Performing Arts Centre report explains that the compilation was based mainly on advertisements in 16 newspapers and 14 magazines, with bulletins/flyers as supplements, and was not checked against physical discs. A catalogue hit can narrow advertised issue chronology and title/number linkage, but cannot authenticate the surviving carrier, label, matrix, recorded text or master.
- Added the access route, evidence caveat and exact search terms to research/japan-ako-gishi-yoshida-naramaru-royal-record.md. No status promotion.
- Sources: https://ndlsearch.ndl.go.jp/rnavi/humanities/engei ; https://ndlsearch.ndl.go.jp/books/R100000002-I000002059548 ; https://ci.nii.ac.jp/ncid/BN04971277 ; https://wahha-kamigata.jp/wordpress/wp-content/uploads/2019/11/55984e475f4733ca7fe6741e5df6f1fc.pdf .

### NEXT
- Request a targeted lookup or consultation from a current holding library for KD1-E21; search 吉田奈良丸, 赤穂義士討入 / 赤穂義士伝討入, ローヤル, 1645 and 1649.
- Capture exact page/category and advertised month. Treat it as discographic chronology only; pair any result with Kushiro inventory and label/runout evidence.
- Keep 1645/1649 separate from Royal 1853, Royal 1723, 1914 Yamato and July 1923 Nipponophone issues unless an exact cross-reference is found.
- No copy consulted, no carrier/label/matrix inspected, no audio played/downloaded, no archive contacted and no rights cleared.

### Supplement — 2026-11-16 file cross-reference
- Added the KD1-E21 library-access route and its advertisement-based evidence limitation to research/global-early-recording-map.md. The route is a next research action only; no candidate grade or date changed.
- Cross-reference: research/japan-ako-gishi-yoshida-naramaru-royal-record.md. No library copy was consulted and no archive contact was made.

## 2026-11-16 — Grok — GM-US-001 successful retrieval

### Task
Retry and complete retrieval of READY FOR GROK item GM-US-001 (Bentley Ball, “Jesse James”, Columbia A3085) from Wikimedia Commons.

### Result
- Source URL: https://upload.wikimedia.org/wikipedia/commons/4/42/Jesse_James_%28Bentley_Ball%29.ogg
- Status: SUCCESS
- Filename: GM-US-001_Bentley_Ball_Jesse_James_Columbia_A3085_1919-1920.ogg
- Format: audio/ogg (Ogg Vorbis)
- Size: 2,334,043 bytes (~2.3 MB)
- Duration: ~180 seconds (from Wikimedia X-Content-Duration header)
- Drive URL: https://drive.google.com/file/d/1m9BAm1M6BRMwHlQSGoHT6hAvV9LeVZ6G/view?usp=drivesdk
- Provenance: Wikimedia Commons access copy of Columbia A3085 side 2; not an authenticated archival transfer. No source carrier, transfer operator or processing chain documented.
- Uploaded to grudgemixes subfolder.

### Handoff
Mark GM-US-001 as GROK REPORTED DOWNLOADED in TRACK_MAPPING.md. Independent inspection recommended before FILE VERIFIED. Thematic fit remains to be confirmed by listening/transcription. Other READY items (Mix 01 FAU-blocked, DAHR) not advanced this session.

---

## 2026-11-16 — Grok — GM-M01-01 UCSB DAHR confirmation + Drive inventory

### Task
Continue READY FOR GROK work on Mix 01 priority (GM-M01-01 Saint-Saëns “Vengeance at Last”, Victor 87501 / B-6227, de Gogorza & Homer, 25 May 1908). Confirm archival source and inventory current Drive contents against mapping.

### Result — GM-M01-01
- Exact archival transfer located at UCSB DAHR: https://adp-assets.library.ucsb.edu/cusb_victor_87501_01_b6227_00/cusb_victor_87501_01_b6227_00d.mp3
- Downloaded and inspected:
  - Format: MP3, 320 kbps, 48 kHz stereo
  - Size: 5,927,085 bytes
  - Duration: 148.152 s (~2:28)
  - MD5: 4f6fded3b1059001de40e8bec5231b1f
- Uploaded to Drive as `GM-M01-01_Saint-Saens_Vengeance_at_Last_deGogorza_Homer_Victor_1908_UCSB_DAHR.mp3`
  - Drive file ID: 1saEeRhaCivlSsvI_7QSi_wevIozCAO7C
  - Link: https://drive.google.com/file/d/1saEeRhaCivlSsvI_7QSi_wevIozCAO7C/view?usp=drivesdk
- Note: An earlier file of identical size already existed in the folder under the short name `GM-M01-01_Saint-Saens_Vengeance_at_Last_deGogorza_Homer_Victor_1908.mp3`. The UCSB-sourced copy is now explicitly labelled for provenance.

### Drive inventory (grudgemixes subfolder, 2026-11-16)
Already present and matching mapping filenames or clear variants:
- GM-M01-01 (both short name and UCSB_DAHR variant)
- GM-US-001 (Bentley Ball Jesse James)
- GM-US-004, GM-US-006, GM-US-010, GM-US-011
- Multiple legacy IT / UK / Tuskegee entries

Still missing from READY FOR GROK priority:
- GM-M01-02 (Scotney / Rimini “Sì, vendetta”, Vocalion 60019) — no matching file
- GM-M01-03 (McEachern “Revenge! Timotheus Cries”, Vocalion X-9560) — no matching file

### Status recommendations for TRACK_MAPPING.md
- GM-M01-01 → GROK REPORTED DOWNLOADED (UCSB DAHR transfer confirmed; independent listen/verify still needed for FILE VERIFIED and thematic fit)
- GM-US-001, GM-US-006, GM-US-004, GM-US-010, GM-US-011 → GROK REPORTED DOWNLOADED (files present; provenance notes already recorded in prior entries)
- GM-M01-02 and GM-M01-03 remain READY FOR GROK / RESEARCH TARGET — source hunt continues

### Handoff
Next concrete retrieval targets: locate downloadable archival transfers for Vocalion 60019 (Scotney/Rimini) and Vocalion X-9560 (McEachern). FAU remains streaming-only. No listening or thematic promotion performed by Grok.

## 2026-11-16 — Grok — Mix 01 remaining tracks source hunt and Drive inventory refresh

### Task
Refresh grudgemixes Drive folder inventory and search for downloadable archival transfers for remaining Mix 01 priority items GM-M01-02 and GM-M01-03.

### Drive inventory confirmation (2026-11-16 evening)
grudgemixes subfolder (1W5kjNo0ygmb-rA6NJF2v5QwMT2Iy58iY) contains:
- GM-M01-01 variants (UCSB DAHR and short name)
- GM-US-001 Bentley Ball Jesse James Ogg
- GM-US-004, 006, 010, 011
- Legacy Caruso, Ruffo, Tuskegee, UK Hagen entries
- Additional: GM-US-Dalhart_Jesse_James_Edison_51621.mp3, GM-US-Waring_Stack_O_Lee_Blues_1924.mp3

No files matching GM-M01-02 or GM-M01-03 proposed filenames.

### Source hunt results
- GM-M01-02 (Scotney/Rimini Vocalion 60019): FAU remains streaming-only. Internet Archive searches returned other Si vendetta performances (Galvany/Ruffo, Battistini/Hayes) but not the exact Scotney/Rimini Vocalion. No independent downloadable archival transfer located.
- GM-M01-03 (McEachern Vocalion X-9560): No archive.org or free downloadable transfer found. Collector CDR listing remains a clue only. FAU-equivalent barriers apply.

### Status
No new files retrieved this session. Existing reported downloads remain GROK REPORTED DOWNLOADED pending independent verification. Mix 01 tracks 2 and 3 remain blocked on source availability.

### Handoff
Continue hunting for exact Vocalion 60019 and X-9560 archival transfers (UCSB DAHR, other national archives, or permitted collector sources). Do not substitute non-matching performances. Update TRACK_MAPPING.md statuses after verification.
