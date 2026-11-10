#!/usr/bin/env python3
"""Bettet Kernmix in eine Zielseite ein (Inhalt, nicht Link), zwischen <!-- KERN-SYSTEM:BEGIN/END --> im <head>.
Reihenfolge: KERN-Kit, km.css (Rollen + Bausteine), Theme. Beim ersten Lauf vor das erste <style> der Seite, damit
deren bisheriges CSS während der Umstellung noch Vorrang hat; danach wird nur der Block ersetzt.
Dazu ein kleines Skript, das data-theme="dark|light" der Seite auf data-kern-theme spiegelt (Dashboard und Lagebild schalten über data-theme).
--zusatz-theme NAME (mehrfach): weiteres Theme, eingebettet mit media="not all" (aus), die Seite schaltet über data-kern-theme-name um.
--schriften: @font-face aus dist/fonts.css mit Pfaden relativ zur Zielseite (Schriften bleiben in Kernmix, nur lokal lauffähig).
Aufruf: python3 tools/einbetten.py <ziel.html> [--theme kern-nah] [--zusatz-theme startklar] [--schriften] [--check]"""
import argparse, os, re, shutil, datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BEGIN, END = '<!-- KERN-SYSTEM:BEGIN', '<!-- KERN-SYSTEM:END -->'

ap = argparse.ArgumentParser()
ap.add_argument('ziel'); ap.add_argument('--theme', default='kern-nah'); ap.add_argument('--check', action='store_true')
ap.add_argument('--zusatz-theme', action='append', default=[]); ap.add_argument('--schriften', action='store_true')
a = ap.parse_args()
ziel = Path(a.ziel).resolve()
version = (ROOT / 'VERSION').read_text().strip(); kern = (ROOT / 'vendor/kern/VERSION').read_text().strip()
teile = [('KERN-Kit ' + kern, ROOT / 'vendor/kern/kern.min.css', ''), ('km.css', ROOT / 'dist/km.css', ''), ('Theme ' + a.theme, ROOT / f'dist/themes/{a.theme}.css', f' data-kern-theme-name="{a.theme}"' if a.zusatz_theme else '')]
teile += [('Theme ' + n, ROOT / f'dist/themes/{n}.css', f' data-kern-theme-name="{n}" media="not all"') for n in a.zusatz_theme]
def lies(p):
    s = p.read_text(encoding='utf-8')
    if p.name == 'fonts.css':  # Pfade von dist/ auf die Zielseite umrechnen
        s = s.replace('url("../assets/', 'url("' + os.path.relpath(ROOT / 'assets', ziel.parent).replace(os.sep, '/') + '/')
    return s.replace('</style', '<\\/style')
if a.schriften: teile.insert(0, ('Schriften', ROOT / 'dist/fonts.css', ''))
block = (f'{BEGIN} Kernmix {version} · KERN-Kit {kern} · Theme {" + ".join([a.theme] + a.zusatz_theme)} · eingebettet mit kernmix/tools/einbetten.py, nicht von Hand ändern -->\n'
         + ''.join(f'<style data-kern-system="{n}"{x}>\n{lies(p)}\n</style>\n' for n, p, x in teile)
         + '<script data-kern-system="km-table.js">\n' + (ROOT / 'dist/km-table.js').read_text(encoding='utf-8').replace('</script', '<\\/script') + '\n</script>\n'  # Tabellen-Bauweg kmTabelle (ADR „Eine Tabelle, ein Bauweg“)
         + '<script data-kern-system="km-popup.js">\n' + (ROOT / 'dist/km-popup.js').read_text(encoding='utf-8').replace('</script', '<\\/script') + '\n</script>\n'  # Esc und Klick daneben schließen jedes Panel
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
