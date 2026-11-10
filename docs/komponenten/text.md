# Hinweis, Fließtext und Textlinks (`km-note`, `km-prose`, `km-link`, `km-details`)

Status: stabil, in Dashboard und Lagebild im Einsatz · Story: `docs/index.html#gruppe` (Hinweis), `#fliesstext`, `#textlinks`, `#teilstuecke` (`km-suffix`) · CSS: `src/km-components.css`, Abschnitte „Zwischenüberschrift in einem Bereich“ (Hinweis), „Fließtext und Kartenfußnote“, „Textlinks“, „Zusatz hinter einem Namen“ · Stand: 2026-11-09

## Kurzbeschreibung

Diese Bausteine setzen Text in Werkzeugseiten. Der Hinweis `km-note` ist ein ruhiger Absatz in einem Bereich, etwa eine Erklärung unter einer Tabelle; als erstes Element im Bereich wird er zur Einleitung in Lesegröße. `km-prose` setzt einen Fließtext-Block mit Zwischenüberschrift, Absätzen und Strichliste. `km-link` ist der Link im Fließtext, gepunktet unterstrichen, mit Varianten für Projekte, Dateien und externe Ziele. `km-details__body` zeigt aufgeklappten Detailtext mit Linie links, `km-suffix` einen gedämpften Zusatz hinter einem Namen.

## Name und Abgrenzung

- `km-note` (Hinweis), `km-prose` (Fließtext), `km-link` mit `--projekt`, `--datei`, `--extern`, `km-details__body`, `km-suffix`.
- Nicht dazu: Warnungen und Fehlermeldungen mit Wirkung (KERN „Alert“), Kartenfußnote `km-card__note` (siehe `karte.md`), Verweis-Chips `km-chip`.
- `km-note` ist kein Warnkasten: keine Fläche, kein Icon, keine Farbe.
- Was Nutzer\*innen sehen müssen, gehört nach oben auf die Seite (Entscheidung 28) bzw. in ein KERN-Alert.

## Einsatz

### Verwenden, wenn

- ein Bereich oder eine Tabelle einen Satz Erklärung braucht (`km-note`);
- längerer beschreibender Text in einer Karte steht (`km-prose`);
- im Text auf ein Projekt, eine Datei oder eine externe Seite verwiesen wird (`km-link`).

### Nicht verwenden, wenn

- die Information kritisch ist: oben auf der Seite, KERN-Alert;
- Verweise gereiht ohne Satz stehen: `km-chips`;
- Bezeichnung und Wert gepaart werden: `km-deflist`.

## Verwendung

```html
<div class="km-section__body">
  <p class="km-note">Einleitung: was dieser Bereich zeigt.</p>
  …
  <div class="km-table-wrap">…</div>
  <p class="km-note">Global = gilt in allen Projekten, Projekt = nur in einem.</p>
</div>
<div class="km-prose"><h3>Worum es geht</h3><p>Fallstudien liegen in <a class="km-link km-link--datei km-link--extern" href="…">entscheidungen.md</a>.</p><ul><li>Erster Punkt</li></ul></div>
<details><summary>Details</summary><div class="km-details__body">Ausführlicher Text.</div></details>
```

## Aufbau

| Teil | Klasse | Funktion |
|---|---|---|
| Hinweis | `km-note` | `--km-font-size-s`, gedämpft, höchstens 78ch; Abstand `--km-space-block` nach oben, wenn etwas davor steht. |
| Einleitung | `.km-section__body > .km-note:first-child` | näher am Titel, `--km-font-size-m`, bis 90ch; gleich wie `km-section__lead`. |
| Fließtext | `km-prose` | Linie und Abstand oben, außer als erstes Element; `h3` kräftig, Absätze und Listen in `--km-font-size-xs`, Zeilenabstand 1,7; Liste mit Geviertstrich. |
| Textlink | `km-link` | Akzent, gepunktet unterstrichen (55 % Deckkraft der Linie), Hover durchgezogen; besucht gleiche Farbe. |
| Projekt-Link | `km-link--projekt` | etwas kräftiger (`--km-font-weight-medium`). |
| Datei-Link | `km-link--datei` | bricht nicht um. |
| Extern | `km-link--extern` | Lucide `arrow-up-right` als Maske davor. |
| Details | `details .km-details__body` | Linie links, gedämpfter Text. |
| Zusatz | `km-suffix` | gedämpft, normaler Schnitt, hinter einem Namen. |

## Varianten

Siehe Aufbau; `--km-link-color` setzt bei Bedarf eine eigene Linkfarbe (nie je Kunde).

## Größen

Hinweis `s`, Einleitung `m`, Fließtext `xs`.

## Zustände

| Zustand | Auslöser | Darstellung | Tokens |
|---|---|---|---|
| Link Ruhe | – | Akzent, gepunktet | `--km-color-accent` |
| Link Hover | `:hover` | Linie durchgezogen, volle Deckkraft | – |
| Link besucht | `:visited` | unverändert | – |
| Link Fokus | `:focus-visible` | Ring außen | `--km-color-focus` |
| Details offen | `details[open]` | Text mit Linie sichtbar | `--km-color-border-card` |

## Verhalten

Kein Skript. Externe Links öffnet die Seite wie jeder Link; ein neues Fenster nur mit Hinweis im Text.

## Text und Wording

- Hinweis: ein bis zwei Sätze, Aussage zuerst; keine Wiederholung des Titels.
- Linktext nennt das Ziel („entscheidungen.md“, „Changelog“), nie „hier“.

## Barrierefreiheit

- Links sind am Unterstrich erkennbar, nicht nur an der Farbe (WCAG 1.4.1).
- Externer Pfeil ist dekorativ; ob ein Link extern ist, sollte der Text oder die Adresse zeigen.
- `km-prose`-Listen sind echte `ul`; der Strich ist ein CSS-Inhalt (`\2014`).
- Kontrast (gerechnet):

| Paar | Kobalt dunkel | Kobalt hell | Papier dunkel | Papier hell |
|---|---|---|---|---|
| Hinweis `--km-color-text-muted` auf `--km-color-section` | 8,41 | 6,69 | 9,27 | 7,32 |
| Fließtext `--km-color-text-muted` auf `--km-color-card` | 7,89 | 7,85 | 8,57 | 7,79 |
| Link `--km-color-accent` auf `--km-color-card` | 8,27 | 6,69 | 8,02 | 8,09 |
| Link `--km-color-accent` auf `--km-color-section` | 8,82 | 5,70 | 8,68 | 7,61 |
| Zusatz `--km-color-text-dim` auf `--km-color-card` | 6,25 | 6,05 | 5,78 | 6,23 |

## Beispiele

### Richtig

```html
<div class="km-table-wrap">…</div>
<p class="km-note">Zahlen ohne Unterprojekte.</p>
```

### Falsch

```html
<!-- Hinweis als Warnkasten umgebaut -->
<p class="km-note" style="background:#fee;border:1px solid red">Achtung: Backup fehlt!</p>
<!-- Link in Kundenfarbe -->
<a class="km-link" style="color:#d97757">…</a>
<!-- Pfeil als Zeichen -->
<a class="km-link">↗ Seite</a>
```

Warum: Kritisches zuerst und mit Alert (Entscheidung 28), Farbe nur über Rollen (Entscheidung 11), keine Schriftzeichen als Icon (Entscheidung 16).

## Seitenregeln

Aus `docs/seitenregeln.md`: Hinweis unter Karte, Raster oder Tabelle mit Abstand; keine harten Farben; keine Schriftzeichen als Icon; kein Abblenden mit `opacity` für Inhalt (gedämpft über `--km-color-text-muted`/`-dim`); lange Pfade dürfen unter 40rem umbrechen.

Entscheidungen: 11, 15, 16, 28.

## Vergleich mit anderen Design-Systemen

| System | Name | Besonderheit | Quelle |
|---|---|---|---|
| GOV.UK Design System | Inset text | grenzt einen Textblock vom Umfeld ab (Zitat, Beispiel, Zusatz); sparsam; nicht für wichtige Informationen, dafür Warning text | design-system.service.gov.uk/components/inset-text |

`km-note` ist schwächer als Inset text (ohne Linie) und teilt dessen Regel: nichts Wichtiges im Hinweis.

## Verwandte Bausteine

`km-section__lead`, `km-card__note`, `km-card__more`, `km-chip`, `km-deflist`.

## Tokens

Rollen: `--km-color-text`, `--km-color-text-muted`, `--km-color-text-dim`, `--km-color-accent`, `--km-color-border-card`, `--km-font-size-xs`, `--km-font-size-s`, `--km-font-size-m`, `--km-space-block`, `--km-space-l`, `--km-underline-offset`, `--km-icon-extern`.

- Komponenten-Haken: `--km-link-color`.
- Hart im Baustein: `78ch`, `90ch`, Abstand `-1 * --km-space-s` der Einleitung, `margin-left: 0.35em` am Zusatz, `font-weight: 500/600` in `km-prose`.

## Offene Punkte

- `km-prose` setzt Absätze in 12 px (`--km-font-size-xs`) bei Zeilenabstand 1,7; für längeren Fließtext ist das klein. Prüfen, ob `s` richtig wäre.
- `km-prose h3` hat `margin-bottom`, aber keinen oberen Abstand zu vorigem Text.
- Kein Baustein für einen sichtbaren Warnhinweis im Werkzeug-Stil; heute KERN-Alert.

## Regeln

- Was: Diese Bausteine setzen Text in Werkzeugseiten: `km-note` (ruhiger Hinweis, als erstes Element im Bereich die Einleitung in Lesegröße), `km-prose` (Fließtext-Block), `km-link` mit `--projekt`, `--datei`, `--extern`, `km-details__body` (Detailtext mit Linie links) und `km-suffix` (gedämpfter Zusatz hinter einem Namen).
- Wann: `km-note` für einen Satz Erklärung unter Bereich oder Tabelle, `km-prose` für beschreibenden Text in einer Karte, `km-link` für Verweise im Text; Kritisches gehört oben auf die Seite oder in ein KERN-Alert, gereihte Verweise in `km-chips`, gepaarte Bezeichnung und Wert in `km-deflist`.
- Wie: `km-note` ohne Fläche, Icon und Farbe, ein bis zwei Sätze mit der Aussage zuerst; Linktext nennt das Ziel, nie „hier“; Icons über `km-link--extern` statt Schriftzeichen, Farben nur über Rollen oder `--km-link-color`, nie je Kunde, Dämpfen über `--km-color-text-muted` oder `-dim` statt `opacity`.
- Prüfen: Fertig ist es, wenn Links am Unterstrich und nicht nur an der Farbe erkennbar sind, der Fokus einen Ring außen zeigt, besuchte Links unverändert bleiben, die gedämpften Texte in allen Themes mindestens 4,5:1 messen und `km-prose`-Listen echte `ul` sind.
