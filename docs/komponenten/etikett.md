# Pill und Chip (`km-pill`, `km-chip`)

Status: stabil, in Dashboard und Lagebild im Einsatz · Story: `docs/index.html#chip-pill`, `#noten`, `#tabelle` (Phasen), `#zustaende` (`--stabil`) · CSS: `src/km-components.css`, Abschnitte „Chip (Verweis) und Pill (Zustand)“, „Phasen als Pill“, „Für das Lagebild“ (Noten) · Stand: 2026-11-09

## Kurzbeschreibung

Pill und Chip sind kleine Etiketten in Mono-Schrift mit Rahmen. Die Pill zeigt einen Zustand (läuft, wartet, fehlt, Phase eines Projekts, Note A bis D) und ist nicht bedienbar. Der Chip ist ein Verweis auf etwas anderes, meist ein Link (Projekt, Datei, Skill), und färbt sich beim Überfahren. Beide sind Werte: Sie brechen nie in sich um und stehen neben ihrem Bezugstext, nicht darunter.

## Name und Abgrenzung

- `km-pill` = Zustand, `km-chip` = Verweis. In der Oberfläche heißen beide nach ihrem Inhalt; im Text der Doku „Etikett“ für beide.
- Zur Pill gehören die Zustände `--ok`, `--info`, `--warn`, `--danger`, `--neutral`, die Phasen `--idee`, `--konzept`, `--prototyp`, `--migration`, `--aktiv`, `--stabil`, `--toolkit` und die Noten `--grade` mit `--grade-a` bis `--grade-d`.
- Zum Chip gehören `--muted` (Pfad, nicht klickbar) und `--extern` (Pfeil davor) sowie die Reihe `km-chips`.
- Nicht dazu: Filter im Suchfeld (`km-filterchips__chip`), Zähler (`km-count`), Kennung einer Aufgabe (`km-task__id`), Filter-Chip im Bereichskopf (`km-section__chip`).
- KERN „Badge“: knapper Status-Hinweis zu einem übergeordneten Element, nicht interaktiv, vier Farben, zwei Größen, Icon optional.
- `km-pill` entspricht dem Badge, ist kleiner (12 px Schrift) und hat eigene Phasen und Noten; einen klickbaren Chip hat KERN nicht.

## Einsatz

### Verwenden, wenn

- ein Zustand in Tabelle, Kartenkopf oder Angabenliste steht (Pill);
- eine Phase oder Note angezeigt wird (Pill mit Modifier);
- ein kurzer Verweis neben Text steht oder Links einer Zeile gereiht werden (Chip, `km-chips`).

### Nicht verwenden, wenn

- der Zustand bedienbar sein soll (an/aus): `km-switch`, `km-iconbtn` mit `aria-pressed`;
- eine Aktion ausgelöst wird: `km-button` oder `km-iconbtn`, nie ein Chip als Knopf-Ersatz;
- der Text länger als drei Wörter ist: Meta-Zeile oder Fließtext;
- ein Link im Fließtext steht: `km-link`.

## Verwendung

```html
<span class="km-pill km-pill--warn">wartet</span>
<span class="km-pill km-pill--prototyp">Prototyp</span>
<span class="km-table__label"><span class="km-pill km-pill--grade km-pill--grade-a">A</span>ab 90</span>
<div class="km-chips"><a class="km-chip" href="#kopiertext">Kopiertext</a><a class="km-chip km-chip--extern" href="https://…">Live</a><span class="km-chip km-chip--muted">~/projekte/projekt-11</span></div>
```

## Aufbau

| Teil | Klasse | Funktion |
|---|---|---|
| Pill | `km-pill` | Mono, `--km-font-size-xs`, Rahmen in der Textfarbe (`currentColor`), keine Fläche, nie umbrechen. |
| Note | `km-pill--grade` + `--grade-a…d` | zentriert, Mindestbreite `--km-icon-tile`, kräftig, Fläche aus der KERN-Rückmeldefarbe. |
| Chip | `km-chip` | Textschrift, Akzentfarbe, Rahmen `--km-color-border-card`, nie unterstrichen. |
| Pfad | `km-chip--muted` | Mono, gedämpft. |
| Extern | `km-chip--extern` | Lucide `arrow-up-right` als Maske davor. |
| Reihe | `km-chips` | Chips im Abstand `--km-space-tight`; in Tabellen ohne Umbruch. |

## Varianten

| Modifier | Farbe | Bedeutung |
|---|---|---|
| `--ok` | `--km-color-feedback-success` | erfüllt, geschützt |
| `--info` | `--km-color-feedback-info` | läuft, offen |
| `--warn` | `--km-color-feedback-warning` | wartet, braucht Aufmerksamkeit |
| `--danger` | `--km-color-feedback-danger` | fehlt, überfällig |
| `--neutral` | `--km-color-text-muted` | ruht, ohne Wertung |
| `--idee` | `--km-color-text-dim` | Phase Idee |
| `--konzept` | `--km-color-text-muted` | Phase Konzept |
| `--prototyp` | warning | Phase Prototyp |
| `--migration` | info | Phase Migration |
| `--aktiv`, `--stabil` | success | Phasen Aktiv, Stabil |
| `--toolkit` | `--km-color-accent` | ältere Phase „Toolkit“, heute als „Stabil“ geführt |
| `--grade-a` bis `--grade-d` | success, info, warning, danger mit Fläche | Score-Note |

## Größen

Eine Größe. Gemessen (headless Chrome, Kobalt dunkel): Pill 20,00 px, Chip 21,00 px hoch.

## Zustände

| Zustand | Auslöser | Darstellung | Tokens |
|---|---|---|---|
| Pill | – | statisch, kein Hover | – |
| Chip Ruhe | – | Akzent-Text, schwacher Rand | `--km-color-accent`, `--km-color-border-card` |
| Chip Hover | `:hover` | Rand im Akzent | `--km-color-accent` |
| Chip Fokus | `:focus-visible` | Ring außen | `--km-color-focus` |
| Chip besucht | `a.km-chip:visited` | unverändert, nie unterstrichen | – |
| Chip deaktiviert | `aria-disabled="true"` | abgeblendet, nicht klickbar | `--km-opacity-disabled` |
| Leer | kein Wert | keine Pill; „leer heißt ohne Wert, nicht ok“ | – |

## Verhalten

Kein Verhalten im Kit. Ein Chip ist ein Link (`<a>`); ist er kein Link, dann `--muted`.

## Text und Wording

- Pill: ein bis zwei Wörter, Adjektiv oder Partizip („läuft“, „wartet“), höchstens etwa 16 Zeichen; Phasen genau mit den sieben Namen der Phasen-Liste.
- Note: ein Buchstabe, Schwelle als Text daneben („A ab 90“) mit `km-table__label` (fester Abstand statt Leerzeichen).
- Chip: Name des Ziels, höchstens etwa 24 Zeichen; Pfade dürfen länger sein und brechen unter 40rem um.

## Barrierefreiheit

- Farbe nie allein: Die Pill trägt den Zustand als Wort, die Note den Buchstaben (WCAG 1.4.1).
- Pill ist kein Fokusziel; nur Chips mit Link sind fokussierbar.
- Dynamisch wechselnde Pills (Status, der sich ändert) braucht die Seite in einem `aria-live`-Bereich.
- Kontrast (gerechnet, Text auf `--km-color-card` bzw. Note auf ihrer Fläche):

| Paar | Kobalt dunkel | Kobalt hell | Papier dunkel | Papier hell |
|---|---|---|---|---|
| `--ok` / Aktiv | 5,55 | 6,01 | 7,51 | 5,17 |
| `--info` / Migration | 5,56 | 6,03 | 8,02 | 8,09 |
| `--warn` / Prototyp | 5,55 | 5,47 | 8,31 | 5,29 |
| `--danger` | 5,56 | 6,01 | 6,64 | 5,99 |
| `--neutral` / Konzept | 7,89 | 7,85 | 8,57 | 7,79 |
| `--idee` | 6,25 | 6,05 | 5,78 | 6,23 |
| Chip `--km-color-accent` | 8,27 | 6,69 | 8,02 | 8,09 |
| Note A auf success-Fläche | 5,34 | 4,99 | 6,23 | 4,59 |
| Note B auf info-Fläche | 5,32 | 5,03 | 6,84 | 7,01 |
| Note C auf warning-Fläche | 5,33 | 4,52 | 6,86 | 4,79 |
| Note D auf danger-Fläche | 5,34 | 4,97 | 5,94 | 5,03 |
| Chip-Rand `--km-color-border-card` | 1,42 | 1,39 | 1,27 | 1,32 |

Alle Texte ≥ 4,5; Note C in Kobalt hell knapp darüber. Der Chip-Rand liegt unter 3:1; den Chip kennzeichnet die Akzentfarbe des Texts.

- Schmal (390 px): Chips mit langen Pfaden brechen um, Pills nicht.

## Beispiele

### Richtig

```html
<td class="km-table__nowrap"><span class="km-pill km-pill--aktiv">Aktiv</span></td>
<p class="km-card__meta">Plugin · 5.5.1</p>
```

### Falsch

```html
<!-- Pill als Knopf -->
<button class="km-pill km-pill--info">Filter setzen</button>
<!-- Zustand nur über Farbe -->
<span class="km-pill km-pill--ok"></span>
<!-- Chip ohne Ziel im Akzent -->
<span class="km-chip">~/projekte/a</span>
<!-- leere Zelle als „ok“ -->
<td><span class="km-pill km-pill--ok">–</span></td>
```

## Seitenregeln

Aus `docs/seitenregeln.md`: Status als Etikett (`--ok/--warn/--danger/--neutral`), leer heißt „ohne Wert“; Status-Spalten `__nowrap` mit `km-pill`; Abstände zwischen Etikett und Text per `gap`, nie per Leerzeichen; nur die sieben Phasen (Project-Dashboard-Regel); keine Schriftzeichen als Icon (Extern-Pfeil als Maske); Knöpfe und Chips nie unterstrichen.

Entscheidungen: 15 (Kontrast), 16 (Icons), 19 (Standard-Tabelle).

## Vergleich mit anderen Design-Systemen

| System | Name | Besonderheit | Quelle |
|---|---|---|---|
| KERN 2.8.2 | Badge | „knapper Status-Hinweis zu einem übergeordneten Element“; nicht interaktiv; Info, Success, Warning, Danger; 24 und 32 px; darf nicht nur über Farbe, Form oder Position beschrieben werden | kern-ux.de/komponenten/badge |
| GOV.UK Design System | Tag | Status, wenige Zustände; „Do not make a tag interactive“; Adjektive statt Verben; gleiche Farbe für gleichen Tag überall; nicht nur über Farbe | design-system.service.gov.uk/components/tag |

- Der Chip als Link weicht von GOV.UK ab („Do not make a tag interactive“).
- Die Trennung Pill = Zustand, Chip = Verweis und die unterschiedliche Schrift (Mono bzw. Text) halten beide auseinander.

## Verwandte Bausteine

`km-count`, `km-filterchips`, `km-section__chip`, `km-task__id`, `km-link`, `km-table__label`.

## Tokens

Rollen: `--km-font-mono`, `--km-font-size-xs`, `--km-space-3xs`, `--km-space-2xs`, `--km-space-xs`, `--km-space-tight`, `--km-border-width`, `--km-color-accent`, `--km-color-border-card`, `--km-color-text-muted`, `--km-color-text-dim`, `--km-icon-extern`, `--km-icon-tile`, `--km-tracking-mono`.

- Rückmelde-Rollen: `--km-color-feedback-success`, `-info`, `-warning`, `-danger` und ihre `-background` (seit 0.6.0).
- Hart im Baustein: Größe des Extern-Pfeils `0.7em`.

## Offene Punkte

- `--toolkit` ist keine der sieben Phasen mehr; entfernen oder als Alias von `--stabil` kennzeichnen.
- Chip ist bedienbar, sieht aber Pill-ähnlich aus; die Abgrenzung beruht auf Schrift und Farbe.

## Regeln

- Was: Pill und Chip sind kleine gerahmte Etiketten: `km-pill` zeigt einen Zustand, eine Phase oder Note und ist nicht bedienbar (`--ok`, `--info`, `--warn`, `--danger`, `--neutral`, Phasen von `--idee` bis `--stabil`, Noten `--grade-a` bis `--grade-d`), `km-chip` ist ein Verweis, meist ein Link (`--muted`, `--extern`, Reihe `km-chips`); beide brechen nie in sich um.
- Wann: Pill für einen Zustand in Tabelle, Kartenkopf oder Angabenliste, für Phase oder Note, Chip für einen kurzen Verweis neben Text; bedienbare Zustände sind `km-switch` oder `km-iconbtn` mit `aria-pressed`, Aktionen `km-button`, Texte über drei Wörter eine Meta-Zeile, Links im Fließtext `km-link`.
- Wie: Pill mit ein bis zwei Wörtern (höchstens etwa 16 Zeichen), Phasen nur mit den sieben Namen, Note als ein Buchstabe mit Schwelle in `km-table__label`, Chip als `<a>` mit dem Namen des Ziels (höchstens etwa 24 Zeichen, ohne Link `--muted`), Status-Spalten mit `km-table__nowrap`, nie unterstrichen.
- Prüfen: Fertig ist es, wenn der Zustand als Wort oder Buchstabe dasteht und nie nur über Farbe, alle Texte mindestens 4,5:1 messen (Note C in Kobalt hell 4,52), nur Chips mit Link fokussierbar sind (Ring `--km-color-focus`), eine leere Zelle keine Pill zeigt und bei 390 px nur lange Chip-Pfade umbrechen.
