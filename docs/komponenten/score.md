# Score und Fortschritt (`km-score`, `km-progress`)

Status: Entwurf · Story: `docs/index.html#score` · CSS: `src/km-components.css`, Abschnitt „Fragebogen-Bausteine“ · Stand: 2026-11-09

## Kurzbeschreibung

Der Score zeigt das Ergebnis eines Fragebogens: große Zahl mit Höchstwert, Stufe als Note A bis E, eine Lesart in einem Satz, Teilwerte als Balken und einen Vergleich mit einer früheren Erhebung. Der Fortschritt zeigt, wie viel beantwortet ist: Beschriftung, Zählung und flacher Balken.

## Name und Abgrenzung

- `km-score` („Score“), `km-progress` („Fortschritt“). Die Note ist `km-pill--grade-a` bis `-e` (Pill-Baustein, E neu in 0.10.0).
- Abgrenzung: Fakten-Kacheln (`km-facts`) zeigen mehrere gleichrangige Werte; der Score einen Hauptwert mit Bewertung.
- KERN `kern-progress` gilt für Formulare mit nativem `<progress>`; `km-progress` ist eine Anzeige mit Zählung für Seitenleisten.

## Einsatz

### Verwenden, wenn

- eine Punktzahl mit Stufe und Teilen live mitläuft (Seitenleiste eines Fragebogens);
- ein Anteil mit Zählung („6 von 15“) zu zeigen ist.

### Nicht verwenden, wenn

- mehrere Werte gleich wichtig sind (dann `km-facts`).

## Verwendung

```html
<div class="km-score">
  <p class="km-score__label">Score</p>
  <p class="km-score__value">62<small>/ 100</small></p>
  <span class="km-pill km-pill--grade km-pill--grade-c km-score__grade">Stufe C</span>
  <p class="km-score__reading">Lesart</p>
  <div class="km-score__parts"><div class="km-progress" style="--km-progress:70%"><div class="km-progress__head"><span>Teil A</span><span class="km-progress__count">51 / 73</span></div><div class="km-progress__bar"></div></div></div>
  <p class="km-score__compare">Vorige Erhebung: <strong>48 / 100</strong></p>
</div>
```

## Aufbau

| Teil | Klasse | Funktion |
|---|---|---|
| Beschriftung | `km-score__label` | Versalien, gedämpft |
| Zahl | `km-score__value` | Überschriftenschrift, `--km-component-score-value-font-size`, Höchstwert klein in `small` |
| Note | `km-score__grade` + `km-pill--grade-*` | links ausgerichtet |
| Lesart | `km-score__reading` | Arbeitstext gedämpft |
| Teile | `km-score__parts` | Liste von `km-progress` |
| Vergleich | `km-score__compare` | Linie oben, Wert fett |
| Fortschritt | `km-progress`, `__head`, `__count`, `__bar`, `--ok` | Anteil über `--km-progress`, Farbe Akzent bzw. Erfolg |

## Varianten

`km-progress--ok` färbt den Balken in der Erfolgsfarbe (fertig).

## Zustände

| Zustand | Auslöser | Darstellung | Tokens |
|---|---|---|---|
| Note A–D | `km-pill--grade-a` bis `-d` | Text und Fläche der Rückmeldefarbe | `--km-color-feedback-*` |
| Note E | `km-pill--grade-e` | gefüllt in der Fehlerfarbe | `--km-color-on-attention`, `--km-color-feedback-danger` |
| Anteil | `--km-progress` (0–100 %) | Balkenlänge | `--km-color-accent`, `--km-color-track` |

## Verhalten

Die Seite rechnet und setzt Zahl, Notenklasse, Lesart und `--km-progress`. Zahlen haben gleich breite Ziffern, damit beim Rechnen nichts springt.

## Barrierefreiheit

- Die Ergebnisleiste der Seite trägt `aria-live="polite"`; der Balken ist `aria-hidden`, die Zählung steht als Text daneben.
- Kontrast Note E: Papier hell 6,2, dunkel 7,19; Kobalt hell 6,01, dunkel 6,14 (gemessen).

## Seitenregeln

Tabellenziffern nur an Zahlen; Nichts springt beim Wählen.

## Vergleich mit anderen Design-Systemen

| System | Name | Besonderheit | Quelle |
|---|---|---|---|
| Carbon | Progress bar | Beschriftung und Wert über dem Balken | ungeprüft |

## Verwandte Bausteine

Pill und Chip (`km-pill`), Kennzahlen (`km-facts`), Prüfkarte (`km-criterion`).

## Tokens

`--km-component-score-value-font-size`, `--km-bar-l`, `--km-color-track`, `--km-color-accent`, `--km-progress`, `--km-progress-color`.

## Offene Punkte

- Mobil legt die Seite den Score als Leiste an den unteren Rand; eine Kit-Variante dafür fehlt noch.

## Regeln

- Was: `km-score` zeigt das Ergebnis eines Fragebogens mit großer Zahl und Höchstwert, Note A bis E als `km-pill--grade-a` bis `-e`, Lesart, Teilwerten als `km-progress` und Vergleich mit einer früheren Erhebung; `km-progress` zeigt Beschriftung, Zählung und flachen Balken, `km-progress--ok` färbt ihn in der Erfolgsfarbe.
- Wann: Für eine Punktzahl mit Stufe und Teilen, die live mitläuft, oder einen Anteil mit Zählung wie „6 von 15“; sind mehrere Werte gleich wichtig, nimm `km-facts`.
- Wie: `km-score__label`, `km-score__value` mit dem Höchstwert in `small`, `km-score__grade` zusammen mit `km-pill--grade-*`, `km-score__reading`, `km-score__parts` mit `km-progress` und Anteil über `--km-progress` (0 bis 100 %), Zahlen mit gleich breiten Ziffern; Zahl, Notenklasse, Lesart und `--km-progress` setzt die Seite.
- Prüfen: Fertig ist es, wenn die Ergebnisleiste `aria-live="polite"` trägt, der Balken `aria-hidden` ist und die Zählung als Text danebensteht, jede Note A bis E in allen Themes lesbar ist und beim Rechnen nichts springt.
