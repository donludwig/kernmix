# Suchfeld und Bedienzeile (`km-searchbox`, `km-toolbar`, `km-filterchips`)

Status: stabil, in Dashboard und Lagebild im Einsatz · Story: `docs/index.html#suchfeld`, `#suche`, `#treffer-kopf`, `#bedienteile` (`km-searchbar`, `km-skillsearch`, `km-toolbar__btn`), `#zustaende-skript` · CSS: `src/km-components.css`, Abschnitte „Werkzeugzeile“, „Info-i, Nach oben, Sync-Schalter, Suchfeld“, „Suche: Ergebnisse, Hinweise, aktive Filter“, „Dashboard-Gerüst“, Schluss-Regeln „Suchfeld: Fokus nur am Rahmen“ · Stand: 2026-11-09

## Kurzbeschreibung

Das Suchfeld ist ein Rahmen mit Eingabefeld, Löschen-Knopf und Trefferzahl, in dem aktive Filter als Chips vor dem Text stehen (`kunde:A`, ausgeschlossen `-tag:alt`). Es steht in der Bedienzeile `km-toolbar` über einer Tabelle oder Liste, zusammen mit Knöpfen, Segmented Control und Spaltenauswahl. Die Bedienzeile streckt alle Elemente auf dieselbe Höhe. Der Fokus zeigt sich einmal am Rahmen, nicht zusätzlich am Eingabefeld.

## Name und Abgrenzung

- `km-searchbox` (Feld), `km-toolbar` (Zeile), `km-filterchips` (aktive Filter im Feld).
- Ältere Suchzeilen: `km-searchbar` (Suchleiste mit Umschaltern) und `km-skillsearch` (einfaches Feld über Karten); neue Seiten nehmen `km-searchbox` in `km-toolbar`.
- Zum Baustein gehören Rahmen, Eingabe, Löschen (`__clear`), Trefferzahl (`__count`, `--none`), Filter-Chips (`__chip`, `__neg`, `__x`), Zeile und Zeilenknopf (`km-toolbar__btn`).
- Nicht dazu: Trefferliste (`km-results`, siehe `trefferliste.md`), Suchlogik und Syntax (Skript der Seite).
- KERN „Input“ (Textfeld in Formularen, ungeprüft) ist größer und trägt Label und Fehlermeldung; `km-searchbox` ist ein Werkzeugfeld ohne sichtbares Label.

## Einsatz

### Verwenden, wenn

- eine Liste oder Tabelle sofort beim Tippen gefiltert wird;
- Filter per Syntax oder aus Hinweisen gesetzt werden und sichtbar bleiben sollen (Filter-Chips);
- mehrere Bedienelemente nebeneinander über einer Liste stehen (`km-toolbar`).

### Nicht verwenden, wenn

- aus einer festen Menge gewählt wird: Auswahl mit Suche (`km-selectpanel`, Seitenregeln „Auswahl mit Suche statt freiem Feld“);
- ein Formularwert eingegeben wird: KERN-Eingabefeld mit Label;
- ein Filter der Seitenleiste gemeint ist: `km-sidebar`.

## Verwendung

```html
<div class="km-toolbar">
  <div class="km-searchbox">
    <span class="km-filterchips"><span class="km-filterchips__chip">kunde:A<button type="button" class="km-filterchips__x" aria-label="Filter kunde:A entfernen"><svg class="km-icon" aria-hidden="true">…</svg></button></span></span>
    <input type="search" placeholder="Projekte durchsuchen …" aria-label="Projekte durchsuchen">
    <button type="button" class="km-searchbox__clear" aria-label="Suche zurücksetzen"><svg class="km-icon" aria-hidden="true">…</svg></button>
  </div>
  <span class="km-searchbox__count" aria-live="polite">3 Treffer</span>
  <div class="km-colpicker">…</div>
</div>
```

## Aufbau

| Teil | Klasse | Funktion |
|---|---|---|
| Zeile | `km-toolbar` | `flex`, umbrechend, `align-items: stretch`, Abstand `--km-space-stack`; streckt direkte Kinder auf die Höhe des höchsten. |
| Rahmen | `km-searchbox` | nimmt den freien Platz (`flex: 1`), Fläche `--km-color-inset`, Rand `--km-color-border-input` (≥ 3:1), mindestens 2.05rem hoch. |
| Eingabe | `km-searchbox input` | ohne eigenen Rand, `--km-font-size-s`, mindestens 8rem breit. |
| Löschen | `km-searchbox__clear` | Lucide `x`, rechts im Rahmen; `hidden`, solange das Feld leer ist. |
| Trefferzahl | `km-searchbox__count`, `--none` | gedämpfte Zahl neben dem Feld; ohne Treffer in der Gefahrfarbe. |
| Filter-Chips | `km-filterchips` (`display: contents`), `__chip`, `__neg`, `__x` | im Rahmen vor der Eingabe; Rand und Text im Akzent, ausgeschlossen gestrichelt. |
| Zeilenknopf | `km-toolbar__btn` | älterer Text-Umschalter in Mono, `km-sync--on` für an; neu: `km-button`. |
| Suchleiste | `km-searchbar` | ältere Zeile mit Eingabe und Umschaltern im Bereichsrumpf. |
| Feld über Karten | `km-skillsearch` | einfaches Eingabefeld mit eigenem Rand, höchstens 32rem. |

## Varianten

- **Suchfeld mit Filtern** (Standard).
- **Suchfeld in einem Panel** (`km-selectpanel__row > .km-searchbox`): volle Breite, ohne Chips.
- **Suchleiste** `km-searchbar` und **Feld** `km-skillsearch`: Altbestand, siehe offene Punkte.
- **Filter-Leiste** `km-filterchips--bar`: dieselben Chips als eigene Zeile oben in jedem Bereich, auf den ein Filter der Seite wirkt, mit Beschriftung `km-filterchips__label` („Gefiltert“) und × je Chip; Farbe eines Kunden als `km-dot` im Chip, Text in Akzent. Vom Filter ausgeblendete Elemente tragen `km-filtered`.

## Größen

- Eine Größe.
- Gemessen (headless Chrome, Kobalt dunkel): Rahmen in `km-toolbar` 33,00 px, daneben `km-iconbtn` und Spaltenauswahl je 33,00 px; das Eingabefeld darin 25,00 px.
- Ohne `km-toolbar` sind die Höhen verschieden (siehe `knopf.md`).

## Zustände

| Zustand | Auslöser | Darstellung | Tokens |
|---|---|---|---|
| Leer | `value=""` | Platzhalter gedämpft, Löschen `hidden` | `--km-color-text-dim` |
| Mit Text | Wert gesetzt | Löschen sichtbar, Zahl daneben | – |
| Fokus | `:has(input:focus-visible)` | Rand und Innenlinie in der Fokusfarbe, eine Linie doppelt so kräftig; kein Ring am Eingabefeld | `--km-color-focus` |
| Mausfokus | `:focus-within` | Rand im Akzent | `--km-color-accent` |
| Keine Treffer | `km-searchbox__count--none` | Zahl in der Gefahrfarbe | `--km-color-feedback-danger` |
| Filter aktiv | `km-filterchips__chip` | Chip im Akzent | `--km-color-accent` |
| Filter ausgeschlossen | `km-filterchips__neg` | Rand gestrichelt | – |
| Löschen Hover | `:hover` | Fläche `--km-color-inset`, Icon voll | `--km-color-text` |

## Verhalten

- Filtern beim Tippen, Syntax (`kunde:`, `-tag:`), Chips aus der Eingabe erzeugen, Löschen und Esc: Skript der Seite.
- Suche in der Adresse und in localStorage (Seitenregeln „Adresse und Speicher“); eine neue Suche hebt einen gesetzten Listenfilter auf.
- Klick ins leere Feld zeigt Suchhinweise (`km-results--hints`).

## Text und Wording

- Platzhalter: „<Gegenstand> durchsuchen …“ mit Auslassungszeichen.
- Trefferzahl: „3 Treffer“, ohne Treffer „0 Treffer“.
- Filter-Chip: `feld:wert` wie in der Syntax, ausgeschlossen mit Minus.

## Barrierefreiheit

- Eingabe mit `aria-label` (kein sichtbares Label); `type="search"` für die Eingabe.
- Löschen und Filter-Entfernen sind Knöpfe mit `aria-label`.
- Trefferzahl als `aria-live="polite"`, damit sie angesagt wird.
- Fokus: eine kräftige Linie am Rahmen (Seitenregeln „Fokus am Suchfeld nur einmal“).
- Kontrast (gerechnet):

| Paar | Kobalt dunkel | Kobalt hell | Papier dunkel | Papier hell |
|---|---|---|---|---|
| Eingabe `--km-color-text` auf `--km-color-inset` | 12,88 | 14,57 | 12,06 | 16,15 |
| Platzhalter `--km-color-text-dim` auf `--km-color-inset` | 5,68 | 5,55 | 5,35 | 5,71 |
| Rand `--km-color-border-input` auf `--km-color-inset` | 5,68 | 5,55 | 5,35 | 5,71 |
| Filter-Chip `--km-color-accent` auf `--km-color-card` | 8,27 | 6,69 | 8,02 | 8,09 |
| Trefferzahl `--km-color-text-dim` auf `--km-color-section` | 6,66 | 5,16 | 6,26 | 5,86 |
| Keine Treffer `danger` auf `--km-color-card` | 5,56 | 6,01 | 6,64 | 5,99 |
| Fokus `--km-color-focus` auf `--km-color-card` | 8,27 | 6,69 | 8,02 | 8,09 |

- Schmal (390 px): Zeile bricht um; das Feld bleibt mindestens 8rem breit.

## Beispiele

### Richtig

```html
<div class="km-toolbar"><div class="km-searchbox"><input type="search" aria-label="Hosts durchsuchen" placeholder="Hosts durchsuchen …"></div><button type="button" class="km-button">…Neue Liste</button></div>
```

### Falsch

```html
<!-- eigene Höhe am Knopf neben dem Feld -->
<div class="km-toolbar"><div class="km-searchbox">…</div><button class="km-button" style="height:28px">…</button></div>
<!-- Feld ohne Bedienzeile, Höhen weichen ab -->
<div><div class="km-searchbox">…</div><button class="km-iconbtn">…</button></div>
<!-- zweiter Fokusrahmen am Eingabefeld -->
<input style="outline:2px solid var(--km-color-focus)">
```

## Seitenregeln

Aus `docs/seitenregeln.md`: Bedienzeilen gleich hoch, immer in `km-toolbar`, nach jeder neuen Zeile messen; Fokus am Suchfeld nur einmal; Ränder von Eingabefeldern ≥ 3:1 über `--km-color-border-input`; Adresse und Speicher; ein Filter zur Zeit aus der Navigation; Logo setzt Suche zurück.

Entscheidungen: 22 (Filter, Adresse, Verlauf), 23 (Bedienzeilen gleich hoch), 15 (Kontrast).

## Vergleich mit anderen Design-Systemen

| System | Name | Besonderheit | Quelle |
|---|---|---|---|
| KERN 2.8.2 | Input | ungeprüft | – |
| GOV.UK Design System | Search | ungeprüft | – |

## Verwandte Bausteine

`km-results`, `km-colpicker`, `km-button`, `km-iconbtn`, `km-segmented`, `km-selectpanel`, `km-clear`.

## Tokens

Rollen: `--km-color-inset`, `--km-color-border-input`, `--km-color-accent`, `--km-color-focus`, `--km-color-text`, `--km-color-text-dim`, `--km-color-card`, `--km-space-stack`, `--km-space-3xs`, `--km-space-2xs`, `--km-space-xs`, `--km-font-size-s`, `--km-font-size-xs`, `--km-icon-xs`, `--km-icon-l`.

- Komponenten-Haken: `--chip` (Farbe eines Filter-Chips, ohne Präfix).
- Hart im Baustein: `min-height: 2.05rem`, Eingabe-Mindestbreite `8rem`, Strich der Chip-Icons `1.4` mit eckigen Enden (folgt nicht dem Theme), `filter: brightness(1.35)` für Chips unter `:root[data-theme="dark"]`.

## Offene Punkte

- Icons in Filter-Chips und Trefferliste setzen Strich und Enden hart (`stroke-width: 1.4; stroke-linecap: square`), statt `--km-icon-*` aus dem Theme (Entscheidung 16).
- `filter: brightness(…)` hängt an `:root[data-theme="dark"]`; die Themes schalten über `data-kern-theme`. Die Regel greift in Kit-Seiten nicht.
- Drei Suchzeilen (`km-searchbox`, `km-searchbar`, `km-skillsearch`); `km-skillsearch input` trägt eigenen Rand und Fokus. Zusammenführen auf `km-searchbox`.
- `km-toolbar__btn` (Mono) überschneidet sich mit `km-button` (Textschrift); Seitenregel „keine Text-Knöpfe in Mono-Schrift“.

## Regeln

- Was: Das Suchfeld `km-searchbox` ist ein Rahmen mit Eingabe, Löschen-Knopf, Trefferzahl und aktiven Filtern als `km-filterchips` vor dem Text und steht mit anderen Bedienelementen in der Bedienzeile `km-toolbar`; Varianten sind das Feld in einem Panel (`km-selectpanel__row`) und die Filter-Leiste `km-filterchips--bar`.
- Wann: Wenn eine Liste oder Tabelle beim Tippen gefiltert wird oder Filter sichtbar bleiben sollen; bei fester Menge `km-selectpanel`, bei Formularwerten das KERN-Eingabefeld mit Label, für Filter der Seitenleiste `km-sidebar`.
- Wie: `km-toolbar` mit `km-searchbox` darin, `input type="search"` mit `aria-label`, `km-searchbox__clear` und Chip-Entfernen als Knöpfe mit `aria-label`, Trefferzahl als `km-searchbox__count` mit `aria-live="polite"`, Platzhalter „<Gegenstand> durchsuchen …“, Chips als `feld:wert`, ausgeschlossen mit Minus; keine eigene Höhe am Nachbarknopf.
- Prüfen: Fertig ist es, wenn alle Elemente der Bedienzeile gleich hoch sind (33,00 px gemessen), der Fokus nur als eine Linie am Rahmen und nicht am Eingabefeld erscheint, der Rand mindestens 3:1 und der Text in allen Themes mindestens 4,5:1 misst und die Zeile bei 390 px umbricht, das Feld aber mindestens 8rem breit bleibt.
