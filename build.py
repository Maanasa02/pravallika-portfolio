#!/usr/bin/env python3
"""Static site generator for Pravallika's portfolio.
Run: python3 build.py   ->  writes index.html, about.html, documentation.html, work/*.html
All copy comes from PT_Portfolio.pdf or cannondesign.com / nyp.org; gaps are marked [like this].
"""
import os, html
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
IMG = "assets/img"

NAME_L1, NAME_L2 = "PRAVALLIKA", "Thirumalasetty"
EMAIL = "pravallika309@gmail.com"
IG = "tpravallika"
LINKEDIN = "https://www.linkedin.com/in/tpravallika/"

# ---------------------------------------------------------------- projects
# Each image list is ordered; the first is the cover. `doc` marks drawing sheets
# that also appear on the Documentation page.
P = [
 dict(slug="seton-hall", num="01", title="SHU Practice Basketball Facility",
      caption="SHU Practice Basketball Facility - South Orange, NJ",
      meta=[("Client","Seton Hall University"),("Firm","CannonDesign"),("Sector","Higher Education, Facility"),
            ("Location","South Orange, New Jersey"),("Size","97,381 SF"),("Construction Cost","$46.3M"),
            ("Completed","September 25th 2025"),("Award","AIA NJ – Honor Award 2025")],
      text=["Expansion and Renovation of Seton Hall University’s Basketball Training Facility for Men and Women.",
            "A three-story addition to Seton Hall’s existing athletic facility, with a basketball court, strength and conditioning area, film room, coaches’ offices, players lounge, dining space, steam and sauna. The building references basketball athleticism through a cantilevered section “inspired by the way basketball players seemingly float above the rim.” — cannondesign.com"],
      role="[Role · Phases (SD / DD / CD / CA) · What I produced]",
      credit="Shared work through team effort. [Photography credit]",
      doc=[13,14,15]),
 dict(slug="msk-pavilion", num="02", title="MSK Pavilion",
      caption="MSK Pavilion - Manhattan, NY",
      meta=[("Client","Memorial Sloan Kettering"),("Project","Pavilion Tower"),("Firm","CannonDesign (AOR)"),("Sector","Healthcare"),
            ("Location","Manhattan, New York"),("Size","823,000 SF"),("Est. Completion","2028–2029")],
      text=["Recovery, Surgery & IR, ICU and Med/Surg experience plans.",
            "The Kenneth C. Griffin Pavilion: a 27-story inpatient pavilion adding 208 beds, designed with Foster + Partners. CannonDesign’s scope includes architecture, experience strategy and design, interior design, sustainability and functional/space programming. Four design guideposts: Sense of Belonging · Progress is Sacred · Environment Contributes to Healing · Future-Facing and Flexible. — cannondesign.com"],
      role="[Role · Phases · What I produced]",
      credit="[Confirm credit line: portfolio lists CannonDesign as AOR; cannondesign.com lists the project as a collaboration with Foster + Partners]",
      doc=[9,10,11,12]),
 dict(slug="polk-learning-commons", num="03", title="Polk Learning Commons",
      caption="Polk Learning Commons - Oshkosh, WI",
      meta=[("Client","University of Wisconsin, Oshkosh"),("Firm","CannonDesign (AOD)"),("Sector","Higher Education"),
            ("Location","Oshkosh, Wisconsin"),("Size","154,190 SF"),("Est. Completion","2028–2029")],
      text=["Section – The Avenue · Study Pod – Acoustic Panelling, Demountable Front, Glazing · Cafe Millwork Detail · Cafe Island – Plan, Exterior · Elevation – Cafe Island + Tile Wall.",
            "A “build back smaller” transformation of the 1960s-era Polk Library: a Campus Porch to the north and an Academic Avenue of “light‑filled, double‑height spaces that make learning visible and accessible.” Services: Architecture, Interior Design, Lighting Design, Sustainability. — cannondesign.com"],
      role="[Role · Phases · What I produced]",
      credit="Shared work through team effort.",
      doc=[8,9,11,12,13]),
 dict(slug="dominos", num="04", title="Dominos",
      caption="Dominos - Pratt Institute, Brooklyn, NY",
      meta=[("Type","Student Work"),("School","Pratt Institute"),("Location","Brooklyn, New York"),("Year","[Year]")],
      text=["Dominos is a cat condo proposed to be made on Pratt Institute’s lawn for Pratt cats that live on the campus. This is a sculptural piece that can be inhabited by both cats and people. The structures are angled to replicate dominos pieces in motion. There are benches made on either sides of these structures for people to occupy while the cats get to engage with the voids made through the tilting structures."],
      role=None, credit=None, doc=[2,3]),
 dict(slug="building-k", num="05", title="Building K",
      caption="Building K - Nassau Community College, NY",
      meta=[("Client","Nassau Community College"),("Program","Culinary Arts Department"),("Firm","CannonDesign"),("Sector","Higher Education"),
            ("Location","Nassau, New York"),("Est. Completion","2028–2029")],
      text=["Entrance Lobby · Classroom · Finish palette: exposed bricks, wood LVT, porcelain floor tile, rubber flooring, solid surface, built-in wood bench, gradient glass, quartz, carpet tile, blackened steel base, ceramic wall tiles, acoustic baffle ceiling, plastic laminate, resinous poured floor, wallcovering."],
      role="[Role · Phases · What I produced]",
      credit="[Unpublished project — confirm CannonDesign clearance before going live]",
      doc=[6,7,8,9]),
 dict(slug="circularity", num="06", title="Circularity",
      caption="Circularity - Domino Sugar Factory, Brooklyn, NY",
      meta=[("Type","Student Work · MFA Thesis Project"),("School","Pratt Institute"),("Site","Domino Sugar Factory"),
            ("Location","Brooklyn, New York"),("Size","132,000 SF"),("Recognition","Featured in Pratt Institute Sustainability Center"),("Year","[Year]")],
      text=["“Circularity” activates a cyclic economy to deploy water and waste production systems to re-imagine the role of housing, as a tool, to foster opportunity. Creating an intrinsic network of resource production, sharing, accumulation, and waste, the Domino Sugar Refinery in Williamsburg transforms into a community generator by re-imagining the food production cycle.",
            "Tackling housing inequity through resources + opportunities. Introduction of a circular economy can provide an opportunity to provide sustainable practices with minimal to no waste produced while simultaneously providing employment and sharing of resources."],
      role=None, credit=None, doc=[7,13,14,15,16]),
 dict(slug="the-one", num="07", title="The One",
      caption="NewYork-Presbyterian The One - Westchester, NY",
      meta=[("Client","New York Presbyterian"),("Firm","CannonDesign"),("Sector","Healthcare"),("Location","Westchester, New York"),
            ("Size","~285,000 SF"),("Completed","1st September 2025")],
      text=["Lobby Entrance · Lobby Check In · Lobby Reception Desk.",
            "A center for advanced care at 1111 Westchester Avenue, White Plains: 155 exam and consult rooms, ambulatory surgery and endoscopy suites, advanced radiology and an infusion center, spanning more than 90 specialties. — nyp.org"],
      role="[Role · Phases · What I produced]",
      credit="[Photography credit]",
      doc=[4,5]),
 dict(slug="in-out", num="08", title="In + Out",
      caption="In + Out - Park Avenue, New York, NY",
      meta=[("Type","Student Work"),("School","Pratt Institute"),("Client","the Agency"),("Location","Park Avenue, New York"),("Floors","21 · 22"),("Year","[Year]")],
      text=["In + Out is a workspace for “the Agency” exploring the concept of exterior vs interior and influenced by their clients for the material palette. The exploration of biophilia along with luxurious materials come into play in this space as it tries to connect the outside to the inside for the “new normal” of COVID‑19.",
            "the Agency is a collaborative creative design consultancy firm that mostly focuses on indian fashion and lifestyle branding. Their clients include Masaba, Anushree Reddy, Manish Malhotra, Shivan & Narresh, and Sabyasachi."],
      role=None, credit=None, doc=[4,7]),
]

# ---------------------------------------------------------------- helpers
def esc(s): return html.escape(s, quote=False)

def images(slug):
    d = os.path.join(ROOT, IMG, slug)
    out = []
    for f in sorted(os.listdir(d)):
        if not f.endswith(".jpg"): continue
        w, h = Image.open(os.path.join(d, f)).size
        out.append((f"{IMG}/{slug}/{f}", w, h))
    return out

def span(w, h):
    r = w / h
    if r >= 2.2: return "s3"
    if r >= 1.15: return "s2"
    return "s1"

def head(title, depth=0):
    b = "../" * depth
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{b}assets/css/site.css">
</head>
<body>
<header class="hd">
  <a class="logo" href="{b}index.html">{NAME_L1}<br>{NAME_L2}</a>
  <nav class="nav">
    <a href="{b}index.html">Projects</a>
    <a href="{b}documentation.html">Documentation</a>
    <a href="{b}about.html">About/Contact</a>
  </nav>
  <div class="soc">
    <a href="{LINKEDIN}" target="_blank" rel="noopener" aria-label="LinkedIn">in</a>
    <a href="https://www.instagram.com/{IG}" target="_blank" rel="noopener" aria-label="Instagram">ig</a>
    <a href="mailto:{EMAIL}" aria-label="Email">@</a>
  </div>
</header>
<main class="main">
"""

FOOT = """</main>
<footer class="ft"><span>© 2026 Pravallika Thirumalasetty</span><span>[Location, e.g. Brooklyn, NY]</span></footer>
<div class="lb" id="lb" hidden><img alt=""><button aria-label="Close">×</button></div>
<script>
(function(){var lb=document.getElementById('lb'),im=lb.querySelector('img');
document.querySelectorAll('.g a.z').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();im.src=a.href;lb.hidden=false;document.body.style.overflow='hidden';});});
function close(){lb.hidden=true;im.src='';document.body.style.overflow='';}
lb.addEventListener('click',close);document.addEventListener('keydown',function(e){if(e.key==='Escape')close();});})();
</script>
</body>
</html>
"""

def write(path, s):
    p = os.path.join(ROOT, path); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w").write(s)

# ---------------------------------------------------------------- pages
# Home: 3-up grid of covers, caption "Title - Location" like the reference.
cards = []
for p in P:
    cov = images(p["slug"])[0][0]
    cards.append(f'<a class="card" href="work/{p["slug"]}.html"><span class="ph"><img src="{cov}" alt="{esc(p["title"])}" loading="lazy"></span><span class="cap">{esc(p["caption"])}</span></a>')
write("index.html", head("Pravallika Thirumalasetty — Interior Design") + '<section class="grid">' + "\n".join(cards) + "</section>\n" + FOOT)

# Project pages
for i, p in enumerate(P):
    imgs = images(p["slug"])
    nxt = P[(i + 1) % len(P)]
    meta = "".join(f"<div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>" for k, v in p["meta"])
    text = "".join(f"<p>{esc(t)}</p>" for t in p["text"])
    role = f'<p class="gap">{esc(p["role"])}</p>' if p["role"] else ""
    credit = f'<p class="credit">{esc(p["credit"])}</p>' if p["credit"] else ""
    tiles = "".join(f'<a class="z {span(w,h)}" href="../{src}"><img src="../{src}" alt="{esc(p["title"])} — {n+1:02d}" loading="{"eager" if n==0 else "lazy"}"></a>'
                    for n, (src, w, h) in enumerate(imgs))
    body = f"""<article class="proj">
  <div class="ph-title"><span class="num">{p["num"]}</span><h1>{esc(p["title"])}</h1></div>
  <div class="info">
    <dl class="meta">{meta}</dl>
    <div class="txt">{text}{role}{credit}</div>
  </div>
  <div class="g">{tiles}</div>
  <a class="next" href="{nxt["slug"]}.html">Next — {nxt["num"]} {esc(nxt["title"])} →</a>
</article>
"""
    write(f"work/{p['slug']}.html", head(f"{p['title']} — Pravallika Thirumalasetty", 1) + body + FOOT)

# Documentation: drawing sheets only, grouped by project.
secs = []
for p in P:
    imgs = images(p["slug"])
    tiles = "".join(f'<a class="z {span(w,h)}" href="{src}"><img src="{src}" alt="{esc(p["title"])} — drawing" loading="lazy"></a>'
                    for n, (src, w, h) in enumerate(imgs) if (n + 1) in p["doc"])
    secs.append(f'<section class="docsec"><h2><a href="work/{p["slug"]}.html">{p["num"]} {esc(p["title"])}</a></h2><div class="g">{tiles}</div></section>')
write("documentation.html", head("Documentation — Pravallika Thirumalasetty") + '<div class="proj"><div class="ph-title"><h1>Documentation</h1></div><p class="lede">Plans, sections, elevations, millwork and partition details.</p>' + "".join(secs) + "</div>\n" + FOOT)

# About / Contact
about = f"""<article class="proj about">
  <div class="ph-title"><h1>About/Contact</h1></div>
  <div class="info">
    <div class="txt">
      <img class="sig" src="{IMG}/about/01.jpg" alt="Pravallika Thirumalasetty">
      <p>Interior Designer, CannonDesign — New York. [Confirm title and start date]</p>
      <p>MFA Interior Design, Pratt Institute. [Confirm degree title and graduation year]</p>
      <p>[Undergraduate degree, institution, year]</p>
      <p>[NCIDQ / WELL / LEED status]</p>
      <p>[Software: Revit, Enscape, SketchUp, Adobe Suite — confirm list]</p>
      <p>[Short bio — 2 to 3 sentences]</p>
    </div>
    <dl class="meta">
      <div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
      <div><dt>LinkedIn</dt><dd><a href="{LINKEDIN}" target="_blank" rel="noopener">linkedin.com/in/tpravallika</a></dd></div>
      <div><dt>Instagram</dt><dd><a href="https://www.instagram.com/{IG}" target="_blank" rel="noopener">@{IG}</a></dd></div>
      <div><dt>Résumé</dt><dd>[Link to PDF]</dd></div>
    </dl>
  </div>
</article>
"""
write("about.html", head("About/Contact — Pravallika Thirumalasetty") + about + FOOT)

# ---------------------------------------------------------------- css
css = """
:root{--ink:#2a2952;--txt:#706c87;--bg:#fff;--line:#e9e8ee;--gap:2px}
*{box-sizing:border-box}
html,body{margin:0;background:var(--bg);color:var(--txt);font:14px/1.55 "Libre Franklin","Helvetica Neue",Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased}
a{color:var(--ink);text-decoration:none}
img{display:block;max-width:100%}
.hd{display:flex;align-items:flex-start;gap:28px;padding:22px 24px 8px;flex-wrap:wrap}
.logo{font-weight:700;font-size:30px;line-height:1.08;letter-spacing:-.01em;color:var(--ink);margin-right:8px}
.nav{display:flex;gap:26px;padding-top:7px;font-size:13px}
.nav a:hover{text-decoration:underline}
.soc{margin-left:auto;display:flex;gap:16px;padding-top:7px;font-size:12px;letter-spacing:.04em;text-transform:uppercase}
.main{padding:64px 60px 40px;max-width:1440px;margin:0 auto}
/* home grid */
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px var(--gap)}
.card .ph{display:block;aspect-ratio:4/3;overflow:hidden;background:#f2f1f5}
.card img{width:100%;height:100%;object-fit:cover;transition:transform .5s ease}
.card:hover img{transform:scale(1.03)}
.card .cap{display:block;text-align:center;font-size:11px;padding:8px 6px 0;color:var(--txt)}
/* project */
.ph-title{display:flex;align-items:baseline;gap:14px;margin:0 0 26px}
.ph-title .num{font-size:12px;letter-spacing:.14em;color:var(--txt)}
.ph-title h1{font-size:22px;font-weight:700;color:var(--ink);margin:0;letter-spacing:-.01em}
.info{display:grid;grid-template-columns:280px 1fr;gap:40px;margin-bottom:38px;max-width:1100px}
.meta{margin:0;font-size:12px}
.meta div{display:grid;grid-template-columns:110px 1fr;gap:10px;padding:5px 0;border-top:1px solid var(--line)}
.meta div:last-child{border-bottom:1px solid var(--line)}
.meta dt{margin:0;color:var(--txt)}.meta dd{margin:0;color:var(--ink)}
.txt p{margin:0 0 12px;max-width:62ch}
.gap,.credit,[class=gap]{color:#b04a4a}
.credit{font-size:12px;font-style:italic;color:#9a97ad}
.lede{margin:-10px 0 30px;max-width:62ch}
.g{display:grid;grid-template-columns:repeat(6,1fr);grid-auto-flow:dense;gap:var(--gap)}
.g a{display:block;overflow:hidden;background:#f6f6f8}
.g a.s1{grid-column:span 2}.g a.s2{grid-column:span 3}.g a.s3{grid-column:span 6}
.g img{width:100%;height:100%;object-fit:contain;aspect-ratio:4/3}
.g a.s3 img{aspect-ratio:auto}
.next{display:block;margin:48px 0 0;font-size:13px}
.docsec{margin:0 0 44px}.docsec h2{font-size:13px;font-weight:500;letter-spacing:.06em;text-transform:uppercase;margin:0 0 10px}
.about .info{grid-template-columns:1fr 320px}
.sig{width:280px;margin:-10px 0 22px}
.ft{display:flex;justify-content:space-between;padding:18px 24px 26px;font-size:11px;color:#9a97ad}
.lb[hidden]{display:none}
.lb{position:fixed;inset:0;background:rgba(255,255,255,.96);display:flex;align-items:center;justify-content:center;z-index:9;cursor:zoom-out}
.lb img{max-width:96vw;max-height:94vh;object-fit:contain}
.lb button{position:absolute;top:14px;right:18px;font-size:30px;border:0;background:none;color:var(--ink);cursor:pointer}
@media (max-width:900px){.main{padding:36px 16px 30px}.grid{grid-template-columns:repeat(2,1fr)}.info{grid-template-columns:1fr;gap:20px}.about .info{grid-template-columns:1fr}
 .g{grid-template-columns:repeat(2,1fr)}.g a.s1,.g a.s2{grid-column:span 1}.g a.s3{grid-column:span 2}.logo{font-size:24px}.nav{gap:16px}.soc{width:100%;margin-left:0;padding-top:0}}
@media (max-width:560px){.grid{grid-template-columns:1fr}}
"""
write("assets/css/site.css", css)
print("built:", len(P), "projects")
