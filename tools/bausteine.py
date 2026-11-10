"""Gemeinsame Quelle der Kit-Bausteine (Werkzeug-Bausteine, Präfix km-): je Baustein Anker, Titel, Zweck, Markup.
Gelesen von tools/build-doku.py (Doku) und tools/build-storybook.py (Storybook)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IC = {k: v['i'] for k, v in json.loads((ROOT / 'assets/lucide.json').read_text(encoding='utf-8')).items()}  # Lucide 1.49.0


VORSCHAU = 'data:image/svg+xml;base64,' + __import__('base64').b64encode((ROOT / 'assets/vorschau-beispiel.svg').read_bytes()).decode()  # Standardbild für Stories, eingebettet, damit es in jeder Vorschau erscheint


def i(name, cls=''):
    c = f' class="km-icon {cls}"' if cls else ' class="km-icon"'
    return f'<svg{c} viewBox="0 0 24 24" aria-hidden="true">{IC[name]}</svg>'  # Strich, Enden, Ecken aus dem Theme (--km-icon-*)


# (Anker, Titel, Zweck, Markup)
BAUSTEINE = [
 ('seitenleiste', 'Seitenleiste', 'Navigation links: Gruppen mit Label, Einträge mit Icon, Farbpunkt oder Zähler. Zustände: Hover mit 8 % Akzent getönt, ausgewählt (<code>aria-pressed</code> bzw. <code>aria-current</code>) mit 16 % Tönung, Akzent-Text und Kante links, deaktiviert (<code>aria-disabled</code>) auf 40 % abgeblendet, wie in KERN (gilt für alle Bausteine). Fokus überall als Doppelring außen. Schalter als Eintrag (<code>role="switch"</code> mit <code>km-switch__knob</code>), Gruppen mit Aufklapp-Pfeil (<code>km-sidebar__label-btn</code>, <code>km-sidebar__caret</code>), Knopf zum Einklappen der Leiste (<code>km-sidebar__toggle</code>).', f'''<nav class="km-sidebar" aria-label="Beispiel-Navigation" style="max-width:15rem">
  <div class="km-sidebar__group">
    <p class="km-sidebar__label">{i('layout-grid')}Bereiche</p>
    <button type="button" class="km-sidebar__item" aria-pressed="true">{i('table','km-sidebar__icon')}Projektübersicht</button>
    <button type="button" class="km-sidebar__item">{i('zap','km-sidebar__icon')}Skills</button>
    <button type="button" class="km-sidebar__item">{i('keyboard','km-sidebar__icon')}Shortcuts</button>
    <button type="button" class="km-sidebar__item" aria-disabled="true">{i('shield','km-sidebar__icon')}Guardrails</button>
  </div>
  <div class="km-sidebar__group">
    <p class="km-sidebar__label">{i('layers')}Filter</p>
    <button type="button" class="km-sidebar__item" role="switch" aria-checked="true"><span class="km-switch__knob" aria-hidden="true"></span>Nur offene</button>
    <button type="button" class="km-sidebar__item" role="switch" aria-checked="false"><span class="km-switch__knob" aria-hidden="true"></span>Aktive</button>
  </div>
  <div class="km-sidebar__group">
    <p class="km-sidebar__label"><button type="button" class="km-sidebar__label-btn" aria-expanded="true">{i('user')}Kunden<span class="km-sidebar__caret" aria-hidden="true"></span></button></p>
    <button type="button" class="km-sidebar__item" style="--km-item-color:var(--km-color-tool-design)"><span class="km-sidebar__dot"></span>Kunde A<span class="km-sidebar__count">26</span></button>
    <button type="button" class="km-sidebar__item" style="--km-item-color:var(--km-color-accent)"><span class="km-sidebar__dot"></span>Kunde B<span class="km-sidebar__count">9</span></button>
  </div>
</nav>'''),
 ('bereich', 'Bereich', 'Die Wanne für jeden Abschnitt der Seite: dunkler als die Karten, mit Rand. Kopf als <code>&lt;summary&gt;</code> mit Icon, Titel samt Aufklapp-Pfeil, Zähler (<code>km-section__count</code>), Meta-Text und Griff zum Verschieben (<code>km-section__grip</code>, beim Ziehen <code>km-section--dragging</code>); Inhalt mit einheitlichem Innenabstand <code>--km-space-section-x</code> (24 px) seitlich und unten.', f'''<details class="km-section" open>
  <summary class="km-section__head"><span class="km-section__icon">{i('zap')}</span><h3 class="km-section__title">Skills</h3><span class="km-section__count">53</span><span class="km-section__meta">33 allgemein</span><span class="km-section__grip" title="Bereich verschieben">{i('grip-vertical')}</span></summary>
  <div class="km-section__body">
    <div class="km-card"><p class="km-card__text">Inhalt des Bereichs: Karten, Tabellen, Listen.</p></div>
  </div>
</details>'''),
 ('karte', 'Karte', 'Grundbaustein für Projekte, Skills, Guardrails, Synergien und Aufgaben. Varianten: Akzentkante oben oder links in der Projekt- bzw. Gruppenfarbe (<code>--km-card-accent</code>), interaktiv mit Hover.', f'''<div class="km-cards">
  <article class="km-card km-card--accent-top km-card--interactive">
    <div class="km-card__head"><span class="km-card__tile">{i('cloud-upload')}</span><div><h4 class="km-card__title">Hochladen</h4><code class="km-card__meta">hochladen</code></div></div>
    <p class="km-card__text">Zeigt genau, was hochgeht, wartet auf die Freigabe und prüft danach den Live-Stand.</p>
    <div class="km-card__foot"><span>Global</span><span>Stand 08.11.2026</span></div>
  </article>
  <article class="km-card km-card--accent-left" style="--km-card-accent:var(--km-color-accent)">
    <h4 class="km-card__title">Akzent links</h4>
    <p class="km-card__text">Für Regeln und Hinweise, etwa Guardrails.</p>
  </article>
</div>'''),
 ('projektkarte', 'Projektkarte', 'Zusammengesetzte Karte: Kopf mit Titel, Untertitel und Schlagworten (<code>km-card__subtitle</code>, <code>km-card__badges</code>), klappbar (<code>km-card--collapsible</code>, zu mit <code>km-card--collapsed</code>), darunter Einführung, Fakten, Flächen für Abschnitte (<code>km-panels</code>, <code>km-panel</code>) und Pfade als Chips. Akzent links in der Projektfarbe.', f'''<article class="km-card km-card--accent-left km-card--collapsible" style="--km-card-accent:var(--km-color-tool-design)">
  <div class="km-card__head"><div><h4 class="km-card__title">Kunde A · Projekt 11</h4><p class="km-card__subtitle">Mitfließender Aktions-Button für die mobile Ansicht</p></div><div class="km-card__badges"><span class="km-pill km-pill--neutral">Komponente</span><span class="km-pill km-pill--neutral">Mobil</span></div></div>
  <dl class="km-facts"><div class="km-fact"><dt class="km-fact__label">{i('flag')}Phase</dt><dd class="km-fact__value">Konzept</dd></div><div class="km-fact"><dt class="km-fact__label">{i('layers')}Typ</dt><dd class="km-fact__value km-fact__value--long">Komponente + Doku</dd></div><div class="km-fact"><dt class="km-fact__label">{i('clock')}Update</dt><dd class="km-fact__value">13 Tage<small>26.10.2026</small></dd><span class="km-fact__bar"><i style="width:56%"></i></span></div></dl>
  <div class="km-panels"><div class="km-panel"><h4>Nächste Schritte</h4><ul><li>Prototyp mit Team abstimmen</li><li>Doku-Entwurf ergänzen</li></ul></div><div class="km-panel"><h4>Offen</h4><ul><li>Verhalten auf kleinen Geräten</li></ul></div></div>
  <div class="km-chips"><a class="km-chip" href="#projektkarte">README öffnen</a><span class="km-chip km-chip--muted">~/projekte/projekt-11</span></div>
</article>'''),
 ('einfuehrung', 'Einführung', 'Bild, Lead-Satz und Text als eine Fläche. Ab 34rem Breite steht das Bild links (48 % der Karte, 240 bis 600 px, Quelle 1200 px für Retina), schmaler darüber. Langer Text wird nach fünf Zeilen gekürzt.', f'''<div class="km-intro" style="--km-card-accent:var(--km-color-tool-design)">
  <div class="km-intro__inner">
    <figure class="km-intro__media"><img src="{VORSCHAU}" alt="Vorschau des Projekts"></figure>
    <div class="km-intro__text">
      <p class="km-intro__lead">Ein Satz, der sagt, worum es geht.</p>
      <p class="km-intro__body km-intro__body--short">Danach der Rest: Stand, Werkzeuge, Entscheidungen. Er darf lang sein, die Karte kürzt ihn und bietet „Weiterlesen“ an. So bleibt die Übersicht ruhig, und wer mehr wissen will, klappt auf. Die Kürzung greift erst ab etwa 420 Zeichen, kurze Texte stehen vollständig da.</p>
      <button type="button" class="km-intro__more" aria-expanded="false">Weiterlesen</button>
    </div>
  </div>
</div>'''),
 ('fakten', 'Fakten-Kacheln', 'Kennzahlen-Streifen: Label klein oben, Wert groß (24 px), keine Flächen, nur Trennlinien. Frische als Balken über die ganze Kachelbreite unten (voll = heute, leer = vor 30 Tagen). Kacheln teilen sich die Breite und brechen nach Inhalt um.', f'''<dl class="km-facts" aria-label="Fakten zum Projekt" style="--km-card-accent:var(--km-color-tool-design)">
  <div class="km-fact"><dt class="km-fact__label">{i('flag')}Phase</dt><dd class="km-fact__value">Prototyp</dd></div>
  <div class="km-fact"><dt class="km-fact__label">{i('layers')}Typ</dt><dd class="km-fact__value">Komponente</dd></div>
  <div class="km-fact"><dt class="km-fact__label">{i('file-code')}Umfang</dt><dd class="km-fact__value">20,9k Z.</dd></div>
  <div class="km-fact"><dt class="km-fact__label">{i('clock')}Update</dt><dd class="km-fact__value">12 Tage<small>27.10.2026</small></dd><span class="km-fact__bar"><i style="width:60%"></i></span></div>
  <div class="km-fact"><dt class="km-fact__label">{i('hourglass')}Stunden</dt><dd class="km-fact__value">20,2 h</dd></div>
</dl>'''),
 ('aufgabe', 'Aufgabe', 'Aufgaben-Karte: Kästchen (<code>km-task__check</code>), Titel mit Kennung (<code>km-task__id</code>) und Status als Pill (offen = info, wartet = warn, erledigt = ok, überfällig = danger), Kurztext, nächster Schritt, Meta mit Projektlink, aufklappbare Details, Aktionsleiste unten mit <code>km-iconbtn</code>. Varianten: <code>--starred</code> (in Arbeit), <code>--dragging</code>. Erledigt: Text auf 40 % abgeblendet.', f'''<div style="max-width:30rem">
<div class="km-task km-task--starred">
  <input type="checkbox" class="km-task__check" aria-label="Erledigt: Nutzertest vorbereiten">
  <div class="km-task__body">
    <div class="km-task__title"><span>Nutzertest vorbereiten</span><span class="km-task__id">DEMO-1</span><span class="km-pill km-pill--info">in 4 Tagen</span></div>
    <p class="km-task__text">Fünf Termine, Aufgaben und Einwilligung vorbereiten.</p>
    <p class="km-task__next"><strong>Nächster Schritt:</strong> Aufgaben für den Test schreiben.</p>
    <div class="km-task__meta"><a class="km-chip" href="#aufgabe">Projekt 1</a></div>
    <details class="km-task__details"><summary>Details</summary><p>Weitere Notizen.</p></details>
  </div>
  <div class="km-task__actions"><button type="button" class="km-iconbtn" aria-label="Bearbeiten">{i('pen')}</button><button type="button" class="km-iconbtn km-iconbtn--attention" aria-pressed="true" aria-label="In Arbeit">{i('star')}</button><button type="button" class="km-iconbtn km-iconbtn--danger" aria-label="Löschen">{i('trash')}</button></div>
</div>
<div class="km-task">
  <input type="checkbox" class="km-task__check" checked aria-label="Erledigt: Bericht abgeben">
  <div class="km-task__body"><div class="km-task__title"><span>Bericht abgeben</span><span class="km-task__id">DEMO-2</span><span class="km-pill km-pill--ok">erledigt</span></div></div>
</div>
<div class="km-task">
  <input type="checkbox" class="km-task__check" aria-label="Erledigt: Interviews auswerten">
  <div class="km-task__body"><div class="km-task__title"><span>Interviews auswerten</span><span class="km-task__id">DEMO-3</span><span class="km-pill km-pill--warn">wartet</span></div>
    <details class="km-task__details" open><summary>Details</summary><p>Zustand „Details offen“: Notizen stehen unter der Zeile.</p></details>
  </div>
</div>
</div>'''),
 ('kuerzel', 'Kürzel-Karte', 'Shortcut als gefüllte Fläche in der Akzentfarbe, ohne Tasten-Unterkante. Variante <code>--attention</code> für Kürzel mit Wirkung nach außen (Freigabe).', f'''<div class="km-cards">
  <article class="km-card km-card--accent-top km-shortcut km-shortcut--attention">
    <div class="km-card__head" style="justify-content:space-between"><kbd class="km-shortcut__key">+fr</kbd><span class="km-card__tile">{i('badge-check')}</span></div>
    <p class="km-card__text">Freigabe der zuletzt gezeigten Liste, einmalig, nie pauschal.</p>
    <div class="km-card__foot"><a class="km-chip" href="#karte">Hochladen</a></div>
  </article>
  <article class="km-card km-card--accent-top km-shortcut">
    <div class="km-card__head" style="justify-content:space-between"><kbd class="km-shortcut__key">+za</kbd><span class="km-card__tile">{i('clipboard-copy')}</span></div>
    <p class="km-card__text">Text kopierfertig ausgeben und in die Zwischenablage legen.</p>
    <div class="km-card__foot"><a class="km-chip" href="#karte">Kopiertext</a></div>
  </article>
</div>'''),
 ('gruppe', 'Zwischenüberschrift, Hinweis, Farbpunkte', 'Innerhalb eines Bereichs: Zwischenüberschrift für eine Gruppe von Karten mit Zahl und Hinweis (<code>km-subhead</code>), Hinweistext (<code>km-note</code>) und Farbpunkte für beteiligte Projekte (<code>km-dots</code>, Farbe über <code>--km-dot-color</code>).', '''<h3 class="km-subhead">Allgemein <span>33</span><small>für alle Projekte nutzbar</small></h3>
<p class="km-note">Global = gilt in allen Projekten, Projekt = nur in einem Projekt.</p>
<p style="margin:0"><span class="km-dots"><i class="km-dots__dot" style="--km-dot-color:var(--km-color-tool-design)"></i><i class="km-dots__dot" style="--km-dot-color:var(--km-color-tool-chatgpt)"></i><i class="km-dots__dot" style="--km-dot-color:var(--km-color-accent)"></i></span> Gemeinsame Methodik</p>'''),
 ('chip-pill', 'Chip und Pill', 'Chip = Verweis auf etwas anderes (Link). Pill = Zustand, Farben aus den KERN-Feedback-Tokens.', '''<p style="display:flex;flex-wrap:wrap;gap:.5rem;margin:0">
  <a class="km-chip" href="#karte">Changelog pflegen</a>
  <span class="km-pill km-pill--ok">401 Passwort</span>
  <span class="km-pill km-pill--info">läuft</span>
  <span class="km-pill km-pill--warn">wartet</span>
  <span class="km-pill km-pill--danger">fehlt</span>
  <span class="km-pill km-pill--neutral">ruht</span>
</p>'''),
 ('schalter', 'Schalter und Demo', 'Schalter mit <code>role="switch"</code> und <code>aria-checked</code>. Der Demo-Schalter ist ein dezentes Kästchen mit Häkchen; mit <code>km-demo--fixed</code> sitzt er fest unten links in der Fensterecke und wechselt zur Demo-Fassung mit erfundenen Daten.', '''<p style="display:flex;flex-wrap:wrap;gap:1.5rem;align-items:center;margin:0">
  <button type="button" class="km-switch" role="switch" aria-checked="true"><span class="km-switch__knob" aria-hidden="true"></span>Aufgaben</button>
  <button type="button" class="km-switch" role="switch" aria-checked="false"><span class="km-switch__knob" aria-hidden="true"></span>Nur offene</button>
  <button type="button" class="km-demo" role="switch" aria-checked="false"><i aria-hidden="true"></i>Demo</button>
  <button type="button" class="km-demo" role="switch" aria-checked="true"><i aria-hidden="true"></i>Demo</button>
</p>'''),
 ('eckleiste', 'Eckleiste', 'Dezente Werkzeug-Einträge fest unten links in der Fensterecke: Demo-Schalter und Links wie zur Komponentenbeschreibung. Klein und gedämpft, beim Zeigen hell. Im Dokument fließt sie hier zur Ansicht mit (position: static).', f'''<div class="km-corner" style="position:static">
  <button type="button" class="km-demo km-demo--fixed" role="switch" aria-checked="false"><i aria-hidden="true"></i>Demo</button>
  <a class="km-corner__link" href="#eckleiste">{i('book-open')}Komponentenbeschreibung</a>
</div>'''),
 ('suche', 'Suche: Filter und Ergebnisse', 'Aktive Filter als Chips im Suchfeld (<code>km-filterchips__chip</code>, ausgeschlossen mit <code>__neg</code>), darunter die Ergebnisliste nach Typ gruppiert (<code>km-results__group</code>, Farbe über <code>--sr-color</code>) mit Treffern (<code>km-results__item</code>).', f'''<div style="max-width:34rem">
<div class="km-toolbar" style="margin-bottom:.5rem"><div class="km-filterchips"><span class="km-filterchips__chip">kunde:A</span><span class="km-filterchips__chip km-filterchips__neg">-tag:alt</span></div></div>
<div class="km-results" style="position:static;display:block">
  <div class="km-results__group" style="--sr-color:var(--km-color-accent)">Projekte <span>2</span></div>
  <div class="km-results__item"><span class="km-results__type" style="color:var(--km-color-accent)">{i('folder')}</span><a class="km-results__name" href="#suche">Projekt 1</a><span class="km-results__kunde">Kunde A</span><span class="km-results__snip">… Formular mit Fehlermeldungen …</span></div>
  <div class="km-results__item"><span class="km-results__type" style="color:var(--km-color-accent)">{i('folder')}</span><a class="km-results__name" href="#suche">Projekt 2</a><span class="km-results__kunde">Kunde A</span><span class="km-results__snip">… Formular im Konto …</span></div>
  <div class="km-results__more">… 3 weitere in der Tabelle</div>
</div></div>'''),
 ('quicklinks', 'Quicklinks', 'Angeheftete Projekte im Kopf als Pillen mit Monogramm, Name, Kopieren und Entfernen (<code>km-quicklinks__pill</code>); leer mit Hinweis (<code>__empty</code>).', f'''<nav class="km-quicklinks" aria-label="Quicklinks"><span class="km-quicklinks__pill"><button type="button" class="km-quicklinks__pill-copy"><span class="km-monogram km-quicklinks__pill-icon" style="--km-monogram-color:var(--km-color-tool-design)">P1</span><span class="km-quicklinks__pill-name">Projekt 1</span>{i('copy')}</button><button type="button" class="km-quicklinks__pill-remove" aria-label="Lösen"></button></span><span class="km-quicklinks__pill"><button type="button" class="km-quicklinks__pill-copy"><span class="km-monogram km-quicklinks__pill-icon" style="--km-monogram-color:var(--km-color-accent)">P2</span><span class="km-quicklinks__pill-name">Projekt 2</span>{i('copy')}</button><button type="button" class="km-quicklinks__pill-remove" aria-label="Lösen"></button></span></nav>
<nav class="km-quicklinks" aria-label="Quicklinks leer" style="margin-top:1rem"><span class="km-quicklinks__empty">Projekte unten mit + hier anheften</span></nav>'''),
 ('kennzahlen', 'Fußzeile mit Kennzahlen', 'Kennzahlen und Verteilungsbalken aus Farbflächen (Segment mit <code>flex</code> = Anteil), dazu Verteilung als Balken (<code>km-histo</code>: Beschriftung, Balken, Wert) am Seitenende (<code>km-bars__line</code>, <code>__bar</code>, <code>__legend</code>, <code>__key</code>, <code>__sw</code>, <code>__pct</code>).', '''<div class="km-bars"><div class="km-bars__line"><span class="km-bars__bar" aria-hidden="true"><span style="flex:12;background:var(--km-color-accent)"></span><span style="flex:8;background:var(--km-color-tool-design)"></span></span><span class="km-bars__legend"><span class="km-bars__key"><span class="km-bars__sw" style="background:var(--km-color-accent)"></span>Persönlich <strong>12</strong> <span class="km-bars__pct">60%</span></span><span class="km-bars__key"><span class="km-bars__sw" style="background:var(--km-color-tool-design)"></span>Kunde A <strong>8</strong> <span class="km-bars__pct">40%</span></span></span></div></div>'<h4 style="margin:var(--km-space-block) 0 var(--km-space-stack);font-size:var(--km-font-size-xs)">Chats pro Monat (km-histo)</h4><div class="km-histo" style="max-width:24rem"><span class="km-histo__label">2026-02</span><span class="km-histo__bar"><i style="width:40%"></i></span><span class="km-histo__value">2</span><span class="km-histo__label">2026-03</span><span class="km-histo__bar"><i style="width:100%"></i></span><span class="km-histo__value">5</span></div>'''),
 ('agent', 'Agenten-Karte', 'Karte für einen Agenten: Symbol, Name, Rolle, Beschreibung, Befehle (<code>km-agent__card</code>, <code>__header</code>, <code>__icon</code>, <code>__name</code>, <code>__role</code>, <code>__desc</code>, <code>__commands</code>, <code>__cmd</code>).', '''<div class="km-agent__card" style="max-width:24rem"><div class="km-agent__header"><div class="km-agent__icon"><svg class="km-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="m12 14 4-4"/><path d="M3.34 19a10 10 0 1 1 17.32 0"/></svg></div><div><div class="km-agent__name">Cockpit</div><div class="km-agent__role">Koordinator</div></div></div><p class="km-agent__desc">Steuert die anderen Agenten und priorisiert.</p><div class="km-agent__commands"><h4>Aktivierung</h4><div class="km-agent__cmd"><code>/cockpit</code> <span>— Skill-Modus</span></div></div></div>'''),
 ('grafik', 'Grafik „Wer ruft wen auf“', 'Vom Generator gezeichnete SVG-Grafik mit Knoten, Kanten, Legende und Filterknöpfen (<code>km-graph</code>, <code>km-graph__svg</code>, <code>__n</code>, <code>__e</code>, <code>__legende</code>, <code>__katknopf</code>). Gezeichnet von <code>grafik()</code> in <code>project-dashboard/tools/build-skills.py</code>; in der Komponentenbeschreibung mit erfundenen Beispieldaten, gleiche Zeichnung und Interaktion wie im Dashboard.', '''<div class="km-graph__legende"><button type="button" class="km-graph__katknopf" aria-pressed="false"><i style="background:var(--km-color-accent)"></i>Texte</button><button type="button" class="km-graph__katknopf" aria-pressed="true"><i style="background:var(--km-color-attention)"></i>Veröffentlichung</button></div>'''),
 ('segmented', 'Segmented Control', 'Zwei bis fünf gleichrangige Ansichten umschalten (Button-Gruppe, <code>aria-pressed</code>), z. B. Karten/Zeitlich, Projekte/Kunden/Aktiv. Aus dem Proposal übernommen (KERN-Issue 1141).', '''<div style="display:flex;flex-direction:column;align-items:flex-start;gap:1.25rem;font-family:var(--km-font);color:var(--km-color-text)">
  <div class="km-segmented" role="group" aria-label="Ansicht">
    <button type="button" class="km-segmented__btn" aria-pressed="true">Karten</button>
    <button type="button" class="km-segmented__btn" aria-pressed="false">Zeitlich</button>
  </div>
  <div class="km-segmented" role="group" aria-label="Sprache">
    <button type="button" class="km-segmented__btn" aria-pressed="false">Deutsch</button>
    <button type="button" class="km-segmented__btn" aria-pressed="true">English</button>
    <button type="button" class="km-segmented__btn" aria-pressed="false" disabled>Leichte Sprache</button>
  </div>
</div>'''),
 ('suchfeld', 'Suchfeld mit Spalten-Auswahl', 'Werkzeugzeile über einer Tabelle: Suchfeld (<code>km-searchbox</code>, Löschen <code>__clear</code>, Trefferzahl <code>__count</code>) und Spalten-Auswahl als Aufklapper (<code>km-colpicker</code>, Knopf <code>__btn</code> mit Zähler <code>__count</code>, Liste <code>__panel</code> mit Kopf <code>__head</code>).', f'''<div class="km-toolbar" style="max-width:40rem">
  <div class="km-searchbox" style="flex:1"><input type="text" placeholder="Projekte durchsuchen …" aria-label="Suche" value="formular"><button type="button" class="km-searchbox__clear" aria-label="Suche zurücksetzen"><svg class="km-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg></button></div>
  <span class="km-searchbox__count">3 Treffer</span>
  <div class="km-colpicker"><button class="km-colpicker__btn km-iconbtn km-iconbtn--label" type="button" aria-expanded="true">Spalten<span class="km-colpicker__count">5/9</span>{i('chevron-down')}</button>
    <div class="km-colpicker__panel" role="menu" style="display:block"><div class="km-colpicker__head">Sichtbare Spalten</div><label><input type="checkbox" checked><span>Typ</span></label><label><input type="checkbox"><span>Umfang</span></label><div class="km-colpicker__head km-colpicker__head--sets">Sets</div><div class="km-colpicker__sets"><button type="button" class="km-colpicker__set" aria-pressed="true">Überblick</button><button type="button" class="km-colpicker__set" aria-pressed="false">Kunden</button><button type="button" class="km-colpicker__set" aria-pressed="false">Pflege</button><button type="button" class="km-colpicker__set" aria-pressed="false">Alle</button></div></div></div>
</div>'''),
 ('vorschlaege', 'Vorschläge', 'Aufklappbarer Block mit automatisch erzeugten Vorschlägen (<code>km-suggest</code>, Kopf <code>__summary</code>, Hinweis <code>__note</code>); jeder Vorschlag ist eine Aufgabe mit <code>km-suggest__task</code>, übernehmen mit <code>__promote</code>.', '''<details class="km-suggest" open style="max-width:30rem"><summary class="km-suggest__summary">Vorschläge <span class="km-section__count">2 Vorschläge</span></summary><p class="km-suggest__note">Automatisch erzeugt, keine verbindlichen Aufgaben.</p>
<div class="km-task km-suggest__task"><div class="km-task__body"><div class="km-task__title"><span>Formular-Muster als Proposal anlegen</span><span class="km-suggest__tag">KI</span></div><p class="km-task__text">Drei Projekte bauen ähnliche Formulare.</p></div><div class="km-task__actions"><button type="button" class="km-suggest__promote km-iconbtn km-iconbtn--label">Übernehmen</button></div></div></details>'''),
 ('zeitlog', 'Zeitlog', 'Zeile mit investierten Stunden und Aufschlüsselung unter einer Projektkarte (<code>km-timelog</code>, <code>__label</code>, <code>__breakdown</code>, <code>__link</code>).', '''<div class="km-timelog"><span class="km-timelog__label">Time Log:</span> <strong>9,0h</strong> investiert <span class="km-timelog__breakdown">(manuell: 9,0 + Claude aktiv: 0,0)</span> · <a class="km-timelog__link" href="#zeitlog">Detail in time-log.md</a></div>'''),
 ('kleinteile', 'Info-i, Sync-Schalter, Nach oben', 'Kleine Bedienteile: Info-Knopf hinter einem Namen, zeigt beim Zeigen ein Vorschaubild (<code>km-infoi</code>); Schalter für eine Verbindung im Kopf (<code>km-sync</code>, an mit <code>km-sync--on</code>); Knopf „Nach oben“ unten rechts (<code>km-totop</code>, hier ohne feste Position).', f'''<p style="display:flex;flex-wrap:wrap;gap:1rem;align-items:center;margin:0">Projekt 1 <button type="button" class="km-infoi" aria-label="Teilbild anzeigen">{i('info')}</button>
<button type="button" class="km-sync">Live-Sync aktivieren</button><button type="button" class="km-sync km-sync--on">Live-Sync an</button>
<button type="button" class="km-totop" aria-label="Nach oben" style="position:static">{i('arrow-up')}</button></p>'''),
 ('tabelle', 'Tabelle', 'Tabelle in einem Rahmen, eingerückt wie jeder andere Inhalt. Gruppenzeile mit Farbkante links (<code>--km-row-color</code>), Unterzeilen (<code>km-table__row--sub</code>) hängen mit einem Einrückungswinkel am Namen unter ihrer Elternzeile, die Zeilennummer rückt nicht ein (Story „Tabelle: Unterprojekte“). Jede Zeile hat als letzte Zelle denselben Aktions-Platz (<code>km-table__actions</code>); Knöpfe kommen nur dort hinein, auch wenn eine Zeile keine hat. Die Aktionsspalte steht immer ganz rechts und bleibt beim waagerechten Scrollen stehen (<code>position: sticky</code>); solange rechts noch Inhalt kommt, läuft der Inhalt davor in einem Verlauf aus (<code>km-scroll--more</code> am scrollenden Rahmen, setzt das Skript der Seite). Nie Aktionen in einer mittleren Spalte. Jeder Spaltenkopf mit Symbol vor dem Namen (<code>.km-table th &gt; .km-icon</code>), kleiner als die Zellschrift. Name als <code>km-table__name</code> mit Monogramm (<code>km-monogram</code>), sortierbare Spalten mit <code>aria-sort</code>, Gruppen klappbar (<code>km-table__toggle</code>, <code>--collapsed</code>), externe Links als <code>km-chip--extern</code>, Knopf mit Text als <code>km-iconbtn--label</code>, Phase als Pill, Zeilenaktionen als <code>km-iconbtn</code>.', f'''<div class="km-table-wrap">
  <table class="km-table">
    <thead><tr><th class="km-table__sort" aria-sort="ascending">{i("folder")}Projekt</th><th class="km-table__sort" aria-sort="none">{i("layers")}Typ</th><th>{i("flag")}Phase</th><th><span class="kern-sr-only">Aktionen</span></th></tr></thead>
    <tbody>
      <tr class="km-table__group" style="--km-row-color:var(--km-color-tool-design)"><td colspan="4"><span class="km-table__toggle" aria-hidden="true"></span>Kunde A · 3 Projekte</td></tr>
      <tr><td><a class="km-table__name" href="#tabelle"><span class="km-monogram" style="--km-monogram-color:var(--km-color-tool-design)">P1</span>Projekt 1</a></td><td>Komponente</td><td><span class="km-pill km-pill--prototyp">Prototyp</span></td><td class="km-table__actions"><button type="button" class="km-iconbtn" aria-pressed="false" aria-label="Fokus">{i('pin')}</button><button type="button" class="km-iconbtn km-iconbtn--attention" aria-pressed="true" aria-label="In Arbeit">{i('star')}</button><button type="button" class="km-iconbtn km-iconbtn--label">Claude {i('copy')}</button></td></tr>
      <tr><td><a class="km-table__name" href="#tabelle"><span class="km-monogram" style="--km-monogram-color:var(--km-color-tool-design)">P2</span>Projekt 2</a></td><td>Werkzeug</td><td><span class="km-pill km-pill--aktiv">Aktiv</span></td><td class="km-table__actions"><button type="button" class="km-iconbtn" aria-pressed="true" aria-label="Fokus">{i('pin')}</button><button type="button" class="km-iconbtn km-iconbtn--attention" aria-pressed="false" aria-label="In Arbeit">{i('star')}</button></td></tr>
      <tr><td><a class="km-table__name" href="#tabelle"><span class="km-monogram" style="--km-monogram-color:var(--km-color-tool-design)">P3</span>Projekt 3</a></td><td>Sandbox <a class="km-chip km-chip--extern" href="#tabelle">Live</a></td><td><span class="km-pill km-pill--idee">Idee</span></td><td class="km-table__actions"></td></tr>
    </tbody>
  </table>
</div>
<p style="display:flex;flex-wrap:wrap;gap:.5rem;margin:1rem 0 0"><span class="km-pill km-pill--idee">Idee</span><span class="km-pill km-pill--konzept">Konzept</span><span class="km-pill km-pill--prototyp">Prototyp</span><span class="km-pill km-pill--migration">Migration</span><span class="km-pill km-pill--aktiv">Aktiv</span><span class="km-pill km-pill--toolkit">Toolkit</span></p>'''),
]

# Nachgetragene Stories (2026-11-08), eigene Datei wegen der Länge
import sys as _sys; _sys.modules.setdefault('bausteine_basis', _sys.modules[__name__])
from bausteine_nachtrag import NACHTRAG as _NACHTRAG, SEG_WRAP as _SEG_WRAP
BAUSTEINE += _NACHTRAG
# Segmented Control: eine Story mit beiden Varianten, Zwischenüberschrift je Variante
_n = [x[0] for x in BAUSTEINE].index('segmented'); _a, _t, _z, _m = BAUSTEINE[_n]
BAUSTEINE[_n] = (_a, _t, _z + ' Variante umbrechend: ' + _SEG_WRAP[0],
                 f'<h3 class="km-subhead">{i("columns-3")}Standard</h3>' + _m + f'<h3 class="km-subhead" style="margin-top:var(--km-space-xl)">{i("wrap-text") if "wrap-text" in IC else i("columns-3")}Umbrechend <small>km-segmented--wrap</small></h3>' + _SEG_WRAP[1])


# Abstands-Regelwerk (2026-11-08): eine Quelle für Doku und Storybook. Werte stehen in src/km-roles.css.
ABSTAENDE = [  # (Ebene, Token, Stufe, wofür)
 ('1', '--km-space-page', '2xl · 32 px', 'zwischen Bereichen der Seite, vor der Fußzeile'),
 ('1', '--km-space-section-x', 'xl · 24 px', 'Innenrand eines Bereichs, seitlich und unten'),
 ('1', '--km-space-section-y', 'l · 20 px', 'Kopf eines Bereichs, oben und unten'),
 ('2', '--km-space-block', 'm · 16 px', 'zwischen Unterbereichen eines Bereichs: Karten, Tabelle, Suchfeld, Ergebnis-Kategorien'),
 ('2', '--km-space-card', 'm · 16 px', 'Innenrand einer Karte'),
 ('3', '--km-space-group', 's · 12 px', 'zwischen Gruppen in einer Karte: Text, Fakten, Panels, Aktionen'),
 ('4', '--km-space-stack', 'xs · 8 px', 'zwischen zusammengehörigen Teilen: Titel und Untertitel, Aufgaben untereinander, Werkzeugleiste'),
 ('5', '--km-space-tight', '2xs · 4 px', 'eng: Label und Wert, Icon und Text, Chips und Treffer untereinander'),
]
ABSTAND_REGELN = [
 'Von außen nach innen wird jede Ebene eine Stufe kleiner; innen ist nie größer als außen.',
 'Nähe gruppiert: großer Abstand vor einer Gruppe, kleiner innerhalb (z. B. Ergebnis-Kategorie 16 px davor, 8 px zur eigenen Liste, 4 px zwischen Treffern).',
 'Nur Werte der Skala (KERN-Raster in 4-px-Schritten: 4, 8, 12, 16, 20, 24, 32). Bausteine nehmen die Rolle, nicht die Stufe, wo eine Rolle passt.',
 'Ausnahmen: Feinmaß kleiner Bedienteile unter 4 px (Chips, Kennungen) und Linienstärken gehören zum Baustein, nicht zur Skala.',
]
ABSTAND_BILD = '''<div style="background:var(--km-color-page);padding:var(--km-space-page);font-size:var(--km-font-size-xs);color:var(--km-color-text-muted);max-width:44rem">
  <div style="display:grid;gap:var(--km-space-page)">
    <div style="background:var(--km-color-section);border:1px solid var(--km-color-border-section);padding:var(--km-space-section-y) var(--km-space-section-x) var(--km-space-section-x)">
      <b style="display:block;margin-bottom:var(--km-space-block);color:var(--km-color-text)">Bereich · Innenrand section-x/-y · Abstand zum nächsten Bereich: page</b>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:var(--km-space-block)">
        <div style="background:var(--km-color-card);border:1px solid var(--km-color-border-card);padding:var(--km-space-card);display:grid;gap:var(--km-space-group)">
          <div style="display:grid;gap:var(--km-space-stack)"><b style="color:var(--km-color-text)">Karte · block zwischen Karten</b><span>Untertitel · stack</span></div>
          <div style="outline:1px dashed var(--km-color-border-section);padding:var(--km-space-tight)">Gruppe · group</div>
          <div style="display:flex;gap:var(--km-space-tight)"><span class="km-chip">tight</span><span class="km-chip">tight</span></div>
        </div>
        <div style="background:var(--km-color-card);border:1px solid var(--km-color-border-card);padding:var(--km-space-card)">Karte</div>
      </div>
    </div>
    <div style="background:var(--km-color-section);border:1px solid var(--km-color-border-section);padding:var(--km-space-section-y) var(--km-space-section-x)">Nächster Bereich</div>
  </div>
</div>'''


def intro_html():
    """Einführung aus docs/intro.md (eine Quelle für Doku und Storybook): Überschriften ab ##, Absätze, Listen, fett, Code; ohne den Titel."""
    import html as _h, re as _re
    def inl(s):
        s = _h.escape(s, quote=False)
        s = _re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
        s = _re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
        return _re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a class="km-link" href="\2">\1</a>', s)
    out, liste = [], False
    for z in (ROOT / 'docs/intro.md').read_text(encoding='utf-8').splitlines():
        if z.startswith('# ') or not z.strip():
            if liste: out.append('</ul>'); liste = False
            continue
        if z.startswith('## '):
            if liste: out.append('</ul>'); liste = False
            out.append(f'<h3>{inl(z[3:])}</h3>'); continue
        if z.startswith('- '):
            if not liste: out.append('<ul>'); liste = True
            out.append(f'<li>{inl(z[2:])}</li>'); continue
        out.append(f'<p>{inl(z)}</p>')
    if liste: out.append('</ul>')
    return '<div class="km-prose">' + ''.join(out) + '</div>'
