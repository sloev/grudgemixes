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
    # Only explicit record-level status fields count. Do not infer readiness from
    # prose such as "no READY FOR DRIVE items" or agent instructions.
    match = re.search(r"(?im)^\\s*(?:\\|\\s*)?(?:\\*\\*)?status(?:\\*\\*)?\\s*[:|]\\s*([^|\\n]+)", raw)
    if not match:
        return "Investigating"
    value = re.sub(r"\\*+", "", match.group(1)).strip().casefold()
    if "reported in drive" in value:
        return "Reported in Drive"
    if "in drive" in value and "listing verified" in value:
        return "In Drive (listed)"
    if "in drive" in value and "verified" in value:
        return "Done"
    if "downloaded" in value and "verified" in value:
        return "Done"
    if "ready for drive" in value or "ready for download" in value:
        return "Ready for Drive"
    if "paid download route" in value or "owner approval" in value:
        return "Owner approval needed"
    if "stream only" in value:
        return "Stream only"
    if "permission needed" in value or "broken link" in value or "identity unresolved" in value:
        return "Blocked / unresolved"
    if value == "researched":
        return "Researched"
    return "Investigating"

def main():
    records, seen = [], set()
    for project, roots in PROJECTS:
        for root in roots:
            folder = ROOT / root
            if not folder.exists(): continue
            for path in folder.rglob("*.md"):
                if path in seen or path.name.casefold() in SKIP or path.name.casefold() == "readme.md": continue
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
              "Ready for Drive":"Exact downloadable object and permitted route identified; awaiting Drive retrieval.",
              "Researched":"Research complete enough for further review; not necessarily downloadable.",
              "Stream only":"A listening route exists; no downloadable file route verified.",
              "Owner approval needed":"A paid route exists but requires owner approval.",
              "Blocked / unresolved":"Access, link, or recording identity remains unresolved.",
              "Investigating":"Research, identity, provenance, or access route still being checked."},
            "records":sorted(unique.values(),key=lambda x:(x["project"],x["status"],x["name"].casefold()))}
    OUT.mkdir(exist_ok=True)
    (OUT/"data.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
if __name__ == "__main__": main()
