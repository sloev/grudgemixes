# Research and audio handoff — grudgemixes

**Purpose:** keep research/evaluation and audio retrieval as two coordinated workstreams. This follows the working collaboration pattern in `sloev/insanemusic`: the project owner/editor sets direction; ChatGPT researches and documents; Grok executes audio retrieval from a specific, evidence-backed queue and reports what it actually obtained.

## Role split

### Project owner / editor
- Sets the brief, priorities, thematic boundaries and editorial decisions.
- Approves mix concepts, final track selection, sequencing and publication decisions.
- Supplies feedback and resolves decisions that require human judgement.

### ChatGPT — research, discovery and evaluation
- Owns the research workstream: global digging, local-language and genre discovery, historical/contextual research, archive/catalogue/press/discography searches, recording identification, chronology, version distinction, lyric/text research and thematic evaluation.
- Maintains candidate/lead dossiers, global map, evidence grades, methodology, mix concepts, `TRACK_MAPPING.md`, `research_method.md` and append-only `coop.log.md`.
- Separates direct source statements, observed evidence and inference; never invents listening, file inspection, lyrics, matrices, dates or transfer details.
- Prepares a **Grok download queue** only for exact or sufficiently specified source targets. Each queue item must include a stable project/lead ID, exact recording identity, source page and direct audio/download URL where available, catalogue/matrix/archive identifiers, expected filename, date confidence, and any uncertainty or access caveat.
- Evaluates retrieved files after Grok reports them: match filename and metadata to the target, compare duration/format/track identity where available, and update the evidence record. A download is not proof of thematic fit or chronology.

### Grok — audio retrieval and file handoff
- Works from the explicit **Grok download queue** prepared in `TRACK_MAPPING.md` / the handoff note; does not independently promote a title or change the research status.
- Retrieves the specified audio into the shared Drive folder below, using the proposed filename. Prefer the archive's supplied download route or the best available source copy; do not silently substitute a reissue, derivative, different take or similarly titled performance.
- For each attempt, reports: queue ID; exact Drive filename; source URL/page; retrieval date; success/failure; file format, size and duration if available; any redirects, login/paywall/access barrier; whether the file is a complete track or excerpt; and any discrepancy between expected and obtained item.
- If a target cannot be retrieved, report the obstacle and stop rather than guessing another URL. Do not change the research dossier or claim an item was obtained without a resulting file.
- Preserve original downloaded files. Do not edit, trim, denoise, resample, rename or convert the source file unless separately asked; if a derivative is made, retain the original and document the transformation.

## Shared Drive destination

Use this folder for all new Grudgemixes audio retrievals:
https://drive.google.com/drive/folders/1cOwvMN1k_bLznh-1K8bCHzRQPAJjnGRO

The folder listing is not independently visible to this research session at present. Treat Grok's file report as **reported present** until the file is independently inspected or a verifiable metadata listing is supplied. The older Drive ID in earlier mapping entries is superseded for new downloads.

## Queue and retrieval statuses

Use these statuses in `TRACK_MAPPING.md`:
- **RESEARCH TARGET** — exact recording/source target researched; not yet handed to Grok.
- **READY FOR GROK** — source and proposed filename supplied; retrieval can be attempted.
- **GROK REPORTED DOWNLOADED** — Grok reports a file in Drive; not independently checked here.
- **FILE VERIFIED** — actual file or reliable file metadata inspected and matched to the intended recording.
- **RETRIEVAL FAILED / BLOCKED** — Grok reports an unsuccessful attempt and the obstacle.
- **IDENTITY MISMATCH** — retrieved item differs from the target; preserve it as an unverified file and investigate.

Research evidence grade (A/B/C), historical date assessment, audio provenance, access conditions and rights are separate fields. Do not promote a C lead because Grok retrieved an audio file. Do not demote a sound research candidate because audio retrieval is temporarily blocked.

## Operating cycle

1. **Start of every research session:** read current `METHODOLOGY.md`, latest `coop.log.md`, `README.md`, `research_method.md`, `TRACK_MAPPING.md`, global map, and the active dossiers/handoff. Check recent commits and preserve existing work.
2. **Research:** choose the highest-value unresolved thread; search original-language sources, archives, catalogues, contemporary press, discographies and contextual sources. Record both useful results and bounded null results.
3. **Evaluate:** distinguish exact recording identity, date, thematic fit, version, audio provenance and access. Grade A/B/C with explicit unresolved questions.
4. **Prepare retrieval batch:** add only researched targets with an actionable source route to the **READY FOR GROK** section. Include exact URLs and expected filenames; do not ask Grok to search blindly.
5. **Grok retrieval:** Grok downloads and reports results using the required fields above. No claim of success without a file in the destination.
6. **Reconcile:** compare Grok's report against the queue; update mapping to GROK REPORTED DOWNLOADED, FILE VERIFIED, BLOCKED or MISMATCH. If audio is accessible for evaluation, listen to the exact version before transcribing or changing thematic status.
7. **Maintain records:** update the relevant dossier, global map, methodology/handoff as needed, README snapshot if material, and append a dated `coop.log.md` entry. Commit actual changes and include commit links in the report.
8. **Report:** concise summary of research, evidence/status changes, new Grok queue items, retrieval items awaiting feedback, repository commits and next concrete research step.

## Non-negotiable evidence rules

- Pre-1926 remains the historical core; publication/issue and recording/fixation dates are separate.
- A title, catalogue hit, downloaded file or later printed text does not prove the exact recorded lyrics or thematic mechanism.
- Distinguish commercial issues from field/ethnographic recordings and later reissues.
- Keep rights/access/consent conditions recorded as separate research metadata. The project may defer commercial clearance during private research, but this does not convert restricted access into permission to download or redistribute.
- Never state that ChatGPT or Grok listened to, inspected or downloaded an item unless that actor actually did so.
- The project owner/editor retains final authority over candidate selection and mixes.

Last updated: 2026-11-15
