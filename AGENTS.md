# AGENTS — how every agent works in this repository

**Applies to every human or AI agent (Claude, Grok, others) and every scheduled task.** Updated 2026-11-20. This repository is private and is the only workspace for two projects. The legacy repositories `sloev/insanemusic` and `sloev/sovietfilm` are retired: never write to them. The Soviet film music project has been dropped; do not restart it here.

## 1. The two projects

| Project | Admission rule | Rules file |
|---|---|---|
| **Grudge Mixes** | A recorded grievance-response (revenge, retaliation, punishment, accusation, curse, feud, defiance, inherited grievance) recorded **before 1926**. | `projects/grudge-mixes/METHODOLOGY.md` |
| **Insane Music** (published as *Music in Spite*) | An extant, identifiable recording of music made where it was not expected or not tolerated: confinement, banned or scratched music, unwelcome voices, untaught/DIY makers, found tapes. Any date. | `projects/insane-music/method.md` |

Keep each project's rules separate. A track may fit both; say so.

## 2. The four files that matter

| File | What it is | Who updates it |
|---|---|---|
| `LEADS.md` | The single register of every track and lead: background, why it fits, sources, listen/download/buy links, download status, planned mix, dossier path. | Every agent that adds or changes a lead, in the same commit. |
| `MIXES.md` | The planned volumes, tracklists, curation rules and balance table. | Only when the owner or an agent proposes a tracklist change; mark proposals as such. |
| `coop.log.md` | Shared dated log. | Every agent, once per session. |
| Dossiers | One Markdown file per lead with the full evidence (`projects/grudge-mixes/candidates/`, `projects/grudge-mixes/leads/`, `projects/grudge-mixes/research/`, `projects/insane-music/research/`, `projects/insane-music/catalogue.md`). | The agent doing the research. |

`LEADS.md` is a summary; the dossier is the evidence. If they disagree, fix `LEADS.md`.

## 3. Repository layout

```
README.md  AGENTS.md  LEADS.md  MIXES.md  coop.log.md
projects/grudge-mixes/    METHODOLOGY.md, candidates/, leads/, research/, drive-audio-inventory/
projects/insane-music/    method.md, research_method.md, catalogue.md, environment-leads.md,
                          archive-requests.md, TRACK_MAPPING.md, research/, drive-audio-inventory/,
                          legacy/ (snapshots from the retired repo and the old duplicate folder)
scripts/build_site.py     builds the encrypted follow-along site
archive/                  superseded plans and root documents; read-only history
```

Do not create new top-level files or folders without the owner's request.

## 4. Work by ability

Start every session by stating your abilities in your claim line (for example `abilities: web, repo-write, no-drive`). Then take only work your tools can actually finish.

| If you can… | Take these tasks | Never… |
|---|---|---|
| **Read the repo only** (no web, no write) | Review dossiers for gaps, contradictions, missing sources and duplicate IDs; draft text and hand it to the owner in chat. | …claim you checked a source online. |
| **Search the web** (search/fetch, no downloads) | Discovery (section 7); confirm label, catalogue and matrix numbers; find archive pages and listen/buy URLs; rights and consent research; mark leads "ready for retrieval" with the exact file URL. | …mark anything downloaded. |
| **Download files** (shell with network or browser) but **no Drive access** | Fetch the audio from the source URL, record duration, checksum (`sha256sum`) and source details in the dossier, then note "fetched, awaiting Drive upload" in the dossier (LEADS.md stays `No`) and hand off in `coop.log.md`. | …delete the local copy before someone confirms it is in Drive. |
| **Google Drive access** | Upload fetched files with the naming rule (section 8); add inventory records with the Drive file ID; reconcile Drive against `LEADS.md`; mark `Yes (listed)`. | …rename or delete files others put in Drive without noting it in the log. |
| **Play or analyse audio** | Listen, time, checksum and spot-check the files in Drive; confirm the recording is the one claimed (label voice-over, take, speed); mark `Yes (verified)`. | …verify from a file name or a listing alone. |
| **Write to the repo** | Every agent with write access commits its own dossier, `LEADS.md` and log updates directly to `main`. | …rewrite another agent's dossier wholesale; append or correct with a dated note. |
| **No repo write** (e.g. a chat-only agent) | Put the finished text, with file paths, in a deposit file the owner pastes in, or give it to the owner in chat; an agent with write access commits it and credits you in the log. | …assume your work was saved. |
| **Run code and push** | Rebuild `LEADS.md` sections, run `scripts/build_site.py` locally to check it builds, fix tooling. | …print or commit the site password. |

If a task needs an ability you lack, finish the part you can do, write the exact next step and the ability it needs in `coop.log.md`, and stop.

## 5. Coordination

- **`coop.log.md` is the shared board.** Every entry starts with a dated heading and the agent's name: `## 2026-11-20 — Grok: …`.
- **Claim before work.** Add a short claim line: `CLAIM <agent> <date>: <task> (IDs or files) — abilities: …`. One claim per agent at a time, kept small (one lead, one region, one volume, or one batch of up to 10 downloads).
- **Check claims first.** Do not work on IDs or files that another agent claimed in the last 48 hours. Claims older than 48 hours with no entry are stale and may be taken; say so in your claim.
- **Hand off explicitly.** When a task moves between abilities (search → download → Drive → verify), end your entry with `HANDOFF → <ability needed>: <IDs>, <exact URLs or paths>`. The next agent copies that line into its claim.
- **Close what you open.** Finish with `DONE` or `PARTIAL` and list changed files. A claim you cannot finish is released with `RELEASED`.
- **Avoid edit collisions.** Pull before you start and again before you commit; commit small and often; on conflict, keep both versions of a log and merge dossiers by hand. Never force-push `main`.
- **Owner decisions win.** Anything about tracklists, consent or clearance is proposed in the log as `PROPOSAL` and waits for the owner.
- **Project logs.** `projects/insane-music/coop.log.md` holds the older Insane Music history; new entries go in the root `coop.log.md`.

## 6. Session routine

1. Read this file, the relevant project rules file, `MIXES.md` and the last entries of `coop.log.md`.
2. Search `LEADS.md` and the dossiers before adding anything, so nothing is duplicated.
3. Claim a bounded task in `coop.log.md` as described in section 5, stating your abilities.
4. Do the work (sections 7–8), within your abilities (section 4).
5. Update the dossier, then `LEADS.md`, then `MIXES.md` if a tracklist is affected.
6. End with a dated `coop.log.md` entry: what changed (files), evidence found, what is still open, and the next action.
7. Commit directly to `main` with a clear message. Do not open pull requests unless the owner asks.

## 7. Discovery (finding leads)

- **Diversity is a requirement, not a bonus.** Before adding a lead, check the region and setting balance in `MIXES.md`. Prefer regions, languages and kinds of maker that are under-represented. Women's voices, non-Anglophone sources and local-language archives come first.
- **Prisons and psychiatric institutions are one strand only.** The owner has asked that they not dominate. Add new prison or hospital leads only when they are exceptional, and say why.
- Search in the local language and in local archives (national libraries, sound archives, university repositories, collectors' small-web sites), not only US/UK English sources.
- Every new lead needs: exact recording identity where possible (performer, title in original script and transliteration, label and catalogue, matrix, date, place, or archive item ID); the story; why it fits which project; sources with URLs; rights and consent flags.

## 8. Enrichment and audio

- **Download status** has three values only: `No`; `Yes (listed)` = in the project Google Drive but not yet played or checksummed; `Yes (verified)` = played, timed and checksummed, with the Drive file ID recorded. Never claim a download you did not make.
- When you put a file in Drive: name it `<ID>_<Performer>_<Title>_<Label-Cat>_<Year>.<ext>`, add an inventory record in the project's `drive-audio-inventory/` (filename, Drive file ID, source URL, source carrier, transfer details, duration), and update the entry's **Downloaded** line in `LEADS.md`.
- Prefer original-carrier transfers from archives (LOC, DAHR, Internet Archive 78s, national libraries) over commercial reissues; record which you used.
- Agents without Drive or download ability must not claim retrieval; they mark a lead "ready for retrieval" in its dossier with the exact source URL.

## 9. Evidence, rights and ethics

- Cite sources next to claims; keep original spellings; state uncertainty and conflicts instead of resolving them by guesswork.
- Keep research grade, project fit, audio availability, rights and consent as separate facts.
- Nothing is cleared until the publisher says so. Flag (⚠) compositions or translations by people who died after 1955, unpublished field recordings, reissue restoration rights and living makers.
- Recordings of patients, prisoners, detainees, Indigenous communities and private individuals need the makers' or their community's consent, not only an archive's permission. Never include private speech (diaries, voicemails, therapy or medical recordings) as a track.
- Never write mockingly about makers. Insane Music material is never tied to joke merchandise.

## 10. IDs

- Grudge Mixes: `GM-<country>-<nnn>` (ISO-style country code, next free number). Insane Music: `IM-<nnn>` (next free number in `catalogue.md`).
- Check for collisions before assigning. Known collisions to fix: two `GM-AM-001` files and two `GM-IN-001` files (listed in `LEADS.md`).
- New leads without IDs live in `LEADS.md` section C until a dossier is written; give them an ID then.

## 11. Follow-along site

`scripts/build_site.py` renders `LEADS.md`, `MIXES.md` and every research Markdown file into one encrypted page and pushes it to the public repository `sloev/grudgemusic-public`. It runs from `.github/workflows/publish-site.yml` on every push to `main`. The page decrypts only in the browser with the owner's password, which is kept in the `SITE_PASSWORD` repository secret and never written into any file. Do not publish anything outside this mechanism.
