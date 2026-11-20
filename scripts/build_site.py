#!/usr/bin/env python3
"""Build the encrypted follow-along site.

Renders LEADS.md, MIXES.md and every other Markdown file in the repository into
one JSON payload, gzips it, encrypts it with AES-256-GCM using a key derived
from SITE_PASSWORD (PBKDF2-SHA256, 600,000 iterations), and writes a single
self-contained index.html that decrypts in the browser.

Usage:  SITE_PASSWORD=... python3 scripts/build_site.py --out site
Needs:  pip install markdown cryptography
The password is never written to disk.
"""
import argparse, base64, gzip, json, os, re, sys
from datetime import datetime, timezone
from pathlib import Path

import markdown
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

ROOT = Path(__file__).resolve().parents[1]
ITER = 600_000
SKIP_DIRS = {".git", ".github", "site", "node_modules"}


def render(text):
    return markdown.markdown(text, extensions=["tables", "fenced_code", "sane_lists"], output_format="html5")


def title_of(text, fallback):
    m = re.search(r"(?m)^#\s+(.+)$", text)
    return (m.group(1).strip() if m else fallback)[:160]


def group_of(rel):
    parts = rel.split("/")
    if parts[0] == "projects" and len(parts) > 2:
        proj = {"grudge-mixes": "Grudge Mixes", "insane-music": "Insane Music"}.get(parts[1], parts[1])
        sub = parts[2] if len(parts) > 3 else "project files"
        return f"{proj} · {sub}"
    if parts[0] == "archive":
        return "Archive · " + (parts[1] if len(parts) > 2 else "")
    return "Workspace"


def collect():
    docs = []
    for p in sorted(ROOT.rglob("*.md")):
        rel = p.relative_to(ROOT).as_posix()
        if any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts):
            continue
        if rel in ("LEADS.md", "MIXES.md"):
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        docs.append({"path": rel, "title": title_of(text, rel), "group": group_of(rel), "html": render(text)})
    return docs


def lead_stats(leads_md):
    entries = len(re.findall(r"(?m)^#### ", leads_md))
    dl = leads_md.count("**Downloaded:** **Yes")
    return {"entries": entries, "downloaded": dl}


def encrypt(payload: bytes, password: str):
    salt, iv = os.urandom(16), os.urandom(12)
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=ITER)
    key = kdf.derive(password.encode("utf-8"))
    ct = AESGCM(key).encrypt(iv, payload, None)
    b = lambda x: base64.b64encode(x).decode()
    return {"salt": b(salt), "iv": b(iv), "iter": ITER, "ct": b(ct)}


PAGE = r"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex,nofollow">
<title>Grudge Mixes · Music in Spite</title>
<style>
:root{--bg:#f7f4ee;--fg:#1d1b18;--mut:#6b655c;--line:#ddd5c8;--acc:#8a2b1a;--card:#fffdf9}
@media (prefers-color-scheme:dark){:root{--bg:#161412;--fg:#ece6dc;--mut:#a39a8c;--line:#3a352f;--acc:#e0785f;--card:#1f1c19}}
*{box-sizing:border-box}html,body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.55 Georgia,"Iowan Old Style",serif}
a{color:var(--acc)}header{position:sticky;top:0;z-index:5;background:var(--bg);border-bottom:1px solid var(--line);padding:.6rem 1rem env(safe-area-inset-top)}
.brand{font:600 .8rem/1 system-ui,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:var(--mut)}
nav{display:flex;gap:.4rem;margin-top:.5rem;overflow-x:auto}
nav button{font:600 .9rem system-ui,sans-serif;border:1px solid var(--line);background:var(--card);color:var(--fg);border-radius:999px;padding:.45rem .9rem;white-space:nowrap;cursor:pointer}
nav button[aria-current=true]{background:var(--fg);color:var(--bg);border-color:var(--fg)}
main{max-width:52rem;margin:0 auto;padding:1rem 1rem 4rem}
.doc h1{font-size:1.6rem;line-height:1.2}.doc h2{margin-top:2rem;border-bottom:1px solid var(--line);padding-bottom:.2rem}
.doc h4{margin:0 0 .4rem;font-size:1.02rem}
.doc table{display:block;overflow-x:auto;border-collapse:collapse;font:.88rem/1.4 system-ui,sans-serif;max-width:100%}
.doc th,.doc td{border:1px solid var(--line);padding:.35rem .5rem;vertical-align:top}.doc th{background:var(--card)}
.doc code{font-size:.85em;word-break:break-all}.doc pre{overflow-x:auto;background:var(--card);padding:.6rem;border:1px solid var(--line)}
.doc ul{padding-left:1.2rem}.doc li{margin:.15rem 0;overflow-wrap:anywhere}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:.8rem 1rem;margin:.7rem 0}
.tools{display:flex;gap:.5rem;flex-wrap:wrap;margin:.5rem 0 1rem}
input[type=search],input[type=password]{font:1rem system-ui,sans-serif;padding:.55rem .7rem;border:1px solid var(--line);border-radius:8px;background:var(--card);color:var(--fg);flex:1;min-width:12rem}
.chip{font:600 .78rem system-ui,sans-serif;border:1px solid var(--line);border-radius:999px;padding:.3rem .65rem;background:var(--card);color:var(--fg);cursor:pointer}
.chip.on{background:var(--acc);border-color:var(--acc);color:#fff}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(9rem,1fr));gap:.5rem;font-family:system-ui,sans-serif}
.stats div{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:.6rem .8rem}.stats b{display:block;font-size:1.5rem}
.list a{display:block;padding:.55rem .2rem;border-bottom:1px solid var(--line);text-decoration:none;color:var(--fg)}
.list small{display:block;color:var(--mut);font-family:system-ui,sans-serif}.grp{font:700 .8rem system-ui,sans-serif;color:var(--mut);text-transform:uppercase;letter-spacing:.06em;margin:1.2rem 0 .2rem}
#lock{max-width:24rem;margin:18vh auto 0;padding:1rem;text-align:center}#lock form{display:flex;gap:.5rem;margin-top:1rem}
#lock button,.btn{font:600 1rem system-ui,sans-serif;padding:.55rem 1rem;border-radius:8px;border:0;background:var(--acc);color:#fff;cursor:pointer}
.err{color:var(--acc);font-family:system-ui,sans-serif;min-height:1.4em}.mut{color:var(--mut);font-family:system-ui,sans-serif;font-size:.85rem}
.hidden{display:none!important}
</style></head><body>
<div id="lock"><div class="brand">Grudge Mixes · Music in Spite</div><h1>Follow-along</h1>
<p class="mut">This page is encrypted. Enter the password to read it.</p>
<form id="f"><input id="pw" type="password" autocomplete="current-password" placeholder="Password" required><button>Open</button></form>
<p id="e" class="err"></p></div>
<div id="app" class="hidden"><header><div class="brand">Grudge Mixes · Music in Spite · updated <span id="built"></span></div>
<nav><button data-v="status">Lead status</button><button data-v="mixes">Mix curations</button><button data-v="research">All research</button></nav></header>
<main id="view"></main></div>
<script id="payload" type="application/json">__PAYLOAD__</script>
<script>
const P=JSON.parse(document.getElementById('payload').textContent);let D=null;
const b64=s=>Uint8Array.from(atob(s),c=>c.charCodeAt(0));
async function unlock(pw){const k0=await crypto.subtle.importKey('raw',new TextEncoder().encode(pw),'PBKDF2',false,['deriveKey']);
const k=await crypto.subtle.deriveKey({name:'PBKDF2',salt:b64(P.salt),iterations:P.iter,hash:'SHA-256'},k0,{name:'AES-GCM',length:256},false,['decrypt']);
const gz=await crypto.subtle.decrypt({name:'AES-GCM',iv:b64(P.iv)},k,b64(P.ct));
const txt=await new Response(new Blob([gz]).stream().pipeThrough(new DecompressionStream('gzip'))).text();return JSON.parse(txt)}
async function tryOpen(pw,quiet){const e=document.getElementById('e');if(!quiet)e.textContent='Opening…';
try{D=await unlock(pw);try{sessionStorage.setItem('gm_pw',pw)}catch(_){}document.getElementById('lock').classList.add('hidden');document.getElementById('app').classList.remove('hidden');
document.getElementById('built').textContent=D.built;route()}catch(err){if(!quiet)e.textContent='Wrong password.'}}
document.getElementById('f').onsubmit=ev=>{ev.preventDefault();tryOpen(document.getElementById('pw').value)};
try{const s=sessionStorage.getItem('gm_pw');if(s)tryOpen(s,true)}catch(_){}
document.querySelectorAll('nav button').forEach(b=>b.onclick=()=>{location.hash=b.dataset.v});
window.onhashchange=route;
function esc(s){return s.replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]))}
function route(){if(!D)return;const h=decodeURIComponent(location.hash.slice(1))||'status';const v=h.split(':')[0];
document.querySelectorAll('nav button').forEach(b=>b.setAttribute('aria-current',b.dataset.v===v));
const m=document.getElementById('view');window.scrollTo(0,0);
if(v==='mixes'){m.innerHTML='<div class="doc">'+D.mixes+'</div>';return}
if(v==='research'){const path=h.slice(9);if(path){const d=D.research.find(x=>x.path===path);
m.innerHTML='<p><a href="#research">← All research</a> <span class="mut">'+esc(path)+'</span></p><div class="doc">'+(d?d.html:'Not found')+'</div>';return}
m.innerHTML='<div class="tools"><input type="search" id="q" placeholder="Search titles and paths"></div><div id="rl" class="list"></div>';
const draw=q=>{let g='',out='';D.research.filter(d=>!q||(d.title+' '+d.path).toLowerCase().includes(q)).forEach(d=>{if(d.group!==g){g=d.group;out+='<div class="grp">'+esc(g)+'</div>'}
out+='<a href="#research:'+encodeURIComponent(d.path)+'">'+esc(d.title)+'<small>'+esc(d.path)+'</small></a>'});document.getElementById('rl').innerHTML=out||'<p class="mut">No match.</p>'};
draw('');document.getElementById('q').oninput=e=>draw(e.target.value.toLowerCase());return}
m.innerHTML='<div class="stats"><div><b>'+D.stats.entries+'</b>entries</div><div><b>'+D.stats.downloaded+'</b>with a downloaded file</div><div><b>'+D.research.length+'</b>research files</div></div>'+
'<div class="tools"><input type="search" id="q" placeholder="Filter leads (name, place, ID, status)"><button class="chip" data-f="dl">Downloaded</button><button class="chip" data-f="gm">Grudge Mixes</button><button class="chip" data-f="im">Insane Music</button></div><div id="sl" class="doc">'+D.status+'</div>';
const root=document.getElementById('sl');const cards=[];let cur=null;
[...root.children].forEach(el=>{if(el.tagName==='H4'){cur=document.createElement('div');cur.className='card';el.before(cur);cur.appendChild(el);cards.push(cur)}
else if(el.tagName==='H2'||el.tagName==='H3'||el.tagName==='HR'){cur=null}else if(cur){cur.appendChild(el)}});
const st={dl:false,gm:false,im:false};
const apply=()=>{const q=document.getElementById('q').value.toLowerCase();cards.forEach(c=>{const t=c.textContent.toLowerCase();
let ok=(!q||t.includes(q))&&(!st.dl||t.includes('downloaded: yes'))&&(!st.gm||t.includes('project: grudge mixes')||t.includes('project: both'))&&(!st.im||t.includes('project: insane music')||t.includes('project: both'));
c.classList.toggle('hidden',!ok)})};
document.getElementById('q').oninput=apply;document.querySelectorAll('.chip').forEach(b=>b.onclick=()=>{st[b.dataset.f]=!st[b.dataset.f];b.classList.toggle('on');apply()})}
</script></body></html>
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="site")
    a = ap.parse_args()
    pw = os.environ.get("SITE_PASSWORD")
    if not pw:
        sys.exit("SITE_PASSWORD is not set")
    leads = (ROOT / "LEADS.md").read_text(encoding="utf-8")
    mixes = (ROOT / "MIXES.md").read_text(encoding="utf-8")
    data = {
        "built": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "status": render(leads),
        "mixes": render(mixes),
        "stats": lead_stats(leads),
        "research": collect(),
    }
    blob = gzip.compress(json.dumps(data, ensure_ascii=False).encode("utf-8"), 9)
    enc = encrypt(blob, pw)
    out = ROOT / a.out if not os.path.isabs(a.out) else Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(PAGE.replace("__PAYLOAD__", json.dumps(enc)), encoding="utf-8")
    (out / ".nojekyll").write_text("")
    (out / "robots.txt").write_text("User-agent: *\nDisallow: /\n")
    print(f"wrote {out/'index.html'}: {len(data['research'])} research files, {data['stats']}, {len(blob)//1024} KiB compressed")


if __name__ == "__main__":
    main()
