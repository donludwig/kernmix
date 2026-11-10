# Schalter und Kästchen (`km-switch`, `km-check`, `km-demo`, `km-sync`)

Status: stabil, in Dashboard und Lagebild im Einsatz · Story: `docs/index.html#schalter`, `#kontrollkaestchen`, `#seitenleiste`, `#sidebar-hierarchie`, `#kleinteile` (`km-sync`) · CSS: `src/km-components.css`, Abschnitte „Schalter“, „Demo-Schalter“, „Kontrollkästchen“, „Einheitliche Bedienelemente“ (Schalter), „Info-i, Nach oben, Sync-Schalter“ · Stand: 2026-11-09

## Kurzbeschreibung

Der Schalter `km-switch` schaltet eine Einstellung sofort an oder aus, etwa „Nur offene“ oder ob ein Bereich sichtbar ist. Er ist ein Knopf mit `role="switch"` und einem kleinen Schiebeknopf, an gefüllt im Akzent. Das Kästchen `km-check` ist die kompakte Fassung der KERN-Checkbox für Aufgaben, Spalten- und Mehrfachauswahl. Der Demo-Schalter `km-demo` ist ein dezenter Schalter in der Fensterecke; `km-sync` ein Umschalter mit Text für eine Verbindung im Kopf.

## Name und Abgrenzung

- `km-switch` + `km-switch__knob`; `km-check` (auch `km-task__check`, Kästchen im Spalten-Panel); `km-demo` (`--fixed`); `km-sync` (`--on`).
- Schalter = Einstellung, die sofort wirkt. Kästchen = Auswahl einer oder mehrerer Dinge, die zusammen gelten. Segmented Control = eine von mehreren Ansichten.
- Für Formulare gelten KERN-Checkbox (`kern-form-check__checkbox`, 32 px) und KERN-Radio.

## Einsatz

### Verwenden, wenn

- eine Einstellung ohne „Speichern“ sofort gilt (Schalter);
- in einer Liste Dinge markiert werden (Kästchen);
- ein Bereich der Seite ein- und ausgeblendet wird (Schalter im Eintrag der Seitenleiste).

### Nicht verwenden, wenn

- die Wahl erst mit Absenden gilt: KERN-Checkbox im Formular;
- zwischen Ansichten gewechselt wird: `km-segmented`;
- eine Aktion ausgelöst wird: Knopf.

## Verwendung

```html
<button type="button" class="km-switch" role="switch" aria-checked="true"><span class="km-switch__knob" aria-hidden="true"></span>Aufgaben</button>
<label><input type="checkbox" class="km-check" checked>Lagebild</label>
```

## Aufbau

| Teil | Klasse | Funktion |
|---|---|---|
| Schalter | `km-switch` | Knopf ohne Rahmen, Text gedämpft, an voll. |
| Schiebeknopf | `km-switch__knob` | Spur 1.6rem × 0.9rem (`--km-color-track`), Knopf quadratisch, an rechts. |
| Kästchen | `km-check` | `appearance: none`, Quadrat `--km-icon` (16 px), Rand 2 px `--km-color-border-input`, Haken in `--km-color-on-accent`. |
| Demo | `km-demo`, `km-demo i` | Schalter mit Text in Versalien-Laufweite; `--fixed` unten links fest. |
| Sync | `km-sync`, `--on` | gerahmter Umschalter mit Icon und Text. |

## Varianten

Schalter mit Text; Schalter ohne Text in `km-sidebar__row` (Name per `aria-label`); Schalter als Eintrag der Seitenleiste (`km-sidebar__item[role="switch"]`); Kästchen; Demo; Sync.

## Größen

Schalter 28,00 px hoch mit Text, Schiebeknopf 25,59 × 14,39 px (gemessen, Kobalt dunkel); Kästchen 16 px.

## Zustände

| Zustand | Auslöser | Darstellung | Tokens |
|---|---|---|---|
| Aus | `aria-checked="false"` | Spur `track`, Knopf links `text-dim`, Text gedämpft | `--km-color-track`, `--km-color-text-dim` |
| An | `aria-checked="true"` | Spur Akzent, Knopf rechts `on-accent`, Text voll | `--km-color-accent` |
| Fokus | `:focus-visible` | Ring außen | `--km-color-focus` |
| Deaktiviert | `disabled`, `aria-disabled` | abgeblendet | `--km-opacity-disabled` |
| Kästchen Hover | `:hover` | Rand Akzent | – |
| Kästchen an | `:checked` | Fläche Akzent, Haken | `--km-color-on-accent` |
| Kästchen deaktiviert | `:disabled` | abgeblendet | – |
| Sync an | `km-sync--on` | Text und Rand Akzent, kein Zeiger | – |

## Verhalten

- Die Seite setzt `aria-checked` bzw. `checked`, wendet die Einstellung an und speichert sie; ein Schalter der Navigation hebt einen gesetzten Listenfilter auf (Seitenregeln „Filter und Verlauf“).
- Die Bewegung des Knopfs dauert 0,15 s.

## Text und Wording

Schalter: Gegenstand, der an ist („Aufgaben“, „Nur offene“), nicht „An/Aus“; die Beschriftung bleibt in beiden Zuständen gleich.

## Barrierefreiheit

- `role="switch"` mit `aria-checked` am Knopf; Schiebeknopf `aria-hidden`. Ohne sichtbaren Text `aria-label` („Aufgaben anzeigen“).
- Kästchen nativ, im `label`.
- Zustand nicht nur über Farbe: Lage des Knopfs.
- Kontrast (gerechnet):

| Paar | Kobalt dunkel | Kobalt hell | Papier dunkel | Papier hell |
|---|---|---|---|---|
| Text aus `--km-color-text-muted` auf `--km-color-card` | 7,89 | 7,85 | 8,57 | 7,79 |
| Knopf aus `--km-color-text-dim` auf `--km-color-track` | 4,88 | 4,62 | 4,57 | 4,94 |
| Spur aus `--km-color-track` auf `--km-color-card` | 1,28 | 1,31 | 1,27 | 1,26 |
| Spur an `--km-color-accent` auf `--km-color-card` | 8,27 | 6,69 | 8,02 | 8,09 |
| Knopf an `--km-color-on-accent` auf `--km-color-accent` | 9,13 | 6,69 | 8,68 | 8,38 |
| Kästchen-Rand `--km-color-border-input` auf `--km-color-card` | 6,25 | 6,05 | 5,78 | 6,23 |

Die Spur im Aus-Zustand hebt sich kaum ab (≈ 1,3:1, Rand `border-card` ≈ 1,4:1); erkennbar ist der Schalter am Knopf (≥ 4,5:1).

## Beispiele

### Richtig

```html
<div class="km-sidebar__row"><a class="km-sidebar__item" href="#aufgaben">Aufgaben</a><button type="button" class="km-switch" role="switch" aria-checked="true" aria-label="Aufgaben anzeigen"><span class="km-switch__knob" aria-hidden="true"></span></button></div>
```

### Falsch

```html
<button class="km-switch" aria-pressed="true">…</button>      <!-- Umschalter-Knopf statt switch -->
<input type="checkbox" style="width:12px">                   <!-- eigenes Kästchen statt km-check -->
<div class="km-sidebar__group"><p>Anzeigen</p>…nur Schalter…</div>  <!-- zweite Liste nur mit Schaltern -->
```

## Seitenregeln

Aus `docs/seitenregeln.md`: Schalter im Eintrag der Seitenleiste, keine zweite Liste nur mit Schaltern; ein Filter zur Zeit; Ränder von Kästchen ≥ 3:1; Eckleiste dezent.

Entscheidungen: 15 (Kontrast), 21 (Seitenleiste), 22 (Filter).

## Vergleich mit anderen Design-Systemen

| System | Name | Besonderheit | Quelle |
|---|---|---|---|
| Primer (GitHub) | ToggleSwitch | „used to immediately toggle a setting on or off“; Name über `aria-labelledby` Pflicht; Zustand Laden mit Ansage | primer.style/product/components/toggle-switch |

## Verwandte Bausteine

`km-sidebar`, `km-selectpanel`, `km-colpicker`, `km-task`, `km-corner`, `km-segmented`.

## Tokens

- Rollen: `--km-color-track`, `--km-color-border-card`, `--km-color-border-input`, `--km-color-text-dim`, `--km-color-text-muted`, `--km-color-text`, `--km-color-accent`, `--km-color-on-accent`, `--km-color-page`, `--km-control-height`, `--km-space-3xs`, `--km-icon`, `--km-border-width-strong`.
- Hart: Spurhöhe `0.9rem`, Dauer `0.15s`.

## Offene Punkte

- Spur aus unter 3:1; Rand der Spur auf `--km-color-border-input` heben?
- `km-demo i` und `km-switch__knob` sind zwei gleiche Regeln; zusammenführen.
- `km-sync` und `km-toolbar__btn` in Mono; Seitenregel „keine Text-Knöpfe in Mono“.
- Kein Laden-Zustand.

## Regeln

- Was: `km-switch` schaltet eine Einstellung sofort an oder aus (Knopf mit `role="switch"` und `km-switch__knob`), `km-check` ist das kompakte Kästchen für Aufgaben, Spalten- und Mehrfachauswahl, `km-demo` ein dezenter Schalter in der Fensterecke und `km-sync` ein Umschalter mit Text.
- Wann: Ein Schalter für eine Einstellung, die ohne Speichern gilt, ein Kästchen für markierte Dinge in einer Liste; gilt die Wahl erst mit Absenden, nimm die KERN-Checkbox, wechselt man zwischen Ansichten `km-segmented`, löst man eine Aktion aus einen Knopf.
- Wie: `<button type="button" class="km-switch" role="switch" aria-checked="true">` mit `km-switch__knob` (`aria-hidden`), Beschriftung als Gegenstand wie „Aufgaben“ und in beiden Zuständen gleich, ohne sichtbaren Text `aria-label`; Kästchen als nativer `input.km-check` im `label`; in der Seitenleiste als Schalter im Eintrag, keine zweite Liste nur mit Schaltern.
- Prüfen: Fertig ist es, wenn An, Aus, Fokus und Deaktiviert der Tabelle erreichbar sind, der Zustand auch an der Lage des Knopfs erkennbar ist, Text und Knopf in allen Themes mindestens 4,5:1 messen und der Kästchen-Rand mindestens 3:1 erreicht.
