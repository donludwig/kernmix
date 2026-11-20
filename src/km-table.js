/* Kernmix · Tabellen-Bauweg (kmTabelle), Entscheidung „Eine Tabelle, ein Bauweg“ (docs/entscheidungen).
   Richtet jede km-table nach ihren Spaltenköpfen und der Liste „Rolle je Spalte“ in docs/seitenregeln.md aus:
   Spaltenrollen, Kopf-Icons, Datum mit relativer Angabe und Aktivitätsbalken, Umfang, Aktionsspalte zuletzt,
   optional laufende Nummer und Sortierung. Ergänzt nur, was fehlt (mehrfach aufrufbar); markiert die Tabelle mit data-km-tabelle.
   Icons (Lucide 1.49.0, ISC) setzt tools/build.py aus assets/lucide.json ein. ES5, ohne Abhängigkeiten. */
(function(){
  var IKON = /*IKONEN*/{};
  // Kopfname (klein) → Lucide-Icon und Rolle; gleiche Spalte, gleiche Rolle auf allen Seiten
  var SPALTEN = {
    projekt: ['folder', 'name'], name: ['folder', 'name'], datei: ['file-text', 'name'], agent: ['bot', 'name'],
    typ: ['tag', 'nowrap'], organisation: ['building', 'nowrap'], kunde: ['building', 'nowrap'], modell: ['cpu', 'nowrap'],
    'was läuft': ['server', 'nowrap'], php: ['code', 'nowrap'], php2shell: ['shield-check', 'nowrap'], spuren: ['activity', 'nowrap'], score: ['gauge', 'nowrap'],
    schutz: ['lock', 'nowrap'], benutzer: ['user', 'nowrap'], passwort: ['key-round', 'nowrap'], links: ['link', 'nowrap'], wann: ['calendar-clock', 'nowrap'],
    phase: ['flag', 'nowrap'], status: ['flag', 'nowrap'],
    'tech stack': ['layers', 'text'], beschreibung: ['text-align-start', 'text'], darf: ['shield-check', 'text'], liefert: ['package', 'text'],
    was: ['file-text', 'text'], wie: ['wrench', 'text'], 'prüfung': ['shield-check', 'text'], 'maßnahmen': ['list-checks', 'text'], 'maßnahmen (punkte)': ['list-checks', 'text'],
    umfang: ['code', 'scope'], 'größe': ['database', 'scope'],
    dateien: ['file', 'num'], anzahl: ['file', 'num'], stunden: ['timer', 'hours'], vor: ['clock-arrow-left', 'since'], start: ['play', 'nowrap'], ende: ['square', 'nowrap'], /* Time Log */
    'letztes update': ['clock-4', 'date'], update: ['clock-4', 'date'], datum: ['calendar', 'date'],
    aktionen: ['mouse-pointer-click', 'actions'], kopieren: ['copy', 'actions'], werkzeug: ['wrench', 'nowrap'],
    /* Doku-Tabellen aus Markdown (Komponenten, Entscheidungen, Doku) */
    teil: ['component', 'name'], baustein: ['component', 'name'], story: ['book-open', 'name'], system: ['library', 'name'], 'fläche': ['square', 'name'], paar: ['contrast', 'name'], ebene: ['layers', 'name'], rolle: ['tag', 'name'],
    klasse: ['code', 'key'], klassen: ['code', 'key'], token: ['code', 'key'], tokens: ['code', 'key'], 'kit-token': ['code', 'key'], 'kern-token': ['code', 'key'], modifier: ['code', 'key'], anker: ['hash', 'key'],
    zustand: ['toggle-right', 'nowrap'], 'auslöser': ['mouse-pointer-click', 'nowrap'], farbe: ['palette', 'nowrap'], stufe: ['ruler', 'nowrap'], quelle: ['link', 'text'],
    funktion: ['text-align-start', 'text'], 'funktion / zustand': ['text-align-start', 'text'], darstellung: ['eye', 'text'], bedeutung: ['text-align-start', 'text'], besonderheit: ['text-align-start', 'text'], zweck: ['target', 'text'], 'wofür': ['target', 'text'], 'gleich gezeichnet wie': ['equal', 'text'], doku: ['file-text', 'text'], 'heimat-stories': ['book-open', 'text'],
    /* Fragebogen (Startklar, 0.10.0) */
    kriterium: ['clipboard-check', 'name'], 'nr.': ['hash', 'key'], punkte: ['calculator', 'nowrap'], pkt: ['calculator', 'num'], lesart: ['text-align-start', 'text'], 'verlangt von': ['link', 'text'],
    kennzahl: ['gauge', 'name'], 'wer schaut hin?': ['user', 'text'], 'zielwert (oder tbd)': ['target', 'text'], eintrag: ['list-checks', 'text'], 'wer klärt?': ['user', 'text'], 'bis wann?': ['calendar', 'nowrap'],
    kontrast: ['contrast', 'nowrap'], 'kobalt dunkel': ['contrast', 'num'], 'kobalt hell': ['contrast', 'num'], 'papier dunkel': ['contrast', 'num'], 'papier hell': ['contrast', 'num'],
    /* Komponenten-Doku Aufbau D */
    'text-regel': ['type', 'text'], bereich: ['layers', 'nowrap'], regel: ['scroll-text', 'text'], beleg: ['file-check', 'text'], fall: ['circle-question-mark', 'text'],
    stattdessen: ['arrow-right-left', 'text'], thema: ['tag', 'nowrap'], punkt: ['circle-alert', 'text'], art: ['tag', 'nowrap'], werte: ['list', 'text'],
    markup: ['code', 'text'], grund: ['text-align-start', 'text'], 'verwendet in': ['component', 'text']
  };
  function svg(n){ return IKON[n] ? '<svg class="km-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">' + IKON[n] + '</svg>' : ''; }
  function kopfName(th){ var t = ''; for (var k = th.firstChild; k; k = k.nextSibling){ if (k.nodeType === 3 || (k.nodeType === 1 && !k.classList.contains('km-table__tool') && !k.classList.contains('km-icon') && k.tagName !== 'svg')) t += k.textContent; } return t.replace(/\s+/g, ' ').trim().toLowerCase(); }
  function rolle(th){ if (th.classList.contains('km-table__actions')) return 'actions'; var s = SPALTEN[kopfName(th)]; return s ? s[1] : ''; }

  // Datum: „2026-09-10 09:03“, „2026-09-10T09:03“ oder „10.09.2026, 09:03“ → Text TT.MM.JJJJ, HH:MM, data-sort ISO
  function iso(t){ var m = t.match(/(\d{4})-(\d{2})-(\d{2})(?:[\sT](\d{2}):(\d{2}))?/); if (m) return m[1] + '-' + m[2] + '-' + m[3] + (m[4] ? 'T' + m[4] + ':' + m[5] : '');
    m = t.match(/(\d{2})\.(\d{2})\.(\d{4})(?:,?\s*(\d{2}):(\d{2}))?/); return m ? m[3] + '-' + m[2] + '-' + m[1] + (m[4] ? 'T' + m[4] + ':' + m[5] : '') : ''; }
  function datum(td, getrennt){ /* getrennt: Tabelle hat eine Spalte „Vor“, dann Datum mit Wochentag, Abstand und Balken stehen dort */
    if (!td.getAttribute('data-sort')){ var s = iso(td.textContent); if (!s) return; td.setAttribute('data-sort', s); }
    var w = td.getAttribute('data-sort'), p = w.split(/[-T:]/), d = new Date(+p[0], +p[1] - 1, +p[2]);
    if (!td.querySelector('.km-table__date-rel')) td.textContent = (getrennt ? ['So', 'Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa'][d.getDay()] + ', ' : '') + p[2] + '.' + p[1] + '.' + p[0] + (p[3] ? ', ' + p[3] + ':' + p[4] : '');
    td.classList.add('km-table__date', 'km-table__nowrap');
    if (getrennt || td.querySelector('.km-table__date-rel')) return;
    alter(td, d, true);
  }
  function alter(td, d, klammer){
    var heute = new Date(), h0 = new Date(heute.getFullYear(), heute.getMonth(), heute.getDate());
    var diff = Math.round((h0 - d) / 86400000), rel = diff <= 0 ? 'heute' : diff === 1 ? 'gestern' : diff < 7 ? 'vor ' + diff + 'd' : diff < 30 ? 'vor ' + Math.floor(diff / 7) + 'w' : 'vor ' + Math.floor(diff / 30) + 'mo';
    var r = document.createElement('span'); r.className = 'km-table__date-rel'; r.textContent = klammer ? '(' + rel + ')' : rel; td.appendChild(r);
    var frisch = Math.max(0, 1 - diff / 30), bar = document.createElement('div'), fill = document.createElement('div');
    bar.className = 'km-table__activity'; fill.className = 'km-table__activity-fill';
    fill.style.width = Math.max(10, Math.round(frisch * 100)) + '%';
    fill.style.background = frisch > 0.7 ? 'var(--kern-color-feedback-success)' : frisch > 0.3 ? 'var(--km-color-attention)' : 'var(--kern-color-feedback-danger)';
    bar.appendChild(fill); td.appendChild(bar);
  }
  /* Spalte „Vor“: wie lange her, als Text und Balken; Wert = Datum (data-sort oder Text) */
  function vor(td){ var w = td.getAttribute('data-sort') || iso(td.textContent); if (!w) return; td.setAttribute('data-sort', w); var p = w.split(/[-T:]/);
    td.textContent = ''; td.classList.add('km-table__date', 'km-table__nowrap'); alter(td, new Date(+p[0], +p[1] - 1, +p[2]), false); }
  // Umfang: „12,7 KB“, „~1,1k Zeilen“ → data-sort als Zahl
  function umfang(td){ td.classList.add('km-table__scope', 'km-table__nowrap'); if (td.getAttribute('data-sort')) return;
    var m = td.textContent.replace(/\s/g, ' ').match(/([\d.,]+)\s*(KB|MB|GB|B|k|M)?/); if (!m) return;
    var z = parseFloat(m[1].replace(/\./g, '').replace(',', '.')) || 0, f = { B: 1, KB: 1024, MB: 1048576, GB: 1073741824, k: 1000, M: 1000000 }[m[2]] || 1;
    td.setAttribute('data-sort', String(Math.round(z * f))); }

  function sortieren(t, th){
    var i = th.cellIndex, auf = th.getAttribute('aria-sort') !== 'ascending', tb = t.tBodies[0]; if (!tb) return;
    [].forEach.call(t.tHead.rows[0].cells, function(c){ if (c.classList.contains('km-table__sort')) c.setAttribute('aria-sort', 'none'); });
    th.setAttribute('aria-sort', auf ? 'ascending' : 'descending');
    var zahl = /^(scope|num|hours)$/.test(rolle(th));
    function vgl(a, b){
      var x = a.cells[i], y = b.cells[i]; x = x ? (x.getAttribute('data-sort') || x.textContent.trim()) : ''; y = y ? (y.getAttribute('data-sort') || y.textContent.trim()) : '';
      var v = zahl ? (parseFloat(x) || 0) - (parseFloat(y) || 0) : x.localeCompare(y, 'de');
      return auf ? v : -v;
    }
    // Gruppenzeilen (km-table__group) bleiben stehen, sortiert wird innerhalb jeder Gruppe
    var teile = [[]]; [].forEach.call(tb.rows, function(r){ if (r.classList.contains('km-table__group')) teile.push([r]); else teile[teile.length - 1].push(r); });
    teile.forEach(function(g){ var kopf = g[0] && g[0].classList.contains('km-table__group') ? g.shift() : null; if (kopf) tb.appendChild(kopf); g.sort(vgl).forEach(function(r){ tb.appendChild(r); }); });
  }

  window.kmTabelle = function(t, o){
    o = o || {}; if (!t || !t.tHead || !t.tHead.rows[0]) return t;
    var kopf = t.tHead.rows[0], ths = [].slice.call(kopf.cells);
    // Aktionsspalte immer zuletzt
    var ai = -1; ths.forEach(function(th, i){ if (rolle(th) === 'actions' || /^aktionen$/.test(kopfName(th))) ai = i; });
    if (ai >= 0 && ai !== ths.length - 1) [].forEach.call(t.rows, function(tr){ var c = tr.cells[ai]; if (c && tr.cells.length === ths.length) tr.appendChild(c); });
    ths = [].slice.call(kopf.cells);
    var rollen = ths.map(function(th){ var r = rolle(th); if (r === 'actions'){ th.classList.add('km-table__actions'); var n = kopfName(th) || 'Aktionen'; if (!th.querySelector('.kern-sr-only')){ th.textContent = ''; th.insertAdjacentHTML('beforeend', '<span class="kern-sr-only"></span>'); th.lastChild.textContent = n.charAt(0).toUpperCase() + n.slice(1); } } return r; });
    // Kopf-Icons
    ths.forEach(function(th){ if (th.querySelector(':scope > .km-icon, :scope > svg')) return; var s = SPALTEN[kopfName(th)] || (th.classList.contains('km-table__actions') ? SPALTEN.aktionen : null); if (s && IKON[s[0]]) th.insertAdjacentHTML('afterbegin', svg(s[0])); var tool = th.querySelector('.km-table__tool'); if (tool && !tool.querySelector('.km-icon')) tool.insertAdjacentHTML('afterbegin', svg('wrench')); });
    // Zellen nach Rolle
    [].forEach.call(t.tBodies, function(tb){ [].forEach.call(tb.rows, function(tr){
      if (tr.cells.length !== ths.length) return;
      [].forEach.call(tr.cells, function(c, i){ var r = rollen[i];
        if (r === 'actions'){ c.classList.add('km-table__actions'); return; }
        if (r === 'date') return datum(c, rollen.indexOf('since') >= 0);
        if (r === 'since') return vor(c);
        if (r === 'scope') return umfang(c);
        if (r === 'name'){ c.classList.add('km-table__nowrap'); if (!c.querySelector('.km-table__name') && c.textContent.trim()){ var n = document.createElement('span'); n.className = 'km-table__name'; while (c.firstChild) n.appendChild(c.firstChild); c.appendChild(n); } return; }  /* Name immer in km-table__name: Textschrift, kräftig (0.11.0) */
        if (r) c.classList.add('km-table__' + r);
        if (r === 'hours') c.classList.add('km-table__nowrap');
      });
    }); });
    if (o.nummern) t.classList.add('km-table--numbered');
    if (o.kompakt === false) t.classList.remove('km-table--compact');
    if (o.sortieren && !t.hasAttribute('data-km-sort')){
      t.setAttribute('data-km-sort', '1');
      ths.forEach(function(th, i){ if (rollen[i] === 'actions') return; th.classList.add('km-table__sort'); if (!th.hasAttribute('aria-sort')) th.setAttribute('aria-sort', 'none'); th.tabIndex = 0; });
      kopf.addEventListener('click', function(e){ var th = e.target.closest('th.km-table__sort'); if (th) sortieren(t, th); });
      kopf.addEventListener('keydown', function(e){ var th = e.target.closest('th.km-table__sort'); if (th && (e.key === 'Enter' || e.key === ' ')){ e.preventDefault(); sortieren(t, th); } });
    }
    t.setAttribute('data-km-tabelle', '1');
    return t;
  };
  // Für Seiten, die nur Kopf-Icons oder Rollen wollen (Projektübersicht mit eigener Sortierung)
  window.kmTabelle.kopfIcons = function(root){ [].forEach.call((root || document).querySelectorAll('table thead th'), function(th){ if (th.querySelector(':scope > .km-icon')) { var tl = th.querySelector('.km-table__tool'); if (tl && !tl.querySelector('.km-icon')) tl.insertAdjacentHTML('afterbegin', svg('wrench')); return; } var s = SPALTEN[kopfName(th)]; if (s && IKON[s[0]]) th.insertAdjacentHTML('afterbegin', svg(s[0])); var tool = th.querySelector('.km-table__tool'); if (tool && !tool.querySelector('.km-icon')) tool.insertAdjacentHTML('afterbegin', svg('wrench')); }); };
  window.kmTabelle.rollen = function(root){ [].forEach.call((root || document).querySelectorAll('table.km-table'), function(t){ if (!t.tHead || !t.tHead.rows[0]) return; var ths = [].slice.call(t.tHead.rows[0].cells), r = ths.map(rolle);
    [].forEach.call(t.tBodies, function(tb){ [].forEach.call(tb.rows, function(tr){ if (tr.cells.length !== ths.length) return; [].forEach.call(tr.cells, function(c, i){ var x = r[i]; if (!x || x === 'actions' || c.classList.contains('km-table__actions')) return; c.classList.add('km-table__' + (x === 'name' || x === 'date' || x === 'scope' || x === 'hours' ? 'nowrap' : x)); }); }); }); }); };
  // ── Spalten verschieben (0.17.0: „generell die Tabellen-Spalten verschiebbar“) ──
  // Reihenfolge nach Spaltennamen in localStorage[schluessel]; erste Spalte (Name) und Aktionen bleiben fest.
  // spaltenOrdnen stellt die gespeicherte Reihenfolge her und liefert perm (perm[neu] = alt) oder null; früh aufrufen,
  // bevor Seitenskripte Spaltennummern merken. spaltenZiehen macht die Köpfe ziehbar; spalteSchieben ist der Weg ohne Maus
  // (Hoch/Runter in der Spaltenauswahl, Seitenregel „Reihenfolge verwalten“). Beide stellen sofort um, lösen auf der Tabelle „km-spalten-verschoben“ aus (detail.perm) und rufen o.nachher(perm) auf.
  function namen(t){ return [].map.call(t.tHead.rows[0].cells, function(th){ return kopfName(th); }); }
  function fest(t, i){ var ths = t.tHead.rows[0].cells; return i === 0 || ths[i].classList.contains('km-table__actions') || rolle(ths[i]) === 'actions'; }
  function anwenden(t, perm){ // Zellen jeder vollständigen Zeile nach perm umstellen; Gruppenzeilen (colspan) bleiben
    [].forEach.call(t.rows, function(tr){ if (tr.cells.length !== perm.length) return; var c = [].slice.call(tr.cells); perm.forEach(function(alt){ tr.appendChild(c[alt]); }); });
  }
  function speichern(k, liste){ try { localStorage.setItem(k, JSON.stringify(liste)); } catch (e) {} }
  window.kmTabelle.spaltenOrdnen = function(t, k){
    if (!t || !t.tHead) return null; var n = namen(t), soll; try { soll = JSON.parse(localStorage.getItem(k)); } catch (e) {}
    if (!Array.isArray(soll)) return null;
    var frei = n.map(function(x, i){ return i; }).filter(function(i){ return !fest(t, i); });
    var rang = function(i){ var r = soll.indexOf(n[i]); return r < 0 ? 1e3 + i : r; };   // unbekannte Spalten hinten, in alter Folge
    var neu = frei.slice().sort(function(a, b){ return rang(a) - rang(b); });
    var perm = n.map(function(x, i){ return fest(t, i) ? i : neu[frei.indexOf(i)]; });
    if (perm.every(function(x, i){ return x === i; })) return null;
    anwenden(t, perm); return perm;
  };
  window.kmTabelle.spalteSchieben = function(t, k, von, nach, nachher){
    var n = namen(t); if (von === nach || fest(t, von) || fest(t, nach)) return;
    var perm = n.map(function(x, i){ return i; }); perm.splice(nach, 0, perm.splice(von, 1)[0]);
    speichern(k, perm.map(function(i){ return n[i]; }));
    anwenden(t, perm); // sofort umstellen, ohne Neuladen
    t.dispatchEvent(new CustomEvent('km-spalten-verschoben', { detail: { perm: perm } }));
    if (nachher) nachher(perm); // Seiten rechnen hier gemerkte Spaltennummern um (perm[neu] = alt)
  };
  // restSpalte (0.20.1, für km-table--knapp): die letzte sichtbare Spalte vor den Aktionen nimmt den freien Platz; nach Ausblenden oder Verschieben erneut aufrufen
  window.kmTabelle.restSpalte = function(t){ if (!t || !t.tHead) return; var ths = [].slice.call(t.tHead.rows[0].cells), rest = null;
    ths.forEach(function(th){ th.classList.remove('km-table__rest'); if (getComputedStyle(th).display !== 'none' && !th.classList.contains('km-table__actions')) rest = th; }); if (rest) rest.classList.add('km-table__rest'); };
  // breitenFest (0.20.1, für km-table--knapp): Breite jeder Spalte aus ALLEN Zeilen, auch gefilterten und eingeklappten, als feste Breite am Kopf;
  // so springen die Spalten nicht, wenn ein Filter (z. B. ein Kunde) andere Zeilen zeigt. Rest-Spalte und Aktionen bleiben frei. Nach Ausblenden, Verschieben und Größenänderung erneut aufrufen.
  window.kmTabelle.breitenFest = function(t, o){ if (!t || !t.tHead) return; var ths = [].slice.call(t.tHead.rows[0].cells), ohne = (o && o.ohne) || [], weg = [];
    // o.ohne: Klassen, mit denen die Seite Zeilen oder die Tabelle filtert (z. B. Kunde); fürs Messen kurz entfernt, damit auch diese Zeilen zählen
    if (ohne.length) [t].concat([].slice.call(t.querySelectorAll('tr'))).forEach(function(el){ ohne.forEach(function(k){ if (el.classList.contains(k)) { el.classList.remove(k); weg.push([el, k]); } }); });
    ths.forEach(function(th){ th.style.removeProperty('--km-th-min'); }); t.classList.add('km-table--messen');
    var w = ths.map(function(th){ return th.getBoundingClientRect().width; /* alle Spalten, auch Rest-Spalte und Aktionen: Mindestbreite aus allen Zeilen, Platz darüber hinaus nimmt die Rest-Spalte */ });
    t.classList.remove('km-table--messen'); weg.forEach(function(x){ x[0].classList.add(x[1]); }); ths.forEach(function(th, i){ if (!w[i]) return; var cs = getComputedStyle(th); th.style.setProperty('--km-th-min', Math.ceil(w[i] - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight)) + 'px'); }); };
  window.kmTabelle.spaltenUmstellen = function(zeilen, perm){ [].forEach.call(zeilen, function(tr){ if (tr.cells.length !== perm.length) return; var c = [].slice.call(tr.cells); perm.forEach(function(alt){ tr.appendChild(c[alt]); }); }); }; // für Kopien von Zeilen außerhalb der Tabelle
  window.kmTabelle.spaltenZiehen = function(t, o){
    o = o || {}; if (!t || !t.tHead || t.hasAttribute('data-km-ziehen')) return t; t.setAttribute('data-km-ziehen', '1');
    var kopf = t.tHead.rows[0], von = -1, linie = null;
    var idx = function(th){ return [].indexOf.call(kopf.cells, th); };
    var weg = function(){ if (linie) linie.classList.remove('km-table__drop--vor', 'km-table__drop--nach'); linie = null; };
    [].forEach.call(kopf.cells, function(th, i){ if (fest(t, i)) return; th.draggable = true; th.classList.add('km-table__th--ziehbar'); th.title = th.title || 'Ziehen, um die Spalte zu verschieben'; });
    kopf.addEventListener('dragstart', function(e){ var th = e.target.closest && e.target.closest('th'); if (!th || !th.draggable) return;
      von = idx(th); th.classList.add('km-table__th--zieht'); e.dataTransfer.effectAllowed = 'move'; try { e.dataTransfer.setData('text/plain', String(von)); } catch (x) {} });
    kopf.addEventListener('dragover', function(e){ var th = e.target.closest && e.target.closest('th'); if (von < 0 || !th) return; var i = idx(th); if (fest(t, i)) return weg();
      e.preventDefault(); var r = th.getBoundingClientRect(), vor = e.clientX < r.left + r.width / 2; weg(); linie = th; th.classList.add(vor ? 'km-table__drop--vor' : 'km-table__drop--nach'); });
    kopf.addEventListener('drop', function(e){ if (von < 0 || !linie) return; e.preventDefault(); var i = idx(linie), vor = linie.classList.contains('km-table__drop--vor');
      var nach = vor ? i : i + 1; if (nach > von) nach--; weg(); var v = von; von = -1; kmTabelle.spalteSchieben(t, o.schluessel, v, nach, o.nachher); });
    kopf.addEventListener('dragend', function(){ von = -1; weg(); [].forEach.call(kopf.cells, function(th){ th.classList.remove('km-table__th--zieht'); }); });
    return t;
  };
  // spaltenMenue verbindet Hoch/Runter in der Spaltenauswahl (Knöpfe mit data-schieben und data-col-von im Label der Spalte) mit spalteSchieben.
  // Nach jeder Verschiebung (auch per Ziehen) stellt es die Labels in die neue Folge, rechnet data-col-von um und lässt das Menü offen, Fokus bleibt auf dem Pfeil
  //. o: { schluessel, panel, nachher }.
  window.kmTabelle.spaltenMenue = function(t, o){
    var p = o && o.panel, zuletzt = null; if (!t || !p) return;
    p.addEventListener('click', function(e){ var b = e.target.closest('[data-schieben]'); if (!b) return; e.preventDefault(); e.stopPropagation();
      var v = +b.dataset.colVon; zuletzt = b; kmTabelle.spalteSchieben(t, o.schluessel, v, v + +b.dataset.schieben, o.nachher); zuletzt = null; });
    t.addEventListener('km-spalten-verschoben', function(e){ var perm = e.detail.perm, f = zuletzt || document.activeElement, letzte = t.tHead.rows[0].cells.length - 1;
      var labs = [].slice.call(p.querySelectorAll('label')).filter(function(l){ return l.querySelector('[data-schieben]'); }); if (!labs.length) return;
      var pos = function(l){ return +l.querySelector('[data-schieben]').dataset.colVon; }, ende = labs[labs.length - 1].nextSibling, eltern = labs[0].parentNode;
      labs.forEach(function(l){ var neu = perm.indexOf(pos(l)); [].forEach.call(l.querySelectorAll('[data-schieben]'), function(b){ b.dataset.colVon = neu; b.disabled = +b.dataset.schieben < 0 ? neu <= 1 : neu >= letzte - 1; }); });
      labs.sort(function(a, b){ return pos(a) - pos(b); }).forEach(function(l){ eltern.insertBefore(l, ende); });
      if (f && p.contains(f)) (f.disabled ? f.closest('label').querySelector('[data-schieben]:not(:disabled)') || f : f).focus(); }); // Verschieben im DOM nimmt den Fokus weg; der geklickte Pfeil zählt, auch wenn der Browser beim Klick nicht fokussiert (Firefox, Safari)
  };
  // leereAktionen blendet die Aktionsspalte aus, solange keine sichtbare Zeile Knöpfe darin hat, etwa nach einem Filter
  //. Klasse km-table--ohne-aktionen.
  window.kmTabelle.leereAktionen = function(t){
    if (!t || t.hasAttribute('data-km-leere-aktionen')) return t; t.setAttribute('data-km-leere-aktionen', '1'); var z;
    var pruefe = function(){ var hat = [].some.call(t.tBodies, function(tb){ return [].some.call(tb.rows, function(r){ var c = r.querySelector('td.km-table__actions');
      return c && r.getClientRects().length && [].some.call(c.querySelectorAll('a, button'), function(b){ return !b.hidden && getComputedStyle(b).display !== 'none'; }); }); });
      if (t.classList.contains('km-table--ohne-aktionen') === hat) t.classList.toggle('km-table--ohne-aktionen', !hat); }; // Knöpfe zählen, nicht ihre Fläche: in der ausgeblendeten Spalte haben sie keine
    new MutationObserver(function(){ clearTimeout(z); z = setTimeout(pruefe, 50); }).observe(t, { subtree: true, childList: true, attributes: true, attributeFilter: 'class hidden style'.split(' ') });
    window.addEventListener('load', pruefe); pruefe(); return t;
  };
  window.kmTabelle.spalten = SPALTEN;
  window.kdTabelle = window.kmTabelle;  /* alter Name bis 0.6.0, bleibt als Alias */
})();
