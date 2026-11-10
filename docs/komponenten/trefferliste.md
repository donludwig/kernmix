# Trefferliste der Suche (`km-results`)

Status: stabil, im Dashboard im Einsatz · Story: `docs/index.html#suche`, `#treffer-kopf`, `#trefferliste`, `#suchhinweise` · CSS: `src/km-components.css`, Abschnitte „Suche: Ergebnisse, Hinweise, aktive Filter“, „Suche: Kopfzeile mit Reitern, Titel je Treffer“ · Stand: 2026-11-09

## Kurzbeschreibung

Die Trefferliste zeigt Ergebnisse einer seitenweiten Suche unter dem Suchfeld, eingerückt und gerahmt wie die Tabelle darunter. Oben stehen Trefferzahl und Leeren, darunter ein Segmented Control je Kategorie mit Zähler, dann die Kategorien als Überschrift mit Linie und je Treffer eine kompakte Zeile: Markierung, Titel mit Kunde, Fundstelle und eine Zeile Auszug. Klickt man ins leere Suchfeld, zeigt dieselbe Fläche Suchhinweise mit Filter-Chips und Syntax.

## Name und Abgrenzung

- `km-results` (Ergebnisse), `km-results--hints` (Hinweise). In der Oberfläche ohne eigenen Namen.
- Zum Baustein gehören Kopf (`__summary`, `__head`, `__stat`, `__types`, `__typ`, `__clear`), Segmented Control (`__tabs` mit `km-segmented`), Kategorie (`__group`), Treffer (`__item`, `--projekt`, `__type`, `__title`, `__name`, `__kunde`, `__field`, `__snip`, `__dot`), Mehr (`__more`, `__showall`), Leer (`__leer`) und Hinweise (`__h-row`, `__h-label`, `__h-chip`, `__h-active`, `__h-syntax`).
- Nicht dazu: Suchlogik, Ranking, Tastatursteuerung.
- `km-table`: dauerhafte Liste; die Trefferliste ist ein vorübergehender Zustand der Suche.

## Einsatz

### Verwenden, wenn

- eine Suche über mehrere Arten von Inhalten (Projekte, Aufgaben, Chats) gleichzeitig läuft;
- Treffer mit Fundstelle und Auszug gezeigt werden.

### Nicht verwenden, wenn

- nur die Zeilen einer Tabelle gefiltert werden: die Tabelle selbst filtern, Trefferzahl am Suchfeld.

## Verwendung

```html
<div class="km-results" role="region" aria-label="Suchergebnisse">
  <div class="km-results__summary"><span><strong>23</strong> Treffer für „token“</span><button type="button" class="km-results__clear" aria-label="Suche leeren">…</button></div>
  <div class="km-results__tabs km-segmented" role="group" aria-label="Kategorie"><button type="button" class="km-segmented__btn" aria-pressed="true">Alle <span class="km-segmented__count">23</span></button>…</div>
  <div role="listbox" aria-label="Treffer">
    <div class="km-results__group">Projekte <span>18</span></div>
    <div class="km-results__item km-results__item--projekt" role="option" tabindex="-1" style="--sr-color:var(--km-color-accent)">…</div>
  </div>
</div>
```

## Aufbau

| Teil | Klasse | Funktion |
|---|---|---|
| Fläche | `km-results` | Rand, Kartenfläche, seitlich `--km-space-section-x` eingerückt. |
| Kopf | `__summary` bzw. `__head` | Trefferzahl, Verteilung nach Werkzeug, Leeren rechts. |
| Segmented Control | `__tabs` + `km-segmented` | Kategorie wählen, leere deaktiviert. |
| Kategorie | `__group` | Versalien mit Linie, `--km-space-2xl` davor, eng zur eigenen Liste. |
| Treffer | `__item` | Raster: Markierung, Titel und Kunde, Fundstelle; darunter Auszug; Pfeil rechts. |
| Projekt-Treffer | `__item--projekt` | Kante links in `--sr-color` (Kundenfarbe). |
| Fundstelle | `__field` | gerahmte Angabe („Beschreibung“). |
| Auszug | `__snip` | eine Zeile mit „…“, Treffer als `mark` im Akzent. |
| Mehr | `__more`, `__showall` | „… 3 weitere“, Knopf „Alle 18 Projekte zeigen“. |
| Leer | `__leer` | Hinweis und Weg zurück zur Übersicht. |
| Hinweise | `km-results--hints`, `__h-*` | Zeilen mit Beschriftung, Filter-Chips in der Farbe ihres Felds, Syntax. |

## Zustände

| Zustand | Auslöser | Darstellung | Tokens |
|---|---|---|---|
| Treffer Hover / Fokus darin | `:hover`, `:focus-within` | Rand Akzent, Fläche `inset`, Pfeil rückt nach rechts | `--km-color-accent`, `--km-color-inset` |
| Per Tastatur gewählt | `aria-selected="true"` | Rand Akzent, Innenring in Fokusfarbe | `--km-color-focus` |
| Kategorie leer | `disabled` am Segment | abgeblendet | `--km-opacity-disabled` |
| Hinweis-Chip aktiv | `__h-active` | 18 % Tönung in der Feldfarbe; Hover streicht durch (entfernen) | `--chip` |
| Keine Treffer | `__leer` | Text gedämpft, Link zurück | – |

## Verhalten

- Das Skript der Seite füllt die Liste, zeigt je Kategorie die besten fünf, steuert Pfeiltasten (`aria-selected`), Enter und Esc.
- Ein Sprung zu einer Aufgabe markiert sie kurz (`km-task--treffer`).

## Text und Wording

„<Zahl> Treffer für „<Begriff>““; Kategorien im Plural; „Alle <Zahl> <Kategorie> zeigen“; ohne Treffer ein Satz und ein Weg zurück.

## Barrierefreiheit

- Listbox-Muster: Container `role="listbox"`, Treffer `role="option"` mit `aria-selected`, Fokus bleibt im Suchfeld (`aria-activedescendant`) oder wandert in die Liste; die Seite muss eines davon vollständig umsetzen.
- Trefferzahl in `aria-live="polite"`.
- Kategorien sind `div`; als Gruppen (`role="group"` mit Namen) wären sie für Screenreader erkennbar.
- Kontrast (gerechnet):

| Paar | Kobalt dunkel | Kobalt hell | Papier dunkel | Papier hell |
|---|---|---|---|---|
| Titel `--km-color-text` auf `--km-color-card` | 14,16 | 15,89 | 13,03 | 17,61 |
| Auszug `--km-color-text-muted` auf `--km-color-card` | 7,89 | 7,85 | 8,57 | 7,79 |
| Kunde `--km-color-text-dim` auf `--km-color-card` | 6,25 | 6,05 | 5,78 | 6,23 |
| Titel auf `--km-color-inset` (Hover) | 12,88 | 14,57 | 12,06 | 16,15 |
| Treffer `mark`: `--km-color-on-accent` auf `--km-color-accent` | 9,13 | 6,69 | 8,68 | 8,38 |
| Hinweis-Chip aktiv: Text auf 18 % Tönung | 9,78 | 12,08 | 9,02 | 12,88 |

## Beispiele

### Richtig

Projekt-Treffer mit Kundenfarbe links, Kategorien mit Linie, Auszug einzeilig.

### Falsch

```html
<!-- Kategorie mit Farbrand: der Farbrand gehört den Projekt-Treffern -->
<div class="km-results__group" style="border-left:3px solid …">Projekte</div>
<!-- Pfeil als Schriftzeichen -->
<span>›</span>
```

## Seitenregeln

Aus `docs/seitenregeln.md`: keine Schriftzeichen als Icon; ein Filter zur Zeit aus der Navigation; Adresse und Speicher; Nähe gruppiert (Abstands-Regelwerk, Kategorie 16 bzw. 32 px davor, 8 px zur Liste, 4 px zwischen Treffern).

Entscheidungen: 12 (Abstände), 16 (Icons), 22 (Filter, Adresse, Verlauf).

## Vergleich mit anderen Design-Systemen

| System | Name | Besonderheit | Quelle |
|---|---|---|---|
| WAI-ARIA APG | Listbox | ungeprüft (Abruf in `auswahl-mit-suche.md` betraf die Combobox) | – |

## Verwandte Bausteine

`km-searchbox`, `km-filterchips`, `km-segmented`, `km-peek` (Vorschau beim Überfahren), `km-task`.

## Tokens

Rollen: `--km-color-card`, `--km-color-inset`, `--km-color-border-card`, `--km-color-border-section`, `--km-color-text`, `--km-color-text-muted`, `--km-color-text-dim`, `--km-color-accent`, `--km-color-on-accent`, `--km-color-focus`, `--km-space-section-x`, `--km-space-2xl`, `--km-mask-chevron`, `--km-mask-x`.

- Komponenten-Haken: `--sr-color` (Kundenfarbe eines Treffers), `--chip` (Feldfarbe eines Hinweis-Chips), beide ohne Präfix.
- Hart im Baustein: Pfeil-Abstand `0.75rem`, Hinweis-Beschriftung `3.6rem`, Tönungen 12, 18 und 55 %, Icon-Strich `1.4`, `vertical-align: -2px`, `font-weight: 700` und `400` statt Rollen.

## Offene Punkte

- Haken `--sr-color` und `--chip` ohne `--km-`-Präfix.
- Feste Pixelwerte (`-2px`) und Schriftstärken als Zahl.
- `km-results__item` hat `cursor: pointer`, ist aber kein Link; das Ziel (Link `__name`) ist kleiner als die Klickfläche.

## Regeln

- Was: Die Trefferliste `km-results` zeigt die Ergebnisse einer seitenweiten Suche unter dem Suchfeld mit Kopf (Trefferzahl, Leeren), Segmented Control je Kategorie, Kategorien mit Linie und je Treffer einer kompakten Zeile aus Titel, Fundstelle und Auszug; `km-results--hints` zeigt im leeren Feld Suchhinweise mit Filter-Chips und Syntax.
- Wann: Wenn eine Suche mehrere Arten von Inhalten gleichzeitig durchsucht und Treffer mit Fundstelle und Auszug zeigt; werden nur Zeilen einer Tabelle gefiltert, filtert die Tabelle selbst und die Trefferzahl steht am Suchfeld.
- Wie: `km-results` mit `role="region"` und `aria-label`, Kategorie über `km-results__tabs` mit `km-segmented`, Treffer als `km-results__item` mit `role="option"` in einem `role="listbox"`, Projekt-Treffer mit `km-results__item--projekt` und Kundenfarbe über `--sr-color`, Auszug einzeilig mit „…“, Trefferzahl in `aria-live="polite"`, Text „<Zahl> Treffer für „<Begriff>““; Pfeile und Icons nie als Schriftzeichen.
- Prüfen: Fertig ist es, wenn Hover, Fokus und Tastaturwahl (`aria-selected="true"`) sichtbar sind, leere Kategorien `disabled` und abgeblendet sind, ohne Treffer ein Satz mit Weg zurück erscheint, entweder `aria-activedescendant` oder Fokus in der Liste vollständig umgesetzt ist und alle Texte in allen Themes mindestens 4,5:1 messen.
