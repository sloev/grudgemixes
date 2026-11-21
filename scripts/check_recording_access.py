#!/usr/bin/env python3
"""Structural check for recording-specific listening URLs or embeddable players.

This does not prove that a remote player works; every destination still needs
human playback verification before it can be considered editorially approved.
"""
from pathlib import Path
from urllib.parse import urlparse
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
COLLECTION = ROOT / "posts" / "_recordings"
GENERIC_PATHS = {
    "", "/", "/catalog", "/catalog/", "/collections", "/collections/",
    "/search", "/search/", "/about", "/about/", "/audio", "/audio/",
    "/listen", "/listen/",
}
EMBED_HOSTS = {
    "youtube.com", "www.youtube.com", "youtube-nocookie.com",
    "www.youtube-nocookie.com", "youtu.be", "archive.org", "www.archive.org",
    "soundcloud.com", "w.soundcloud.com", "bandcamp.com", "open.spotify.com",
    "player.vimeo.com",
}
BAD_ARTICLE_PATTERNS = (
    "artsandculture.google.com/story/",
)

def parse_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---(?:\s*\n|\Z)", text, re.S)
    if not match:
        return {}
    data = yaml.safe_load(match.group(1)) or {}
    return data if isinstance(data, dict) else {}

def usable_url(value, field):
    if not isinstance(value, str) or not value.strip():
        return False, "missing"
    value = value.strip()
    parsed = urlparse(value)
    if parsed.scheme != "https" or not parsed.hostname:
        return False, "must be an absolute https URL"
    host = parsed.hostname.lower()
    path = parsed.path.lower()
    if path in GENERIC_PATHS:
        return False, "generic homepage/catalogue path"
    if any(pattern in value.lower() for pattern in BAD_ARTICLE_PATTERNS):
        return False, "editorial story, not a player"
    if field == "recording_embed_url":
        if not any(host == allowed or host.endswith("." + allowed) for allowed in EMBED_HOSTS):
            return False, "embed provider is not allow-listed"
        if host.endswith("youtube.com") and not (path == "/embed/" or path.startswith("/embed/")):
            return False, "YouTube embed URL must use /embed/VIDEO_ID"
        if host == "youtu.be":
            return False, "use a provider embed URL, not a short watch link"
        if host == "w.soundcloud.com" and not path.startswith("/player/"):
            return False, "SoundCloud embed URL must use /player/"
        if host == "player.vimeo.com" and not path.startswith("/video/"):
            return False, "Vimeo embed URL must use /video/"
    return True, ""

def main():
    files = sorted(COLLECTION.glob("*.md"))
    config = yaml.safe_load((ROOT / "_config.yml").read_text(encoding="utf-8")) or {}
    excluded = set(config.get("exclude") or [])
    failures = []
    checked = 0
    for path in files:
        data = parse_frontmatter(path)
        if data.get("type") != "recording":
            continue
        relative = path.relative_to(ROOT).as_posix()
        if relative in excluded:
            continue
        checked += 1
        if data.get("draft") is True:
            failures.append((path.relative_to(ROOT), "draft is still included in the public collection"))
            continue
        valid_url, why_url = usable_url(data.get("recording_url"), "recording_url")
        valid_embed, why_embed = usable_url(data.get("recording_embed_url"), "recording_embed_url")
        if not (valid_url or valid_embed):
            reasons = []
            if not valid_url:
                reasons.append("recording_url: " + why_url)
            if not valid_embed:
                reasons.append("recording_embed_url: " + why_embed)
            failures.append((path.relative_to(ROOT), "; ".join(reasons)))
    print(f"PUBLISHED RECORDINGS CHECKED: {checked}")
    print(f"PUBLISHED LISTENING-LINK FAILURES: {len(failures)}")
    for path, reason in failures:
        print(f"MISSING/INVALID: {path} — {reason}")
    report = ROOT / "missing-recording-links.txt"
    report.write_text(
        "\n".join(f"{path} — {reason}" for path, reason in failures) + ("\n" if failures else ""),
        encoding="utf-8",
    )
    print(f"REPORT WRITTEN: {report.name}")
    print("NOTE: passing this check confirms only a specific-looking HTTPS URL or approved embed format; it does not verify playback.")
    return 1 if failures else 0

if __name__ == "__main__":
    sys.exit(main())
