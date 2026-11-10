# Ziehen und Ablegen (`km-dnd`, `km-resizer`)

Status: stabil, im Dashboard im Einsatz · Story: `docs/index.html#bedienteile`, `#zustaende`, `#zustaende-skript` · CSS: `src/km-components.css`, Abschnitt „Dashboard-Gerüst“ · Stand: 2026-11-09

## Kurzbeschreibung

Teile zum Umsortieren per Ziehen: Griff an einer Zeile (`km-dnd__grip`), Einfügelinie zwischen Zeilen (`km-dnd__line`), Spaltenmarke (`km-dnd__marker`), Mitläufer am Mauszeiger (`km-dnd__ghost`) und die gezogene Tabellenzeile (`km-table__row--dragging`). Bereiche, Aufgaben und Quicklinks haben eigene Zieh-Zustände (`km-section--dragging`, `km-task--dragging`, `km-quicklinks__dragging`). Die Ziehleiste `km-resizer` verändert die Breite der Seitenleiste.

## Name und Abgrenzung

Nur Darstellung; Ziehen, Ablegen, Tastatur-Alternative und Speichern der Rangfolge macht das Skript der Seite (Entscheidung 9: Zeilenordnung als Rangfolge).

## Einsatz

### Verwenden, wenn

- Nutzer*innen die Reihenfolge von Tabellenzeilen, Bereichen, Aufgaben oder Quicklinks selbst festlegen und die Seite sie als Rangfolge innerhalb der Struktur speichert, die das Markup vorgibt (Entscheidung 9); im Lagebild werden Bereiche je Spalte verschoben (das Migrationsprotokoll);
- die Seitenleiste in der Breite verstellbar sein soll (`km-resizer`, Lagebild: drei Spalten, ab 961 px getrennt scrollend, das Migrationsprotokoll); unter 60em blendet das Kit die Ziehleiste aus.

### Nicht verwenden, wenn

- die Seite keinen Weg ohne Maus anbietet (Pfeiltasten oder Knöpfe „nach oben/unten“, WCAG 2.5.7, siehe Barrierefreiheit).

## Verwendung

```html
<tr class="km-table__row--dragging"><td>…<span class="km-dnd__grip" role="button" tabindex="0" aria-label="Projekt 1 verschieben">…</span></td></tr>
<div class="km-dnd__line" style="top:…;left:…;width:…"></div>
<div class="km-resizer" role="separator" aria-orientation="vertical" aria-label="Breite der Seitenleiste" tabindex="0"></div>
```

## Zustände

| Teil | Zustand | Darstellung |
|---|---|---|
| Griff | Ruhe / Zeile Hover / Griff Hover / Fokus | unsichtbar / 55 % / voll / voll |
| Einfügelinie | beim Ziehen | 2 px Akzent mit Quadrat am Anfang |
| Mitläufer | beim Ziehen | Akzentfläche, Name, höchstens 17.5rem |
| Ziehleiste | Hover / `--dragging` | Linie `border-section` / Akzent; unter 60em ausgeblendet |

## Barrierefreiheit

- Ziehen braucht eine Alternative ohne Maus (WCAG 2.5.7): Griff fokussierbar mit Pfeiltasten oder Knöpfe „nach oben/unten“.
- Ziehleiste als `role="separator"` mit `aria-valuenow` und Pfeiltasten.
- Griff unsichtbar in Ruhe: für Tastatur muss er im Fokus sichtbar sein (`:focus-visible` setzt Deckkraft 1).

## Beispiele

### Falsch

Umsortieren nur per Maus, Griff ohne `tabindex` und Namen.

## Seitenregeln

Keine Überlappungen; Abblenden mit `opacity` nur für vorübergehende Zustände (Ziehen). Entscheidungen 9, 15.

## Vergleich mit anderen Design-Systemen

| System | Name | Besonderheit | Quelle |
|---|---|---|---|
| – | – | ungeprüft | – |

## Tokens

- `--km-color-accent`, `--km-color-on-accent`, `--km-color-border-section`, `--km-color-inset`, `--km-color-text-dim`, `--km-border-width-strong`, `--km-dot`, `--km-bar`, `--km-shadow-strong`, `--km-drop-line`.
- Hart: `left: -3px`, `opacity: 0.55`/`0.9`, `z-index` 45, 60, 200.

## Offene Punkte

- Kein Tastaturweg im Kit beschrieben; Vertrag für die Seiten fehlt.
- `--km-drop-line` ist definiert, die Einfügelinie nutzt aber `--km-border-width-strong` direkt.

## Regeln

- Was: Ziehen und Ablegen besteht aus Darstellungsteilen zum Umsortieren per Ziehen (Griff `km-dnd__grip`, Einfügelinie `km-dnd__line`, Spaltenmarke `km-dnd__marker`, Mitläufer `km-dnd__ghost`, gezogene Zeile `km-table__row--dragging`) und der Ziehleiste `km-resizer`, die die Breite der Seitenleiste verändert.
- Wann: Wo Nutzer*innen die Reihenfolge von Zeilen, Bereichen, Aufgaben oder Quicklinks selbst festlegen und die Seite sie als Rangfolge innerhalb der vorgegebenen Struktur speichert, oder wo die Seitenleiste in der Breite verstellbar ist, immer zusammen mit einem Weg ohne Maus; der Baustein liefert nur die Darstellung, Ziehen, Ablegen, Tastaturweg und Speichern der Rangfolge macht das Skript der Seite.
- Wie: Griff als `km-dnd__grip` mit `role="button"`, `tabindex="0"` und `aria-label`, Ziehleiste als `km-resizer` mit `role="separator"`, `aria-orientation="vertical"`, `aria-label` und `tabindex="0"`, Lage der Einfügelinie über Stilangaben der Seite, Farben und Maße über Tokens.
- Prüfen: Fertig ist es, wenn jedes Umsortieren und Verstellen auch ohne Maus geht (Pfeiltasten oder Knöpfe „nach oben/unten“), der Griff im Fokus voll sichtbar ist, Einfügelinie und Mitläufer beim Ziehen erscheinen und die Ziehleiste unter 60em ausgeblendet ist.
