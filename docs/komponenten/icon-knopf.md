# Icon-Knopf (`km-iconbtn`)

Status: stabil, in Dashboard und Lagebild im Einsatz · Story: `docs/index.html#zustaende`, `#aufgabe`, `#tabelle`, `#verdeckt` (`--done`), `#suchfeld` (`--label`) · CSS: `src/km-components.css`, Abschnitte „Kleiner Knopf mit Icon“, „Für das Lagebild“ (`--done`), „Ausgewählt gewinnt gegen Hover“ · Stand: 2026-11-09

## Kurzbeschreibung

Der Icon-Knopf ist ein kleiner quadratischer Knopf nur mit Lucide-Icon für häufige Aktionen in Tabellenzeilen, Karten, Aufgaben und der Kopfzeile: anheften, in Arbeit markieren, kopieren, bearbeiten, löschen. Als Umschalter (`aria-pressed`) ist er gedrückt gefüllt im Akzent; für Aktionen mit Wirkung nach außen in der Signalfarbe. Nach dem Kopieren zeigt er kurz einen Erfolgszustand. Die Variante mit Text (`--label`) ist älter und steht für Knöpfe in der Kopfzeile.

## Name und Abgrenzung

- Klasse `km-iconbtn`; Varianten `--on`, `--attention`, `--danger`, `--done`, `--label`. In der Oberfläche ohne sichtbaren Namen, der Name steht in `aria-label`.
- `km-button`: Knopf mit Text in Textschrift; für Aktionen über Listen.
- `kern-btn`: Hauptaktion und Formulare.
- `km-iconbtn--label`: Text in Mono, gleich hoch wie Kopfzeilen-Knöpfe; überschneidet sich mit `km-button` (siehe `knopf.md`).

## Einsatz

### Verwenden, wenn

- eine Aktion je Zeile oder Karte wiederkehrt und ihr Icon allein verständlich ist;
- ein Zustand umgeschaltet wird (angeheftet, in Arbeit);
- kopiert wird (Link, Passwort, Befehl).

### Nicht verwenden, wenn

- das Icon nicht eindeutig ist: `km-button` mit Text;
- die Aktion selten oder gefährlich ist und Bestätigung braucht: Löschen im Menü, zweistufig (Entscheidung 24);
- eine Ansicht gewählt wird: `km-segmented`.

## Verwendung

```html
<td class="km-table__actions"><span class="km-table__actions-row">
  <button type="button" class="km-iconbtn" aria-pressed="false" aria-label="Anheften"><svg class="km-icon" aria-hidden="true">…</svg></button>
  <button type="button" class="km-iconbtn km-iconbtn--attention" aria-pressed="true" aria-label="In Arbeit"><svg class="km-icon" aria-hidden="true">…</svg></button>
  <button type="button" class="km-iconbtn" aria-label="Link kopieren"><svg class="km-icon" aria-hidden="true">…</svg></button>
</span></td>
```

## Aufbau

| Teil | Klasse | Funktion |
|---|---|---|
| Knopf | `km-iconbtn` | Quadrat `--km-control-height` (1.6rem), Rand `--km-color-border-card`, ohne Fläche, Icon gedämpft. |
| Icon | `svg.km-icon` | `--km-icon-xs`, `aria-hidden="true"`. |
| Mit Text | `km-iconbtn--label` | Breite nach Inhalt, Mono, `--km-font-size-xs`. |

## Varianten

- **Umschalter** `aria-pressed` bzw. `--on`: gedrückt Akzentfläche.
- **Signal** `--attention`: gedrückt in `--km-color-attention` (in Arbeit, Freigabe).
- **Gefahr** `--danger`: Hover in der Gefahrfarbe (Löschen).
- **Erledigt** `--done`: kurz nach dem Kopieren grün, setzt das Skript.
- **Mit Text** `--label`.

## Größen

- Eine Größe, 25,59 px außerhalb einer Bedienzeile; in `km-toolbar` gestreckt auf 33,00 px (gemessen, Kobalt dunkel).
- In der Kopfzeile `--km-header-control-height`.

## Zustände

| Zustand | Auslöser | Darstellung | Tokens |
|---|---|---|---|
| Ruhe | – | Icon `--km-color-text-dim`, schwacher Rand | `--km-color-border-card` |
| Hover | `:hover` | Icon voll, Rand `--km-color-border-section` | `--km-color-text` |
| Fokus | `:focus-visible` | Ring außen | `--km-color-focus` |
| Gedrückt | `aria-pressed="true"`, `--on` | Akzentfläche, bleibt unter der Maus | `--km-color-accent`, `--km-color-on-accent` |
| Gedrückt Signal | `--attention` + gedrückt | Signalfläche | `--km-color-attention`, `--km-color-on-attention` |
| Gefahr Hover | `--danger:hover` | Icon und Rand rot | `--km-color-feedback-danger` |
| Kopiert | `--done` | Icon und Rand grün | `--km-color-feedback-success` |
| Deaktiviert | `disabled` | nicht definiert | offen |

## Verhalten

- Natives `button`.
- Kopieren liest den Wert erst beim Klick aus der Zeile (Seitenregeln „Aktionen rechts“), setzt `--done` und nimmt es nach kurzer Zeit wieder weg.
- Umschalter setzen `aria-pressed`.

## Text und Wording

`aria-label` als Verb oder Zustand, gleich in beiden Zuständen („Anheften“, nicht „Angeheftet“ / „Lösen“ im Wechsel); `title` mit demselben Text, wenn ein Tooltip gewünscht ist.

## Barrierefreiheit

- Name über `aria-label` (Pflicht), Icon `aria-hidden`.
- Zielgröße 25,6 px liegt über dem WCAG-2.2-Mindestmaß 24 px (2.5.8), unter den 44 px, die KERN für Kartenaktionen nennt.
- Kontrast (gerechnet):

| Paar | Kobalt dunkel | Kobalt hell | Papier dunkel | Papier hell |
|---|---|---|---|---|
| Icon `--km-color-text-dim` auf `--km-color-card` | 6,25 | 6,05 | 5,78 | 6,23 |
| Gedrückt `--km-color-on-accent` auf `--km-color-accent` | 9,13 | 6,69 | 8,68 | 8,38 |
| Signal `--km-color-on-attention` auf `--km-color-attention` | 8,60 | 5,47 | 8,99 | 5,47 |
| Gefahr `danger` auf `--km-color-card` | 5,56 | 6,01 | 6,64 | 5,99 |
| Rand `--km-color-border-card` auf `--km-color-card` | 1,42 | 1,39 | 1,27 | 1,32 |

Der Rand in Ruhe liegt unter 3:1; den Knopf kennzeichnet das Icon (≥ 3:1) und seine feste Stelle in der Aktionsspalte.

## Beispiele

### Richtig

Knöpfe nur in `km-table__actions` als Block `km-table__actions-row`; drei Zugangsknöpfe in fester Reihenfolge: Link, Passwort, Nachricht.

### Falsch

```html
<button class="km-iconbtn">⚙</button>                 <!-- Schriftzeichen statt Lucide, ohne Namen -->
<td><a class="km-table__name">Host</a><button class="km-iconbtn" aria-label="Kopieren">…</button></td>  <!-- Kopier-Knopf in der Namenszelle -->
```

## Seitenregeln

Aus `docs/seitenregeln.md`: Aktionen rechts in `km-table__actions` mit `km-iconbtn`, Kopier-Knöpfe dort, nicht in Name oder Wert; nur Lucide-Icons; Nur-Icon-Knöpfe bleiben `km-iconbtn`; ausgewählt bleibt ausgewählt; Kopfzeile mit `km-iconbtn--label` gleich hoch; Bedienzeilen in `km-toolbar`.

Entscheidungen: 16 (Icons), 20 (Aktionsspalte), 23 (gleich hoch), 24 (Löschen im Menü).

## Vergleich mit anderen Design-Systemen

| System | Name | Besonderheit | Quelle |
|---|---|---|---|
| Primer (GitHub) | IconButton | Icon statt Text; `aria-label` Pflicht; `description` zeigt einen Tooltip; Größen small, medium, large; Varianten default, primary, danger, invisible, link | primer.style/product/components/icon-button |
| KERN 2.8.2 | Button | Icon-only braucht `kern-sr-only`-Text | kern-ux.de/komponenten/button (siehe `knopf.md`) |

## Verwandte Bausteine

`km-button`, `km-table__actions`, `km-secret`, `km-task__actions`, `km-card__actions`, `km-header__actions`.

## Tokens

- Rollen: `--km-control-height`, `--km-icon-xs`, `--km-color-text-dim`, `--km-color-text`, `--km-color-border-card`, `--km-color-border-section`, `--km-color-accent`, `--km-color-on-accent`, `--km-color-attention`, `--km-color-on-attention`, `--km-color-focus`.
- Rückmelde-Rollen: `--km-color-feedback-danger`, `-success`.
- Hart: `min-height: 2rem` in `km-toolbar`.

## Offene Punkte

- Deaktiviert-Zustand fehlt (`km-iconbtn:disabled` steht nicht in der gemeinsamen Deaktiviert-Regel).
- `--label` (Mono) und `km-button` (Textschrift) zusammenführen oder abgrenzen.
- Rand in Ruhe unter 3:1 in allen Themes.

## Regeln

- Was: `km-iconbtn` ist ein kleiner quadratischer Knopf nur mit Lucide-Icon für häufige Aktionen in Zeilen, Karten, Aufgaben und Kopfzeile; als Umschalter (`aria-pressed` bzw. `--on`) gedrückt im Akzent, dazu `--attention`, `--danger`, `--done` und `--label` (mit Text).
- Wann: Wenn eine Aktion je Zeile oder Karte wiederkehrt und ihr Icon allein eindeutig ist, bei Umschaltern und Kopieren; bei unklarem Icon `km-button` mit Text, bei seltenen oder gefährlichen Aktionen Löschen zweistufig im Menü, für eine Ansicht `km-segmented`.
- Wie: Natives `button` mit Pflicht-`aria-label` (Verb oder Zustand, in beiden Zuständen gleich) und `svg.km-icon` mit `aria-hidden="true"`, nur Lucide-Icons, in Tabellen nur in `km-table__actions-row` (nie in der Namens- oder Wertzelle), Kopieren liest den Wert beim Klick und setzt kurz `--done`, Bedienzeilen in `km-toolbar`.
- Prüfen: Fertig ist es, wenn Ruhe, Hover, Fokus, gedrückt, Gefahr und Kopiert erreichbar sind (Deaktiviert ist nicht definiert), das Icon mindestens 3:1 misst, gedrückt der Text mindestens 4,5:1 misst, die Zielgröße von 25,6 px über den 24 px liegt und ein gewählter Knopf auch unter der Maus gewählt bleibt.
