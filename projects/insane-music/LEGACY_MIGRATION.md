# Insane Music legacy migration audit

**Audit date:** 2026-11-17  
**Source:** `sloev/insanemusic`, default branch `main`  
**Destination:** `sloev/grudgemixes/projects/insane-music/`

## Result

The legacy repository contains 14 tracked files (no audio or other binary assets). All 12 substantive project files have been copied into the active `projects/insane-music/` workspace. Their destination Git blob SHAs were compared with the source tree; all 12 match exactly.

The two remaining source files, `AGENTS.md` and `WORKSPACE_REDIRECT.md`, are duplicate workspace-routing instructions, not project research material. They were intentionally not copied into the active project folder; the canonical repository's root `AGENTS.md` and `WORKFLOW.md` govern work there.

## Migrated files

- `README.md`
- `TRACK_MAPPING.md`
- `archive-requests.md`
- `catalogue.md`
- `coop.log.md`
- `environment-leads.md`
- `method.md`
- `research_method.md`
- `research/brazil-demo-tapes-small-web-2026-11-16.md`
- `research/flinders-retrieval-2026-11-16.md`
- `research/philippines-cordillera-country-cassette-ecology-2026-11-16.md`
- `research/philippines-cordillera-salidummay-2026-11-16.md`

## Scope and limitations

- The three legacy Drive handoff entries remain represented in the migrated `TRACK_MAPPING.md`; they are not proof that corresponding files are present in Drive.
- The five audio inventory records in `drive-audio-inventory/` are separate, newer records based on the user's 2026-11-17 recursive Drive listing. They are not a substitute for the legacy catalogue or research files.
- No audio binaries were tracked in the legacy repository tree, so no audio files could be migrated from Git.
- The old repository remains read-only. Future edits belong only in the canonical project directory.
