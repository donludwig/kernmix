# Tabelle (`km-table`)

Status: stabil, in Dashboard und Lagebild im Einsatz · Story: `docs/index.html#tabelle`, `#tabelle-spalten`, `#tabelle-regeln`, `#unterzeilen`, `#zahlenliste` · CSS: `src/km-components.css`, Abschnitte „Tabelle im Bereich“, „Tabellenspalten“, „Laufende Nummer“, „Weiter-Verlauf“, „Tabellen einheitlich“ · Stand: 2026-11-09

## Kurzbeschreibung

Die Tabelle zeigt eine Liste gleichartiger Dinge (Projekte, Dateien, Hosts) in Zeilen und Spalten zum Vergleichen und Wiederfinden. Sie liegt immer in einem Rahmen, der quer scrollt, statt Spalten zu quetschen. Die Breite jeder Spalte ergibt sich aus ihrer Rolle: Name, Kennung, Wert, Zahl, Fließtext, Aktionen. Werte brechen nie um, alle Zeilen sind gleich hoch, Zellen beginnen oben. Gruppenzeilen fassen Zeilen zusammen und lassen sich zuklappen, Unterzeilen hängen an ihrer Elternzeile. Aktionen stehen immer in der letzten Spalte und bleiben beim Scrollen rechts stehen.

## Name und Abgrenzung

- Klasse `km-table` im Rahmen `km-table-wrap`; in der Oberfläche „Tabelle“ bzw. der Name der Liste („Projektübersicht“).
- Zum Baustein gehören Rahmen, Kopf, Zeilen, Spaltenrollen, Gruppen- und Unterzeilen, laufende Nummer, Aktionsspalte und der Verlauf am rechten Rand.
- Nicht dazu gehören Sortieren, Filtern, Zuklappen und Spaltenauswahl als Verhalten: Das CSS zeigt die Zustände, das Skript der Seite setzt sie.
- Spaltenauswahl (`km-colpicker`), Zwischenüberschrift (`km-subhead`) und Suchfeld sind eigene Bausteine, die mit der Tabelle auftreten.
- Gegenüber der KERN-Tabelle (`kern-table`): `km-table` ist dichter (Schrift 14 px statt Standardgröße), hat Spaltenrollen, Gruppen- und Unterzeilen, Monogramm und eine feste Aktionsspalte.
- Für einfache Inhaltstabellen in Fließtext reicht `kern-table`.
- Kennzahlen in kleinen Tabellen nebeneinander: Raster `km-tables` (Story `#zahlenliste`), ebenfalls mit `km-table`.

## Einsatz

### Verwenden, wenn

- eine Menge gleichartiger Dinge mit denselben Merkmalen gezeigt wird (jede Liste von Projekten, Dateien, Hosts ist diese Tabelle);
- Werte über Zeilen hinweg verglichen oder sortiert werden;
- Zeilen Aktionen haben (Kopieren, Öffnen, Markieren).

### Nicht verwenden, wenn

- Inhalte vor allem Text sind: dann Info-Karten im Raster (`km-card--info`);
- es nur um Layout geht (Spalten nebeneinander): dann Raster;
- eine abgespeckte Eigen-Tabelle für denselben Inhalt entstehen würde: Listen von Dingen sehen überall gleich aus;
- die Tabelle hinter einer Aufklapp-Zeile („… anzeigen“) versteckt wäre: Tabellen sind immer offen, darüber eine Zwischenüberschrift mit Icon und Anzahl.

## Verwendung

```html
<h3 class="km-subhead" id="t-projekte"><svg class="km-icon" …></svg>Projekte <span>3</span></h3>
<div class="km-table-wrap">
  <table class="km-table km-table--numbered" aria-labelledby="t-projekte">
    <thead><tr>
      <th class="km-table__sort" aria-sort="ascending"><svg class="km-icon" aria-hidden="true">…</svg>Projekt</th>
      <th><svg class="km-icon" aria-hidden="true">…</svg>Phase</th>
      <th class="km-table__num">Dateien</th>
      <th class="km-table__actions"><span class="kern-sr-only">Aktionen</span></th>
    </tr></thead>
    <tbody>
      <tr>
        <td class="km-table__nowrap"><a class="km-table__name" href="#p1"><span class="km-monogram" style="--km-monogram-color:var(--km-color-accent)">P1</span>Projekt 1</a></td>
        <td class="km-table__nowrap"><span class="km-pill km-pill--aktiv">Aktiv</span></td>
        <td class="km-table__num">12</td>
        <td class="km-table__actions"><span class="km-table__actions-row"><button type="button" class="km-iconbtn" aria-label="Link kopieren">…</button></span></td>
      </tr>
    </tbody>
  </table>
</div>
```

## Aufbau

| Teil | Klasse | Funktion |
|---|---|---|
| Rahmen | `km-table-wrap` | Kartenfläche mit Rand, scrollt quer; Bezugspunkt für absolut gesetzte Teile. Jede Tabelle steht in einem Rahmen. |
| Tabelle | `km-table` | `table-layout: auto`, volle Breite, Schrift `--km-font-size-s`, Zellen oben ausgerichtet. |
| Kopfzelle | `th`, darin `.km-icon` | Versalien, gedämpft, bricht nicht um; jede Spalte mit kleinem Icon vor dem Namen. |
| Sortierbare Spalte | `km-table__sort` + `aria-sort` | Flaches Dreieck hinter dem Namen (`--km-sort-w`, `--km-sort-h`). |
| Name | `km-table__name` | Erste Spalte: Textschrift, kräftig, einzeilig mit „…“ ab 22rem, voller Name im `title`. Mit Monogramm (`km-monogram`) oder Favicon davor. |
| Typ neben dem Namen | `km-table__tool` | Schmale Spalte rechts in der Namenszelle (Punkt in `--km-dot-color` oder Icon), im Kopf als Knopf, der nach Typ sortiert. |
| Kennung | `km-table__key` | Mono, kräftig, nie umbrechen: Pfad als Wert, Ticket-Kennung, Demo-Link. |
| Wert | `km-table__nowrap` | Kurzer Wert, Pill, Datum; so schmal wie der Inhalt. |
| Zahl | `km-table__num` | Rechtsbündig, gleich breite Ziffern. |
| Datum | `km-table__date`, `__date-rel`, `__activity` | Datum, relative Angabe und Aktivitätsbalken in einer Zeile. |
| Stunden, Umfang | `km-table__hours`, `km-table__scope` | Mono rechtsbündig bzw. Umfang mit Balken. |
| Fließtext | `km-table__text`, `km-table__text--wide` | Bricht um, 22rem bzw. ab 26rem. Bekommt den restlichen Platz. |
| Aktionen | `km-table__actions`, `km-table__actions-row` | Immer letzte Spalte, Knöpfe `km-iconbtn` als ein Block, klebt rechts. Kopfzelle zeigt nur Icon oder `kern-sr-only`. |
| Gruppenzeile | `km-table__group`, `__group-label`, `__group-count`, `__toggle` | Ganze Breite (`colspan`), Fläche `--km-color-inset`, Farbkante links als Innenschatten in `--km-row-color`, Pfeil und Anzahl. |
| Unterzeile | `km-table__row--sub`, `--sub-2` | Zeile unter ihrer Elternzeile, Name mit Einrückungswinkel. |
| Laufende Nummer | `km-table--numbered` | Zähler vor der ersten Zelle, mittig zur ersten Zeile bzw. zum Monogramm; Gruppenzeilen und ausgeblendete Zeilen zählen nicht. |

## Varianten

- **Standard** für alle inhaltlichen Tabellen.
- **Kompakt** `km-table--compact`: geringerer Zeilenabstand, nur für lange Dokumentlisten.
- **Nummeriert** `km-table--numbered`: jede Liste von Dingen (Projekte, Dateien, Hosts).
- **Gruppenzeile ohne Farbkante** `km-table__group--plain`: nicht klappbar, ohne Kante.

## Größen

Eine Größe. Abstände: Kopf `--km-space-xs` / `--km-space-m`, Zelle `--km-space-s` / `--km-space-m`, erste und letzte Spalte außen `--km-space-l`.

## Zustände

| Zustand | Auslöser | Darstellung | Tokens |
|---|---|---|---|
| Ruhe | – | Zeilen mit Linie unten | `--km-color-border-card` |
| Zeile überfahren | `tr:hover` | ganze Zeile, auch die Aktionszelle, auf `--km-color-inset` | `--km-color-inset` |
| Sortiert auf- oder absteigend | `aria-sort="ascending"` / `"descending"` am `th` | Dreieck nach oben bzw. unten | `--km-sort-w`, `--km-sort-h` |
| Unsortiert | `aria-sort="none"` | kein Dreieck, Kopf bei Hover heller | `--km-color-text-muted` |
| Gruppe offen | `km-table__group` | Pfeil nach unten | `--km-caret-mask`, `--km-icon-2xs` |
| Gruppe zu | `km-table__group--collapsed` | Pfeil nach rechts; Zeilen darunter blendet die Seite aus | – |
| Ausgeblendete Zeile | `display: none` bzw. `hidden` | zählt nicht in der Nummer | – |
| Läuft rechts über | `km-scroll--more` am Rahmen (setzt die Seite) | Verlauf links an der Aktionsspalte, Inhalt verschwindet darunter | `--km-color-card`, `--km-color-inset` |
| Name überfahren | `a.km-table__name:hover` | Unterstreichung | `--km-underline-offset` |
| Name besucht | `:visited` | bleibt Textfarbe | `--km-color-text` |
| Leere Zelle | Strich als Inhalt | gedämpft | `--km-color-text-dim` |
| Status | `km-pill--ok`, `--warn`, `--danger`, `--neutral`, Phasen-Pills | Etikett; leer heißt „ohne Wert“, nicht „ok“ | Rückmeldefarben |
| Aktion gedrückt | `km-iconbtn[aria-pressed="true"]` | gefüllt im Akzent bzw. Signalfarbe (`--attention`) | `--km-color-accent`, `--km-color-attention` |
| Leer (keine Zeilen) | – | kein eigener Zustand im Baustein | offen |

## Verhalten

- Breite: keine festen Breiten in der Seite.
- `__key`, `__nowrap`, `__num` sind so schmal wie ihr Inhalt (`width: 1%`), Fließtext bekommt den Rest.
- Reicht der Platz nicht, scrollt der Rahmen quer.
- Die Aktionsspalte bleibt beim Querscrollen stehen (`position: sticky` über `km-table__actions:last-child`).
- Den Verlauf schaltet die Seite mit `km-scroll--more`, solange rechts noch Inhalt kommt.
- Sortieren, Zuklappen, Filtern und Spaltenwahl setzt das Skript der Seite über `aria-sort`, `km-table__group--collapsed`, `hidden`.
- Unterzeilen bleiben beim Sortieren unter ihrer Elternzeile; eine Filterwahl schaltet die Spaltensortierung ab.
- Spalten, die für keinen sichtbaren Zeilentyp gelten, blendet die Seite aus.
- Kopier-Knöpfe lesen ihren Wert erst beim Klick aus der Zeile.

## Text und Wording

- Spaltenköpfe: ein Wort, höchstens etwa 12 Zeichen (Versalien mit Sperrung brauchen Platz; „WERKZEUG“ mit Pfeil misst rund 7rem).
- Namen: höchstens 22rem, darüber „…“ und voller Name im `title`.
- Gruppenzeile: Name und Anzahl („Kunde A · 3 Projekte“).
- Status-Etiketten: ein Wort.

## Barrierefreiheit

- Rollen: natives `table`, `thead`, `tbody`, `th`.
- Spaltenköpfe sollten `scope="col"` tragen, Namen in der ersten Spalte als Zeilenkopf `th scope="row"` sind möglich (Klasse für Zeilenkopf vorhanden).
- Name der Tabelle über `aria-labelledby` auf die Zwischenüberschrift, da der Baustein kein `caption` nutzt.
- Aktionsspalte: Kopf mit `kern-sr-only`-Text „Aktionen“; jeder Icon-Knopf mit `aria-label`, das den Bezug zur Zeile herstellt (z. B. „Link von Projekt 1 kopieren“) oder per `aria-describedby` auf den Namen verweist.
- Tastatur: Sortierbare Köpfe und klappbare Gruppenzeilen sind im Kit-Markup reine Zellen ohne Knopf; ohne Knopf im `th` bzw. in der Gruppenzelle sind sie per Tastatur nicht erreichbar (siehe offene Punkte).
- Der quer scrollende Rahmen braucht `tabindex="0"` und einen Namen, damit er per Tastatur scrollbar ist.
- Fokus: Doppelring außen über `--km-color-focus`, `--km-border-width-strong`, `--km-focus-offset`.
- Information nicht nur über Farbe: Farbkante der Gruppe, Werkzeugpunkt und Monogramm sind Zusatz; Gruppenname und Typ stehen als Text daneben.
- Kontrast (gerechnet, WCAG-Formel):

| Paar | Kobalt dunkel | Kobalt hell | Papier dunkel | Papier hell |
|---|---|---|---|---|
| Kopf und Zähler `--km-color-text-dim` auf `--km-color-card` | 6,25 | 6,05 | 5,78 | 6,23 |
| `--km-color-text-dim` auf `--km-color-inset` (Gruppenzeile, Hover) | 5,68 | 5,55 | 5,35 | 5,71 |
| `--km-color-text` auf `--km-color-inset` | 12,88 | 14,57 | 12,06 | 16,15 |
| Zeilenlinie `--km-color-border-card` auf `--km-color-card` | 1,42 | 1,39 | 1,27 | 1,32 |

Die Zeilenlinie liegt unter 3:1; sie trennt nur und trägt keine Information (WCAG 1.4.11 verlangt 3:1 nur für Grafik, die zum Verstehen nötig ist).

- Schmal (390 px): Seite ohne waagerechte Scrollleiste, Tabelle scrollt im Rahmen.

## Beispiele

### Richtig

```js
window.kmTabelle(document.querySelector('#hosts'), { nummern: true, sortieren: true });
```

```html
<tr class="km-table__row--sub"><td class="km-table__nowrap"><a class="km-table__name" href="#">Navigation</a></td><td class="km-table__nowrap">Prototyp</td><td class="km-table__actions"><span class="km-table__actions-row">…</span></td></tr>
```

### Falsch

```html
<td><a class="km-table__name">Host</a> <button class="km-iconbtn">…</button></td>     <!-- Aktion in der Namenszelle -->
<th>Aktionen</th><th>Datum</th>                                                     <!-- Aktionen nicht zuletzt -->
<details><summary>Tabelle anzeigen</summary><table class="km-table">…</table></details>  <!-- Tabelle versteckt, ohne km-table-wrap -->
<td class="km-table__key">beispiel.example</td>                                     <!-- Name der ersten Spalte als Kennung statt km-table__name -->
```

## Seitenregeln

- Aus `docs/seitenregeln.md`, Abschnitt „Tabellen“: eine Standard-Tabelle überall; Rolle je Spalte nach der Liste dort; Name zuerst, dann Werte, Fließtext, Datum, Aktionen; Aktionen immer ganz rechts, fest, mit Verlauf, nie in einer mittleren Spalte; Kopf-Icons in jeder Spalte; jede Tabelle im Rahmen; Tabellen nicht verstecken; kompakt nur für Dokumentlisten; Status als Etikett; Kopier-Knöpfe in die Aktionsspalte; bei Zugängen drei Knöpfe in fester Reihenfolge (Link, Passwort, Nachricht).
- Farbkanten nur als Innenschatten.

## Vergleich mit anderen Design-Systemen

| System | Name | Besonderheit | Quelle |
|---|---|---|---|
| KERN 2.8.2 | Table (`kern-table`) | Varianten Small, Striped, Footer, Responsive (Scroll-Hülle mit `tabindex="0"`); Aktions-Spalte `kern-table__cell--action` am rechten Rand mit Knöpfen in x-small, nur Secondary und Tertiary, per `aria-describedby` mit dem Zeilenkopf verknüpft; Zahlen rechtsbündig; „nicht interaktiv“ | kern-ux.de/komponenten/table |
| GOV.UK Design System | Table | Zahlen rechtsbündig (`govuk-table__header--numeric`), `caption` wie eine Überschrift, `scope` für Zeilen- und Spaltenköpfe; nie für Layout | design-system.service.gov.uk/components/table |
| Carbon | Data table | fünf Zeilenhöhen (xs bis xl), Werkzeugleiste mit höchstens fünf Aktionen, Batch-Aktionen sperren Zeilenaktionen, Überlaufmenü je Zeile, aufklappbare Zeilen, Sortierpfeil nur an der sortierten Spalte dauerhaft | carbondesignsystem.com/components/data-table/usage |

Unterschied zu allen drei: `km-table` hat Spaltenrollen statt fester Spaltenbreiten und eine klebende Aktionsspalte mit Verlauf; Carbons Lage der Zeilenaktionen (rechts) ist auf der Seite nicht ausdrücklich genannt.

## Verwandte Bausteine

Zwischenüberschrift `km-subhead`, Spaltenauswahl `km-colpicker`, Knopf mit Icon `km-iconbtn`, Pill `km-pill`, Monogramm `km-monogram`, Verdeckter Wert `km-secret`, Info-Karte `km-card--info`, Raster kleiner Tabellen `km-tables`.

## Tokens

Rollen, die der Baustein liest: `--km-color-card`, `--km-color-inset`, `--km-color-border-card`, `--km-color-text`, `--km-color-text-dim`, `--km-color-text-muted`, `--km-color-accent`, `--km-color-track`, `--km-font-size-xs`, `--km-font-size-s`, `--km-font-mono`, `--km-font-weight-medium`, `--km-font-weight-strong`, `--km-tracking-caps`, `--km-space-2xs` bis `--km-space-l`, `--km-border-width`, `--km-border-width-accent`, `--km-sort-w`, `--km-sort-h`, `--km-monogram-size`, `--km-icon-xs`, `--km-icon-2xs`, `--km-bar`, `--km-dot`, `--km-underline-offset`.

Komponenten-Tokens (Haken): `--km-row-color` (Farbkante der Gruppe), `--km-monogram-color`, `--km-dot-color` (Typ-Punkt), `--km-table-tool-w` (Breite der Typ-Spalte, 7.5rem), `--km-table-num-lh` (Zeilenhöhe der Nummer).

Harte Werte, die Token werden sollten (Zeilen in `src/km-components.css`): Namensbreite `max-width: 22rem` und `line-height: 1.25rem` (231, auch 1222 und 1267 rechnen mit 1.25rem), Fließtext `width: 22rem; min-width: 12rem` (803), breiter Fließtext `26rem`/`30rem` (1322), Aktivitätsbalken `width: 4rem` (829), Verlauf `4rem` (918, 921), Nummernbreite `1.4em` (907), `font-weight: 500` in `km-table__scope` (807), `700` in `km-table__group-label` (811 ff.).

## Offene Punkte

- **Aktionsspalte:** Stories `#tabelle-regeln` und `#tabelle-spalten` folgen dem Code (immer rechts, fest, mit Verlauf).
- Der CSS-Kommentar „Aktionsspalte klebt nicht mehr“ in `src/km-components.css` (Abschnitt „Weiter-Verlauf“) widerspricht noch und sollte entfallen.
- **Unterzeilen:** Story `#tabelle` folgt den Seitenregeln (Einrückungswinkel am Namen).
- Der CSS-Kommentar an `.km-table__name` („Unterzeilen ohne Einrückung und Strich“) widerspricht noch.
- Sortierbare Köpfe und Gruppenzeilen ohne Knopf: Kit-Variante mit `<button>` im `th` (wie es die Spalte `km-table__tool` im Kopf schon tut) fehlt.
- Kein Zustand „leer“ (keine Treffer) im Baustein; heute löst das die Seite mit `km-results__leer`.
- Bekannte Abweichung aus den Seitenregeln: Spalte „Dateien“ im Dashboard ist `__nowrap` statt `__num`.

## Regeln

- Was: Die Tabelle `km-table` im Rahmen `km-table-wrap` zeigt eine Liste gleichartiger Dinge in Zeilen und Spalten, mit Spaltenrollen (Name, Kennung, Wert, Zahl, Fließtext, Aktionen), Gruppen- und Unterzeilen; Varianten sind Standard, `km-table--compact`, `km-table--numbered` und `km-table__group--plain`.
- Wann: Für jede Menge gleichartiger Dinge, die verglichen, sortiert oder mit Zeilenaktionen bedient wird; bei vor allem Text Info-Karten (`km-card--info`), für reines Layout ein Raster, und eine Tabelle wird nie hinter einer Aufklapp-Zeile versteckt.
- Wie: `table.km-table` immer in `km-table-wrap`, benannt per `aria-labelledby` auf die Zwischenüberschrift `km-subhead`, jede Spalte mit Icon im Kopf und Rolle über `km-table__name`, `__key`, `__nowrap`, `__num`, `__text`, Aktionen als `km-iconbtn` mit `aria-label` in `km-table__actions` als letzte Spalte, Sortierung über `aria-sort`, keine festen Breiten in der Seite.
- Prüfen: Fertig ist es, wenn Werte nie umbrechen und alle Zeilen gleich hoch sind, der Rahmen bei Überlauf quer scrollt (`tabindex="0"` mit Namen) und die Aktionsspalte rechts stehen bleibt, Kopf- und Gruppentext in allen Themes mindestens 4,5:1 misst, der Fokus als Doppelring sichtbar ist und bei 390 px die Seite nicht waagerecht scrollt.
