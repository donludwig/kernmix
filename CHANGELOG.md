# Changelog Kernmix

Format: neueste Version oben, je Eintrag eine Zeile. Jede Version hat einen Release-Namen nach ihrem Kern („…“ in der Überschrift). Basis: KERN-Kit (@kern-ux/native) 2.8.2.

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

