/*! Kernmix 0.21.0 · kmAnsicht · EUPL-1.2 · erzeugt mit tools/build.py aus src/km-ansicht.js, nicht von Hand ändern */
/* kmAnsicht (0.19.3: „Switch hell/dunkel und Theme-Switch“, als Baustein statt je Seite): Knöpfe mit data-km-modus="light|dark"
   setzen data-kern-theme, Knöpfe mit data-km-theme="<name>" schalten zwischen den eingebetteten Themes (style[data-kern-theme-name], einbetten.py --zusatz-theme).
   Die Wahl gilt je Seite (localStorage km-ansicht:<Pfad>) und wird vor dem ersten Zeichnen angewendet; ?modus=light|dark in der Adresse geht vor und wird nicht gemerkt.
   Ein einzelner Knopf mit data-km-modus="wechsel" (km-iconbtn, Symbol sun-moon) schaltet um; so in der Seitenleiste (km-shell__controls, Vorbild Local AI Guide).
   Markup: <div class="km-segmented" role="group" aria-label="Modus"><button type="button" class="km-segmented__btn" data-km-modus="light">Hell</button>…</div> */
(function () {
  var root = document.documentElement, KEY = 'km-ansicht:' + location.pathname, url = new URLSearchParams(location.search).get('modus');
  function lies() { try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) { return {}; } }
  function themes() { return document.querySelectorAll('style[data-kern-theme-name], link[data-kern-theme-name]'); }
  function aktuell() { var t = [].filter.call(themes(), function (s) { return s.media !== 'not all'; })[0];
    return { modus: root.getAttribute('data-kern-theme') || (matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark'), theme: t ? t.getAttribute('data-kern-theme-name') : '' }; }
  function markieren() { var a = aktuell();
    [].forEach.call(document.querySelectorAll('[data-km-modus]:not([data-km-modus="wechsel"])'), function (b) { b.setAttribute('aria-pressed', String(b.getAttribute('data-km-modus') === a.modus)); });
    [].forEach.call(document.querySelectorAll('[data-km-theme]'), function (b) { b.setAttribute('aria-pressed', String(b.getAttribute('data-km-theme') === a.theme)); }); }
  function setzen(a) { if (url === 'light' || url === 'dark') a.modus = url; if (a.modus) root.setAttribute('data-kern-theme', a.modus);
    if (a.theme && [].some.call(themes(), function (s) { return s.getAttribute('data-kern-theme-name') === a.theme; }))
      [].forEach.call(themes(), function (s) { s.media = s.getAttribute('data-kern-theme-name') === a.theme ? 'all' : 'not all'; });
    markieren(); }
  setzen(lies());
  document.addEventListener('click', function (e) { var b = e.target.closest && e.target.closest('[data-km-modus], [data-km-theme]'); if (!b) return;
    var a = lies(); if (b.hasAttribute('data-km-modus')) { a.modus = b.getAttribute('data-km-modus') === 'wechsel' ? (aktuell().modus === 'dark' ? 'light' : 'dark') : b.getAttribute('data-km-modus'); url = null; } else a.theme = b.getAttribute('data-km-theme');
    try { localStorage.setItem(KEY, JSON.stringify(a)); } catch (x) {} setzen(a); });
  document.addEventListener('DOMContentLoaded', markieren);
  window.kmAnsicht = { setzen: function (a) { var b = lies(); for (var k in a) b[k] = a[k]; try { localStorage.setItem(KEY, JSON.stringify(b)); } catch (x) {} setzen(b); } };
})();
