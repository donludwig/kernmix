#!/usr/bin/env python3
"""Komponentenbeschreibung ohne Abhängigkeiten: storybook/index.html (läuft per file://; Aufbau wie ein Storybook, sichtbar heißt die Seite Komponentenbeschreibung).

Drei Gruppen:
- KERN-Standard: die offiziellen KERN-Stories, statisches Markup aus ../kern-fluid-type/stories (KERN 2.5.0);
  jede Klasse wird gegen das eingebettete Kit (vendor/kern, 2.8.2) geprüft, fehlende werden an der Story markiert.
- Erweiterungen: die Kit-Bausteine (km-) aus tools/bausteine.py, dieselbe Quelle wie die Doku.
- Proposals: je Datei in proposals/*.html eine Story; erste Zeile <!-- titel: … | status: … | datum: … | bezug: … -->.
Themes: „KERN (Original)“ plus jede Datei in dist/themes/. Modus dunkel, hell oder System; Breiten 360, 768, 1280, voll.
Aufruf: python3 tools/build-storybook.py (vorher tools/build.py)."""
import html, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from bausteine import BAUSTEINE, ABSTAENDE, ABSTAND_REGELN, ABSTAND_BILD, intro_html, i as ikon  # noqa: E402

import os
KERN_STORIES = Path(os.environ.get('KERN_STORIES', ROOT / 'vendor/kern-stories'))  # offizielle KERN-Stories (*.stories.js), optional; ohne sie entfällt die Gruppe KERN-Standard
VERSION = (ROOT / 'VERSION').read_text().strip()
KERN = (ROOT / 'vendor/kern/VERSION').read_text().strip()
kern_css = (ROOT / 'vendor/kern/kern.min.css').read_text(encoding='utf-8')
kd_css = (ROOT / 'dist/km.css').read_text(encoding='utf-8')
KLASSEN = set(re.findall(r'\.(-?[A-Za-z_][\w-]*)', kern_css + kd_css))


def lesbar(n):
    return re.sub(r'(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])', ' ', n).strip()


def fehlend(markup):
    cls = set()
    for c in re.findall(r'class="([^"]+)"', markup):
        cls.update(x for x in c.split() if x.startswith(('kern-', 'km-')))
    return sorted(c for c in cls if c not in KLASSEN)


stories = []
# KERN-Standard
for f in sorted(KERN_STORIES.rglob('*.stories.js')):
    t = f.read_text(encoding='utf-8')
    m = re.search(r"title:\s*['\"]([^'\"]+)", t)
    titel = m.group(1) if m else f.stem
    if titel.startswith('All Stories'):
        continue
    for s in re.finditer(r'export const (\w+)\s*=\s*\(\s*\)\s*=>\s*`(.*?)`\s*;', t, flags=re.S):
        markup = s.group(2).strip()
        if '${' in markup:
            continue  # Vorlagen mit Variablen lassen sich nicht statisch zeigen
        stories.append({'gruppe': 'KERN-Standard', 'pfad': titel, 'name': lesbar(s.group(1)), 'html': markup, 'fehlt': fehlend(markup),
                        'quelle': f'kern-fluid-type/stories/{f.relative_to(KERN_STORIES)}'})
# Einleitung gliedern: erster Satz als Vorspann, Rest als Absatz, Klassennamen aus den Klammern als eigene Zeile
def gliedern(roh):
    klassen = list(dict.fromkeys(re.findall(r'<code>((?:km|kern)-[^<]+)</code>', roh or '')))
    prosa = re.sub(r'\s*\((?:[^()]|\([^()]*\))*?<code>(?:[^()]|\([^()]*\))*?\)', '', roh or '')
    prosa = re.sub(r'<(?!/?code\b)[^>]+>', '', prosa).replace(' ,', ',').replace(' .', '.').strip()
    m = re.search(r'(?<![zZ]\.)(?<!\b[a-zA-Z]\.)(?<=[.!?])\s+(?=[A-ZÄÖÜ„])', prosa)
    vor, rest = (prosa[:m.start()], prosa[m.end():]) if m else (prosa, '')
    # Rest als Punktliste, ein Satz je Punkt; „Kennung: …“ vorn fett
    saetze = [s.strip() for s in re.split(r'(?<![zZ]\.)(?<!\b[a-zA-Z]\.)(?<=[.!?])\s+(?=[A-ZÄÖÜ„])', rest) if s.strip()]
    def punkt(s):
        k = re.match(r'^([A-ZÄÖÜ][\wäöüß\- ]{1,24}):\s+(.*)$', s)
        return f'<li><strong>{k.group(1)}</strong> {k.group(2)}</li>' if k else f'<li>{s}</li>'
    rest = ('<ul class="sb-punkte">' + ''.join(punkt(s) for s in saetze) + '</ul>') if len(saetze) > 1 or (saetze and ':' in saetze[0][:26]) else (f'<p>{saetze[0]}</p>' if saetze else '')
    return prosa, '', klassen  # ein Einleitungsabsatz in großer Schrift statt Vorspann plus Liste
# Erweiterungen (Kit-Bausteine)
for _ord, (anker, titel, zweck, markup) in enumerate(BAUSTEINE):
    stories.append({'ordnung': _ord, 'anker': anker, 'gruppe': 'Erweiterungen', 'pfad': 'Werkzeug-Bausteine (km-)', 'name': titel, 'html': markup, 'fehlt': fehlend(markup),
                    'zweck': re.sub(r'<[^>]+>', '', zweck), 'zweck_roh': zweck, 'quelle': 'tools/bausteine.py', 'gliederung': gliedern(zweck),
                    'punkte': [x for x in re.split(r'(?<![zZ]\.)(?<!\b[a-zA-Z]\.)(?<!bzw\.)(?<!ggf\.)(?<!vgl\.)(?<!usw\.)(?<!etc\.)(?<!Nr\.)(?<!ca\.)(?<=[.!?])\s+(?=[A-ZÄÖÜ„<])', zweck) if x.strip()]})  # „In dieser Story“: ein Satz je Punkt
# Grafik „Wer ruft wen auf“: echte Zeichenfunktion aus dem Dashboard-Generator, Beispieldaten statt echter Skills
try:
    import importlib.util
    _spec = importlib.util.spec_from_file_location('build_skills', os.environ.get('KM_SKILLS_TOOL', ''))
    _bs = importlib.util.module_from_spec(_spec); _argv = sys.argv; sys.argv = ['build-skills']; _spec.loader.exec_module(_bs); sys.argv = _argv
    _bs.kanten = lambda s: [('angebot-schreiben', 'kopiertext', False), ('kopiertext', 'stop-slop-de', False), ('protokoll', 'kopiertext', False),
                            ('prototyp-version', 'sichtpruefung', False), ('prototyp-version', 'changelog-pflegen', False), ('changelog-pflegen', 'sichtpruefung', False),
                            ('hochladen', 'sichtpruefung', True), ('projekt-anlegen', 'paket-check', False), ('design-system-bauen', 'sichtpruefung', False)]
    for s in stories:
        if s['name'] == 'Grafik „Wer ruft wen auf“':
            s['html'] = _bs.grafik([]) + _bs.SG_CSS_JS; s['quelle'] = 'project-dashboard: build-skills.py (grafik, Beispieldaten)'
except Exception as e:
    print('Grafik-Story: Dashboard-Generator nicht geladen, Legende bleibt:', e)
# Proposals
for f in sorted((ROOT / 'proposals').glob('*.html')):
    t = f.read_text(encoding='utf-8')
    kopf = dict(re.findall(r'(\w+):\s*([^|>]+?)\s*(?=\||-->)', t.split('\n', 1)[0]))
    if kopf.get('status', '').lower() == 'übernommen': continue  # im Kit aufgegangen: Datei bleibt als Historie, Story nur unter den Bausteinen
    stories.append({'gruppe': 'Proposals', 'pfad': kopf.get('status', 'Vorschlag').capitalize(), 'name': kopf.get('titel', f.stem), 'html': t, 'fehlt': fehlend(t),
                    'zweck': (kopf.get('bezug', '') + (' · ' if kopf.get('bezug') else '') + 'Stand ' + kopf.get('datum', '?')).strip(), 'quelle': f'proposals/{f.name}'})
# Grundlagen: Farben und Schriftgrößen, Werte live aus dem gewählten Theme und Modus gelesen
KERN_CSS = (ROOT / 'vendor/kern/kern.min.css').read_text(encoding='utf-8')
ROLLEN_CSS = (ROOT / 'src/km-roles.css').read_text(encoding='utf-8')
WERT = ('<script>addEventListener("load",function(){var x=document.createElement("canvas").getContext("2d",{willReadFrequently:true}),m=document.createElement("i");x.canvas.width=x.canvas.height=1;document.body.appendChild(m);'
        'function rgb(v){m.style.background="var("+v+")";x.clearRect(0,0,1,1);x.fillStyle=getComputedStyle(m).backgroundColor;x.fillRect(0,0,1,1);return x.getImageData(0,0,1,1).data}'
        'function hx(d){return d[3]?"#"+[d[0],d[1],d[2]].map(function(v){return("0"+v.toString(16)).slice(-2)}).join(""):"transparent"}'
        'function lum(d){return [0,1,2].reduce(function(s,i){var c=d[i]/255;c=c<=.04045?c/12.92:Math.pow((c+.055)/1.055,2.4);return s+[.2126,.7152,.0722][i]*c},0)}'
        'document.querySelectorAll("[data-farbe]").forEach(function(e){var d=rgb(e.dataset.farbe),h=e.querySelector(".sb-hex");if(h)h.textContent=hx(d);else e.title=e.dataset.farbe+" "+hx(d)});'
        'document.querySelectorAll("[data-kontrast]").forEach(function(e){var p=e.dataset.kontrast.split(" "),a=lum(rgb(p[0])),b=lum(rgb(p[1])),r=(Math.max(a,b)+.05)/(Math.min(a,b)+.05);e.textContent=r.toFixed(1).replace(".",",")+":1 "+(r>=4.5?"AA":r>=3?"AA groß":"zu wenig")});'
        'document.querySelectorAll("[data-wert]").forEach(function(e){e.querySelector("b").textContent=getComputedStyle(document.documentElement).getPropertyValue(e.dataset.wert).trim().slice(0,40)});'
        'document.querySelectorAll("[data-groesse]").forEach(function(e){e.querySelector("small").textContent=getComputedStyle(e.lastElementChild).fontSize})})</script>'
        '<style>h3.sb-h{font-size:var(--km-font-size-m);margin:var(--km-space-xl) 0 var(--km-space-2xs)}h3.sb-h:first-of-type{margin-top:0}p.sb-z{margin:0 0 var(--km-space-s);font-size:var(--km-font-size-s);color:var(--km-color-text-muted)}'
        '.sb-r{display:grid;grid-template-columns:4.5rem minmax(14rem,1fr) 5.5rem 7.5rem;gap:var(--km-space-xs) var(--km-space-m);align-items:center;max-width:56rem}'
        '.sb-r>div{display:contents}.sb-s{height:2.75rem;display:grid;place-items:center;font-weight:600;border:var(--km-border-width) solid var(--km-color-border-card)}'
        '.sb-r code,.sb-hex,.sb-r [data-kontrast]{font-family:var(--km-font-mono);font-size:var(--km-font-size-xs);white-space:nowrap}.sb-r p{margin:0;font-size:var(--km-font-size-s);line-height:1.35}.sb-r p small{display:block;color:var(--km-color-text-muted)}.sb-hex,.sb-r [data-kontrast]{color:var(--km-color-text-muted)}'
        '.sb-p{display:grid;grid-template-columns:7rem 1fr;gap:var(--km-space-2xs) var(--km-space-m);align-items:center}.sb-p b{font-size:var(--km-font-size-s);font-weight:600}.sb-p ol{display:flex;margin:0;padding:0;list-style:none}'
        '.sb-p li{flex:1;min-width:0;display:grid;gap:2px;font:var(--km-font-size-xs)/1.2 var(--km-font-mono);color:var(--km-color-text-muted);text-align:center}.sb-p li span{height:2.25rem}'
        '.sb-w{display:grid;grid-template-columns:minmax(12rem,16rem) minmax(10rem,18rem) 8rem 1fr;gap:var(--km-space-xs) var(--km-space-m);align-items:center;max-width:64rem}.sb-w>div{display:contents}.sb-w code{font-family:var(--km-font-mono);font-size:var(--km-font-size-xs);white-space:nowrap}.sb-w b{font:var(--km-font-size-xs) var(--km-font-mono);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.sb-w .sb-hex{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}'
        '.sb-t{display:grid;grid-template-columns:14rem 4rem 1fr;gap:var(--km-space-xs) var(--km-space-m);align-items:baseline;margin:0 0 var(--km-space-xl)}.sb-t code{font-size:var(--km-font-size-xs)}.sb-t small{color:var(--km-color-text-muted);font-size:var(--km-font-size-xs)}.sb-t p{margin:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}'
        '.sb-w b,.sb-w .sb-hex{white-space:normal;overflow:visible;overflow-wrap:anywhere}'
        '@media (max-width:40rem){.sb-r code,.sb-hex,.sb-r [data-kontrast]{white-space:normal;overflow-wrap:anywhere}.sb-r,.sb-w,.sb-t,.sb-p{grid-template-columns:minmax(0,1fr) auto}.sb-r>div>*:nth-child(n+3),.sb-w>div>*:nth-child(n+3){grid-column:1/-1}.sb-t>*:nth-child(3n){grid-column:1/-1}.sb-t p{white-space:normal}.sb-p ol{flex-wrap:wrap}.sb-p li{flex:1 0 2.5rem}}</style>')  # schmal ohne Überlauf (Prüfbericht 2026-11-08)  # läuft in jeder Story mit (D.interaktion), stört ohne data-* nicht


def eindeutig(muster, text):
    return list(dict.fromkeys(re.findall(muster, text)))


def zeile(n, zweck='', flaeche=None, schrift=None, ring=None):
    """Eine Farbe: Probe-Feld, Name und Zweck, Hex, Kontrast (wenn Schrift auf Fläche)."""
    stil = f'background:var({flaeche or n})' + (f';color:var({schrift})' if schrift else '') + (f';box-shadow:inset 0 0 0 3px var({ring})' if ring else '')
    kontrast = f'<span data-kontrast="{schrift} {flaeche or n}"></span>' if schrift else '<span></span>'
    return (f'<div data-farbe="{n}"><span class="sb-s" style="{stil}">' + ('Aa' if schrift else '') + f'</span><p><code>{n}</code>'
            + (f'<small>{zweck}</small>' if zweck else '') + f'</p><span class="sb-hex"></span>{kontrast}</div>')


def gruppe(titel, zweck, zeilen):
    return f'<h3 class="sb-h">{titel}</h3>' + (f'<p class="sb-z">{zweck}</p>' if zweck else '') + '<div class="sb-r">' + ''.join(zeilen) + '</div>'


def k(r): return '--km-color-' + r


FLAECHE, TEXT, LINIE = (lambda r: dict(schrift=k('text'))), (lambda r: dict(flaeche=k('card'), schrift=k(r))), (lambda r: dict(flaeche=k('card'), ring=k(r)))
ROLLEN = [  # (Gruppe, Satz, [(Rolle, Zweck, Probe)])
    ('Flächen', 'Von außen nach innen; jede Ebene liegt auf der vorigen. Probe: Fließtext darauf.', [
        ('page', 'Seitenhintergrund', FLAECHE), ('section', 'Bereich, die Wanne um jeden Abschnitt', FLAECHE), ('card', 'Karte, Dialog', FLAECHE),
        ('inset', 'Eingelassene Fläche: Tabellenkopf, Eingabefeld', FLAECHE), ('track', 'Spur von Balken und Schaltern', FLAECHE)]),
    ('Linien', 'Rahmen und Trenner, gezeigt auf der Karte.', [('border-section', 'Rahmen der Bereiche', LINIE), ('border-card', 'Rahmen der Karten, Trennlinien', LINIE)]),
    ('Text', 'Probe auf der Karte, Kontrast nach WCAG gerechnet.', [('text', 'Fließtext und Titel', TEXT), ('text-muted', 'Nebentext, Beschreibungen', TEXT), ('text-dim', 'Meta, Beschriftungen, Zähler', TEXT)]),
    ('Aktion', 'Alles, was man anklicken kann.', [('accent', 'Links, aktive Zustände; Probe: Text darauf', lambda r: dict(schrift=k('on-accent'))),
        ('accent', 'als Linkfarbe auf der Karte', TEXT), ('focus', 'Fokusring der Tastatur', LINIE)]),
    ('Hinweis und Hervorhebung', 'Wirkung nach außen und angeheftete Bereiche.', [('attention', 'Freigabe, Upload, Wirkung nach außen', lambda r: dict(schrift=k('on-attention'))),
        ('highlight-bg', 'Fläche eines hervorgehobenen Bereichs', FLAECHE), ('highlight', 'Rand und Symbol der Hervorhebung', lambda r: dict(flaeche=k('highlight-bg'), ring=k(r)))]),
]
erfasst = {k(r) for _, _, zs in ROLLEN for r, _, _ in zs} | {k('on-accent'), k('on-attention')}  # on-* stecken in der Probe
rollen_html = ''.join(gruppe(g, s, [zeile(k(r), z, **pr(r)) for r, z, pr in zs]) for g, s, zs in ROLLEN)
rest = [r for r in eindeutig(r'(--km-color-[a-z-]+)\s*:', ROLLEN_CSS) if r not in erfasst]
if rest:
    rollen_html += gruppe('Weitere', 'Noch keiner Gruppe zugeordnet.', [zeile(r) for r in rest])

# Übrige Kit-Tokens: Werte live, Abstände und Linien als Probe
ROH = dict(re.findall(r'^\s*(--km-(?!color)[a-z0-9-]+)\s*:\s*([^;]+);', ROLLEN_CSS, flags=re.M))
TOKEN_GRUPPEN = [('Abstände', 'km-space', lambda n: f'<span style="display:block;height:.75rem;width:var({n});background:var(--km-color-accent)"></span>'),
                 ('Lücke', 'km-gap', lambda n: f'<span style="display:block;height:.75rem;width:var({n});background:var(--km-color-accent)"></span>'),
                 ('Linien und Ecken', 'km-border|km-radius', lambda n: f'<span style="display:block;height:1.5rem;border:var({n}) solid var(--km-color-text)"></span>' if 'border' in n else ''),
                 ('Schrift', 'km-font(?!-size)', lambda n: f'<span style="font-family:var({n})">Projekt 0123</span>' if n in ('--km-font', '--km-font-mono') else f'<span style="font-weight:var({n})">Projekt 0123</span>'),
                 ('Schriftgrößen', 'km-font-size', lambda n: f'<span style="font-size:var({n})">Projekt 0123</span>'),
                 ('Icons', 'km-icon', lambda n: ''), ('Schatten und Zustände', 'km-shadow|km-opacity', lambda n: ''), ('Formen', 'km-caret', lambda n: f'<span style="display:block;width:1rem;height:1rem;background:var(--km-color-text);mask:var({n}) center/contain no-repeat;-webkit-mask:var({n}) center/contain no-repeat"></span>')]
tok_rest, tok_html = dict(ROH), ''
for titel, muster, probe in TOKEN_GRUPPEN:
    ns = [n for n in ROH if re.match('--(' + muster + ')', n)]
    for n in ns: tok_rest.pop(n, None)
    if ns:
        tok_html += f'<h3 class="sb-h">{titel}</h3><div class="sb-w">' + ''.join(
            f'<div data-wert="{n}"><code>{n}</code><span class="sb-hex">{html.escape(ROH[n].strip()[:60])}</span><b></b><span>{probe(n)}</span></div>' for n in ns) + '</div>'
if tok_rest:
    tok_html += '<h3 class="sb-h">Weitere</h3><div class="sb-w">' + ''.join(f'<div data-wert="{n}"><code>{n}</code><span class="sb-hex">{html.escape(v[:60])}</span><b></b><span></span></div>' for n, v in tok_rest.items()) + '</div>'

semantik = {}
for n in sorted(eindeutig(r'(--kern-color-(layout|action|feedback|decorative|form)[a-z-]*)\s*:', KERN_CSS)):
    semantik.setdefault(n[1], []).append(n[0])
SEM_TITEL = {'layout': ('Layout', 'Flächen, Rahmen, Text'), 'action': ('Aktion', 'Links, Knöpfe, Zustände'), 'feedback': ('Rückmeldung', 'Info, Erfolg, Warnung, Fehler'),
             'decorative': ('Dekor', 'Trenner und Schmuckflächen'), 'form': ('Formular', 'Eingabefelder')}
semantik_html = ''.join(gruppe(*SEM_TITEL.get(k, (k, '')), [zeile(n) for n in ns]) for k, ns in semantik.items())

farbtoene = {}
for n in eindeutig(r'(--kern-color-([a-z]+)-(\d{3}))\s*:', KERN_CSS):
    farbtoene.setdefault(n[1], []).append((n[2], n[0]))
palette_html = '<div class="sb-p">' + ''.join(f'<b>{h}</b><ol>' + ''.join(f'<li data-farbe="{v}"><span style="background:var({v})"></span>{s}</li>' for s, v in sorted(st)) + '</ol>' for h, st in farbtoene.items()) + '</div>'

grundlagen = [
    ('Farben: Rollen (--km-)', 'Farben nach Aufgabe; Bausteine lesen nur diese. Werte und Kontraste live aus Theme und Modus.', rollen_html),
    ('Farben: KERN-Semantik', 'Die KERN-Farben, auf die die Rollen zeigen, nach Familie.', semantik_html),
    ('Farben: KERN-Palette', 'Alle Farbtöne des KERN-Kits als Verlauf von hell nach dunkel; Zahl = Stufe, Hex beim Überfahren.', palette_html),
    ('Abstände', 'Regelwerk: von außen nach innen jede Ebene eine Stufe kleiner. Schaubild mit den Werten des gewählten Themes.', '<div class="km-prose"><ul>' + ''.join(f'<li>{r}</li>' for r in ABSTAND_REGELN) + '</ul></div><div class="km-table-wrap" style="margin:var(--km-space-block) 0"><table class="km-table"><thead><tr><th>Ebene</th><th>Token</th><th>Stufe</th><th>Wofür</th></tr></thead><tbody>' + ''.join(f'<tr><td>{e}</td><td class="km-table__nowrap"><code>{tk}</code></td><td class="km-table__nowrap">{st}</td><td>{w}</td></tr>' for e, tk, st, w in ABSTAENDE) + '</tbody></table></div>' + ABSTAND_BILD),
    ('Weitere Tokens', 'Abstände, Linien, Schrift, Icons, Zustände: Quelle in src/km-roles.css, berechneter Wert live aus Theme und Modus.', tok_html),
    ('Schriftgrößen', 'Rollen (--km-font-size-*) und die ganze KERN-Skala; Größe live gemessen.',
     '<h3 class="sb-h">Rollen</h3><div class="sb-t">' + ''.join(f'<div data-groesse style="display:contents"><code>{n}</code><small></small><p style="font-size:var({n})">Projektübersicht 0123</p></div>' for n in eindeutig(r'(--km-font-size-[a-z0-9]+)\s*:', ROLLEN_CSS)) + '</div>'
     + '<h3 class="sb-h">KERN-Skala</h3><div class="sb-t">' + ''.join(f'<div data-groesse style="display:contents"><code>{n}</code><small></small><p style="font-size:var({n})">Projektübersicht 0123</p></div>' for n in sorted(eindeutig(r'(--kern-font-size-\d+)\s*:', KERN_CSS), key=lambda x: int(x.rsplit('-', 1)[1]))) + '</div>'),
]
for name, zweck, markup in grundlagen:
    stories.append({'gruppe': 'Grundlagen', 'pfad': 'Tokens', 'name': name, 'html': markup, 'fehlt': [], 'zweck': zweck, 'quelle': 'src/km-roles.css, vendor/kern/kern.min.css'})
# Einstieg: Einführung aus docs/intro.md als erste Story
from einfuehrung import einfuehrung_html, changelog_html  # gemeinsame Quelle mit der Doku (0.9.0)
stories.insert(0, {'gruppe': 'Grundlagen', 'pfad': 'Kernmix', 'name': 'Einführung', 'html': einfuehrung_html('h2'), 'seite': True, 'fehlt': [], 'zweck': 'Ein Remix von KERN: worum es geht, für wen und was im Mix steckt.', 'quelle': 'docs/intro.md, assets/einfuehrung/*.svg (tools/einfuehrung.py)'})
stories.insert(1, {'gruppe': 'Grundlagen', 'pfad': 'Kernmix', 'name': 'Changelog', 'html': '<header class="km-hero km-hero--start"><p class="km-hero__kicker">Kernmix</p><h2 class="km-hero__title">Changelog</h2></header>' + changelog_html('h2'), 'seite': True, 'fehlt': [], 'zweck': 'Alle Versionen mit Release-Namen, neueste oben.'})  # eigene Seite statt Sprung in die Doku
ORDNUNG = {'Grundlagen': -1, 'Erweiterungen': 0, 'Proposals': 1, 'KERN-Standard': 2}
stories.sort(key=lambda s: (ORDNUNG[s['gruppe']], s['pfad'].lower() if s['gruppe'] == 'KERN-Standard' else '', s['pfad'] != 'Kernmix'))
for n, s in enumerate(stories):
    s['id'] = re.sub(r'[^a-z0-9]+', '-', f"{s['gruppe']}-{s['pfad']}-{s['name']}".lower()).strip('-')

# Querverweise: je km-Baustein eine Heimat-Story; je Story „Enthält“ (andere Bausteine im Markup) und „Verwendet in“
def _bloecke(html): return {re.split(r'__|--', c)[0] for c in re.findall(r'km-[a-z0-9_-]+', ' '.join(re.findall(r'class="([^"]*)"', html)))} - {'km-icon'}  # Grundklasse der Symbole erzeugt keine Bezüge
_erw = [s for s in stories if s['gruppe'] == 'Erweiterungen']
_heimat = {}
def _klassen(html): return [c for c in re.findall(r'km-[a-z0-9_-]+', ' '.join(re.findall(r'class="([^"]*)"', html)))]
from bausteine_nachtrag import NACHTRAG as _NT
_grund = len(BAUSTEINE) - len(_NT)  # Grund-Stories (bausteine.py) vor den Nachträgen
for s in sorted(_erw, key=lambda s: (s.get('ordnung', 0) >= _grund, s.get('ordnung', 0))):  # Heimat: zuerst Grund-Stories (größter Anteil am Markup), Nachträge nur für Bausteine, die dort fehlen
    kl = _klassen(s['html']); n = len(kl) or 1
    for bl in {re.split(r'__|--', c)[0] for c in kl}:
        anteil = sum(1 for c in kl if re.split(r'__|--', c)[0] == bl) / n
        stufe = s.get('ordnung', 0) >= _grund
        if bl not in _heimat or (stufe == _heimat[bl][2] and anteil > _heimat[bl][1]): _heimat[bl] = (s['id'], anteil, stufe)
for s in stories:
    eig = {bl for bl, h in _heimat.items() if h[0] == s['id']}
    s['enthaelt'] = sorted({_heimat[bl][0] for bl in _bloecke(s['html']) if bl in _heimat and _heimat[bl][0] != s['id']})
    s['verwendet'] = sorted({x['id'] for x in _erw if x['id'] != s['id'] and eig & _bloecke(x['html'])})
_namen = {s['id']: s['name'] for s in stories}
for s in stories:
    s['enthaelt'] = [[i, _namen[i]] for i in s['enthaelt'] if _namen[i] != s['name']]; s['verwendet'] = [[i, _namen[i]] for i in s['verwendet'] if _namen[i] != s['name']]

themes = [{'id': 'kern', 'name': 'KERN', 'css': []}] + [
    {'id': p.stem, 'name': {'kern-nah': 'Kobalt', 'startklar': 'Papier'}.get(p.stem, p.stem.replace('-', ' ').title()), 'css': [f'../dist/themes/{p.name}']}
    for p in sorted((ROOT / 'dist/themes').glob('*.css'))]

# ── Doku je Story: Erweiterungen zeigen ihre Komponenten-Doku aus docs/komponenten/*.md im Aufbau D „Vier Fragen mit Kapitelleiste“
#; KERN-Standard verweist auf die KERN-Doku (Code im Repository, Online-Doku) ──
from komponenten_doku import doku_html, kapitel_huelle  # noqa: E402
# Zuordnung Story (Anker in tools/bausteine*.py) → Doku-Dateien; erste Datei ist die Heimat-Doku
DOKU = {
 'seitenleiste': ['seitenleiste', 'schalter'], 'sidebar-hierarchie': ['seitenleiste', 'schalter'], 'sidebar-rail': ['seitenleiste'],
 'bereich': ['bereich'], 'fokus': ['bereich'], 'gruppe': ['bereich', 'text', 'kleinteile'], 'teilstuecke': ['seitenrahmen', 'bereich', 'karte', 'text'],
 'bedienteile': ['bereich', 'suchfeld', 'kopfzeile', 'ziehen'], 'zustaende-skript': ['spaltenauswahl', 'suchfeld', 'aufgabe', 'bereich', 'seitenrahmen'],
 'karte': ['karte'], 'projektkarte': ['karte', 'kennzahlen'], 'info-karte': ['karte'], 'kuerzel': ['karte'], 'fliesstext': ['text', 'karte'], 'hinweiskasten': ['text'], 'lesetext': ['text'],
 'einfuehrung': ['einfuehrung'], 'hero': ['einfuehrung', 'kennzahlen'], 'funktionen': ['einfuehrung'],
 'fakten': ['kennzahlen'], 'kacheln-raster': ['kennzahlen'], 'kennzahlen': ['kennzahlen', 'seitenrahmen'],
 'aufgabe': ['aufgabe', 'icon-knopf'], 'aufgabe-loeschen': ['aufgabe'], 'vorschlaege': ['aufgabe'],
 'chip-pill': ['etikett'], 'noten': ['etikett'], 'schalter': ['schalter'], 'kontrollkaestchen': ['schalter'], 'eckleiste': ['seitenrahmen', 'schalter'],
 'suche': ['suchfeld', 'trefferliste'], 'suchfeld': ['suchfeld', 'spaltenauswahl'], 'treffer-kopf': ['trefferliste', 'suchfeld'], 'trefferliste': ['trefferliste', 'segmented-control'],
 'suchhinweise': ['trefferliste'], 'quicklinks': ['kopfzeile', 'monogramm'], 'agent': ['agent'], 'agenten-varianten': ['agent'],
 'grafik': ['grafik'], 'grafik-zustaende': ['grafik'], 'segmented': ['segmented-control', 'knopf'],
 'zeitlog': ['kleinteile'], 'kleinteile': ['kleinteile', 'schalter', 'seitenrahmen'], 'einheitlich': ['kleinteile'], 'werkzeugfarben': ['kleinteile'], 'vorschaukarte': ['kleinteile'],
 'tabelle': ['tabelle', 'monogramm', 'etikett'], 'tabelle-spalten': ['tabelle'], 'tabelle-regeln': ['tabelle'], 'unterzeilen': ['tabelle'], 'zahlenliste': ['tabelle', 'kennzahlen'],
 'zustaende': ['icon-knopf', 'tabelle', 'aufgabe', 'etikett', 'kopfzeile'], 'dialog': ['dialog'], 'textlinks': ['text'], 'verdeckt': ['verdeckter-wert', 'icon-knopf'],
 'antwort': ['antwort'], 'pruefkarte': ['pruefkarte', 'antwort'], 'score': ['score', 'etikett'],
 'massnahmen': ['listen'], 'angaben': ['listen'], 'knopf': ['knopf'], 'selectpanel': ['auswahl-mit-suche'], 'kopfzeile': ['kopfzeile', 'seitenrahmen'],
 'filterleiste': ['filterleiste', 'seitenleiste'], 'metaline': ['metaline', 'etikett'],
}
DOKUS = {}
_ANKER_ID = {s['anker']: (s['id'], s['name']) for s in stories if s.get('anker')}
for _d in sorted({d for ds in DOKU.values() for d in ds}):
    _t = (ROOT / f'docs/komponenten/{_d}.md').read_text(encoding='utf-8')
    DOKUS[_d] = doku_html(_t, _d, _ANKER_ID)
_fehlt_doku = [a for a, *_ in BAUSTEINE if a not in DOKU]
if _fehlt_doku: print('Stories ohne Doku-Zuordnung:', _fehlt_doku)
# KERN-Standard: Code im offiziellen Repository (Tag der eingebundenen Version) und Online-Doku auf kern-ux.de, je Story-Ordner in kern-fluid-type/stories.
# Alle Adressen am 2026-11-09 abgerufen (HTTP 200). Wo es keine Einzelseite gibt, steht die nächsthöhere Seite (Kommentar).
KERN_REPO = f'https://gitlab.opencode.de/kern-ux/kern-ux-plain/-/blob/v{KERN}/src/scss/core/'
KERN_WEB = 'https://www.kern-ux.de/komponenten/'
KERN_DOKU = {  # Ordner: (Datei im Repository, Seite auf kern-ux.de)
 'Accordion': ('components/_accordion.scss', 'accordion'), 'Alert': ('components/_alert.scss', 'alert'), 'Badge': ('components/_badge.scss', 'badge'),
 'Body': ('typography/_body.scss', 'text/body'), 'Button': ('components/_button.scss', 'button'), 'Card': ('components/_card.scss', 'card'),
 'Checkbox': ('components/_checkbox.scss', 'form-inputs/checkboxes'), 'CheckboxList': ('components/_checkbox.scss', 'form-inputs/checkboxes'),
 'CssFlex': ('layout/_utilities.scss', 'layout/hilfsklassen'), 'CssGrid': ('layout/_grid.scss', 'layout/grid-system'), 'Gap': ('layout/_utilities.scss', 'layout/hilfsklassen'),
 'Grid': ('layout/_grid.scss', 'layout/grid-system'), 'Spacing': ('layout/_spacing.scss', 'layout/hilfsklassen'), 'Stack': ('layout/_utilities.scss', 'layout/hilfsklassen'),
 'UtilityHelper': ('layout/_utilities.scss', 'layout/hilfsklassen'),
 'DescriptionList': ('components/_description-list.scss', 'descriptionlist'), 'Dialog': ('components/_dialog.scss', 'dialog'), 'Divider': ('components/_divider.scss', 'divider'),
 'Fieldset': ('components/_fieldset.scss', 'fieldset'), 'Heading': ('typography/_heading.scss', 'text/heading'), 'Icon': ('components/_icon.scss', 'icon'),
 'InputDate': ('components/_input.scss', 'form-inputs/date'), 'InputEmail': ('components/_input.scss', 'form-inputs/e-mail'), 'InputFile': ('components/_input.scss', 'form-inputs/file'),
 'InputGroup': ('components/_input-group.scss', 'form-inputs/input-group'), 'InputNumber': ('components/_input.scss', 'form-inputs/number'),
 'InputPassword': ('components/_input.scss', 'form-inputs/password'), 'InputTel': ('components/_input.scss', 'form-inputs/tel'), 'InputText': ('components/_input.scss', 'form-inputs/text'),
 'InputUrl': ('components/_input.scss', 'form-inputs/url'), 'Textarea': ('components/_input.scss', 'form-inputs/textarea'),
 'Kopfzeile': ('components/_kopfzeile.scss', 'kopfzeile'), 'Label': ('typography/_label.scss', 'text/label'), 'Link': ('typography/_link.scss', 'link'),
 'Lists': ('typography/_list.scss', 'text/list'), 'Loader': ('components/_loader.scss', 'loader'), 'Preline': ('typography/_preline.scss', 'text/preline'),
 'Progress': ('components/_progress.scss', 'progress'), 'Radio': ('components/_radio.scss', 'form-inputs/radios'), 'Select': ('components/_select.scss', 'form-inputs/select'),
 'Subline': ('typography/_subline.scss', 'text/subline'), 'Summary': ('components/_summary.scss', 'summary'), 'Table': ('components/_table.scss', 'table'),
 'Tasklist': ('components/_task-list.scss', 'tasklist'), 'Title': ('typography/_title.scss', 'text/title'),
 'Pattern': ('layout/_grid.scss', 'header'),  # Header-Muster aus Raster und Hilfsklassen: keine eigene Datei im Repository, daher layout/_grid.scss
}
for _s in stories:
    if _s['gruppe'] == 'Erweiterungen':
        _s['doku'] = DOKU.get(_s.get('anker'), [])
    elif _s['gruppe'] == 'KERN-Standard':
        _ordner = _s['quelle'].split('/')[2]
        if _ordner in KERN_DOKU:
            _r, _w = KERN_DOKU[_ordner]; _s['kern'] = [KERN_REPO + _r, KERN_WEB + _w]
        else: print('KERN-Story ohne Doku-Verweis:', _s['quelle'])
# Icon je Story in der Navigation: Erweiterungen nach Anker, KERN-Standard nach Story-Ordner, Grundlagen nach Name; sonst „component“
ICON_STORY = {
 'seitenleiste': 'panel-left', 'sidebar-hierarchie': 'panel-left', 'sidebar-rail': 'panel-left-close', 'bereich': 'panel-top', 'fokus': 'pin',
 'karte': 'square', 'projektkarte': 'folder-kanban', 'info-karte': 'info', 'kuerzel': 'keyboard', 'einfuehrung': 'image', 'hero': 'megaphone', 'funktionen': 'layout-grid',
 'fakten': 'gauge', 'kacheln-raster': 'layout-grid', 'kennzahlen': 'chart-column', 'aufgabe': 'square-check', 'aufgabe-loeschen': 'trash', 'vorschlaege': 'sparkles',
 'gruppe': 'heading', 'chip-pill': 'tag', 'noten': 'award', 'schalter': 'toggle-left', 'kontrollkaestchen': 'square-check', 'eckleiste': 'panel-bottom',
 'suche': 'search', 'suchfeld': 'search', 'treffer-kopf': 'search', 'trefferliste': 'list', 'suchhinweise': 'lightbulb', 'quicklinks': 'link',
 'agent': 'bot', 'agenten-varianten': 'bot', 'grafik': 'network', 'grafik-zustaende': 'network', 'segmented': 'columns-3',
 'zeitlog': 'clock', 'kleinteile': 'info', 'einheitlich': 'shapes', 'werkzeugfarben': 'palette', 'vorschaukarte': 'image',
 'tabelle': 'table', 'tabelle-spalten': 'table', 'tabelle-regeln': 'table', 'unterzeilen': 'list-tree', 'zahlenliste': 'table',
 'zustaende': 'mouse-pointer-click', 'zustaende-skript': 'code', 'teilstuecke': 'puzzle', 'bedienteile': 'grip-vertical', 'dialog': 'message-square',
 'textlinks': 'link', 'fliesstext': 'text-align-start', 'hinweiskasten': 'circle-alert', 'lesetext': 'book-open-text', 'verdeckt': 'eye-off', 'massnahmen': 'list-checks', 'angaben': 'list',
 'knopf': 'square-mouse-pointer', 'selectpanel': 'list-filter', 'kopfzeile': 'panel-top',
 # KERN-Standard (Story-Ordner)
 'Accordion': 'chevrons-up-down', 'Alert': 'triangle-alert', 'Badge': 'tag', 'Body': 'pilcrow', 'Button': 'square-mouse-pointer', 'Card': 'square',
 'Checkbox': 'square-check', 'CheckboxList': 'list-checks', 'CssFlex': 'columns-3', 'CssGrid': 'layout-grid', 'Gap': 'space', 'Grid': 'layout-grid',
 'Spacing': 'space', 'Stack': 'rows-3', 'UtilityHelper': 'wrench', 'DescriptionList': 'list', 'Dialog': 'message-square', 'Divider': 'minus',
 'Fieldset': 'group', 'Heading': 'heading', 'Icon': 'shapes', 'InputDate': 'calendar', 'InputEmail': 'mail', 'InputFile': 'file-up', 'InputGroup': 'text-cursor-input',
 'InputNumber': 'hash', 'InputPassword': 'key-round', 'InputTel': 'phone', 'InputText': 'text-cursor-input', 'InputUrl': 'link', 'Textarea': 'text-align-start',
 'Kopfzeile': 'panel-top', 'Label': 'tag', 'Link': 'link', 'Lists': 'list', 'Loader': 'loader', 'Preline': 'heading', 'Progress': 'chart-no-axes-gantt',
 'Radio': 'circle-dot', 'Select': 'chevron-down', 'Subline': 'heading', 'Summary': 'list-collapse', 'Table': 'table', 'Tasklist': 'list-todo', 'Title': 'heading',
 'Pattern': 'panel-top',
 # Grundlagen
 'Einführung': 'disc-3', 'Changelog': 'scroll-text', 'Farben: Rollen (--km-)': 'palette', 'Farben: KERN-Semantik': 'palette', 'Farben: KERN-Palette': 'swatch-book', 'Abstände': 'space', 'Weitere Tokens': 'variable', 'Schriftgrößen': 'type',
}
from bausteine import IC as _IC
for _s in stories:
    _k = _s.get('anker') if _s['gruppe'] == 'Erweiterungen' else (_s['quelle'].split('/')[2] if _s['gruppe'] == 'KERN-Standard' else _s['name'])
    _n = ICON_STORY.get(_k, 'component')
    _s['icon'] = ikon(_n if _n in _IC else 'component', 'km-sidebar__icon')
_fehlt_icon = sorted({n for n in ICON_STORY.values() if n not in _IC})
if _fehlt_icon: print('Icons nicht in Lucide 1.49.0, Ersatz component:', _fehlt_icon)
for _s in stories: _s.pop('zweck_roh', None)
DOKU_HEIM = {}  # Doku-Datei → erste Story, deren Heimat-Doku sie ist
for _s in stories:
    if _s.get('doku'): DOKU_HEIM.setdefault(_s['doku'][0], _s['id'])
daten = json.dumps({'stories': stories, 'dokus': DOKUS, 'dokuheim': DOKU_HEIM, 'themes': themes, 'interaktion': WERT + '<script>document.addEventListener("click",function(e){var t=e.target,s;if((s=t.closest(".km-segmented__btn"))&&!s.disabled){s.parentNode.querySelectorAll(".km-segmented__btn").forEach(function(b){b.setAttribute("aria-pressed",String(b===s))});return}if((s=t.closest("[role=switch]"))&&!s.disabled&&s.getAttribute("aria-disabled")!=="true"){s.setAttribute("aria-checked",String(s.getAttribute("aria-checked")!=="true"));return}if((s=t.closest(".km-sidebar__item"))&&s.getAttribute("aria-disabled")!=="true"){s.closest(".km-sidebar__group").querySelectorAll(".km-sidebar__item[aria-pressed]").forEach(function(b){b.setAttribute("aria-pressed",String(b===s))});return}if((s=t.closest("button[aria-pressed]"))&&!s.disabled){s.setAttribute("aria-pressed",String(s.getAttribute("aria-pressed")!=="true"));return}if((s=t.closest("[aria-expanded]"))){var z=s.getAttribute("aria-expanded")!=="true";s.setAttribute("aria-expanded",String(z));if(s.classList.contains("km-intro__more")){var b=s.previousElementSibling;if(b)b.classList.toggle("km-intro__body--short",!z);s.textContent=z?"Weniger":"Weiterlesen";return}if(s.classList.contains("km-sidebar__label-btn")){s.closest(".km-sidebar__group").querySelectorAll(".km-sidebar__item").forEach(function(b){b.hidden=!z});return}var n=s.nextElementSibling;if(n)n.style.display=z?"block":"none";return}if((s=t.closest(".km-card--collapsible > .km-card__head"))){s.parentNode.classList.toggle("km-card--collapsed");return}if((s=t.closest(".km-table__group"))){s.classList.toggle("km-table__group--collapsed");var r=s.nextElementSibling;while(r&&!r.classList.contains("km-table__group")){r.hidden=s.classList.contains("km-table__group--collapsed");r=r.nextElementSibling}return}if((s=t.closest(".km-table__sort"))){var a=s.getAttribute("aria-sort")==="ascending"?"descending":"ascending";s.closest("tr").querySelectorAll(".km-table__sort").forEach(function(h){h.setAttribute("aria-sort","none")});s.setAttribute("aria-sort",a);return}if((s=t.closest(".km-quicklinks__pill-remove"))){s.closest(".km-quicklinks__pill").remove();return}});</script>'}, ensure_ascii=False).replace('</', '<\\/')
anzahl = {g: sum(1 for s in stories if s['gruppe'] == g) for g in ('Grundlagen', 'KERN-Standard', 'Erweiterungen', 'Proposals')}

_SEK, _NAV = kapitel_huelle(
    vor={'was': '<div class="sb-buehne" aria-label="Beispiel"><iframe id="buehne" title="Vorschau der Story"></iframe></div>'},
    nach={'wie': f'<h4 class="km-subhead">{ikon("code")}Markup der Story</h4><div class="km-codeblock__box"><pre class="km-codeblock sb-markup" aria-label="Markup der Story"><code id="code"></code></pre><button type="button" class="km-iconbtn km-iconbtn--label km-codeblock__copy" id="kopie">{ikon("copy")}Kopieren</button></div>'})
seite = f'''<!doctype html>
<html lang="de" data-kern-theme="dark">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Kernmix · Komponentenbeschreibung</title>
<link rel="stylesheet" href="../vendor/kern/kern.min.css">
<link rel="stylesheet" href="../vendor/kern/fonts/fira-sans.css">
<link rel="stylesheet" href="../dist/km.css">
<link rel="stylesheet" href="../dist/fonts.css">
<script src="../dist/km-table.js"></script>
<script src="../dist/km-popup.js"></script>
<link rel="stylesheet" id="huelle-theme" href="../dist/themes/kern-nah.css">
<!-- Hülle folgt seit 2026-11-08 dem gewählten Theme (vorher Standard-KERN; im hellen Modus lagen Seite, Abschnitt und Karte dort alle auf Weiß). Hülle überarbeitet 2026-11-08: Ebenen Seite → Abschnitt → Karte, nur --km-*-Tokens und Kit-Bausteine -->
<style>
  html, body {{ height: 100%; }}
  body {{ margin: 0; display: grid; grid-template-rows: auto minmax(0, 1fr) auto; background: var(--km-color-page); color: var(--km-color-text); font-family: var(--km-font); font-size: var(--km-font-size-s); }}
  .sb-kopf {{ display: flex; flex-wrap: wrap; align-items: center; gap: var(--km-space-s) var(--km-space-l); padding: var(--km-space-s) var(--km-space-page); background: var(--km-color-page); /* dunkler als der Rest */ border-bottom: var(--km-border-width) solid var(--km-color-border-card); box-shadow: var(--km-shadow); position: relative; z-index: 1; }}
  .sb-marke {{ display: flex; align-items: center; gap: var(--km-space-s); }}
  a.sb-marke {{ color: inherit; text-decoration: none; }} a.sb-marke:hover h1 {{ color: var(--km-color-accent); }} /* Logo und Icon führen zur Startseite des aktuellen Bereichs */
  .sb-marke .km-monogram {{ --km-monogram-color: var(--km-color-accent); color: var(--km-color-on-accent); width: calc(1.3 * var(--km-monogram-size)); height: calc(1.3 * var(--km-monogram-size)); font-size: var(--km-font-size-xs); }}
  .sb-marke h1 {{ margin: 0; font-size: var(--km-font-size-m); font-weight: var(--km-font-weight-strong); line-height: 1.2; }}
  .sb-marke small {{ display: block; color: var(--km-color-text-muted); font-size: var(--km-font-size-xs); }}
  .sb-tabs {{ margin-left: var(--km-space-m); }}
  .sb-tabs .km-segmented__btn {{ display: inline-flex; align-items: center; gap: var(--km-space-icon-text); height: calc(1.3 * var(--km-monogram-size)); }} /* so hoch wie das Logo daneben */
  .sb-tabs .km-segmented__btn > .km-icon {{ width: var(--km-icon-s); height: var(--km-icon-s); }}
  .sb-steuer {{ display: flex; flex-wrap: wrap; align-items: center; gap: var(--km-space-s) var(--km-space-m); margin-left: auto; }}
  .sb-steuer label {{ display: flex; align-items: center; gap: var(--km-space-icon-text); font-size: var(--km-font-size-xs); color: var(--km-color-text-muted); }}
  .sb-steuer select {{ font: inherit; font-size: var(--km-font-size-xs); color: var(--km-color-text); background: var(--km-color-card); border: var(--km-border-width) solid var(--km-color-border-input); padding: var(--km-space-2xs) var(--km-space-xs); border-radius: 0; }}
  .km-segmented__btn {{ font-size: var(--km-font-size-xs); padding: var(--km-space-2xs) var(--km-space-s); }}
  .sb-steuer select:focus-visible, .km-segmented__btn:focus-visible {{ outline: none; box-shadow: 0 0 0 var(--km-border-width-strong) var(--km-color-page), 0 0 0 calc(2 * var(--km-border-width-strong)) var(--km-color-focus); }}
  body:not([data-tab="storybook"]) .sb-haupt {{ display: none; }}
  body:not([data-tab="prototyp"]) .sb-proto:not(.sb-ents) {{ display: none; }}
  body:not([data-tab="entscheidungen"]) .sb-ents {{ display: none; }} /* Reiter „Entscheidungen“: Review-Seite aus tools/build-entscheidungen.py */
  .sb-proto {{ min-height: 0; display: grid; }}
  .sb-proto {{ justify-items: center; background: var(--km-color-section); }}
  .sb-proto iframe {{ border: 0; width: 100%; height: 100%; background: var(--km-color-page); }}
  .sb-proto iframe[data-breite]:not([data-breite="voll"]) {{ border-left: var(--km-border-width) solid var(--km-color-border-card); border-right: var(--km-border-width) solid var(--km-color-border-card); }}
  /* Kopf: Logo links, Tabs mittig, Steuerung rechts; alle Bedienelemente so hoch wie das Logo, mit Icons */
  .sb-kopf {{ display: grid; grid-template-columns: minmax(0, 1fr) auto minmax(0, 1fr); align-items: center; }}
  .sb-tabs {{ justify-self: center; margin-left: 0; }}
  .sb-steuer {{ justify-self: end; flex-wrap: nowrap; margin-left: 0; }}
  .sb-steuer .km-segmented__btn, .sb-steuer select {{ height: calc(1.3 * var(--km-monogram-size)); box-sizing: border-box; }}
  .sb-steuer .km-segmented__btn, .sb-tabs .km-segmented__btn {{ display: inline-flex; align-items: center; gap: var(--km-space-icon-text); }}
  .sb-steuer .km-icon {{ width: var(--km-icon-s); height: var(--km-icon-s); flex: none; }}
  .sb-select {{ position: relative; }}
  .sb-select > .km-icon:last-child {{ left: auto; right: var(--km-space-s); }} /* eigener Pfeil, gleicher Abstand wie das Icon links */
  .sb-select > .km-icon {{ position: absolute; left: var(--km-space-s); top: 50%; transform: translateY(-50%); pointer-events: none; color: var(--km-color-text-muted); }} /* Icon im Feld, wie bei den Knöpfen links */
  .sb-steuer .sb-select select {{ appearance: none; font-weight: var(--km-font-weight-regular); -webkit-appearance: none; padding: 0 calc(var(--km-space-s) + var(--km-icon-s) + var(--km-space-xs)); font-size: var(--km-font-size-xs); line-height: calc(1.3 * var(--km-monogram-size) - 2 * var(--km-border-width)); }} /* Text in jedem Browser mittig, gleiche Größe wie die Knöpfe */
  @media (max-width: 1180px) {{ .sb-kopf {{ grid-template-columns: minmax(0, 1fr) auto; }} .sb-steuer {{ grid-column: 1 / -1; justify-self: start; flex-wrap: wrap; }} }}
  .sb-haupt {{ display: grid; grid-template-columns: clamp(17rem, 30vw, 27rem) minmax(0, 1fr); min-height: 0; }}
  .sb-nav {{ overflow-y: auto; padding: var(--km-space-m) var(--km-space-m) var(--km-space-m) var(--km-space-page); background: var(--km-color-section); border-right: var(--km-border-width) solid var(--km-color-border-card); }}
  .sb-top {{ display: flex; align-items: center; gap: var(--km-space-xs); }} .sb-top > .km-searchbox {{ flex: 1 1 auto; min-width: 0; }} /* Suche ganz oben, Einklapp-Knopf daneben (wie Entscheidungen) */
  /* Navigation: Kit-Baustein Seitenleiste mit Baum (km-sidebar__group--tree, 0.15.0), keine eigenen Regeln für Auswahl, Hover, Einzug oder Icons */
  @media (min-width: 861px) {{ .sb-haupt.sb-zu {{ grid-template-columns: auto minmax(0, 1fr); }} }} /* eingeklappt bekommt der Inhalt die Breite; schmal bleibt eine Spalte, die Leiste steht oben */
  @media (min-width: 861px) {{ .sb-nav.km-sidebar--rail {{ width: calc(var(--km-component-sidebar-rail-width) + var(--km-sidebar-inset)); padding-inline: var(--km-sidebar-inset) 0; }} }} /* eingeklappt so breit wie die Leiste im Prototyp */
  @media (max-width: 860px) {{ .sb-nav.km-sidebar--rail {{ flex-direction: row; flex-wrap: wrap; }} }} /* schmal steht die Leiste oben: eingeklappt eine Zeile mit Knopf und Icons */
  /* Doku je Story im Aufbau D: vier Kapitel mit Kapitelleiste (km-chapters), nichts aufklappbar; KERN-Bausteine verweisen auf die KERN-Doku */
  .sb-markup {{ max-height: 40vh; overflow: auto; }}
  /* Startseite (Story „Einführung“, 0.9.0): ganze Seite aus tools/einfuehrung.py, ohne Bühne und Markup */
  .sb-inhalt--seite {{ background: var(--km-color-page); padding: var(--km-space-xl) var(--km-space-page) var(--km-space-2xl); }}
  .sb-inhalt--seite > :not(#seite), .sb-inhalt:not(.sb-inhalt--seite) > #seite {{ display: none !important; }}
  .sb-kern {{ display: flex; flex-wrap: wrap; align-items: center; gap: var(--km-space-xs); margin: 0; font-size: var(--km-font-size-xs); color: var(--km-color-text-muted); }}
  .sb-kern .km-chip {{ gap: var(--km-space-2xs); }}
  .sb-kern .km-chip > .km-icon {{ width: var(--km-icon-xs); height: var(--km-icon-xs); }}
  .sb-nav, .sb-inhalt, .sb-titel {{ min-width: 0; }}
  .sb-zweck, .sb-marke small {{ overflow-wrap: anywhere; }}
  .sb-inhalt {{ display: grid; background: var(--km-color-section); grid-auto-rows: max-content; align-content: start; min-height: 0; padding: var(--km-space-l) var(--km-space-xl); gap: var(--km-space-block); }}
  .sb-titel {{ display: grid; gap: var(--km-space-xs); }}
  .sb-pfad.km-hero__kicker {{ margin: 0; }} /* Kopf der Story wie km-hero im Dashboard */
  .sb-titel .km-hero__title {{ margin: 0; max-width: none; }}
  .sb-zweck {{ margin: 0; max-width: var(--km-metric-measure-default); font-size: var(--km-typography-font-size-body); color: var(--km-color-text-muted); line-height: var(--km-typography-line-height-body); display: grid; gap: var(--km-space-xs); }}
  .sb-zweck p {{ margin: 0; }}
  .sb-zweck + .sb-bezug {{ margin-top: var(--km-space-s); padding-top: var(--km-space-m); border-top: var(--km-border-width) solid var(--km-color-border-card); }} /* Optionen klar vom Einleitungstext getrennt */
  .sb-zweck + .sb-bezug:empty {{ display: none; }}
  .sb-bezug {{ display: grid !important; gap: var(--km-space-xs) !important; margin: 0; }}
  .sb-bezug:empty {{ display: none !important; }} /* leere Liste ohne Trennlinie, sonst zwei Striche ohne Inhalt */
  .sb-zeile {{ display: grid; grid-template-columns: 7rem minmax(0, 1fr); gap: var(--km-space-m); align-items: baseline; }}
  .sb-zeile dt {{ margin: 0; font-size: var(--km-font-size-xs); font-weight: var(--km-font-weight-strong); letter-spacing: var(--km-tracking-caps); text-transform: uppercase; color: var(--km-color-text-muted); }}
  .sb-zeile dd {{ margin: 0; display: flex; flex-wrap: wrap; gap: var(--km-space-2xs) var(--km-space-xs); }}
  .sb-kontrast {{ padding-left: calc(7rem + var(--km-space-m)); }} /* Kontrastzeile fluchtet mit den Chips */
  .sb-zweck + .sb-bezug:empty + .sb-bezug {{ margin-top: var(--km-space-s); padding-top: var(--km-space-m); border-top: var(--km-border-width) solid var(--km-color-border-card); }}

  .sb-zweck code, .sb-bezug code {{ font-family: var(--km-font-mono); font-size: 0.9em; }}
  .sb-zweck .hinweis {{ display: flex; align-items: center; gap: var(--km-space-icon-text); color: var(--km-color-attention); }} /* Icon statt Schriftzeichen ⚠ (0.13.0) */
  .sb-bezug {{ display: flex; flex-wrap: wrap; align-items: center; gap: var(--km-space-2xs) var(--km-space-xs); margin: 0; font-size: var(--km-font-size-xs); color: var(--km-color-text-muted); }}
  .sb-bezug b {{ font-weight: var(--km-font-weight-strong); margin-right: var(--km-space-3xs); }}
  .sb-bezug b:not(:first-child) {{ margin-left: var(--km-space-s); }}
  .sb-kontrast {{ margin: 0; font-size: var(--km-font-size-xs); display: flex; align-items: center; gap: var(--km-space-xs); }}
  .sb-kontrast button {{ font: inherit; background: none; border: var(--km-border-width) solid currentColor; color: inherit; padding: 0 var(--km-space-xs); cursor: pointer; }}
  .sb-buehne {{ overflow: auto; background: var(--km-color-card); border: var(--km-border-width) solid var(--km-color-border-card); box-shadow: var(--km-shadow); display: flex; justify-content: center; }}
  .sb-buehne iframe {{ border: 0; width: 100%; height: 100%; min-height: 20rem; background: transparent; }}
  .sb-inhalt {{ overflow-y: auto; }} .sb-buehne {{ min-height: 16rem; }} .sb-buehne iframe {{ min-height: 16rem; }} /* Bühne so hoch wie die Story (höchstens 75 % des Fensters), darunter folgt die Doku */ /* langer Kopf mit offener Doku: der Inhalt scrollt, die Bühne bleibt mindestens 24rem hoch (2026-11-09) */
  @media (max-width: 860px) {{ .sb-kopf {{ grid-template-columns: minmax(0, 1fr); }} .sb-tabs, .sb-steuer {{ justify-self: start; flex-wrap: wrap; }} .sb-steuer {{ grid-column: auto; }} }} /* schmal: Logo, Reiter, Steuerung untereinander, nichts ragt über 390 px hinaus */
  @media (max-width: 860px) {{ .sb-haupt {{ grid-template-columns: minmax(0, 1fr); grid-template-rows: auto minmax(0, 1fr); }} .sb-nav {{ max-height: 30vh; border-right: 0; border-bottom: var(--km-border-width) solid var(--km-color-border-card); }} .sb-inhalt {{ padding: var(--km-space-m); }} .sb-tabs {{ margin-left: 0; }} .sb-steuer {{ margin-left: 0; }} .sb-steuer label {{ flex-wrap: wrap; }} }}
</style>
</head>
<body>
<header class="sb-kopf">
  <a class="sb-marke" id="sb-start" href="#" title="Zur Startseite dieses Bereichs"><span class="km-monogram" aria-hidden="true">Km</span><div><h1>Kernmix</h1><small>Ein Remix von KERN · {VERSION} · KERN {KERN}</small></div></a>
  <nav class="km-segmented sb-tabs" id="tab" aria-label="Ansicht"><button type="button" class="km-segmented__btn" data-v="storybook">{ikon("blocks")}Komponenten</button><button type="button" class="km-segmented__btn" data-v="prototyp">{ikon("monitor")}Prototyp</button></nav>
  <div class="sb-steuer">
    <label class="sb-select" title="Theme">{ikon("palette")}<span class="kern-sr-only">Theme</span><select id="theme"></select>{ikon("chevron-down")}</label>
    <span class="km-segmented" id="modus" role="group" aria-label="Modus"><button type="button" class="km-segmented__btn" data-v="dark">{ikon("moon")}Dunkel</button><button type="button" class="km-segmented__btn" data-v="light">{ikon("sun")}Hell</button></span>
    
  </div>
</header>
<div class="sb-haupt">
  <nav class="sb-nav km-sidebar" id="sb-nav" aria-label="Stories"><div class="sb-top"><span class="km-searchbox">{ikon("search")}<input id="suche" type="search" placeholder="Stories filtern …" aria-label="Stories filtern"></span><button type="button" class="km-sidebar__toggle" id="sb-collapse" aria-expanded="true" aria-controls="sb-nav" title="Navigation ein-/ausklappen">{ikon("chevron-left")}</button></div></nav>
  <main class="sb-inhalt">
    <div class="km-chapters">
      <div class="km-doc km-chapters__main">
        <div class="sb-titel km-hero km-hero--display"><p class="sb-pfad km-hero__kicker" id="pfad"></p><h2 class="km-hero__title" id="titel"></h2><div class="sb-zweck" id="meta"></div><dl class="km-facts km-facts--cols" id="fakten" aria-live="polite"></dl></div>
        <div id="offen" hidden></div>
        {_SEK}
      </div>
      {_NAV}
    </div>
    <div id="seite"></div>
    <button type="button" class="km-totop" id="nach-oben" aria-label="Nach oben" title="Nach oben">{ikon("arrow-up")}</button>
  </main>
</div>
<div class="sb-proto"><iframe id="proto" title="Prototyp: Project Dashboard im Demo-Modus" data-src="../prototyp/index.html"></iframe></div>
<script id="daten" type="application/json">{daten}</script>
<script>
(function(){{
  var D = JSON.parse(document.getElementById('daten').textContent), S = D.stories;
  var st = {{ tab: 'storybook', story: S[0].id, theme: 'kern-nah', modus: 'dark', breite: 'voll' }};
  location.hash.replace(/^#/, '').split('&').forEach(function(p){{ var kv = p.split('='); if (kv[0] in st && kv[1]) st[kv[0]] = decodeURIComponent(kv[1]); }});
  if (!D.themes.some(function(t){{ return t.id === st.theme; }})) st.theme = D.themes[0].id;
  if (!S.some(function(s){{ return s.id === st.story; }})) st.story = st.story.replace('-kd-', '-km-');  /* Adressen von vor 0.7.0 (Präfix kd-) führen weiter zur Story */
  window.addEventListener('hashchange', function(){{ var vor = st.story; location.hash.replace(/^#/, '').split('&').forEach(function(p){{ var kv = p.split('='); if (kv[0] in st && kv[1]) st[kv[0]] = decodeURIComponent(kv[1]); }}); if (typeof zeigen === 'function') zeigen(); }});  /* Links auf #story=… innerhalb der Seite (z. B. „Changelog“ unten links) */
  var sel = document.getElementById('theme');
  D.themes.forEach(function(t){{ var o = document.createElement('option'); o.value = t.id; o.textContent = t.name; sel.appendChild(o); }});
  function esc(s){{ return s.replace(/[&<>"]/g, function(c){{ return {{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}}[c]; }}); }}
  // Navigation: Gruppe > Pfad > Story, Kit-Baustein Seitenleiste als Baum (km-sidebar__group--tree, 0.15.0)
  var baum = document.getElementById('sb-nav'), ende = baum.querySelector('.sb-top').nextElementSibling, gruppen = {{}};  /* Gruppen vor Rechtlichem bzw. „Download und Quellen“ (online) */
  S.forEach(function(s){{ (gruppen[s.gruppe] = gruppen[s.gruppe] || {{}}); (gruppen[s.gruppe][s.pfad] = gruppen[s.gruppe][s.pfad] || []).push(s); }});
  var GI = {{ 'Grundlagen': '{ikon("book-open").replace("'", "&#39;")}', 'Erweiterungen': '{ikon("blocks").replace("'", "&#39;")}', 'Proposals': '{ikon("lightbulb").replace("'", "&#39;")}', 'KERN-Standard': '{ikon("package").replace("'", "&#39;")}' }};
  var CARET = '<span class="km-sidebar__caret" aria-hidden="true"></span>';
  function labelBtn(id, ic, text, n, zu){{ return '<p class="km-sidebar__label"><button type="button" class="km-sidebar__label-btn" aria-expanded="' + !zu + '" aria-controls="' + id + '" title="' + esc(text) + ' ein- oder ausklappen">' + ic + '<span>' + esc(text) + '</span>' + CARET + '<span class="km-sidebar__count">' + n + '</span></button></p>'; }}
  ['Grundlagen', 'Erweiterungen', 'Proposals', 'KERN-Standard'].forEach(function(g, gi){{
    if (!gruppen[g]) return;
    var zu = g === 'KERN-Standard', n = 0, innen = '', pfade = Object.keys(gruppen[g]), flach = pfade.length === 1;  /* KERN-Standard beim Laden eingeklappt; Gruppe mit nur einem Pfad wird aufgelöst, der Pfad steht oben */
    pfade.forEach(function(p, pi){{
      var l = gruppen[g][p]; n += l.length;
      innen += (flach ? '' : labelBtn('sb-p' + gi + '-' + pi, l[0].icon.replace('km-sidebar__icon', ''), p, l.length, zu) + '<div class="km-sidebar__list" id="sb-p' + gi + '-' + pi + '"' + (zu ? ' hidden' : '') + '>') + l.map(function(s){{
        return '<a class="km-sidebar__item" href="#story=' + s.id + '" data-id="' + s.id + '" title="' + esc(s.name) + '" data-such="' + esc((g + ' ' + p + ' ' + s.name).toLowerCase()) + '">' + s.icon + '<span class="km-sidebar__text">' + esc(s.name) + '</span>' + (s.fehlt.length ? '<span class="km-sidebar__warn" title="Klassen fehlen in KERN {KERN}" aria-label="Klassen fehlen in KERN {KERN}">{ikon("triangle-alert").replace("'", "&#39;")}</span>' : '') + '</a>';
      }}).join('') + (flach ? '' : '</div>');
    }});
    (ende || baum).insertAdjacentHTML(ende ? 'beforebegin' : 'beforeend', '<div class="km-sidebar__group km-sidebar__group--tree' + (flach ? ' km-sidebar__group--flach' : '') + '">' + labelBtn('sb-g' + gi, GI[g] || '', flach ? pfade[0] : g, n, zu) + '<div class="km-sidebar__list" id="sb-g' + gi + '"' + (zu ? ' hidden' : '') + '>' + innen + '</div></div>');
  }});
  function auf(btn, offen){{ var l = document.getElementById(btn.getAttribute('aria-controls')); if (l) l.hidden = !offen; btn.setAttribute('aria-expanded', String(offen)); }}
  function aufZu(el){{ for (var l = el.closest('.km-sidebar__list'); l; l = l.parentNode.closest('.km-sidebar__list')){{ var b = baum.querySelector('[aria-controls="' + l.id + '"]'); if (b) auf(b, true); }} }}  /* Gruppe und Pfad eines Eintrags aufklappen */
  baum.addEventListener('click', function(ev){{ var t = ev.target.closest('.km-sidebar__label-btn'); if (!t) return; if (baum.classList.contains('km-sidebar--rail')){{ document.getElementById('sb-collapse').click(); auf(t, true); return; }} auf(t, t.getAttribute('aria-expanded') !== 'true'); }});  /* eingeklappt: Icon der Gruppe klappt die Leiste auf und öffnet die Gruppe */
  (function(){{ var col = document.getElementById('sb-collapse'), P = 'kernmix-storybook:v1:nav-zu';  /* Einklappen wie Dashboard, Lagebild, Entscheidungen; Zustand in localStorage */
    function setz(zu, merken){{ baum.parentNode.classList.toggle('sb-zu', zu); baum.classList.toggle('km-sidebar--rail', zu); col.setAttribute('aria-expanded', zu ? 'false' : 'true'); if (merken) try {{ localStorage.setItem(P, zu ? '1' : '0'); }} catch (x){{}} }}
    col.addEventListener('click', function(){{ setz(!baum.classList.contains('km-sidebar--rail'), true); }});
    try {{ setz(localStorage.getItem(P) === '1', false); }} catch (x){{}} }})();
  document.getElementById('suche').addEventListener('input', function(e){{
    var q = e.target.value.trim().toLowerCase();
    baum.querySelectorAll('a[data-id]').forEach(function(a){{ a.hidden = q && a.dataset.such.indexOf(q) < 0; }});
    baum.querySelectorAll('.km-sidebar__group--tree .km-sidebar__list').forEach(function(l){{ var b = baum.querySelector('[aria-controls="' + l.id + '"]'), sichtbar = !!l.querySelector('a[data-id]:not([hidden])'); b.closest('.km-sidebar__label').hidden = !sichtbar; if (!sichtbar) auf(b, false); else if (q) auf(b, true); }});
    baum.querySelectorAll('.km-sidebar__group--tree').forEach(function(g){{ g.hidden = !g.querySelector('a[data-id]:not([hidden])'); }});
  }});
  document.querySelector('.km-chapters__main').addEventListener('click', function(e){{
    var cp = e.target.closest('[data-copy]'); if (cp){{ var q = document.getElementById(cp.dataset.copy); if (q && navigator.clipboard) navigator.clipboard.writeText(q.textContent); cp.setAttribute('title', 'Kopiert'); return; }}
    var en = e.target.closest('a[data-ent]'); if (en){{ e.preventDefault(); st.tab = 'entscheidungen'; zeigen(); var f = document.getElementById('ents'); f.setAttribute('src', f.getAttribute('src').split('#')[0] + '#E' + en.dataset.ent); return; }}  /* Entscheidung im Reiter „Entscheidungen“ öffnen */
    var kb = e.target.closest('[data-kopieren]'); if (kb){{ var tr = kb.closest('tr'), ths = [].slice.call(tr.closest('table').tHead.rows[0].cells), ki = ths.findIndex(function(th){{ return /^(Klasse|Klassen|Token|Tokens|Kit-Token|KERN-Token|Modifier)$/i.test(th.textContent.trim()); }});
      var w = ki >= 0 ? tr.cells[ki].textContent.trim() : ''; if (w && navigator.clipboard) navigator.clipboard.writeText(w); kb.setAttribute('title', 'Kopiert: ' + w); return; }}  /* Kennung erst beim Klick aus der Zeile lesen */
    var a = e.target.closest('a[data-id]'); if (!a) return; e.preventDefault(); st.story = a.dataset.id; zeigen(); }});
  baum.addEventListener('click', function(e){{ var a = e.target.closest('a[data-id]'); if (!a) return; e.preventDefault(); st.story = a.dataset.id; zeigen(); }});
  sel.addEventListener('change', function(){{ st.theme = sel.value; zeigen(); }});
  var scroll = {{}};  /* Scrollstand von Navigation und Inhalt je Tab merken */
  document.getElementById('tab').addEventListener('click', function(){{ ['.sb-nav', '.sb-inhalt'].forEach(function(s){{ var e = document.querySelector(s); if (e && e.offsetParent) scroll[s] = e.scrollTop; }}); }}, true);
  function scrollZurueck(){{ if (st.tab !== 'storybook') return; requestAnimationFrame(function(){{ ['.sb-nav', '.sb-inhalt'].forEach(function(s){{ var e = document.querySelector(s); if (e && scroll[s] != null) e.scrollTop = scroll[s]; }}); }}); }}
  ['tab', 'modus'].forEach(function(k){{ document.getElementById(k).addEventListener('click', function(e){{ var b = e.target.closest('button'); if (!b) return; st[k] = b.dataset.v; zeigen(); }}); }});
  document.getElementById('kopie').addEventListener('click', function(e){{ e.preventDefault(); var s = S.find(function(x){{ return x.id === st.story; }}); navigator.clipboard && navigator.clipboard.writeText(s.html); this.setAttribute('title', 'Kopiert'); }});
  /* Prototyp folgt Theme, Modus und Breite des Kopfs */
  /* Prototyp folgt Theme, Modus und Breite des Kopfs; Theme und Modus über die Adresse des Prototyps, der sie vor dem Zeichnen setzt */
  document.getElementById('sb-start').addEventListener('click', function(e){{ e.preventDefault();
    if (st.tab === 'storybook'){{ st.story = S[0].id; zeigen(); var z = document.querySelector('.sb-inhalt'); if (z) z.scrollTo({{ top: 0, behavior: 'instant' }}); }}
    else {{ var f = document.querySelector(st.tab === 'prototyp' ? '#proto' : '#ents'); try {{ f.contentWindow.scrollTo({{ top: 0, behavior: 'instant' }}); var m = f.contentDocument && f.contentDocument.getElementById('main-col'); if (m) m.scrollTo({{ top: 0, behavior: 'instant' }}); }} catch (x){{}} }} }});
  function protoSync(){{
    var pr = document.getElementById('proto'); if (!pr) return;
    pr.dataset.breite = st.breite; pr.style.maxWidth = st.breite === 'voll' ? '' : st.breite + 'px';
    if (st.tab === 'storybook') return;
    var m = st.modus === 'light' ? 'light' : 'dark', th = D.themes.find(function(t){{ return t.id === st.theme; }});
    var ziel = pr.dataset.src + '?modus=' + m + '&theme=' + (th && th.css.length ? th.id : '');  /* Suchparameter statt #: nur so lädt der Prototyp wirklich neu */
    if (pr.getAttribute('src') !== ziel) pr.setAttribute('src', ziel);
    var en = document.getElementById('ents'); if (en && st.tab === 'entscheidungen'){{ var ez = en.dataset.src + '?modus=' + m + '&theme=' + (th && th.css.length ? th.id : ''); if (en.getAttribute('src') !== ez) en.setAttribute('src', ez); }}
  }}
  var kontrastZuletzt = '';
  function zeigen(){{
    var s = S.find(function(x){{ return x.id === st.story; }}) || S[0], th = D.themes.find(function(t){{ return t.id === st.theme; }});
    sel.value = th.id;
    var ht = document.getElementById('huelle-theme'); if (th.css.length) {{ ht.disabled = false; ht.href = th.css[0]; }} else ht.disabled = true;
    ['tab', 'modus'].forEach(function(k){{ document.querySelectorAll('#' + k + ' button').forEach(function(b){{ b.setAttribute('aria-pressed', String(b.dataset.v === st[k])); }}); }});
    baum.querySelectorAll('a[data-id][aria-current]').forEach(function(a){{ a.removeAttribute('aria-current'); }});
    var a = baum.querySelector('a[data-id="' + s.id + '"]'); if (a){{ a.setAttribute('aria-current', 'page'); aufZu(a); }}
    document.body.dataset.tab = st.tab; var pr = document.getElementById('proto'); protoSync(); if (st.tab !== window.sbLetzterTab) scrollZurueck(); window.sbLetzterTab = st.tab;  /* Scroll nur beim Reiterwechsel zurückholen, eine Auswahl in der Leiste lässt alles an seiner Stelle */
    var inh = document.querySelector('.sb-inhalt'), sei = document.getElementById('seite');  /* Startseite: ganze Seite statt Bühne (0.9.0) */
    inh.classList.toggle('sb-inhalt--seite', !!s.seite);
    if (s.seite){{ if (sei.dataset.id !== s.id){{ sei.innerHTML = s.html; sei.dataset.id = s.id; }} if (st.modus === 'system') document.documentElement.removeAttribute('data-kern-theme'); else document.documentElement.setAttribute('data-kern-theme', st.modus); document.getElementById('buehne').dataset.key = ''; history.replaceState(null, '', '#' + Object.keys(st).map(function(k){{ return k + '=' + encodeURIComponent(st[k]); }}).join('&')); return; }}
    document.getElementById('pfad').textContent = Object.keys(gruppen[s.gruppe] || {{}}).length === 1 ? s.pfad : s.gruppe + ' · ' + s.pfad;  /* aufgelöste Gruppe: nur der Pfad */
    document.getElementById('titel').textContent = s.name;
    /* Kopf wie die Einführung (0.11.0): Titel, Zweck als km-lead, Fakten als Kacheln; darunter Bühne, dann Rubriken als Karten im Raster (Paare nebeneinander), Markup */
    var ds = s.doku || [], x0 = ds.length && D.dokus[ds[0]], g = s.gliederung;
    var fakt = function(ic, l, w, lang, sp){{ return '<div class="km-fact' + (sp > 1 ? ' km-fact--span-' + sp : '') + '"><dt class="km-fact__label">' + ic + l + '</dt><dd class="km-fact__value' + (lang ? ' km-fact__value--long' : '') + '">' + w + '</dd></div>'; }};
    var chip = function(l){{ return l.map(function(x){{ return '<a class="km-chip" href="#" data-id="' + x[0] + '">' + esc(x[1]) + '</a>'; }}).join(' '); }};
    var lead = s.kern ? 'Offizielle Story aus dem KERN-Repository, Markup unverändert. Jede Klasse ist gegen das eingebettete Kit KERN {KERN} geprüft.' : x0 ? x0.lead : (g ? g[0] : esc(s.zweck || ''));
    document.getElementById('meta').innerHTML = (lead ? '<p class="km-lead">' + lead + '</p>' : '') +  (s.fehlt.length ? '<p class="hinweis">{ikon("triangle-alert")}nicht in KERN {KERN}: ' + esc(s.fehlt.join(', ')) + '</p>' : '');
    document.getElementById('fakten').innerHTML = s.kern
      ? fakt('{ikon("package")}', 'Quelle', 'KERN-Standard<small>' + esc(s.pfad) + '</small>') + fakt('{ikon("shield-check")}', 'Kit', 'KERN {KERN}<small>' + (s.fehlt.length ? s.fehlt.length + ' Klassen fehlen' : 'alle Klassen vorhanden') + '</small>') + '<div class="km-fact" id="kontrast"></div>'
        + fakt('{ikon("book-open")}', 'KERN-Doku', '<a class="km-link" href="' + esc(s.kern[0]) + '" target="_blank" rel="noopener">Code</a> · <a class="km-link" href="' + esc(s.kern[1]) + '" target="_blank" rel="noopener">kern-ux.de</a>', true)
      : x0 ? x0.fakten : fakt('{ikon("file-code")}', 'Quelle', '<code>' + esc(s.quelle) + '</code>', true, 2) + '<div class="km-fact km-fact--span-2" id="kontrast"></div>';
    document.getElementById('kontrast').innerHTML = kontrastZuletzt;  /* Messung der Vorschau als Kachel; neu gemessen, wenn sich Story, Theme oder Modus ändern */
    var karte = function(ic, titel, inhalt, breit){{ return '<article class="km-card km-card--accent-top' + (breit ? ' km-card--span' : '') + '"><div class="km-card__head"><span class="km-card__tile">' + ic + '</span><h4 class="km-card__title">' + titel + '</h4></div><div class="km-prose">' + inhalt + '</div></article>'; }};
    var weitere = ds.slice(1).filter(function(d){{ return D.dokus[d] && D.dokuheim[d] && D.dokuheim[d] !== s.id; }}).map(function(d){{ return [D.dokuheim[d], D.dokus[d].titel]; }});
    /* Zusammenhang kompakt als Angabenliste (km-deflist): je Zeile Bezeichnung und Chips */
    var zeile = function(l, w){{ return '<div><dt>' + l + '</dt><dd class="km-chips">' + w + '</dd></div>'; }};
    var zus = [['Enthält', s.enthaelt], ['Verwendet in', s.verwendet], ['Weitere Doku', weitere]].filter(function(x){{ return x[1] && x[1].length; }}).map(function(x){{ return zeile(x[0], chip(x[1])); }}).join('')
      + (g && g[2].length ? zeile('Klassen der Story', g[2].map(function(k){{ return '<code class="km-chip km-chip--muted">' + esc(k) + '</code>'; }}).join(' ')) : '')
      + (x0 ? zeile('Quelle der Story', '<code class="km-chip km-chip--muted">' + esc(s.quelle) + '</code>') : '');
    var ueber = x0 && x0.mehr.length ? karte('{ikon("info")}', 'Überblick', '<ul>' + x0.mehr.map(function(x){{ return '<li>' + x + '</li>'; }}).join('') + '</ul>') : '';
    var inStory = x0 && s.punkte && s.punkte.length ? karte('{ikon("eye")}', 'In dieser Story', '<ul>' + s.punkte.map(function(x){{ return '<li>' + x + '</li>'; }}).join('') + '</ul>') : '';
    var zusKarte = s.gruppe === 'Erweiterungen' && zus ? karte('{ikon("network")}', 'Zusammenhang', zus, true).replace('<div class="km-prose">', '<dl class="km-deflist">').replace(/<.div><.article>$/, '</dl></article>') : '';
    /* Aufbau D: offene Punkte oben, vier Kapitel mit Karten im Raster und „Regel:“ am Ende; leere Kapitel (ohne Doku) fallen samt Eintrag in der Kapitelleiste weg */
    var of = document.getElementById('offen'); of.innerHTML = x0 ? x0.offen : ''; of.hidden = !of.innerHTML;
    var vorn = {{ was: ueber + inStory, wann: zusKarte, wie: '', pruefen: '' }};
    ['was', 'wann', 'wie', 'pruefen'].forEach(function(k){{
      var gr = document.getElementById('kap-' + k + '-karten'), rg = document.getElementById('kap-' + k + '-regel');
      gr.innerHTML = vorn[k] + (x0 ? x0.kapitel[k] : ''); gr.hidden = !gr.children.length;
      rg.innerHTML = x0 && x0.regeln[k] || ''; rg.hidden = !rg.innerHTML;
      /* Paare: eine halbe Karte ohne Partner geht über die ganze Zeile, damit die Paare darunter nebeneinander bleiben */
      var lauf = []; [].concat([].slice.call(gr.children), [null]).forEach(function(c){{ if (c && !c.classList.contains('km-card--span')){{ lauf.push(c); return; }} if (lauf.length % 2) lauf[lauf.length - 1].classList.add('km-card--span'); lauf = []; }});
      var leer = gr.hidden && rg.hidden && k !== 'was' && k !== 'wie';
      document.getElementById('kap-' + k).hidden = leer; document.querySelector('.km-chapters__nav a[href="#kap-' + k + '"]').hidden = leer;
      if (window.kmTabelle) [].forEach.call(gr.querySelectorAll('table.km-table'), function(t){{ window.kmTabelle(t); }});  /* Doku-Tabellen aus Markdown: Rollen und Kopf-Icons wie überall */
    }});
    /* Nur vorhandene Kapitel, fortlaufend nummeriert (KERN-Stories und Grundlagen ohne Doku: Beispiel und Markup als 1 und 2) */
    var nr = 0; ['was', 'wann', 'wie', 'pruefen'].forEach(function(k){{ var sk = document.getElementById('kap-' + k); if (sk.hidden) return; nr++;
      [sk.querySelector('.km-doc__title > span'), document.querySelector('.km-chapters__nav a[href="#kap-' + k + '"] > span')].forEach(function(e){{ e.textContent = e.textContent.replace(/^\\d+/, nr); }}); }});
    if (window.kmKapitel) window.kmKapitel();
    document.getElementById('code').textContent = s.html;
    if (st.modus === 'system') document.documentElement.removeAttribute('data-kern-theme'); else document.documentElement.setAttribute('data-kern-theme', st.modus);  // ganze Seite, nicht nur die Vorschau
    var modus = st.modus === 'system' ? '' : ' data-kern-theme="' + st.modus + '"';
    var css = ['../vendor/kern/kern.min.css', '../vendor/kern/fonts/fira-sans.css', '../dist/fonts.css', '../dist/km.css'].concat(th.css).map(function(h){{ return '<link rel="stylesheet" href="' + h + '">'; }}).join('') + '<script src="../dist/km-popup.js"><\\/script>';
    var f = document.getElementById('buehne');
    f.style.maxWidth = st.breite === 'voll' ? '' : st.breite + 'px';
    var key = s.id + '|' + st.theme + '|' + st.modus; if (f.dataset.key === key) {{ history.replaceState(null, '', '#' + Object.keys(st).map(function(k){{ return k + '=' + encodeURIComponent(st[k]); }}).join('&')); return; }} f.dataset.key = key; kontrastZuletzt = ''; document.getElementById('kontrast').innerHTML = '';  /* Tab-Wechsel zeichnet die Vorschau nicht neu, Zustand bleibt */
    f.onload = function(){{ pruefen(f); }};
    f.srcdoc = '<!doctype html><html lang="de"' + modus + '><head><meta charset="utf-8"><base href="' + location.href.replace(/[^\\/]*$/, '') + '">' + css + D.interaktion + '<style>body{{margin:0;padding:24px;background:var(--kern-color-layout-background-default);color:var(--kern-color-layout-text-default);font-family:var(--kern-typography-font-family-default)}}</style></head><body>' + s.html + '</body></html>';
    history.replaceState(null, '', '#' + Object.keys(st).map(function(k){{ return k + '=' + encodeURIComponent(st[k]); }}).join('&'));
  }}
  // Kontrast: jede sichtbare Textstelle gegen ihren tatsächlichen Hintergrund (erstes deckendes Elternelement), WCAG 2.1
  // Farben über ein Canvas in sRGB umrechnen: KERN liefert oklch(), das lässt sich nicht als Zahlenliste lesen
  var cx = document.createElement('canvas').getContext('2d', {{ willReadFrequently: true }});
  function rgba(s){{ if (!s || s === 'transparent') return [0,0,0,0]; cx.clearRect(0,0,1,1); cx.fillStyle = '#000'; cx.fillStyle = s; cx.fillRect(0,0,1,1); var d = cx.getImageData(0,0,1,1).data; return [d[0], d[1], d[2], d[3] / 255]; }}
  function lum(c){{ return [0,1,2].map(function(i){{ var v = c[i] / 255; return v <= .03928 ? v / 12.92 : Math.pow((v + .055) / 1.055, 2.4); }}).reduce(function(s, v, i){{ return s + v * [.2126, .7152, .0722][i]; }}, 0); }}
  function kr(a, b){{ var x = lum(a), y = lum(b); return (Math.max(x, y) + .05) / (Math.min(x, y) + .05); }}
  function grund(el, w){{ for (var e = el; e; e = e.parentElement){{ var c = rgba(w.getComputedStyle(e).backgroundColor); if (c[3] > .5) return c; }} return rgba(w.getComputedStyle(w.document.documentElement).backgroundColor || 'rgb(255,255,255)'); }}
  function pruefen(f){{
    var w = f.contentWindow, d = f.contentDocument; if (!d || !d.body) return;
    var hoehe = function(){{ f.style.height = Math.round(Math.min(Math.max(d.body.scrollHeight + 2, 256), innerHeight * 0.75)) + 'px'; }};
    hoehe(); if (w.ResizeObserver) new w.ResizeObserver(hoehe).observe(d.body);
    // Hilfskästen der Beispiel-Stories (fester Hintergrund im style-Attribut) bekommen die lesbare Schrift
    d.querySelectorAll('[style*="background"]').forEach(function(el){{ var b = rgba(w.getComputedStyle(el).backgroundColor); if (b[3] < .5) return; el.style.color = kr([0,0,0], b) >= kr([255,255,255], b) ? '#111' : '#fff'; }});
    var schlecht = [];
    var it = d.createTreeWalker(d.body, NodeFilter.SHOW_TEXT, null), n;
    while ((n = it.nextNode())){{
      if (!n.data.trim()) continue; var el = n.parentElement; var cs = w.getComputedStyle(el);
      if (cs.visibility === 'hidden' || cs.display === 'none' || !el.getClientRects().length || /^(SCRIPT|STYLE|OPTION)$/.test(el.nodeName)) continue;
      var fg = rgba(cs.color); if (fg[3] < .5) continue;
      var gross = parseFloat(cs.fontSize) >= 24 || (parseFloat(cs.fontSize) >= 18.66 && +cs.fontWeight >= 700);
      var k = kr(fg, grund(el, w)); if (k < (gross ? 3 : 4.5) && schlecht.indexOf(el) < 0) schlecht.push(el);
    }}
    var box = document.getElementById('kontrast'), kopf = '<dt class="km-fact__label">{ikon("contrast")}Kontrast</dt>';
    if (!schlecht.length){{ kontrastZuletzt = kopf + '<dd class="km-fact__value">AA<small>alle Textstellen in diesem Theme und Modus</small></dd>'; if (box) {{ box.classList.remove('km-fact--danger'); box.classList.add('km-fact--ok'); box.innerHTML = kontrastZuletzt; }} return; }}
    kontrastZuletzt = kopf + '<dd class="km-fact__value">' + schlecht.length + '<small>Textstelle' + (schlecht.length > 1 ? 'n' : '') + ' unter 4,5:1 bzw. 3:1 <button type="button" class="km-link">markieren</button></small></dd>';
    if (box) {{ box.classList.remove('km-fact--ok'); box.classList.add('km-fact--danger'); box.innerHTML = kontrastZuletzt; box.querySelector('button').onclick = function(){{ schlecht.forEach(function(el){{ el.style.outline = '2px dashed #d00'; el.style.outlineOffset = '2px'; }}); schlecht[0].scrollIntoView({{ block: 'center' }}); }}; }}
  }}
  zeigen();
}})();
  (function(){{ var b = document.getElementById('nach-oben'), z = document.querySelector('.sb-inhalt'); if (!b || !z) return; function zeig(){{ b.classList.toggle('km-totop--visible', z.scrollTop > z.clientHeight * 0.8); }} z.addEventListener('scroll', zeig, {{ passive: true }}); zeig(); b.addEventListener('click', function(){{ z.scrollTo({{ top: 0, behavior: 'instant' }}); }}); }})();  /* Nach oben rechts unten, scrollt den Inhaltsbereich */
</script>
</body>
</html>
'''
(ROOT / 'storybook').mkdir(exist_ok=True)
(ROOT / 'storybook/index.html').write_text(seite, encoding='utf-8')
fehl = [s for s in stories if s['fehlt']]
print(f'storybook/index.html {len(seite) // 1024} KB · {anzahl} · {len(fehl)} Stories mit Klassen, die in KERN {KERN} fehlen')
for s in fehl[:12]:
    print('  ', s['pfad'], '/', s['name'], s['fehlt'])
