# Knopf mit Text (`km-button`)

Status: neu, in Dashboard und Lagebild im Einsatz · Story: `docs/index.html#knopf` · CSS: `src/km-components.css`, Abschnitt „Knopf mit Text (km-button)“ · Stand: 2026-11-09

## Kurzbeschreibung

Der Knopf mit Text löst eine Aktion aus, die seine Beschriftung benennt: „Neue Liste“, „Liste bearbeiten“, „Projekte“. Er trägt ein Icon vor dem Text, auf Wunsch eine Anzahl und einen Pfeil, wenn er ein Menü oder eine Auswahl öffnet. Er ist ein ruhiger Werkzeugknopf ohne gefüllte Fläche und steht in Bedienzeilen neben Suchfeld, Segmenten und Auswahl, alle gleich hoch. Für Aktionen ohne Text gibt es den Icon-Knopf, für die eine Hauptaktion einer Seite den KERN-Button.

## Name und Abgrenzung

- Klasse `km-button`; in der Oberfläche heißt er nach seiner Aktion.
- Zum Baustein gehören Rahmen, Icon, Text, Anzahl (`km-button__count`) und Menü-Pfeil.
- Nicht dazu gehört, was er öffnet (Auswahl mit Suche `km-selectpanel`, Dialog).
- `km-iconbtn`: Knopf nur mit Icon, quadratisch (`--km-control-height`), für Zeilenaktionen und Kopfzeile.
- `km-iconbtn--label`: älterer Knopf mit Text in Mono-Schrift (Tabellenzeile, Kopfzeile der Seite). Überschneidet sich mit `km-button`; siehe offene Punkte.
- `kern-btn` (KERN): Primary, Secondary, Tertiary in fünf Größen von 32 bis 64 px.
- Für die Hauptaktion einer Seite und für Formulare und Dialoge (`kern-btn` mit `km-btn--danger` für das zweite Bestätigen beim Löschen).
- `km-segmented`: wählt eine Ansicht aus; der Knopf wählt nichts aus.
- Eine seltene Aktion neben Segmenten („Neue Liste“) ist ein Knopf in eigener Gruppe, nicht ein weiteres Segment.

## Einsatz

### Verwenden, wenn

- eine Aktion in einer Bedienzeile über einer Liste oder Tabelle steht (anlegen, bearbeiten, Auswahl öffnen);
- eine seltene Aktion nicht als großes Eingabefeld erscheinen soll: Knopf, der ein Menü öffnet, in dem der Name eingegeben wird;
- die Aktion ein Menü oder Panel öffnet und die Anzahl der gewählten Dinge zeigen soll.

### Nicht verwenden, wenn

- die Aktion die Hauptaktion der Seite oder eines Formulars ist: `kern-btn--primary`;
- es ein Wechsel zu einer anderen Seite ist: Link;
- eine Ansicht gewählt wird: `km-segmented`;
- in einer Tabellenzeile: dort nur `km-iconbtn` in der Aktionsspalte;
- der Text nur ein Icon ersetzen soll, das allein verständlich ist: `km-iconbtn` mit `aria-label`.

## Verwendung

```html
<div class="km-toolbar">
  <button type="button" class="km-button"><svg class="km-icon" aria-hidden="true">…</svg>Neue Liste</button>
  <button type="button" class="km-button" aria-haspopup="dialog" aria-expanded="false" aria-controls="panel-projekte">
    <svg class="km-icon" aria-hidden="true">…</svg>Projekte<span class="km-button__count">6</span><svg class="km-icon" aria-hidden="true"><!-- chevron-down --></svg>
  </button>
</div>
```

## Aufbau

| Teil | Klasse | Funktion |
|---|---|---|
| Knopf | `km-button` | Rahmen `--km-color-border-section`, Fläche `--km-color-card`, Text `--km-color-text-muted` in `--km-font-size-xs`, Textschrift wie das Segmented Control, bricht nicht um. |
| Icon vorn | `svg.km-icon` | Lucide, `aria-hidden="true"`; Abstand `--km-space-xs`. |
| Text | Textknoten | Benennt die Aktion. |
| Anzahl | `km-button__count` | gleich breite Ziffern, gedämpft. |
| Menü-Pfeil | `svg.km-icon` (chevron-down) am Ende | nur, wenn der Knopf etwas öffnet. |

## Varianten

Eine Variante. Es gibt keinen gefüllten, keinen Gefahr- und keinen kleinen `km-button`; dafür stehen `kern-btn` und `km-iconbtn` bereit.

## Größen

- Eine Größe.
- In einer `km-toolbar` gestreckt auf die Höhe der höchsten Nachbarn.
- Gemessen (headless Chrome, Kobalt dunkel): Suchfeld, Segmented Control, `km-button` und `km-iconbtn` in `km-toolbar` je 33,00 px.
- Außerhalb der Zeile: `km-button` 33,00 px, Segmented Control 33,00 px, Suchfeld 32,80 px, `km-iconbtn` 25,59 px.
- Ohne `km-toolbar` sind die Höhen also nicht gleich.

## Zustände

| Zustand | Auslöser | Darstellung | Tokens |
|---|---|---|---|
| Ruhe | – | Rahmen, Kartenfläche, gedämpfter Text | `--km-color-border-section`, `--km-color-card`, `--km-color-text-muted` |
| Hover | `:hover` | Text voll, Fläche 8 % Akzent getönt | `--km-color-text`, `--km-color-accent` |
| Fokus | `:focus-visible` | Doppelring außen | `--km-color-focus`, `--km-border-width-strong`, `--km-focus-offset` |
| Menü offen | `aria-expanded="true"` | Text voll, Rahmen im Akzent | `--km-color-accent` |
| Gedrückt (Umschalter) | `aria-pressed` | nicht definiert | offen |
| Deaktiviert | `disabled` | nicht definiert; der gemeinsame Deaktiviert-Stil (`--km-opacity-disabled`) schließt `km-button` nicht ein | offen |
| Laden | – | nicht definiert | offen |

## Verhalten

- Natives `<button type="button">`. Öffnet der Knopf ein Panel, setzt die Seite `aria-expanded` und gibt beim Schließen den Fokus an den Knopf zurück.
- Die Anzahl aktualisiert die Seite.

## Text und Wording

- Verb oder Gegenstand der Aktion, ein bis drei Wörter, höchstens etwa 24 Zeichen („Liste bearbeiten“, „Neue Liste“).
- Satzschreibweise, keine Versalien.
- Öffnet der Knopf etwas: Gegenstand als Text („Projekte“), Pfeil am Ende, Anzahl der gewählten Dinge dahinter.

## Barrierefreiheit

- Rolle: natives `button`.
- Öffnet er ein Panel: `aria-haspopup="dialog"` (oder `"listbox"`, je nach Inhalt), `aria-expanded`, `aria-controls`.
- Icons `aria-hidden="true"`.
- Tastatur: Enter und Leertaste lösen aus (nativ). Nach dem Öffnen geht der Fokus in das Geöffnete, nach Esc zurück auf den Knopf.
- Fokus: Ring außen in `--km-color-focus`.
- Ein Umschalter (`aria-pressed`) behält seine Beschriftung in beiden Zuständen (WAI-ARIA APG, Button Pattern).
- Kontrast (gerechnet):

| Paar | Kobalt dunkel | Kobalt hell | Papier dunkel | Papier hell |
|---|---|---|---|---|
| Text `--km-color-text-muted` auf `--km-color-card` | 7,89 | 7,85 | 8,57 | 7,79 |
| Text bei Hover auf 8 % Akzent | 12,17 | 14,10 | 11,13 | 15,42 |
| Rahmen `--km-color-border-section` auf `--km-color-card` | 1,92 | 1,74 | 1,77 | 1,63 |
| Rahmen offen `--km-color-accent` auf `--km-color-card` | 8,27 | 6,69 | 8,02 | 8,09 |
| Fokusring `--km-color-focus` auf `--km-color-page` | 9,30 | 5,97 | 9,03 | 7,29 |

- Der Rahmen in Ruhe liegt unter 3:1.
- Ob WCAG 1.4.11 hier greift, hängt davon ab, ob der Rand zum Erkennen des Knopfs nötig ist; der Text allein kennzeichnet ihn kaum als Knopf, weil die Fläche der Kartenfläche gleicht.
- Siehe offene Punkte.

## Beispiele

### Richtig

```html
<div class="km-toolbar"><div class="km-segmented km-segmented--wrap" role="group" aria-label="Listen">…</div><button type="button" class="km-button"><svg class="km-icon" aria-hidden="true">…</svg>Neue Liste</button></div>
```

### Falsch

```html
<button class="km-iconbtn km-iconbtn--label">Neue Liste</button>        <!-- Text-Knopf in Mono über einer Liste -->
<button class="km-segmented__btn">Neue Liste</button>                    <!-- Aktion als Segment -->
<button class="km-button" style="height:30px">…</button>                 <!-- eigene Höhe statt km-toolbar -->
```

## Seitenregeln

Aus `docs/seitenregeln.md`: Bedienzeilen gleich hoch, immer in `km-toolbar`, nie eigene Höhen; seltene Aktionen als Knopf, nicht als großes Feld, in eigener Gruppe neben den Segmenten und so hoch wie ein Segment (`.km-toolbar > .km-segmented--wrap ~ .km-button` richtet ihn oben aus); Knöpfe in der Kopfzeile gleich hoch (`km-iconbtn--label`); Befehlsknöpfe kopieren den Befehl, sie führen nichts aus; nur Lucide-Icons; Knöpfe nie unterstrichen.

## Vergleich mit anderen Design-Systemen

| System | Name | Besonderheit | Quelle |
|---|---|---|---|
| KERN 2.8.2 | Button (`kern-btn`) | Primary, Secondary, Tertiary; ein Primary je Seite; fünf Größen 32 bis 64 px; Icon links, rechts möglich; Icon-only braucht `kern-sr-only`-Text; Deaktiviert nur, wenn es Verständnis oder Konsistenz fördert | kern-ux.de/komponenten/button |
| GOV.UK Design System | Button | Default, Secondary, Start, Warning, Inverse; Text in Satzschreibweise, beschreibt die Aktion; deaktivierte Knöpfe möglichst vermeiden; Start-Knopf als Link, wenn er keine Daten sendet | design-system.service.gov.uk/components/button |
| WAI-ARIA APG | Button Pattern | Enter und Leertaste lösen aus; Umschalter mit `aria-pressed`, Beschriftung ändert sich nicht; Menü-Knopf mit `aria-haspopup` | w3.org/WAI/ARIA/apg/patterns/button |

`km-button` entspricht am ehesten einem Secondary- bzw. Tertiary-Knopf in kleiner Größe; eine eigene Hierarchie hat er nicht.

## Verwandte Bausteine

`km-iconbtn`, `km-iconbtn--label`, `km-toolbar`, `km-segmented`, `km-selectpanel`, `kern-btn`, `km-btn--danger`.

## Tokens

Rollen: `--km-color-border-section`, `--km-color-card`, `--km-color-text-muted`, `--km-color-text`, `--km-color-text-dim`, `--km-color-accent`, `--km-color-focus`, `--km-font-size-xs`, `--km-space-xs`, `--km-space-s`, `--km-border-width`, `--km-border-width-strong`, `--km-focus-offset`, `--km-radius`, `--km-icon-xs`.

Komponenten-Tokens: keine. Hart im Baustein: Tönung `8%` im Hover (auch in `km-segmented__btn:hover` und `km-sidebar__item:hover`), `line-height: normal`.

## Offene Punkte

- Deaktiviert-Zustand fehlt (`.km-button:disabled`); der gemeinsame Deaktiviert-Stil sollte ihn einschließen.
- `km-button` und `km-iconbtn--label` sind zwei Knöpfe mit Text (Textschrift bzw. Mono). Zusammenführen oder Abgrenzung festlegen.
- Rahmen in Ruhe unter 3:1 in allen Themes: Entscheidung, ob `--km-color-border-input` (≥ 3:1) als Rahmen gilt.
- Gefüllte Hauptaktion im Werkzeug-Stil gibt es nicht; heute `kern-btn--primary`.

## Regeln

- Was: `km-button` ist der ruhige Werkzeugknopf mit Text für eine Aktion, die seine Beschriftung benennt, mit Icon vorn, auf Wunsch Anzahl (`km-button__count`) und Menü-Pfeil; es gibt nur eine Variante und eine Größe.
- Wann: Für eine Aktion in einer Bedienzeile über einer Liste oder Tabelle oder einen Knopf, der ein Menü oder Panel öffnet; die Hauptaktion einer Seite ist `kern-btn--primary`, ein Seitenwechsel ein Link, eine Ansichtswahl `km-segmented`, eine Tabellenzeile `km-iconbtn` und ein Icon allein `km-iconbtn` mit `aria-label`.
- Wie: Natives `<button type="button" class="km-button">` mit `svg.km-icon` (`aria-hidden="true"`) vor dem Text, Beschriftung als Verb oder Gegenstand in Satzschreibweise mit ein bis drei Wörtern, immer in `km-toolbar` ohne eigene Höhe; öffnet er ein Panel, kommen `aria-haspopup`, `aria-expanded` und `aria-controls` dazu, der Fokus geht ins Geöffnete und nach Esc zurück auf den Knopf.
- Prüfen: Fertig ist es, wenn Ruhe, Hover, Fokus und Menü offen der Tabelle erreichbar sind, der Text in allen Themes mindestens 4,5:1 misst, der Fokusring sichtbar ist und der Knopf in `km-toolbar` so hoch ist wie Suchfeld und Segmented Control; Deaktiviert, Gedrückt und Laden sind nicht definiert.
