#!/usr/bin/env python3
"""Validate every post against the fixed schema. Exit 1 on any error. Run before every commit."""
import re, sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
REC = ["type", "title", "slug", "date", "draft", "who", "when", "where", "what", "tags", "recording_url", "urls", "images"]
COL = ["type", "title", "slug", "date", "draft", "description", "tracks", "images"]
TAGS = {"the-account", "out-of-turn", "made-anyway", "unwanted", "fighting-words", "found"}
errors, slugs, recs = [], {}, {}

def load(f):
    m = re.match(r"---\n(.*?)\n---\n(.*)", f.read_text(encoding="utf-8"), re.S)
    if not m: raise ValueError("no front matter")
    return yaml.safe_load(m.group(1)), m.group(2)

for kind, keys, folder in (("recording", REC, "recordings"), ("collection", COL, "collections")):
    for f in sorted((ROOT / "posts" / folder).glob("*.md")):
        try:
            m, body = load(f)
        except Exception as e:
            errors.append(f"{f}: {e}"); continue
        if list(m) != keys: errors.append(f"{f}: keys must be exactly, in order: {keys}")
        if m.get("type") != kind: errors.append(f"{f}: type must be {kind}")
        if f.stem != m.get("slug"): errors.append(f"{f}: file name must equal slug")
        if m.get("slug") in slugs: errors.append(f"{f}: duplicate slug")
        slugs[m.get("slug")] = f
        if not isinstance(m.get("draft"), bool): errors.append(f"{f}: draft must be true or false")
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", str(m.get("date"))): errors.append(f"{f}: date must be YYYY-MM-DD")
        for k in ("urls", "images", "tags", "tracks"):
            if k in keys and not isinstance(m.get(k), list): errors.append(f"{f}: {k} must be a list")
        if kind == "recording":
            recs[m["slug"]] = m
            bad = set(m.get("tags") or []) - TAGS
            if bad: errors.append(f"{f}: unknown tags {bad}")
            if m.get("draft") is False:
                for k in ("who", "what"):
                    if not m.get(k): errors.append(f"{f}: finished post needs '{k}'")
                if "## To do" in body: errors.append(f"{f}: finished post still has a '## To do' section")
        else:
            m["file"] = f
            recs.setdefault("__cols__", []).append(m)

for c in recs.pop("__cols__", []):
    for t in c["tracks"]:
        if t not in recs: errors.append(f"{c['file']}: track '{t}' has no recording post")
        elif c["draft"] is False and recs[t]["draft"]: errors.append(f"{c['file']}: finished mixtape lists draft track '{t}'")

for e in errors: print(e)
print(f"{len(errors)} error(s); {len(recs)} recordings checked")
sys.exit(1 if errors else 0)
