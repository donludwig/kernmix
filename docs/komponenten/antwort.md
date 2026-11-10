# Antwort-Knöpfe (`km-answer`)

Status: Entwurf · Story: `docs/index.html#antwort` · CSS: `src/km-components.css`, Abschnitt „Fragebogen-Bausteine“ · Stand: 2026-11-09

## Kurzbeschreibung

Eine Radiogruppe als Reihe eckiger Symbol-Knöpfe für kurze, wiederkehrende Antworten: ja, nein, offen; bei Sperr-Regeln „sperrt, sperrt nicht, offen“; bei der Ampel grün, gelb, rot als farbige Quadrate. Die Knöpfe sind gleich breit, die Bedeutung steht im Tooltip und für Screenreader. Ein zweiter Klick auf die gewählte Antwort setzt sie zurück.

## Name und Abgrenzung

- Klasse `km-answer`, in der Oberfläche „Antwort“; Teile `km-answer__opt`, `__face`, `__sign`, `__reset`, `__swatch`.
- Zum Baustein gehören Form, Farben und das Zurück-Symbol. Das Zurücksetzen beim zweiten Klick und das Speichern macht das Skript der Seite.
- Abgrenzung: Segmented Control (`km-segmented`) wählt eine Ansicht und trägt Text; Antwort-Knöpfe beantworten eine Frage und tragen ein Symbol.
- KERN-Radios (`kern-form-check__radio`) bleiben für Formulare mit sichtbarem Text.

## Einsatz

### Verwenden, wenn

- viele gleichartige Fragen untereinander stehen (Prüfliste, Fragebogen) und die Antwort auf einen Blick lesbar sein soll;
- eine Antwort auch „noch offen“ sein darf und zurückgesetzt werden muss.

### Nicht verwenden, wenn

- die Optionen lange Texte haben (dann Auswahlliste mit `km-check` oder KERN-Radio);
- es mehr als drei oder vier Optionen gibt.

## Verwendung

```html
<div class="km-answer" role="radiogroup" aria-label="Antwort">
  <label class="km-answer__opt km-answer__opt--ok" title="ja"><input type="radio" name="f1" value="ja">
    <span class="km-answer__face"><svg class="km-icon km-answer__sign">…check…</svg><svg class="km-icon km-answer__reset">…rotate-ccw…</svg><span class="kern-sr-only">ja</span></span></label>
  … nein (--danger, x), offen (--warn, circle-question-mark) …
</div>
```

Ampel: statt des Symbols `<span class="km-answer__swatch" aria-hidden="true"></span>`.

## Aufbau

| Teil | Klasse | Funktion |
|---|---|---|
| Gruppe | `km-answer` | Reihe mit Abstand `--km-space-icon-text`; in einem `fieldset` ohne eigene Rolle, sonst `role="radiogroup"` mit `aria-label` |
| Option | `km-answer__opt` + `--ok`, `--danger`, `--warn` | `label` mit unsichtbarem Radio über der ganzen Fläche, Farbe nach Bedeutung |
| Fläche | `km-answer__face` | Quadrat `--km-component-answer-size` (2rem), Rand ≥ 3:1 |
| Symbol | `km-answer__sign` | Lucide check, x, circle-question-mark, octagon-x |
| Zurück | `km-answer__reset` | Lucide rotate-ccw, nur unter der Maus oder mit Fokus auf der gewählten Antwort |
| Farbfeld | `km-answer__swatch` | Ampel: Quadrat in der Farbe der Option, auch ungewählt |

## Zustände

| Zustand | Auslöser | Darstellung | Tokens |
|---|---|---|---|
| Ruhe | – | Karte, Rand gedämpft, Symbol gedämpft | `--km-color-card`, `--km-color-border-input`, `--km-color-text-dim` |
| Hover | `:hover` (ungewählt) | Rand und Symbol kräftiger | `--km-color-text-muted`, `--km-color-text` |
| Gewählt | `input:checked` | Fläche, Rand und Symbol in der Rückmeldefarbe, bleibt auch unter der Maus | `--km-color-feedback-*`, `-background` |
| Zurücksetzbar | gewählt + Hover oder Fokus | Zurück-Symbol statt Zeichen | – |
| Frisch gewählt | `km-answer__opt--fresh` (setzt die Seite beim Klick, entfernt bei `mouseleave`) | kein Zurück-Symbol, bis die Maus einmal weg war | – |
| Fokus | `input:focus-visible` | Fokusrahmen um die Fläche | `--km-color-focus`, `--km-focus-offset` |

## Verhalten

- Das CSS liefert Form, Farben und Symbolwechsel.
- Die Seite speichert die Wahl und setzt beim zweiten Klick zurück: `pointerdown` merkt sich, ob das Radio schon gewählt war; ist es so, hebt der folgende `click` die Wahl auf und löscht den gespeicherten Wert.
- Mit der Tastatur gilt dasselbe für die Leertaste.
- Startklar zeigt die Umsetzung (`Startklar/vorlage-neu.html`, Abschnitt „Zweiter Klick“).

## Text und Wording

Kurze Bedeutung in Kleinschreibung („ja“, „nein“, „offen“, „sperrt nicht“), gleich im `title` und in `kern-sr-only`.

## Barrierefreiheit

- Native Radios, gruppiert über `fieldset`/`legend` oder `role="radiogroup"` mit `aria-label`; Pfeiltasten wechseln innerhalb der Gruppe.
- Text für Screenreader in jeder Option; die Farbe ist nie die einzige Information (Symbol bzw. Text).
- Kontrast gewählt (Symbol auf Fläche) und Rand bzw. Farbfeld auf der Karte, gemessen:

| Paar | Papier hell | Papier dunkel | Kobalt hell | Kobalt dunkel |
|---|---|---|---|---|
| ja gewählt: Symbol auf Fläche | 4,59 | 6,23 | 4,99 | 5,34 |
| ja: Rand auf Karte | 5,17 | 7,51 | 6,01 | 5,55 |
| nein gewählt: Symbol auf Fläche | 5,03 | 5,94 | 4,97 | 5,34 |
| nein: Rand auf Karte | 5,99 | 6,64 | 6,01 | 5,56 |
| offen gewählt: Symbol auf Fläche | 4,79 | 6,86 | 4,52 | 5,33 |
| offen: Rand auf Karte | 5,29 | 8,31 | 5,47 | 5,55 |
| Rand ungewählt auf Karte | 6,23 | 5,78 | 6,05 | 6,25 |

- Bewegung: Übergang nur ohne `prefers-reduced-motion: reduce`. Bei 390 px stehen die Knöpfe unter dem Fragetext.

## Seitenregeln

- Eckig, Lucide-Icons statt Schriftzeichen, Ränder von Bedienelementen ≥ 3:1.
- „Ausgewählt bleibt ausgewählt, auch unter der Maus“: Zeile am Ende des Abschnitts.

## Vergleich mit anderen Design-Systemen

| System | Name | Besonderheit | Quelle |
|---|---|---|---|
| Carbon | Radio button | Textradios, kein Zurücksetzen | ungeprüft |
| GOV.UK | Radios, inline | Textradios nebeneinander für ja/nein | ungeprüft |

## Verwandte Bausteine

Prüfkarte (`km-criterion`), Segmented Control (`km-segmented`), Kontrollkästchen (`km-check`).

## Tokens

`--km-component-answer-size`, `--km-color-feedback-success|danger|warning` mit `-background`, `--km-color-border-input`, `--km-color-card`, `--km-color-text-dim`, `--km-color-focus`, `--km-icon`, `--km-icon-xs`.

## Offene Punkte

- Das Zurücksetzen beim zweiten Klick lebt im Skript der Seite; ein gemeinsames Skript im Kit wäre möglich, sobald eine zweite Seite den Baustein nutzt.

## Regeln

- Was: `km-answer` ist eine Radiogruppe aus gleich breiten, eckigen Symbol-Knöpfen für kurze Antworten (ja, nein, offen) mit den Optionen `--ok`, `--danger`, `--warn`; bei der Ampel zeigt `km-answer__swatch` ein farbiges Quadrat statt des Symbols.
- Wann: Bei vielen gleichartigen Fragen untereinander, wenn die Antwort auch „offen“ sein und zurückgesetzt werden darf; bei langen Optionstexten oder mehr als drei oder vier Optionen `km-check` oder KERN-Radio, für eine Ansicht `km-segmented`.
- Wie: Gruppe mit `role="radiogroup"` und `aria-label` (im `fieldset` ohne eigene Rolle), je Option ein `label.km-answer__opt` mit Radio, `km-answer__face`, Lucide-Symbol `__sign` und `__reset` sowie gleichem Kleintext in `title` und `kern-sr-only`; Speichern und Zurücksetzen beim zweiten Klick macht das Skript der Seite.
- Prüfen: Fertig ist es, wenn jeder Zustand der Tabelle erreichbar ist, die Wahl auch unter der Maus bleibt, der Fokus mit `--km-color-focus` sichtbar ist, die Farbe nie die einzige Information ist, Symbol auf Fläche mindestens 4,5:1 und der Rand mindestens 3:1 misst und bei 390 px die Knöpfe unter dem Fragetext stehen.
