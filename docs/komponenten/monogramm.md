# Monogramm (`km-monogram`)

Status: stabil, in Dashboard und Lagebild im Einsatz · Story: `docs/index.html#tabelle`, `#tabelle-spalten`, `#quicklinks`, `#selectpanel` (laut Seitenregel) · CSS: `src/km-components.css`, Abschnitt „Monogramm“ · Stand: 2026-11-09

## Kurzbeschreibung

Das Monogramm ist eine kleine quadratische Kachel mit einem Kürzel aus zwei Zeichen in der Farbe eines Projekts oder einer Gruppe. Es steht vor dem Namen in der Tabelle, in Quicklinks und in Auswahlmenüs und hilft beim Wiedererkennen. Es ist Schmuck: Der Name steht immer daneben als Text.

## Name und Abgrenzung

- Klasse `km-monogram`; Farbe über `--km-monogram-color`, Kantenlänge `--km-monogram-size`.
- Nicht dazu: Favicon oder Logo (`img` an derselben Stelle), Farbpunkt `km-dot` (ohne Kürzel), Icon-Kachel `km-card__tile`.
- Vergleichbar mit einem Avatar mit Initialen in anderen Systemen (ungeprüft).

## Einsatz

### Verwenden, wenn

- Dinge einer Liste eine Farbe und ein Kürzel haben (Projekte) und kein Favicon vorhanden ist.

### Nicht verwenden, wenn

- nur die Farbe zählt: `km-dot`;
- das Kürzel die einzige Benennung wäre;
- es ein Icon gibt, das die Art zeigt: `km-icon`.

## Verwendung

```html
<a class="km-table__name" href="#p1"><span class="km-monogram" style="--km-monogram-color:var(--km-color-tool-design)" aria-hidden="true">P1</span>Projekt 1</a>
```

## Aufbau

| Teil | Klasse | Funktion |
|---|---|---|
| Kachel | `km-monogram` | Quadrat `--km-monogram-size` (1.25rem), Fläche `--km-monogram-color` (Standard `--km-color-text-dim`), Text weiß oder schwarz je nach Helligkeit der Fläche (OKLCH L < 0,565 weiß, sonst schwarz; Rückfall `--km-color-on-data`), 0.6rem fett, mittig. |

## Größen

Eine Größe; die Marke der Komponentenbeschreibung vergrößert sie auf das 1,6-Fache. Gemessen 20,00 px (Kobalt dunkel). Die Zeilennummer der Tabelle steht mittig dazu.

## Zustände

Nur fachliche Zustände, aus `src/km-components.css`, Abschnitt „Monogramm“. Hover und Fokus hat das Monogramm nicht; sie liegen am umgebenden Link (`a.km-table__name:hover` unterstreicht den Namen).

| Zustand | Auslöser | Darstellung | Tokens |
|---|---|---|---|
| Ohne eigene Farbe | `--km-monogram-color` nicht gesetzt | Fläche gedämpft | `--km-color-text-dim` |
| Projekt- oder Gruppenfarbe | `--km-monogram-color` gesetzt | Fläche in dieser Farbe | `--km-monogram-color` |
| Dunkle Fläche | OKLCH-Helligkeit L < 0,565 | Kürzel weiß | – |
| Helle Fläche | L ≥ 0,565 | Kürzel schwarz | – |
| Browser ohne `oklch(from …)` | keine Relative Color Syntax | Kürzel in der Rückfallfarbe | `--km-color-on-data` |

## Text und Wording

Zwei Zeichen, Großbuchstaben oder Buchstabe plus Ziffer; dasselbe Kürzel wie in der Seitenleiste bzw. im Projekt.

## Barrierefreiheit

- `aria-hidden="true"`: das Kürzel ist dekorativ, der Name folgt als Text (Rollen-Kommentar „dekorativ“).
- Kontrast (gemessen im Browser, Text automatisch weiß oder schwarz):

| Fläche | Kobalt dunkel | Kobalt hell | Papier dunkel | Papier hell |
|---|---|---|---|---|
| Standard `--km-color-text-dim` | 7,84 | 6,05 | 7,48 | 6,45 |
| `--km-color-accent` (tool-code) | 10,39 | 6,69 | 10,37 | 8,38 |
| `--km-color-tool-design` | 6,73 | 4,99 | 6,73 | 4,99 |
| `--km-color-tool-desktop` | 10,63 | 4,99 | 10,63 | 4,99 |
| `--km-color-tool-chat` | 5,33 | 5,33 | 5,33 | 5,33 |
| `--km-color-tool-chatgpt` | 5,18 | 5,18 | 5,18 | 5,18 |

Jede Fläche erreicht mindestens 4,5:1, weil das Kürzel je nach Helligkeit der Fläche weiß oder schwarz wird (Relative Color Syntax, `oklch(from …)`); Browser ohne diese Syntax nehmen `--km-color-on-data`.

## Beispiele

### Richtig

Monogramm mit `aria-hidden`, Name als Text daneben, Farbe aus einer Rolle.

### Falsch

```html
<span class="km-monogram" style="--km-monogram-color:#ff00aa">P1</span>  <!-- harte Farbe, Name fehlt -->
```

## Seitenregeln

Aus `docs/seitenregeln.md`: jede Liste von Dingen ist die Standard-Tabelle mit Name, Monogramm oder Favicon; auch in Auswahlmenüs steht das Monogramm vor dem Namen; Maße über `--km-monogram-size`; Laufende Nummer mittig zum Monogramm; Beispiele ohne harte Farben.

Entscheidungen: 15 (Kontrast), 19 (Standard-Tabelle).

## Vergleich mit anderen Design-Systemen

| System | Name | Besonderheit | Quelle |
|---|---|---|---|
| Primer (GitHub) | Avatar | ungeprüft | – |

## Verwandte Bausteine

`km-table__name`, `km-quicklinks`, `km-selectpanel`, `km-dot`, `km-header__icon`.

## Tokens

- Rollen: `--km-color-on-data`, `--km-color-text-dim`, `--km-font`, `--km-font-size-monogram`, `--km-monogram-size`.
- Haken: `--km-monogram-color`.
- Hart: `font-weight: 700`.

## Offene Punkte

- Quicklinks setzen am Monogramm zusätzlich eine eigene Größe (`km-quicklinks__pill-icon`, 1.25rem fest) statt `--km-monogram-size`.
- `aria-hidden` steht in keiner Story am Monogramm.

## Regeln

- Was: Das Monogramm `km-monogram` ist eine kleine quadratische Kachel mit einem Kürzel aus zwei Zeichen in der Farbe eines Projekts oder einer Gruppe, rein dekorativ, in einer Größe (`--km-monogram-size`).
- Wann: Wenn Dinge einer Liste eine Farbe und ein Kürzel haben und kein Favicon vorhanden ist; zählt nur die Farbe, nimm `km-dot`, gibt es ein Icon für die Art, nimm `km-icon`, und das Kürzel ist nie die einzige Benennung.
- Wie: `<span class="km-monogram" style="--km-monogram-color:var(--km-color-tool-design)" aria-hidden="true">P1</span>` vor dem Namen als Text, zwei Zeichen (Großbuchstaben oder Buchstabe plus Ziffer) wie in der Seitenleiste, Farbe aus einer Rolle und nie hart, Größe nur über `--km-monogram-size`.
- Prüfen: Fertig ist es, wenn das Kürzel auf jeder Fläche in allen Themes mindestens 4,5:1 misst (weiß auf dunkler, schwarz auf heller Fläche), ohne gesetzte Farbe die Fläche `--km-color-text-dim` zeigt, `aria-hidden="true"` gesetzt ist und der Name als Text daneben steht; Hover und Fokus trägt der umgebende Link, nicht das Monogramm.
