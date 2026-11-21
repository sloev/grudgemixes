# AGENTS — Spite Frequencies

Work directly on `main` only. Never create branches or pull requests, and never force-push. GitHub Pages builds from the root of `main` using its native Jekyll builder. Do not add a custom site generator or Actions deployment workflow.

## Content locations

- Recordings: `posts/_recordings/<slug>.md`
- Mixtapes: `posts/_mixtapes/<slug>.md`
- Images: `media/`
- Templates: `_layouts/` and root listing pages.

Every document in the Jekyll collections is rendered, including documents marked `draft: true`. Draft is editorial metadata only; it does not prevent publication.

## Recording schema

Keep the established front matter field order: `type`, `title`, `slug`, `date`, `draft`, `summary`, `who`, `when`, `where`, `country`, `what`, `medium`, `tags`, `recording_url`, `urls`, `images`. Use double-quoted strings and YAML lists. Recording stories should be 80–200 words and factual claims should have sources in `urls`.

Allowed media: 78 rpm disc, wax cylinder, x-ray record, vinyl, cassette, reel-to-reel, radio, field recording, live performance, video, digital, or empty. Allowed tags: the-account, out-of-turn, made-anyway, unwanted, fighting-words, found.

## Mixtape schema

Use `type: collection`, then `title`, `slug`, `date`, `draft`, `description`, `tracks`, and `images`. Track slugs should refer to recording documents. Liner notes should be 100–250 words.

## Ethics and rights

- Never publish recordings of patients, prisoners, detainees, Indigenous or sacred material, minors, or private people unless consent from makers or their community is documented. Private speech (letters, calls, diaries, therapy) is never published.
- Never mock makers. Do not reproduce lyrics or long quotations; paraphrase and state uncertainty.
- Never upload copyrighted audio. Link to or embed the rights-holder's public player.
- Use only public-domain or freely licensed images, with author, licence, caption and source. No photographs of people.
- Prefer under-represented regions and languages, women's voices, and local-language archives.
