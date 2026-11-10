"""Komponenten-Doku im Aufbau D „Vier Fragen mit Kapitelleiste“, gemeinsame Quelle für tools/build-storybook.py.
Aus docs/komponenten/<name>.md: Titel, Einleitung (km-lead), Fakten-Kacheln, offene Punkte als Hinweiskasten oben, dann vier Kapitel
1 · Was ist es? · 2 · Wann nehmen? · 3 · Wie bauen? · 4 · Wie prüfen?, je mit Karten im Raster und am Ende dem Kasten „Regel:“ aus „## Regeln“.
Jeder ##-Abschnitt erscheint genau einmal; unbekannte Abschnitte landen in Kapitel 4 unter „Bezug“. Nichts aufklappbar, nichts frei stehend."""
import ast, html, re
from pathlib import Path

from bausteine import i as ikon

ROOT = Path(__file__).resolve().parents[1]

# Markdown-Helfer inline(), md(), tabelle()
PFAD = re.compile(r'(?<![\w/.<>-])((?:\.{0,2}/)?(?:[\w.-]+/)+[\w.*-]*|[\w*-]+\.(?:md|css|py|js|html|json|svg|ttf|woff2|sh|txt))(?![\w/])')

def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    # Pfade und Dateinamen ohne Backticks auch in Mono; nur außerhalb von <code> und Tags
    teile = re.split(r'(<code>.*?</code>|<[^>]+>)', t)
    return ''.join(x if x.startswith('<') else PFAD.sub(r'<code>\1</code>', x) for x in teile)

def tabelle(zeilen, fmt=None):
    """Markdown-Tabelle → Standard-Tabelle des Kits (km-table-wrap + km-table), Rollen und Kopf-Icons setzt kmTabelle() nach dem Laden."""
    fmt = fmt or inline
    zellen = [[c.strip() for c in z.strip().strip('|').split('|')] for z in zeilen if not re.match(r'^\|[\s:|-]+\|$', z.strip())]
    kopf, *rumpf = zellen
    return ('<div class="km-table-wrap"><table class="km-table"><thead><tr>' + ''.join(f'<th>{fmt(c)}</th>' for c in kopf) + '</tr></thead><tbody>'
            + ''.join('<tr>' + ''.join(f'<td>{fmt(c)}</td>' for c in r) + '</tr>' for r in rumpf) + '</tbody></table></div>')

def md(text):
    """Kleines Markdown: Überschriften ab ##, Absätze, Listen (auch eingerückt als Unterliste), Code, fett."""
    out, liste, sub = [], False, False
    def zu():
        nonlocal liste, sub
        if sub: out.append('</ul></li>'); sub = False
        if liste: out.append('</ul>'); liste = False
    zeilen, n = text.splitlines(), 0
    while n < len(zeilen):
        z = zeilen[n]; n += 1
        if z.startswith('|'):
            zu(); tab = [z]
            while n < len(zeilen) and zeilen[n].startswith('|'): tab.append(zeilen[n]); n += 1
            out.append(tabelle(tab)); continue
        if not z.strip(): zu(); continue
        m = re.match(r'(#{2,4}) (.+)', z)
        if m: zu(); out.append(f'<h{len(m.group(1)) + 2}>{inline(m.group(2))}</h{len(m.group(1)) + 2}>'); continue
        m = re.match(r'(\s*)[-*] (.+)', z)
        if m:
            if m.group(1) and liste:
                if not sub: out[-1] = out[-1][:-5] + '<ul>'; sub = True
                out.append(f'<li>{inline(m.group(2))}</li>'); continue
            if sub: out.append('</ul></li>'); sub = False
            if not liste: out.append('<ul>'); liste = True
            out.append(f'<li>{inline(m.group(2))}</li>'); continue
        zu(); out.append(f'<p>{inline(z)}</p>')
    zu()
    return ''.join(out)
_md_ns = {'inline': inline, 'md': md, 'tabelle': tabelle}

_LINK = re.compile(r'\[([^\]]+)\]\(([^)\s]+)\)')
def _links(h): return _LINK.sub(lambda m: f'<a class="km-link" href="{m.group(2) if "://" in m.group(2) else "../docs/komponenten/" + m.group(2)}">{m.group(1)}</a>', h)
def inl(s): return _links(_md_ns['inline'](s))
_KENNUNG = ('klasse', 'klassen', 'token', 'tokens', 'kit-token', 'kern-token', 'modifier')
def _kopierspalte(h):
    """Tabellen mit Kennungs-Spalte (Klasse, Token): Kopieren-Knopf in einer Aktionsspalte rechts (Seitenregel „Aktionen rechts“), Wert erst beim Klick aus der Zeile."""
    kopf = [re.sub(r'<[^>]+>', '', x).strip().lower() for x in re.findall(r'<th>(.*?)</th>', h)]
    if not any(k in _KENNUNG for k in kopf): return h
    knopf = f'<td><span class="km-table__actions-row"><button type="button" class="km-iconbtn" data-kopieren aria-label="Kennung kopieren" title="Kennung kopieren">{ikon("copy")}</button></span></td>'
    return h.replace('</tr></thead>', '<th>Kopieren</th></tr></thead>', 1).replace('</td></tr>', '</td>' + knopf + '</tr>')

def code_box(code, cid, titel='Markup'):
    """Code-Block mit Kopieren oben rechts im Block (km-codeblock__box, km-codeblock__copy); die Seite kopiert den Text von #cid."""
    return (f'<div class="km-codeblock__box"><pre class="km-codeblock" id="{cid}" aria-label="{html.escape(titel)}"><code>{html.escape(code)}</code></pre>'
            f'<button type="button" class="km-iconbtn km-iconbtn--label km-codeblock__copy" data-copy="{cid}">{ikon("copy")}Kopieren</button></div>')

def md_html(zeilen):
    """Markdown eines Abschnitts: Text als Lesetext (km-prose), Tabellen als Standard-Tabelle, Code als km-codeblock."""
    out, rest, n = [], [], 0
    def flush():
        if rest and ''.join(rest).strip(): out.append('<div class="km-prose">' + _links(_md_ns['md']('\n'.join(rest))) + '</div>')
        rest.clear()
    while n < len(zeilen):
        z = zeilen[n]
        if z.startswith('```'):
            flush(); code = []; n += 1
            while n < len(zeilen) and not zeilen[n].startswith('```'): code.append(zeilen[n]); n += 1
            out.append('<pre class="km-codeblock"><code>' + html.escape('\n'.join(code)) + '</code></pre>'); n += 1; continue
        if z.startswith('|'):
            flush(); tab = []
            while n < len(zeilen) and zeilen[n].startswith('|'): tab.append(zeilen[n]); n += 1
            out.append(_kopierspalte(_md_ns['tabelle'](tab, inl)))
            continue
        rest.append(z); n += 1
    flush()
    return ''.join(out)

def _teile(text):
    """Markdown in (Titel, Kopfzeilen, {##: Zeilen}, {(##, ###): Zeilen})."""
    titel, kopf, teile, unter, akt, sub = '', [], {}, {}, None, None
    for z in text.splitlines():
        if z.startswith('# '): titel = z[2:].strip(); continue
        m = re.match(r'^(#{2,3}) (.+)$', z)
        if m and m.group(1) == '##': akt, sub = m.group(2).strip(), None; teile.setdefault(akt, []); continue
        if m and akt: sub = m.group(2).strip(); unter.setdefault((akt, sub), []); teile[akt] += ['', '## ' + sub, '']; continue
        if akt is None: kopf.append(z); continue
        teile[akt].append(z); unter.setdefault((akt, sub), []).append(z)
    return titel, kopf, teile, unter

def _fact(ic, label, wert, lang=False, span=1):
    return f'<div class="km-fact{f" km-fact--span-{span}" if span > 1 else ""}"><dt class="km-fact__label">{ikon(ic)}{label}</dt><dd class="km-fact__value{" km-fact__value--long" if lang else ""}">{wert}</dd></div>'

def karte(titel, ic, inhalt, art='paar'):
    kl = 'km-card km-card--accent-top' + (' km-card--span' if art == 'breit' else '') + {'Richtig': ' km-card--ok', 'Falsch': ' km-card--danger', 'Verwenden, wenn': ' km-card--ok', 'Nicht verwenden, wenn': ' km-card--danger'}.get(titel, '')
    return (f'<article class="{kl}"><div class="km-card__head"><span class="km-card__tile">{ikon(ic)}</span>'
            f'<h4 class="km-card__title">{html.escape(titel)}</h4></div>{inhalt}</article>')

# Kapitel: (Schlüssel, Titel, Icon, Regel-Präfix in „## Regeln“)
KAPITEL = [('was', 'Was ist es?', 'eye', 'Was'), ('wann', 'Wann nehmen?', 'circle-question-mark', 'Wann'),
           ('wie', 'Wie bauen?', 'hammer', 'Wie'), ('pruefen', 'Wie prüfen?', 'clipboard-check', 'Prüfen')]
# Rubrik: (Kapitel, Titel, Icon, [##-Abschnitte oder (Abschnitt, ###-Unterabschnitt)], Art); Art 'paar' (halbe Breite) oder 'breit'
RUBRIKEN = [
 ('was', 'Varianten', 'layers', ['Varianten'], 'paar'),
 ('was', 'Name und Abgrenzung', 'split', ['Name und Abgrenzung'], 'paar'),
 ('wann', 'Verwenden, wenn', 'circle-check', [('Einsatz', 'Verwenden, wenn'), ('Einsatz', None)], 'paar'),
 ('wann', 'Nicht verwenden, wenn', 'circle-x', [('Einsatz', 'Nicht verwenden, wenn')], 'paar'),
 ('wann', 'Verwandte Bausteine', 'component', ['Verwandte Bausteine'], 'paar'),
 ('wann', 'Vergleich mit anderen Design-Systemen', 'scale', ['Vergleich mit anderen Design-Systemen'], 'breit'),
 ('wie', 'Aufbau und Klassen', 'blocks', ['Aufbau', 'Aufbau und Größen', 'Aufbau und Zustände', 'Aufbau, Größen, Zustände'], 'breit'),
 ('wie', 'Text und Wording', 'type', ['Text und Wording'], 'paar'),
 ('wie', 'Tokens', 'palette', ['Tokens'], 'paar'),
 ('wie', 'Richtig', 'check', [('Beispiele', 'Richtig')], 'paar'),
 ('wie', 'Falsch', 'x', [('Beispiele', 'Falsch')], 'paar'),
 ('pruefen', 'Zustände', 'mouse-pointer-click', ['Zustände'], 'breit'),
 ('pruefen', 'Verhalten', 'workflow', ['Verhalten'], 'paar'),
 ('pruefen', 'Barrierefreiheit', 'accessibility', ['Barrierefreiheit'], 'paar'),
 ('pruefen', 'Größen', 'ruler', ['Größen'], 'paar'),
 ('pruefen', 'Bezug', 'link', ['Seitenregeln'], 'paar'),
]
_BEKANNT = {(h if isinstance(h, str) else h[0]) for *_, hs, _a in RUBRIKEN for h in hs} | {'Kurzbeschreibung', 'Beispiele', 'Verwendung', 'Offene Punkte', 'Regeln'}
_TAB = re.compile(r'<div class="km-table-wrap">.*?</table></div>', re.S)
SATZ = r'(?<![zZ]\.)(?<!\b[a-zA-Z]\.)(?<=[.!?])\s+(?=[A-ZÄÖÜ„`])'

def callout(ic, inhalt, art=''):
    return f'<aside class="km-callout{" km-callout--" + art if art else ""}">{ikon(ic)}<div class="km-prose">{inhalt}</div></aside>'

def doku_html(text, datei, anker_id):
    """{'titel', 'lead', 'mehr', 'fakten', 'offen', 'kapitel': {Schlüssel: Karten-HTML}, 'regeln': {Schlüssel: Kasten-HTML}}."""
    titel, kopf, teile, unter = _teile(text)
    voll = lambda zs: zs and ''.join(zs).strip()
    entsch = sorted({int(n) for n in re.findall(r'(?:Entscheidung(?:en)?|DDR|ADR) (\d+)', text)})
    kap = {k: [] for k, *_ in KAPITEL}
    for k, name, ic, hs, art in RUBRIKEN:
        zs = []
        for h in hs:
            if isinstance(h, str): zs += (['', f'## {h}', ''] if len([x for x in hs if isinstance(x, str) and voll(teile.get(x))]) > 1 and h != 'Aufbau' else []) + teile.get(h, []) if voll(teile.get(h)) else []
            elif voll(unter.get(h)): zs += unter[h]
        if name == 'Bezug': zs += sum((['', f'## {h}', ''] + teile[h] for h in teile if h not in _BEKANNT and voll(teile[h])), [])
        inhalt = md_html(zs) if voll(zs) else ''
        if name == 'Bezug' and entsch:
            inhalt += '<p class="km-chips">' + ''.join(f'<span class="km-chip">{ikon("scale")}Entscheidung {n}</span>' for n in entsch) + '</p>'
        if name == 'Aufbau und Klassen' and voll(teile.get('Verwendung')):  # Grundmarkup mit Kopieren im Block
            for n, c in enumerate(re.findall(r'```[a-z]*\n(.*?)\n```', '\n'.join(teile['Verwendung']), re.S)):
                inhalt += f'<h5 class="km-subhead">{ikon("code")}Grundmarkup</h5>' + code_box(c, f'md-{datei}-{n}', 'Grundmarkup')
            rest = re.sub(r'```.*?```', '', '\n'.join(teile['Verwendung']), flags=re.S)
            if rest.strip(): inhalt += md_html(rest.splitlines())
        if not inhalt: continue
        inhalt = re.sub(r'<h4>(.*?)</h4>', r'<h5 class="km-subhead">\1</h5>', inhalt)
        tabs = _TAB.findall(inhalt) if art == 'paar' else []
        if tabs:  # Tabellen gehen über die ganze Breite: eigene breite Karte direkt dahinter
            rest = re.sub(r'<(li|p)>Kontrast[^<]*:</\1>', '', _TAB.sub('', inhalt))  # Einleitungszeile der Tabelle wandert mit
            if re.sub(r'<[^>]+>', '', rest).strip(): kap[k].append(karte(name, ic, rest, art))
            kap[k].append(karte('Kontrast (gerechnet)' if name == 'Barrierefreiheit' else name + ': Übersicht', 'contrast' if name == 'Barrierefreiheit' else 'table', ''.join(tabs), 'breit'))
            continue
        kap[k].append(karte(name, ic, inhalt.replace('class="km-codeblock"', 'class="km-codeblock km-codeblock--wrap"') if art == 'paar' else inhalt, art))  # Beispiele in halben Karten umbrechen
    # Regel-Sätze je Kapitel aus „## Regeln“ (- Was: …, - Wann: …, - Wie: …, - Prüfen: …)
    regeln = {}
    for z in teile.get('Regeln', []):
        m = re.match(r'^- (Was|Wann|Wie|Prüfen):\s*(.+)$', z.strip())
        if m: regeln[next(k for k, *_r, p in KAPITEL if p == m.group(1))] = callout('bot', f'<p><strong>Regel:</strong> {inl(m.group(2))}</p>')
    offen = [z[2:].strip() for z in teile.get('Offene Punkte', []) if z.startswith('- ')]
    offen_html = callout('circle-alert', '<p><strong>Offene Punkte</strong></p><ul>' + ''.join(f'<li>{inl(x)}</li>' for x in offen) + '</ul>', 'attention') if offen else ''
    # Kopf: Lead aus der Kurzbeschreibung (ein bis zwei Sätze), Rest als Punkte in der Karte „Überblick“
    lead = ' '.join(z.strip() for z in teile.get('Kurzbeschreibung', []) if z.strip())
    s2 = re.split(SATZ, lead)
    lang = len(s2[0]) > 90 or len(s2) < 2
    lead, mehr = (s2[0], s2[1:]) if lang else (' '.join(s2[:2]), s2[2:])
    meta = dict((k.strip(), v.strip()) for k, v in (t.split(':', 1) for t in ' '.join(kopf).split(' · ') if ':' in t))
    # Kacheln in fester Reihenfolge, Raster lückenlos (DDR 48): Reihe 1 Status · Stand · Kontrast · Varianten, Reihe 2 Klassen | Quellen, Reihe 3 Stories
    klein, halb, ganz = [], [], []
    if meta.get('Status'):
        st, *rest = re.split(r'[;,]\s*', meta['Status'], maxsplit=1)
        klein.append(('flag', 'Status', inl(st.strip()) + (f'<small>{inl(rest[0])}</small>' if rest else ''), False))
    if meta.get('Stand'): klein.append(('calendar', 'Stand', re.sub(r'(\d{4})-(\d\d)-(\d\d)', r'\3.\2.\1', html.escape(meta['Stand'])), False))  # Datum TT.MM.JJJJ
    klein.append(None)  # Kontrast-Messung der Vorschau, füllt das Skript der Seite
    var = [z for z in teile.get('Varianten', []) if z.startswith('- ')]
    if var: klein.append(('layers', 'Varianten', str(len(var)), False))
    kl = re.findall(r'`([^`]+)`', titel)
    if kl: halb.append(('code', 'Klasse' if len(kl) == 1 else f'Klassen ({len(kl)})', ' '.join(f'<code class="km-chip km-chip--muted">{html.escape(k)}</code>' for k in kl), True))
    css = re.sub(r'^`src/km-components\.css`,?\s*', '', meta.get('CSS', ''))
    halb.append(('file-code', 'Quellen', f'<a class="km-link" href="../docs/komponenten/{datei}.md">{datei}.md</a> · <a class="km-link" href="../src/km-components.css">km-components.css</a>' + (f'<small>{inl(css)}</small>' if css else ''), True))
    st_links = [a for a in dict.fromkeys(re.findall(r'#([a-z0-9-]+)', meta.get('Story', ''))) if a in anker_id]
    if st_links: ganz.append(('book-open', 'Stories', ' '.join(f'<a class="km-chip" href="#" data-id="{anker_id[a][0]}">{html.escape(anker_id[a][1])}</a>' for a in st_links), True))
    f = []
    for reihe in (klein, halb, ganz):
        if not reihe: continue
        spans = [4 // len(reihe)] * len(reihe); spans[-1] += 4 - sum(spans)  # letzte Kachel streckt sich
        f += [f'<div class="km-fact{f" km-fact--span-{s}" if s > 1 else ""}" id="kontrast"></div>' if k is None else _fact(k[0], k[1], k[2], k[3], s) for k, s in zip(reihe, spans)]
    return {'titel': re.sub(r'\s*\(`.*$', '', titel), 'lead': inl(lead), 'mehr': [inl(x) for x in mehr], 'fakten': ''.join(f),
            'offen': offen_html, 'kapitel': {k: ''.join(v) for k, v in kap.items()}, 'regeln': regeln}

def kapitel_huelle(vor=None, nach=None):
    """Statische Hülle: vier Kapitel (km-doc__section mit km-doc__title--icon) und die Kapitelleiste (km-chapters__nav).
    vor, nach: {Schlüssel: HTML vor bzw. nach dem Karten-Raster}; Raster (#kap-<k>-karten) und Regel-Kasten (#kap-<k>-regel) füllt die Seite."""
    vor, nach = vor or {}, nach or {}
    sek = ''.join(f'<section class="km-doc__section" id="kap-{k}" aria-labelledby="kap-{k}-titel"><h3 class="km-doc__title km-doc__title--icon" id="kap-{k}-titel">{ikon(ic)}<span>{n + 1} · {t}</span></h3>'
                  f'{vor.get(k, "")}<div class="km-cards km-cards--two" id="kap-{k}-karten"></div>{nach.get(k, "")}<div id="kap-{k}-regel" hidden></div></section>'
                  for n, (k, t, ic, _p) in enumerate(KAPITEL))
    nav = ('<nav class="km-sidebar km-chapters__nav" aria-label="Kapitel"><div class="km-sidebar__group"><p class="km-sidebar__label">' + ikon('list-tree') + 'Kapitel</p>'
           + ''.join(f'<a class="km-sidebar__item" href="#kap-{k}"{" aria-current=\"location\"" if n == 0 else ""}>{ikon(ic)}<span>{n + 1} · {t}</span></a>' for n, (k, t, ic, _p) in enumerate(KAPITEL))
           + '</div></nav>')
    return sek, nav
