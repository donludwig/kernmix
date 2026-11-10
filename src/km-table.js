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
    dateien: ['file', 'num'], anzahl: ['file', 'num'], stunden: ['timer', 'hours'],
    'letztes update': ['clock-4', 'date'], update: ['clock-4', 'date'], datum: ['calendar', 'date'],
    aktionen: ['mouse-pointer-click', 'actions'], kopieren: ['copy', 'actions'], werkzeug: ['wrench', ''],
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
  function datum(td){
    if (!td.getAttribute('data-sort')){ var s = iso(td.textContent); if (!s) return; td.setAttribute('data-sort', s); }
    var w = td.getAttribute('data-sort'), p = w.split(/[-T:]/);
    if (!td.querySelector('.km-table__date-rel')) td.textContent = p[2] + '.' + p[1] + '.' + p[0] + (p[3] ? ', ' + p[3] + ':' + p[4] : '');
    td.classList.add('km-table__date', 'km-table__nowrap');
    if (td.querySelector('.km-table__date-rel')) return;
    var heute = new Date(), h0 = new Date(heute.getFullYear(), heute.getMonth(), heute.getDate()), d = new Date(+p[0], +p[1] - 1, +p[2]);
    var diff = Math.round((h0 - d) / 86400000), rel = diff <= 0 ? 'heute' : diff === 1 ? 'gestern' : diff < 7 ? 'vor ' + diff + 'd' : diff < 30 ? 'vor ' + Math.floor(diff / 7) + 'w' : 'vor ' + Math.floor(diff / 30) + 'mo';
    var r = document.createElement('span'); r.className = 'km-table__date-rel'; r.textContent = '(' + rel + ')'; td.appendChild(r);
    var frisch = Math.max(0, 1 - diff / 30), bar = document.createElement('div'), fill = document.createElement('div');
    bar.className = 'km-table__activity'; fill.className = 'km-table__activity-fill';
    fill.style.width = Math.max(10, Math.round(frisch * 100)) + '%';
    fill.style.background = frisch > 0.7 ? 'var(--kern-color-feedback-success)' : frisch > 0.3 ? 'var(--km-color-attention)' : 'var(--kern-color-feedback-danger)';
    bar.appendChild(fill); td.appendChild(bar);
  }
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
    [].slice.call(tb.rows).sort(function(a, b){
      var x = a.cells[i], y = b.cells[i]; x = x ? (x.getAttribute('data-sort') || x.textContent.trim()) : ''; y = y ? (y.getAttribute('data-sort') || y.textContent.trim()) : '';
      var v = zahl ? (parseFloat(x) || 0) - (parseFloat(y) || 0) : x.localeCompare(y, 'de');
      return auf ? v : -v;
    }).forEach(function(r){ tb.appendChild(r); });
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
        if (r === 'date') return datum(c);
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
  window.kmTabelle.spalten = SPALTEN;
  window.kdTabelle = window.kmTabelle;  /* alter Name bis 0.6.0, bleibt als Alias */
})();
