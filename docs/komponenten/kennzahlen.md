# Kennzahlen (`km-facts`, `km-bars`, `km-histo`)

Status: stabil, in Dashboard und Lagebild im Einsatz · Story: `docs/index.html#fakten`, `#kacheln-raster`, `#kennzahlen`, `#projektkarte`, `#hero` · CSS: `src/km-components.css`, Abschnitte „Fakten-Kacheln“, „Fußzeile mit Kennzahlen und Balken“, Histogramm im „Dashboard-Gerüst“, „Lagebild-Umbau“ (`--grid`, `--ok`, `--danger`) · Stand: 2026-11-09

## Kurzbeschreibung

Kennzahlen zeigen wenige wichtige Werte auf einen Blick. Die Fakten-Kacheln (`km-facts`) setzen je Wert eine Kachel mit kleiner Beschriftung samt Icon oben und großem Wert darunter, optional mit Unterzeile und einem Frische-Balken über die ganze Kachelbreite. Als festes Raster (`--grid`) stehen vier Kacheln 2×2, Zustand nur über Icon und Balken. Verteilungen zeigen der gestapelte Balken mit Legende (`km-bars`) und das Balken-Histogramm (`km-histo`).

## Name und Abgrenzung

- `km-facts`/`km-fact` (Kacheln), `km-facts--grid` (Raster), `km-fact--ok`/`--danger` (Zustand), `km-bars` (Anteile), `km-histo` (Verteilung).
- In der Oberfläche heißen die Kacheln nach ihrer Größe („Phase“, „Update“).
- Nicht dazu: Kennzahlen als kleine Tabellen (`km-tables`, siehe `tabelle.md`), Zähler neben Titeln (`km-count`), werbliche Einleitung (`km-hero`, siehe `einfuehrung.md`).
- Daten als `<dl>`: Beschriftung `dt`, Wert `dd`.

## Einsatz

### Verwenden, wenn

- drei bis sechs Werte zu einer Sache oben in Karte oder Bereich stehen (Kacheln);
- vier Prüfwerte mit Zustand gleich groß nebeneinander stehen sollen (`--grid`);
- Anteile einer Gesamtmenge gezeigt werden (`km-bars`), oder eine Verteilung über Zeiträume (`km-histo`).

### Nicht verwenden, wenn

- viele Werte je Gruppe verglichen werden: `km-tables`;
- die Zahl nur Zusatz zu einem Titel ist: `km-count`;
- ein Wert ohne Bezeichnung auskommt: Text.

## Verwendung

```html
<dl class="km-facts" aria-label="Fakten zum Projekt" style="--km-card-accent:var(--km-color-tool-design)">
  <div class="km-fact"><dt class="km-fact__label"><svg class="km-icon" aria-hidden="true">…</svg>Phase</dt><dd class="km-fact__value">Prototyp</dd></div>
  <div class="km-fact"><dt class="km-fact__label"><svg class="km-icon" aria-hidden="true">…</svg>Update</dt><dd class="km-fact__value">12 Tage<small>27.10.2026</small></dd><span class="km-fact__bar" aria-hidden="true"><i style="width:60%"></i></span></div>
</dl>
```

## Aufbau

| Teil | Klasse | Funktion |
|---|---|---|
| Streifen | `km-facts` | Kacheln so breit wie ihr Inhalt, füllen die Reihe, brechen um; jede Kachel zeichnet ihre Linien selbst. |
| Kachel | `km-fact` | Kartenfläche, mindestens 5.75rem, Innenrand `--km-space-m`. |
| Beschriftung | `km-fact__label` | Versalien, gedämpft, Icon in der Kartenfarbe (mit Textfarbe gemischt, ≥ 3:1). |
| Wert | `km-fact__value` | 18 px, kräftig, gleich breite Ziffern, nie umbrechen; `small` für die Unterzeile. |
| Langer Wert | `km-fact__value--long` | `--km-font-size-s`, darf umbrechen. |
| Frische | `km-fact__bar` | Balken unten über die ganze Kachel; voll = heute, leer = vor 30 Tagen (setzt die Seite). |
| Raster | `km-facts--grid` | 2 Spalten gleich breit, Unterzeile einzeilig mit „…“. |
| Zustand | `km-fact--ok`, `--danger` | Icon und Balken grün bzw. rot, Wert bleibt in Textfarbe. |
| Anteile | `km-bars`, `__line`, `__bar`, `__legend`, `__key`, `__sw`, `__pct` | Balken 12rem aus Segmenten (`flex` = Anteil), Legende mit Zahl und Prozent. |
| Verteilung | `km-histo`, `__label`, `__bar`, `__value` | Raster Beschriftung, Balken, Wert. |

## Varianten

Streifen (Standard), Raster `--grid`, Zustand `--ok` / `--danger`, Anteile, Verteilung.

## Größen

Wert 18 px (`--kern-font-size-18`), lange Werte 14 px.

## Zustände

| Zustand | Auslöser | Darstellung | Tokens |
|---|---|---|---|
| Neutral | – | Icon in Kartenfarbe | `--km-card-accent` |
| In Ordnung | `km-fact--ok` | Icon und Balken grün | `--km-color-feedback-success` |
| Problem | `km-fact--danger` | Icon und Balken rot | `--km-color-feedback-danger` |
| Frische | Breite von `km-fact__bar > i` | Balkenlänge | `--km-color-track` |
| Leer | kein Wert | Kachel weglassen; leere Felder bleiben ohne Rahmen | – |

## Verhalten

Kein Skript im Kit; Werte, Balkenbreite und Zustand setzt die Seite.

## Text und Wording

- Beschriftung ein bis zwei Wörter; Wert kurz mit Einheit („20,2 h“, „20,9k Z.“); Unterzeile Datum oder Bezug.
- Zustand steckt im Wert („0 Befunde“), nicht nur in der Farbe.

## Barrierefreiheit

- `<dl>` mit `aria-label`; jedes Paar in `div`.
- Balken sind dekorativ (`aria-hidden="true"`), die Zahl steht als Text daneben bzw. in der Unterzeile.
- Kontrast (gerechnet):

| Paar | Kobalt dunkel | Kobalt hell | Papier dunkel | Papier hell |
|---|---|---|---|---|
| Wert `--km-color-text` auf `--km-color-card` | 14,16 | 15,89 | 13,03 | 17,61 |
| Beschriftung, Unterzeile `--km-color-text-dim` auf `--km-color-card` | 6,25 | 6,05 | 5,78 | 6,23 |
| Legende `--km-color-text-dim` auf `--km-color-page` | 7,02 | 5,40 | 6,51 | 5,61 |
| Balken-Spur `--km-color-track` auf `--km-color-card` | 1,28 | 1,31 | 1,27 | 1,26 |
| Icon ok `success` auf `--km-color-card` | 5,55 | 6,01 | 7,51 | 5,17 |
| Icon Problem `danger` auf `--km-color-card` | 5,56 | 6,01 | 6,64 | 5,99 |

Die Spur des Balkens ist schwach; der gefüllte Teil trägt die Aussage, der Wert steht als Text.

## Beispiele

### Richtig

```html
<div class="km-fact km-fact--danger"><dt class="km-fact__label">…Punkte</dt><dd class="km-fact__value">62<small title="4 Sites">4 Sites</small></dd></div>
```

### Falsch

```html
<!-- Wert in Zustandsfarbe -->
<dd class="km-fact__value" style="color:var(--km-color-feedback-danger)">62</dd>
<!-- Balken ohne Zahl -->
<span class="km-bars__bar"><span style="flex:3"></span></span>
```

Warum: Wert immer in derselben Schrift, Größe und Farbe (Story `#kacheln-raster`); Farbe nie allein (Entscheidung 15).

## Seitenregeln

Aus `docs/seitenregeln.md`: keine harten Werte; Datenfarben ≥ 3:1 je Modus; mit eingebetteten Schriften Zahlen mit `tabular-nums` selbst setzen; Raster mit `minmax(min(Xrem, 100%), 1fr)` für schmale Breite.

Entscheidungen: 15 (Kontrast), 17 (Schrift und Ziffern), 27 (schmale Breite).

## Vergleich mit anderen Design-Systemen

| System | Name | Besonderheit | Quelle |
|---|---|---|---|
| GOV.UK Design System | Summary list | Schlüssel-Wert-Paare als `<dl>`; nicht für tabellarische Daten | design-system.service.gov.uk/components/summary-list |

## Verwandte Bausteine

`km-card`, `km-hero`, `km-tables`, `km-deflist`, `km-dot`, `km-footer`.

## Tokens

Rollen: `--km-color-card`, `--km-color-border-card`, `--km-color-track`, `--km-color-text`, `--km-color-text-dim`, `--km-color-text-muted`, `--km-color-accent`, `--km-bar`, `--km-bar-l`, `--km-dot`, `--km-icon-xs`, `--km-space-m`, `--km-space-xs`, `--km-space-3xs`.

- Komponenten-Haken: `--km-card-accent`.
- Direkt gelesen: `--kern-font-size-18`, `--km-color-feedback-success`, `-danger`.
- Hart im Baustein: Mindestbreite `5.75rem`, Balkenbreite `12rem`, Mischung 65 % für das Icon, `filter: brightness(1.6)` an `:root[data-theme="dark"]` in der Legende.

## Offene Punkte

- Wertgröße liest `--kern-font-size-18` direkt; eine Rolle zwischen `m` und `l` fehlt.
- `filter: brightness(…)` an `:root[data-theme="dark"]` greift nicht bei `data-kern-theme`.
- `km-bars` steht in der Fußzeile; ob es dort ein eigener Baustein „Fußzeile“ bleibt, siehe `seitenrahmen.md`.

## Regeln

- Was: Kennzahlen zeigen wenige wichtige Werte auf einen Blick: Fakten-Kacheln `km-facts` mit `km-fact` (Beschriftung, Wert, optional Unterzeile und Frische-Balken `km-fact__bar`), das Raster `km-facts--grid` mit vier Kacheln, die Zustände `km-fact--ok` und `km-fact--danger`, Anteile als `km-bars` und Verteilungen als `km-histo`.
- Wann: Für drei bis sechs Werte zu einer Sache, vier Prüfwerte mit Zustand, Anteile einer Gesamtmenge oder eine Verteilung über Zeiträume; viele Werte je Gruppe gehören in `km-tables`, eine Zahl neben einem Titel in `km-count`, ein Wert ohne Bezeichnung in Text.
- Wie: `<dl class="km-facts" aria-label="…">` mit je einem `div.km-fact` aus `dt.km-fact__label` (ein bis zwei Wörter, Icon in `--km-card-accent`) und `dd.km-fact__value` (kurz mit Einheit, `small` für die Unterzeile), Wert immer in Textfarbe, Zustand im Wert wie „0 Befunde“ und nicht nur in der Farbe, Balkenbreite und Zustand setzt die Seite.
- Prüfen: Fertig ist es, wenn Wert und Beschriftung in allen Themes mindestens 4,5:1 messen, Balken `aria-hidden="true"` sind und die Zahl als Text danebensteht, Datenfarben mindestens 3:1 erreichen und das Raster mit `minmax(min(Xrem, 100%), 1fr)` bei schmaler Breite nicht scrollt.
