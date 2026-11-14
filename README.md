# Grudge Mixes

**An archival music series for spite, retaliation, revenge, punishment and collective grievance.**

This repository coordinates research and editorial development for a series of global mixes for [spitebites.party](https://spitebites.party), built from early commercial recordings. The companion book, [*How to Keep a Grudge for Generations*](https://github.com/sloev/grudgebook), provides the conceptual and editorial framework.

The subject is not simply “angry songs.” The project investigates how musical performances represent remembered offences, costly harm, payback, sanctions, betrayal, insult and collective grievance across different languages, genres and historical settings.

## Editorial premise

Treat the archive seriously. The central conceit is the existence of a rigorous musical archive of resentment; the research and writing should remain historically and discographically exact.

Do not moralize, prescribe forgiveness, ridicule grudge-holders or force puns. Preserve local terminology and explain its context. Avoid treating a country, culture or genre as uniform or timeless.

### Working distinctions

- **Spite:** deliberately imposing a cost on another while accepting a cost to oneself.
- **Retaliation:** a response to a prior injury, often immediate.
- **Punishment:** a sanction imposed for a perceived or established violation.
- **Revenge:** payback, often calculated or delayed.
- **Resentment:** a durable response to perceived wrong.
- **Grudge:** the maintained record or stance of an unresolved grievance.

These are editorial tools, not universal translations. A song title alone does not establish motive. Distinguish documented events, folklore, literary representation, stage convention and later popular myth.

## Non-negotiable candidate gates

A recording must pass all three gates before it can be called a verified candidate:

1. **Date and composition**
   - The master was published or fixed before **1926-01-01**. Record publication and fixation dates separately.
   - The composition is traditional with documented provenance, or its author/composer/lyricist died before **1956-01-01**.
   - Identify translators, arrangers and later adaptations separately. Do not assume an old melody makes a later lyric or arrangement eligible.

2. **Archival audio**
   - Identify the exact archival item and direct audio file.
   - Establish whether the file is an unedited transfer of the original 78rpm shellac disc or wax cylinder.
   - Document restoration, equalization, speed correction, filtering, edits and derivative formats. An archive page or MP3 access copy is not proof of a raw transfer.

3. **Rights**
   - Assess composition, master/phonogram, performer, transfer/digitization and repository terms separately.
   - Assess the United States, EU/EEA, UK and every intended commercial territory independently.
   - Never infer worldwide public-domain status from age, a catalogue date or an archive label. Use **NOT CLEARED** until reviewed.

## Candidate status vocabulary

| Status | Meaning |
|---|---|
| **VERIFIED** | Evidence supports the date/composition and exact archival-audio gates. Rights assessment is documented; this status alone does not mean cleared. |
| **PARTIALLY VERIFIED** | Strong primary evidence exists, but one or more required fields or gates remain unresolved. |
| **LEAD** | A promising title, performer or discographical reference; not yet tied to the exact eligible master and archival audio. |
| **REJECTED** | Fails a hard gate or has a documented reason not to proceed. Preserve the reason so the lead is not repeatedly re-investigated. |

Commercial clearance is a separate decision and requires human legal/editorial review.

## Preferred archives and discovery sources

Prioritize:

- [Internet Archive — Great 78 Project](https://archive.org/details/georgeblood)
- [Library of Congress — National Jukebox](https://www.loc.gov/collections/national-jukebox/)
- [UCSB Cylinder Audio Archive](https://www.library.ucsb.edu/special-collections/performing-arts/cylinders)
- [Europeana](https://www.europeana.eu/)
- National sound archives and specialist discographies with explicit provenance and rights information.

Use collector databases, commercial catalogues, discographies and secondary scholarship as discovery and corroboration sources—not as substitutes for the exact archival audio object or primary metadata.

## Required candidate record

Every substantial candidate should have a Markdown file under `candidates/` or a clearly labelled research lead under `research/`. Include:

- Stable candidate ID (once sufficiently established), status and proposed mix/sequence.
- Performer(s), catalogue title, original language and local genre.
- Recording date and evidence; recording location and evidence.
- Label, catalogue number, matrix and take.
- Exact archive item URL and direct audio URL; file format and transfer details.
- Publication/fixation evidence; composition author/traditional provenance and death-date evidence.
- Rights notes by territory and rights layer.
- Taxonomic mechanism, supported by lyrics/performance/context.
- Original-language excerpt with verified transcription, literal and idiomatic translation, and sources.
- 150–250 word liner note in the project's editorial voice.
- Open questions, confidence and decision.

Do not invent lyrics, translations, matrices, dates or audio URLs. Quote only what has been verified against a reliable text or recording. Record uncertainty explicitly.

## Taxonomy and sequencing

Possible non-exclusive classifications:

- Calculated revenge / delayed payback
- Immediate retaliation
- Punishment / sanction
- Public shaming, insult or counter-insult
- Spite / costly harm
- Maintained personal grievance
- Intergenerational or collective grievance
- Protest / grievance testimony (not automatically revenge)
- Betrayal / lament (not automatically a grudge)

Build a geographically and linguistically varied sequence, not a country-by-country checklist. Sequence by mechanism and sound-world while retaining local context. Possible groupings—*The Insult*, *The Debt*, *The Betrayal*, *The Feud*, *The Public Answer*, *The Inherited Account*—are provisional editorial structures, not claims about local genres.

## Repository map

```
README.md
coop.log.md                  Multi-agent coordination and dated research ledger
candidates/                   Candidate records with stable IDs
research/                     Screening notes, leads, rejected candidates, methods
```

The companion book lives in [sloev/grudgebook](https://github.com/sloev/grudgebook).

## How to contribute

1. Read this README and the full [`coop.log.md`](coop.log.md) before starting.
2. Read the relevant parts of the companion `grudgebook` repository to understand the editorial voice and terminology.
3. Check existing candidate and research files before creating a duplicate.
4. Work additively. Prefer a new, clearly named file; do not silently rewrite another contributor's findings or upgrade a status.
5. Append a dated entry to `coop.log.md` with agent, task, files created/edited, sources, status, unresolved questions and handoff.
6. Cite primary evidence wherever possible. Preserve negative findings and reasons for rejection.
7. Separate what is known from what is inferred. Do not call an item commercially cleared without a territory-specific rights review.

## Current research snapshot

As of **2026-11-14**, the repository contains:

| Recording / lead | Status | Current limitation |
|---|---|---|
| Enrico Caruso, “Vesti la giubba” (Victor 930, 1904) | **PARTIALLY VERIFIED** | Exact issue/publication and raw-transfer details; rights review |
| “Papus Rache,” Carl Gutentag / *Bar Kochba* (Homocord 1118) | **LEAD** | Exact master, matrix, recording date/location and archival audio |
| “Revenge! Timotheus Cries,” Handel / HMV D589 (1921), and Vocalion X-9560 (1924) | **LEAD** | Stronger discographical evidence now exists for HMV matrix Cc584-2, issue 02927; exact archival audio and rights remain unlocated/unassessed |
| Robert Radford, “Hagen meditates revenge,” Wagner / HMV D704 (1922) | **LEAD** | Strong UCSB/Victor discographical metadata; exact archival audio and rights remain unlocated/unassessed |
| Emilio de Gogorza and Louise Homer, “Vengeance at Last,” Saint-Saëns / Victor 87501 (1908) | **PARTIALLY VERIFIED** | Exact FAU archive item and strong matrix/session metadata; FAU public access is non-downloadable and not a commercial licence; transfer and rights review remain open |

None of these entries is represented as commercially cleared. The current evidence does **not** establish a five-to-eight-track verified batch. The project should prefer a small defensible selection over a larger speculative one.

See [`research/first-pass-screening.md`](research/first-pass-screening.md), the individual candidate/lead records and [`coop.log.md`](coop.log.md) for the evidence trail.

## Immediate priorities

1. Find exact archival transfers for the HMV Handel D589 and Wagner D704 recordings.
2. Find exact archival transfers for Vocalion X-9560 and Goldfaden/Homocord 1118.
3. Expand searches across non-English commercial catalogues and cylinder collections.
4. Verify publication and fixation dates from primary catalogues, labels, ledgers or contemporary trade sources.
5. Build a separate rights/clearance register for intended territories.
6. Do not assign production IDs or sequence tracks until their evidence is strong enough.
