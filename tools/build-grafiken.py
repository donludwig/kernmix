#!/usr/bin/env python3
"""Grafiken der Einführung (assets/einfuehrung/*.svg): animiert, klickbar, mit Lucide-Icons.

Farben über Kit-Tokens (folgen Theme und Modus), Bewegung nur ohne „weniger Bewegung“ im System (prefers-reduced-motion),
Links führen in die Komponenten-Seite (storybook/index.html#story=… bzw. #tab=…). Eingebunden über tools/einfuehrung.py.
Aufruf: python3 tools/build-grafiken.py (danach build-storybook.py und build-doku.py)."""
import json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from grafik_stil import LUC, ic, STIL, HOCH_B, text_zeilen  # gemeinsamer Stil, auch für Grafiken auf Seiten (Dashboard)

ROOT = Path(__file__).resolve().parent.parent
ZIEL = ROOT / 'assets/einfuehrung'
SB = '../storybook/index.html#'


def link(href, titel, inhalt):
    if href == 'tab=entscheidungen': return f'<g>{inhalt}</g>'  # Reiter Entscheidungen gibt es in dieser Fassung nicht
    return f'<a href="{SB}{href}" target="_top" class="lk"><title>{titel}</title>{inhalt}</a>'


def svg(name, w, h, titel, desc, body):
    s = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="t d" font-family="inherit">
<title id="t">{titel}</title><desc id="d">{desc}</desc>
<style>{STIL}</style>
<g style="--fb:{FARBE[0]}">{body}</g>
</svg>
'''
    (ZIEL / f'{name}.svg').write_text(s, encoding='utf-8')


# 1) Der Mix
b = '<text class="k" x="40" y="40">GRUNDSPUR</text>'
b += link('story=grundlagen-tokens-farben-kern-semantik', 'KERN: Grundwerte und Semantik ansehen',
          '<rect class="f" x="40" y="70" width="170" height="300"/>' + ic('landmark', 107, 130, 36) + '<text class="h" x="125" y="210" text-anchor="middle">KERN</text><text class="m" x="125" y="238" text-anchor="middle">Kit, Raster,</text><text class="m" x="125" y="258" text-anchor="middle">Barrierefreiheit,</text><text class="m" x="125" y="278" text-anchor="middle">Grundwerte</text>')
b += '<path class="flow flowan" d="M214 220 H262"/>'
b += '<text class="k" x="280" y="40">KANÄLE AM PULT</text>'
FARBE = ['var(--km-color-accent)'] * 5  # je Grafik eine Akzentfarbe; Mix im Akzent
kanaele = [('Tokens', 'variable', 'story=grundlagen-tokens-farben-rollen-km', 40, 0), ('Bausteine', 'blocks', 'story=erweiterungen-werkzeug-bausteine-km-segmented-control', -55, 1.2),
           ('Themes', 'palette', 'story=grundlagen-tokens-farben-kern-palette', 30, 2.1), ('Regeln', 'scale', 'tab=entscheidungen', -35, 0.6)]
for n, (name, icon, ziel, weg, delay) in enumerate(kanaele):
    x = 280 + n * 125
    knopf_y = 205 + (n % 2) * 30
    inhalt = (f'<g style="--fb:{FARBE[n]}"><rect class="f" x="{x}" y="70" width="110" height="300"/><rect class="kante" x="{x}" y="70" width="110" height="4"/>' + ic(icon, x + 43, 84, 24) + f'<text class="t" x="{x + 55}" y="132" text-anchor="middle">{name}</text>'
              + f'<line class="l" x1="{x + 55}" y1="150" x2="{x + 55}" y2="350"/>'
              + f'<rect class="a fader" style="--weg:{weg}px;animation-delay:{delay}s" x="{x + 33}" y="{knopf_y}" width="44" height="22"/></g>')
    b += link(ziel, f'{name}: ansehen', inhalt)
b += '<path class="flow flowan" d="M784 220 H842"/>'
b += '<text class="k" x="850" y="40">SUMME</text>'
b += link('story=grundlagen-kernmix-changelog', 'Kernmix: alle Versionen im Changelog',
          '<rect class="a puls" x="850" y="140" width="150" height="160"/>' + ic('sliders-vertical', 908, 156, 34, 'icon') + '<text class="c" x="925" y="222" text-anchor="middle" style="font-size:22px">Kernmix</text><text class="c" x="925" y="248" text-anchor="middle" style="font-size:13px;font-weight:600">Ein Remix von KERN</text>')
b += '<text class="k" x="1040" y="40">AUSGÄNGE</text>'
for n, (name, icon) in enumerate([('Project Dashboard', 'layout-dashboard'), ('Lagebild', 'shield-check'), ('KI-Design-Runde', 'users'), ('Startklar', 'rocket')]):
    y = 80 + n * 75
    b += f'<path class="flow flowan" style="animation-delay:{n * .15}s" d="M1000 220 C1020 220 1020 {y + 25} 1040 {y + 25}"/>'
    box = f'<g style="--fb:{FARBE[n]}"><rect class="f out" style="animation-delay:{n}s" x="1040" y="{y}" width="200" height="50"/><rect class="kante" x="1040" y="{y}" width="4" height="50"/>' + ic(icon, 1054, y + 15, 20) + f'<text class="t" x="1084" y="{y + 31}">{name}</text></g>'
    b += link('tab=prototyp', 'Das Dashboard als Prototyp ansehen', box) if n == 0 else box
svg('mix', 1260, 400, 'Der Mix', 'KERN liefert die Grundspur. Am Pult laufen Tokens, Bausteine, Themes und Regeln als Kanäle zusammen. Die Summe ist Kernmix, ausgegeben an Dashboard, Lagebild, KI-Design-Runde und Startklar. Kanäle und Kästen führen zur passenden Seite.', b)

# 2) Token-Ebenen
FARBE = ['var(--km-color-data-5)'] * 5  # Token-Ebenen in Jade
b = '<text class="k" x="40" y="40">TOKEN-EBENEN WIE BEI KERN</text>'
ebenen = [('Grundwerte', 'droplet', 'rohe Werte ohne Bedeutung', '#3451c6 · 16px · 0,16', 'story=grundlagen-tokens-farben-kern-palette'),
          ('Core Token', 'swatch-book', 'benannte Skalen und Farbreihen', '--kern-color-darkblue-500 · --kern-16', 'story=grundlagen-tokens-farben-kern-palette'),
          ('Semantische Token', 'tag', 'Bedeutung: wofür ein Wert steht', '--km-color-accent · --km-space-s', 'story=grundlagen-tokens-farben-rollen-km'),
          ('Komponente', 'component', 'Typ component im Namen, je Baustein', '--km-component-sidebar-width', 'story=erweiterungen-werkzeug-bausteine-km-seitenleiste')]
b += '<line class="l" x1="70" y1="78" x2="70" y2="400" style="stroke-dasharray:3 6"/>'
b += '<circle class="a tropfen" cx="70" cy="70" r="5"/><circle class="a tropfen" style="animation-delay:1.4s" cx="70" cy="70" r="5"/>'
for n, (name, icon, d, beispiel, ziel) in enumerate(ebenen):
    y = 70 + n * 92; x = 100; w = 1120  # alle Ebenen gleich breit
    hervor = n == 2
    rect = f'<g style="--fb:{FARBE[n]}"><rect class="{"a" if hervor else "f"} ebene" style="animation-delay:{n * .18}s" x="{x}" y="{y}" width="{w}" height="72"/>' + ('' if hervor else f'<rect class="kante ebene" style="animation-delay:{n * .18}s" x="{x}" y="{y}" width="4" height="72"/>')
    t1, t2, ick = ('c', 'c', 'icon') if hervor else ('t', 'm', 'ic')
    inhalt = (rect + f'<g class="ebene" style="animation-delay:{n * .18}s">' + ic(icon, x + 22, y + 24, 24, ick)
              + f'<text class="{t1}" x="{x + 62}" y="{y + 31}" style="font-size:19px">{name}</text><text class="{t2}" x="{x + 62}" y="{y + 55}" style="font-weight:400">{d}</text>'
              + f'<text class="{t2}" x="{x + w - 24}" y="{y + 43}" text-anchor="end" style="font-family:var(--km-font-mono,monospace);font-weight:400">{beispiel}</text></g></g>')
    b += link(ziel, f'{name}: ansehen', inhalt)
b += '<text class="m" x="40" y="452">Bausteine lesen nur semantische und Komponenten-Token. Themes setzen nur Werte, nie Regeln.</text>'
svg('token-ebenen', 1260, 470, 'Token-Ebenen', 'Vier Ebenen nach KERN: Grundwerte, Core Token, Semantische Token und Komponenten-Token. Bausteine lesen nur semantische und Komponenten-Token. Jede Ebene führt zur passenden Seite.', b)

# 3) Von der Regel zur Seite
FARBE = ['var(--km-color-data-2)'] * 5  # Koralle: Kupfer hatte hell nur 3,94:1 für Text auf der Fläche (2026-11-09)
b = '<text class="k" x="40" y="40">VON DER REGEL ZUR SEITE</text>'
schritte = [('Entscheidung', 'scale', 'ADR oder DDR, begründet', 'tab=entscheidungen'), ('Seitenregel', 'list-checks', 'kurze Prüfliste', 'story=grundlagen-kernmix-einf-hrung'),
            ('Baustein', 'blocks', 'im Kit, mit Doku und Story', 'story=erweiterungen-werkzeug-bausteine-km-segmented-control'), ('Prüfung', 'gauge', 'misst, statt zu behaupten', 'story=grundlagen-tokens-farben-rollen-km'),
            ('Seite', 'monitor', 'Mensch oder Agent baut', 'tab=prototyp')]
for n, (name, icon, d, ziel) in enumerate(schritte):
    x = 40 + n * 240
    hervor = n == 4
    t1, t2, ick = ('c', 'c', 'icon') if hervor else ('t', 'm', 'ic')
    inhalt = (f'<g style="--fb:{FARBE[n]}"><rect class="{"a" if hervor else "f schritt"}" style="animation-delay:{n * 2}s" x="{x}" y="70" width="210" height="170"/>' + ('' if hervor else f'<rect class="kante" x="{x}" y="70" width="210" height="4"/>') + ic(icon, x + 22, 92, 30, ick)
              + f'<text class="{t1}" x="{x + 166}" y="118" text-anchor="end" style="font-size:30px;font-weight:700;opacity:.55">{n + 1}</text>'
              + f'<text class="{t1}" x="{x + 22}" y="170">{name}</text><text class="{t2}" x="{x + 22}" y="198" style="font-weight:400">{d}</text></g>')
    b += link(ziel, f'{name}: ansehen', inhalt)
    if n < 4:
        b += f'<path class="flow flowan" style="animation-delay:{n * .2}s" d="M{x + 214} 155 H{x + 236}"/>'
svg('regel-zur-seite', 1260, 270, 'Von der Regel zur Seite', 'Fünf Schritte: Entscheidung, Seitenregel, Baustein im Kit, Prüfung, Seite. Ein Lichtpunkt läuft durch die Schritte; jeder Schritt führt zur passenden Seite.', b)

# Hochformat-Fassungen (0.13.0): gleiche Inhalte senkrecht, 250 breit; die Seite zeigt sie unter 56rem Breite der Fläche (km-figure__tall)
W = HOCH_B

# 1h) Der Mix, hoch
FARBE = ['var(--km-color-accent)'] * 5
b = '<text class="k" x="0" y="16">GRUNDSPUR</text>'
b += link('story=grundlagen-tokens-farben-kern-semantik', 'KERN: Grundwerte und Semantik ansehen',
          f'<rect class="f" x="0" y="28" width="{W}" height="104"/>' + ic('landmark', 14, 42, 28) + '<text class="h" x="52" y="64">KERN</text><text class="m" x="14" y="96">Kit, Raster, Barrierefreiheit,</text><text class="m" x="14" y="116">Grundwerte</text>')
b += f'<path class="flow flowan" d="M{W // 2} 136 V160"/>'
b += '<text class="k" x="0" y="180">KANÄLE AM PULT</text>'
for n, (name, icon, ziel, weg, delay) in enumerate(kanaele):
    x = (n % 2) * 130; y = 192 + (n // 2) * 140
    knopf_y = y + 78 + (n % 2) * 18
    inhalt = (f'<g style="--fb:{FARBE[n]}"><rect class="f" x="{x}" y="{y}" width="120" height="128"/><rect class="kante" x="{x}" y="{y}" width="120" height="4"/>' + ic(icon, x + 48, y + 14, 24) + f'<text class="t" x="{x + 60}" y="{y + 60}" text-anchor="middle">{name}</text>'
              + f'<line class="l" x1="{x + 60}" y1="{y + 74}" x2="{x + 60}" y2="{y + 118}"/>'
              + f'<rect class="a fader" style="--weg:{18 if n % 2 == 0 else -18}px;animation-delay:{delay}s" x="{x + 38}" y="{knopf_y}" width="44" height="16"/></g>')
    b += link(ziel, f'{name}: ansehen', inhalt)
b += f'<path class="flow flowan" d="M{W // 2} 476 V500"/>'
b += '<text class="k" x="0" y="520">SUMME</text>'
b += link('story=grundlagen-kernmix-changelog', 'Kernmix: alle Versionen im Changelog',
          f'<rect class="a puls" x="0" y="532" width="{W}" height="84"/>' + ic('sliders-vertical', 14, 556, 32, 'icon') + '<text class="c" x="60" y="572" style="font-size:22px">Kernmix</text><text class="c" x="60" y="596" style="font-size:13px;font-weight:600">Ein Remix von KERN</text>')
b += f'<path class="flow flowan" d="M{W // 2} 620 V644"/>'
b += '<text class="k" x="0" y="664">AUSGÄNGE</text>'
for n, (name, icon) in enumerate([('Project Dashboard', 'layout-dashboard'), ('Lagebild', 'shield-check'), ('KI-Design-Runde', 'users'), ('Startklar', 'rocket')]):
    y = 676 + n * 56
    box = f'<g style="--fb:{FARBE[n]}"><rect class="f out" style="animation-delay:{n}s" x="0" y="{y}" width="{W}" height="46"/><rect class="kante" x="0" y="{y}" width="4" height="46"/>' + ic(icon, 16, y + 13, 20) + f'<text class="t" x="48" y="{y + 29}">{name}</text></g>'
    b += link('tab=prototyp', 'Das Dashboard als Prototyp ansehen', box) if n == 0 else box
svg('mix-hoch', W, 900, 'Der Mix', 'KERN liefert die Grundspur. Am Pult laufen Tokens, Bausteine, Themes und Regeln als Kanäle zusammen. Die Summe ist Kernmix, ausgegeben an Dashboard, Lagebild, KI-Design-Runde und Startklar. Kanäle und Kästen führen zur passenden Seite.', b)

# 2h) Token-Ebenen, hoch
FARBE = ['var(--km-color-data-5)'] * 5
b = '<text class="k" x="0" y="16">TOKEN-EBENEN WIE BEI KERN</text>'
y = 30
for n, (name, icon, d, beispiel, ziel) in enumerate(ebenen):
    hervor = n == 2
    t1, t2, ick = ('c', 'c', 'icon') if hervor else ('t', 'm', 'ic')
    dz, dy = text_zeilen(t2, 14, y + 64, d, 30, 18, ' style="font-weight:400"')
    bz, by = text_zeilen(t2 + ' mono', 14, dy + 24, beispiel.replace(' · ', '  '), 30, 18, ' style="font-weight:400;font-size:12px"')
    h = by - y + 16
    rect = f'<g style="--fb:{FARBE[n]}"><rect class="{"a" if hervor else "f"} ebene" style="animation-delay:{n * .18}s" x="0" y="{y}" width="{W}" height="{h}"/>' + ('' if hervor else f'<rect class="kante ebene" style="animation-delay:{n * .18}s" x="0" y="{y}" width="4" height="{h}"/>')
    inhalt = (rect + f'<g class="ebene" style="animation-delay:{n * .18}s">' + ic(icon, 14, y + 16, 24, ick)
              + f'<text class="{t1}" x="48" y="{y + 35}" style="font-size:19px">{name}</text>' + dz + bz + '</g></g>')
    b += link(ziel, f'{name}: ansehen', inhalt)
    y += h + 12
zt, zy = text_zeilen('m', 0, y + 14, 'Bausteine lesen nur semantische und Komponenten-Token. Themes setzen nur Werte, nie Regeln.', 32)
b += zt
svg('token-ebenen-hoch', W, zy + 10, 'Token-Ebenen', 'Vier Ebenen nach KERN: Grundwerte, Core Token, Semantische Token und Komponenten-Token. Bausteine lesen nur semantische und Komponenten-Token. Jede Ebene führt zur passenden Seite.', b)

# 3h) Von der Regel zur Seite, hoch
FARBE = ['var(--km-color-data-2)'] * 5  # Koralle: Kupfer hatte hell nur 3,94:1 für Text auf der Fläche (2026-11-09)
b = '<text class="k" x="0" y="16">VON DER REGEL ZUR SEITE</text>'
for n, (name, icon, d, ziel) in enumerate(schritte):
    y = 30 + n * 96
    hervor = n == 4
    t1, t2, ick = ('c', 'c', 'icon') if hervor else ('t', 'm', 'ic')
    inhalt = (f'<g style="--fb:{FARBE[n]}"><rect class="{"a" if hervor else "f schritt"}" style="animation-delay:{n * 2}s" x="0" y="{y}" width="{W}" height="78"/>' + ('' if hervor else f'<rect class="kante" x="0" y="{y}" width="{W}" height="4"/>') + ic(icon, 14, y + 16, 24, ick)
              + f'<text class="{t1}" x="{W - 14}" y="{y + 38}" text-anchor="end" style="font-size:24px;font-weight:700;opacity:.55">{n + 1}</text>'
              + f'<text class="{t1}" x="48" y="{y + 35}">{name}</text><text class="{t2}" x="14" y="{y + 62}" style="font-weight:400">{d}</text></g>')
    b += link(ziel, f'{name}: ansehen', inhalt)
    if n < 4:
        b += f'<path class="flow flowan" style="animation-delay:{n * .2}s" d="M{W // 2} {y + 80} V{y + 94}"/>'
svg('regel-zur-seite-hoch', W, 30 + 5 * 96, 'Von der Regel zur Seite', 'Fünf Schritte: Entscheidung, Seitenregel, Baustein im Kit, Prüfung, Seite. Ein Lichtpunkt läuft durch die Schritte; jeder Schritt führt zur passenden Seite.', b)
print(f'{len(list(ZIEL.glob("*.svg")))} Grafiken geschrieben:', ', '.join(p.name for p in sorted(ZIEL.glob('*.svg'))))
