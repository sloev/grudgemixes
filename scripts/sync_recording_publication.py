#!/usr/bin/env python3
"""Keep unfinished or unlistenable recording posts out of the public Jekyll build.

The source files remain in the repository. They return to the site automatically
when the draft flag is cleared and a recording-specific listening URL or approved
embed is present. Mixtapes are withheld if they are drafts or depend on withheld
recordings.
"""
from pathlib import Path
import yaml

from check_recording_access import ROOT, COLLECTION, parse_frontmatter, usable_url

MIXTAPES = ROOT / "posts" / "_mixtapes"
CONFIG = ROOT / "_config.yml"
REPORT = ROOT / "unready-publication-items.txt"
BEGIN = "# BEGIN GENERATED RECORDING PUBLICATION EXCLUSIONS"
END = "# END GENERATED RECORDING PUBLICATION EXCLUSIONS"

def main():
    excluded = []
    reasons = []
    ready_slugs = set()
    recording_files = sorted(COLLECTION.glob("*.md"))

    for path in recording_files:
        data = parse_frontmatter(path)
        if data.get("type") != "recording":
            continue
        valid_url, why_url = usable_url(data.get("recording_url"), "recording_url")
        valid_embed, why_embed = usable_url(data.get("recording_embed_url"), "recording_embed_url")
        why = []
        if data.get("draft") is True:
            why.append("marked draft")
        if not (valid_url or valid_embed):
            why.append("no valid recording-specific URL/embed")
        if why:
            rel = path.relative_to(ROOT).as_posix()
            excluded.append(rel)
            reasons.append(f"{rel} — {'; '.join(why)}")
        else:
            ready_slugs.add(str(data.get("slug") or path.stem))

    mixtape_files = sorted(MIXTAPES.glob("*.md"))
    ready_mixtapes = 0
    for path in mixtape_files:
        data = parse_frontmatter(path)
        if data.get("type") != "collection":
            continue
        tracks = data.get("tracks") or []
        if isinstance(tracks, str):
            tracks = [tracks]
        missing = [str(slug) for slug in tracks if str(slug) not in ready_slugs]
        why = []
        if data.get("draft") is True:
            why.append("marked draft")
        if not tracks:
            why.append("no tracklist")
        if missing:
            why.append("contains withheld recording(s): " + ", ".join(missing))
        if why:
            rel = path.relative_to(ROOT).as_posix()
            excluded.append(rel)
            reasons.append(f"{rel} — {'; '.join(why)}")
        else:
            ready_mixtapes += 1

    config_text = CONFIG.read_text(encoding="utf-8")
    block = BEGIN + "\n" + "".join(f"  - {path}\n" for path in sorted(set(excluded))) + END + "\n"
    if BEGIN in config_text and END in config_text:
        start = config_text.index(BEGIN)
        finish = config_text.index(END, start) + len(END)
        config_text = config_text[:start] + block.rstrip("\n") + config_text[finish:]
    else:
        config_text = config_text.rstrip() + "\n" + block
    CONFIG.write_text(config_text.rstrip() + "\n", encoding="utf-8")
    REPORT.write_text("\n".join(reasons) + ("\n" if reasons else ""), encoding="utf-8")

    print(f"RECORDINGS SCANNED: {len(recording_files)}")
    print(f"PUBLIC-READY RECORDINGS: {len(ready_slugs)}")
    print(f"WITHHELD RECORDING POSTS: {sum(1 for x in excluded if x.startswith('posts/_recordings/'))}")
    print(f"MIXTAPES SCANNED: {len(mixtape_files)}")
    print(f"PUBLIC-READY MIXTAPES: {ready_mixtapes}")
    print(f"WITHHELD MIXTAPES: {sum(1 for x in excluded if x.startswith('posts/_mixtapes/'))}")
    print(f"REPORT WRITTEN: {REPORT.name}")

if __name__ == "__main__":
    main()
