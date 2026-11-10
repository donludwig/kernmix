#!/usr/bin/env python3
"""Baut docs/index.html: Doku-Seite des Dashboard-Kits mit allen Bausteinen in beiden Themes.
Jeder Baustein steht einmal als Markup in BAUSTEINE; daraus entstehen Vorschau und Code-Beispiel, damit beide nie auseinanderlaufen.
Aufruf: python3 tools/build-doku.py (vorher tools/build.py)."""
import html, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
import sys; sys.path.insert(0, str(Path(__file__).resolve().parent))
from bausteine import BAUSTEINE, IC, i, ABSTAENDE, ABSTAND_REGELN, ABSTAND_BILD  # gemeinsame Quelle mit dem Storybook
from einfuehrung import einfuehrung_html, vorschau, karte  # Startseite: gemeinsame Quelle mit dem Storybook (0.9.0)
VERSION = (ROOT / 'VERSION').read_text().strip()
KERN = (ROOT / 'vendor/kern/VERSION').read_text().strip()


TOKENS = [
 ('Seite', '--km-color-page', '--kern-color-layout-background-default'),
 ('Bereich (Wanne)', '--km-color-section', '--kern-color-layout-background-level-1'),
 ('Karte', '--km-color-card', '--kern-color-layout-background-level-1-surface'),
 ('Fläche in der Karte', '--km-color-inset', '--kern-color-layout-background-level-2'),
 ('Spur, Balken', '--km-color-track', '--kern-color-layout-background-level-2-surface'),
 ('Rand Bereich', '--km-color-border-section', '--kern-color-layout-border'),
 ('Rand Karte', '--km-color-border-card', '--kern-color-layout-border-level-1'),
 ('Text', '--km-color-text', '--kern-color-layout-text-default'),
 ('Text gedämpft', '--km-color-text-muted', '--kern-color-layout-text-muted'),
 ('Text Meta', '--km-color-text-dim', '(eigener Wert)'),
 ('Akzent', '--km-color-accent', '--kern-color-action-default'),
 ('Auf Akzent', '--km-color-on-accent', '--kern-color-action-on-default'),
 ('Aufmerksamkeit', '--km-color-attention', '(eigener Wert)'),
]

nav = ''.join(f'<a class="km-sidebar__item" href="#{a}">{t}</a>' for a, t, *_ in BAUSTEINE)
PRINZIP = [('target', 'Ziel', 'Eine Definition, die gut genug ist, dass Agenten und KI damit verlässlich Webseiten bauen. Dazu gehört mehr als CSS: Tokens in festen Ebenen, Bausteine mit Beschreibung, Zuständen und Abgrenzung, begründete Entscheidungen (ADR und DDR), Seitenregeln als Prüfliste und Prüfungen, die Abweichungen melden.'), ('layers', 'Zwei Ebenen Tokens', 'KERN-Tokens tragen die Werte je Theme, <code>--km-*</code> verweist nur auf sie. Bausteine lesen ausschließlich <code>--km-*</code>.'), ('layout-template', 'Ebenen wie KERN', 'Seite, Bereich (Wanne, <code>level-1</code>), Karte (<code>level-1-surface</code>), Fläche in der Karte (<code>level-2</code>).'), ('square', 'Eckig, Kontrast geprüft', 'Alle Radien 0. Text mindestens 4,5:1, Bedienelemente 3:1, in beiden Themes.'), ('space', 'Einheitlicher Innenabstand', 'Jeder Bereich 24 px seitlich und unten, Kopf 20 px oben und unten.'), ('shapes', 'Icons', 'Lucide 1.49.0 (ISC, <code>assets/lucide.json</code>, 1.857 Icons): 24er-Raster, Farbe über <code>currentColor</code>, Klasse <code>km-icon</code>. Strichstärke, Linienenden und Ecken setzt das Theme (<code>--km-icon-stroke</code>, <code>-linecap</code>, <code>-linejoin</code>). Eigene Icons auf demselben Raster zeichnen.'), ('sun-moon', 'Themes', '<code>data-kern-theme="dark|light"</code> am <code>&lt;html&gt;</code>, ohne Attribut nach Systemeinstellung.')]
tok_rows = ''.join(f'<tr><td><span class="sw" style="background:var({k})"></span>{n}</td><td><code>{k}</code></td><td><code>{html.escape(src)}</code></td><td class="cr" data-token="{k}"></td></tr>' for n, k, src in TOKENS)
SATZ = re.compile(r'(?<![zZ]\.)(?<!\b[a-zA-Z]\.)(?<=[.!?])\s+(?=[A-ZÄÖÜ„])')
def einstieg(zweck):
    """Erster Satz als Einleitung (km-lead), Rest als Lesetext (km-prose)."""
    m = SATZ.search(re.sub(r'<code>.*?</code>', lambda x: 'x' * len(x.group(0)), zweck))  # nicht in Code trennen
    vor, rest = (zweck[:m.start()], zweck[m.end():]) if m else (zweck, '')
    return f'<p class="km-lead">{vor}</p>' + (f'<div class="km-prose"><p>{rest}</p></div>' if rest else '')
def abschnitt(anker, titel, inhalt):
    return f'<section class="km-doc__section" id="{anker}"><h2 class="km-doc__title">{titel}</h2>{inhalt}</section>'
bausteine = ''.join(abschnitt(a, t, einstieg(zweck)
    + f'<figure class="km-figure"><div class="km-figure__media doc-demo">{markup}</div><figcaption class="km-figure__caption">Vorschau im gewählten Modus; Markup darunter.</figcaption></figure>'
    + f'<pre class="km-codeblock km-codeblock--wrap" aria-label="Markup {html.escape(t)}"><code>{html.escape(markup)}</code></pre>') for a, t, zweck, markup in BAUSTEINE)

def changelog_html():
    from einfuehrung import changelog_html as _cl  # gemeinsame Quelle mit der Seite „Changelog“ im Reiter Komponenten
    return abschnitt('changelog', 'Changelog', _cl('h3'))


changelog = changelog_html()

seite = f'''<!doctype html>
<html lang="de" data-kern-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Kernmix {VERSION}</title>
<link rel="stylesheet" href="../vendor/kern/kern.min.css">
<link rel="stylesheet" href="../dist/fonts.css">
<script src="../dist/km-table.js"></script>
<script src="../dist/km-popup.js"></script>
<link rel="stylesheet" href="../dist/km.css">
<link rel="stylesheet" href="../dist/themes/kern-nah.css">
<style>
  body {{ margin: 0; background: var(--km-color-page); color: var(--km-color-text); font-family: var(--km-font); }}
  .doc-kopf {{ position: sticky; top: 0; z-index: 5; display: flex; align-items: center; gap: var(--km-space-m); padding: var(--km-space-s) var(--km-space-xl); background: var(--km-color-page); border-bottom: 1px solid var(--km-color-border-card); }}
  .doc-kopf h1 {{ margin: 0; font-size: var(--km-font-size-m); font-weight: var(--km-font-weight-strong); }}
  .doc-kopf small {{ color: var(--km-color-text-dim); font-size: var(--km-font-size-xs); }}
  .doc-kopf .km-switch {{ margin-left: auto; }}
  .doc-layout {{ display: grid; grid-template-columns: 15rem minmax(0, 1fr); gap: var(--km-space-xl); padding: var(--km-space-xl); max-width: 76rem; }}
  .doc-layout > nav {{ position: sticky; top: 4.5rem; align-self: start; max-height: calc(100vh - 4.5rem - 2.5rem); overflow-y: auto; }} /* endet über der Eckleiste unten links */
  main [id] {{ scroll-margin-top: 4.5rem; }} /* Sprungziel unter dem festen Kopf */
  .sw {{ display: inline-block; width: 1rem; height: 1rem; margin-right: .5rem; vertical-align: -3px; border: 1px solid var(--km-color-border-section); }}
  @media (max-width: 860px) {{ .doc-layout {{ grid-template-columns: minmax(0, 1fr); }} .doc-layout > nav {{ position: static; }} }}
</style>
</head>
<body class="km-page">
<header class="doc-kopf">
  <h1>Kernmix</h1><small>Ein Remix von KERN · Version {VERSION} · KERN-Kit {KERN} · Präfix <code>km-</code> · EUPL-1.2</small>
  <button type="button" class="km-switch" role="switch" aria-checked="true" id="thema"><span class="km-switch__knob" aria-hidden="true"></span>Dunkel</button>
</header>
<div class="doc-layout">
<nav class="km-sidebar" aria-label="Inhalt">
  <div class="km-sidebar__group"><p class="km-sidebar__label">{i('book-open')}Grundlagen</p><a class="km-sidebar__item" href="#einfuehrung">Einführung</a><a class="km-sidebar__item" href="#prinzip">Prinzip</a><a class="km-sidebar__item" href="#tokens">Farben und Tokens</a><a class="km-sidebar__item" href="#abstaende">Abstände</a><a class="km-sidebar__item" href="#changelog">Changelog</a></div>
  <div class="km-sidebar__group"><p class="km-sidebar__label">{i('component')}Bausteine</p>{nav}</div>
</nav>
<main class="km-doc">
<section id="einfuehrung">{einfuehrung_html('h2')}</section>
{abschnitt('prinzip', 'Prinzip', '<p class="km-lead">Das Kit ist die gemeinsame Code-Basis für Project Dashboard, Lagebild und weitere eigene Seiten. Es baut auf KERN auf und ändert dessen Kit nicht: Ein Theme setzt KERN-Tokens auf den eigenen Look, Bausteine mit dem Präfix <code>km-</code> ergänzen, was KERN für Werkzeuge nicht mitbringt.</p><div class="km-cards km-cards--wide">' + ''.join(karte(*k) for k in PRINZIP) + '</div>')}
{abschnitt('tokens', 'Farben und Tokens', '<p class="km-lead">Rollen <code>--km-*</code> zeigen auf KERN-Tokens. Der Kontrast wird im Browser gemessen: Flächen gegen Text, Text gegen Karte.</p><div class="km-table-wrap"><table class="km-table"><thead><tr><th>Rolle</th><th>Kit-Token</th><th>KERN-Token</th><th>Kontrast</th></tr></thead><tbody>' + tok_rows + '</tbody></table></div>')}
{abschnitt('abstaende', 'Abstände', '<p class="km-lead">Von außen nach innen wird jede Ebene eine Stufe kleiner. Die Rollen stehen in <code>src/km-roles.css</code>.</p><div class="km-cards km-cards--two">' + ''.join(karte(ic, n, r) for ic, n, r in zip(['arrow-down-wide-narrow' if 'arrow-down-wide-narrow' in IC else 'layers', 'group', 'ruler', 'scissors'], ['Außen groß, innen klein', 'Nähe gruppiert', 'Nur Werte der Skala', 'Ausnahmen'], ABSTAND_REGELN)) + '</div><div class="km-table-wrap"><table class="km-table"><thead><tr><th>Ebene</th><th>Token</th><th>Stufe</th><th>Wofür</th></tr></thead><tbody>' + ''.join(f'<tr><td>{e}</td><td class="km-table__nowrap"><code>{tk}</code></td><td class="km-table__nowrap">{s}</td><td>{w}</td></tr>' for e, tk, s, w in ABSTAENDE) + '</tbody></table></div><figure class="km-figure"><div class="km-figure__media doc-demo">' + ABSTAND_BILD + '</div><figcaption class="km-figure__caption">Schaubild mit den Werten des gewählten Themes: Bereich, Karte, Gruppe, eng.</figcaption></figure>')}
{bausteine}
{changelog}
</main>
</div>
<button type="button" class="km-totop" id="nach-oben" aria-label="Nach oben" title="Nach oben">{i("arrow-up")}</button>
<script>
(function(){{
  var html = document.documentElement, knopf = document.getElementById('thema');
  function rgb(farbe){{ var c = document.createElement('canvas').getContext('2d'); c.fillStyle = farbe; c.fillRect(0,0,1,1); return c.getImageData(0,0,1,1).data; }}
  function lum(d){{ return [0,1,2].map(function(k){{ var v = d[k] / 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); }}).reduce(function(s, v, k){{ return s + v * [0.2126, 0.7152, 0.0722][k]; }}, 0); }}
  function kontrast(a, b){{ var x = lum(rgb(a)), y = lum(rgb(b)); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); }}
  function messen(){{
    var st = getComputedStyle(html), text = st.getPropertyValue('--km-color-text').trim(), karte = st.getPropertyValue('--km-color-card').trim();
    document.querySelectorAll('.cr').forEach(function(td){{
      var v = st.getPropertyValue(td.dataset.token).trim(), tk = td.dataset.token;
      // Paare: Vordergrund gegen Karte, Hintergründe gegen Text, „auf Akzent“ gegen Akzent
      var gegen = tk === '--km-color-on-accent' ? st.getPropertyValue('--km-color-accent').trim() : (/text|accent|attention/.test(tk) ? karte : text);
      var k = kontrast(v, gegen); var soll = /border|track|section|page|inset|card/.test(tk) ? 1 : 4.5;
      td.textContent = v + ' · ' + k.toFixed(2).replace('.', ',') + ':1' + (tk === '--km-color-on-accent' ? ' (auf Akzent)' : '') + (soll > 1 && k < soll ? ' (unter Ziel)' : '');
    }});
  }}
  knopf.addEventListener('click', function(){{ var dunkel = html.getAttribute('data-kern-theme') !== 'dark'; html.setAttribute('data-kern-theme', dunkel ? 'dark' : 'light'); knopf.setAttribute('aria-checked', String(dunkel)); knopf.lastChild.textContent = dunkel ? 'Dunkel' : 'Hell'; messen(); }});
  document.querySelectorAll('.km-intro__more').forEach(function(b){{ b.addEventListener('click', function(){{ var t = b.previousElementSibling; var auf = t.classList.toggle('km-intro__body--short') === false; b.textContent = auf ? 'Weniger' : 'Weiterlesen'; b.setAttribute('aria-expanded', String(auf)); }}); }});
  messen();
}})();
</script>
<script>(function(){{ var b = document.getElementById('nach-oben'); if (!b) return; function zeig(){{ b.classList.toggle('km-totop--visible', scrollY > innerHeight * 0.8); }} addEventListener('scroll', zeig, {{ passive: true }}); zeig(); b.addEventListener('click', function(){{ scrollTo({{ top: 0, behavior: 'instant' }}); }}); }})();</script>
<script>/* Jede Tabelle über den Kit-Bauweg */if (window.kmTabelle) [].forEach.call(document.querySelectorAll("table.km-table:not(.doc-demo table)"), function(t){{ window.kmTabelle(t); }});</script>
</body>
</html>
'''
(ROOT / 'docs/index.html').write_text(seite, encoding='utf-8')  # changelog: siehe changelog_html() oben
print('docs/index.html', len(seite) // 1024, 'KB,', len(BAUSTEINE), 'Bausteine,', len(TOKENS), 'Tokens')

print('dist/einfuehrung-vorschau.html', len(vorschau()) // 1024, 'KB (aus tools/einfuehrung.py)')
