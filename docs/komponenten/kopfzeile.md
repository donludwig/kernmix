# Kopfzeile (`km-header`, `km-quicklinks`, `km-brand`)

Status: neu (`km-header` seit 2026-11-09), in Dashboard und Lagebild im Einsatz · Story: `docs/index.html#kopfzeile` (`km-header`), dazu `#quicklinks`, `#bedienteile` (`km-brand`), `#zustaende` (Quicklink beim Ziehen), `#zustaende-skript` (kopiert) · CSS: `src/km-components.css`, Abschnitte „Kopfzeile der Seite“, „Quicklinks im Kopf“, „Dashboard-Gerüst“ (`km-brand`) · Stand: 2026-11-09

## Kurzbeschreibung

Die Kopfzeile steht oben fest über der Seite: links Logo und Titel, die die Seite zurücksetzen, in der Mitte Platz für angeheftete Quicklinks, rechts die Knöpfe der Seite in fester Reihenfolge, gleich hoch, der Theme-Schalter ganz rechts. Quicklinks sind Pillen mit Monogramm, Name und Kopier-Icon; ein Klick kopiert, das Kreuz löst sie.

## Name und Abgrenzung

- `km-header` (`__title`, `__icon`, `__actions`), `km-quicklinks` (`__pill`, `__pill-copy`, `__pill-icon`, `__pill-name`, `__pill-remove`, `__empty`, `__dragging`, `__pill-copy--done`), `km-brand` (`__select`, `__dot`, Auswahl eines Kunden mit Farbpunkt).
- Nicht dazu: Seitenleiste und Einklapp-Knopf (`km-sidebar__toggle`), Verhalten von Zurücksetzen, Kopieren und Ziehen.
- KERN „Header“ (Kopf einer Verwaltungsseite mit Wortmarke, ungeprüft) ist für Publikationsseiten; `km-header` ist eine dichte Werkzeugzeile.

## Einsatz

### Verwenden, wenn

eine Werkzeugseite einen festen Kopf mit Titel und Seitenknöpfen braucht.

### Nicht verwenden, wenn

eine Publikationsseite gebaut wird: KERN-Header.

## Verwendung

```html
<header class="km-header">
  <h1 class="km-header__title"><a href="./"><img class="km-header__icon" src="favicon.svg" alt="">Project Dashboard</a></h1>
  <nav class="km-quicklinks" aria-label="Quicklinks">…</nav>
  <div class="km-header__actions">
    <button type="button" class="km-iconbtn km-iconbtn--label">Scan<svg class="km-icon" aria-hidden="true">…</svg></button>
    <button type="button" class="km-iconbtn" aria-label="Hell oder dunkel"><svg class="km-icon" aria-hidden="true">…</svg></button>
  </div>
</header>
```

## Aufbau

| Teil | Klasse | Funktion |
|---|---|---|
| Zeile | `km-header` | `sticky` oben, `z-index: 50`, Kartenfläche, Linie und Schatten unten, Innenrand `--km-space-s` / `--km-space-2xl`. |
| Titel | `km-header__title` | `h1`, `--km-font-size-m`, kräftig, einzeilig; Hover im Akzent. |
| Logo | `km-header__icon` | Quadrat `--km-monogram-size`; auf derselben Linie wie die Icons der Seitenleiste. |
| Knöpfe | `km-header__actions` | rechts, jedes Kind genau `--km-header-control-height` hoch. |
| Quicklinks | `km-quicklinks` | nimmt den Platz dazwischen, scrollt quer, kein Innenabstand oben/unten. |
| Pille | `km-quicklinks__pill` | Kopieren (`__pill-copy` mit Monogramm, Name, Icon) und Lösen (`__pill-remove`, Lucide `x` als Maske). |
| Kundenwahl | `km-brand__select`, `km-brand__dot` | natives `select` im Rahmen mit Farbpunkt. |

## Größen

Knöpfe 1.75rem (`--km-header-control-height`); unter 60em stehen die Knöpfe in eigener Zeile und brechen um.

## Zustände

| Zustand | Auslöser | Darstellung |
|---|---|---|
| Titel Hover | `:hover` | Akzentfarbe |
| Quicklink Hover | `__pill-copy:hover` | Fläche `inset` |
| Kopiert | `__pill-copy--done` | Text und Icon grün |
| Lösen Hover/Fokus | `__pill-remove:hover` | rot auf `inset` |
| Ziehen | `km-quicklinks__dragging` | gestrichelter Rahmen im Akzent |
| Leer | `km-quicklinks__empty` | Hinweistext gedämpft |

## Verhalten

- Titelklick setzt Filter, Suche, Sortierung und Klappen zurück (Seitenregeln „Logo setzt zurück“).
- Befehlsknöpfe kopieren den Befehl, sie führen nichts aus.
- Quicklinks: Klick kopiert, Ziehen sortiert, Kreuz löst; alles Skript der Seite.

## Text und Wording

Knöpfe mit kurzem Text in fester Reihenfolge der Seite; Theme-Schalter ganz rechts. Quicklink: Name des Projekts.

## Barrierefreiheit

- Titel ist die `h1` der Seite; das Logo `alt=""`, der Titel steht als Text.
- Quicklinks als `nav` mit `aria-label`; Lösen mit `aria-label` („Projekt 1 lösen“), nicht nur „Lösen“.
- Kontrast (gerechnet): Titel `--km-color-text` auf `--km-color-card` 14,16 / 15,89 / 13,03 / 17,61; Quicklink-Icon und Leerhinweis `--km-color-text-dim` auf `--km-color-page` 7,02 / 5,40 / 6,51 / 5,61 (Kobalt dunkel, Kobalt hell, Papier dunkel, Papier hell).

## Beispiele

### Richtig

Alle Knöpfe direkt in `km-header__actions`, ohne eigene Höhen.

### Falsch

```html
<div class="km-header__actions"><button style="height:30px">🌙</button></div>  <!-- Emoji als Icon, eigene Höhe -->
<button class="km-quicklinks__pill-remove">×</button>                           <!-- Schriftzeichen statt Maske, ohne Namen -->
```

## Seitenregeln

Aus `docs/seitenregeln.md`, „Kopfzeile“ und „Seitenrahmen gleich“: Knöpfe rechts in fester Reihenfolge, gleich hoch (`km-iconbtn--label`), Theme-Schalter ganz rechts, Befehlsknöpfe kopieren; Maße über `--km-header-control-height`, `--km-monogram-size`; eine Linie mit dem Logo; Logo setzt zurück.

Entscheidungen: 18 (Ausrichtung), 22 (Filter, Adresse), 23 (Kopfzeile gleich hoch).

## Vergleich mit anderen Design-Systemen

| System | Name | Besonderheit | Quelle |
|---|---|---|---|
| KERN 2.8.2 | Header | ungeprüft | – |

## Verwandte Bausteine

`km-iconbtn`, `km-iconbtn--label`, `km-monogram`, `km-sidebar`, `km-dnd`.

## Tokens

- Rollen: `--km-color-card`, `--km-color-page`, `--km-color-border-card`, `--km-color-inset`, `--km-color-text`, `--km-color-text-dim`, `--km-color-accent`, `--km-shadow`, `--km-header-control-height`, `--km-monogram-size`, `--km-space-s`, `--km-space-2xl`, `--km-mask-x`.
- Rückmelde-Rollen: `--km-color-feedback-success`, `-danger`.
- Hart: `z-index: 50`, `letter-spacing: -0.02em`, Pillen-Icon `1.25rem`, Lösen-Knopf `1.5rem`, Umbruch bei `60em`.

## Offene Punkte

- Die Story `#kopfzeile` zeigt Titel und Knöpfe; Quicklinks im Kopf stehen noch in ihrer eigenen Story.
- Story `#quicklinks` enthält „×“ im Lösen-Knopf; das CSS ersetzt es per Maske, das Markup sollte trotzdem kein Schriftzeichen tragen.
- `km-brand__select` ohne Story-Erklärung, wofür er heute dient.

## Regeln

- Was: Die Kopfzeile `km-header` steht oben fest mit Logo und Titel links (`km-header__title`, `km-header__icon`), den Quicklinks `km-quicklinks` in der Mitte und den Seitenknöpfen `km-header__actions` rechts; dazu gehört die Kundenwahl `km-brand`.
- Wann: Wenn eine Werkzeugseite einen festen Kopf mit Titel und Seitenknöpfen braucht; eine Publikationsseite bekommt den KERN-Header.
- Wie: `header.km-header` mit `h1.km-header__title` (Logo `alt=""`, Titel als Text), `nav.km-quicklinks` mit `aria-label`, alle Knöpfe direkt in `km-header__actions` in fester Reihenfolge, der Theme-Schalter ganz rechts, Maße über `--km-header-control-height` und `--km-monogram-size`, kein Emoji und kein Schriftzeichen als Icon; Lösen-Knöpfe mit `aria-label` wie „Projekt 1 lösen“.
- Prüfen: Fertig ist es, wenn jedes Kind von `km-header__actions` genau `--km-header-control-height` hoch ist, die Zustände der Tabelle (Hover, Kopiert, Lösen, Ziehen, Leer) erreichbar sind, der Titel in allen Themes mindestens 4,5:1 misst und die Knöpfe unter 60em in eigener Zeile umbrechen.
