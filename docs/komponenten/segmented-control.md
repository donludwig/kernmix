# Segmented Control (`km-segmented`, `km-segmented--wrap`)

Status: stabil; Variante `--wrap` neu, im Dashboard im Einsatz · Story: `docs/index.html#segmented` (Standard und umbrechend `--wrap` mit Icon, Zähler, Ein-Knopf-Gruppe), Zähler auch in `#trefferliste` · CSS: `src/km-components.css`, Abschnitt „Segmented Control“ und Regeln zu `km-segmented--wrap` · Stand: 2026-11-09

## Kurzbeschreibung

Das Segmented Control schaltet zwischen gleichrangigen Ansichten derselben Sache um, zum Beispiel Karten und Zeitlich oder die Listen über einer Projektübersicht. Es steht als zusammenhängende Knopfgruppe in einer Bedienzeile; genau ein Segment ist gewählt und gefüllt im Akzent. Jedes Segment trägt sein Icon vor dem Namen und auf Wunsch eine Anzahl dahinter. Werden es mehr Segmente, als in die Zeile passen, brechen sie mit der Variante `--wrap` in eine zweite Zeile um, statt aus dem Bereich zu laufen.

## Name und Abgrenzung

- Klasse `km-segmented`, Name „Segmented Control“ (KERN führt das Muster als Release Candidate).
- In der Oberfläche heißen die Segmente nach ihren Ansichten.
- „Reiter“ meint im System nur echte Tabs (WAI-ARIA Tabs), nicht diesen Baustein.
- Zum Baustein gehören Gruppe, Segmente, Icon, Zähler und die Umbruch-Variante.
- Nicht dazu gehört, was die Ansicht zeigt, und das Umschalten selbst (Skript der Seite).
- Keine Tabs im Sinne von WAI-ARIA: Die Segmente sind Umschalt-Knöpfe (`aria-pressed`), sie steuern kein eigenes `tabpanel`.
- Wo jedes Segment einen eigenen Inhaltsbereich zeigt und Pfeiltasten erwartet werden, wäre das Tabs-Muster richtig (KERN „Tabs“ ist laut KERN noch in Bearbeitung).
- `km-button`: löst eine Aktion aus und wählt nichts.
- Eine seltene Aktion neben den Segmenten („Neue Liste“) steht als eigene Gruppe daneben, nie als weiteres Segment.
- `km-sidebar`-Filter: Filter der Navigation, nicht Ansichten in einem Bereich.

Name entschieden: Segmented Control. Die Teile heißen Segmente.

## Einsatz

### Verwenden, wenn

- zwei bis fünf gleichrangige Ansichten derselben Daten umgeschaltet werden (`km-segmented`);
- mehr als fünf benannte Listen oder Kategorien umgeschaltet werden, deren Zahl wächst (`km-segmented--wrap`);
- die Wahl sofort wirkt.

### Nicht verwenden, wenn

- mehrere Optionen gleichzeitig gelten: Kästchen oder Auswahl mit Suche;
- Optionen ein Formularwert sind: Radios;
- ganze Seiten oder Bereiche gewechselt werden: Navigation;
- eine Aktion ausgelöst wird: `km-button`;
- Löschen oder Bearbeiten neben den Segmenten stehen soll: das gehört ins Menü „… bearbeiten“.

## Verwendung

```html
<div class="km-toolbar">
  <div class="km-segmented km-segmented--wrap" role="group" aria-label="Listen">
    <button type="button" class="km-segmented__btn" aria-pressed="true"><svg class="km-icon" aria-hidden="true">…</svg>Alle <span class="km-segmented__count">64</span></button>
    <button type="button" class="km-segmented__btn" aria-pressed="false"><svg class="km-icon" aria-hidden="true">…</svg>Quickliste <span class="km-segmented__count">6</span></button>
  </div>
  <div class="km-segmented" role="group" aria-label="Listen verwalten">
    <button type="button" class="km-segmented__btn"><svg class="km-icon" aria-hidden="true">…</svg>Neue Liste</button>
  </div>
</div>
```

## Aufbau

| Teil | Klasse | Funktion |
|---|---|---|
| Gruppe | `km-segmented` | `inline-flex`, ein gemeinsamer Rahmen `--km-color-border-section`, Fläche `--km-color-card`. |
| Segment | `km-segmented__btn` | Knopf, Trennlinie links (außer am ersten), Text `--km-font-size-xs`, gedämpft. |
| Icon | `svg.km-icon` | vor dem Namen, `aria-hidden="true"`. |
| Anzahl | `km-segmented__count` | gedämpfte Zahl hinter dem Namen; im gewählten oder deaktivierten Segment in dessen Textfarbe. |
| Umbruch | `km-segmented--wrap` | Gruppe ohne eigenen Rahmen, jedes Segment mit eigenem Rahmen, um eine Rahmenbreite überlappend (keine Doppellinie); bricht um. |

## Varianten

- **Standard** `km-segmented`: eine Zeile, zwei bis fünf Segmente.
- **Umbrechend** `km-segmented--wrap`: viele Segmente; in `km-toolbar` nimmt die Gruppe den freien Platz (`flex: 1 1 0`, Mindestbreite 12rem) und richtet sich oben aus, Knöpfe und Gruppen danach stehen rechts in Höhe der ersten Segmentzeile.
- **Ein-Knopf-Gruppe**: `km-segmented` mit einem Knopf für eine seltene Aktion neben umbrechenden Segmenten, so hoch wie ein Segment.

## Größen

- Eine Größe.
- Gemessen (headless Chrome, Kobalt dunkel): Segmentgruppe 33,00 px hoch, gleich wie `km-button`; in `km-toolbar` gleich hoch wie Suchfeld und `km-iconbtn`.

## Zustände

| Zustand | Auslöser | Darstellung | Tokens |
|---|---|---|---|
| Ruhe | `aria-pressed="false"` | gedämpfter Text auf Kartenfläche | `--km-color-text-muted`, `--km-color-card` |
| Hover | `:hover` | Text voll, 8 % Akzent getönt | `--km-color-text`, `--km-color-accent` |
| Gewählt | `aria-pressed="true"` | Fläche Akzent, Text `--km-color-on-accent`, Schriftstärke unverändert | `--km-color-accent`, `--km-color-on-accent` |
| Fokus | `:focus-visible` | Doppelring außen, Segment über die Nachbarn gehoben (`z-index: 1`) | `--km-color-focus` |
| Deaktiviert | `disabled` | abgeblendet, kein Zeiger | `--km-opacity-disabled` |
| Leer | Anzahl 0 | kein eigener Zustand; leere Kategorien werden deaktiviert (Story `#trefferliste`) | – |
| Umgebrochen | `--wrap`, zu wenig Breite | zweite Segmentzeile, Ränder überlappend | `--km-border-width` |

## Verhalten

- Genau ein Segment gedrückt; die Seite setzt `aria-pressed` und zeigt die Ansicht.
- Das gewählte Segment behält seine Schriftstärke; nichts wird breiter, nichts springt (Entscheidung 36).
- Wahl in Adresse und Speicher, wenn die Ansicht teilbar sein soll (Seitenregeln „Adresse und Speicher“).

## Text und Wording

- Ein bis zwei Wörter je Segment, höchstens etwa 20 Zeichen; Satzschreibweise.
- Icon vor dem Namen, Anzahl dahinter.
- Bezeichnungen schließen sich gegenseitig aus.

## Barrierefreiheit

- Rolle: Gruppe `role="group"` mit `aria-label`; Segmente: native `button` mit `aria-pressed` (WAI-ARIA APG, Toggle Button).
- Die Beschriftung ändert sich beim Wählen nicht.
- Tastatur: Jedes Segment ist ein eigener Tab-Halt, Enter und Leertaste wählen.
- Pfeiltasten sind nicht vorgesehen; bei vielen Segmenten (`--wrap`) wird die Tab-Folge lang.
- Eine `role="toolbar"` mit Pfeiltasten (APG Toolbar) wäre die Alternative.
- Fokus: Doppelring außen, über die Nachbarn gehoben.
- Gewählter Zustand nicht nur über Farbe: Füllung und Schriftstärke; `aria-pressed` für Screenreader.
- Kontrast (gerechnet):

| Paar | Kobalt dunkel | Kobalt hell | Papier dunkel | Papier hell |
|---|---|---|---|---|
| Ruhe: `--km-color-text-muted` auf `--km-color-card` | 7,89 | 7,85 | 8,57 | 7,79 |
| Gewählt: `--km-color-on-accent` auf `--km-color-accent` | 9,13 | 6,69 | 8,68 | 8,38 |
| Hover: `--km-color-text` auf 8 % Akzent | 12,17 | 14,10 | 11,13 | 15,42 |
| Rahmen `--km-color-border-section` auf `--km-color-card` | 1,92 | 1,74 | 1,77 | 1,63 |

Der Rahmen liegt unter 3:1; das gewählte Segment ist über die Füllung klar erkennbar, die Grenzen der übrigen Segmente nur schwach.

- Schmal (390 px): Standard-Segmente laufen nicht um und können überlaufen; dort `--wrap` nutzen.

## Beispiele

### Richtig

```html
<div class="km-segmented" role="group" aria-label="Ansicht"><button type="button" class="km-segmented__btn" aria-pressed="true">Karten</button><button type="button" class="km-segmented__btn" aria-pressed="false">Zeitlich</button></div>
```

### Falsch

```html
<div class="km-segmented">…12 Segmente ohne --wrap…</div>                      <!-- läuft aus dem Bereich -->
<div class="km-segmented"><button class="km-segmented__btn">Alle</button>…<button class="km-segmented__btn">Löschen</button></div>  <!-- Aktion als Segment -->
<div class="km-segmented" role="tablist">…</div>                                <!-- Tabs-Rolle ohne Tabpanel und Pfeiltasten -->
```

## Seitenregeln

Aus `docs/seitenregeln.md`: viele Segmente brechen um (`km-segmented--wrap`), Icon vor dem Namen, Anzahl dahinter; seltene Aktionen als eigener Knopf in eigener Gruppe, so hoch wie ein Segment; Bearbeiten im Menü, Löschen nie neben den Segmenten; Bedienzeilen gleich hoch in `km-toolbar`; nichts springt beim Wählen (für die Seitenleiste ausdrücklich, siehe offene Punkte).

## Vergleich mit anderen Design-Systemen

| System | Name | Besonderheit | Quelle |
|---|---|---|---|
| Primer (GitHub) | SegmentedControl | „pick one choice from a linear set of closely related choices, and immediately apply that selection“; Icon vor dem Text oder nur Icon; Zähler per `count`; bei wenig Platz `variant` mit `hideLabels` oder `dropdown` je Breite (schmal, normal, breit), kein Umbruch | primer.style/product/components/segmented-control |
| GOV.UK Design System | Tabs | für klar benannte Abschnitte, die man nicht gleichzeitig sehen muss; warnt, dass viele oder lange Reiter über mehrere Zeilen umbrechen und dann der Bezug zum aktiven Reiter schwer erkennbar ist; schmal als eine Seite mit Inhaltsverzeichnis | design-system.service.gov.uk/components/tabs |
| WAI-ARIA APG | Tabs Pattern | `tablist`, `tab`, `tabpanel`, `aria-selected`; ein Tab-Halt für die ganze Liste, Pfeiltasten zwischen den Tabs | w3.org/WAI/ARIA/apg/patterns/tabs |
| KERN 2.8.2 | Tabs | „derzeit noch in Bearbeitung“; der KERN-Vorschlag für ein Segmented Control ist Issue 1141 (Bezug laut Code-Kommentar, Inhalt ungeprüft) | kern-ux.de/komponenten/tabs |

- `km-segmented--wrap` geht bewusst den Weg, vor dem GOV.UK für Tabs warnt (Umbruch); bei Umschalt-Knöpfen ohne angehängtes Panel wiegt der Einwand geringer, weil das gewählte Segment gefüllt ist.
- Primer löst Platzmangel mit Ausblenden der Texte oder einem Dropdown.

## Verwandte Bausteine

`km-toolbar`, `km-button`, `km-selectpanel`, `km-results__tabs` (Segmented Control der Suche), `km-colpicker__set` (Spalten-Sets).

## Tokens

Rollen: `--km-color-border-section`, `--km-color-card`, `--km-color-text-muted`, `--km-color-text`, `--km-color-text-dim`, `--km-color-accent`, `--km-color-on-accent`, `--km-color-focus`, `--km-font-size-xs`, `--km-space-xs`, `--km-space-s`, `--km-border-width`, `--km-opacity-disabled`.

- Komponenten-Tokens: keine.
- Hart im Baustein: Tönung `8%` im Hover, `line-height: normal`, Mindestbreite `12rem` der umbrechenden Gruppe in der Bedienzeile, `z-index: 1` im Fokus.

## Offene Punkte

- Tastatur bei vielen Segmenten: Pfeiltasten (APG Toolbar) prüfen.
- Doppelte Fokus-Regel (`km-segmented__btn:focus-visible` steht zweimal im CSS).

## Regeln

- Was: Ein Segmented Control ist eine Knopfgruppe für gleichrangige Ansichten derselben Sache; genau ein Segment ist gewählt; ab sechs Segmenten oder wachsender Zahl `km-segmented--wrap`.
- Wann: Nur, wenn genau eine Ansicht gilt und die Wahl sofort wirkt; Mehrfachwahl, Formularwerte, Seitenwechsel und Aktionen bekommen ihren eigenen Baustein.
- Wie: Gruppe mit `role="group"` und `aria-label`, Segmente als `button` mit `aria-pressed`, Icon vor dem Namen, Anzahl dahinter; seltene Aktionen als eigene Gruppe daneben, alles in `km-toolbar`.
- Prüfen: Fertig ist es, wenn jeder Zustand der Tabelle erreichbar ist, Text in allen Themes mindestens 4,5:1 misst, das gewählte Segment nicht breiter wird und bei 390 px nichts waagerecht scrollt.
