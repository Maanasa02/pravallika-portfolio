# Pravallika Thirumalasetty — portfolio site

Static site. All copy comes from `PT_Portfolio.pdf` or cannondesign.com / nyp.org; anything unknown is marked `[in brackets]` on the pages themselves.

## Edit & rebuild

Text, project order and metadata live in `build.py` (the `P` list). Images live in `assets/img/<project>/NN.jpg` — `01.jpg` is the cover; the `doc=[...]` list picks which numbers appear on the Documentation page.

```bash
python3 build.py
```

## Preview locally

```bash
python3 -m http.server 8765
```

## Deploy (Netlify)

Site: `pravallika-thirumalasetty` · id `482829cf-953f-415e-b14a-4ca519a4bff6` · https://pravallika-thirumalasetty.netlify.app

Visitor access is currently **team login only** (free plan; real password protection needs Netlify Pro). Change it under Site configuration → Access & security in app.netlify.com.

## Gaps to fill (search the site for `[`)

- Per project: role, phases (SD/DD/CD/CA), what she produced
- Photography credits (Seton Hall, The One)
- MSK credit line (portfolio says CannonDesign AOR; cannondesign.com says with Foster + Partners)
- Building K / Polk / MSK — CannonDesign clearance for unpublished work
- Student project years (Dominos, Circularity, In + Out)
- About: résumé link, footer location
- Phone number deliberately left off the site (it's in the PDF) — add to About if wanted
