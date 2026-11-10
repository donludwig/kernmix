# Bereich (`km-section`, `km-subhead`, `km-cardgroup`, `km-focus`)

Status: stabil, in Dashboard und Lagebild im Einsatz · Story: `docs/index.html#bereich`, `#fokus`, `#gruppe` (Zwischenüberschrift), `#teilstuecke`, `#bedienteile`, `#zustaende-skript` · CSS: `src/km-components.css`, Abschnitte „Bereich (Wanne)“, „Zwischenüberschrift in einem Bereich“, „Fokus (angeheftete Projekte)“, „Dashboard-Gerüst“ (Kartengruppe, Bereichs-Einleitung) · Stand: 2026-11-09

## Kurzbeschreibung

Der Bereich ist die Wanne um jeden Abschnitt einer Werkzeugseite: eine Fläche mit Rand, dunkler als die Karten darin, mit einem Kopf aus Icon, Titel, Zähler und Werkzeugen. Der Kopf ist ein `<summary>`, der Bereich klappt also nativ auf und zu. Im Rumpf liegen Karten, Tabellen, Suchfelder und Listen mit festen Abständen nach dem Abstands-Regelwerk. Innerhalb eines Bereichs gliedern Zwischenüberschriften (`km-subhead`) und Kartengruppen (`km-cardgroup`); der hervorgehobene Bereich (`km-focus`) zeigt angeheftete Einträge über der Hauptliste.

## Name und Abgrenzung

- Klasse `km-section`; in der Oberfläche trägt der Bereich seinen Titel („Skills“, „Projektübersicht“). „Wanne“ ist der Arbeitsbegriff im CSS.
- Zum Baustein gehören Kopf (`__head`, `__icon`, `__title`, `__count`, `__meta`, `__chip`, `__tools`, `__grip`), Rumpf (`__body`, `__body--stack`), Einleitung (`__lead`), Zwischenüberschrift (`km-subhead`), Kartengruppe (`km-cardgroup`) und die Hervorhebung (`km-focus`).
- Nicht dazu gehören Inhalt, Reihenfolge der Bereiche und das Verschieben selbst (Skript der Seite).
- `km-card`: liegt im Bereich, nie umgekehrt.
- Ein Bereich hat keinen Akzentstrich; der Farbstrich gehört an die innerste Karte (Seitenregeln „Karten“, Entscheidung 25).
- KERN hat keinen eigenen Abschnitts-Baustein; nächstverwandt ist das KERN-„Accordion“ (ungeprüft), weil der Kopf aufklappt.
- Ein Bereich ist aber Seitengliederung mit eigener Navigation in der Seitenleiste, kein Akkordeon in einem Inhalt.

## Einsatz

### Verwenden, wenn

- eine Werkzeugseite in Abschnitte gegliedert wird, die in der Seitenleiste als Sprungziel stehen;
- ein Abschnitt zuklappbar sein soll;
- angeheftete Einträge über einer Liste gezeigt werden (`km-focus` zusätzlich am Bereich).

### Nicht verwenden, wenn

- nur eine Gruppe von Karten innerhalb eines Bereichs benannt werden soll: `km-subhead` oder `km-cardgroup`;
- Inhalt in Fließtext aufklappen soll: `<details>` mit `km-details__body`;
- ein Bereich in einem Bereich entstehen würde: Bereiche verschachteln nicht.

## Verwendung

```html
<details class="km-section" id="skills" open>
  <summary class="km-section__head">
    <span class="km-section__icon"><svg class="km-icon" aria-hidden="true">…</svg></span>
    <h2 class="km-section__title">Skills</h2>
    <span class="km-section__count">53</span>
    <span class="km-section__meta">33 allgemein</span>
    <span class="km-section__tools"><button type="button" class="km-iconbtn km-iconbtn--label">Alle zu</button></span>
  </summary>
  <div class="km-section__body">
    <p class="km-note">Einleitung des Bereichs in einem Satz.</p>
    <h3 class="km-subhead"><svg class="km-icon" aria-hidden="true">…</svg>Allgemein <span>33</span><small>für alle Projekte nutzbar</small></h3>
    <div class="km-cards">…</div>
  </div>
</details>
```

## Aufbau

| Teil | Klasse | Funktion |
|---|---|---|
| Wanne | `km-section` | Fläche `--km-color-section`, Rand `--km-color-border-section`, Abstand nach unten `--km-space-page`; meist `<details>`. |
| Kopf | `km-section__head` | `<summary>` ohne Browser-Marker, Innenrand `--km-space-section-y` / `-x`, Teile im Abstand `--km-space-group`. |
| Icon | `km-section__icon` | Kachel 2rem auf `--km-color-inset`, Icon im Akzent. |
| Titel | `km-section__title` | `--km-font-display`, `--km-font-size-l`, kräftig; Aufklapp-Pfeil per `::after` (offen nach unten). |
| Zähler | `km-section__count` | Mono, gerahmt, so hoch wie `km-iconbtn--label` (`--km-control-height`); gleiches Bild wie `km-count--boxed`. |
| Meta | `km-section__meta` | gedämpfter Zusatz, `--km-font-size-xs`. |
| Filter-Chip | `km-section__chip` | aktiver Filter im Kopf, Kante links in `--chip-color`. |
| Werkzeuge | `km-section__tools` | rechtsbündig im Fluss; wird es eng, rutschen sie in die nächste Zeile. |
| Griff | `km-section__grip` | Verschieben des Bereichs, oben rechts. |
| Rumpf | `km-section__body`, `--stack` | Innenrand seitlich und unten `--km-space-section-x`; `--stack` setzt Inhalte untereinander im Abstand `--km-space-block`. |
| Einleitung | `km-section__lead` oder erste `km-note` im Rumpf | Lesegröße `--km-font-size-m`, höchstens 90ch. |
| Zwischenüberschrift | `km-subhead` | Versalien, Zahl (`span`) und Hinweis (`small`) dahinter, optional Icon im Akzent. |
| Kartengruppe | `km-cardgroup`, `__count`, `__toggle` | Knopf als Kopf einer Kartengruppe, Kante links in `--org-color`. |
| Hervorhebung | `km-focus`, `__table`, `__count`, `__hint`, `__scroll` | Rand und Fläche in `--km-color-highlight` / `-bg`, Kante an jeder Zeile der Tabelle. |

## Varianten

- **Standard**: `<details class="km-section" open>`.
- **Gestapelt** `km-section__body--stack`: Rumpf mit lauter gleichrangigen Blöcken (Lagebild).
- **Hervorgehoben** `km-section km-focus`: angeheftete Einträge; ist nichts angeheftet, `hidden`.
- **Umgebrochener Kopf** `km-section__head--wrapped` (setzt das Skript): Werkzeuge linksbündig unter dem Titel.

## Größen

Eine Größe. Gemessen (headless Chrome, Kobalt dunkel): Zähler `km-section__count` und `km-iconbtn--label` im Kopf je 25,59 px hoch.

## Zustände

| Zustand | Auslöser | Darstellung | Tokens |
|---|---|---|---|
| Offen | `details[open]` | Rumpf sichtbar, Pfeil nach unten | `--km-caret-mask` |
| Zu | ohne `open` | nur Kopf, Pfeil nach rechts | – |
| Fokus Kopf | `:focus-visible` am `summary` | Ring außen (gemeinsame Fokus-Regel) | `--km-color-focus` |
| Griff Hover | `:hover` | Fläche `--km-color-inset`, Icon voll | `--km-color-text` |
| Ziehen | `km-section--dragging` | 40 % abgeblendet, gestrichelter Rahmen im Akzent | `--km-color-accent` |
| Kopf umgebrochen | `km-section__head--wrapped` | Werkzeuge unter dem Titel | – |
| Hervorgehoben leer | `km-focus[hidden]` | ausgeblendet | – |
| Hinweis blendet aus | `km-focus__hint--out` | Hinweis wird durchsichtig | – |

## Verhalten

- Auf- und Zuklappen nativ über `<details>`; den Zustand speichert die Seite in localStorage (Entscheidung 9).
- Verschieben über den Griff und die Rangfolge der Bereiche: Skript der Seite (Ziehen siehe `ziehen.md`).
- Bereichsklick in der Seitenleiste springt hierher und öffnet den Bereich (Seitenregeln „Filter öffnet, was er zeigt“).

## Text und Wording

- Titel: ein bis zwei Wörter, Substantiv („Skills“, „Weitere Server“).
- Zähler: Zahl und höchstens ein Wort („36 offen“).
- Einleitung: ein bis zwei Sätze; was der Bereich zeigt, nicht wie er bedient wird.
- Zwischenüberschrift: ein Wort plus Zahl, Hinweis höchstens etwa 40 Zeichen.

## Barrierefreiheit

- Struktur: Titel ist eine echte Überschrift (`h2` bzw. passend zur Seite) im `summary`.
- Ein Knopf im `summary` (Werkzeuge) ist erlaubt, bekommt aber eigene Klicks; die Seite muss verhindern, dass der Klick den Bereich zuklappt.
- Tastatur: `summary` ist nativ fokussierbar, Enter und Leertaste klappen.
- Hervorhebung nicht nur über Farbe: der hervorgehobene Bereich trägt einen eigenen Titel und Zähler.
- Kontrast (gerechnet):

| Paar | Kobalt dunkel | Kobalt hell | Papier dunkel | Papier hell |
|---|---|---|---|---|
| Meta `--km-color-text-dim` auf `--km-color-section` | 6,66 | 5,16 | 6,26 | 5,86 |
| Einleitung `--km-color-text-muted` auf `--km-color-section` | 8,41 | 6,69 | 9,27 | 7,32 |
| Icon `--km-color-accent` auf `--km-color-inset` | 7,52 | 6,14 | 7,43 | 7,42 |
| Zähler `--km-color-text-muted` auf `--km-color-track` | 6,16 | 6,00 | 6,77 | 6,17 |
| Rand `--km-color-border-section` auf `--km-color-page` | 2,16 | 1,55 | 2,00 | 1,47 |
| Hervorhebung: Rand `--km-color-highlight` gegen Seite, Bereich, Karte und `--km-color-highlight-bg` (kleinster Wert) | 3,13 | 3,11 | 3,12 | 3,12 |
| Hervorhebung: Text auf `--km-color-highlight-bg` | 12,88 | 14,19 | 12,06 | 16,15 |

- Der Rand des Bereichs grenzt eine Fläche ab, er ist kein Bedienelement; die Fläche selbst unterscheidet sich vom Seitenhintergrund.
- Der Rand der Hervorhebung ist bewusst dezent (Theme-Kommentar „zu krass“); die Hervorhebung trägt sich über den eigenen Titel.

- Schmal (390 px): Titel bricht unter 40rem um, Werkzeuge rutschen in die nächste Zeile.

## Beispiele

### Richtig

```html
<details class="km-section" open>
  <summary class="km-section__head"><span class="km-section__icon">…</span><h2 class="km-section__title">Aufgaben</h2><span class="km-section__count">12</span></summary>
  <div class="km-section__body"><div class="km-cards">…</div></div>
</details>
```

### Falsch

```html
<!-- Bereich mit Akzentstrich und eigenem Innenabstand -->
<section class="km-section km-card--accent-left" style="padding:20px">…</section>
<!-- Bereich im Bereich -->
<div class="km-section__body"><details class="km-section">…</details></div>
```

Warum: Farbstrich nur an der innersten Karte (Entscheidung 25), Abstände nur über Rollen (Entscheidung 12), Bereiche verschachteln nicht.

## Seitenregeln

Aus `docs/seitenregeln.md`: Navi wie Inhalt (jeder Bereich ein Eintrag der Seitenleiste); Filter öffnet, was er zeigt; Bereichsklick setzt Filter zurück; keine harten Werte, nur Abstandsrollen; Farbkanten als Innenschatten; Farbstrich nur an der innersten Karte; Tabellen nicht verstecken, darüber `km-subhead` mit Icon und Anzahl.

Entscheidungen: 12 (Abstände als Rollen), 18 (Ausrichtung, Kanten, Überlappung), 21 (Seitenleiste folgt dem Inhalt), 25 (Karten), 27 (schmale Breite).

## Vergleich mit anderen Design-Systemen

| System | Name | Besonderheit | Quelle |
|---|---|---|---|
| KERN 2.8.2 | Accordion | ungeprüft | – |
| GOV.UK Design System | Accordion | ungeprüft | – |

## Verwandte Bausteine

`km-card`, `km-cards`, `km-note`, `km-sidebar`, `km-count`, `km-caret`, `km-iconbtn--label`, `km-table`.

## Tokens

Rollen: `--km-color-section`, `--km-color-border-section`, `--km-color-inset`, `--km-color-track`, `--km-color-border-card`, `--km-color-text`, `--km-color-text-muted`, `--km-color-text-dim`, `--km-color-accent`, `--km-color-highlight`, `--km-color-highlight-bg`, `--km-space-page`, `--km-space-section-x`, `--km-space-section-y`, `--km-space-block`, `--km-space-group`, `--km-space-stack`, `--km-font-display`, `--km-font-size-l`, `--km-control-height`, `--km-icon-tile`.

- Komponenten-Haken: `--chip-color` (Filter-Chip), `--org-color` (Kartengruppe), beide ohne `--km-`-Präfix.
- Hart im Baustein: Icon-Kachel `2rem` (`.km-section__icon`, auch im Versatz von `__head--wrapped`), `z-index: 6` am Griff, `z-index: 200` am Hinweis.

## Offene Punkte

- Haken `--chip-color` und `--org-color` ohne Präfix; nach `tokens-ebenen.md` sollten sie `--km-section-chip-color` bzw. `--km-cardgroup-color` heißen.
- Icon-Kachel 2rem statt `--km-icon-tile` (2.25rem wie in der Karte): zwei Kachelgrößen im System.

## Regeln

- Was: `km-section` ist die Wanne um jeden Abschnitt einer Werkzeugseite, meist als `<details>` mit Kopf aus Icon, Titel, Zähler und Werkzeugen im `<summary>`; darin gliedern `km-subhead` und `km-cardgroup`, `km-focus` zeigt angeheftete Einträge, `km-section__body--stack` stapelt gleichrangige Blöcke.
- Wann: Für Abschnitte, die in der Seitenleiste als Sprungziel stehen und zuklappbar sind, sowie für angeheftete Einträge; für eine Kartengruppe im Bereich `km-subhead` oder `km-cardgroup`, für aufklappenden Fließtext `<details>` mit `km-details__body`, und Bereiche verschachteln nie.
- Wie: `<details class="km-section" open>` mit `summary.km-section__head`, Überschrift `km-section__title` (ein bis zwei Wörter, Substantiv) und `km-section__body`; Abstände nur über Rollen, kein Akzentstrich am Bereich (der Farbstrich gehört an die innerste Karte), Einleitung in ein bis zwei Sätzen.
- Prüfen: Fertig ist es, wenn der Bereich per Enter und Leertaste auf- und zuklappt, ein Knopf in den Werkzeugen den Bereich nicht zuklappt, der Fokus am Kopf als Ring sichtbar ist ohne abgeblendet zu werden, Meta und Einleitung den gerechneten Kontrast halten (mindestens 5,16) und bei 390 px die Werkzeuge in die nächste Zeile rutschen.
