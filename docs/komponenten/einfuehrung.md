# Einführung, Einleitung und Funktionsraster (`km-intro`, `km-hero`, `km-features`)

Status: stabil, im Dashboard im Einsatz · Story: `docs/index.html#einfuehrung`, `#hero`, `#funktionen` · CSS: `src/km-components.css`, Abschnitte „Einführung“, „Werbliche Einleitung und Funktionsraster“ · Stand: 2026-11-09

## Kurzbeschreibung

Drei Bausteine für den Einstieg in eine Sache. `km-intro` setzt Bild, Lead-Satz und Text als eine Fläche, ab 40rem Breite mit dem Bild links, schmaler darüber; langer Text wird nach fünf Zeilen gekürzt und lässt sich mit „Weiterlesen“ öffnen. `km-hero` ist der werbliche Einstieg in einen Bereich mit Kopfzeile, großer Schlagzeile, Einleitung und optional Kennzahlen. `km-features` zeigt Funktionen als große Kacheln mit Symbol, Titel und ein bis zwei Sätzen Nutzen.

## Name und Abgrenzung

- `km-intro` (`__inner`, `__media`, `__text`, `__lead`, `__body`, `__body--short`, `__more`), `km-hero` (`__kicker`, `__title`, `__text`), `km-features` / `km-feature` (`__icon`, `__title`, `__text`).
- `km-card`: Inhalt im Raster; `km-section__lead`: ein Satz Einleitung ohne Schlagzeile. `km-hero` ist ohne Bild.

## Einsatz

### Verwenden, wenn

- ein Projekt oben in seiner Karte vorgestellt wird (`km-intro`);
- ein Über-Bereich die Seite erklärt (`km-hero`, `km-features`).

### Nicht verwenden, wenn

- nur ein Satz gebraucht wird: `km-section__lead` bzw. erste `km-note`;
- mehr als sechs Funktionen gezeigt werden: Liste oder Tabelle.

## Verwendung

```html
<div class="km-intro" style="--km-card-accent:var(--km-color-tool-design)"><div class="km-intro__inner">
  <figure class="km-intro__media"><img src="vorschau.png" alt="Vorschau des Projekts"></figure>
  <div class="km-intro__text"><p class="km-intro__lead">Ein Satz, worum es geht.</p><p class="km-intro__body km-intro__body--short" id="intro-1">…</p><button type="button" class="km-intro__more" aria-expanded="false" aria-controls="intro-1">Weiterlesen</button></div>
</div></div>
<div class="km-hero"><p class="km-hero__kicker">Über</p><h2 class="km-hero__title">Alle Projekte auf einen Blick</h2><p class="km-hero__text">…</p></div>
<ul class="km-features"><li class="km-feature"><span class="km-feature__icon">…</span><h3 class="km-feature__title">Suche</h3><p class="km-feature__text">Findet Projekte und Aufgaben.</p></li></ul>
```

## Aufbau, Größen, Zustände

| Teil | Funktion |
|---|---|
| `km-intro` | Container-Abfrage; Fläche `inset`; Bild 16:9 (breit 16:10), Bildspalte `clamp(15rem, 48cqw, 37.5rem)`; Kante oben am Bild in der Kartenfarbe. |
| `__body--short` | kürzt nach fünf Zeilen (`line-clamp`); „Weiterlesen“ setzt die Seite. |
| `__more` | Text-Knopf im Akzent, unterstrichen; Zustand `aria-expanded`. |
| `km-hero` | Kopf im Akzent, Titel `--km-font-display` `--km-font-size-xl`, Text bis 62ch; `> .km-facts` mit Abstand. |
| `km-features` | Raster ab 16rem, Kachel mit Symbol-Kachel `--km-icon-tile`, Titel `l`, Text `m`. |

Zustände: `__more` Fokus mit Ring (siehe offene Punkte), deaktiviert abgeblendet; sonst statisch.

## Barrierefreiheit

- Bild mit Alt-Text, der das Bild beschreibt; dekorative Bilder `alt=""`.
- `__more` mit `aria-expanded` und `aria-controls`.
- Kontrast (gerechnet): Lead `--km-color-text` auf `--km-color-inset` 12,88 / 14,57 / 12,06 / 16,15; Text `--km-color-text-muted` auf `inset` 7,18 / 7,20 / 7,93 / 7,14; Kopf `--km-color-accent` auf `--km-color-section` 8,82 / 5,70 / 8,68 / 7,61; „Weiterlesen“ Akzent auf `inset` 7,52 / 6,14 / 7,43 / 7,42 (Kobalt dunkel, Kobalt hell, Papier dunkel, Papier hell).

## Beispiele

### Falsch

```html
<img src="…" style="width:300px">  <!-- feste Breite statt Container-Raster -->
<p class="km-intro__body" style="max-height:5em;overflow:hidden">…</p>  <!-- eigene Kürzung -->
```

## Seitenregeln

Schmal prüfen (Bild über dem Text unter 40rem); keine harten Werte; Raster mit `minmax(min(…, 100%), 1fr)`. Entscheidungen: 17 (Schrift), 27 (schmale Breite).

## Vergleich mit anderen Design-Systemen

| System | Name | Besonderheit | Quelle |
|---|---|---|---|
| KERN 2.8.2 | – | ungeprüft | – |

## Verwandte Bausteine

`km-card`, `km-facts`, `km-section__lead`, `km-agent__grid`.

## Tokens

- `--km-color-inset`, `--km-color-card`, `--km-color-border-card`, `--km-color-text`, `--km-color-text-muted`, `--km-color-accent`, `--km-font-display`, `--km-font-size-m`/`-l`/`-xl`, `--km-icon-tile`, `--km-icon-l`, `--km-card-accent`.
- Hart: `30ch`, `62ch`, `16rem`, `40rem`, `clamp(15rem, 48cqw, 37.5rem)`.

## Offene Punkte

- `km-hero` Zweck „werblich“ in einem Werkzeug: Einsatz auf Über-Bereiche begrenzen.

## Regeln

- Was: Drei Einstiegsbausteine: `km-intro` setzt Bild, Lead und Text als eine Fläche (ab 40rem Bild links, Text nach fünf Zeilen gekürzt mit „Weiterlesen“), `km-hero` ist der werbliche Einstieg ohne Bild mit Kopfzeile, Schlagzeile, Einleitung und optional Kennzahlen, `km-features` zeigt Funktionen als Kacheln mit Symbol, Titel und ein bis zwei Sätzen.
- Wann: `km-intro` oben in einer Projektkarte, `km-hero` und `km-features` für Über-Bereiche; für nur einen Satz `km-section__lead` bzw. die erste `km-note`, für mehr als sechs Funktionen Liste oder Tabelle, für Inhalt im Raster `km-card`.
- Wie: `km-intro__inner` mit `__media` (`figure` mit `img` und Alt-Text) und `__text` aus `__lead`, `__body--short` und Knopf `__more` mit `aria-expanded` und `aria-controls`; Raster mit `minmax(min(…, 100%), 1fr)`, keine festen Breiten, keine eigene Kürzung, keine harten Werte.
- Prüfen: Fertig ist es, wenn das Bild unter 40rem über dem Text steht, der Alt-Text das Bild beschreibt (dekorative Bilder `alt=""`), `__more` mit Ring fokussierbar ist und seinen Zustand über `aria-expanded` meldet und Lead, Text, Kopf und „Weiterlesen“ in allen Themes mindestens 4,5:1 messen.
