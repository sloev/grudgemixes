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
- Genuine image gaps are listed in [missing-post-images.txt](missing-post-images.txt). No placeholders are used.

See [AGENTS.md](AGENTS.md) for the full editorial and rights rules.

## The idea

A grudge is a wrong someone refuses to let go of, and music is one of the oldest ways people keep that refusal alive. Every post asks what the wrong or refusal was, who stood on each side, and what the music does about it: keep the record, defy, annoy, or strike back.

We never mock the people who made this music. When there is a joke, it is on taste.
