# AGENTS — how to work on this blog

This repository is a music blog, **Spite Frequencies**. Read the README for the idea. Every agent does one of two jobs: **finish posts** or **add new posts**. The only data is Markdown posts (one file per post) plus media files in `media/`. Do not add other data files, logs or registers.

## Post types and the fixed schema

Every post starts with front matter whose keys appear exactly in this order. `scripts/check.py` enforces this. Strings in double quotes; lists as YAML lists (or `[]`).

### A. Recording: `posts/recordings/<slug>.md`

```yaml
---
type: recording
title: "Headline, written like a sentence"
slug: "same-as-file-name"
date: "YYYY-MM-DD"               # date the post was written or last substantially rewritten
draft: true                      # true until the post is finished
summary: "One sentence (max 240 characters) shown in post lists"
who: "Performer(s); composer/author/recordist where relevant"
when: "1919"                     # year, date or range of the recording
where: "City, Country"
country: "Latvia"                # one place name for the location pill (modern country, or the historic state if clearer: "USSR"); "" if unknown
what: "Title in original script and translation; label & catalogue / matrix or archive item"
medium: "78 rpm disc"            # one of: 78 rpm disc, wax cylinder, x-ray record, vinyl, cassette, reel-to-reel, radio, field recording, live performance, video, digital; "" if unknown
tags:
  - "the-account"                # one or more of: the-account, out-of-turn, made-anyway, unwanted, fighting-words, found
recording_url: "https://..."     # the best public place to hear it ("" if none). YouTube, Internet Archive, SoundCloud or a direct audio file is embedded; anything else is shown as a Listen button
urls:
  - "https://..."                # sources, archive records, buy links, articles
images:
  - "media/<slug>.jpg | Credit, licence"   # or "https://... | Credit, licence"; first one is the cover. Leave [] for a generated cover
---

The story in Markdown: 80–200 words, your own words.
```

### B. Collection (a mixtape): `posts/collections/<slug>.md`

```yaml
---
type: collection
title: "Mixtape name"
slug: "same-as-file-name"
date: "YYYY-MM-DD"
draft: true
description: "One sentence about what the mixtape tells."
tracks:
  - "recording-slug-1"           # ordered; every slug must be an existing recording post
images: []
---

Liner notes: 100–250 words about what the tracks tell, in order.
```

## How posts appear in lists

Lists show each post as a row: headline, a recording indicator (*Playable here* when `recording_url` can be embedded, *Recording link* when it can only be linked), pills, the `summary`, and *Read more*. A thumbnail appears only if `images` has an entry. The pills come from `medium`, the period (decade worked out from `when`), `country`, and `tags`. Readers filter by clicking a pill, so fill these fields consistently.

## Drafts and finishing

- A post that isn't finished has `draft: true` and ends with a `## To do` list of what's missing. Drafts are kept in the repo but never published.
- A **recording** is finished when:
  - `summary`, `who`, `what`, `when`, `where`, `country` and `medium` are filled in precisely (many draft summaries, countries and media were auto-filled; check them);
  - the story is in plain blog voice and every fact is backed by a link in `urls`;
  - `recording_url` is set if any public recording exists;
  - any consent or privacy question is resolved (see Ethics);
  - the `## To do` section is removed.

  Then set `draft: false`.
- A **collection** is finished when every track is a finished recording and the liner notes are written. Then set `draft: false`.
- `check.py` refuses a finished post that still has a `## To do` section, and a finished mixtape that lists a draft track.

## How agents work together

- **Pull before you start; commit small; push to `main`.** Never force-push. There is no log and no claim system. The posts are the shared state.
- **Pick work from the drafts.** `grep -l "draft: true" posts/recordings/*.md` lists them, and each draft's `## To do` says what's needed. To avoid clashes, take a post nobody changed in the last day (`git log -1 --format=%cr -- <file>`), finish what you can, and update its `## To do` with what is still open.
- **Add details to existing posts** whenever you find them: a better source, an exact catalogue number, a recording link, a free image. Edit the post; don't create duplicates. Search titles and `who` before making a new post.
- **Add new posts** for new finds: a `draft: true` recording with whatever you know and a `## To do` list is welcome. New mixtapes may start as drafts listing draft tracks.
- **Run `python3 scripts/check.py` before every commit** (`pip install pyyaml markdown`). To preview, run `python3 scripts/build.py --out _site` and open `_site/index.html`. Never commit `_site/`.

## What to look for

Recordings where music answers a wrong:
- old grievance songs, revenge vows, accusations and feud ballads;
- music made under bans or ridicule, or by people nobody wanted to hear;
- song duels and music treated as a weapon;
- home tapes and found recordings that survived by accident.

Prefer under-represented regions and languages, women's voices, and local-language archives and small-web blogs. Confinement material (hospitals, prisons) is one theme among many, not the centre.

## Ethics and rights

- Never publish (keep `draft: true`) any recording of patients, prisoners, detainees, Indigenous or sacred material, minors, or private people until the post documents consent from the makers or their community. Private speech (taped letters, phone calls, diaries, therapy) is never published.
- Never write mockingly about makers.
- No lyrics and no long quotes from sources; paraphrase.
- Say what is uncertain.
- **Audio:** never upload copyrighted audio. Link or embed from the owner's public player. Put audio in `media/` only if it is public domain or you have permission, and say which in the story.
- **Images:** put in `media/` only images that are public domain or freely licensed (e.g. Wikimedia Commons), with credit and licence in the `images` entry. No photographs of people. Disc labels, sleeves, objects, places and instruments are fine.
