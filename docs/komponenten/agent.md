# Agenten-Karte (`km-agent`)

Status: stabil, im Dashboard im Einsatz · Story: `docs/index.html#agent`, `#agenten-varianten` · CSS: `src/km-components.css`, Abschnitt „Agenten-Karten“ · Stand: 2026-11-09

## Kurzbeschreibung

Karte für einen KI-Agenten: Symbol-Kachel, Name, Rolle, Beschreibung und die Befehle zum Aufrufen. Im Raster `km-agent__grid` stehen mehrere Agenten nebeneinander; eine farbige Kante oben unterscheidet Koordinator, Sucher und Verbinder. Darunter sagt eine Zeile, wer wen koordiniert.

## Name und Abgrenzung

- `km-agent__grid`, `__card`, `__header`, `__icon`, `__name`, `__role`, `__desc`, `__commands`, `__cmd`, `__coord`; Varianten `__cockpit`, `__radar`, `__bridge` (Kante oben als Verlauf).
- Feste Karte für diesen einen Inhalt; allgemeine Karten sind `km-card`.

## Einsatz

### Verwenden, wenn

- KI-Agenten mit Rolle und Befehlen zum Aufrufen vorgestellt werden, etwa im Über-Bereich einer Werkzeugseite unter der Einführung (Dashboard „Über dieses Projekt & Agents“; CSS `.km-hero__text + .km-agent__grid`; das Migrationsprotokoll, Zeile „Agents im Über-Bereich“);
- mehrere Agenten ihre Aufgaben teilen (Koordinator, Sucher, Verbinder) und eine Zeile darunter sagt, wer wen koordiniert (Story `#agenten-varianten`).

### Nicht verwenden, wenn

- allgemeine Inhalte im Raster stehen: `km-card`;
- Agenten als Liste mit gleichen Spalten verglichen werden: Standard-Tabelle `km-table`, Name in `km-table__name` (`docs/seitenregeln.md`, „Rolle je Spalte“ nennt Agent als Name, „Jede Liste von Dingen ist die Standard-Tabelle“).

## Verwendung

Markup wie Story `#agent`; Modell oder Status als `km-pill` rechts im Kopf.

## Zustände

Statisch. Kopf bricht unter 40rem um, Befehle dürfen dann umbrechen.

## Barrierefreiheit

- Name als Überschrift setzen (Story nutzt `div`).
- Kontrast: Beschreibung `--km-color-text-muted` auf `--km-color-card` 7,89 / 7,85 / 8,57 / 7,79; Rolle `--km-color-text-dim` auf `card` 6,25 / 6,05 / 5,78 / 6,23 (Kobalt dunkel, Kobalt hell, Papier dunkel, Papier hell).
- Die Farbkante ist Zierde, die Rolle steht als Text.

## Beispiele

### Falsch

```html
<div class="km-agent__card" style="border-top:3px solid #f60">…</div>   <!-- harte Farbe statt Variante -->
```

## Seitenregeln

Farbkanten einheitlich; keine harten Werte; nur Lucide-Icons. Entscheidungen 16, 18, 25.

## Vergleich mit anderen Design-Systemen

| System | Name | Besonderheit | Quelle |
|---|---|---|---|
| – | – | ungeprüft | – |

## Tokens

- `--km-color-card`, `--km-color-border-card`, `--km-color-track`, `--km-color-text`, `--km-color-text-muted`, `--km-color-text-dim`, `--km-color-attention`, `--km-color-accent`, `--km-color-highlight`, `--km-bar`, `--km-space-xl`.
- Rückmelde-Rollen: `--km-color-feedback-danger`, `-info`, `-success`.
- Hart: Kachel `2.25rem`, `font-weight: 600/500`.

## Offene Punkte

- Varianten heißen nach den Agenten des Dashboards (`__cockpit`, `__radar`, `__bridge`) und als Elemente (`__`) statt Modifier (`--`); inhaltsneutral benennen (`--coordinator`, `--worker`, `--analyst`).
- Kante oben als `::before`-Verlauf statt Innenschatten wie die übrigen Farbkanten.
- Name und Rolle als `div` ohne Überschrift.

## Regeln

- Was: Die Agenten-Karte `km-agent` zeigt einen KI-Agenten mit Symbol-Kachel, Name, Rolle, Beschreibung und Aufrufbefehlen; mehrere stehen im Raster `km-agent__grid`, die Farbkante oben unterscheidet die Varianten `__cockpit`, `__radar` und `__bridge`.
- Wann: Wenn KI-Agenten mit Rolle und Aufrufbefehlen vorgestellt werden, einzeln oder zu mehreren im Raster mit der Zeile, wer wen koordiniert, etwa im Über-Bereich unter der Einführung; allgemeine Inhalte im Raster gehören in `km-card`, Agenten als Liste mit gleichen Spalten in die Standard-Tabelle `km-table`.
- Wie: Markup wie Story `#agent` mit `__header`, `__icon`, `__name`, `__role`, `__desc`, `__commands`, `__coord`, Modell oder Status als `km-pill` rechts im Kopf, Farbe nur über die Variante statt harter Werte, nur Lucide-Icons.
- Prüfen: Fertig ist es, wenn der Name als Überschrift gesetzt ist, die Rolle als Text dasteht (die Farbkante ist nur Zierde), Beschreibung und Rolle in allen vier Themes den gerechneten Kontrast halten (mindestens 7,79 bzw. 5,78) und der Kopf unter 40rem umbricht.
