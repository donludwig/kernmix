# Karte (`km-card`, `km-cards`)

Status: stabil, in Dashboard und Lagebild im Einsatz · Story: `docs/index.html#karte`, `#projektkarte`, `#info-karte`, `#kuerzel`, `#fliesstext` (Fußnote, „Mehr“), `#teilstuecke` (Unterkarte), `#karte-bild` (Karte mit Bild) · CSS: `src/km-components.css`, Abschnitte „Karte“, „Kürzel-Karte“, „Fließtext und Kartenfußnote“, „Info-Karte“, „Funktionsknöpfe im Kartenkopf“ · Stand: 2026-11-09

## Kurzbeschreibung

Die Karte fasst eine zusammengehörige Sache in einer abgegrenzten Fläche: ein Projekt, einen Skill, eine Regel, einen Bestandteil einer Website. Sie hat einen Kopf mit Kachel, Titel und Etiketten, darunter Text, Fakten, Flächen für Abschnitte und eine Fußzeile. Karten stehen im Raster `km-cards`, das die Breite füllt und auf schmalen Bildschirmen einspaltig wird. Eine farbige Kante oben oder links ordnet die Karte einem Projekt, einer Gruppe oder einem Zustand zu.

## Name und Abgrenzung

- Klasse `km-card`, Raster `km-cards`; in der Oberfläche heißt die Karte nach ihrem Gegenstand.
- Zum Baustein gehören Kopf (`__head`, `__tile`, `__title`, `__subtitle`, `__meta`, `__badges`, `__actions`), Körper (`__body`, `__text`, `__text--dim`), Fuß (`__foot`, `__note`, `__more`), Flächen (`km-panels`, `km-panel`) und die Varianten.
- Nicht dazu gehören Inhalte anderer Bausteine darin (Fakten `km-facts`, Einführung `km-intro`, Chips) und das Auf- und Zuklappen als Verhalten.
- KERN „Card“ (`kern-card`): Media, Header, Body, Footer mit ein bis zwei Knöpfen, interaktiv als Ganzes, drei Größen.
- `km-card` ist dichter, hat Akzentkanten, Kachel, Etiketten im Kopf und ist klappbar; ein großes Bild neben Text steht in `km-intro`; ein Vorschaubild oben in der Karte über `km-card__media` (seit 0.15.0, mit Link `km-card__link` unten).
- `km-agent__card`, `km-feature`, `km-task` sind eigene Karten-Bausteine mit festem Inhalt; `km-card` ist der allgemeine.
- `km-shortcut` ist eine Variante von `km-card` (Kürzel als gefüllte Fläche), keine eigene Karte.

## Einsatz

### Verwenden, wenn

- mehrere gleichartige Dinge als Text nebeneinander stehen (Skills, Bestandteile, Regeln);
- ein Ding viele verschiedene Angaben hat (Projektkarte mit Fakten, Abschnitten, Pfaden);
- Inhalte Text sind und eine Tabelle sie quetschen würde (`km-card--info`, Seitenregeln „Karten“).

### Nicht verwenden, wenn

- gleichartige Dinge mit gleichen Spalten verglichen werden: Standard-Tabelle (Entscheidung 19);
- ein ganzer Abschnitt der Seite gemeint ist: `km-section`;
- eine Aufgabe mit Kästchen gezeigt wird: `km-task`;
- nur ein kurzer Hinweis gebraucht wird: `km-note`.

## Verwendung

```html
<div class="km-cards">
  <article class="km-card km-card--accent-top" style="--km-card-accent:var(--km-color-tool-design)">
    <div class="km-card__head">
      <span class="km-card__tile"><svg class="km-icon" aria-hidden="true">…</svg></span>
      <div><h3 class="km-card__title">Hochladen</h3><code class="km-card__meta">hochladen</code></div>
    </div>
    <p class="km-card__text">Zeigt, was hochgeht, wartet auf die Freigabe, prüft danach den Live-Stand.</p>
    <div class="km-card__foot"><span>Global</span><span>Stand 08.11.2026</span></div>
  </article>
</div>
```

## Aufbau

| Teil | Klasse | Funktion |
|---|---|---|
| Raster | `km-cards` | `auto-fill`, Spalten mindestens 15rem (bzw. 100 %), Abstand `--km-space-block`. |
| Karte | `km-card` | Spalte, Teile im Abstand `--km-space-group`, Innenrand `--km-space-card`, Fläche `--km-color-card`, Rand `--km-color-border-card`. |
| Kopf | `km-card__head` | Zeile, bricht um; Titelblock mindestens 8rem breit, Etiketten rutschen darunter. |
| Kachel | `km-card__tile` | Icon-Kachel `--km-icon-tile` (2.25rem) in der Akzentfarbe der Karte. |
| Titel | `km-card__title` | `--km-font-size-m`, kräftig, `text-wrap: balance`. |
| Untertitel, Meta | `km-card__subtitle`, `km-card__meta` | Nebentext bzw. Kennung, gedämpft. |
| Etiketten | `km-card__badges` oder einzelne `km-pill` im Kopf | rechts im Kopf. |
| Aktionen | `km-card__actions` | eigene Zeile unter Titel und Etiketten, dieselben `km-iconbtn` wie in der Tabellenzeile. |
| Körper | `km-card__body`, `km-card__text`, `__text--dim` | Fließtext `--km-font-size-s`, gedämpft. |
| Flächen | `km-panels`, `km-panel` | Abschnitte im Raster (ab 16rem zweispaltig), Kante oben in der Kartenfarbe, Listenpunkte als Lucide-Chevron, nummeriert mit Zahl. |
| Fuß | `km-card__foot` | Linie oben, Meta-Angaben. |
| Mehr | `km-card__more` | `<details>` für Zusatzangaben. |
| Fußnote | `km-card__note` | Quelle oder Stand, Linie oben; in der Info-Karte unten bündig. |

## Varianten

- **Akzent oben** `km-card--accent-top`: Karten im Raster mit Gruppenfarbe (Skills, Kürzel).
- **Akzent links** `km-card--accent-left`: Projekt- und Regelkarten. Farbe je Karte über `--km-card-accent`, Standard Akzent.
- **Interaktiv** `km-card--interactive`: ganze Karte als Ziel, Hover tönt 5 %.
- **Klappbar** `km-card--collapsible`, zu mit `km-card--collapsed`: nur der Kopf bleibt; Pfeil hinter dem Titel.
- **Info-Karte** `km-card--info`: kleine Karte für Bestandteile; Kachel 1.75rem, Titel `--km-font-size-s`, Pill rechts mittig zur ersten Titelzeile, Fußnote unten bündig, Karten einer Reihe gleich hoch.
- **Unterkarte** `km-card--sub`, `--sub-2`: Unterprojekt unter seinem Hauptprojekt, eingerückt um `--km-space-xl` bzw. das Doppelte.
- **Kürzel-Karte** `km-shortcut` (mit `km-card--accent-top`): Kürzel `km-shortcut__key` als gefüllte Fläche im Akzent; `km-shortcut--attention` in der Signalfarbe für Kürzel mit Wirkung nach außen.

## Größen

Eine Größe; die Info-Karte ist die kleine Fassung.

## Zustände

| Zustand | Auslöser | Darstellung | Tokens |
|---|---|---|---|
| Ruhe | – | Kartenfläche, Rand | `--km-color-card`, `--km-color-border-card` |
| Hover (interaktiv) | `.km-card--interactive:hover` | 5 % Akzent auf der Fläche, Rand 40 % Akzent | `--km-color-accent` |
| Fokus | `:focus-visible` an Link oder `[tabindex]` in der Karte | Ring außen | `--km-color-focus` |
| Zu | `km-card--collapsed` | nur der Kopf, Pfeil nach rechts | `--km-caret-mask` |
| Offen | `km-card--collapsible` ohne `--collapsed` | Pfeil nach unten | – |
| Deaktiviert | `.km-card--interactive[aria-disabled="true"]` | abgeblendet, keine Hover-Wirkung | `--km-opacity-disabled` |
| Leerer Kopfteil | `:empty` im Kopf | ausgeblendet | – |

## Verhalten

- Klappen: Die Seite setzt `km-card--collapsed`; ein klappbarer Titel bekommt `role="button"`, `tabindex="0"`, `aria-expanded` und Tastaturbedienung (Story `#zustaende-skript`).
- Karten einer Reihe sind im Raster gleich hoch (Grid streckt), die Info-Karte schiebt die Fußnote nach unten.

## Text und Wording

- Titel: Name der Sache, höchstens etwa 40 Zeichen; Untertitel eine Zeile.
- Text: zwei bis drei Sätze; längere Texte gehören in `km-intro` mit „Weiterlesen“.
- Fuß und Fußnote: Stand, Quelle oder Geltung, kein Fließtext.

## Barrierefreiheit

- Struktur: `article` je Karte, Titel als Überschrift passender Ebene; im Raster eine Liste (`ul`/`li`) wäre für Screenreader genauer, die Stories nutzen `div`.
- Interaktive Karte: nur ein Ziel je Karte; weitere Knöpfe darin konkurrieren mit dem Kartenklick.
- Akzentfarbe ist nie die einzige Information; die Gruppe steht auch als Text.
- Kontrast (gerechnet):

| Paar | Kobalt dunkel | Kobalt hell | Papier dunkel | Papier hell |
|---|---|---|---|---|
| Titel `--km-color-text` auf `--km-color-card` | 14,16 | 15,89 | 13,03 | 17,61 |
| Text `--km-color-text-muted` auf `--km-color-card` | 7,89 | 7,85 | 8,57 | 7,79 |
| Meta, Fuß `--km-color-text-dim` auf `--km-color-card` | 6,25 | 6,05 | 5,78 | 6,23 |
| Text bei Hover auf 5 % Akzent | 7,19 | 7,28 | 7,83 | 7,17 |
| Kachel-Icon `--km-color-accent` auf `--km-color-inset` | 7,52 | 6,14 | 7,43 | 7,42 |
| Kürzel `--km-color-on-accent` auf `--km-color-accent` | 9,13 | 6,69 | 8,68 | 8,38 |
| Kürzel Signal `--km-color-on-attention` auf `--km-color-attention` | 8,60 | 5,47 | 8,99 | 5,47 |
| Rand `--km-color-border-card` auf `--km-color-card` | 1,42 | 1,39 | 1,27 | 1,32 |

Der Kartenrand ist schwach; die Karte grenzt sich über die Fläche vom Bereich ab. Für eine interaktive Karte fordert KERN 3:1 zum Umfeld (WCAG 1.4.11).

- Schmal (390 px): Raster einspaltig (`minmax(min(15rem, 100%), 1fr)`).

## Beispiele

### Richtig

```html
<article class="km-card km-card--accent-left km-card--info">
  <div class="km-card__head"><span class="km-card__tile">…</span><h4 class="km-card__title">Konten</h4><span class="km-pill km-pill--neutral">2FA an</span></div>
  <p class="km-card__meta">Konten · 1 Admin</p>
  <p class="km-card__note">Pflege: von Hand</p>
</article>
```

### Falsch

```html
<!-- Akzentstrich an der äußeren Container-Karte und an der inneren -->
<article class="km-card km-card--accent-left"><article class="km-card km-card--accent-left">…</article></article>
<!-- langer Status in der Pill quetscht den Titel -->
<span class="km-pill km-pill--ok">aktiv seit dem letzten Update, automatisch gepflegt</span>
<!-- Kante mit border-left neben einer Kante als Innenschatten -->
<article class="km-card" style="border-left:3px solid #d97757">…</article>
```

Warum: Farbstrich nur an der innersten Karte; lange Status-Texte gehören in die Meta-Zeile; keine harten Farben, Kanten einheitlich (Entscheidungen 11, 18, 25).

## Seitenregeln

- Aus `docs/seitenregeln.md`, „Karten“: Kartenkopf mit Mindestbreite des Titels, Etiketten rutschen darunter; Info-Karten nebeneinander statt Tabellen, wenn Inhalte Text sind; Farbstrich links nur an der innersten Karte.
- Dazu: Symbol mittig zur ersten Zeile; Farbkanten mit derselben Technik; keine harten Werte; Beispiele ohne harte Farben.

Entscheidungen: 11 (Token-Rollen), 12 (Abstände), 18 (Ausrichtung und Kanten), 25 (Karten), 27 (schmale Breite).

## Vergleich mit anderen Design-Systemen

| System | Name | Besonderheit | Quelle |
|---|---|---|---|
| KERN 2.8.2 | Card | „strukturierte Präsentation eines bestimmten Inhalts“; Teile Media, Header, Body, Footer mit ein bis zwei Knöpfen; interaktiv als Ganzes (`kern-card--interactive`); Größen small, default, large; Kontrast zum Umfeld mindestens 3:1 | kern-ux.de/komponenten/card |

## Verwandte Bausteine

`km-section`, `km-facts`, `km-intro`, `km-pill`, `km-chip`, `km-iconbtn`, `km-task`, `km-agent`, `km-feature`.

## Tokens

Rollen: `--km-color-card`, `--km-color-border-card`, `--km-color-inset`, `--km-color-text`, `--km-color-text-muted`, `--km-color-text-dim`, `--km-color-accent`, `--km-color-on-accent`, `--km-color-attention`, `--km-color-on-attention`, `--km-space-card`, `--km-space-group`, `--km-space-block`, `--km-border-width-accent`, `--km-icon-tile`, `--km-icon-m`, `--km-font-size-m`, `--km-font-size-s`, `--km-font-size-xl`.

- Komponenten-Haken: `--km-card-accent` (Kartenfarbe, auch von `km-fact`, `km-panel`, `km-intro`, `km-histo` gelesen), `--km-pill-h` (gemessene Pill-Höhe 1,575rem in der Info-Karte).
- Hart im Baustein: Tönungen 5 % und 40 % im Hover, Mindestbreiten 15rem (Raster), 16rem und 8rem (Kopf), `font-weight: 700` des Kürzels.

## Offene Punkte

- Fußnote `km-card__note` ist kursiv, in der Info-Karte nicht; einheitlich festlegen.
- `km-card__head > .km-pill` ist zweimal geregelt: einmal `flex: none` (so breit wie der Text), weiter unten `white-space: normal` (darf umbrechen); die Seitenregel sagt „Etiketten rutschen darunter“, die Pill-Regel „bricht nie in sich um“.
- Kartenraster ohne Listen-Semantik.

## Regeln

- Was: Die Karte `km-card` fasst eine zusammengehörige Sache in einer abgegrenzten Fläche mit Kopf (Kachel, Titel, Etiketten), Text, Fakten, Flächen und Fuß und steht im Raster `km-cards`; Varianten sind `km-card--accent-top`, `km-card--accent-left`, `km-card--interactive`, `km-card--collapsible`, `km-card--info`, `km-card--sub`, die Karte mit Bild (`km-card__media` oben, `km-card__link` unten) und die Kürzel-Karte `km-shortcut`.
- Wann: Für mehrere gleichartige Dinge als Text oder ein Ding mit vielen verschiedenen Angaben; gleichartige Dinge mit gleichen Spalten gehören in die Standard-Tabelle, ein ganzer Abschnitt in `km-section`, eine Aufgabe in `km-task`, ein kurzer Hinweis in `km-note`.
- Wie: `article` mit `km-card__head`, `km-card__title` als Überschrift passender Ebene, `km-card__text` (zwei bis drei Sätze) und `km-card__foot` für Stand oder Quelle; Farbe über `--km-card-accent` aus einer Rolle, Farbstrich nur an der innersten Karte, lange Status-Texte in die Meta-Zeile statt in die Pill, bei klappbarer Karte `role="button"`, `tabindex="0"` und `aria-expanded` am Titel.
- Prüfen: Fertig ist es, wenn Ruhe, Hover, Fokus, Zu und Offen der Tabelle erreichbar sind, Titel und Text in allen Themes mindestens 4,5:1 messen, die Gruppe auch als Text dasteht, eine interaktive Karte nur ein Ziel hat und das Raster bei 390 px einspaltig ist.
