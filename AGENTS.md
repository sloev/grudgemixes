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
summary: "3–5 sentences (400–650 characters, max 900) shown in post lists: the story in brief, in plain words"
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
  - "media/<slug>.jpg | Caption saying what it shows. Author, licence, via source"   # first one is shown; [] = no image (nothing is shown)
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

## How posts appear on the site

- **Front page:** every finished recording, newest first, on one continuously growing page (no pagination, ever). Each row shows the headline, a recording indicator (*Playable here* when `recording_url` can be embedded, *Recording link* when it can only be linked), pills, the `summary` and *Read more*, plus a thumbnail only if the post has an image.
- **Pills:** they come from `medium`, the period (the decade worked out from `when`), `country` and `tags`. Readers filter by clicking a pill, so fill these fields consistently.
- **Mixtapes:** they have their own page under the *Mixtapes* menu item.
- **Post pages:** they show an image only if `images` has an entry. Nothing is generated in its place.

## Images: find one for every post

A good picture makes a post. Finding one is a priority whenever you work on a post, and the picture should be close to the story:
- the disc label, sleeve or cassette;
- the instrument;
- the building, street or place where it happened;
- a period print, newspaper drawing or score;
- a patent drawing or poster.

A generic stand-in (any cassette, any record) is a last resort.

Rules:
- Use only public-domain or freely licensed images (Wikimedia Commons is the main source).
- No photographs of people, and no street scenes where people dominate. Drawings, prints and paintings are fine.
- Save a copy as `media/<slug>.jpg`, at most 1200 px on the long side. Commons serves `…/thumb/…/1280px-<name>` when the full file is refused.
- Write a caption that says what the picture shows and how it connects to the story, then the author, licence and source.
- Add the image's Commons file page to `urls`.

A public-domain recording on Commons (`upload.wikimedia.org/…mp3` or `.ogg`) can be used as `recording_url` and plays on the page.

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

- **`main` is the only working branch.** Start by pulling the latest `main`, make changes directly on `main`, and commit directly to `main`. Never create, check out, push to, or otherwise work on another branch. Never open a pull request. If direct writes to `main` are unavailable, stop and ask the repository owner to fix access; do not create a workaround branch. Never force-push. There is no log and no claim system. The posts are the shared state.
- **Pick work from the drafts.** `grep -l "draft: true" posts/recordings/*.md` lists them, and each draft's `## To do` says what's needed. To avoid clashes, take a post nobody changed in the last day (`git log -1 --format=%cr -- <file>`), finish what you can, and update its `## To do` with what is still open.
- **Add details to existing posts** whenever you find them: a better source, an exact catalogue number, a recording link, a free image. Edit the post; don't create duplicates. Search titles and `who` before making a new post.
- **Add new posts** for new finds: a `draft: true` recording with whatever you know and a `## To do` list is welcome. New mixtapes may start as drafts listing draft tracks.
- **Before every commit run `python3 scripts/check.py && python3 scripts/build.py --out docs`** (`pip install pyyaml markdown`) and commit the regenerated `docs/` together with your post changes. GitHub Pages serves `docs/` directly, so the site only updates when `docs/` is rebuilt. Never edit files in `docs/` by hand. If two agents' `docs/` changes conflict, take either side and rebuild.

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
