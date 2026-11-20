#!/usr/bin/env python3
"""Build the public blog "Spite Frequencies" into a static site.

Posts come from two places:
  1. blog/posts/*.md           hand-written posts (front matter + Markdown). These win.
  2. LEADS.md                  every other publishable lead becomes an auto-generated post.

Nothing else from the private repository is published. Leads that need consent or touch
private people (see SKIP_* below) are never turned into posts.

Usage:  python3 scripts/build_blog.py --out site [--base https://sloev.github.io/grudgemusic-public/]
Needs:  pip install markdown
"""
import argparse, hashlib, html, re, shutil
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
from pathlib import Path
from urllib.parse import quote

import markdown

ROOT = Path(__file__).resolve().parents[1]
NAME = "Spite Frequencies"
TAGLINE = "Music made where it wasn't wanted, and songs that kept the score."
STRANDS = ["The Account", "Out of Turn", "Made Anyway", "Unwanted", "Fighting Words", "Found"]
COLORS = {"The Account": "#8a2b1a", "Out of Turn": "#b5651d", "Made Anyway": "#2f6b4f",
          "Unwanted": "#5b3f8c", "Fighting Words": "#1f3f6b", "Found": "#6b5a2f"}

# Leads are not published if their text matches these (consent, privacy, minors, sacred material).
SKIP_ALWAYS = re.compile(r"consent|privacy|private speech|\bminor\b|children's voices|sacred|do not prioritise|indigenous", re.I)
# Confinement material is published only when the makers themselves released it.
SKIP_CONFINED = re.compile(r"psychiatric|patient|hospital|prison|inmate|detainee|\bcamp\b|asylum|sanatori", re.I)
SELF_RELEASED = re.compile(r"bandcamp\.com", re.I)
SKIP_IDS = {"IM-022", "IM-031", "IM-020", "IM-034", "IM-013", "IM-023", "IM-026", "IM-035", "IM-036", "IM-029"}
DROP_KEYS = {"project", "research status", "status", "planned mix", "downloaded", "dossier", "rights", "rights / consent",
             "consent", "visibility", "evidence note", "conflict", "privacy", "next", "to do"}

def slugify(s):
    s = re.sub(r"[^\w\s-]", "", s.lower(), flags=re.U)
    s = re.sub(r"[\s_]+", "-", s).strip("-")
    return s[:70] or "post"

# ---------------------------------------------------------------- hand-written posts
def read_handwritten():
    posts = []
    for f in sorted((ROOT / "blog/posts").glob("*.md")):
        text = f.read_text(encoding="utf-8")
        m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
        if not m:
            continue
        meta = {"listen": [], "source": []}
        for line in m.group(1).splitlines():
            k, _, v = line.partition(":")
            k, v = k.strip(), v.strip()
            if k in ("listen", "source"):
                meta[k].append(v)
            else:
                meta[k] = v
        meta["body"] = m.group(2).strip()
        meta["hand"] = True
        posts.append(meta)
    return posts

# ---------------------------------------------------------------- auto posts from LEADS.md
def strand_for(section, block):
    if section.startswith("C3"): return "Unwanted"
    if section.startswith("C4"): return "Fighting Words"
    if section.startswith("C5"): return "Found"
    if re.search(r"Project:\*\*\s*(Grudge Mixes|Both)", block): return "The Account"
    if re.search(r"found|thrift|cassette", block, re.I) and section.startswith(("C", "D")): return "Found"
    return "Made Anyway"

def parse_leads():
    text = (ROOT / "LEADS.md").read_text(encoding="utf-8")
    posts, section = [], ""
    blocks = re.split(r"(?m)^(?=#{2,4} )", text)
    for b in blocks:
        head = b.splitlines()[0] if b.strip() else ""
        if head.startswith("## ") or head.startswith("### "):
            section = re.sub(r"^#+\s*", "", head)
            continue
        if not head.startswith("#### ") or section.startswith("E."):
            continue
        title_raw = head[5:].strip()
        if title_raw.lower().startswith("context"):
            continue
        body_lines = b.splitlines()[1:]
        block = "\n".join(body_lines)
        if SKIP_ALWAYS.search(block) or SKIP_ALWAYS.search(title_raw):
            continue
        if SKIP_CONFINED.search(block + title_raw) and not SELF_RELEASED.search(block):
            continue
        # fields
        fields, extra = {}, []
        for line in body_lines:
            mm = re.match(r"\s*-\s*\*\*([^*]+?):\*\*\s*(.*)", line)
            if mm:
                for part in re.split(r"\s·\s(?=\*\*)", mm.group(1) + ":** " + mm.group(2)):
                    pm = re.match(r"\**([^*]+?):\*\*\s*(.*)", part.strip())
                    if pm:
                        fields[pm.group(1).strip().lower()] = pm.group(2).strip()
            elif line.strip() and not line.strip().startswith("- http") and not re.match(r"\s+- https?://", line):
                extra.append(line.strip())
        urls = []
        for u in re.findall(r"https?://[^\s)|`>\]]+", block):
            u = u.rstrip(".,;")
            if u not in urls:
                urls.append(u)
        # title / id / year / place
        idm = re.match(r"((?:GM|IM)-[A-Z]*-?\d+[a-z]?)\s*[—-]*\s*(.*)", title_raw)
        lead_id, title = (idm.group(1), idm.group(2)) if idm else ("", title_raw)
        title = re.sub(r"\s*—\s*NEW 2026-11-20", "", title).strip()
        title = re.sub(r"^(Note|Note·\w+)\s*—\s*", "", title)
        title = re.sub(r"^(Candidate research|Candidate recording|Candidate lead|Research lead|Candidate|Lead)\s*[:—]\s*", "", title, flags=re.I).strip()
        if lead_id in SKIP_IDS:
            continue
        if not re.search(r"\w", title):
            continue
        place = ""
        pm = re.match(r"([^·]{2,40}) · (.*)", title)
        if pm:
            place, title = pm.group(1).strip(), pm.group(2).strip()
        ym = re.findall(r"\b(1[89]\d\d|20[0-2]\d)\b", title_raw)
        year = ym[0] if ym else ""
        if not place:
            sm = re.search(r"Environment & place:\s*([^;]+)", block)
            if sm: place = sm.group(1).strip()[:60]
        # body
        parts = []
        for key in ("recording", "background", "setting", "story", "why it fits", "what it is", "notes", "context"):
            if key in fields and fields[key]:
                label = {"why it fits": "Why it's here", "setting": "Where and when"}.get(key, key.capitalize())
                parts.append(f"**{label}:** {fields[key]}")
        for k, v in fields.items():
            if k in DROP_KEYS or k.startswith("sources") or k.startswith("listen") or k in ("recording", "background", "setting", "story", "why it fits", "what it is", "notes", "context"):
                continue
            if v and not v.startswith("http"):
                parts.append(f"**{k.capitalize()}:** {v}")
        body = "\n\n".join(parts)
        if len(body) < 60:
            continue
        body = re.sub(r"Environment & place:\s*", "", body)
        body = re.sub(r";?\s*Pathway[^;\n]*", "", body)
        body = re.sub(r"⚠[^.;]*[.;]?", "", body)            # internal rights flags out
        body = re.sub(r"`[^`]*\.md`", "", body)             # internal file paths out
        body = re.sub(r"\(?§\s?[\w.]+\)?", "", body)
        posts.append({"title": title, "slug": slugify((lead_id + "-" if lead_id else "") + title),
                      "place": place, "year": year, "strand": strand_for(section, block), "id": lead_id,
                      "body": body, "urls": urls, "hand": False})
    return posts

# ---------------------------------------------------------------- embeds and links
def embed_html(spec):
    if not spec: return ""
    kind, _, val = spec.partition(":")
    if kind == "youtube":
        return f'<div class="embed"><iframe src="https://www.youtube-nocookie.com/embed/{html.escape(val)}" title="Player" loading="lazy" allowfullscreen></iframe></div>'
    if kind == "archive":
        return f'<div class="embed audio"><iframe src="https://archive.org/embed/{html.escape(val)}" title="Player" loading="lazy"></iframe></div>'
    if kind == "soundcloud":
        return f'<div class="embed audio"><iframe src="https://w.soundcloud.com/player/?url={quote(val, safe="")}" title="Player" loading="lazy"></iframe></div>'
    if kind == "audio":
        return f'<audio controls preload="none" src="{html.escape(val)}"></audio>'
    return ""

def auto_embed(urls):
    for u in urls:
        m = re.search(r"(?:youtube\.com/watch\?v=|youtu\.be/)([\w-]{11})", u)
        if m: return "youtube:" + m.group(1)
    for u in urls:
        m = re.search(r"archive\.org/details/([^/?#]+)", u)
        if m and m.group(1) not in ("cassettetapes", "lofinest", "noise-arch"): return "archive:" + m.group(1)
    for u in urls:
        if "soundcloud.com/" in u and "/sets/" not in u and u.count("/") >= 4: return "soundcloud:" + u
    return ""

LISTEN_HOSTS = re.compile(r"demo-tapes|tapestash|bodegapop|youtu|bandcamp|soundcloud|archive\.org|loc\.gov/item/jukebox|mediafire|\.mp3|ubu\.|phonobase|frontera|lautarchiv|songpoemmusic|deezer|spotify|apple\.com", re.I)

def host(u):
    return re.sub(r"^https?://(www\.)?", "", u).split("/")[0]

# ---------------------------------------------------------------- covers
def cover_svg(p):
    h = hashlib.sha1(p["slug"].encode()).digest()
    col = COLORS.get(p["strand"], "#444")
    hue = h[0] * 360 // 255
    year = html.escape(p.get("year") or "")
    place = html.escape((p.get("place") or "")[:34])
    rings = "".join(f'<circle cx="300" cy="300" r="{r}" fill="none" stroke="rgba(255,255,255,.10)" stroke-width="2"/>' for r in range(70, 250, 9 + h[1] % 6))
    tape = p["strand"] in ("Found", "Made Anyway", "Unwanted")
    motif = (f'<rect x="90" y="190" width="420" height="250" rx="22" fill="rgba(0,0,0,.35)" stroke="rgba(255,255,255,.5)" stroke-width="4"/>'
             f'<circle cx="215" cy="315" r="44" fill="none" stroke="#fff" stroke-width="8"/><circle cx="385" cy="315" r="44" fill="none" stroke="#fff" stroke-width="8"/>'
             f'<rect x="150" y="220" width="300" height="40" fill="rgba(255,255,255,.85)"/>') if tape else \
            (f'<circle cx="300" cy="300" r="250" fill="#111"/>{rings}<circle cx="300" cy="300" r="70" fill="{col}"/><circle cx="300" cy="300" r="8" fill="#111"/>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" role="img" aria-label="Cover">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{col}"/><stop offset="1" stop-color="hsl({hue},45%,22%)"/></linearGradient></defs>
<rect width="600" height="600" fill="url(#g)"/>{motif}
<text x="40" y="560" font-family="Georgia,serif" font-size="44" fill="#fff">{year}</text>
<text x="560" y="560" text-anchor="end" font-family="system-ui,sans-serif" font-size="20" fill="rgba(255,255,255,.85)">{place}</text>
</svg>'''

# ---------------------------------------------------------------- page templates
CSS = """:root{--bg:#f6f2ea;--fg:#1c1a17;--mut:#6b655c;--line:#ddd4c6;--card:#fffdf8;--acc:#8a2b1a}
@media (prefers-color-scheme:dark){:root{--bg:#141210;--fg:#ece5d9;--mut:#a2998b;--line:#36312b;--card:#1d1a17;--acc:#e07a5f}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.6 Georgia,"Iowan Old Style",serif}
a{color:var(--acc)}header.site{border-bottom:1px solid var(--line);padding:1rem}
header.site a.brand{font:700 1.4rem/1.1 Georgia,serif;color:var(--fg);text-decoration:none}
header.site p{margin:.2rem 0 0;color:var(--mut);font:.9rem system-ui,sans-serif}
header.site nav{margin-top:.5rem;font:600 .9rem system-ui,sans-serif;display:flex;gap:1rem}
main{max-width:46rem;margin:0 auto;padding:1rem}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(14rem,1fr));gap:1rem;max-width:72rem;margin:0 auto;padding:1rem}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;overflow:hidden;text-decoration:none;color:var(--fg);display:flex;flex-direction:column}
.card img{width:100%;aspect-ratio:1;display:block}.card div{padding:.6rem .8rem .9rem}
.card h2{font-size:1.02rem;line-height:1.3;margin:.2rem 0}.meta{font:.78rem system-ui,sans-serif;color:var(--mut)}
.tag{display:inline-block;font:600 .72rem system-ui,sans-serif;padding:.15rem .5rem;border-radius:999px;color:#fff}
.tools{max-width:72rem;margin:0 auto;padding:1rem 1rem 0;display:flex;flex-wrap:wrap;gap:.4rem}
.tools input{flex:1 1 100%;font:1rem system-ui,sans-serif;padding:.6rem .8rem;border:1px solid var(--line);border-radius:10px;background:var(--card);color:var(--fg)}
.chip{font:600 .8rem system-ui,sans-serif;border:1px solid var(--line);background:var(--card);color:var(--fg);border-radius:999px;padding:.35rem .7rem;cursor:pointer}
.chip.on{background:var(--fg);color:var(--bg)}
article img.cover{width:100%;max-width:28rem;border-radius:12px;display:block;margin:1rem auto}
article h1{font-size:1.7rem;line-height:1.2;margin:.6rem 0}
.embed{position:relative;padding-top:56.25%;margin:1rem 0}.embed iframe{position:absolute;inset:0;width:100%;height:100%;border:0;border-radius:10px}
.embed.audio{padding-top:0;height:140px}.embed.audio iframe{position:static;height:140px}
audio{width:100%;margin:1rem 0}
.listen a{display:block;padding:.6rem .8rem;margin:.35rem 0;border:1px solid var(--line);border-radius:10px;background:var(--card);text-decoration:none;font:600 .92rem system-ui,sans-serif;overflow-wrap:anywhere}
.sources{font:.85rem system-ui,sans-serif;color:var(--mut)}.sources li{overflow-wrap:anywhere}
.pn{display:flex;justify-content:space-between;gap:1rem;margin:2rem 0;font:.9rem system-ui,sans-serif}
footer{text-align:center;color:var(--mut);font:.8rem system-ui,sans-serif;padding:2rem 1rem}
.hidden{display:none!important}"""

def page(title, body, base, rel, desc=""):
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc or TAGLINE)}">
<link rel="stylesheet" href="{rel}style.css"><link rel="alternate" type="application/rss+xml" title="{NAME}" href="{base}feed.xml">
</head><body><header class="site"><a class="brand" href="{rel}">{NAME}</a><p>{TAGLINE}</p>
<nav><a href="{rel}">All posts</a><a href="{rel}about/">About</a><a href="{base}feed.xml">RSS</a></nav></header>
{body}<footer>{NAME} · notes from the Grudge Mixes and Music in Spite research · <a href="{base}feed.xml">RSS</a></footer></body></html>"""

def excerpt(md_text, n=220):
    t = re.sub(r"<[^>]+>", "", markdown.markdown(md_text))
    t = re.sub(r"\s+", " ", t).strip()
    return t[:n].rsplit(" ", 1)[0] + "…" if len(t) > n else t

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="site")
    ap.add_argument("--base", default="https://sloev.github.io/grudgemusic-public/")
    a = ap.parse_args()
    base = a.base.rstrip("/") + "/"
    out = Path(a.out)
    if out.exists(): shutil.rmtree(out)
    (out / "covers").mkdir(parents=True)

    hand = read_handwritten()
    auto = parse_leads()
    keys = []
    for p in hand:
        keys += [w.lower() for w in re.findall(r"[A-Za-zÀ-žĀ-ž]{5,}", p["title"] + " " + p.get("place", ""))][:0]
    # de-duplicate: an auto post is dropped if a hand post shares its distinctive name
    hand_text = " ".join((p["title"] + " " + p["body"]).lower() for p in hand)
    DUP = ["zaghl", "russolo", "plaatje", "gm-gl-001", "gauhar", "pelo telefone", "hagen", "bézazian", "bezazian", "bentley ball",
           "heraclio", "montéhus", "propeller", "pērkons", "nsrd", "garūta", "velly", "ir visa tai", "echidna", "bone record", "ribs",
           "rimitti", "haló", "skengdo", "most unwanted", "opus no. 1", "vexations", "msr 851", "cencerrada", "malinda", "wesseh",
           "gania", "yoshimatsu", "turnstyle", "ata kak", "nassem", "grime-encrusted"]
    seen, posts = set(), []
    for p in hand:
        seen.add(p["slug"]); posts.append(p)
    for p in auto:
        t = (p["id"] + " " + p["title"]).lower()
        if any(k in t for k in DUP) or p["slug"] in seen:
            continue
        seen.add(p["slug"]); posts.append(p)

    now = datetime(2026, 11, 20, 18, 0, tzinfo=timezone.utc)
    for i, p in enumerate(posts):
        p["date"] = now - timedelta(minutes=i)
        if not p.get("hand"):
            p["embed"] = auto_embed(p["urls"])
            p["listen"] = [f"{host(u)}|{u}" for u in p["urls"] if LISTEN_HOSTS.search(u)][:6]
            p["source"] = [f"{host(u)}|{u}" for u in p["urls"] if not LISTEN_HOSTS.search(u)][:8]
        (out / "covers" / f"{p['slug']}.svg").write_text(cover_svg(p), encoding="utf-8")

    (out / "style.css").write_text(CSS, encoding="utf-8")

    # posts
    for i, p in enumerate(posts):
        d = out / "posts" / p["slug"]; d.mkdir(parents=True)
        tag = f'<span class="tag" style="background:{COLORS.get(p["strand"], "#444")}">{html.escape(p["strand"])}</span>'
        meta = " · ".join(x for x in [html.escape(p.get("place", "")), html.escape(p.get("year", ""))] if x)
        listen = "".join(f'<a href="{html.escape(u.split("|",1)[-1])}" rel="noopener">▶ {html.escape(u.split("|",1)[0])}</a>' for u in p.get("listen", []))
        srcs = "".join(f'<li><a href="{html.escape(u.split("|",1)[-1])}" rel="noopener">{html.escape(u.split("|",1)[0])}</a></li>' for u in p.get("source", []))
        prev = posts[i - 1] if i > 0 else None
        nxt = posts[i + 1] if i + 1 < len(posts) else None
        pn = '<div class="pn">' + (f'<a href="../{prev["slug"]}/">← {html.escape(prev["title"][:50])}</a>' if prev else "<span></span>") + \
             (f'<a href="../{nxt["slug"]}/">{html.escape(nxt["title"][:50])} →</a>' if nxt else "") + "</div>"
        body = f"""<main><article>{tag} <span class="meta">{meta}</span>
<h1>{html.escape(p['title'])}</h1>
<img class="cover" src="../../covers/{p['slug']}.svg" alt="">
{embed_html(p.get('embed'))}
{markdown.markdown(p['body'], extensions=['sane_lists'])}
{('<h3>Listen</h3><div class="listen">' + listen + '</div>') if listen else '<p class="meta">No public recording link yet. If you know of one, tell us.</p>'}
{('<h3>Sources</h3><ul class="sources">' + srcs + '</ul>') if srcs else ''}
<p class="meta">Posted {p['date'].strftime('%d %B %Y')}</p>{pn}</article></main>"""
        (d / "index.html").write_text(page(f"{p['title']} · {NAME}", body, base, "../../", excerpt(p["body"], 160)), encoding="utf-8")

    # index
    chips = '<button class="chip on" data-s="">All</button>' + "".join(f'<button class="chip" data-s="{s}">{s}</button>' for s in STRANDS)
    cards = "".join(f"""<a class="card" href="posts/{p['slug']}/" data-s="{p['strand']}"><img src="covers/{p['slug']}.svg" alt="" loading="lazy"><div>
<span class="tag" style="background:{COLORS.get(p['strand'],'#444')}">{html.escape(p['strand'])}</span>
<h2>{html.escape(p['title'])}</h2><div class="meta">{html.escape(' · '.join(x for x in [p.get('place',''), p.get('year','')] if x))}</div></div></a>""" for p in posts)
    js = """<script>const q=document.getElementById('q');let s='';function f(){const t=q.value.toLowerCase();document.querySelectorAll('.card').forEach(c=>{c.classList.toggle('hidden',!((!s||c.dataset.s===s)&&c.textContent.toLowerCase().includes(t)))})}
q.oninput=f;document.querySelectorAll('.chip').forEach(b=>b.onclick=()=>{document.querySelectorAll('.chip').forEach(x=>x.classList.remove('on'));b.classList.add('on');s=b.dataset.s;f()})</script>"""
    body = f'<div class="tools"><input id="q" type="search" placeholder="Search {len(posts)} posts: a place, a year, a name">{chips}</div><div class="grid">{cards}</div>{js}'
    (out / "index.html").write_text(page(NAME, body, base, ""), encoding="utf-8")

    # about
    about_md = (ROOT / "blog/about.md").read_text(encoding="utf-8")
    (out / "about").mkdir()
    (out / "about/index.html").write_text(page(f"About · {NAME}", f"<main><article>{markdown.markdown(about_md)}</article></main>", base, "../"), encoding="utf-8")

    # RSS
    items = []
    for p in posts:
        link = f"{base}posts/{p['slug']}/"
        desc = f'<p><img src="{base}covers/{p["slug"]}.svg" alt="" width="300"/></p>' + markdown.markdown(p["body"])
        items.append(f"""<item><title>{html.escape(p['title'])}</title><link>{link}</link><guid isPermaLink="true">{link}</guid>
<pubDate>{format_datetime(p['date'])}</pubDate><category>{html.escape(p['strand'])}</category>
<description><![CDATA[{desc.replace(']]>', ']]&gt;')}]]></description></item>""")
    rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel>
<title>{NAME}</title><link>{base}</link><description>{html.escape(TAGLINE)}</description><language>en</language>
<lastBuildDate>{format_datetime(now)}</lastBuildDate><atom:link href="{base}feed.xml" rel="self" type="application/rss+xml"/>
{''.join(items)}
</channel></rss>"""
    (out / "feed.xml").write_text(rss, encoding="utf-8")
    (out / ".nojekyll").write_text("")
    (out / "README.md").write_text(f"# {NAME}\n\n{TAGLINE}\n\nRead it at {base}\n\nThis repository is generated. Do not edit by hand.\n", encoding="utf-8")
    print(f"built {len(posts)} posts ({len(hand)} hand-written, {len(posts)-len(hand)} from leads) into {out}")

if __name__ == "__main__":
    main()
