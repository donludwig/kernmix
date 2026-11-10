# Auswahl mit Suche (`km-selectpanel`)

Status: neu, im Dashboard im Einsatz · Story: `docs/index.html#selectpanel` · CSS: `src/km-components.css`, Abschnitt „Auswahl mit Suche (km-selectpanel)“ · Stand: 2026-11-09

## Kurzbeschreibung

Die Auswahl mit Suche lässt aus einer langen Liste wählen, ohne dass die Liste dauerhaft Platz braucht. Ein Knopf mit Pfeil öffnet ein schwebendes Panel: oben ein Suchfeld, in dem der Fokus startet, darunter alle Einträge als Kästchen in einer scrollenden Liste, ausgewählte zuerst, unten ein Hinweis zur Anzahl. Enter nimmt den ersten passenden Treffer, Esc oder ein Klick daneben schließt. Dasselbe Panel trägt auch Icon-Auswahl und kleine Formulare wie „Neue Liste“.

## Name und Abgrenzung

- Klasse `km-selectpanel`; Name des Musters nach Primer „SelectPanel“. In der Oberfläche heißt der auslösende Knopf nach dem Gegenstand („Projekte“).
- Zum Baustein gehören Panel, Kopfzeilen, Zeilen (Suchfeld, Formular, Icon-Raster), Liste mit Kästchen und Fußhinweis.
- Nicht dazu gehören der auslösende Knopf (`km-button`), das Suchfeld (`km-searchbox`), die Kästchen (`km-check`) und das Verhalten (Öffnen, Filtern, Lage am Knopf, Schließen): das setzt das Skript der Seite.
- `km-colpicker` (Spaltenauswahl): älterer Baustein mit eigenem Panel und Sets; folgt in Schrift und Icons inzwischen demselben Muster. Siehe offene Punkte.
- Natives `select` bzw. KERN „Input Select“: Einfachauswahl aus wenigen Optionen in einem Formular.
- KERN „Dropdown“ bündelt Aktionen oder Links und ist laut KERN noch in Bearbeitung.
- Keine Combobox im engen Sinn: Das Suchfeld filtert die Liste, sein Wert ist nicht der gewählte Wert.

Namensalternativen (Entscheidung offen): Auswahl mit Suche (heute), Suchauswahl, Auswahlpanel, Filterliste, Mehrfachauswahl.

## Einsatz

### Verwenden, wenn

- aus einer Menge von etwa 10 bis einigen hundert Dingen gewählt wird (Projekte auf eine Liste setzen, Icon wählen);
- mehrere gleichzeitig gewählt werden können;
- die Wahl selten ist und keinen festen Platz in der Seite verdient.

### Nicht verwenden, wenn

- es nur zwei bis fünf Optionen gibt: Segmented Control (`km-segmented`) oder Radios;
- eine einzelne Auswahl in einem Formular gebraucht wird: natives `select`;
- frei eingegeben wird, ohne Liste: Suchfeld;
- Aktionen statt Werte angeboten werden: Menü bzw. KERN-Dropdown.

## Verwendung

```html
<button type="button" class="km-button" aria-haspopup="dialog" aria-expanded="true" aria-controls="sp-projekte">
  <svg class="km-icon" aria-hidden="true">…</svg>Projekte<span class="km-button__count">2</span><svg class="km-icon" aria-hidden="true">…</svg>
</button>
<div class="km-selectpanel km-selectpanel--open" id="sp-projekte" role="dialog" aria-label="Projekte auswählen">
  <div class="km-selectpanel__head">Projekte auf „Quickliste“</div>
  <div class="km-selectpanel__row"><span class="km-searchbox"><input type="search" placeholder="Projekt suchen …" aria-label="Projekt suchen"></span></div>
  <div class="km-selectpanel__list">
    <label><input type="checkbox" class="km-check" checked><span class="km-monogram" aria-hidden="true">LB</span>Lagebild</label>
    <label><input type="checkbox" class="km-check">Projekt B</label>
  </div>
  <div class="km-selectpanel__head km-selectpanel__head--sep" aria-live="polite">95 Projekte · 2 ausgewählt</div>
</div>
```

## Aufbau

| Teil | Klasse | Funktion |
|---|---|---|
| Panel | `km-selectpanel` | `position: fixed`, über allem (`z-index: 100`), 17 bis 24rem breit, Kartenfläche, Rand, Schatten. Ohne `--open` unsichtbar. |
| Offen | `km-selectpanel--open` | zeigt das Panel. Lage setzt die Seite (am Knopf). |
| Kopfzeile | `km-selectpanel__head` | Versalien, gedämpft: Titel oben, Anzahl unten. |
| Trenner | `km-selectpanel__head--sep` | Kopfzeile mit Linie darüber, trennt Abschnitte (z. B. „Neue Liste“, „Icons“). |
| Zeile | `km-selectpanel__row` | Suchfeld, Formular oder Icon-Raster; Suchfeld volle Breite. |
| Liste | `km-selectpanel__list` | alle Einträge, scrollt (höchstens 22rem bzw. 55 % der Fensterhöhe), Scrollen bleibt im Panel. |
| Eintrag | `label` mit `km-check` | Kästchen, optional Monogramm, Name einzeilig; ganze Zeile klickbar. |

## Varianten

- **Mehrfachauswahl** mit Kästchen (Standard, Story).
- **Icon-Auswahl**: Raster aus `km-iconbtn` in einer Zeile mit `role="group"`, gewähltes Icon `aria-pressed="true"`; höchstens 12 bis 48 Treffer und Hinweis „… von … · Suche eingrenzen“.
- **Formular im Panel**: Zeile als `form` mit Eingabefeld und Knopf (Name einer neuen Liste), Löschen unten, zweistufig („Wirklich löschen?“).

## Größen

Eine Größe; Breite 17 bis 24rem, nie breiter als das Fenster minus 1rem.

## Zustände

| Zustand | Auslöser | Darstellung | Tokens |
|---|---|---|---|
| Zu | ohne `km-selectpanel--open` | `display: none` | – |
| Offen | `km-selectpanel--open`, am Knopf `aria-expanded="true"` | Panel mit Schatten; Knopf mit Akzent-Rand | `--km-shadow-strong` (dunkel), `--km-shadow` (hell) |
| Eintrag überfahren | `label:hover` | Fläche `--km-color-inset` | `--km-color-inset` |
| Eintrag gewählt | `input:checked` | Kästchen gefüllt; Eintrag rückt beim nächsten Öffnen nach oben | `km-check` |
| Eintrag deaktiviert | `input:disabled` | Kästchen abgeblendet | `--km-opacity-disabled` |
| Suchfeld fokussiert | `:focus-visible` im Feld | eine kräftige Linie am Rahmen des Felds, kein zweiter Ring | `--km-color-focus` |
| Keine Treffer | – | kein eigener Zustand im Baustein; Fußzeile meldet 0 | offen |
| Zu viele Treffer | – | Fußhinweis „… von … · Suche eingrenzen“ | – |

## Verhalten

Das Kit liefert nur CSS. Die Seite muss leisten:

- Öffnen per Klick auf den Knopf, Lage am Knopf (fixed, im Fenster bleibend), Fokus ins Suchfeld.
- Filtern beim Tippen; ausgewählte zuerst; Enter nimmt den ersten Treffer.
- Schließen per Esc, Klick daneben oder erneuten Klick auf den Knopf; danach Fokus zurück auf den Knopf und `aria-expanded="false"`.
- Anzahl im Knopf und im Fußhinweis aktualisieren.

## Text und Wording

- Kopfzeile: Gegenstand und Ziel („Projekte auf „Quickliste““), höchstens etwa 40 Zeichen.
- Platzhalter im Suchfeld: „<Gegenstand> suchen …“.
- Fußhinweis: „<Anzahl> <Gegenstand> · <Anzahl> ausgewählt“.
- Einträge: Name einzeilig; lange Namen mit „…“ und vollem Namen im `title`.

## Barrierefreiheit

- Rolle: Panel `role="dialog"` mit `aria-label`, weil es Suchfeld, Kästchen und Formulare enthält; nicht `role="menu"` (ein Menü erlaubt nur Menüeinträge).
- Knopf mit `aria-haspopup="dialog"`, `aria-expanded`, `aria-controls`.
- Kästchen nativ (`input type="checkbox"` im `label`); Monogramm `aria-hidden="true"`, der Name steht als Text daneben.
- Fußhinweis als `aria-live="polite"`, damit die Trefferzahl angesagt wird.
- Tastatur: Tab vom Suchfeld in die Liste und zurück, Leertaste schaltet ein Kästchen, Esc schließt.
- Ein nicht-modales Panel muss den Fokus nicht einsperren; verlässt der Fokus das Panel, sollte es schließen.
- Fokus: Suchfeld mit einer Linie am Rahmen (`.km-searchbox:has(input:focus-visible)`), Kästchen mit Doppelring.
- Kontrast: Einträge `--km-color-text` auf `--km-color-card` bzw. `--km-color-inset` (12,88 / 14,57 / 12,06 / 16,15 auf `inset` für Kobalt dunkel, Kobalt hell, Papier dunkel, Papier hell); Kopfzeilen `--km-color-text-dim` auf `--km-color-card` 6,25 / 6,05 / 5,78 / 6,23; Rand der Kästchen über `--km-color-border-input` ≥ 3:1 (5,78 bis 6,25).
- Schmal (390 px): Panel höchstens Fensterbreite minus 1rem, Liste höchstens 55 % der Fensterhöhe.

## Beispiele

### Richtig

Knopf `km-button` mit `aria-haspopup="dialog"` öffnet `km-selectpanel` mit `role="dialog"`, Fokus im Filterfeld, Kästchen `km-check` mit Monogramm.

### Falsch

```html
<input type="text" placeholder="Projekt eintippen">            <!-- freies Feld statt Auswahl -->
<div class="km-selectpanel" role="menu">…<input type="checkbox">…</div>  <!-- Menü-Rolle mit Kästchen -->
```

## Seitenregeln

Aus `docs/seitenregeln.md`, „Auswahl, Menüs und Segmented Control“: Auswahl mit Suche statt freiem Feld; Knopf mit Pfeil öffnet das Menü; Enter nimmt den ersten Treffer; gleicher Baustein wie Spaltenauswahl und Listen-Menü in den Zeilen; auch in Auswahlmenüs steht das Monogramm vor dem Namen; Bearbeiten (Name, Icon, Löschen) gesammelt hinter „… bearbeiten“, Löschen unten, zweistufig, kein `confirm`; Icon-Suche über die englischen Lucide-Begriffe.

## Vergleich mit anderen Design-Systemen

| System | Name | Besonderheit | Quelle |
|---|---|---|---|
| Primer (GitHub) | SelectPanel | „a dialog that allows users to quickly navigate and select one or multiple items from a list“; verankert (Änderung gilt beim Schließen) oder modal (gilt nach Bestätigen); Filterfeld mit Platzhalter „Filter items“, Name über `inputLabel` | primer.style/product/components/select-panel |
| WAI-ARIA APG | Combobox mit Listbox-Popup | Eingabe mit `role="combobox"`, `aria-expanded`, `aria-controls`; Fokus bleibt im Feld, Liste über `aria-activedescendant`; Pfeil runter in die Liste, Esc schließt und gibt den Fokus ans Feld, Enter übernimmt die Option | w3.org/WAI/ARIA/apg/patterns/combobox |
| KERN 2.8.2 | Input Select, Dropdown | Input Select: Auswahl aus einer ausklappbaren Optionsliste; Dropdown bündelt Aktionen oder Links und ist „derzeit noch in Bearbeitung“; keine Auswahl mit Suche | kern-ux.de/komponenten, kern-ux.de/komponenten/dropdown |

`km-selectpanel` folgt Primer (Dialog mit Filterfeld und Kästchen) und nicht der APG-Combobox: Die Kästchen sind eigene Fokusziele, `aria-activedescendant` wird nicht genutzt.

## Verwandte Bausteine

`km-button` (Auslöser), `km-searchbox`, `km-check`, `km-monogram`, `km-iconbtn` (Icon-Raster), `km-colpicker` (Spaltenauswahl), `km-segmented` (wenige Optionen).

## Tokens

Rollen: `--km-color-card`, `--km-color-inset`, `--km-color-border-card`, `--km-color-text`, `--km-color-text-dim`, `--km-color-focus`, `--km-color-border-input`, `--km-shadow`, `--km-shadow-strong`, `--km-font-size-xs`, `--km-tracking-caps`, `--km-space-2xs`, `--km-space-xs`, `--km-space-s`, `--km-space-m`, `--km-space-tight`, `--km-radius`, `--km-border-width`.

- Komponenten-Tokens: keine.
- Hart im Baustein (`src/km-components.css`, Regeln `.km-selectpanel`, `.km-selectpanel__head`, `.km-selectpanel__list`): `z-index: 100`, `min-width: 17rem`, `max-width: min(24rem, calc(100vw - 1rem))`, `max-height: min(22rem, 55vh)`, `font-weight: 500`.
- Der Schatten wechselt über `:root[data-theme="light"]` statt über ein Token, obwohl die Themes `data-kern-theme` setzen.

## Offene Punkte

- **Modus-Selektor:** Die Regel für den hellen Schatten nutzt `:root[data-theme="light"]`; die Themes schalten über `data-kern-theme` bzw. `prefers-color-scheme`.
- Der helle Schatten greift also nur, wenn die Seite zusätzlich `data-theme` setzt; ohne dieses Attribut (oder bei hellem System ohne Attribut) bleibt der dunkle `--km-shadow-strong`.
- Besser ein Token `--km-selectpanel-shadow`, das das Theme setzt.
- Kein Verhalten im Kit: Öffnen, Lage, Filtern und Schließen leben im Skript jeder Seite.
- Ein kleines gemeinsames Skript oder eine Verhaltensbeschreibung als Vertrag fehlt.
- `role`: Mindestens eine Nutzerseite setzt für ein Panel mit Kästchen `role="menu"`; nach dieser Doku ist `role="dialog"` richtig.
- Kein Zustand „keine Treffer“.
- `km-colpicker` und `km-selectpanel` überschneiden sich; Zusammenführen prüfen.

## Regeln

- Was: `km-selectpanel` ist ein schwebendes, nicht-modales Panel an einem Knopf mit Pfeil: oben ein Suchfeld mit Startfokus, darunter eine scrollende Liste mit Kästchen (ausgewählte zuerst), unten ein Fußhinweis zur Anzahl; Varianten sind Mehrfachauswahl, Icon-Auswahl und Formular im Panel.
- Wann: Für etwa 10 bis einige hundert Dinge bei seltener Mehrfachwahl; bei zwei bis fünf Optionen `km-segmented` oder Radios, für eine Einzelwahl im Formular natives `select`, für freie Eingabe ein Suchfeld, für Aktionen ein Menü.
- Wie: Auslöser `km-button` mit `aria-haspopup="dialog"`, `aria-expanded` und `aria-controls`, Panel `km-selectpanel` plus `--open` mit `role="dialog"` und `aria-label` (nie `role="menu"`), Suchfeld `km-searchbox` in `__row`, Einträge als `label` mit `km-check` und optional `km-monogram` in `__list`, Fußhinweis `__head--sep` mit `aria-live="polite"`; Öffnen, Lage, Filtern, Enter auf den ersten Treffer und Schließen macht das Skript der Seite.
- Prüfen: Fertig ist es, wenn der Fokus im Suchfeld startet, Esc und Klick daneben schließen und der Fokus mit `aria-expanded="false"` zurück auf den Knopf geht, Tab und Leertaste in der Liste arbeiten, die Trefferzahl angesagt wird, Text und Kopfzeilen den gerechneten Kontrast halten (Kästchen-Rand mindestens 3:1) und das Panel bei 390 px höchstens Fensterbreite minus 1rem misst.
