#!/usr/bin/env python3
"""Prüft die System-Seiten headless (Komponentenbeschreibung, Doku):
- Fakten-Kacheln der Komponenten-Seite lückenlos (jede Reihe bis an den Rand, je Story);
- Kennungs-Spalten (Klasse, Token) in Mono und normal, Code in Zellen als Code (keine rohen Backticks);
- jede <table> ist die Standard-Tabelle: Klasse km-table, im Rahmen km-table-wrap, nach kmTabelle mit Icon in jeder Kopfzelle
  (Komponenten-Seite: alle Doku-Tabellen aus docs/komponenten/*.md, je Doku einmal gerendert);
- jeder Panel-Knopf (aria-haspopup, km-colpicker__btn) schließt mit Esc und mit Klick daneben, Fokus zurück;
- keine Schriftzeichen als Icon (×, ✕, ›, ↗, ★, ✓, ▸, ▾ …) in Knöpfen, Links, Etiketten, Köpfen und CSS-content (0.13.0);
- Navigation ohne eigene Regeln für Auswahl und Hover: kein Selektor der Seite mit :hover oder [aria-current|pressed|selected], der einen Link oder Knopf
  in einer <nav> trifft, ohne dass sein letztes Glied eine km-Klasse trägt;
- keine Skriptfehler.
Headless Chrome auf file://, ohne Server, nur Standardbibliothek. Aufruf: python3 tools/pruefe-seiten.py   (Ausgabe „FUNDE: 0“ = gut)."""
import html, os, re, shutil, subprocess, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
SEITEN = {'Komponenten': ROOT / 'storybook/index.html', 'Doku': ROOT / 'docs/index.html'}
JS = r"""<pre id="pf-out"></pre><script>setTimeout(function(){
  var o = [], stage = document.createElement('div');
  function tabellen(root, wo){ [].forEach.call(root.querySelectorAll('table'), function(t, n){
    if (t.closest('.doc-demo, .sb-buehne, iframe')) return;  /* Vorführungen von Bausteinen zählen nicht */
    var id = wo + ' #' + n + ' (' + (t.tHead && t.tHead.rows[0] ? t.tHead.rows[0].textContent.trim().slice(0, 40) : 'ohne Kopf') + ')';
    if (!t.classList.contains('km-table')) o.push('Tabelle ohne km-table: ' + id);
    if (!t.closest('.km-table-wrap')) o.push('Tabelle ohne Rahmen km-table-wrap: ' + id);
    if (t.tHead && t.tHead.rows[0]) [].forEach.call(t.tHead.rows[0].cells, function(th){ if (!th.querySelector('svg')) o.push('Kopf ohne Icon: ' + id + ' / ' + th.textContent.trim().slice(0, 30)); });
    /* Kennungs-Spalten (Klasse, Token) in Mono und normal, Code nie roh (Backticks) oder ohne Code-Schrift (0.11.0) */
    if (t.tHead && t.tHead.rows[0]) [].forEach.call(t.tHead.rows[0].cells, function(th, i){ if (!/^(klasse|klassen|token|tokens|kit-token|kern-token|modifier)$/i.test(th.textContent.trim())) return;
      [].forEach.call(t.tBodies[0] ? t.tBodies[0].rows : [], function(tr){ var c = tr.cells[i]; if (!c) return; var cs = getComputedStyle(c.querySelector('code') || c);
        if (!/mono/i.test(cs.fontFamily)) o.push('Kennung nicht in Mono: ' + id + ' / ' + c.textContent.trim().slice(0, 30));
        if (+cs.fontWeight >= 600) o.push('Kennung fett: ' + id + ' / ' + c.textContent.trim().slice(0, 30)); }); });
    [].forEach.call(t.querySelectorAll('td'), function(c){ if (c.textContent.indexOf('`') >= 0) o.push('Backticks roh in Zelle: ' + id + ' / ' + c.textContent.trim().slice(0, 30)); });
    [].forEach.call(t.querySelectorAll('td code'), function(c){ if (!/mono/i.test(getComputedStyle(c).fontFamily)) o.push('Code ohne Code-Schrift: ' + id + ' / ' + c.textContent.trim().slice(0, 30)); });
  }); }
  var daten = document.getElementById('daten'), D = null; try { D = JSON.parse(daten.textContent); } catch(e){}
  if (D && D.dokus){ document.body.appendChild(stage); Object.keys(D.dokus).forEach(function(k){ var dk = D.dokus[k]; stage.innerHTML = dk.offen + Object.keys(dk.kapitel).map(function(x){ return dk.kapitel[x]; }).join('') + Object.keys(dk.regeln).map(function(x){ return dk.regeln[x]; }).join(''); if (window.kmTabelle) [].forEach.call(stage.querySelectorAll('table.km-table'), function(t){ window.kmTabelle(t); }); tabellen(stage, 'Doku ' + k); }); stage.remove(); }
  tabellen(document, 'Seite');
  /* Schriftzeichen als Icon (0.13.0): Knöpfe, Links, Etiketten und Köpfe beginnen oder enden nicht mit ×, ✕, ›, ↗, ★, ✓, ▸, ▾ …; CSS-content ebenso. Lucide statt Zeichen */
  var ZEICHEN = /[×✕✖✗✘›‹»«↗↘↙↖→←↑↓⇄⇅★☆✓✔▸▾▴◂▶◀▲▼►◄⚙☐☑◎●○◉⌄⌃⋯⧉⎘]/;
  [].forEach.call(document.querySelectorAll('button, a, summary, [role="button"], [role="tab"], label, th, .km-chip, .km-pill, .km-iconbtn, .km-button, .km-sidebar__item, .km-corner__link, .km-subhead, .km-card__title'), function(el){
    var t = [].filter.call(el.childNodes, function(n){ return n.nodeType === 3; }).map(function(n){ return n.textContent; }).join('').trim();
    if (t && (ZEICHEN.test(t[0]) || ZEICHEN.test(t[t.length - 1]))) o.push('Schriftzeichen als Icon: ' + el.tagName.toLowerCase() + '.' + String(el.className.baseVal || el.className).split(' ')[0] + ' „' + t.slice(0, 30) + '“'); });
  [].forEach.call(document.querySelectorAll('body *'), function(el){ ['::before', '::after'].forEach(function(ps){ var c = getComputedStyle(el, ps).content; if (c && c !== 'none' && c !== 'normal' && ZEICHEN.test(c)) o.push('Schriftzeichen als Icon in CSS: ' + String(el.className.baseVal || el.className).split(' ')[0] + ps + ' ' + c); }); });
  /* Fakten-Kacheln lückenlos (DDR 48): je Story jede Kachelreihe bis an den rechten Rand gefüllt */
  /* Navigation nur mit Kit-Klassen (0.15.0): eigene Auswahl- oder Hover-Regeln der Seite (Inline-<style>) auf Links und Knöpfen in <nav> sind ein Fund */
  function teile(sel){ var r = [], t = 0, a = ''; for (var i = 0; i < sel.length; i++){ var c = sel[i]; if (c === '(' || c === '[') t++; if (c === ')' || c === ']') t--; if (c === ',' && !t){ r.push(a); a = ''; } else a += c; } r.push(a); return r.map(function(x){ return x.trim(); }); }
  function letztes(sel){ var t = 0, k = 0; for (var i = 0; i < sel.length; i++){ var c = sel[i]; if (c === '(' || c === '[') t++; if (c === ')' || c === ']') t--; if (!t && /[\s>+~]/.test(c)) k = i + 1; } return sel.slice(k); }
  function regeln(liste, f){ [].forEach.call(liste, function(r){ if (r.cssRules && !r.selectorText) regeln(r.cssRules, f); else if (r.selectorText) f(r.selectorText); }); }
  [].forEach.call(document.querySelectorAll('style'), function(st){ if (!st.sheet || st.closest('#daten')) return; regeln(st.sheet.cssRules, function(sel){ teile(sel).forEach(function(teil){
    if (!/:hover|\[aria-(current|pressed|selected)/.test(teil) || /\.km-/.test(letztes(teil))) return;
    var basis = teil.replace(/:hover|:focus-visible|:focus-within|:focus|:active|\[aria-(current|pressed|selected)[^\]]*\]/g, '').replace(/(^|[\s>+~])(?=[\s>+~]|$)/g, '$1*'); var els = []; try { els = document.querySelectorAll(basis); } catch (x){ return; }
    if ([].some.call(els, function(el){ return el.matches('a, button, summary, [role="link"], [role="tab"], [role="treeitem"]') && el.closest('nav, [role="navigation"]'); })) o.push('Navigation mit eigener Auswahl-/Hover-Regel statt Kit-Klasse: ' + teil); }); }); });
  var fk = document.getElementById('fakten'), baum = document.getElementById('sb-nav'), nk = 0;
  if (fk && baum) [].forEach.call(baum.querySelectorAll('a[data-id]'), function(a, n){ if (n > 90) return; a.click();
    var kids = [].filter.call(fk.children, function(c){ return c.getClientRects().length; }); if (!kids.length) return; nk++;
    var fr = fk.getBoundingClientRect(), reihen = {};
    kids.forEach(function(c){ var r = c.getBoundingClientRect(), k = Math.round(r.top); (reihen[k] = reihen[k] || []).push(r); });
    Object.keys(reihen).forEach(function(k){ var rechts = Math.max.apply(null, reihen[k].map(function(r){ return r.right; })); if (fr.right - rechts > 3) o.push('Kachelreihe mit Lücke: ' + a.textContent.trim() + ' (' + Math.round(fr.right - rechts) + ' px frei)'); }); });
  var seen = {}, knoepfe = [].filter.call(document.querySelectorAll('[aria-haspopup]:not([aria-haspopup="false"]), .km-colpicker__btn'), function(b){ var k = b.className; if (seen[k] || !b.getClientRects().length || b.closest('.doc-demo')) return false; return seen[k] = 1; });
  function ende(){ (window.__err || []).forEach(function(e){ if (!/replaceState|pushState/.test(e)) o.push('Skriptfehler: ' + e); });  /* Verlauf geht in der Prüfkopie (andere Adresse) nicht, das ist kein Fehler der Seite */ document.getElementById('pf-out').textContent = '@@' + o.join('\n') + '@@' + knoepfe.length + '##'; }
  function test(i){ if (i >= knoepfe.length) return ende(); var b = knoepfe[i], name = b.className.split(' ').pop(), auf = function(){ return b.getAttribute('aria-expanded') === 'true'; };
    b.click(); setTimeout(function(){ if (!auf()){ o.push('Panel öffnet nicht: ' + name); return test(i + 1); }
      (document.activeElement || document.body).dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', bubbles: true }));
      setTimeout(function(){ if (auf()) o.push('Esc schließt nicht: ' + name); else if (document.activeElement !== b) o.push('Esc: Fokus nicht zurück: ' + name);
        if (auf()) b.click(); b.click(); setTimeout(function(){ document.body.dispatchEvent(new PointerEvent('pointerdown', { bubbles: true })); document.body.click();
          setTimeout(function(){ if (auf()){ o.push('Klick daneben schließt nicht: ' + name); b.click(); } test(i + 1); }, 60); }, 60); }, 60); }, 60); }
  test(0);
}, 2000);</script>"""

funde, tmp = [], tempfile.mkdtemp(prefix='kmpruef-')
try:
    for name, pfad in SEITEN.items():
        t = pfad.read_text(encoding='utf-8')
        t = t.replace('<head>', '<head><base href="file://' + str(pfad.parent) + '/"><script>window.__err=[];addEventListener("error",function(e){__err.push(e.message)})</script>', 1)
        i = t.rindex('</body>'); t = t[:i] + JS + t[i:]  # letztes </body>: frühere stehen in JS-Strings (Story-Vorschau)
        kopie = Path(tmp) / (name + '.html'); kopie.write_text(t, encoding='utf-8')
        r = subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--user-data-dir=' + os.path.join(tmp, 'p-' + name), '--window-size=1400,900', '--virtual-time-budget=10000', '--timeout=60000', '--dump-dom', 'file://' + str(kopie)], capture_output=True, text=True, timeout=120)
        m = re.search(r'<pre id="pf-out">@@(.*?)@@(\d+)##</pre>', r.stdout, re.S)
        if not m: funde.append(f'{name}: keine Ausgabe von Chrome ' + (re.search(r'<pre id="pf-out">(.{0,200})', r.stdout, re.S) or [None, '?'])[1]); continue
        f = [x for x in html.unescape(m.group(1)).split('\n') if x.strip()]
        print(f'{name}: {len(f)} Funde, {m.group(2)} Panel-Knöpfe geprüft')
        funde += [f'{name}: {x}' for x in f]
finally:
    shutil.rmtree(tmp, ignore_errors=True)
for x in funde[:40]: print(' -', x)
if len(funde) > 40: print(f' … {len(funde) - 40} weitere')
print('FUNDE:', len(funde))
raise SystemExit(1 if funde else 0)
