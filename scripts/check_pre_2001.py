#!/usr/bin/env python3
"""Validate the Spite Frequencies pre-2001 recording catalogue."""
from pathlib import Path
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
RECORDINGS = ROOT / "posts" / "_recordings"
MIXTAPES = ROOT / "posts" / "_mixtapes"
YEAR_RE = re.compile(r"(?<!\d)(1[0-9]{3}|20[0-9]{2})(?!\d)")

def frontmatter(path):
    raw = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*(?:\n|$)", raw, re.S)
    if not match:
        raise ValueError("missing YAML front matter")
    return yaml.safe_load(match.group(1)) or {}

errors = []
by_slug = {}
for path in sorted(RECORDINGS.glob("*.md")):
    try:
        data = frontmatter(path)
    except Exception as exc:
        errors.append(f"{path.relative_to(ROOT)}: {exc}")
        continue
    slug = str(data.get("slug") or path.stem)
    by_slug[slug] = (path, data)
    when = str(data.get("when") or "").strip()
    years = [int(y) for y in YEAR_RE.findall(when)]
    if not years:
        errors.append(f"{path.relative_to(ROOT)}: add a sourced original recording year/range in 'when'")
    elif max(years) > 1999:
        errors.append(f"{path.relative_to(ROOT)}: recording date {when!r} is after the 2000 cutoff")
    active_until = str(data.get("active_until") or "").strip()
    active_years = [int(y) for y in YEAR_RE.findall(active_until)]
    act_status = str(data.get("act_status") or "").strip()
    if act_status not in {"one-off", "anonymous-traditional", "archival-field-recording"}:
        if not active_years:
            errors.append(f"{path.relative_to(ROOT)}: add a sourced final active year in active_until, or a justified one-off act_status")
        elif max(active_years) > 1999:
            errors.append(f"{path.relative_to(ROOT)}: act remained active after 1999 ({active_until!r})")
    if len(str(data.get("why_outsider") or "").strip()) < 20:
        errors.append(f"{path.relative_to(ROOT)}: explain the marginalised, unknown, or outsider relevance in why_outsider")
    if not data.get("urls"):
        errors.append(f"{path.relative_to(ROOT)}: add at least one source URL")
    if data.get("type") != "recording":
        errors.append(f"{path.relative_to(ROOT)}: type must be recording")

for path in sorted(MIXTAPES.glob("*.md")):
    try:
        data = frontmatter(path)
    except Exception as exc:
        errors.append(f"{path.relative_to(ROOT)}: {exc}")
        continue
    if data.get("type") != "collection":
        errors.append(f"{path.relative_to(ROOT)}: type must be collection")
    tracks = data.get("tracks") or []
    if not tracks:
        errors.append(f"{path.relative_to(ROOT)}: add at least one recording slug to tracks")
    for slug in tracks:
        slug = str(slug)
        if slug not in by_slug:
            errors.append(f"{path.relative_to(ROOT)}: track {slug!r} does not resolve to a recording post")
            continue
        rec_path, rec = by_slug[slug]
        when = str(rec.get("when") or "")
        years = [int(y) for y in YEAR_RE.findall(when)]
        active_until = str(rec.get("active_until") or "")
        active_years = [int(y) for y in YEAR_RE.findall(active_until)]
        act_status = str(rec.get("act_status") or "").strip()
        if not years or max(years) > 1999:
            errors.append(f"{path.relative_to(ROOT)}: track {slug!r} is not verified as recorded by 1999")
        if act_status not in {"one-off", "anonymous-traditional", "archival-field-recording"} and (not active_years or max(active_years) > 1999):
            errors.append(f"{path.relative_to(ROOT)}: track {slug!r} is by an act not verified to have ended by 1999")
        if len(str(rec.get("why_outsider") or "").strip()) < 20 or not rec.get("urls"):
            errors.append(f"{path.relative_to(ROOT)}: track {slug!r} lacks outsider rationale or source URLs")

if errors:
    print("PRE-2001 CATALOGUE CHECK FAILED")
    for error in errors:
        print(" - " + error)
    print(f"\n{len(errors)} issue(s). Correct the recording history or remove ineligible tracks.")
    sys.exit(1)
print("Pre-2001 catalogue check passed.")
