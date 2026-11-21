# AGENTS — Spite Frequencies

Work directly on `main` only. Never create branches or pull requests, and never force-push. GitHub Pages builds from the root of `main` using its native Jekyll builder. Do not add a custom site generator or Actions deployment workflow.

## Content locations

- Recordings: `posts/_recordings/<NNN>-<slug>.md`
- Mixtapes: `posts/_mixtapes/<NNN>-<slug>.md`
- Assign one unique, incrementing, zero-padded catalogue number across both collections. Never renumber existing posts; new posts use the next unused number. Keep the original `slug` front-matter value unchanged for mixtape track references.
- Images: `media/`
- Templates: `_layouts/` and root listing pages.

Every document in the Jekyll collections is rendered, including documents marked `draft: true`. Draft is editorial metadata only; it does not prevent publication. Catalogue numbers are the stable visible identifiers; dates remain metadata, not identifiers.

## One-entry-per-artist rule

- Keep at most one recording post per named artist, band, group, or recording project. Do not create separate posts for different songs, sides, matrix numbers, releases, or sessions by the same act.
- When an artist has solo and group recordings under closely related identities, consolidate them into one artist entry unless there is a clear, sourced reason they are distinct acts.
- Put multiple recordings and their catalogue details inside that single post. Update mixtape track references to the surviving slug; never leave references to deleted posts.
- For anonymous or traditional performances, use one post per distinct archival recording event or documented collection, not one post per track.
- Before adding a post, search the existing catalogue for the artist's name, aliases, collaborators, and group affiliations.

## Date eligibility (hard rule)

- Every recording featured anywhere in the catalogue must have been originally recorded no later than 31 December 1999. Release date alone is not sufficient when it differs from the recording date.
- Recording posts must state a sourced original recording year or range in `when`; uncertain or missing dates must be researched before inclusion.
- Every named performer, band, or project must have ceased performing or releasing as that act by 31 December 2000. Record the sourced final active year in `active_until`. For a genuinely anonymous, traditional, one-off, or archival field recording with no continuing named act, use a justified `act_status` value of `anonymous-traditional`, `one-off`, or `archival-field-recording`.
- Every post must explain its relevance to marginalised, unknown, or outsider music in `why_outsider`, and cite source URLs in `urls`. No generic mainstream catalogue entries. Every mixtape track must resolve to a recording post that passes the date, act-status, outsider-relevance, and source checks. Do not add post-1999 recordings, continuing acts, or undated material to new posts or track lists.
- `scripts/check_pre_2001.py` and `.github/workflows/pre-2001-check.yml` enforce these rules.

## Recording schema

Keep the established front matter field order: `type`, `title`, `slug`, `date`, `draft`, `summary`, `who`, `when`, `active_until`, `act_status`, `why_outsider`, `where`, `country`, `what`, `medium`, `tags`, `recording_url`, `urls`, `images`. Use double-quoted strings and YAML lists. Recording stories should be 80–200 words and factual claims should have sources in `urls`.

Allowed media: 78 rpm disc, wax cylinder, x-ray record, vinyl, cassette, reel-to-reel, radio, field recording, live performance, video, digital, or empty. Allowed tags: the-account, out-of-turn, made-anyway, unwanted, fighting-words, found.

## Mixtape schema

Use `type: collection`, then `title`, `slug`, `date`, `draft`, `description`, `tracks`, and `images`. Track slugs should refer to recording documents. Liner notes should be 100–250 words.

## Ethics and rights

- Never publish recordings of patients, prisoners, detainees, Indigenous or sacred material, minors, or private people unless consent from makers or their community is documented. Private speech (letters, calls, diaries, therapy) is never published.
- Never mock makers. Do not reproduce lyrics or long quotations; paraphrase and state uncertainty.
- Never upload copyrighted audio. Link to or embed the rights-holder's public player.
- Use only public-domain or freely licensed images, with author, licence, caption and source. No photographs of people.
- Prefer under-represented regions and languages, women's voices, and local-language archives.
