#!/usr/bin/env python3
"""Generate a privacy-minimal public lead status feed; never copy source URLs or notes."""
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
        "coop.log.md","research_method.md","track_mapping.md","archive-requests.md"}

def status(text):
    t = text.casefold()
    if any(s in t for s in ["in drive — verified","in drive - verified","downloaded — verified","downloaded - verified","status: done","status: complete"]):
        return "Done"
    if any(s in t for s in ["ready for drive","ready to download","status: researched","research complete"]):
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
                name = re.sub(r"^#+\\s*|\\s*#+$", "", heading.strip())[:140]
                if name.casefold() in {"research","leads","catalogue","films","cues"}: continue
                records.append({"name":name,"project":project,"status":status(raw),
                                "updated":datetime.fromtimestamp(path.stat().st_mtime,timezone.utc).date().isoformat(),
                                "kind":"Research record"})
    unique = {(x["project"],x["name"].casefold()):x for x in records}
    data = {"generated_at":datetime.now(timezone.utc).isoformat(timespec="minutes"),
            "projects":[x[0] for x in PROJECTS],
            "status_definitions":{"Done":"Track downloaded and independently verified.",
              "Researched":"Research complete enough; ready for a download-capable agent.",
              "Investigating":"Research, identity, or access route still being checked."},
            "records":sorted(unique.values(),key=lambda x:(x["project"],x["status"],x["name"].casefold()))}
    OUT.mkdir(exist_ok=True)
    (OUT/"data.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\\n",encoding="utf-8")
if __name__ == "__main__": main()
