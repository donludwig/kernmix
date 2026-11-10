# Kleinteile (`km-clear`, `km-info`, `km-count`, `km-dot`, `km-caret`, `km-peek`, `km-timelog`)

Status: stabil, in Dashboard und Lagebild im Einsatz · Story: `docs/index.html#einheitlich`, `#kleinteile`, `#gruppe` (`km-dots`), `#werkzeugfarben`, `#vorschaukarte`, `#zeitlog` · CSS: `src/km-components.css`, Abschnitte „Einheitliche Bedienelemente“, „Info-i, Nach oben, Sync-Schalter“, „Vorschaukarte“, „Zeitlog“ · Stand: 2026-11-09

## Kurzbeschreibung

Je Bedienelement ein Baustein: Schließen und Leeren (`km-clear`, Lucide „x“), Info-Symbol (`km-info`, `km-infoi`, Lucide „info“), Zähler (`km-count`, gerahmt `--boxed`), Farbpunkt (`km-dot`, Reihe `km-dots`), Aufklapp-Pfeil (`km-caret`, zu `--zu`). Dazu zwei kleine Anzeigen: die Vorschaukarte (`km-peek`), die beim Überfahren eines Auslösers schwebt, und die Zeitlog-Zeile (`km-timelog`) unter einer Projektkarte. Ältere Klassen derselben Sache (`km-searchbox__clear`, `km-sidebar__count`, `km-table__toggle` …) stehen in denselben Selektorlisten und sehen gleich aus.

## Name und Abgrenzung

| Baustein | Gleich gezeichnet wie | Zweck |
|---|---|---|
| `km-clear` | `km-searchbox__clear`, `km-results__clear`, `km-filterchips__x` | Inhalt leeren, Filter entfernen, schließen |
| `km-info`, `km-infoi` | – | Erklärung per Tooltip bzw. Teilbild per Vorschaukarte |
| `km-count`, `--boxed` | `km-sidebar__count`, `km-segmented__count`, `km-table__group-count`, `km-section__count` | Anzahl neben einem Namen |
| `km-dot`, `km-dots__dot` | `km-sidebar__dot`, `km-brand__dot`, `km-results__dot`, `km-bars__sw` | Datenfarbe (Werkzeug, Kunde) |
| `km-caret`, `--zu` | `km-sidebar__caret`, `km-table__toggle`, `km-cardgroup__toggle`, Pfeil am Bereichs- und Kartentitel | offen nach unten, zu nach rechts |
| `km-peek` | – | Vorschau mit Bild 1200:630, Titel, vier Zeilen Text; nur Anzeige |
| `km-timelog` | – | investierte Stunden mit Aufschlüsselung und Link |

Werkzeugfarben `--km-color-tool-code`, `-design`, `-desktop`, `-chat`, `-chatgpt` sind Datenfarben für Punkte, Ränder und Balken, nie Textfarbe.

## Einsatz

### Verwenden, wenn

die Seite eines dieser Kleinteile braucht; nie ein eigenes bauen.

### Nicht verwenden, wenn

- eine Zahl ein Wert der Zeile ist: Tabellenspalte `__num`;
- eine Farbe Bedeutung trägt (Zustand): `km-pill` mit Text;
- die Vorschau bedienbar sein soll: Karte oder Dialog.

## Verwendung

```html
<button type="button" class="km-clear" aria-label="Suche leeren"><svg class="km-icon" aria-hidden="true">…x…</svg></button>
<button type="button" class="km-info" aria-label="Was heißt Score?" title="Punkte aus 21 Kriterien"><svg class="km-icon" aria-hidden="true">…info…</svg></button>
<span class="km-count">12</span> <span class="km-count km-count--boxed">36 offen</span>
<span class="km-dot" style="--km-dot-color:var(--km-color-tool-code)" aria-hidden="true"></span>
<span class="km-caret km-caret--zu" aria-hidden="true"></span>
```

## Aufbau und Größen

- `km-clear`: Quadrat `--km-icon-l` (20 px), Icon `--km-icon-xs`, ohne Rand.
- `km-info`: ohne Rand, Icon `--km-icon-xs`; als Knopf `cursor: pointer`, sonst `help`; in Tabellen mittig zur ersten Zeile.
- `km-count`: `--km-font-size-xs`, gleich breite Ziffern, gedämpft; `--boxed` Mono, gerahmt, `--km-control-height` hoch.
- `km-dot`: Quadrat `--km-dot` (8 px), Farbe `--km-dot-color`.
- `km-caret`: Maske `--km-caret-mask`, `--km-icon-2xs`, dreht 0,15 s.
- `km-peek`: `position: fixed`, 26rem, Schatten; Lage setzt das Skript.
- `km-timelog`: Fläche `inset`, Kante links `border-card`, Stunden in Mono.

## Zustände

| Baustein | Zustand | Darstellung |
|---|---|---|
| `km-clear` | Hover | Fläche `inset`, Icon voll |
| `km-info` | Hover | Icon voll |
| `km-count` | im gewählten Segment / Eintrag | Textfarbe des Trägers |
| `km-caret` | zu | `--zu` bzw. Zustand des Trägers (`aria-expanded="false"`, `--collapsed`, ohne `open`) |
| `km-peek` | ohne Bild / Text | Teil entfällt (`:empty`) |
| alle Knöpfe | Fokus | Ring außen in `--km-color-focus` |

## Barrierefreiheit

- `km-clear` und `km-info` als Knöpfe brauchen `aria-label`; Tooltips nur per `title` erreichen Tastatur und Touch nicht.
- `km-dot` und `km-caret` sind dekorativ (`aria-hidden`); Bedeutung steht als Text bzw. in `aria-expanded`.
- `km-peek` hat `pointer-events: none` und ist für Screenreader nicht erreichbar; der Inhalt muss auch anders zugänglich sein (Karte).
- Kontrast (gerechnet): Zähler `--km-color-text-dim` auf `--km-color-card` 6,25 / 6,05 / 5,78 / 6,23; Werkzeugfarben auf `--km-color-card`: design 5,36 / 4,99 / 5,20 / 4,82, desktop 8,47 / 4,99 / 8,22 / 4,83, chat 4,25 / 3,94 / 4,12 / 3,81, chatgpt 4,13 / 4,05 / 4,01 / 3,92, code = Akzent 8,27 / 6,69 / 8,02 / 8,09 (Kobalt dunkel, Kobalt hell, Papier dunkel, Papier hell).
- Alle Datenfarben ≥ 3:1.

## Beispiele

### Falsch

```html
<button>×</button>  <span>▸</span>  <span style="color:#84cc16">Desktop</span>  <!-- Schriftzeichen, Datenfarbe als Text -->
<button class="km-infoi">i</button>                                           <!-- Buchstabe statt Lucide „info“ (Story #kleinteile) -->
```

## Seitenregeln

- Nur Lucide-Icons, auch in CSS (Masken); keine Schriftzeichen; Symbol mittig zur ersten Zeile; Datenfarben ≥ 3:1 je Modus; Abstand Etikett–Text per `gap`.
- Entscheidungen: 15, 16, 18.

## Vergleich mit anderen Design-Systemen

| System | Name | Besonderheit | Quelle |
|---|---|---|---|
| Primer (GitHub) | CounterLabel | „Adds a count to navigational elements and buttons“; Varianten primary (dunkler Grund) und secondary | primer.style/product/components/counter-label |

## Verwandte Bausteine

`km-searchbox`, `km-sidebar`, `km-segmented`, `km-table`, `km-section`, `km-card`.

## Tokens

- `--km-icon-l`, `--km-icon-xs`, `--km-icon-2xs`, `--km-dot`, `--km-dot-color`, `--km-caret-mask`, `--km-mask-x`, `--km-control-height`, `--km-color-text-dim`, `--km-color-text-muted`, `--km-color-inset`, `--km-color-track`, `--km-color-tool-*`.
- Hart: `km-peek` 26rem, `z-index: 1000`; `km-infoi` Versatz mit `1.25rem`.

## Offene Punkte

- Story `#kleinteile` zeigt `km-infoi` mit dem Buchstaben „i“ statt Lucide „info“.
- Werkzeugfarben `-design`, `-desktop`, `-chat`, `-chatgpt` sind harte Hex-Werte in `km-roles.css` (Ausnahme von „Rollen verweisen nur auf KERN“).
- `km-peek` ohne Weg für Tastatur und Screenreader.

## Regeln

- Was: Kleinteile sind je ein Baustein pro Bedienelement: Schließen und Leeren `km-clear`, Info-Symbol `km-info` und `km-infoi`, Zähler `km-count` (gerahmt `--boxed`), Farbpunkt `km-dot` in der Reihe `km-dots`, Aufklapp-Pfeil `km-caret` (zu `--zu`), dazu die Vorschaukarte `km-peek` und die Zeitlog-Zeile `km-timelog`.
- Wann: Immer wenn die Seite eines dieser Elemente braucht, nie ein eigenes bauen; ein Zeilenwert gehört in die Tabellenspalte `__num`, eine Farbe mit Bedeutung in `km-pill` mit Text, eine bedienbare Vorschau in Karte oder Dialog.
- Wie: Nur Lucide-Icons und Masken wie `--km-caret-mask`, keine Schriftzeichen; `km-clear` und `km-info` als `button` mit `aria-label`, `km-dot` mit `--km-dot-color` aus einer `--km-color-tool-*`-Rolle und `km-caret` mit `aria-hidden`, Werkzeugfarben nie als Textfarbe.
- Prüfen: Fertig ist es, wenn jeder Knopf einen Fokusring in `--km-color-focus` zeigt, `km-caret` den Zustand des Trägers (`aria-expanded`, `--collapsed`, ohne `open`) abbildet, der Zähler in allen Themes mindestens 4,5:1 misst, alle Datenfarben mindestens 3:1 erreichen und der Inhalt von `km-peek` auch ohne Hover zugänglich ist.
