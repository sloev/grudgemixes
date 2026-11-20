#!/usr/bin/env python3
"""Build the blog from posts/ into a static site. Only posts with `draft: false` are published.

    pip install markdown pyyaml
    python3 scripts/build.py --out docs [--base https://sloev.github.io/grudgemixes/]
"""
import argparse, hashlib, html, re, shutil
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path
from urllib.parse import quote

import markdown, yaml

ROOT = Path(__file__).resolve().parents[1]
NAME = "Spite Frequencies"
TAGLINE = "Music made where it wasn't wanted, and songs that kept the score."
TAGCOL = {"the-account": "#8a2b1a", "out-of-turn": "#b5651d", "made-anyway": "#2f6b4f", "unwanted": "#5b3f8c",
          "fighting-words": "#1f3f6b", "found": "#6b5a2f"}

def load(f):
    m = re.match(r"---\n(.*?)\n---\n(.*)", f.read_text(encoding="utf-8"), re.S)
    meta = yaml.safe_load(m.group(1)); meta["body"] = m.group(2).strip(); meta["file"] = f
    return meta

def esc(s): return html.escape(str(s or ""))
def md(s): return markdown.markdown(s or "", extensions=["sane_lists"])

def embed(url):
    if not url: return ""
    m = re.search(r"(?:youtube\.com/watch\?v=|youtu\.be/)([\w-]{11})", url)
    if m: return f'<div class="embed"><iframe src="https://www.youtube-nocookie.com/embed/{m.group(1)}" title="Player" loading="lazy" allowfullscreen></iframe></div>'
    m = re.search(r"archive\.org/details/([^/?#]+)", url)
    if m: return f'<div class="embed audio"><iframe src="https://archive.org/embed/{m.group(1)}" title="Player" loading="lazy"></iframe></div>'
    if "soundcloud.com/" in url: return f'<div class="embed audio"><iframe src="https://w.soundcloud.com/player/?url={quote(url, safe="")}" title="Player" loading="lazy"></iframe></div>'
    if re.search(r"\.(mp3|ogg|wav|m4a)(\?|$)", url, re.I): return f'<audio controls preload="none" src="{esc(url)}"></audio>'
    return ""

def host(u): return re.sub(r"^https?://(www\.)?", "", u).split("/")[0]

def image_of(p, rel):
    """First entry of `images` ("path-or-url | credit"), else a generated cover."""
    if p.get("images"):
        src, _, credit = str(p["images"][0]).partition("|")
        src = src.strip()
        if not src.startswith("http"): src = rel + src
        return src, credit.strip()
    return f"{rel}covers/{p['slug']}.svg", ""

def cover_svg(p):
    h = hashlib.sha1(p["slug"].encode()).digest()
    tag = (p.get("tags") or ["mix"])[0]
    col = TAGCOL.get(tag, "#3a3a3a") if p["type"] == "recording" else "#1c1a17"
    hue = h[0] * 360 // 255
    tape = p["type"] == "collection" or tag in ("found", "made-anyway", "unwanted")
    rings = "".join(f'<circle cx="300" cy="300" r="{r}" fill="none" stroke="rgba(255,255,255,.1)" stroke-width="2"/>' for r in range(70, 250, 9 + h[1] % 6))
    motif = ('<rect x="90" y="190" width="420" height="250" rx="22" fill="rgba(0,0,0,.35)" stroke="rgba(255,255,255,.5)" stroke-width="4"/>'
             '<circle cx="215" cy="315" r="44" fill="none" stroke="#fff" stroke-width="8"/><circle cx="385" cy="315" r="44" fill="none" stroke="#fff" stroke-width="8"/>'
             '<rect x="150" y="220" width="300" height="40" fill="rgba(255,255,255,.85)"/>') if tape else \
            f'<circle cx="300" cy="300" r="250" fill="#111"/>{rings}<circle cx="300" cy="300" r="70" fill="{col}"/><circle cx="300" cy="300" r="8" fill="#111"/>'
    a = esc(p.get("when") or ("Mixtape" if p["type"] == "collection" else ""))
    b = esc((p.get("where") or "")[:34])
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">'
            f'<stop offset="0" stop-color="{col}"/><stop offset="1" stop-color="hsl({hue},45%,22%)"/></linearGradient></defs>'
            f'<rect width="600" height="600" fill="url(#g)"/>{motif}<text x="40" y="560" font-family="Georgia,serif" font-size="44" fill="#fff">{a}</text>'
            f'<text x="560" y="560" text-anchor="end" font-family="system-ui,sans-serif" font-size="20" fill="rgba(255,255,255,.85)">{b}</text></svg>')

CSS = """:root{--bg:#f6f2ea;--fg:#1c1a17;--mut:#6b655c;--line:#ddd4c6;--card:#fffdf8;--acc:#8a2b1a}
@media (prefers-color-scheme:dark){:root{--bg:#141210;--fg:#ece5d9;--mut:#a2998b;--line:#36312b;--card:#1d1a17;--acc:#e07a5f}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.6 Georgia,serif}a{color:var(--acc)}
header{border-bottom:1px solid var(--line);padding:1rem}header .b{font:700 1.4rem Georgia,serif;color:var(--fg);text-decoration:none}
header p{margin:.2rem 0 0;color:var(--mut);font:.9rem system-ui,sans-serif}nav{margin-top:.5rem;display:flex;gap:1rem;font:600 .9rem system-ui,sans-serif}
main{max-width:46rem;margin:0 auto;padding:1rem}h2.sec{max-width:72rem;margin:1.5rem auto 0;padding:0 1rem;font-size:1.3rem}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(14rem,1fr));gap:1rem;max-width:72rem;margin:0 auto;padding:1rem}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;overflow:hidden;text-decoration:none;color:var(--fg)}
.card img{width:100%;aspect-ratio:1;object-fit:cover;display:block}.card div{padding:.6rem .8rem .9rem}.card h3{font-size:1.02rem;line-height:1.3;margin:.2rem 0}
.meta{font:.8rem system-ui,sans-serif;color:var(--mut)}.tag{display:inline-block;font:600 .72rem system-ui,sans-serif;padding:.15rem .5rem;border-radius:999px;color:#fff;margin-right:.3rem}
.tools{max-width:72rem;margin:0 auto;padding:1rem 1rem 0}.tools input{width:100%;font:1rem system-ui,sans-serif;padding:.6rem .8rem;border:1px solid var(--line);border-radius:10px;background:var(--card);color:var(--fg)}
article img.cover{width:100%;max-width:28rem;border-radius:12px;display:block;margin:1rem auto}article h1{font-size:1.7rem;line-height:1.2}
dl.facts{display:grid;grid-template-columns:max-content 1fr;gap:.3rem 1rem;font:.92rem system-ui,sans-serif;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:.8rem 1rem}dl.facts dt{color:var(--mut)}dl.facts dd{margin:0}
.embed{position:relative;padding-top:56.25%;margin:1rem 0}.embed iframe{position:absolute;inset:0;width:100%;height:100%;border:0;border-radius:10px}
.embed.audio{padding-top:0;height:140px}.embed.audio iframe{position:static;height:140px}audio{width:100%;margin:1rem 0}
.btn{display:block;padding:.6rem .8rem;margin:.35rem 0;border:1px solid var(--line);border-radius:10px;background:var(--card);text-decoration:none;font:600 .92rem system-ui,sans-serif;overflow-wrap:anywhere}
.list{max-width:52rem;margin:0 auto;padding:.5rem 1rem}
.row{display:flex;gap:1rem;padding:1rem 0;border-bottom:1px solid var(--line)}.row:last-child{border-bottom:0}
.row .thumb{flex:0 0 7.5rem}.row .thumb img{width:7.5rem;height:7.5rem;object-fit:cover;border-radius:10px;display:block;border:1px solid var(--line)}
.row .txt{flex:1;min-width:0}.row h3{font-size:1.15rem;line-height:1.3;margin:0 0 .25rem}.row h3 a{color:var(--fg);text-decoration:none}.row h3 a:hover{text-decoration:underline}
.row p{margin:.4rem 0 .2rem}.num{font:600 .85rem system-ui,sans-serif;color:var(--mut);margin-right:.5rem}
.more{font:600 .85rem system-ui,sans-serif;text-decoration:none}
.rec{display:inline-block;font:600 .75rem system-ui,sans-serif;color:var(--mut);margin-bottom:.15rem}.rec.r-embed{color:#2f6b4f}.rec.r-link{color:var(--acc)}
@media (prefers-color-scheme:dark){.rec.r-embed{color:#7fc79f}}
.pills{display:flex;flex-wrap:wrap;gap:.3rem;margin:.3rem 0}
.pill{font:600 .72rem system-ui,sans-serif;padding:.15rem .55rem;border-radius:999px;border:1px solid var(--c);color:var(--c);text-decoration:none;background:transparent}
@media (prefers-color-scheme:dark){.pill{filter:brightness(1.7)}}
a.pill:hover,a.pill.on{background:var(--c);color:#fff;filter:none}
.filter{max-width:52rem;margin:0 auto;padding:0 1rem;font:.9rem system-ui,sans-serif;color:var(--mut)}.filter button{font:inherit;margin-left:.5rem;cursor:pointer}
@media (max-width:540px){.row .thumb{flex-basis:5rem}.row .thumb img{width:5rem;height:5rem}}
.tools{max-width:52rem}h2.sec{max-width:52rem}
ol.tl li{margin:.4rem 0}.links{font:.88rem system-ui,sans-serif}.links li{overflow-wrap:anywhere}footer{text-align:center;color:var(--mut);font:.8rem system-ui,sans-serif;padding:2rem 1rem}.hidden{display:none!important}"""

def page(title, body, base, rel, desc=""):
    return (f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{esc(title)}</title><meta name="description" content="{esc(desc or TAGLINE)}"><link rel="stylesheet" href="{rel}style.css">'
            f'<link rel="alternate" type="application/rss+xml" title="{NAME}" href="{base}feed.xml"></head><body>'
            f'<header><a class="b" href="{rel}">{NAME}</a><p>{TAGLINE}</p><nav><a href="{rel}">Home</a><a href="{rel}about/">About</a><a href="{base}feed.xml">RSS</a></nav></header>'
            f'{body}<footer>{NAME} · <a href="{base}feed.xml">RSS</a></footer></body></html>')

def period(when):
    """Pill for the time period, derived from `when`."""
    w = str(when or "")
    if re.search(r"tradition", w, re.I): return "traditional"
    m = re.search(r"\b(1[0-9]|20)(\d)\d\b", w)
    if not m: return ""
    y = int(m.group(0))
    return f"{y // 10 * 10}s" if y >= 1900 else f"{y // 100 + 1}th century"

def key(s): return re.sub(r"[^\w]+", "-", str(s).lower()).strip("-")

def rec_status(url):
    """'embed' if the recording plays on the page, 'link' if it is only linked, '' if none."""
    return "embed" if embed(url) else "link" if url else ""

REC_LABEL = {"embed": "▶ Playable here", "link": "↗ Recording link", "": "No recording yet"}

def facets(p, recs=None):
    """(group, value, label, colour) tuples for the pills: medium, period, place, category."""
    if p["type"] == "collection":
        tr = [recs[s] for s in p["tracks"] if s in recs and not recs[s].get("draft")]
        out = [("kind", "mixtape", "mixtape", "#1c1a17"), ("kind", "", f"{len(tr)} tracks", "#6b655c")]
        pers = sorted({period(r.get("when")) for r in tr} - {""}, key=lambda x: (not x[0].isdigit(), x))
        out += [("period", key(x), x, "#6b655c") for x in pers]
        return out
    out = []
    if p.get("medium"): out.append(("medium", key(p["medium"]), p["medium"], "#3c5a6b"))
    if period(p.get("when")): out.append(("period", key(period(p.get("when"))), period(p.get("when")), "#6b655c"))
    if p.get("country"): out.append(("place", key(p["country"]), p["country"], "#4f6b3c"))
    out += [("category", t, t.replace("-", " "), TAGCOL.get(t, "#444")) for t in p.get("tags") or []]
    return out

def pills(fs, link=""):
    """Pills are filter buttons on the home page; on other pages they link to the filtered home page."""
    h = []
    for g, v, label, col in fs:
        if not v: h.append(f'<span class="pill" style="--c:{col}">{esc(label)}</span>'); continue
        h.append(f'<a class="pill" style="--c:{col}" href="{link}#{g}={v}" data-f="{g}={v}">{esc(label)}</a>')
    return f'<div class="pills">{"".join(h)}</div>'

def row(p, rel, recs, n=None):
    col = p["type"] == "collection"
    href = f'{rel}{"mixtapes" if col else "posts"}/{p["slug"]}/'
    thumb = ""
    if p.get("images"):
        src, _ = image_of(p, rel)
        thumb = f'<a class="thumb" href="{href}" tabindex="-1"><img src="{esc(src)}" alt="" loading="lazy"></a>'
    if col:
        tr = [recs[s] for s in p["tracks"] if s in recs and not recs[s].get("draft")]
        k = sum(1 for r in tr if r.get("recording_url"))
        ind = f'<span class="rec {"r-embed" if k else ""}">▶ {k} of {len(tr)} playable</span>'
        summ = p.get("description")
    else:
        st = rec_status(p.get("recording_url"))
        ind = f'<span class="rec r-{st}">{REC_LABEL[st]}</span>'
        summ = p.get("summary")
    fs = facets(p, recs)
    data = " ".join(f"{g}={v}" for g, v, *_ in fs if v) + ("" if col else f' recording={rec_status(p.get("recording_url")) or "none"}')
    num = f'<span class="num">{n}</span>' if n else ""
    return (f'<article class="row{" has-img" if thumb else ""}" data-f="{esc(data)}">{thumb}<div class="txt">'
            f'<h3>{num}<a href="{href}">{esc(p["title"])}</a></h3>{ind}{pills(fs, rel)}'
            f'<p>{esc(summ)}</p><a class="more" href="{href}">Read more →</a></div></article>')

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", default="docs"); ap.add_argument("--base", default="https://sloev.github.io/grudgemixes/")
    a = ap.parse_args(); base = a.base.rstrip("/") + "/"; out = Path(a.out)
    if out.exists(): shutil.rmtree(out)
    (out / "covers").mkdir(parents=True)
    if (ROOT / "media").exists(): shutil.copytree(ROOT / "media", out / "media")
    recs = {p["slug"]: p for p in map(load, sorted((ROOT / "posts/recordings").glob("*.md")))}
    cols = [load(f) for f in sorted((ROOT / "posts/collections").glob("*.md"))]
    live = [p for p in recs.values() if not p.get("draft")]
    live_cols = [c for c in cols if not c.get("draft")]
    live.sort(key=lambda p: (str(p.get("date")), p["title"]), reverse=True)
    (out / "style.css").write_text(CSS, encoding="utf-8")
    for p in live + live_cols:
        (out / "covers" / f"{p['slug']}.svg").write_text(cover_svg(p), encoding="utf-8")

    for p in live:
        d = out / "posts" / p["slug"]; d.mkdir(parents=True)
        src, credit = image_of(p, "../../")
        facts = "".join(f"<dt>{k}</dt><dd>{esc(p.get(k))}</dd>" for k in ("who", "what", "when", "where") if p.get(k))
        rec = p.get("recording_url")
        listen = f'<a class="btn" href="{esc(rec)}" rel="noopener">▶ Listen at {esc(host(rec))}</a>' if rec else '<p class="meta">No public recording link yet.</p>'
        links = "".join(f'<li><a href="{esc(u)}" rel="noopener">{esc(host(u))}</a></li>' for u in p.get("urls") or [])
        inmix = [c for c in live_cols if p["slug"] in c["tracks"]]
        mixes = "".join(f'<li><a href="../../mixtapes/{c["slug"]}/">{esc(c["title"])}</a></li>' for c in inmix)
        tags = pills(facets(p), "../../")
        body = (f'<main><article><h1>{esc(p["title"])}</h1>{tags}<p><em>{esc(p.get("summary"))}</em></p><img class="cover" src="{src}" alt="">'
                f'{f"<p class=meta>Image: {esc(credit)}</p>" if credit else ""}<dl class="facts">{facts}</dl>{embed(rec)}{listen}{md(p["body"])}'
                f'{f"<h3>Links</h3><ul class=links>{links}</ul>" if links else ""}{f"<h3>On the mixtapes</h3><ul>{mixes}</ul>" if mixes else ""}</article></main>')
        (d / "index.html").write_text(page(f"{p['title']} · {NAME}", body, base, "../../", p.get("what") or ""), encoding="utf-8")

    for c in live_cols:
        d = out / "mixtapes" / c["slug"]; d.mkdir(parents=True)
        src, credit = image_of(c, "../../")
        items = "".join(row(recs[s], "../../", recs, i + 1) for i, s in enumerate(x for x in c["tracks"] if not recs[x].get("draft")))
        body = (f'<main><article><span class="meta">Mixtape</span><h1>{esc(c["title"])}</h1><img class="cover" src="{src}" alt=""><p><em>{esc(c.get("description"))}</em></p>'
                f'{md(c["body"])}<h3>Tracklist</h3></article></main><div class="list">{items}</div>')
        (d / "index.html").write_text(page(f"{c['title']} · {NAME}", body, base, "../../", c.get("description")), encoding="utf-8")

    js = """<script>
const q=document.getElementById('q'),rows=[...document.querySelectorAll('#rec .row, #mix .row')],fb=document.getElementById('fb');
function apply(){const f=decodeURIComponent(location.hash.slice(1)),t=q.value.toLowerCase();let n=0;
 rows.forEach(r=>{const ok=(!f||(' '+r.dataset.f+' ').includes(' '+f+' '))&&(!t||r.textContent.toLowerCase().includes(t));r.classList.toggle('hidden',!ok);if(ok)n++});
 document.querySelectorAll('a.pill').forEach(a=>a.classList.toggle('on',f&&a.dataset.f===f));
 fb.innerHTML=f?'Showing '+n+' posts with <b>'+f.replace('=',': ').replace(/-/g,' ')+'</b><button onclick="location.hash=\\'\\'">Clear</button>':'';
 document.querySelectorAll('h2.sec').forEach(h=>{const l=h.nextElementSibling.classList.contains('list')?h.nextElementSibling:h.nextElementSibling.nextElementSibling;h.classList.toggle('hidden',![...l.children].some(c=>!c.classList.contains('hidden')))})}
q.oninput=apply;addEventListener('hashchange',apply);
document.addEventListener('click',e=>{const a=e.target.closest('a.pill');if(a){e.preventDefault();location.hash=location.hash.slice(1)===a.dataset.f?'':a.dataset.f}});apply();
</script>"""
    playable = sum(1 for p in live if rec_status(p.get("recording_url")))
    body = (f'<div class="tools"><input id="q" type="search" placeholder="Search {len(live)} recordings and {len(live_cols)} mixtapes"></div>'
            f'<p class="filter" id="fb"></p>'
            f'<h2 class="sec">Mixtapes</h2><div class="list" id="mix">{"".join(row(c, "", recs) for c in live_cols)}</div>'
            f'<h2 class="sec">Recordings <span class="meta">· {playable} with a recording · <a href="#recording=embed">playable here</a></span></h2>'
            f'<div class="list" id="rec">{"".join(row(p, "", recs) for p in live)}</div>{js}')
    (out / "index.html").write_text(page(NAME, body, base, ""), encoding="utf-8")

    about = (ROOT / "README.md").read_text(encoding="utf-8").split("<!-- about-end -->")[0]
    (out / "about").mkdir(); (out / "about/index.html").write_text(page(f"About · {NAME}", f"<main><article>{md(about)}</article></main>", base, "../"), encoding="utf-8")

    now = max(datetime.strptime(str(p.get("date") or "2026-11-20"), "%Y-%m-%d") for p in live_cols + live).replace(tzinfo=timezone.utc, hour=12); items = []
    for i, p in enumerate(live_cols + live):
        kind = "mixtapes" if p["type"] == "collection" else "posts"
        link = f"{base}{kind}/{p['slug']}/"
        d = datetime.strptime(str(p.get("date") or "2026-11-20"), "%Y-%m-%d").replace(tzinfo=timezone.utc, hour=12, minute=i % 60)
        img = image_of(p, base)[0] if p.get("images") else ""
        desc = (f'<p><img src="{img}" width="300" alt=""/></p>' if img else "") + md(p["body"])
        items.append(f"<item><title>{esc(p['title'])}</title><link>{link}</link><guid isPermaLink=\"true\">{link}</guid><pubDate>{format_datetime(d)}</pubDate>"
                     f"<description><![CDATA[{desc.replace(']]>', ']]&gt;')}]]></description></item>")
    (out / "feed.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel><title>{NAME}</title>'
        f'<link>{base}</link><description>{esc(TAGLINE)}</description><language>en</language><lastBuildDate>{format_datetime(now)}</lastBuildDate>'
        f'<atom:link href="{base}feed.xml" rel="self" type="application/rss+xml"/>{"".join(items)}</channel></rss>', encoding="utf-8")
    (out / ".nojekyll").write_text("")
    print(f"published {len(live)} recordings and {len(live_cols)} mixtapes ({len(recs) - len(live)} recording drafts, {len(cols) - len(live_cols)} mixtape drafts)")

if __name__ == "__main__":
    main()
