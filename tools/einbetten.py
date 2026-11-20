#!/usr/bin/env python3
"""Bettet Kernmix in eine Zielseite ein (Inhalt, nicht Link), zwischen <!-- KERN-SYSTEM:BEGIN/END --> im <head>.
Reihenfolge: KERN-Kit, km.css (Rollen + Bausteine), Theme. Beim ersten Lauf vor das erste <style> der Seite, damit
deren bisheriges CSS während der Umstellung noch Vorrang hat; danach wird nur der Block ersetzt.
Dazu ein kleines Skript, das data-theme="dark|light" der Seite auf data-kern-theme spiegelt (Dashboard und Lagebild schalten über data-theme).
--zusatz-theme NAME (mehrfach): weiteres Theme, eingebettet mit media="not all" (aus), die Seite schaltet über data-kern-theme-name um.
--schriften: @font-face aus dist/fonts.css mit Pfaden relativ zur Zielseite (Schriften bleiben in Kernmix, nur lokal lauffähig).
--schlank: aus dem KERN-Kit nur Regeln, deren kern-*-Klassen die Zielseite (Markup und Skripte) verwendet; Bausteine (km.css) bleiben vollständig.
  Neue kern-*-Klassen in der Seite brauchen danach einen neuen Lauf.
Aufruf: python3 tools/einbetten.py <ziel.html> [--theme kern-nah] [--zusatz-theme startklar] [--schriften] [--schlank] [--check]"""
import argparse, os, re, shutil, datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BEGIN, END = '<!-- KERN-SYSTEM:BEGIN', '<!-- KERN-SYSTEM:END -->'

ap = argparse.ArgumentParser()
ap.add_argument('ziel'); ap.add_argument('--theme', default='kern-nah'); ap.add_argument('--check', action='store_true')
ap.add_argument('--zusatz-theme', action='append', default=[]); ap.add_argument('--schriften', action='store_true'); ap.add_argument('--schlank', action='store_true')
a = ap.parse_args()
ziel = Path(a.ziel).resolve()
version = (ROOT / 'VERSION').read_text().strip(); kern = (ROOT / 'vendor/kern/VERSION').read_text().strip()
teile = [('KERN-Kit ' + kern, ROOT / 'vendor/kern/kern.min.css', ''), ('km.css', ROOT / 'dist/km.css', ''), ('Theme ' + a.theme, ROOT / f'dist/themes/{a.theme}.css', f' data-kern-theme-name="{a.theme}"' if a.zusatz_theme else '')]
teile += [('Theme ' + n, ROOT / f'dist/themes/{n}.css', f' data-kern-theme-name="{n}" media="not all"') for n in a.zusatz_theme]
def _teile(sel):  # Selektorliste an Kommas außerhalb von Klammern trennen
    out, tiefe, start = [], 0, 0
    for i, ch in enumerate(sel):
        if ch == '(': tiefe += 1
        elif ch == ')': tiefe -= 1
        elif ch == ',' and tiefe == 0: out.append(sel[start:i]); start = i + 1
    return out + [sel[start:]]
def _pflicht(sel):  # kern-*-Klassen außerhalb von Klammern (:not/:is/:has bleiben unberücksichtigt, im Zweifel behalten)
    tiefe, ohne = 0, []
    for ch in sel:
        if ch == '(': tiefe += 1
        elif ch == ')': tiefe -= 1
        elif tiefe == 0: ohne.append(ch)
    return set(re.findall(r'\.(kern-[A-Za-z0-9_-]+)', ''.join(ohne)))
def schlank(css):
    seite = re.sub(re.escape(BEGIN) + r'.*?' + re.escape(END), '', ziel.read_text(encoding='utf-8'), flags=re.S)
    genutzt = set(re.findall(r'kern-[A-Za-z0-9_-]+', seite))
    praefixe = tuple(re.findall(r'''['"](kern-[A-Za-z0-9_-]*[-_])['"]''', seite))  # 'kern-x--' + wert
    ok = lambda k: k in genutzt or k.startswith(praefixe)
    css = re.sub(r'/\*(?!!).*?\*/', '', css, flags=re.S)
    def block(t):
        out, i = [], 0
        while i < len(t):
            j = t.find('{', i)
            if j < 0: out.append(t[i:]); break
            kopf = t[i:j]; tiefe, k = 1, j + 1
            while tiefe:
                tiefe += {'{': 1, '}': -1}.get(t[k], 0); k += 1
            innen = t[j + 1:k - 1]; kk = kopf.strip()
            if kk.startswith(('@media', '@supports', '@container', '@layer')) and '{' in innen:
                r = block(innen)
                if r.strip(): out.append(kopf + '{' + r + '}')
            elif kk.startswith('@'): out.append(kopf + '{' + innen + '}')
            else:
                behalten = [x for x in _teile(kopf) if all(ok(c) for c in _pflicht(x))]
                if behalten: out.append(','.join(behalten) + '{' + innen + '}')
            i = k
        return ''.join(out)
    return block(css)
def lies(p):
    s = p.read_text(encoding='utf-8')
    if a.schlank and p.name == 'kern.min.css': s = schlank(s)
    if p.name == 'fonts.css':  # Pfade von dist/ auf die Zielseite umrechnen
        s = s.replace('url("../assets/', 'url("' + os.path.relpath(ROOT / 'assets', ziel.parent).replace(os.sep, '/') + '/')
    return s.replace('</style', '<\\/style')
if a.schriften: teile.insert(0, ('Schriften', ROOT / 'dist/fonts.css', ''))
def vorladen():  # Schriften der eingebetteten Themes vorab anfordern (normaler Schnitt), sonst zeigt der Browser erst eine Ersatzschrift und Text bricht beim Tausch um (FOUT)
    if not a.schriften: return ''
    themes = ''.join((ROOT / f'dist/themes/{n}.css').read_text(encoding='utf-8') for n in [a.theme] + a.zusatz_theme)
    erste = set(re.findall(r'font-family[\w-]*:\s*"([^"]+)"', themes))  # nur die erste Schrift je Angabe, Ersatzschriften nicht
    out = []
    for f in re.findall(r'@font-face\s*{[^}]*}', lies(ROOT / 'dist/fonts.css')):
        fam = re.search(r'font-family:\s*"([^"]+)"', f); url = re.search(r'url\("([^"]+)"\)', f)
        if fam and url and 'italic' not in f and fam.group(1) in erste:
            typ = 'font/woff2' if url.group(1).endswith('.woff2') else 'font/ttf'
            out.append(f'<link rel="preload" as="font" type="{typ}" href="{url.group(1)}" crossorigin>\n')
    return ''.join(out)
block = (f'{BEGIN} Kernmix {version} · KERN-Kit {kern}{" schlank" if a.schlank else ""} · Theme {" + ".join([a.theme] + a.zusatz_theme)} · eingebettet mit kernmix/tools/einbetten.py, nicht von Hand ändern -->\n'
         + vorladen() + ''.join(f'<style data-kern-system="{n}"{x}>\n{lies(p)}\n</style>\n' for n, p, x in teile)
         + '<script data-kern-system="km-table.js">\n' + (ROOT / 'dist/km-table.js').read_text(encoding='utf-8').replace('</script', '<\\/script') + '\n</script>\n'  # Tabellen-Bauweg kmTabelle (ADR „Eine Tabelle, ein Bauweg“)
         + '<script data-kern-system="km-popup.js">\n' + (ROOT / 'dist/km-popup.js').read_text(encoding='utf-8').replace('</script', '<\\/script') + '\n</script>\n'
         + '<script data-kern-system="km-ansicht.js">\n' + (ROOT / 'dist/km-ansicht.js').read_text(encoding='utf-8').replace('</script', '<\\/script') + '\n</script>\n'  # hell/dunkel und Theme umschalten, vor dem ersten Zeichnen (kmAnsicht, 0.19.3)  # Esc und Klick daneben schließen jedes Panel
         + '<script>/* data-theme der Seite auf data-kern-theme spiegeln */(function(){var h=document.documentElement;function s(){var t=h.getAttribute("data-theme");if(t)h.setAttribute("data-kern-theme",t==="light"?"light":"dark");}s();new MutationObserver(s).observe(h,{attributes:true,attributeFilter:["data-theme"]});})();</script>\n'
         + END)
t = ziel.read_text(encoding='utf-8')
if BEGIN in t:
    neu = re.sub(re.escape(BEGIN) + r'.*?' + re.escape(END), lambda m: block, t, count=1, flags=re.S)
else:
    i = t.index('<style'); neu = t[:i] + block + '\n' + t[i:]
if neu == t:
    print('unverändert'); raise SystemExit(0)
if a.check:
    print('würde sich ändern'); raise SystemExit(1)
sich = ziel.parent / '_backups' if (ziel.parent / '_backups').is_dir() else ziel.parent
shutil.copy2(ziel, sich / f'{ziel.name}.vor-{dt.date.today():%Y-%m-%d}-kern-system')
ziel.write_text(neu, encoding='utf-8')
print(f'{ziel.name}: Kernmix {version} eingebettet ({len(block.encode()) // 1024} KB), Sicherung in {sich.name}/')
