/*! Kernmix 0.16.4 · kmTabelle · EUPL-1.2 · erzeugt mit tools/build.py aus src/km-table.js, nicht von Hand ändern */
/* Kernmix · Tabellen-Bauweg (kmTabelle), Entscheidung „Eine Tabelle, ein Bauweg“ (docs/entscheidungen).
   Richtet jede km-table nach ihren Spaltenköpfen und der Liste „Rolle je Spalte“ in docs/seitenregeln.md aus:
   Spaltenrollen, Kopf-Icons, Datum mit relativer Angabe und Aktivitätsbalken, Umfang, Aktionsspalte zuletzt,
   optional laufende Nummer und Sortierung. Ergänzt nur, was fehlt (mehrfach aufrufbar); markiert die Tabelle mit data-km-tabelle.
   Icons (Lucide 1.49.0, ISC) setzt tools/build.py aus assets/lucide.json ein. ES5, ohne Abhängigkeiten. */
(function(){
  var IKON = {"activity":"<path d=\"M22 12h-2.48a2 2 0 0 0-1.93 1.46l-2.35 8.36a.25.25 0 0 1-.48 0L9.24 2.18a.25.25 0 0 0-.48 0l-2.35 8.36A2 2 0 0 1 4.49 12H2\"/>","arrow-right-left":"<path d=\"m16 3 4 4-4 4\"/><path d=\"M20 7H4\"/><path d=\"m8 21-4-4 4-4\"/><path d=\"M4 17h16\"/>","book-open":"<path d=\"M12 5v16\"/><path d=\"M20.001 19A2 2 0 0022 17V5a2 2 0 00-1.999-2L16 3.002A5 5 0 0012 5a5 5 0 00-4-2H4a2 2 0 00-2 2v12a2 2 0 001.999 2H8a5 5 0 014 2 5 5 0 014-2z\"/>","bot":"<path d=\"M12 8V4H8\"/><rect width=\"16\" height=\"12\" x=\"4\" y=\"8\" rx=\"2\"/><path d=\"M2 14h2\"/><path d=\"M20 14h2\"/><path d=\"M15 13v2\"/><path d=\"M9 13v2\"/>","building":"<path d=\"M12 10h.01\"/><path d=\"M12 14h.01\"/><path d=\"M12 6h.01\"/><path d=\"M16 10h.01\"/><path d=\"M16 14h.01\"/><path d=\"M16 6h.01\"/><path d=\"M8 10h.01\"/><path d=\"M8 14h.01\"/><path d=\"M8 6h.01\"/><path d=\"M9 22v-3a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v3\"/><rect x=\"4\" y=\"2\" width=\"16\" height=\"20\" rx=\"2\"/>","calculator":"<rect width=\"16\" height=\"20\" x=\"4\" y=\"2\" rx=\"2\"/><line x1=\"8\" x2=\"16\" y1=\"6\" y2=\"6\"/><line x1=\"16\" x2=\"16\" y1=\"14\" y2=\"18\"/><path d=\"M16 10h.01\"/><path d=\"M12 10h.01\"/><path d=\"M8 10h.01\"/><path d=\"M12 14h.01\"/><path d=\"M8 14h.01\"/><path d=\"M12 18h.01\"/><path d=\"M8 18h.01\"/>","calendar":"<path d=\"M8 2v3\"/><path d=\"M16 2v3\"/><rect x=\"3\" y=\"3\" width=\"18\" height=\"18\" rx=\"2\"/><path d=\"M3 9h18\"/>","calendar-clock":"<path d=\"M16 14v2.2l1.6 1\"/><path d=\"M16 2v3\"/><path d=\"M21 7.338V5a2 2 0 00-2-2H5a2 2 0 00-2 2v14a2 2 0 002 2h2.338\"/><path d=\"M3 9h5.859\"/><path d=\"M8 2v3\"/><circle cx=\"16\" cy=\"16\" r=\"6\"/>","circle-alert":"<circle cx=\"12\" cy=\"12\" r=\"10\"/><line x1=\"12\" x2=\"12\" y1=\"8\" y2=\"12\"/><line x1=\"12\" x2=\"12.01\" y1=\"16\" y2=\"16\"/>","circle-question-mark":"<circle cx=\"12\" cy=\"12\" r=\"10\"/><path d=\"M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3\"/><path d=\"M12 17h.01\"/>","clipboard-check":"<rect width=\"8\" height=\"4\" x=\"8\" y=\"2\" rx=\"1\" ry=\"1\"/><path d=\"M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2\"/><path d=\"m9 14 2 2 4-4\"/>","clock-4":"<circle cx=\"12\" cy=\"12\" r=\"10\"/><path d=\"M12 6v6l4 2\"/>","code":"<path d=\"m16 18 6-6-6-6\"/><path d=\"m8 6-6 6 6 6\"/>","component":"<path d=\"M15.536 11.293a1 1 0 0 0 0 1.414l2.376 2.377a1 1 0 0 0 1.414 0l2.377-2.377a1 1 0 0 0 0-1.414l-2.377-2.377a1 1 0 0 0-1.414 0z\"/><path d=\"M2.297 11.293a1 1 0 0 0 0 1.414l2.377 2.377a1 1 0 0 0 1.414 0l2.377-2.377a1 1 0 0 0 0-1.414L6.088 8.916a1 1 0 0 0-1.414 0z\"/><path d=\"M8.916 17.912a1 1 0 0 0 0 1.415l2.377 2.376a1 1 0 0 0 1.414 0l2.377-2.376a1 1 0 0 0 0-1.415l-2.377-2.376a1 1 0 0 0-1.414 0z\"/><path d=\"M8.916 4.674a1 1 0 0 0 0 1.414l2.377 2.376a1 1 0 0 0 1.414 0l2.377-2.376a1 1 0 0 0 0-1.414l-2.377-2.377a1 1 0 0 0-1.414 0z\"/>","contrast":"<circle cx=\"12\" cy=\"12\" r=\"10\"/><path d=\"M12 18a6 6 0 0 0 0-12v12z\"/>","copy":"<rect width=\"14\" height=\"14\" x=\"8\" y=\"8\" rx=\"2\" ry=\"2\"/><path d=\"M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2\"/>","cpu":"<path d=\"M12 20v2\"/><path d=\"M12 2v2\"/><path d=\"M17 20v2\"/><path d=\"M17 2v2\"/><path d=\"M2 12h2\"/><path d=\"M2 17h2\"/><path d=\"M2 7h2\"/><path d=\"M20 12h2\"/><path d=\"M20 17h2\"/><path d=\"M20 7h2\"/><path d=\"M7 20v2\"/><path d=\"M7 2v2\"/><rect x=\"4\" y=\"4\" width=\"16\" height=\"16\" rx=\"2\"/><rect x=\"8\" y=\"8\" width=\"8\" height=\"8\" rx=\"1\"/>","database":"<ellipse cx=\"12\" cy=\"5\" rx=\"9\" ry=\"3\"/><path d=\"M3 5V19A9 3 0 0 0 21 19V5\"/><path d=\"M3 12A9 3 0 0 0 21 12\"/>","equal":"<line x1=\"5\" x2=\"19\" y1=\"9\" y2=\"9\"/><line x1=\"5\" x2=\"19\" y1=\"15\" y2=\"15\"/>","eye":"<path d=\"M2.062 12.348a1 1 0 0 1 0-.696 10.75 10.75 0 0 1 19.876 0 1 1 0 0 1 0 .696 10.75 10.75 0 0 1-19.876 0\"/><circle cx=\"12\" cy=\"12\" r=\"3\"/>","file":"<path d=\"M6 22a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8a2.4 2.4 0 0 1 1.704.706l3.588 3.588A2.4 2.4 0 0 1 20 8v12a2 2 0 0 1-2 2z\"/><path d=\"M14 2v5a1 1 0 0 0 1 1h5\"/>","file-check":"<path d=\"M6 22a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8a2.4 2.4 0 0 1 1.704.706l3.588 3.588A2.4 2.4 0 0 1 20 8v12a2 2 0 0 1-2 2z\"/><path d=\"M14 2v5a1 1 0 0 0 1 1h5\"/><path d=\"m9 15 2 2 4-4\"/>","file-text":"<path d=\"M6 22a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8a2.4 2.4 0 0 1 1.704.706l3.588 3.588A2.4 2.4 0 0 1 20 8v12a2 2 0 0 1-2 2z\"/><path d=\"M14 2v5a1 1 0 0 0 1 1h5\"/><path d=\"M10 9H8\"/><path d=\"M16 13H8\"/><path d=\"M16 17H8\"/>","flag":"<path d=\"M4 22V4a1 1 0 0 1 .4-.8A6 6 0 0 1 8 2c3 0 5 2 7.333 2q2 0 3.067-.8A1 1 0 0 1 20 4v10a1 1 0 0 1-.4.8A6 6 0 0 1 16 16c-3 0-5-2-8-2a6 6 0 0 0-4 1.528\"/>","folder":"<path d=\"M20 20a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.69-.9L9.6 3.9A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2Z\"/>","gauge":"<path d=\"m12 14 4-4\"/><path d=\"M3.34 19a10 10 0 1 1 17.32 0\"/>","hash":"<line x1=\"4\" x2=\"20\" y1=\"9\" y2=\"9\"/><line x1=\"4\" x2=\"20\" y1=\"15\" y2=\"15\"/><line x1=\"10\" x2=\"8\" y1=\"3\" y2=\"21\"/><line x1=\"16\" x2=\"14\" y1=\"3\" y2=\"21\"/>","key-round":"<path d=\"M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z\"/><circle cx=\"16.5\" cy=\"7.5\" r=\".5\" fill=\"currentColor\"/>","layers":"<path d=\"M12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83z\"/><path d=\"M2 12a1 1 0 0 0 .58.91l8.6 3.91a2 2 0 0 0 1.65 0l8.58-3.9A1 1 0 0 0 22 12\"/><path d=\"M2 17a1 1 0 0 0 .58.91l8.6 3.91a2 2 0 0 0 1.65 0l8.58-3.9A1 1 0 0 0 22 17\"/>","library":"<path d=\"m16 6 4 14\"/><path d=\"M12 6v14\"/><path d=\"M8 8v12\"/><path d=\"M4 4v16\"/>","link":"<path d=\"M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71\"/><path d=\"M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71\"/>","list":"<path d=\"M3 5h.01\"/><path d=\"M3 12h.01\"/><path d=\"M3 19h.01\"/><path d=\"M8 5h13\"/><path d=\"M8 12h13\"/><path d=\"M8 19h13\"/>","list-checks":"<path d=\"M13 5h8\"/><path d=\"M13 12h8\"/><path d=\"M13 19h8\"/><path d=\"m3 17 2 2 4-4\"/><path d=\"m3 7 2 2 4-4\"/>","lock":"<rect width=\"18\" height=\"11\" x=\"3\" y=\"11\" rx=\"2\" ry=\"2\"/><path d=\"M7 11V7a5 5 0 0 1 10 0v4\"/>","mouse-pointer-click":"<path d=\"M14 4.1 12 6\"/><path d=\"m5.1 8-2.9-.8\"/><path d=\"m6 12-1.9 2\"/><path d=\"M7.2 2.2 8 5.1\"/><path d=\"M9.037 9.69a.498.498 0 0 1 .653-.653l11 4.5a.5.5 0 0 1-.074.949l-4.349 1.041a1 1 0 0 0-.74.739l-1.04 4.35a.5.5 0 0 1-.95.074z\"/>","package":"<path d=\"M11 21.73a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73z\"/><path d=\"M12 22V12\"/><polyline points=\"3.29 7 12 12 20.71 7\"/><path d=\"m7.5 4.27 9 5.15\"/>","palette":"<path d=\"M12 22a1 1 0 0 1 0-20 10 9 0 0 1 10 9 5 5 0 0 1-5 5h-2.25a1.75 1.75 0 0 0-1.4 2.8l.3.4a1.75 1.75 0 0 1-1.4 2.8z\"/><circle cx=\"13.5\" cy=\"6.5\" r=\".5\" fill=\"currentColor\"/><circle cx=\"17.5\" cy=\"10.5\" r=\".5\" fill=\"currentColor\"/><circle cx=\"6.5\" cy=\"12.5\" r=\".5\" fill=\"currentColor\"/><circle cx=\"8.5\" cy=\"7.5\" r=\".5\" fill=\"currentColor\"/>","ruler":"<path d=\"M21.3 15.3a2.4 2.4 0 0 1 0 3.4l-2.6 2.6a2.4 2.4 0 0 1-3.4 0L2.7 8.7a2.41 2.41 0 0 1 0-3.4l2.6-2.6a2.41 2.41 0 0 1 3.4 0Z\"/><path d=\"m14.5 12.5 2-2\"/><path d=\"m11.5 9.5 2-2\"/><path d=\"m8.5 6.5 2-2\"/><path d=\"m17.5 15.5 2-2\"/>","scroll-text":"<path d=\"M15 12h-5\"/><path d=\"M15 8h-5\"/><path d=\"M19 17V5a2 2 0 0 0-2-2H4\"/><path d=\"M8 21h12a2 2 0 0 0 2-2v-1a1 1 0 0 0-1-1H11a1 1 0 0 0-1 1v1a2 2 0 1 1-4 0V5a2 2 0 1 0-4 0v2a1 1 0 0 0 1 1h3\"/>","server":"<rect width=\"20\" height=\"8\" x=\"2\" y=\"2\" rx=\"2\" ry=\"2\"/><rect width=\"20\" height=\"8\" x=\"2\" y=\"14\" rx=\"2\" ry=\"2\"/><line x1=\"6\" x2=\"6.01\" y1=\"6\" y2=\"6\"/><line x1=\"6\" x2=\"6.01\" y1=\"18\" y2=\"18\"/>","shield-check":"<path d=\"M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z\"/><path d=\"m9 12 2 2 4-4\"/>","square":"<rect width=\"18\" height=\"18\" x=\"3\" y=\"3\" rx=\"2\"/>","tag":"<path d=\"M12.586 2.586A2 2 0 0 0 11.172 2H4a2 2 0 0 0-2 2v7.172a2 2 0 0 0 .586 1.414l8.704 8.704a2.426 2.426 0 0 0 3.42 0l6.58-6.58a2.426 2.426 0 0 0 0-3.42z\"/><circle cx=\"7.5\" cy=\"7.5\" r=\".5\" fill=\"currentColor\"/>","target":"<circle cx=\"12\" cy=\"12\" r=\"10\"/><circle cx=\"12\" cy=\"12\" r=\"6\"/><circle cx=\"12\" cy=\"12\" r=\"2\"/>","text-align-start":"<path d=\"M21 5H3\"/><path d=\"M15 12H3\"/><path d=\"M17 19H3\"/>","timer":"<line x1=\"10\" x2=\"14\" y1=\"2\" y2=\"2\"/><line x1=\"12\" x2=\"15\" y1=\"14\" y2=\"11\"/><circle cx=\"12\" cy=\"14\" r=\"8\"/>","toggle-right":"<circle cx=\"15\" cy=\"12\" r=\"3\"/><rect width=\"20\" height=\"14\" x=\"2\" y=\"5\" rx=\"7\"/>","type":"<path d=\"M12 4v16\"/><path d=\"M4 7V5a1 1 0 0 1 1-1h14a1 1 0 0 1 1 1v2\"/><path d=\"M9 20h6\"/>","user":"<path d=\"M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2\"/><circle cx=\"12\" cy=\"7\" r=\"4\"/>","wrench":"<path d=\"M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.106-3.105c.32-.322.863-.22.983.218a6 6 0 0 1-8.259 7.057l-7.91 7.91a1 1 0 0 1-2.999-3l7.91-7.91a6 6 0 0 1 7.057-8.259c.438.12.54.662.219.984z\"/>"};
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
