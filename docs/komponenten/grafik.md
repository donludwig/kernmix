# Grafik „Wer ruft wen auf“ (`km-graph`)

Status: stabil, im Dashboard im Einsatz · Story: `docs/index.html#grafik`, `#grafik-zustaende` · CSS: `src/km-components.css`, Abschnitt „Skill-Grafik“ · Stand: 2026-11-09

## Kurzbeschreibung

Eine vom Generator gezeichnete SVG-Grafik, die zeigt, welche Skills welche anderen aufrufen: Knoten in Spalten, Kanten dazwischen, darüber Legende mit Filterknöpfen je Kategorie, darunter Info zum gewählten Knoten, Erklärung, Liste und Hilfe. Wählt man einen Knoten, treten seine Nachbarn und Kanten hervor, ausgehende im Akzent, eingehende in der Signalfarbe. Die Zeichnung liefert `grafik()` im Generator des Project Dashboards; das Kit liefert Farben und Zustände.

## Name und Abgrenzung

- Ebenen `__koepfe` (`__sk`, `__sk2`), `__es` (`__e`, `__frage`), `__ns` (`__n`, `__kat`, `__ico`, `__zahl`); Zustände `__an`, `__ich`, `__fest`, `__nb`, `__aus`, `__ein`; Teile `__legende`, `__katknopf`, `__info`, `__kopf`, `__kurz`, `__zeile`, `__erklaerung`, `__sws`, `__sw`, `__sw-rand`, `__liste`, `__hilfe`, `__l-aus`, `__l-ein`, `__linie`, `__zahl-l`, `__wrap`, `__svg`.
- Keine allgemeine Diagramm-Bibliothek; für Kennzahlen gelten `km-bars` und `km-histo`.
- Erklärgrafiken im Stil der Einführung (animiert, klickbar, Inline-SVG in `km-figure`) nutzen den gemeinsamen Stil `tools/grafik_stil.py` (`STIL`, `ic`, `scope`); `scope()` beschränkt jede Stilregel auf die eine Grafik, damit sie inline in einer Seite nichts anderes trifft. Bewegung nur ohne `prefers-reduced-motion`.

## Einsatz

### Verwenden, wenn

- gezeigt werden soll, welche Skills welche anderen aufrufen oder vorher fragen, gezeichnet von `grafik()` im Generator des Project Dashboards (Story `#grafik`; das Migrationsprotokoll, Zeile „Grafik Wer ruft wen auf“).

### Nicht verwenden, wenn

- Kennzahlen gezeigt werden: `km-bars`, `km-histo`;
- eine Erklärgrafik gebraucht wird (Ablauf, Schichten, animiert oder klickbar): Inline-SVG in `km-figure` mit dem Stil aus `tools/grafik_stil.py`, quer und hoch (`km-figure__wide`, `km-figure__tall`) (`docs/seitenregeln.md`, „Grafiken haben eine Hochformat-Fassung“; `CHANGELOG.md` 0.12.0, gemeinsamer Grafik-Stil);
- andere Beziehungen als Skill-Aufrufe gezeichnet werden sollen: `km-graph` ist keine allgemeine Diagramm-Bibliothek.

## Zustände

| Zustand | Auslöser | Darstellung |
|---|---|---|
| Ruhe | – | Kanten 50 % Deckkraft, Knoten auf `inset` |
| Etwas gewählt | `km-graph__an` am SVG | übrige Kanten 8 % |
| Gewählter Knoten | `__ich`, festgehalten `__fest` | Rand Text bzw. Akzent |
| Nachbar | `__nb` | voll sichtbar |
| Ausgehend / eingehend | `__aus` / `__ein` | Akzent / Signal, 2,6 px |
| Fokus Knoten | `:focus-visible` | Rand in Fokusfarbe |
| Kategorie gedrückt | `__katknopf[aria-pressed="true"]` | Rand Akzent |

## Barrierefreiheit

- Knoten sind `g` mit `tabindex="0"`, `role="button"`, `aria-pressed`, `aria-label`.
- Die Liste `__liste` gibt die Verbindungen als Text wieder; sie ist der Weg für Screenreader.
- Ausgehend und eingehend unterscheiden sich nur in der Farbe (Akzent und Signal); die Info-Zeile benennt sie zusätzlich als Text.
- Breite: SVG mindestens 68.75rem, scrollt quer in `__wrap`.

## Beispiele

### Falsch

Grafik ohne Textliste (`km-graph__liste`): Screenreader erfahren die Verbindungen nicht.

## Seitenregeln

Beispiele mit erfundenen Daten; Datenfarben ≥ 3:1; breite Grafiken in scrollenden Rahmen mit `position: relative`. Entscheidungen 15, 27.

## Vergleich mit anderen Design-Systemen

| System | Name | Besonderheit | Quelle |
|---|---|---|---|
| – | – | ungeprüft | – |

## Tokens

- `--km-color-text`, `--km-color-text-muted`, `--km-color-text-dim`, `--km-color-accent`, `--km-color-attention`, `--km-color-focus`, `--km-color-inset`, `--km-color-card`, `--km-color-border-card`.
- Haken: `--sg-k` (Kategoriefarbe am Knoten).
- Hart: Strichstärken 1, 1,5, 2, 2,5, 2,6, Deckkräfte 0,5 und 0,08, `min-width: 68.75rem`.

## Offene Punkte

- Viele harte Strichstärken und Deckkräfte; als Komponenten-Tokens sammeln.
- Haken `--sg-k` ohne Präfix.
- Teilnamen auf Deutsch gekürzt (`__sk`, `__nb`, `__es`); für Agenten schwer lesbar.

## Regeln

- Was: `km-graph` ist eine vom Generator gezeichnete SVG-Grafik, die zeigt, welche Skills welche anderen aufrufen: Knoten in Spalten, Kanten dazwischen, darüber die Legende mit Filterknöpfen je Kategorie, darunter Info, Erklärung, Liste und Hilfe; ein gewählter Knoten hebt Nachbarn hervor, ausgehende Kanten im Akzent, eingehende in der Signalfarbe.
- Wann: Nur für Aufruf-Beziehungen zwischen Skills, die der Generator zeichnet; für Kennzahlen `km-bars` und `km-histo`, für Erklärgrafiken Inline-SVG in `km-figure` mit dem Stil aus `tools/grafik_stil.py` in Quer- und Hochformat, eine allgemeine Diagramm-Bibliothek ist `km-graph` nicht.
- Wie: Knoten als `g` mit `tabindex="0"`, `role="button"`, `aria-pressed` und `aria-label`, Verbindungen zusätzlich als Text in `km-graph__liste`, Farben aus den Tokens (Kategoriefarbe über `--sg-k`), das SVG in `__wrap` mit `position: relative`, Bewegung nur ohne `prefers-reduced-motion`, Beispiele mit erfundenen Daten.
- Prüfen: Fertig ist es, wenn jeder Zustand der Tabelle erreichbar ist (`__an`, `__ich`, `__fest`, `__nb`, `__aus`, `__ein`, Fokus, gedrückte Kategorie), `km-graph__liste` alle Verbindungen als Text wiedergibt, ausgehend und eingehend auch in der Info-Zeile als Text benannt sind, Datenfarben mindestens 3:1 messen und das SVG ab 68.75rem Breite quer in `__wrap` scrollt.
