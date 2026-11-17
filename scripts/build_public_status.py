#!/usr/bin/env python3
"""Generate a privacy-minimal status feed; never copy source URLs, filenames or notes."""
import json, re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "public"
PROJECTS = [
    ("Grudge Mixes", ["candidates", "research", "leads", "projects/grudgemixes"]),
    ("Insane Music", ["projects/insanemusic"]),
    ("Soviet Film Music", ["projects/sovietfilm"]),
]
SKIP = {"readme.md","methodology.md","method.md","workflow.md","agents.md",
        "coop.log.md","research_method.md","track_mapping.md","archive-requests.md",
        "workspace_redirect.md"}

def status(raw):
    t = raw.casefold()
    if "reported in drive" in t:
        return "Reported in Drive"
    if any(s in t for s in ["in drive — listing verified","in drive - listing verified"]):
        return "In Drive (listed)"
    if any(s in t for s in ["in drive — verified","in drive - verified","downloaded — verified","downloaded - verified"]):
        return "Done"
    if any(s in t for s in ["ready for drive","ready to download","ready for download","status: researched"]):
        return "Researched"
    return "Investigating"

def main():
    records, seen = [], set()
    for project, roots in PROJECTS:
        for root in roots:
            folder = ROOT / root
            if not folder.exists(): continue
            for path in folder.rglob("*.md"):
                if path in seen or path.name.casefold() in SKIP: continue
                if any(x in path.name.casefold() for x in ["log","queue","request","method"]): continue
                seen.add(path)
                raw = path.read_text(encoding="utf-8", errors="replace")
                heading = next((x for x in raw.splitlines() if x.lstrip().startswith("#")), path.stem)
                name = re.sub(r"^#+\s*|\s*#+$", "", heading.strip())[:140]
                if name.casefold() in {"research","leads","catalogue","films","cues"}: continue
                kind = "Drive audio inventory" if "drive-audio-inventory" in path.parts else "Research record"
                records.append({"name":name,"project":project,"status":status(raw),
                                "updated":datetime.fromtimestamp(path.stat().st_mtime,timezone.utc).date().isoformat(),
                                "kind":kind})
    unique = {(x["project"],x["name"].casefold()):x for x in records}
    data = {"generated_at":datetime.now(timezone.utc).isoformat(timespec="minutes"),
            "projects":[x[0] for x in PROJECTS],
            "status_definitions":{
              "Done":"Downloaded audio independently verified.",
              "In Drive (listed)":"A Drive inventory lists the file; this does not establish playback or isolated-track status.",
              "Reported in Drive":"Legacy project notes report a file in Drive; current Drive listing has not been independently checked.",
              "Researched":"Research or a lawful retrieval route is ready for a download-capable agent.",
              "Investigating":"Research, identity, provenance, or access route still being checked."},
            "records":sorted(unique.values(),key=lambda x:(x["project"],x["status"],x["name"].casefold()))}
    OUT.mkdir(exist_ok=True)
    (OUT/"data.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
if __name__ == "__main__": main()
