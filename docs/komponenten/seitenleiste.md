# Seitenleiste (`km-sidebar`)

Status: stabil, in Dashboard und Lagebild im Einsatz · Story: `docs/index.html#seitenleiste`, `#sidebar-hierarchie`, `#sidebar-rail` · CSS: `src/km-components.css`, Abschnitte „Seitenleiste“, „Seitenleiste nach Inhalts-Hierarchie“, „Eingeklappt“ · Stand: 2026-11-09

## Kurzbeschreibung

Die Seitenleiste ist die Navigation einer Werkzeugseite am linken Rand. Sie spiegelt den Aufbau der Seite: je Spalte eine Gruppe, darunter die Bereiche, eingerückt das, was im Inhalt unter einem Bereich liegt, etwa Filter nach Kunde, Typ und Phase mit Zählern. Gruppen und Einträge mit Unterebene klappen auf und zu, ausblendbare Bereiche haben ihren Schalter im selben Eintrag. Eingeklappt zeigt die Leiste nur noch die Icons der obersten Einträge. Gewählt wird über Farbe, Strich und Tönung; nichts verschiebt sich beim Wählen.

## Name und Abgrenzung

- Klasse `km-sidebar`; in der Oberfläche ohne eigene Überschrift.
- Achtung Begriff: Die rechte Spalte einer Seite heißt in den Seitenregeln „Sidebar“; die Navigation links ist die Seitenleiste.
- Zum Baustein gehören Gruppen, Überschriften, Einträge, Icons, Farbpunkte, Zähler, Schalter im Eintrag, Unterebenen, Klapp-Pfeile, Einklapp-Knopf und die eingeklappte Icon-Leiste (`--rail`).
- Nicht dazu gehören das Seitengerüst (Breite, Lage, Kopfzeile mit Logo) und das Verhalten (Springen, Filtern, Zustand speichern).
- KERN „Sidebar“ (seitlicher Bereich für Navigation oder ergänzende Inhalte) und „Nav“ sind laut KERN in Bearbeitung bzw. für Bereichswechsel gedacht; `km-sidebar` ist dichter und trägt Filter.
- Das Segmented Control (`km-segmented`) schaltet Ansichten innerhalb eines Bereichs; die Seitenleiste springt zu Bereichen und setzt seitenweite Filter.

## Einsatz

### Verwenden, wenn

- eine Werkzeugseite mehrere Bereiche und Spalten hat, zwischen denen man springt;
- seitenweite Filter (Kunde, Typ, Phase) mit Zählern angeboten werden;
- Bereiche ein- und ausgeblendet werden können.

### Nicht verwenden, wenn

- die Seite nur einen Bereich hat oder linear gelesen wird (Artikel, Guide): Inhaltsverzeichnis;
- zwischen Ansichten derselben Daten gewechselt wird: Segmented Control;
- eine zweite Liste nur mit Schaltern entstehen würde: Schalter gehören in den Eintrag.

## Verwendung

```html
<nav class="km-sidebar" aria-label="Seitennavigation">
  <div class="km-sidebar__group">
    <p class="km-sidebar__label"><button type="button" class="km-sidebar__label-btn" aria-expanded="true" aria-controls="nav-inhalt">Inhalt<span class="km-sidebar__caret" aria-hidden="true"></span></button></p>
    <div class="km-sidebar__list" id="nav-inhalt">
      <div class="km-sidebar__branch">
        <div class="km-sidebar__row">
          <a class="km-sidebar__item" href="#uebersicht" aria-current="location" title="Übersicht"><svg class="km-icon km-sidebar__icon" aria-hidden="true">…</svg>Übersicht</a>
          <button type="button" class="km-sidebar__branch-toggle" aria-expanded="true" aria-controls="nav-uebersicht" aria-label="Unterebene von Übersicht ein- oder ausklappen"><span class="km-sidebar__caret" aria-hidden="true"></span></button>
        </div>
        <div class="km-sidebar__nest" id="nav-uebersicht">
          <p class="km-sidebar__label">Kunden</p>
          <button type="button" class="km-sidebar__item" aria-pressed="true">Alle<span class="km-sidebar__count">12</span></button>
          <button type="button" class="km-sidebar__item" style="--km-item-color:var(--km-color-tool-code)"><span class="km-sidebar__dot"></span>Kunde A<span class="km-sidebar__count">7</span></button>
        </div>
      </div>
      <div class="km-sidebar__row">
        <a class="km-sidebar__item" href="#aufgaben" title="Aufgaben"><svg class="km-icon km-sidebar__icon" aria-hidden="true">…</svg>Aufgaben</a>
        <button type="button" class="km-switch" role="switch" aria-checked="true" aria-label="Aufgaben anzeigen"><span class="km-switch__knob" aria-hidden="true"></span></button>
      </div>
    </div>
  </div>
</nav>
```

## Aufbau

| Teil | Klasse | Funktion |
|---|---|---|
| Leiste | `km-sidebar` | Spalte mit Gruppen im Abstand `--km-space-l`, Schrift `--km-font-size-s`; setzt `--km-sidebar-inset` (Auswahlstrich plus Innenabstand). |
| Gruppe | `km-sidebar__group` | eine Spalte der Seite. |
| Überschrift | `km-sidebar__label`, `km-sidebar__label-btn` | Versalien, gedämpft, mit kleinem Icon; als Knopf klappbar (`aria-expanded`). |
| Inhalt der Gruppe | `km-sidebar__list` | zu = `hidden`. |
| Eintrag | `km-sidebar__item` | Knopf oder Link, einzeilig, Strich links reserviert; fluchtet mit Überschrift und Logo, der Strich steht davor. |
| Icon | `km-sidebar__icon` | Lucide in `--km-icon-s`, Farbe `--km-item-color` oder gedämpft. Pflicht an obersten Einträgen. |
| Farbpunkt | `km-sidebar__dot` | quadratisch, Farbe `--km-item-color`. |
| Zähler | `km-sidebar__count` | rechts im Eintrag, gedämpft; im gewählten Eintrag in dessen Farbe. |
| Schalter als Eintrag | `km-sidebar__item[role="switch"]` mit `km-switch__knob` | Filter zum Ein- und Ausschalten. |
| Eintrag mit Schalter | `km-sidebar__row` + `km-switch` | Bereich anzeigen oder ausblenden, Schalter rechts, Name per `aria-label`. |
| Eintrag mit Unterebene | `km-sidebar__branch`, `km-sidebar__nest`, `km-sidebar__branch-toggle` | Unterebene eingerückt mit Linie; Klapp-Pfeil direkt hinter dem Text im Abstand `--km-space-xs`; zu = `hidden` am Nest. |
| Einklapp-Knopf | `km-sidebar__toggle` | Quadrat `--km-sidebar-toggle-size`, Pfeil dreht sich. |

## Varianten

- **Ausgeklappt** (Standard), Breite `--km-sidebar-w` (17.5rem), mindestens `--km-sidebar-min-w`.
- **Eingeklappt** `km-sidebar--rail`: nur die Icons der obersten Einträge als Quadrate in `--km-sidebar-toggle-size`, in einer Achse mit dem Ausklapp-Knopf und der Mitte des Logo-Icons; Überschriften, Unterebenen, Zähler, Schalter und Klapp-Pfeile ausgeblendet.
- Breite `--km-sidebar-rail-w`.
- **Filtergruppe** `km-sidebar__group--filter`: eigene Gruppe „Filter“ oberhalb der Bereiche, wenn die Filter auf mehrere Bereiche wirken. Zwischen-Labels (Status, Kunden, Typen, Phase, Pflege) beginnen beim ersten Textzeichen von „Filter“, ihre Einträge beim ersten Textzeichen ihres Labels (DDR 47, rekursiv); jede Liste trägt `km-sidebar__list`. Eingeklappt entfällt die Gruppe.

## Größen

Eine Größe je Variante.

## Zustände

| Zustand | Auslöser | Darstellung | Tokens |
|---|---|---|---|
| Ruhe | – | Text voll, Icon gedämpft oder in Eintragsfarbe | `--km-color-text`, `--km-item-color` |
| Hover | `:hover` | 8 % Akzent auf der Bereichsfläche | `--km-color-accent`, `--km-color-section` |
| Gewählt / aktuell | `aria-pressed="true"` oder `aria-current` | Akzent-Text, Strich links, 16 % Tönung; nicht fett | `--km-color-accent`, `--km-border-width-strong` |
| Fokus | `:focus-visible` | Doppelring außen | `--km-color-focus` |
| Deaktiviert | `aria-disabled="true"` | auf 40 % abgeblendet, keine Hover-Wirkung, nicht klickbar | `--km-opacity-disabled` |
| Schalter an / aus | `role="switch"`, `aria-checked` | Knopf gefüllt im Akzent bzw. leer | `--km-color-accent`, `--km-color-on-accent` |
| Bereich ausgeblendet | Schalter aus, Sprung `aria-disabled` | Eintrag abgeblendet | `--km-opacity-disabled` |
| Gruppe / Unterebene offen | `aria-expanded="true"` | Pfeil nach unten | `--km-caret-mask` |
| Gruppe / Unterebene zu | `aria-expanded="false"`, `hidden` am Inhalt | Pfeil nach rechts, Inhalt weg | – |
| Eingeklappt | `km-sidebar--rail` | nur Icons, Name als `title` und für Screenreader im Eintrag | `--km-sidebar-toggle-size`, `--km-icon-l` |
| Langer Name | Überlänge | einzeilig mit „…“, voller Name im `title` | – |

## Verhalten

- Sprung zum Bereich, Filter setzen, Klappen und Ein-/Ausblenden setzt das Skript der Seite; Klappzustand in localStorage.
- Filter der Navigation schließen sich aus (Kunde, Typ, Phase, Schutz); eine neue Wahl hebt einen gesetzten Listenfilter auf; jede Wahl ist ein Schritt im Verlauf.
- Ein Filter öffnet, was er zeigt; „Alle“ je Gruppe mit Zähler; Zähler folgen den anderen Filtern.
- Logo setzt Filter, Suche, Sortierung und Klappen zurück.
- Eingeklappt springt ein Klick wie ausgeklappt.

## Text und Wording

- Einträge: ein bis zwei Wörter; die Breite ist fest (17.5rem, breitester gemessener Fall 271 px), längere Namen enden mit „…“.
- Gruppenüberschriften: ein Wort in Versalien („Inhalt“, „Sidebar“, „Kunden“).
- Reihenfolge der Filtergruppen: Kunden, Typen, dann weitere (Phase, Schutz, Pflege).

## Barrierefreiheit

- Rolle: `nav` mit `aria-label`.
- Sprünge zu Bereichen besser als Links mit `aria-current="location"` (aktueller Abschnitt), Filter als Knöpfe mit `aria-pressed`, Schalter `role="switch"` mit `aria-checked`.
- Klappknöpfe mit `aria-expanded` und `aria-controls` (WAI-ARIA APG Disclosure, Beispiel „Disclosure Navigation Menu“).
- Struktur: Die Story setzt Einträge als Folge von Knöpfen in `div`; Listen (`ul`/`li`) würden Screenreadern Anzahl und Lage mitteilen.
- Überschriften sind `p`, keine Überschriften-Elemente.
- Tastatur: alle Teile native Knöpfe und Links, Tab-Folge von oben nach unten, Enter und Leertaste.
- Eingeklappt bleiben nur die obersten Einträge fokussierbar; ausgeblendete Teile sind `display: none` und damit nicht im Fokus.
- Eingeklappt: Der Name bleibt als Text im Eintrag (Schriftgröße 0) und als `title`; Screenreader lesen ihn.
- Fokus: Doppelring außen.
- Gewählt nicht nur über Farbe: Strich links und Tönung zusätzlich zur Akzentfarbe; `aria-pressed` bzw. `aria-current`.
- Kontrast (gerechnet; Tönung auf `--km-color-section`):

| Paar | Kobalt dunkel | Kobalt hell | Papier dunkel | Papier hell |
|---|---|---|---|---|
| Gewählt: `--km-color-accent` auf 16 % Tönung | 6,44 | 4,53 | 6,36 | 5,79 |
| Hover: `--km-color-text` auf 8 % Tönung | 13,05 | 12,14 | 12,26 | 14,49 |
| Überschrift `--km-color-text-dim` auf `--km-color-section` | 6,66 | 5,16 | 6,26 | 5,86 |

- Kobalt hell erreicht im gewählten Eintrag knapp 4,5.
- Der Kommentar im CSS nennt „dunkel 6,2, hell 4,9“; die Rechnung hier (WCAG-Formel, sRGB-Mischung auf `--km-color-section`) ergibt 6,44 und 4,53.
- Der Unterschied kommt vermutlich von einer anderen Grundfläche; nachmessen.

## Beispiele

### Richtig

Oberste Einträge mit Icon und `title`, Unterebene in `km-sidebar__nest`, Schalter im Eintrag (`km-sidebar__row`), gewählt mit `aria-current` bzw. `aria-pressed`.

### Falsch

```html
<button class="km-sidebar__item" style="font-weight:700" aria-pressed="true">Projektübersicht</button>  <!-- fett: Eintrag springt -->
<div class="km-sidebar__group"><p class="km-sidebar__label">Anzeigen</p>…nur Schalter…</div>           <!-- zweite Liste nur mit Schaltern -->
<button class="km-sidebar__item">Weitere Server</button>                                               <!-- oberster Eintrag ohne Icon: eingeklappt leer -->
```

## Seitenregeln

Aus `docs/seitenregeln.md`, „Navigation (Seitenleiste)“ und „Seitenrahmen gleich“: Navi wie Inhalt; alles klappbar, auch die erste Ebene; Klapp-Pfeil direkt hinter dem Text; Schalter im Eintrag; Reihenfolge der Filtergruppen; eine Linie mit dem Logo, Auswahlstrich davor; eingeklappt nur Icons, jeder oberste Eintrag mit Icon und `title`; nichts springt beim Wählen; erster Eintrag endet vor dem Einklapp-Knopf; Maße nur über `--km-sidebar-*`, `--km-monogram-size`, `--km-header-control-height`; keine Überlappungen, auch nicht im Randfall.

## Vergleich mit anderen Design-Systemen

| System | Name | Besonderheit | Quelle |
|---|---|---|---|
| Primer (GitHub) | NavList | senkrechte Liste von Navigationslinks; Gruppen mit Titel; Unterebenen per `SubNav`, nur oberste Einträge klappen und sind dann keine Links; höchstens vier Ebenen; `aria-current="page"` bzw. `"location"`; Zähler als Trailing Visual | primer.style/product/components/nav-list |
| Carbon | UI Shell, Left panel | sekundäre Navigation fest am linken Rand; Links und Untermenüs gemischt; höchstens zwei Ebenen („does not support three tiers“); empfohlen ab mehr als fünf Punkten | carbondesignsystem.com/components/UI-shell-left-panel/usage |
| GOV.UK Design System | Service navigation | Navigation innerhalb eines Dienstes, aktiver Punkt mit `aria-current`; keine Seitenleisten-Komponente | design-system.service.gov.uk/components/service-navigation |
| KERN 2.8.2 | Sidebar, Nav | Sidebar „derzeit noch in Bearbeitung“ | kern-ux.de/komponenten/sidebar |

Besonders an `km-sidebar`: Filter mit Zählern und Schalter zum Ausblenden von Bereichen in derselben Leiste; Primer und Carbon trennen Navigation und Filter.

## Verwandte Bausteine

`km-switch`, `km-header` (Kopfzeile mit Logo), `km-count`, `km-dot`, `km-caret`, `km-segmented`.

## Tokens

Rollen: `--km-color-text`, `--km-color-text-dim`, `--km-color-accent`, `--km-color-on-accent`, `--km-color-section`, `--km-color-border-card`, `--km-color-border-section`, `--km-color-focus`, `--km-font-size-xs`, `--km-font-size-s`, `--km-tracking-caps`, `--km-space-3xs` bis `--km-space-l`, `--km-border-width`, `--km-border-width-strong`, `--km-icon-xs`, `--km-icon-s`, `--km-icon-l`, `--km-opacity-disabled`, `--km-caret-mask`.

Komponenten-Tokens: `--km-sidebar-toggle-size` (1.9rem), `--km-sidebar-rail-w` (2.6rem), `--km-sidebar-min-w` (14.375rem), `--km-sidebar-w` (17.5rem), alle in `src/km-roles.css`; `--km-sidebar-inset` und `--km-rail-versatz` (berechnet, im Baustein); `--km-item-color` (Haken für Icon- und Punktfarbe, ohne Standardwert in den Rollen).

Hart im Baustein: Tönungen `8%` (Hover) und `16%` (gewählt), Dauer `0.15s` des Einklapp-Pfeils.

## Offene Punkte

- Kontrastwert im CSS-Kommentar (hell 4,9) weicht von der Rechnung (4,53) ab.
- Listen-Semantik (`ul`/`li`) und Überschriften-Elemente fehlen im Markup der Stories.
- Knöpfe statt Links für Sprünge zu Bereichen in den Stories; Empfehlung: Links mit `aria-current="location"`.
- `--km-sidebar-*` stehen in den Rollen (`km-roles.css`), sind aber Komponenten-Tokens; siehe eine Analyse.

## Regeln

- Was: Die Seitenleiste `km-sidebar` ist die Navigation einer Werkzeugseite am linken Rand mit Gruppen, Einträgen, Unterebenen, Zählern und Schaltern im Eintrag, ausgeklappt (Standard) oder eingeklappt mit `km-sidebar--rail` als reine Icon-Leiste; `km-sidebar__group--filter` ist die eigene Gruppe „Filter“ oberhalb der Bereiche.
- Wann: Nur bei Werkzeugseiten mit mehreren Bereichen, seitenweiten Filtern mit Zählern oder ausblendbaren Bereichen; bei einem Bereich oder linearem Lesen ein Inhaltsverzeichnis, für Ansichten derselben Daten `km-segmented`, und eine zweite Liste nur mit Schaltern gibt es nicht, Schalter gehören in den Eintrag.
- Wie: `nav` mit `aria-label`, Sprünge als Links mit `aria-current="location"`, Filter als Knöpfe mit `aria-pressed`, Schalter als `km-switch` mit `role="switch"` und `aria-checked`, Klappknöpfe mit `aria-expanded` und `aria-controls`, Unterebenen in `km-sidebar__nest`, oberste Einträge mit Icon und `title`, Maße nur über `--km-sidebar-*`.
- Prüfen: Fertig ist es, wenn der gewählte Eintrag über Strich und Tönung erkennbar ist und sich nichts verschiebt (nicht fett), Fokus als Doppelring sichtbar und der Eintrag bedienbar bleibt, der gewählte Text in allen Themes mindestens 4,5:1 misst, lange Namen mit „…“ enden und eingeklappt jeder oberste Eintrag Icon und `title` hat.
