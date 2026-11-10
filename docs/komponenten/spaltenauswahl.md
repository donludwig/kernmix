# Spaltenauswahl (`km-colpicker`)

Status: stabil, in Dashboard und Lagebild im Einsatz · Story: `docs/index.html#suchfeld`, `#zustaende-skript` · CSS: `src/km-components.css`, Abschnitte „Spalten-Auswahl“, Schluss-Regeln „Spaltenauswahl wie die übrigen Auswahl-Menüs“ und „Ausgewählt gewinnt gegen Hover“ · Stand: 2026-11-09

## Kurzbeschreibung

Die Spaltenauswahl blendet Spalten einer Tabelle ein und aus. Ein Knopf „Spalten“ in der Bedienzeile öffnet ein Panel mit einem Kästchen je Spalte, jedes mit dem Icon aus dem Spaltenkopf, und darunter benannte Sets („Überblick“, „Pflege“, „Alle“), die eine fertige Kombination setzen. Ein Set ist gedrückt, wenn die Auswahl ihm genau entspricht. Weicht die Auswahl vom Standard ab, zeigt der Knopf die Anzahl („5/9“). Name und Aktionen bleiben immer sichtbar.

## Name und Abgrenzung

- Klasse `km-colpicker`; in der Oberfläche „Spalten“.
- Zum Baustein gehören Hülle, Knopf (`__btn`, `__btn--filter`), Zähler (`__count`), Panel (`__panel`, `__panel--open`), Kopfzeilen (`__head`, `__head--sets`), Zeilen (`label` mit Kästchen), Sets (`__sets`, `__set`).
- Nicht dazu: welche Spalten es gibt und das Ein- und Ausblenden der Zellen (Skript der Seite, Spaltennamen aus `kmTabelle()`).
- `km-selectpanel`: allgemeine Auswahl mit Suche; die Spaltenauswahl hat keine Suche, dafür Sets, und ihr Panel hängt absolut am Knopf statt `fixed`.

## Einsatz

### Verwenden, wenn

- eine Standard-Tabelle mehr Spalten hat, als in eine Breite passen;
- es wiederkehrende Sichten gibt, die als Set benannt werden können.

### Nicht verwenden, wenn

- die Tabelle wenige Spalten hat: alle zeigen, quer scrollen;
- Zeilen gefiltert werden sollen: Suchfeld oder Seitenleiste.

## Verwendung

```html
<div class="km-colpicker">
  <button type="button" class="km-colpicker__btn km-iconbtn km-iconbtn--label km-colpicker__btn--filter" aria-expanded="true" aria-controls="cp-projekte">Spalten<span class="km-colpicker__count">5/9</span><svg class="km-icon" aria-hidden="true"><!-- chevron-down --></svg></button>
  <div class="km-colpicker__panel km-colpicker__panel--open" id="cp-projekte" role="group" aria-label="Sichtbare Spalten">
    <div class="km-colpicker__head">Sichtbare Spalten</div>
    <label><input type="checkbox" checked><svg class="km-icon" aria-hidden="true">…</svg><span>Typ</span></label>
    <div class="km-colpicker__head km-colpicker__head--sets">Sets</div>
    <div class="km-colpicker__sets"><button type="button" class="km-colpicker__set" aria-pressed="true">Überblick</button><button type="button" class="km-colpicker__set" aria-pressed="false">Alle</button></div>
  </div>
</div>
```

## Aufbau

| Teil | Klasse | Funktion |
|---|---|---|
| Hülle | `km-colpicker` | Bezugspunkt (`position: relative`). |
| Knopf | `km-colpicker__btn` | Textschrift `--km-font-size-xs`, Fläche `--km-color-inset`; meist zusammen mit `km-iconbtn km-iconbtn--label`. |
| Zähler | `km-colpicker__count` | nur sichtbar mit `__btn--filter` (Auswahl weicht ab). |
| Panel | `km-colpicker__panel` | absolut unter dem Knopf, rechtsbündig, Schatten, mindestens 12rem; zu ohne `--open`. |
| Kopfzeile | `km-colpicker__head`, `--sets` | Versalien, gedämpft; vor den Sets mit Linie. |
| Zeile | `label` mit `input[type=checkbox]` | Kästchen im Stil `km-check`, Icon der Spalte, Name. |
| Sets | `km-colpicker__sets`, `km-colpicker__set` | Knöpfe mit `aria-pressed`, gedrückt gefüllt im Akzent. |

## Varianten

Eine Variante.

## Größen

Eine Größe. Gemessen (headless Chrome, Kobalt dunkel): Knopf in `km-toolbar` 33,00 px, gleich hoch wie Suchfeld und `km-iconbtn`.

## Zustände

| Zustand | Auslöser | Darstellung | Tokens |
|---|---|---|---|
| Zu | ohne `__panel--open` | Panel `display: none` | – |
| Offen | `__panel--open`, Knopf `aria-expanded="true"` | Panel mit Schatten | `--km-shadow-strong` |
| Auswahl weicht ab | `__btn--filter` | Zähler „5/9“ im Knopf | – |
| Spalte an / aus | `input:checked` | Kästchen gefüllt / leer | `--km-color-accent` |
| Spalte fest | `input:disabled` (Name, Aktionen) | Kästchen abgeblendet | `--km-opacity-disabled` |
| Set gedrückt | `aria-pressed="true"` | Akzentfläche, bleibt unter der Maus | `--km-color-accent`, `--km-color-on-accent` |
| Zeile Hover | `label:hover` | Fläche `--km-color-inset` | – |
| Knopf Hover | `:hover` | Fläche `--km-color-inset`, Text voll | – |

## Verhalten

- Öffnen, Schließen (Esc, Klick daneben), Anwenden und Speichern: Skript der Seite.
- Spaltenauswahl wird gespeichert und bleibt beim Zurücksetzen über das Logo; in der Adresse steht sie nur, wenn sie gerade geändert wurde (Seitenregeln „Adresse und Speicher“).
- Spalten, die für keinen sichtbaren Zeilentyp gelten, blendet die Seite aus, unabhängig von der Auswahl.

## Text und Wording

- Knopf „Spalten“; Zähler „sichtbar/gesamt“.
- Spaltennamen wie im Tabellenkopf, Sets ein Wort („Überblick“, „Kunden“, „Pflege“, „Alle“).

## Barrierefreiheit

- Knopf mit `aria-expanded` und `aria-controls`.
- Die Story setzt am Panel `role="menu"`; ein Menü erlaubt nur Menüeinträge, Kästchen und Knöpfe darin brauchen `role="group"` (oder `dialog`) mit `aria-label`.
- Kästchen nativ im `label`; feste Spalten `disabled` statt nur abgeblendet.
- Sets: `aria-pressed`, die Beschriftung ändert sich nicht.
- Kontrast (gerechnet):

| Paar | Kobalt dunkel | Kobalt hell | Papier dunkel | Papier hell |
|---|---|---|---|---|
| Zeile `--km-color-text` auf `--km-color-card` | 14,16 | 15,89 | 13,03 | 17,61 |
| Kopfzeile `--km-color-text-dim` auf `--km-color-card` | 6,25 | 6,05 | 5,78 | 6,23 |
| Set Ruhe `--km-color-text-muted` auf `--km-color-card` | 7,89 | 7,85 | 8,57 | 7,79 |
| Set gedrückt `--km-color-on-accent` auf `--km-color-accent` | 9,13 | 6,69 | 8,68 | 8,38 |
| Kästchen-Rand `--km-color-border-input` auf `--km-color-card` | 6,25 | 6,05 | 5,78 | 6,23 |

## Beispiele

### Richtig

Name und Aktionen fehlen in der Liste oder stehen dort `disabled checked`; Sets entsprechen benannten Sichten.

### Falsch

```html
<!-- Aktionsspalte abwählbar -->
<label><input type="checkbox" checked><span>Aktionen</span></label>
<!-- Set ohne Zustand -->
<button class="km-colpicker__set km-iconbtn--on">Alle</button>
```

## Seitenregeln

Aus `docs/seitenregeln.md`: Spaltenauswahl mit Sets, Name und Aktionen immer dabei, ein Set ist gedrückt, wenn die Auswahl ihm genau entspricht; Spalten folgen den sichtbaren Zeilen; Adresse und Speicher; Logo setzt zurück, die Spaltenauswahl bleibt; ausgewählt bleibt ausgewählt, auch unter der Maus; Bedienzeilen gleich hoch.

Entscheidungen: 19 (Standard-Tabelle), 22 (Filter, Adresse, Verlauf), 23 (Bedienzeilen), 24 (Auswahl und Menüs).

## Vergleich mit anderen Design-Systemen

| System | Name | Besonderheit | Quelle |
|---|---|---|---|
| Carbon | Data table, column settings | ungeprüft | – |

## Verwandte Bausteine

`km-table`, `km-selectpanel`, `km-check`, `km-toolbar`, `km-iconbtn--label`, `km-button`.

## Tokens

Rollen: `--km-color-card`, `--km-color-inset`, `--km-color-border-card`, `--km-color-text`, `--km-color-text-muted`, `--km-color-text-dim`, `--km-color-accent`, `--km-color-on-accent`, `--km-shadow`, `--km-shadow-strong`, `--km-font-size-xs`, `--km-space-2xs` bis `--km-space-s`, `--km-icon-xs`.

Hart im Baustein: `z-index: 100`, Mindestbreite doppelt gesetzt (`17rem`, später `12rem`), `font-weight: 500` der Kopfzeile.

## Offene Punkte

- `min-width` steht zweimal (17rem mit Kommentar „vier Sets in einer Reihe“, später 12rem); die frühere Regel ist tot.
- Heller Schatten hängt an `:root[data-theme="light"]` statt an `data-kern-theme` (gleiches Problem wie bei `km-selectpanel`).
- Knopf nutzt zusätzlich `km-iconbtn km-iconbtn--label` (Mono), bekommt die Textschrift erst über eine spätere Regel; mit `km-button` als Auslöser wäre der Knopf einheitlich.
- `role="menu"` im Story-Markup; Zusammenführen mit `km-selectpanel` prüfen.

## Regeln

- Was: Die Spaltenauswahl `km-colpicker` blendet Spalten einer Tabelle ein und aus: Knopf „Spalten“ mit Panel aus einem Kästchen je Spalte und benannten Sets, einer Variante und einer Größe.
- Wann: Wenn eine Standard-Tabelle mehr Spalten hat, als in die Breite passen, oder wiederkehrende Sichten als Set benennbar sind; bei wenigen Spalten alle zeigen und quer scrollen, zum Filtern von Zeilen Suchfeld oder Seitenleiste.
- Wie: Hülle `km-colpicker` mit `km-colpicker__btn` (`aria-expanded`, `aria-controls`) und `km-colpicker__panel` (`role="group"` mit `aria-label`, offen mit `--open`), je Spalte ein `label` mit Kästchen und Icon, Sets als `km-colpicker__set` mit `aria-pressed`, Name und Aktionen fest mit `disabled checked`, Knopf in `km-toolbar`.
- Prüfen: Fertig ist es, wenn ein Set genau dann gedrückt ist, wenn die Auswahl ihm entspricht, der Zähler („5/9“) bei abweichender Auswahl mit `km-colpicker__btn--filter` erscheint, feste Spalten `disabled` statt nur abgeblendet sind, die Auswahl nach dem Zurücksetzen über das Logo bleibt und der Text in allen Themes mindestens 4,5:1 misst.
