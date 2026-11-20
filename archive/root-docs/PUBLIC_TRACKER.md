# Public progress tracker

The static site publishes a deliberately small allowlist: lead title, project, status, record kind, and last-modified date. It does not copy source URLs, citations, raw notes, Google Drive links or IDs, filenames, archive requests, or full dossiers.

## Status rules
- **Done:** track downloaded and independently verified.
- **Researched:** research sufficiently complete; ready for a download-capable agent.
- **Investigating:** research, identity, evidence, or access route still being checked.

## One-time setup
1. Create the public repository `sloev/grudgemusic-public` with a `main` branch.
2. In that repository, enable GitHub Pages: Settings → Pages → Deploy from a branch → `main` → `/(root)`.
3. In `sloev/grudgemixes`, add repository secret `PUBLIC_SITE_TOKEN`: a fine-grained PAT restricted to `sloev/grudgemusic-public`, with **Contents: Read and write**. The source repo's GITHUB_TOKEN cannot push to another repository.
4. Run Actions → Publish public research tracker → Run workflow.

## Cost-conscious choices
- No Node build, dependency installation, third-party action, or cache.
- Python standard library only.
- Shallow source checkout and shallow destination clone.
- Runs on relevant source changes, manual dispatch, and once daily.
- Five-minute timeout; concurrency cancels superseded runs.

The generator scans current Grudge Mixes candidate/research files and future `projects/insanemusic` and `projects/sovietfilm` directories. As material is migrated, place it in those project folders. Only explicit verified-download and ready-for-download markers advance status; otherwise it remains Investigating.
