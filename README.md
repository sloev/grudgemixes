# Spite Frequencies

*Music made where it wasn't wanted, and songs that kept the score.*

A music blog about recordings and mixtapes: named collections of recordings that already have their own posts.

## Publishing

GitHub Pages builds this site with its built-in Jekyll builder from the root of the `main` branch. There is no custom site generator and no Actions deployment workflow.

GitHub Settings → Pages → Build and deployment → Deploy from a branch → `main` → `/(root)`.

- `_config.yml` configures Jekyll collections.
- `posts/_recordings/` contains recording documents; `posts/_mixtapes/` contains mixtapes.
- Every Markdown filename begins with a unique, zero-padded catalogue number followed by its slug (for example, `001-example-title.md`). Numbers are permanent identifiers, shared across both collections; new posts take the next unused number. The slug remains in front matter for cross-linking.
- `media/` contains post images.
- `_layouts/`, `index.html`, and `mixtapes/index.html` are Jekyll templates. There is no About page.
- `style.css` is the stylesheet.
- `jekyll-feed` generates the RSS feed.

All collection documents are rendered. The `draft` field is editorial metadata and does not hide a document from Jekyll output. The catalogue number—not the publication date—is the visible post identifier; dates remain descriptive metadata.

Site: https://sloev.github.io/grudgemixes/ · Feed: https://sloev.github.io/grudgemixes/feed.xml

## Editorial rules

- One recording post per artist, band, group, or recording project; multiple sides, songs, and sessions belong together in that entry.
- Original recording date must be before 2000, and a named act must have ceased by the end of 2000.
- The catalogue prioritises marginalised, unknown, and outsider music; sources and uncertainty should be stated.
- Every recording post must provide either `recording_url` (a verified, recording-specific public listening page or direct audio/video stream) or `recording_embed_url` (a verified player embed for that exact recording). The recording layout renders supported embeds responsively. General archive homepages, catalogues, biographies, and related articles do not count. If the exact recording cannot be played publicly, do not fabricate a link; withhold the post until access is secured. `draft: true` does not hide a post on this site.
- Genuine image gaps are listed in [missing-post-images.txt](missing-post-images.txt). No placeholders are used.

See [AGENTS.md](AGENTS.md) for the full editorial and rights rules.

## The idea

A grudge is a wrong someone refuses to let go of, and music is one of the oldest ways people keep that refusal alive. Every post asks what the wrong or refusal was, who stood on each side, and what the music does about it: keep the record, defy, annoy, or strike back.

We never mock the people who made this music. When there is a joke, it is on taste.


## Public catalogue readiness

The source repository keeps research drafts, but the live site publishes only recordings with \`draft: false\` and a recording-specific listening URL or approved player embed. Mixtapes are published only when every referenced recording is public. Unfinished or unlistenable entries remain in the repository and are automatically excluded from the site; they return when their story, access, and playback checks are complete.

The GitHub Actions audit reports withheld entries and checks the public set. Its URL check is structural, not proof of playback: each link still requires a human check that the exact recording plays.
