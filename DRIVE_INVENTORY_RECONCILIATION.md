# Drive inventory reconciliation — 2026-11-17

## Result from the supplied recursive Google Drive listing

| Project | Audio files listed | Staging archives |
|---|---:|---:|
| Grudge Mixes | 17 | 0 |
| Insane Music | 5 | 0 |
| Soviet Film Music | 13 | 1 |
| **Total** | **35** | **1** |

All 35 MP3/FLAC/OGG filenames supplied by the user are now represented as individual Markdown inventory records under the three project folders' `drive-audio-inventory/` directories. The Kancheli MKM 197 TAR archive is separately recorded and is not counted as an audio track.

## Interpretation

- The 35 audio files are **listed in Drive according to the user-supplied recursive listing**. This is evidence against the public site's earlier zero-file count.
- The live Drive contents, file bytes, playback, duration, checksum and exact file IDs have not been independently inspected in this pass. The tracker therefore says "In Drive (listed)", not "Done / independently verified".
- Soviet Film Music's 13 audio files are film-mix excerpts/full mixes according to their filenames, not 13 isolated soundtrack tracks.
- Insane Music's five filenames are recorded exactly as supplied. Three earlier provisional filenames (Lonesome Jailhouse Blues, Faust, and Mille et un jours) do not occur in this supplied list and have been marked as superseded provisional notes.
- The two Saint-Saëns de Gogorza/Homer files are retained separately; do not deduplicate without comparing file hashes or audio.

## Inventory locations

- Grudge Mixes: `projects/grudge-mixes/drive-audio-inventory/`
- Insane Music: `projects/insane-music/drive-audio-inventory/`
- Soviet Film Music: `projects/soviet-film-music/drive-audio-inventory/`

## Next verification pass

When live Drive access is available, match each filename to its Drive file ID and capture size, duration, MIME type and checksum. Reopen/play each file where practical. Preserve separate copies and transfers until hashes and audio comparison establish duplicates.
