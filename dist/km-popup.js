/*! Kernmix 0.16.5 · kmPopup · EUPL-1.2 · erzeugt mit tools/build.py aus src/km-popup.js, nicht von Hand ändern */
/* Kernmix · Aufklappbares schließen (kmPopup): „Jedes Dropdown, Menü und Panel schließt mit Esc und mit Klick daneben, danach Fokus zurück auf den auslösenden Knopf.“
   Greift für jeden Knopf mit aria-expanded="true", der ein schwebendes Panel öffnet: aria-haspopup gesetzt, oder das Panel (aria-controls bzw. das nächste Geschwister) liegt absolut oder fest.
   Auf- und Zuklapp-Bereiche im Fluss (Seitenleisten-Gruppen, Karten, Bereiche) sind keine Panels und bleiben unberührt.
   Schließen läuft über einen Klick auf den Knopf (die Seite räumt ihren Zustand selbst auf); bleibt er offen, setzt kmPopup aria-expanded="false" und blendet das Panel aus.
   Dazu: schwebende Vorschau (km-peek) schließt mit Esc (WCAG 1.4.13). ES5, ohne Abhängigkeiten; einmal je Seite. */
(function(){
  if (window.kmPopup) return;
  function panel(b){
    var id = b.getAttribute('aria-controls'), p = id && document.getElementById(id);
    return p || b.nextElementSibling;
  }
  function schwebt(el){ if (!el || !el.getClientRects().length) return false; var s = getComputedStyle(el).position; return s === 'absolute' || s === 'fixed'; }
  function istPopup(b){
    if (b.closest('[aria-hidden="true"], [inert]')) return false;
    if (b.classList.contains('km-sidebar__toggle')) return false;  /* Seitenleiste ist kein Panel: seit sie fest steht (position: fixed), schloss jeder Klick daneben sie */
    var h = b.getAttribute('aria-haspopup');
    return (h && h !== 'false') || b.hasAttribute('data-km-popup') || schwebt(panel(b));
  }
  function offen(){ return [].slice.call(document.querySelectorAll('[aria-expanded="true"]')).filter(istPopup); }
  function drin(b, ziel){
    var p = panel(b);
    if (b.contains(ziel) || (p && p.contains(ziel))) return true;
    var box = b.closest('.km-colpicker, .km-selectpanel, [data-km-popup-root]');
    if (box && box.contains(ziel)) return true;
    var schwebend = ziel.closest && ziel.closest('[role="dialog"], [role="menu"], [role="listbox"], .km-selectpanel, .km-colpicker__panel');
    return !!(schwebend && schwebt(schwebend));  /* Klick in ein anderes offenes Panel (z. B. Untermenü) zählt nicht als daneben */
  }
  function zu(b, fokus){
    b.click();
    if (b.getAttribute('aria-expanded') === 'true'){ b.setAttribute('aria-expanded', 'false'); var p = panel(b); if (p && schwebt(p)) p.hidden = true; }
    if (fokus) setTimeout(function(){ if (b.isConnected) b.focus({ preventScroll: true }); }, 0);  /* nach dem Mausklick, der den Fokus sonst auf body setzt */
  }
  /* Esc im Bubbling am window: eigene Handler der Seite laufen zuerst und räumen auf; kmPopup schließt nur, was danach noch offen ist */
  window.addEventListener('keydown', function(e){
    if (e.key !== 'Escape' && e.key !== 'Esc') return;
    var peek = [].slice.call(document.querySelectorAll('.km-peek')).filter(function(x){ return x.getClientRects().length && !x.hidden; });
    peek.forEach(function(x){ x.hidden = true; });
    /* Begriff mit Erklärung (km-term, 0.10.0): Esc schließt die Erklärung, bis Fokus oder Maus den Begriff verlassen */
    var term = document.activeElement && document.activeElement.closest && document.activeElement.closest('.km-term');
    [].forEach.call(document.querySelectorAll('.km-term:hover'), function(x){ x.classList.add('km-term--closed'); });
    if (term) term.classList.add('km-term--closed');
    var o = offen(); if (!o.length) return;
    e.preventDefault();
    zu(o[o.length - 1], true);
  });
  document.addEventListener('pointerdown', function(e){
    offen().forEach(function(b){
      if (drin(b, e.target)) return;
      var a = document.activeElement, fokusDrin = a && a !== document.body && drin(b, a) && !b.contains(a);
      zu(b, fokusDrin);  /* Fokus nur zurück, wenn er im Panel lag; ein angeklicktes anderes Bedienelement bekommt ihn selbst */
    });
  }, true);
  /* Sprungnavigation: Klick auf einen Anker-Eintrag der Seitenleiste markiert ihn sofort (aria-current), nicht erst, wenn ein Beobachter nachzieht.
     Gescrollt wird ohne Animation (km.css setzt html { scroll-behavior: auto }). */
  document.addEventListener('click', function(e){
    var a = e.target.closest && e.target.closest('a.km-sidebar__item[href^="#"], button.km-sidebar__item[data-target]'); if (!a || (a.tagName === 'A' && a.getAttribute('href').length < 2)) return;
    var nav = a.closest('nav, .km-sidebar') || document;
    [].forEach.call(nav.querySelectorAll('.km-sidebar__item[aria-current]'), function(x){ if (x !== a) x.removeAttribute('aria-current'); });
    a.setAttribute('aria-current', 'location');
    if (a.closest('.km-chapters__nav, .km-shell__nav')) { ruhe = Date.now(); fest = a; setTimeout(kapitel, 0); }  /* geklicktes Kapitel bleibt markiert, bis wieder gescrollt wird */
  });
  /* Kapitelleiste (km-chapters__nav): markiert das Kapitel, dessen Anfang im oberen Drittel des Scrollbereichs steht
     (Fenster oder nächster scrollender Vorfahr). Ein Kapitel gilt erst als erreicht, wenn sein Anfang diese Linie passiert; auf kurzen Seiten wird das letzte
     deshalb nicht schon am unteren Ende markiert, sondern nur, wenn es die Linie erreicht oder angeklickt wurde. Ein geklicktes Kapitel bleibt markiert,
     bis selbst gescrollt wird (Rad, Wischen, Tasten). Ganz unten wird das letzte Kapitel markiert, dessen Anfang im Bild ist. Seiten, die Kapitel neu zeichnen oder ausblenden, rufen danach window.kmKapitel() auf. */
  var ruhe = 0, fest = null;
  function scroller(el){ for (var e = el.parentElement; e && e !== document.body && e !== document.documentElement; e = e.parentElement){ var o = getComputedStyle(e).overflowY; if (o === 'auto' || o === 'scroll') return e; } return null; }
  function kapitel(){
    var still = Date.now() - ruhe < 400;
    [].forEach.call(document.querySelectorAll('.km-chapters__nav, .km-shell__nav'), function(nav){
      var links = [].filter.call(nav.querySelectorAll('a.km-sidebar__item[href^="#"]'), function(a){ return !a.hidden && document.getElementById(a.getAttribute('href').slice(1)); });
      if (!links.length) return;
      var box = scroller(document.getElementById(links[0].getAttribute('href').slice(1))), oben = box ? box.getBoundingClientRect().top : 0, hoch = box ? box.clientHeight : innerHeight;
      var pos = box ? box.scrollTop : scrollY, akt = links[0];
      if (fest && links.indexOf(fest) >= 0) return;  /* geklicktes Ziel bleibt, bis selbst gescrollt wird (Rad, Wischen, Tasten); weiches Scrollen löst es nicht mehr */
      if (still) return;
      links.forEach(function(a){ var z = document.getElementById(a.getAttribute('href').slice(1)); if (z.getClientRects().length && z.getBoundingClientRect().top - oben <= hoch * 0.3) akt = a; });
      /* ganz unten: Ziele, die die Linie nie erreichen können, weil die Seite endet; markiert wird das letzte, dessen Anfang im Bild ist */
      var ende = box ? box.scrollHeight - box.clientHeight : document.documentElement.scrollHeight - innerHeight;
      if (pos >= ende - 2) links.forEach(function(a){ var z = document.getElementById(a.getAttribute('href').slice(1)); if (z.getClientRects().length && z.getBoundingClientRect().top - oben < hoch) akt = a; });
      [].forEach.call(nav.querySelectorAll('.km-sidebar__item'), function(a){ if (a === akt) a.setAttribute('aria-current', 'location'); else a.removeAttribute('aria-current'); });
    });
  }
  document.addEventListener('scroll', kapitel, { capture: true, passive: true });
  function selbst(e){ if (e.type === 'keydown' && !/^(Arrow|Page|Home|End| )/.test(e.key === ' ' ? ' ' : e.key)) return; if (fest && Date.now() - ruhe > 100) { fest = null; ruhe = 0; } }
  ['wheel', 'touchmove', 'keydown'].forEach(function(t){ addEventListener(t, selbst, { capture: true, passive: true }); });
  addEventListener('load', kapitel); addEventListener('resize', kapitel);
  window.kmKapitel = function(){ if (Date.now() - ruhe >= 400) fest = null; kapitel(); };  /* neu gezeichnet: Markierung aus der Lage, nicht aus einem alten Klick (außer direkt nach dem Klick) */
  function termAuf(e){ var x = e.target.closest && e.target.closest('.km-term'); if (x) x.classList.remove('km-term--closed'); }
  document.addEventListener('focusout', termAuf); document.addEventListener('mouseout', termAuf);
  window.kmPopup = { offen: offen, zu: zu };
})();
/* Bildvergrößerung (km-lightbox, 0.15.0): jedes Bild in einem Bereich mit data-km-lightbox öffnet groß;
   ←/→ blättern durch alle Bilder dieses Bereichs, Esc oder Klick daneben schließt. Großes Bild aus data-gross, sonst src. Eigener <dialog>, Fokus kehrt zurück. */
(function(){
  var dlg, bild, text, liste = [], pos = 0, zurueck = null;
  function bauen(){
    if (dlg) return;
    dlg = document.createElement('dialog'); dlg.className = 'km-lightbox'; dlg.setAttribute('aria-label', 'Bild vergrößert');
    dlg.innerHTML = '<figure class="km-lightbox__figur"><img class="km-lightbox__bild" alt=""><figcaption class="km-lightbox__text"></figcaption></figure>'
      + '<button type="button" class="km-lightbox__knopf km-lightbox__knopf--zurueck" aria-label="Vorheriges Bild">‹</button>'
      + '<button type="button" class="km-lightbox__knopf km-lightbox__knopf--weiter" aria-label="Nächstes Bild">›</button>'
      + '<button type="button" class="km-lightbox__knopf km-lightbox__knopf--zu" aria-label="Schließen">×</button>';
    document.body.appendChild(dlg);
    bild = dlg.querySelector('img'); text = dlg.querySelector('figcaption');
    dlg.addEventListener('click', function(e){
      if (e.target.closest('.km-lightbox__knopf--zurueck')) return zeigen(pos - 1);
      if (e.target.closest('.km-lightbox__knopf--weiter')) return zeigen(pos + 1);
      if (e.target === dlg || e.target.closest('.km-lightbox__knopf--zu') || e.target.classList.contains('km-lightbox__figur')) dlg.close();
    });
    dlg.addEventListener('keydown', function(e){ if (e.key === 'ArrowLeft') { e.preventDefault(); zeigen(pos - 1); } else if (e.key === 'ArrowRight') { e.preventDefault(); zeigen(pos + 1); } });
    dlg.addEventListener('close', function(){ if (zurueck) zurueck.focus(); });
  }
  function zeigen(i){
    pos = (i + liste.length) % liste.length; var q = liste[pos];
    bild.src = q.dataset.gross || q.currentSrc || q.src; bild.alt = q.alt || '';
    text.textContent = (q.alt || '') + (liste.length > 1 ? '  ·  ' + (pos + 1) + ' / ' + liste.length : '');
    dlg.classList.toggle('km-lightbox--einzeln', liste.length < 2);
  }
  document.addEventListener('click', function(e){
    var q = e.target.closest && e.target.closest('[data-km-lightbox] img:not([data-km-lightbox-ohne])'); if (!q || e.target.closest('a, button')) return;
    var feld = q.closest('[data-km-lightbox]'); liste = [].slice.call(feld.querySelectorAll('img:not([data-km-lightbox-ohne])')).filter(function(x){ return x.getClientRects().length; });
    bauen(); zurueck = q; zeigen(liste.indexOf(q)); dlg.showModal();
  });
  document.addEventListener('keydown', function(e){ if ((e.key === 'Enter' || e.key === ' ') && e.target.matches && e.target.matches('[data-km-lightbox] img:not([data-km-lightbox-ohne])')) { e.preventDefault(); e.target.click(); } });
  document.addEventListener('DOMContentLoaded', function(){ [].forEach.call(document.querySelectorAll('[data-km-lightbox] img:not([data-km-lightbox-ohne])'), function(q){ q.tabIndex = 0; q.setAttribute('role', 'button'); q.setAttribute('aria-label', 'Vergrößern: ' + (q.alt || 'Bild')); }); });
})();
