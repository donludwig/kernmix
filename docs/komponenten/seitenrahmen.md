# Seitenrahmen: Fläche, Fußzeile, Eckleiste, Nach oben (`km-page`, `km-footer`, `km-corner`, `km-totop`)

Status: stabil, in Dashboard und Lagebild im Einsatz · Story: `docs/index.html#teilstuecke`, `#eckleiste`, `#kleinteile` (`km-totop`), `#kennzahlen`, `#zustaende-skript` · CSS: `src/km-components.css`, Abschnitte „Demo-Schalter“ (Eckleiste), „Fußzeile mit Kennzahlen“, „Info-i, Nach oben“, „Dashboard-Gerüst“ · Stand: 2026-11-09

## Kurzbeschreibung

Die Teile rund um den Inhalt einer Werkzeugseite: `km-page` setzt Seitenfläche, Textfarbe und Schrift. `km-footer` ist die Fußzeile mit Kennzahlen (`__top`, `__stats`, `__sub`), Meta-Zeile (`__meta`) und Zurücksetzen (`__reset`). Die Eckleiste `km-corner` steht fest unten links mit dezenten Werkzeug-Einträgen wie Demo-Schalter und Link zur Komponentenbeschreibung. `km-totop` ist der Knopf „Nach oben“ unten rechts, der erst nach dem Scrollen erscheint.

## Name und Abgrenzung

- Kopfzeile und Seitenleiste haben eigene Dokus (`kopfzeile.md`, `seitenleiste.md`).
- Kennzahlen in der Fußzeile nutzen `km-bars` (siehe `kennzahlen.md`).

## Einsatz

### Verwenden, wenn

- eine Werkzeugseite ihren Rahmen braucht: einmal je Seite;
- Werkzeug-Einträge nicht zur Seite gehören: Eckleiste.

### Nicht verwenden, wenn

- Einträge zur Seite selbst gehören: nicht in die Eckleiste.

## Verwendung

```html
<body class="km-page">
  …
  <footer class="km-footer"><div class="km-footer__top"><span class="km-footer__stats"><strong>64</strong> Projekte <span class="km-footer__sub">· 662 h</span></span><button type="button" class="km-footer__reset" aria-label="Ansicht zurücksetzen">…</button></div><p class="km-footer__meta">Stand 09.11.2026</p></footer>
  <div class="km-corner"><button type="button" class="km-demo km-demo--fixed" role="switch" aria-checked="false"><i aria-hidden="true"></i>Demo</button><a class="km-corner__link" href="storybook/">…Komponentenbeschreibung</a></div>
  <button type="button" class="km-totop" aria-label="Nach oben">…</button>
</body>
```

## Aufbau und Zustände

| Teil | Klasse | Funktion / Zustand |
|---|---|---|
| Fläche | `km-page` | `--km-color-page`, `--km-color-text`, `--km-font`. |
| Fußzeile | `km-footer`, `__top`, `__stats`, `__sub`, `__meta` | `margin-top: auto`, Abstand `--km-space-page`, gedämpft, Zahlen kräftig. |
| Zurücksetzen | `km-footer__reset` | Quadrat `--km-icon-l`, Hover Text voll. |
| Eckleiste | `km-corner`, `__link` | `fixed` unten links, `z-index: 60`, dezent; Hover und Fokus hell, Link unterstrichen. |
| Nach oben | `km-totop`, `--visible` | `fixed` unten rechts, unsichtbar und nicht klickbar, bis das Skript `--visible` setzt. |

## Verhalten

Sichtbarkeit von „Nach oben“, Zurücksetzen und Demo-Wechsel setzt das Skript der Seite.

## Barrierefreiheit

- `km-totop` ohne `--visible` hat `opacity: 0` und `pointer-events: none`, ist aber weiter fokussierbar; die Seite sollte `tabindex="-1"` oder `hidden` setzen, solange er unsichtbar ist.
- Eckleiste: `--km-color-text-dim` auf `--km-color-page` 7,02 / 5,40 / 6,51 / 5,61 (Kobalt dunkel, Kobalt hell, Papier dunkel, Papier hell).
- Feste Elemente dürfen bei 390 px nichts verdecken (Seitenregeln „Keine Überlappungen“).

## Beispiele

### Falsch

```html
<div style="position:fixed;bottom:8px;left:12px">Demo</div>  <!-- eigene Eckleiste mit harten Werten -->
```

## Seitenregeln

Keine Überlappungen; keine harten Werte; Logo bzw. Zurücksetzen setzt Filter, Suche, Sortierung zurück, Spaltenauswahl bleibt. Entscheidungen: 18, 22, 27.

## Vergleich mit anderen Design-Systemen

| System | Name | Besonderheit | Quelle |
|---|---|---|---|
| KERN 2.8.2 | Footer | ungeprüft | – |

## Verwandte Bausteine

`km-header`, `km-sidebar`, `km-bars`, `km-demo`.

## Tokens

- `--km-color-page`, `--km-color-card`, `--km-color-text`, `--km-color-text-dim`, `--km-color-text-muted`, `--km-color-border-card`, `--km-space-page`, `--km-space-tight`, `--km-icon-l`, `--km-icon-tile`, `--km-shadow`.
- Hart: `km-totop` `bottom/right: 1.5rem`, `z-index: 99`; `km-corner` `z-index: 60`.

## Offene Punkte

- Unsichtbarer „Nach oben“-Knopf bleibt im Tab-Fluss.
- `km-footer__reset` und `km-totop` in Mono-Grundform (gemeinsame Knopf-Regel); beide sind Nur-Icon-Knöpfe und könnten `km-iconbtn` sein.

## Regeln

- Was: Der Seitenrahmen besteht aus `km-page` (Fläche, Textfarbe, Schrift), `km-footer` (Fußzeile mit Kennzahlen, Meta-Zeile und Zurücksetzen), `km-corner` (Eckleiste unten links für Werkzeug-Einträge) und `km-totop` (Knopf „Nach oben“ unten rechts, sichtbar mit `--visible`).
- Wann: Einmal je Werkzeugseite als Rahmen; Werkzeug-Einträge ohne Bezug zur Seite gehören in die Eckleiste, Einträge, die zur Seite selbst gehören, nicht.
- Wie: `km-page` am `body`, Fußzeile mit `km-footer__top`, `__stats`, `__sub`, `__meta` und `km-footer__reset` mit `aria-label`, `km-corner` mit `km-corner__link`, `km-totop` mit `aria-label="Nach oben"`; Lage und Abstände über Tokens, keine eigene Eckleiste mit harten Werten.
- Prüfen: Fertig ist es, wenn `km-totop` ohne `--visible` unsichtbar und nicht fokussierbar ist (`tabindex="-1"` oder `hidden`), der Text der Eckleiste (`--km-color-text-dim` auf `--km-color-page`) in allen Themes mindestens 4,5:1 misst und feste Elemente bei 390 px nichts verdecken.
