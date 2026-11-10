# Prüfkarte, Feld und Begriff (`km-criterion`, `km-field`, `km-term`)

Status: Entwurf · Story: `docs/index.html#pruefkarte` · CSS: `src/km-components.css`, Abschnitt „Fragebogen-Bausteine“ · Stand: 2026-11-09

## Kurzbeschreibung

Die Prüfkarte zeigt ein Kriterium eines Fragebogens: Nummer, Titel und Punkte, wo man nachsieht, Teilfragen mit Antwort-Knöpfen oder eine Auswahl, Beleg und Notiz als Felder, Verweise, einen Hinweis, wenn Punkte noch nicht zählen, einen Vorschlag und den Hintergrund. Die Kante links zeigt den Stand. Das Feld ist die Eingabe mit Beschriftung. Der Begriff erklärt ein Fachwort beim Überfahren oder mit dem Fokus.

## Name und Abgrenzung

- `km-criterion` heißt in der Oberfläche „Prüfkarte“, `km-field` „Feld“, `km-term` „Begriff“.
- Abgrenzung: `km-card` ist die allgemeine Karte; die Prüfkarte hat feste Teile für Fragen und Felder und eine Zustandskante.
- KERN-Eingaben (`kern-form-input`) sind für Formulare in KERN-Größe (48 px hoch, einzeilig); `km-field` passt zu dichten Werkzeugseiten und kann mehrzeilig wachsen.
- Inhalt, Punkte, Speichern und gleiche Höhe der Felder liefert die Seite.

## Einsatz

### Verwenden, wenn

- ein Kriterium aus mehreren Teilfragen mit Beleg geprüft wird (Reifegrad, Abnahme, Prüfliste);
- Begriffe im Fließtext ohne Seitenwechsel erklärt werden sollen (`km-term`).

### Nicht verwenden, wenn

- nur ein Text steht (dann `km-card` oder `km-callout`).

## Verwendung

```html
<article class="km-criterion km-criterion--partial">
  <div class="km-criterion__head"><h3 class="km-criterion__title"><span class="km-criterion__nr">A1</span> Titel</h3><span class="km-criterion__points">4<small> / 8</small></span></div>
  <p class="km-criterion__where"><strong>Wo nachsehen:</strong> problem.md</p>
  <div class="km-criterion__questions"><fieldset class="km-criterion__q"><legend>Teilfrage<span class="km-criterion__pkt">· 2 Pkt.</span></legend> km-answer </fieldset></div>
  <div class="km-criterion__fields"><label class="km-field"><span class="km-field__label">Beleg</span><textarea class="km-field__control"></textarea></label> … </div>
  <ul class="km-criterion__refs"></ul><p class="km-criterion__missing"></p>
  <details class="km-criterion__more"><summary>Hintergrund</summary> km-cards </details>
</article>
```

## Aufbau

| Teil | Klasse | Funktion |
|---|---|---|
| Karte | `km-criterion` | Fläche Karte, Kante links als Innenschatten |
| Kopf | `__head`, `__title`, `__nr`, `__points` | Titel in der Überschriftenschrift, Nummer im Akzent, Punkte rechts mit gleich breiten Ziffern |
| Hinweis | `__where`, `__text` | Arbeitstext gedämpft, Maß breit |
| Teilfragen | `__questions`, `__q`, `__pkt` | Zeile mit Linie oben, Frage links, Antwort-Knöpfe rechts |
| Auswahl | `__options` | Liste mit `km-check` (auch als Radio), Kästchen mittig zur ersten Zeile |
| Felder | `__fields`, `km-field`, `__label`, `__control`, `__hint` | Raster, ab 16rem nebeneinander; `km-field--inline` legt die Beschriftung neben die Auswahl |
| Verweise | `__refs` | Kürzel fett, Klartext gedämpft, leer ausgeblendet |
| Fehlhinweis | `__missing` | Fehlerfarbe, leer ausgeblendet |
| Vorschlag | `__proposal` | gestrichelte Fläche mit Titel in Versalien und Knopf |
| Hintergrund | `__more`, `__more--open` | aufklappbar; `--open` blendet den Aufklapp-Knopf aus |
| Begriff | `km-term`, `__tip`, `--closed` | gepunktet unterstrichen, Erklärung schwebt darunter |

## Zustände

| Zustand | Auslöser | Darstellung | Tokens |
|---|---|---|---|
| offen | – | Kante Rand | `--km-color-border-section` |
| teilweise | `km-criterion--partial` | Kante gelb | `--km-color-feedback-warning` |
| fertig | `km-criterion--done` | Kante grün | `--km-color-feedback-success` |
| gesperrt | `km-criterion--blocked` | Kante rot, Fläche leicht getönt | `--km-color-feedback-danger`, `-background` |
| Feld Hover, Fokus | `:hover`, `:focus-visible` | Rand kräftiger, Fokusrahmen | `--km-color-text-muted`, `--km-color-focus` |
| Begriff offen | `:hover`, `:focus` | Erklärung sichtbar | `--km-color-text` als Fläche |
| Begriff geschlossen | Esc (`km-term--closed`, setzt kmPopup) | Erklärung aus, bis Maus oder Fokus gehen | – |

## Verhalten

- Die Seite rechnet Punkte und setzt die Zustandsklasse, füllt Verweise und Fehlhinweis und gleicht die Höhe nebeneinanderstehender Felder an (größte `scrollHeight`).
- Mit `km-criterion__more--open` und `open` zeigt eine Leseansicht den Hintergrund ohne Aufklappen; beim Drucken ist er immer offen.
- `kmPopup` schließt die Erklärung eines Begriffs mit Esc.

## Text und Wording

Titel mit Nummer; Punkte als „4 / 8“; Fehlhinweis als ganzer Satz („6 Punkte zählen erst mit Beleg.“).

## Barrierefreiheit

- `article` mit `aria-labelledby` auf den Titel; Teilfragen als `fieldset` mit `legend`; Felder mit sichtbarer Beschriftung im `label`.
- Fehlhinweis mit `aria-live="polite"`.
- Begriff: `tabindex="0"`, Erklärung `role="tooltip"`, sichtbar mit Fokus, Esc schließt (WCAG 1.4.13).
- KERN setzt an `[tabindex]` den Fokusrahmen auf 0; das Kit setzt ihn für alle km-Elemente mit `tabindex` wieder (seit 0.10.0).
- Kontrast Feldrand auf der Karte: Papier hell 6,23, dunkel 5,78; Kobalt hell 6,05, dunkel 6,25 (gemessen).
- 390 px: Felder untereinander, Kopf bricht um, keine waagerechte Scrollleiste.

## Seitenregeln

Farbkanten als Innenschatten; Kachel und Nummer mittig zur ersten Zeile; Doku nicht aufklappbar (Hintergrund in Leseansicht offen); Bedienzeilen gleich hoch (`km-toolbar`).

## Vergleich mit anderen Design-Systemen

| System | Name | Besonderheit | Quelle |
|---|---|---|---|
| Primer | Tooltip | Erklärung bei Hover und Fokus | ungeprüft |

## Verwandte Bausteine

Antwort-Knöpfe (`km-answer`), Score (`km-score`), Karte (`km-card`), Hinweiskasten (`km-callout`).

## Tokens

`--km-component-field-textarea-min-height`, `--km-component-term-tip-width`, `--km-border-width-accent`, `--km-color-feedback-*`, `--km-color-border-input`, `--km-typography-font-size-heading-medium`, `--km-font-display`.

## Offene Punkte

- Die gleiche Höhe der Felder setzt die Seite per Skript; mit `field-sizing: content` ginge es ohne, sobald Firefox es kann.

## Regeln

- Was: Die Prüfkarte `km-criterion` zeigt ein Kriterium eines Fragebogens mit Kopf aus Nummer, Titel und Punkten, Teilfragen, Feldern `km-field`, Verweisen, Fehlhinweis, Vorschlag und Hintergrund, die Kante links zeigt den Stand (offen, `--partial`, `--done`, `--blocked`); `km-term` erklärt einen Begriff bei Hover oder Fokus.
- Wann: Wenn ein Kriterium aus mehreren Teilfragen mit Beleg geprüft wird oder Begriffe im Fließtext ohne Seitenwechsel erklärt werden sollen; steht nur ein Text, nimm `km-card` oder `km-callout`.
- Wie: `article.km-criterion` mit `aria-labelledby` auf den Titel, Teilfragen als `fieldset` mit `legend`, Felder als `label.km-field` mit sichtbarer Beschriftung, Punkte als „4 / 8“, Fehlhinweis als ganzer Satz mit `aria-live="polite"`, Begriff mit `tabindex="0"` und Erklärung `role="tooltip"`; Punkte, Zustandsklasse und Feldhöhe setzt die Seite.
- Prüfen: Fertig ist es, wenn jeder Zustand der Tabelle erreichbar ist, die Erklärung eines Begriffs mit Fokus sichtbar ist und mit Esc schließt, der Feldrand in allen Themes mindestens 3:1 misst und bei 390 px die Felder untereinander stehen, der Kopf umbricht und nichts waagerecht scrollt.
