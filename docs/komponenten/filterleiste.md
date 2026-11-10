# Filter-Leiste und Filtergruppe (`km-filterchips--bar`, `km-sidebar__group--filter`)

Status: stabil, im Dashboard im Einsatz · Story: `docs/index.html#filterleiste` · CSS: `src/km-components.css`, Abschnitte „Filter über mehrere Bereiche“ und „Filtergruppe der Seitenleiste“, Chips im Abschnitt „Suche: Ergebnisse, Hinweise, aktive Filter“ · Stand: 2026-11-09

## Kurzbeschreibung

Wirken Filter einer Seite auf mehrere Bereiche, zeigt oben in jedem betroffenen Bereich eine Filter-Leiste die aktiven Filter als Chips mit ×; so ist klar, warum etwas fehlt. In der Seitenleiste stehen dieselben Filter als eigene Gruppe „Filter“ oberhalb der Bereiche, Unterebenen rekursiv eingerückt. Vom Filter ausgeblendete Elemente tragen `km-filtered`.

## Name und Abgrenzung

- Klassen: Leiste `km-filterchips--bar`, Beschriftung `km-filterchips__label`, Chip `km-filterchips__chip`, Aufheben `km-filterchips__x`, ausgeblendet `km-filtered`, Gruppe der Seitenleiste `km-sidebar__group--filter`.
- Im Suchfeld bleibt `km-filterchips` ohne Modifier (`display: contents`), die Chips stehen dort im Feld.
- Welche Dinge zum Filter passen, entscheidet die Seite an einer Stelle (die Übersicht); der Baustein zeigt nur die aktiven Filter und blendet aus.
- Die übrigen Einträge der Seitenleiste, ihre Zustände und der Einzug gehören zur Seitenleiste (`seitenleiste.md`).

## Einsatz

### Verwenden, wenn

- ein Filter der Navigation in mehreren Bereichen derselben Seite gilt (Übersicht, Karten, Aufgaben, Listen);
- Nutzer\*innen sehen sollen, warum ein Bereich weniger zeigt, und den Filter dort aufheben wollen.

### Nicht verwenden, wenn

- Filter nur im Suchfeld gelten: dort `km-filterchips` ohne `--bar`;
- ein Bereich andere Dinge zeigt, für die es die Eigenschaft nicht gibt: dort keine Leiste.

## Verwendung

```html
<div class="km-filterchips km-filterchips--bar">
  <span class="km-filterchips__label"><svg class="km-icon" aria-hidden="true">…</svg>Gefiltert</span>
  <span class="km-filterchips__chip"><span class="km-dot" style="--km-dot-color:var(--km-color-data-2)"></span>kunde:Kunde A<button type="button" class="km-filterchips__x" aria-label="Filter Kunde A aufheben"><svg class="km-icon" aria-hidden="true">…</svg></button></span>
</div>
```

## Aufbau

| Teil | Klasse | Funktion |
|---|---|---|
| Leiste | `km-filterchips--bar` | Zeile mit Umbruch, über die ganze Breite eines Rasters (`grid-column: 1 / -1`), Abstand `--km-space-tight` bzw. `--km-space-xs`. |
| Beschriftung | `km-filterchips__label` | Icon und Text in `--km-color-text-dim`, Größe xs. |
| Chip | `km-filterchips__chip` | Rahmen und Text in Akzent auf Kartenfläche; Kundenfarbe als `km-dot` im Chip. |
| Aufheben | `km-filterchips__x` | Knopf mit Icon x; seine Klickfläche deckt den ganzen Chip ab. |
| Ausgeblendet | `km-filtered` | `display: none !important`, stärker als die Anzeige der Bausteine. |
| Filtergruppe | `km-sidebar__group--filter` | eigene Gruppe der Seitenleiste; Zwischen-Labels beim ersten Textzeichen von „Filter“, ihre Einträge beim ersten Textzeichen ihres Labels (DDR 47). |

## Zustände

| Zustand | Auslöser | Darstellung | Tokens |
|---|---|---|---|
| Ruhe | Chip mit `km-filterchips__x` | Rahmen und Text in Akzent auf Kartenfläche, Zeiger als Hand | `--km-color-accent`, `--km-color-card` |
| Hover | `:hover` am Chip | Fläche mit Akzent getönt, × in Textfarbe | `--km-color-action-state-opacity-selected`, `--km-color-text` |
| Dunkel | Modus dunkel | Chip aufgehellt über einen Filter | `--km-component-chip-filter` (hell `none`) |
| Ausgeblendet | `km-filtered` | Element entfällt, Zähler zählen es nicht mit | – |
| Eingeklappt | `km-sidebar--rail` | Filtergruppe entfällt wie jede Unterebene | – |

## Verhalten

- Ein Klick auf den Chip oder sein × hebt den Filter auf; das Skript der Seite setzt Filter, Leiste und `km-filtered`.
- Zähler folgen den Filtern überall; eine Gruppe ohne sichtbaren Eintrag verschwindet samt Kopf (`km-filtered`).
- Filter stehen in der Adresse und in localStorage; jede Filterwahl ist ein Schritt im Verlauf (Seitenregeln „Filter und Zustand“, „Filter und Verlauf“).

## Barrierefreiheit

- Das × ist ein natives `button` mit `aria-label`, das den Filter nennt („Filter Kunde A aufheben“).
- Icons tragen `aria-hidden="true"`.
- Kontrast (gerechnet in der Story, headless Chrome, Filter im Dunkelmodus eingerechnet):

| Paar | Kobalt dunkel | Kobalt hell | Papier dunkel | Papier hell |
|---|---|---|---|---|
| Chip: Akzent auf Kartenfläche | 12,98 | 6,69 | 12,28 | 8,09 |
| Beschriftung `--km-color-text-dim` | 7,02 | 5,56 | 6,51 | 5,61 |
| Gewählter Eintrag der Filtergruppe | 6,44 | 4,66 | 6,36 | 5,79 |

## Seitenregeln

Aus `docs/seitenregeln.md`: Filter wirken auf alle Bereiche mit denselben Dingen, stehen als eigene Gruppe „Filter“ oberhalb der Bereiche, oben in jedem betroffenen Bereich zeigt die Filter-Leiste die aktiven Filter mit ×; Zähler folgen den Filtern überall; vorgefertigte Filter schließen sich aus.

## Verwandte Bausteine

`km-sidebar` (Seitenleiste), `km-searchbox` (Chips im Suchfeld), `km-dot`, `km-results`.

## Tokens

Rollen: `--km-color-accent`, `--km-color-card`, `--km-color-text`, `--km-color-text-dim`, `--km-color-action-state-opacity-selected`, `--km-space-tight`, `--km-space-xs`, `--km-space-icon-text`, `--km-font-size-xs`, `--km-icon-xs`, `--km-icon-l`, `--km-component-sidebar-indent-label`.

- Komponenten-Tokens: `--km-component-chip-filter`.

## Regeln

- Was: Die Filter-Leiste `km-filterchips--bar` zeigt die aktiven Filter einer Seite oben in jedem betroffenen Bereich als Chips mit ×, die Filtergruppe `km-sidebar__group--filter` stellt dieselben Filter als eigene Gruppe der Seitenleiste.
- Wann: Nur, wenn ein Filter der Navigation in mehreren Bereichen gilt; Filter im Suchfeld bleiben `km-filterchips` ohne `--bar`.
- Wie: Leiste mit `km-filterchips__label` und je Filter einem `km-filterchips__chip` mit `km-filterchips__x` samt `aria-label`, Ausgeblendetes mit `km-filtered`, die Gruppe oberhalb der Bereiche.
- Prüfen: Fertig ist es, wenn × den Filter aufhebt, Zähler nur Sichtbares zählen und Text in allen Themes mindestens 4,5:1 misst.
