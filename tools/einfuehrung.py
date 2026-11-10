"""Einführung (Startseite) aus docs/intro.md und assets/einfuehrung/*.svg, nur aus Kit-Bausteinen.
Eine Quelle für die erste Story im Reiter „Komponenten“ (build-storybook.py), den ersten Abschnitt der Doku (build-doku.py)
und die Vorschau dist/einfuehrung-vorschau.html (wird hier erzeugt, nicht von Hand ändern).
Aufbau: km-hero--start (Titel, Untertitel, km-lead) · km-figure (Grafik inline, folgt dem Theme) · km-callout--quote ·
km-cards mit Icon je Listenpunkt · km-prose für reinen Text. Die Zuordnung Abschnitt → Darstellung steht in ABSCHNITTE."""
import html, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
import sys; sys.path.insert(0, str(Path(__file__).resolve().parent))
from bausteine import i  # Lucide-Icon als Inline-SVG
from grafik_stil import scope

# Abschnitt aus intro.md → (Darstellung, Raster, Icons je Listenpunkt). Darstellung: lead, zitat, karten, prosa
ABSCHNITTE = {
    'Die Idee': ('lead', None, []),
    'Warum ein Bassist so etwas baut': ('zitat', None, []),
    'Sechs Prinzipien': ('karten', 'wide', ['message-square', 'code', 'blocks', 'refresh-cw', 'accessibility', 'target']),
    'KERN-Updates laufen durch': ('karten', 'two', ['package-check', 'refresh-ccw', 'shield-alert', 'ruler']),
    'Wofür Kernmix da ist': ('karten', 'two', ['bot', 'flask-conical', 'layout-template', 'globe']),
    'Was im Mix steckt': ('karten', 'wide', ['disc-3', 'sliders-vertical', 'notebook-text']),
    'Kurz auf Englisch': ('prosa', None, []),
}
# Grafiken: (Datei, nach Abschnitt, eigene Überschrift oder None, Bildunterschrift)
GRAFIKEN = [
    ('mix', 'Die Idee', None, 'KERN liefert die Grundspur. Tokens, Bausteine, Themes und Regeln laufen am Pult zusammen; die Summe geht an alle Projekte.'),
    ('token-ebenen', 'Was im Mix steckt', 'Tokens in vier Ebenen', 'Die Ebenen folgen KERN. Bausteine lesen nur semantische und Komponenten-Token, Themes setzen nur Werte.'),
    ('regel-zur-seite', 'Was im Mix steckt', 'Von der Regel zur Seite', 'Jede Regel hat einen Weg: begründet, als Prüfliste, als Baustein im Kit, gemessen, gebaut.'),
]


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a class="km-link" href="\2">\1</a>', s)


def svg(name, cls=''):
    """Grafik inline: IDs und Stilregeln je Grafik eindeutig (grafik_stil.scope), damit mehrere Grafiken auf einer Seite sich nicht stören."""
    s = scope((ROOT / f'assets/einfuehrung/{name}.svg').read_text(encoding='utf-8').strip(), f'km-fig-{name}')
    return s.replace('<svg id=', f'<svg class="{cls}" id=', 1) if cls else s


def abbildung(name, unterschrift):
    """Abbildung; gibt es eine Hochformat-Fassung (<name>-hoch.svg), stehen beide darin, die Fläche zeigt je nach Breite eine (km-figure__tall)."""
    hoch = (ROOT / f'assets/einfuehrung/{name}-hoch.svg').exists()
    medien = svg(name, 'km-figure__wide') + svg(name + '-hoch', 'km-figure__tall') if hoch else svg(name)
    return f'<figure class="km-figure"><div class="km-figure__media">{medien}</div><figcaption class="km-figure__caption">{html.escape(unterschrift)}</figcaption></figure>'


def karte(icon, titel, text):
    return (f'<article class="km-card km-card--accent-top"><div class="km-card__head"><span class="km-card__tile">{i(icon)}</span>'
            f'<h3 class="km-card__title">{titel}</h3></div><div class="km-prose"><p>{text}</p></div></article>')


def lesen():
    """intro.md in (Titel, Untertitel, [(Abschnitt, [Zeilen])])."""
    titel, unter, teile = '', '', []
    for z in (ROOT / 'docs/intro.md').read_text(encoding='utf-8').splitlines():
        if z.startswith('# '): titel = z[2:].strip(); continue
        if z.startswith('## '): teile.append((z[3:].strip(), [])); continue
        if not z.strip(): continue
        if not teile:
            m = re.match(r'\*\*(.+?)\.?\*\*\s*(.*)$', z)
            unter = m.group(1) if m else z
            continue
        teile[-1][1].append(z)
    return titel, unter, teile


def punkte(zeilen):
    """Listenpunkte „- **Titel:** Text“ bzw. „1. **Titel.** Text“ → [(Titel, Text)]."""
    out = []
    for z in zeilen:
        m = re.match(r'^(?:-|\d+\.)\s+\*\*(.+?)[.:]?\*\*\s*(.*)$', z)
        if m: out.append((inline(m.group(1)), inline(m.group(2))))
    return out


def einfuehrung_html(kopf='h1'):
    """Ganze Einführung als <div class="km-doc">. kopf: Ebene des Seitentitels (h1 auf eigener Seite, h2 eingebettet)."""
    titel, unter, teile = lesen()
    h2 = 'h3' if kopf == 'h2' else 'h2'
    bekannt = [t for t, _ in teile]
    fehlt = [t for t in bekannt if t not in ABSCHNITTE]
    if fehlt: raise SystemExit('docs/intro.md: Abschnitt ohne Darstellung in tools/einfuehrung.py: ' + ', '.join(fehlt))
    out = []
    for t, zeilen in teile:
        art, raster, icons = ABSCHNITTE[t]
        if art == 'lead':
            out.append(f'<header class="km-hero km-hero--start"><p class="km-hero__kicker">Einführung</p><{kopf} class="km-hero__title">{inline(titel)}</{kopf}>'
                       f'<p class="km-hero__subtitle">{inline(unter)}</p>' + ''.join(f'<p class="km-lead">{inline(z)}</p>' for z in zeilen) + '</header>')
        else:
            sek = f'<section class="km-doc__section"><{h2} class="km-doc__title">{inline(t)}</{h2}>'
            if art == 'zitat':
                sek += f'<blockquote class="km-callout km-callout--quote">{i("quote")}<div>' + ''.join(f'<p>{inline(z)}</p>' for z in zeilen) + '</div></blockquote>'
            elif art == 'karten':
                vor = [z for z in zeilen if not re.match(r'^(?:-|\d+\.)\s', z)]
                ps = punkte(zeilen)
                if len(ps) != len(icons): raise SystemExit(f'tools/einfuehrung.py: „{t}“ hat {len(ps)} Punkte, aber {len(icons)} Icons')
                sek += ''.join(f'<p class="km-lead">{inline(z)}</p>' for z in vor)
                sek += f'<div class="km-cards km-cards--{raster}">' + ''.join(karte(ic, a, b) for ic, (a, b) in zip(icons, ps)) + '</div>'
            else:
                sek += '<div class="km-prose"' + (' lang="en"' if 'Englisch' in t else '') + '>' + ''.join(f'<p>{inline(z)}</p>' for z in zeilen) + '</div>'
            out.append(sek + '</section>')
        for name, nach, ueber, unterschrift in GRAFIKEN:
            if nach != t: continue
            fig = abbildung(name, unterschrift)
            out.append(f'<section class="km-doc__section"><{h2} class="km-doc__title">{html.escape(ueber)}</{h2}>{fig}</section>' if ueber else fig)
    # „Kurz auf Englisch“ ans Ende, nach den Grafiken
    en = [x for x in out if 'lang="en"' in x]
    out = [x for x in out if 'lang="en"' not in x] + en
    return '<div class="km-doc">' + ''.join(out) + '</div>'


def vorschau():
    """dist/einfuehrung-vorschau.html: die Einführung als eigene Seite, aus derselben Quelle."""
    version = (ROOT / 'VERSION').read_text().strip()
    seite = ('<!doctype html><html lang="de" data-kern-theme="dark"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
             f'<meta name="robots" content="noindex, nofollow"><title>Kernmix {version} · Einführung</title>'
             '<link rel="stylesheet" href="../vendor/kern/kern.min.css"><link rel="stylesheet" href="../dist/km.css"><link rel="stylesheet" href="../dist/fonts.css"><link rel="stylesheet" href="../dist/themes/kern-nah.css">'
             '<!-- erzeugt mit tools/einfuehrung.py aus docs/intro.md und assets/einfuehrung/, nicht von Hand ändern -->'
             '</head><body class="km-page">' + einfuehrung_html().replace('<div class="km-doc">', '<main class="km-doc km-doc--page">', 1)[:-len('</div>')] + '</main></body></html>\n')
    (ROOT / 'dist/einfuehrung-vorschau.html').write_text(seite, encoding='utf-8')
    return seite


if __name__ == '__main__':
    print('dist/einfuehrung-vorschau.html', len(vorschau()) // 1024, 'KB')


MONATE = ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember']


def changelog_html(ebene='h2'):
    """Changelog aus CHANGELOG.md im Stil der Einführung: je Version eine Karte mit Release-Namen, Datum und Punkten, neueste oben.
    Gemeinsame Quelle für die Seite „Changelog“ im Reiter Komponenten und den Abschnitt der Doku."""
    root = Path(__file__).resolve().parent.parent
    teile, aktuell = [], None
    for z in (root / 'CHANGELOG.md').read_text(encoding='utf-8').splitlines():
        m = re.match(r'## (.+?) „(.+?)“ · (.+)$', z)
        if m: aktuell = [m.group(1), m.group(2), m.group(3), []]; teile.append(aktuell); continue
        if aktuell and re.match(r'\s*- ', z): aktuell[3].append((z.startswith('  '), z.strip()[2:]))
    h2 = ebene; h3 = 'h3' if ebene == 'h2' else 'h4'
    out = [f'<p class="km-lead">Jede Version hat einen Release-Namen, neueste oben. Quelle ist <code>CHANGELOG.md</code>; der Changelog wächst mit jeder Änderung am Kit.</p>']
    for n, (ver, name, datum, punkte) in enumerate(teile):
        li, offen = '', False
        for sub, t in punkte:
            if sub and not offen: li = li[:-5] + '<ul>'; offen = True
            if not sub and offen: li += '</ul></li>'; offen = False
            li += f'<li>{inline(t)}</li>'
        if offen: li += '</ul></li>'
        neu = ' <span class="km-pill km-pill--ok">aktuell</span>' if n == 0 else ''
        try:
            j, mo, ta = datum.strip().split('-'); datum_de = f'{int(ta)}. {MONATE[int(mo) - 1]} {j}'
        except ValueError:
            datum_de = datum
        zahl = sum(1 for sub, _ in punkte if not sub)
        meta = f'{datum_de} · {zahl} {"Änderung" if zahl == 1 else "Änderungen"}'
        # Datum und Anzahl direkt unter dem Release-Namen statt frei im Kopf
        out.append(f'<article class="km-card km-card--accent-left km-doc__release"><div class="km-card__head"><span class="km-card__tile">{i("disc-3")}</span><div><{h3} class="km-card__title">{html.escape(ver)} „{html.escape(name)}“{neu}</{h3}><p class="km-card__subtitle">{html.escape(meta)}</p></div></div><div class="km-prose km-prose--columns"><ul>{li}</ul></div></article>')  # Punkte auf breiten Flächen zweispaltig (0.13.0)
    return '<div class="km-doc">' + ''.join(out) + '</div>'
