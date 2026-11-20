# Changelog Kernmix

Format: neueste Version oben, je Eintrag eine Zeile. Jede Version hat einen Release-Namen nach ihrem Kern („…“ in der Überschrift). Basis: KERN-Kit (@kern-ux/native) 2.8.2.

## 0.21.0 „Hosentasche“ · 2026-11-19

Kernmix ist für den Desktop gestaltet und bleibt auf Telefon und Tablet benutzbar.

- Untergrenze für Geräte ohne Maus nach WCAG 2.2: kein seitliches Scrollen bei 320 px, Tippziele mindestens 24 × 24 px, nichts nur per Hover, Fokusrahmen nur bei Tastatur. Am Desktop ändert sich nichts.
- Fokusrahmen erscheint nur noch bei Tastaturbedienung (`:focus-visible`), nicht mehr nach Tipp oder Klick auf Elemente mit `tabindex`.
- Bei grobem Zeiger (`pointer: coarse`) mindestens 24 × 24 px: Name und Öffnen-Knopf in Tabellen, Leeren-Knöpfe in Suchfeld und Filter-Chips, Info-Knopf, Entfernen in Schnellzugriffen, Gruppenköpfe der Seitenleiste, Knöpfe mit Text, Kästchen, Links in `km-task__meta` und `km-card__foot`.
- Griff zum Verschieben von Tabellenzeilen ohne Maus immer sichtbar (`hover: none`).
- Schmale Bildschirme: langer Code im Fließtext bricht um, Segmented Control scrollt in sich, Pills brechen um.

## 0.20.1 „Knapp“ · 2026-11-18

Tabellenspalten nur so breit wie ihr Inhalt.

- Tabelle: Variante `km-table--knapp`, den freien Platz nimmt die letzte sichtbare Spalte vor den Aktionen (`kmTabelle.restSpalte(t)`); der Abstand zwischen den Spalten wächst mit der Bildschirmbreite (`--km-component-table-knapp-luft`).
- `kmTabelle.breitenFest(t)` mit `km-table--messen`: Spaltenbreiten aus allen Zeilen, auch gefilterten; die Spalten springen nicht, wenn ein Filter andere Zeilen zeigt.
- Tabelle: `km-table--laedt` hält eine Tabelle unsichtbar mit reserviertem Platz, bis die Seite sie gebaut hat; `km-table__tool--spalte` zeigt das Werkzeug als eigene Spalte.
- `einbetten.py --schriften` lädt die Hauptschrift per `<link rel="preload">` vorab; `einbetten.py --schlank` übernimmt aus dem KERN-Kit nur Regeln mit genutzten `kern-*`-Klassen.

## 0.20.0 „Nachtblau“ · 2026-11-16

Neues Theme in Dunkelblau, dunkel und hell.

- Theme „Nachtblau“ (`src/themes/nachtblau.css`): tiefes Dunkelblau, Akzent Himmelblau, Radius 4 px, runde Icon-Enden; Kontrast auf allen Flächen gerechnet (Text ≥ 11,1, Lesetext ≥ 7,7, Meta ≥ 5,1, Akzent ≥ 7,3).
- Radius aus dem Theme (`--km-radius`) für Segmented Control, Knöpfe, Etiketten, Chips, Hinweiskasten, Suchfeld, Kästchen, Karten, Kacheln, Tabellenrahmen, Codeblock, Panels und Abbildungen. Kobalt und Papier setzen 0.

## 0.19.3 „Wissen“ · 2026-11-16

Aufklappbare Zeilen, Bereiche in Karten und Ansichtsschalter.

- Tabelle: Pfeil `km-table__chevron`, Öffnen-Symbol `km-table__open`, Typ-Symbol `km-table__typ`; aufgeklappte Zeile mit durchgehendem Rahmen; Wertzellen auf gemeinsamer Grundlinie; Varianten `km-table--text-frei` und `km-table-wrap--schmal`.
- `kmTabelle`: Spalten „Start“, „Ende“ und „Vor“ (wie lange her); Sortieren innerhalb von Gruppenzeilen.
- Neue Bausteine: `km-card__section` (aufklappbarer Bereich in einer Karte), `kmAnsicht` (hell/dunkel und Theme umschalten, vor dem ersten Zeichnen angewendet), `km-paar` (Vergleich „Nicht so / So“).
- Panel: Variante `km-panel--schritte`; Karte: `km-card__foot` steht unten, in `km-cards` auf gleicher Höhe (Subgrid).

## 0.19.2 „Wissen“ · 2026-11-15

- Tabelle: `km-table__detail` für aufgeklappte Zeilen, `km-table__row--offen`, `km-table__row--aufklappbar`.

## 0.19.1 „Wissen“ · 2026-11-15

- `km-finder`: fast bildschirmfüllend, Liste und Vorschau nebeneinander, Fundstellen mit Abschnittsname.

## 0.19.0 „Wissen“ · 2026-11-15

- Neuer Baustein `km-finder`: Suche als Fenster über der Seite (`<dialog>`) mit Filter-Chips, Trefferliste in Gruppen, Vorschau und Tastenhinweisen.

## 0.18.4 „Wissen“ · 2026-11-15

- Grafik `km-graph`: gestrichelte Linien in eigener Farbe `--km-component-graph-frage`; hervorgehobene Linien mit Rand und vorn.

## 0.18.3 „Wissen“ · 2026-11-15

- Eckleiste bei eingeklappter Seitenleiste mittig unter dem Einklapp-Knopf (`--km-corner-rail-left`).

## 0.18.2 „Wissen“ · 2026-11-15

- Seitenkopf: Icon-Knöpfe ohne Text in `km-header__actions` quadratisch.

## 0.18.1 „Wissen“ · 2026-11-15

- Dokumentkopf: Abstand für `km-metaline` direkt unter `km-lead` in `km-hero`.

## 0.18.0 „Wissen“ · 2026-11-15

Bausteine für Seitenkopf, Werkzeugzeile und Inhalt.

- Seitenkopf: `km-shell__titles` und `km-shell__claim` für Name mit Unterzeile.
- Seitenleiste: `km-shell__tools` für Suche plus quadratische Knöpfe in einer Zeile.
- Seitengerüst: `km-shell__content` für den Innenabstand des Inhalts.
- Dokumentkopf: Abstand für `km-toolbar` in `km-hero`.

## 0.17.0 „Umgestellt“ · 2026-11-11

Spalten lassen sich verschieben.

- Tabellen (`km-table.js`): `kmTabelle.spaltenZiehen(tabelle, { schluessel })` macht die Spaltenköpfe ziehbar, `kmTabelle.spalteSchieben(…)` verschiebt ohne Maus (Hoch/Runter in der Spaltenauswahl), `kmTabelle.spaltenOrdnen(tabelle, schluessel)` stellt die gespeicherte Reihenfolge beim Laden her. Gespeichert wird nach Spaltennamen; Name vorn und Aktionen hinten bleiben fest. CSS: Greifzeiger, abgeblendeter Kopf beim Ziehen, Einfügelinie mit `--km-drop-line`, Knöpfe `km-colpicker__move`. Verschieben stellt sofort um, ohne Neuladen; die Spaltenauswahl bleibt dabei offen (`kmTabelle.spaltenMenue(tabelle, { schluessel, panel, nachher })`, Labels ziehen mit, Fokus bleibt auf dem Pfeil), die Tabelle meldet `km-spalten-verschoben` (`detail.perm`), Kopien von Zeilen stellt `kmTabelle.spaltenUmstellen(zeilen, perm)` um.
- Tabellen: `kmTabelle.leereAktionen(tabelle)` blendet die Aktionsspalte aus, solange keine sichtbare Zeile Aktionen hat, etwa nach einem Filter (Klasse `km-table--ohne-aktionen`).

## 0.16.11 „Eine Linie“ · 2026-11-10

Nummer, Symbol und Name stehen auf einer Linie.

- Tabellen: Ein Symbol im `km-table__name` ist so hoch wie die Namenszeile; die laufende Nummer (`km-table--numbered`) richtet sich bei Namen ohne Monogramm nach der Namenszeile.

## 0.16.10 „Markiert“ · 2026-11-10

- Seitenleiste: Ein Klick auf `km-sidebar__action` markiert den Eintrag derselben Zeile als aktuell und hebt die übrigen Markierungen auf.

## 0.16.9 „Zahnrad“ · 2026-11-10

Klappen und Funktion in der Seitenleiste getrennt.

- Seitenleiste: neuer Baustein `km-sidebar__action`, ein Symbol rechts im Eintrag für Bearbeiten oder Verwalten. Einträge mit Unterebene klappen per Klick nur auf und zu.

## 0.16.8 „Schmal“ · 2026-11-10

- Tabellen: Die Namensspalte nimmt den freien Platz; die Aktionsspalte ist nur so breit wie ihre Knöpfe.

## 0.16.7 „Rechts“ · 2026-11-10

- Tabellen: Knöpfe der Aktionsspalte stehen rechtsbündig; `km-table__actions--start` bleibt linksbündig.

## 0.16.6 „Gleiche Kachel“ · 2026-11-10

- Fokus (`km-focus`): Symbol im Bereichskopf in der Akzentfarbe wie bei allen Bereichen; die Kachel bleibt in der Bereichsfarbe.

## 0.16.5 „Stimmig“ · 2026-11-10

Versionsangaben im Prototyp stimmen.

- Prototyp: Die Karte unter Design-Systeme nennt die aktuelle Kernmix-Version.

## 0.16.4 „Überblick“ · 2026-11-10

Der Prototyp beginnt mit dem Überblick.

- Startansicht: Projektübersicht und Listen offen, Projektdetails zugeklappt.
- Seitenleiste des Prototyps: „Kernmix auf GitHub“ führt wieder zum Repo, die Kachel „Eigenes Design-System“ und die Kernmix-Karte ebenso.

## 0.16.3 „Erster Eindruck“ · 2026-11-10

- Prototyp: ruhigere Startansicht ohne Fokus-Box; Projektübersicht zugeklappt, Projektdetails und Listen offen, Über dieses Projekt weiter unten; Filter „nur offene“ an. README- und Social-Bilder ohne Versionsnummer.

## 0.16.2 „Aufgeräumt“ · 2026-11-10

- Prototyp: Die Kachel „Eigenes Design-System“ und die Kernmix-Karte verlinken auf kernmix.thinkrepeat.com und dieses Repo; eigene Projekte stehen in den Projektdetails unter Claude Code, Skill-Texte ohne Domain.

## 0.16.1 „Ruhig“ · 2026-11-10

- `km-netz`: Die Drift des Hintergrundnetzes läuft auf einer eigenen Grafikebene (`will-change`, `translate3d`); Safari auf iPad und iPhone zeichnet den Hintergrund nicht mehr bei jedem Schritt neu.

## 0.16.0 „Editorial“ · 2026-11-09

- Seiten-Varianten als Modifier am body: `km-page--editorial` (Linien statt Flächen, große Kennzahlen, Zitat groß ohne Kasten), `km-page--farbig` (Farbe je Gruppe) und `km-page--kraeftig` (getönter Kopf mit Bildmosaik `km-mosaik`); Gruppenfarben `km-ton--1` bis `--3` aus vorhandenen Rollen, ohne neue Farbwerte. Ohne Modifier sieht jede Seite unverändert aus.
- Editorial auf dem Tablet (640 bis 1200 px): Lesetext in Karten im breiten Maß, Display-Überschriften 10 bis 15 % kleiner. Breite Bildkarten (`km-card--wide`) teilen sich quer (1025 bis 1200 px) Bild und Text je zur Hälfte.
- Karten-Raster: `km-cards--wechsel` (breite Karten abwechselnd mit Bild links und rechts), `km-cards--frei` (Textraster ohne Fläche und Rahmen), Titel in Akzent- oder Kupferton (`km-cards--akzent`, `km-cards--koralle`).
- `km-profil`: Visitenkarte mit Porträt, Name, Rolle, Text und Links, ohne Kasten.
- `km-lightbox`: Bilder in einem Bereich mit `data-km-lightbox` öffnen per Klick groß, ←/→ blättern, Esc schließt; `data-gross` für ein größeres Bild, `data-km-lightbox-ohne` nimmt ein Bild aus.
- Lesetext: Blöcke (Hinweiskasten, Tabelle, Karten, Code, Abbildung, Zitat) stehen mit 24 px Abstand zum Text (`--km-space-prose-block`), über Zwischentiteln 32 px; Zitate mit 32 px oben und unten. `km-prose--wide` macht den Lesetext so breit wie die Einleitung; `km-shell--nav-wide` und `km-chapters--breit` für lange Kapitelnamen; `km-lead--frei` für eine Einleitung ohne Lesemaß.
- Prüfwerkzeuge: `km-signal--fehler` setzt in einem Bereich die Signal- und Warnfarbe auf die Fehlerfarbe (Markierungen, Warn-Symbole, `km-pill--warn`). `km-header--begrenzt` hält den Inhalt der Kopfzeile höchstens 1400 px breit und mittig. Erste Nutzung: Kunstgriff.
- `km-sidebar__group--fuss`: Fuß der Seitenleiste, auf breiten Bildschirmen unten angeheftet.
- Fehlerbehebung: Die feste Seitenleiste von `km-shell` klappt nicht mehr bei einem Klick daneben, einem Cmd-Klick auf einen Link oder Esc zu; `kmPopup` behandelt ihren Einklapp-Knopf nicht als Panel. Abschnittstitel mit Icon behalten die Display-Schrift.

## 0.15.0 „Schaufenster“ · 2026-11-09

- Erste öffentliche Version, Lizenz EUPL-1.2: eine Design-System-Erweiterung für KERN. Die Versionen darunter sind der Rückblick auf die Entwicklung bis dahin, je Version in einer Zeile.
- Inhalt: Rollen-Tokens `--km-*` (`src/km-roles.css`), eigene Farbreihen und Datenfarben (`src/km-core.css`), über 30 Werkzeug-Bausteine mit Präfix `km-` (`src/km-components.css`), zwei Skripte (`km-table.js` für Standard-Tabellen, `km-popup.js` für Panels und Kapitelleiste), Themes „Kobalt“ (`kern-nah.css`) und „Papier“ (`startklar.css`), gebaut nach `dist/`.
- Doku: Komponentenbeschreibung (`storybook/index.html`) mit Einführung, Grundlagen (Farben, Abstände, Schriftgrößen, Tokens), allen Bausteinen und den offiziellen KERN-Stories; Komponenten-Doku je Baustein in vier Kapiteln („Was ist es?“, „Wann nehmen?“, „Wie bauen?“, „Wie prüfen?“) mit Kapitelleiste; Doku-Seite `docs/index.html`; Seitenregeln `docs/seitenregeln.md`.
- Entscheidungen werden als ADR und DDR festgehalten; sie sind in dieser Fassung noch nicht enthalten und werden später veröffentlicht.
- Schriften lokal, ohne fremde Server: Atkinson Hyperlegible Next (Kobalt), Inter und Archivo (Papier, Überschriften als Extrabold mit 88 % Breite), alle unter SIL OFL 1.1.
- Icons: Lucide 1.49.0 (ISC), 24er-Raster; Strich, Linienenden und Ecken setzt das Theme.
- Werkzeuge ohne Abhängigkeiten (Python-Standardbibliothek): `tools/build.py` prüft jeden `--kern-…`-Bezug gegen das eingebundene Kit und baut `dist/`; `tools/einbetten.py` bettet das System in eine einzelne HTML-Seite ein; `tools/pruefe-seiten.py` prüft die gebauten Seiten in Headless Chrome.
- Kontraste aller Textrollen auf allen Flächen gerechnet: Text mindestens 4,5:1, Bedienelemente mindestens 3:1, in beiden Themes und Modi.
- Bausteine für Prüfwerkzeuge: Eingabe mit Zeilennummern `km-lines`, Markierung im Text `km-mark`, verknüpfte Hervorhebung `km-linked` für Tabellenzeile, Karte und Markierung, Fokusrahmen an fokussierbaren Tabellenzeilen, Hinweiskasten `km-callout--ok` in der Erfolgsfarbe.
- Karte mit Bild: Vorschaubild oben über die ganze Kartenbreite (`km-card__media`, 16:10, oben links angeschnitten) und Link unten (`km-card__link` mit Icon, steht im Raster auf einer Linie).

## 0.14.0 „Liner Notes“ · 2026-11-09

- Komponenten-Doku in vier Kapiteln mit Kapitelleiste und Regeln je Baustein; Entscheidungen in fünf Abschnitten mit Meta-Zeile; Standard-Seitenleiste mit Einklapp-Knopf; Hellmodus Kobalt „Papierweiß, kühl“ und Papier „Warm neutral“.

## 0.13.0 „Hochkant“ · 2026-11-09

- Jede Erklärgrafik quer und hochkant, schmale Flächen zeigen die Hochformat-Fassung; Listen zweispaltig für viele kurze Punkte; keine Schriftzeichen als Icon.

## 0.12.0 „Setlist“ · 2026-11-09

- Kontraste aller Textrollen auf allen Flächen nachgerechnet; Filter-Leiste mit Etiketten und Filtergruppe der Seitenleiste; ein gemeinsamer Stil für alle Grafiken.

## 0.11.0 „Tracklist“ · 2026-11-09

- Komponenten-Doku und Entscheidungen mit Fakten-Kacheln und Kartenraster; ein Listenzeichen für alle Listen; Einzug der Seitenleiste nach Ebenen.

## 0.10.0 „Prüfstand“ · 2026-11-09

- Bausteine für Fragebögen (Antwort-Knöpfe, Prüfkarte, Feld, Score, Fortschritt, Begriff).

## 0.9.0 „Intro“ · 2026-11-09

- Startseite mit Einführung und Grafiken aus einer Quelle; Doku im selben Stil; Prüfung der KERN-Tokens beim Bauen.

## 0.8.0 „Liner Notes“ · 2026-11-09

- Komponenten-Dokus nach einer Vorlage, Entscheidungen als eigene Seite.

## 0.7.0 „Remix“ · 2026-11-09

- Name Kernmix und Präfix `km-` für Klassen, Tokens und Dateien.

## 0.6.0 „Reihe und Rolle“ · 2026-11-09

- Token-Ebenen wie bei KERN (Grundwerte, Core Token, Semantische Token), Komponenten-Tokens `--km-component-*`, Rollen zeigen auf semantische KERN-Tokens, eigene Farbreihen und Datenfarben.

## 0.5.0 „Gleiche Höhe“ · 2026-11-09

- Bedienelemente einer Zeile gleich hoch; Segmented Control mit Umbruch.

## 0.4.0 „Kobalt und Papier“ · 2026-11-08

- Die beiden Themes, je hell und dunkel; lokale Schriften; Standard-Tabelle mit fester Aktionsspalte rechts.

## 0.3.0 und früher „Grundstein“ · 2026-11-08

- Aufbau auf KERN 2.8.2, Rollen-Tokens, erste Bausteine, Doku und Komponentenbeschreibung aus einer Quelle, Einbetten in Zielseiten.

