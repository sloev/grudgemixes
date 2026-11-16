# Shared research and production workflow

**Applies to:** Grudge Mixes  
**Operating model:** two parallel tracks, one evidence standard, one auditable hand-off.

This document standardises *how work moves* across the three Sloev research repositories. It does not merge their editorial admission rules, historical periods, terminology, or rights policies. The project-specific methodology remains authoritative whenever it is stricter.

## 1. Two tracks

### Track A — discover new leads
1. Search broadly, including original-language terms, scripts, regional archives, specialist catalogues, community sources and the small web.
2. Capture each plausible find as a lead before spending heavily on it.
3. Deduplicate against the existing catalogue, dossiers, queues and aliases.
4. Record why it matters, the strongest source, confidence, gaps and the next bounded research action.
5. Promote only when the project's own admission/evidence rules are met.

Discovery should diversify coverage, not just add more hits from familiar English-language sources. Record bounded null searches when they close a meaningful route.

### Track B — advance existing leads into usable outputs
1. Work the highest-value unresolved lead already in the backlog.
2. Verify identity, context, chronology/version, provenance, access and rights as separate questions.
3. Update the source dossier and canonical catalogue/compendium record.
4. Where an audio object is relevant, create or update a precise retrieval request for a Drive-enabled agent.
5. Reconcile the agent's report against the exact requested object; distinguish reported upload from independently verified file.
6. Produce editorial-ready data only after the relevant project criteria are met.

Track B is not simply more research notes: its outputs are improved canonical records, usable editorial datasets, and actionable asset requests.

## 2. Shared lead lifecycle

Use these workflow states consistently (they describe *work progress*, not research quality):

- **INBOX** — captured, not yet triaged.
- **TRIAGED** — scope relevance and next action assessed; duplicate check done.
- **ACTIVE** — a bounded research task is underway and claimed in the collaboration log.
- **WAITING** — blocked on archive, rights-holder, owner, access or external response.
- **READY_FOR_EDITORIAL** — project-specific evidence/admission threshold met; ready for human editorial decision.
- **READY_FOR_ASSET_REQUEST** — exact asset target and lawful/access-permitted route are sufficiently specified.
- **ASSET_REQUESTED** — handed to a Drive-capable agent; awaiting result.
- **ASSET_REPORTED** — agent reports upload/retrieval; not independently verified here.
- **ASSET_VERIFIED** — file/metadata inspected and matched to the intended object.
- **CLOSED** — completed, rejected, superseded or intentionally deferred, with reason recorded.

Never conflate workflow state with evidence grade, thematic fit, audio status, rights status or editorial approval. Keep each independent.

## 3. Minimum lead record

For every new or materially updated lead, capture as much of this as evidence permits:

| Field | Requirement |
|---|---|
| Stable ID | Persistent project-local ID; never recycle |
| Canonical subject | Exact title/name, original script and transliteration/aliases |
| Lead type | Artist, work, recording, film, cue, archive, institution, scene, etc. |
| Relevance | Why it belongs in this project's scope; cite the project's specific criterion |
| Evidence | Claim-level source links, source title/institution, date/access date and what each supports |
| Confidence | VERIFIED / WELL-SUPPORTED / PROVISIONAL / DISPUTED / UNKNOWN, or the project's more specific grade |
| Identity | Exact version/object/issue/recording where applicable; distinguish related objects |
| Chronology | Dates and what each date actually refers to |
| Provenance/access | Holding institution, identifier, access route, restrictions and transfer details if known |
| Rights | Separate status for underlying work, recording, performer/third-party rights, supplied file and intended use |
| Workflow | Lifecycle state, owner, last checked date and next action |
| Output links | Dossier, catalogue/compendium row, mix/cue list and asset request, as applicable |

Unknown means unknown. Do not fill gaps with plausible-sounding inference. Preserve original-language spellings and conflicting evidence.

## 4. Asset-request contract for Google Drive-enabled agents

A request is actionable only when it identifies a specific object, not merely an artist, film or search topic. Include:

- Stable lead/request ID and canonical title.
- Exact recording/release/version, track or cue; include catalogue, matrix, archive or other identifiers where available.
- Primary source page and direct file URL only when verified and permitted.
- Access/download terms and permission status; label paid routes and permission-needed routes explicitly.
- Expected filename, destination folder and any known format/duration.
- Identity uncertainties and prohibited substitutions.
- Request owner, date, and result fields.

**No silent substitution.** A reissue, reconstruction, alternate take, fan upload, film mix, stream and archival master are different objects unless evidence establishes otherwise. Do not purchase, bypass access controls, or redistribute restricted/copyrighted material. A stream/catalogue entry is not a downloaded file.

Use these result states: **REQUESTED**, **BLOCKED**, **REPORTED_UPLOADED**, **VERIFIED_IN_DRIVE**, **IDENTITY_MISMATCH**. Only **VERIFIED_IN_DRIVE** counts as collected. Record exact filename, source, retrieval date, format/size/duration when available, and verification method. Research-only agents must never claim a Drive upload.

## 5. Editorial and production outputs

The canonical record should be reusable without rereading the whole research log. Maintain structured, consistent fields in the project's existing catalogue/queue and link to focused dossiers.

- mix concepts, candidate shortlists, verified track mapping and compendium-ready contextual records; each track should retain its historical recording/date, thematic mechanism, version and rights distinctions.
- Keep raw evidence and editorial interpretation distinguishable.
- Preserve a clear chain from source → lead → verified record → editorial selection → asset request/result.
- Do not imply that a lead is approved for publication or commercial use merely because it is well researched or available in Drive.

## 6. Collaboration cadence

At session start: read this file, `METHODOLOGY.md`, the current catalogue/queue, relevant dossiers and the latest `coop.log.md`. Check recent commits and active claims before choosing work.

Claim a bounded task in `coop.log.md` with date, agent, track, scope and expected output. Work in focused files. Append a DONE / PARTIAL / BLOCKED hand-off with files changed, evidence, lifecycle changes, asset-request changes and next action. Do not overwrite another contributor's active work.

Prefer parallel work across distinct leads or dossiers. Avoid parallel edits to the same shared log or canonical queue; reconcile those sequentially.

## 7. Project-specific boundaries

- Keep the pre-1926 core and the A/B/C candidate grades from `METHODOLOGY.md`; a lead is not a track.
- Keep publication/issue date separate from recording/fixation date; thematic fit, audio provenance and rights are independent.
- Use `TRACK_MAPPING.md` as the retrieval queue and `GROK_HANDOFF.md` for the existing Grok-specific protocol. The shared Drive destination above is the Grudgemixes destination.
- Mix inclusion, sequencing and publication remain owner/editor decisions.

This shared protocol is subordinate to the project's existing methodology and owner/editor decisions.

---
