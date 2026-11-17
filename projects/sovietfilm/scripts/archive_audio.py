#!/usr/bin/env python3
"""Download individually approved audio URLs into Artist/Album folders.

Requires Python 3.10+ and yt-dlp on PATH. Every item must explicitly set
permission_confirmed=true. No DRM, login, paywall, or access-control bypass.
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse


def safe_name(value: str) -> str:
    value = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", str(value)).strip(" .")
    return value or "Unknown"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", nargs="?", default="audio-manifest.json")
    parser.add_argument("--output", default="audio")
    args = parser.parse_args()

    if not shutil.which("yt-dlp"):
        print("ERROR: yt-dlp is not installed or not on PATH", file=sys.stderr)
        return 2

    data = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    items = data.get("items", [])
    root = Path(args.output)
    report = []
    failures = 0

    for item in items:
        title = item.get("title") or "Untitled"
        url = item.get("url", "")
        if item.get("permission_confirmed") is not True:
            report.append({"title": title, "status": "SKIPPED", "reason": "permission_confirmed is not true"})
            continue
        parsed = urlparse(url)
        if parsed.scheme != "https" or not parsed.netloc:
            failures += 1
            report.append({"title": title, "status": "FAILED", "reason": "URL must be a valid HTTPS URL"})
            continue

        artist = safe_name(item.get("artist", "Unknown Artist"))
        album = safe_name(item.get("album", "Unsorted"))
        track = int(item.get("track_number", 0))
        track_title = safe_name(title)
        filename = f"{track:02d} - {track_title}.%(ext)s" if track > 0 else f"{track_title}.%(ext)s"
        folder = root / artist / album
        folder.mkdir(parents=True, exist_ok=True)

        cmd = [
            "yt-dlp", "--format", "bestaudio/b",
            "--output", str(folder / filename),
            "--no-overwrites", "--continue",
            "--retries", "3", "--fragment-retries", "3",
            "--embed-metadata", "--no-write-playlist-metafiles",
            "--no-progress", "--print", "after_move:filepath", url,
        ]
        try:
            result = subprocess.run(cmd, check=True, text=True, capture_output=True)
            landed = [line for line in result.stdout.splitlines() if line.strip()]
            report.append({"title": title, "status": "DOWNLOADED", "files": landed})
        except subprocess.CalledProcessError as exc:
            failures += 1
            report.append({
                "title": title, "status": "FAILED",
                "reason": (exc.stderr or str(exc)).strip()[-1500:],
            })
            print(f"FAILED: {artist}/{album}/{title}", file=sys.stderr)

    root.mkdir(parents=True, exist_ok=True)
    report_path = root / "download-report.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"items": len(items), "failed": failures, "report": str(report_path)}, ensure_ascii=False))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
