#!/usr/bin/env python3
"""Baut dist/km.css aus src/km-core.css, src/km-roles.css und src/km-components.css (keine Abhängigkeiten).
Aufruf: python3 tools/build.py   — schreibt nur, wenn sich etwas ändert; meldet Größe und Prüfsumme."""
import hashlib
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
VERSION = (ROOT / 'VERSION').read_text().strip()
KERN = (ROOT / 'vendor/kern/VERSION').read_text().strip()
def schreiben(ziel, css):
    alt = ziel.read_text(encoding='utf-8') if ziel.exists() else ''
    if css != alt: ziel.write_text(css, encoding='utf-8')
    print(f'{ziel.relative_to(ROOT)} {len(css.encode()) / 1024:.1f} KB, sha256 {hashlib.sha256(css.encode()).hexdigest()[:12]}' + ('' if css != alt else ' (unverändert)'))


# KERN-Prüfung (ADR 43): jeder Bezug var(--kern-…) und jeder Wert, den ein Theme für --kern-… setzt, muss im eingebundenen Kit
# definiert sein. Nach einem Kit-Update meldet das umbenannte oder entfernte Tokens, statt dass Bausteine still auf den Rückfall fallen.
import re as _re
KERN_AUSNAHMEN = {  # Token: Begründung
    '--kern-typography-font-family-mono': 'Erweiterung im KERN-Schema: KERN kennt nur fira-mono; die Themes setzen die Mono-Schrift, km-roles.css fällt auf fira-mono zurück',
}
_kern_def = set(_re.findall(r'(--kern-[\w-]+)\s*:', (ROOT / 'vendor/kern/kern.min.css').read_text(encoding='utf-8')))
_kern_fehlt = []
for _f in sorted((ROOT / 'src').rglob('*.css')) + sorted((ROOT / 'src').rglob('*.js')):
    _t = _re.sub(r'/\*.*?\*/', '', _f.read_text(encoding='utf-8'), flags=_re.S)  # Kommentare zählen nicht
    for _n in sorted(set(_re.findall(r'var\(\s*(--kern-[\w-]+)', _t)) | set(_re.findall(r'(--kern-[\w-]+)\s*:', _t))):
        if _n not in _kern_def and _n not in KERN_AUSNAHMEN: _kern_fehlt.append(f'{_f.relative_to(ROOT)}: {_n}')
if _kern_fehlt:
    raise SystemExit(f'KERN-Prüfung: {len(_kern_fehlt)} Tokens fehlen in vendor/kern/kern.min.css {KERN} (umbenannt oder entfernt?):\n  ' + '\n  '.join(_kern_fehlt))
print(f'KERN-Prüfung: alle --kern-Bezüge in src/ im Kit {KERN} definiert ({len(KERN_AUSNAHMEN)} Ausnahme mit Begründung)')

kopf = lambda was: (f'/*! Kernmix {VERSION} · {was} · baut auf KERN-Kit (@kern-ux/native) {KERN} · EUPL-1.2\n'
                    f'    erzeugt mit tools/build.py aus src/ — nicht von Hand ändern. Reihenfolge: kern.min.css, km.css, Theme. */\n')
# Core Token (eigene Farbreihen) + Rollen-Tokens + Bausteine (ohne Theme: sieht aus wie Original-KERN)
schreiben(ROOT / 'dist/km.css', kopf('Rollen und Bausteine') + '\n'.join((ROOT / 'src' / f).read_text(encoding='utf-8') for f in ('km-core.css', 'km-roles.css', 'km-components.css')))
# Schriften: lokal, ohne fremde Server; nur Storybook, Doku und Online-Paket binden sie ein (eingebettete Seiten kennen den Pfad nicht)
schreiben(ROOT / 'dist/fonts.css', (ROOT / 'src/fonts.css').read_text(encoding='utf-8'))
# Themes: je Datei in src/themes/ eine Datei in dist/themes/
(ROOT / 'dist/themes').mkdir(exist_ok=True)
for th in sorted((ROOT / 'src/themes').glob('*.css')):
    schreiben(ROOT / 'dist/themes' / th.name, kopf(f'Theme {th.stem}') + th.read_text(encoding='utf-8'))

# Tabellen-Bauweg (kmTabelle): src/km-table.js mit eingesetzten Lucide-Icons nach dist/km-table.js
import json, re
_js = (ROOT / 'src/km-table.js').read_text(encoding='utf-8')
_luc = json.loads((ROOT / 'assets/lucide.json').read_text(encoding='utf-8'))
_namen = sorted(set(re.findall(r"\[\s*'([a-z0-9-]+)'\s*,", _js)) | {'wrench', 'mouse-pointer-click'})
_fehlt = [n for n in _namen if n not in _luc]
if _fehlt: raise SystemExit('km-table.js: Icons fehlen in lucide.json: ' + ', '.join(_fehlt))
_js = _js.replace('/*IKONEN*/{}', json.dumps({n: _luc[n]['i'] for n in _namen}, ensure_ascii=False, separators=(',', ':')))
schreiben(ROOT / 'dist/km-table.js', f'/*! Kernmix {VERSION} · kmTabelle · EUPL-1.2 · erzeugt mit tools/build.py aus src/km-table.js, nicht von Hand ändern */\n' + _js)

# Aufklappbares schließen (kmPopup): src/km-popup.js nach dist/km-popup.js
schreiben(ROOT / 'dist/km-popup.js', f'/*! Kernmix {VERSION} · kmPopup · EUPL-1.2 · erzeugt mit tools/build.py aus src/km-popup.js, nicht von Hand ändern */\n' + (ROOT / 'src/km-popup.js').read_text(encoding='utf-8'))
