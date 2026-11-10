# Dialog-Zusätze (`km-dialog`, `km-btn--danger`)

Status: stabil, im Dashboard im Einsatz · Story: `docs/index.html#dialog` · CSS: `src/km-components.css`, Abschnitte „Gefahr-Knopf“, „Dialog-Fußleiste“ · Stand: 2026-11-09

## Kurzbeschreibung

Der Dialog ist der KERN-Dialog (`kern-dialog`, natives `<dialog>` mit `showModal()`). Das Kit ergänzt nur, was Werkzeugseiten brauchen: zentriert auch bei Seiten mit eigenem Reset, Inhalt in voller Breite, Kopf mit Etikett auf einer Linie, Fußleiste in einer Reihe mit einem Knopf links (`km-dialog__start`, etwa Löschen), Icons in Knöpfen in der Label-Farbe, und den Gefahr-Zustand `km-btn--danger` für den zweiten Klick beim Löschen.

## Name und Abgrenzung

- Kein eigener Dialog: `kern-dialog` mit KERN-Klassen; Zusätze `km-dialog__start`, `kern-btn.km-btn--danger`, `kern-btn > .km-icon`.
- `km-selectpanel`: nicht-modales Panel am Knopf; der Dialog ist modal.

## Einsatz

### Verwenden, wenn

- mehrere Felder einer Sache bearbeitet werden;
- eine Bestätigung Folgen hat.

### Nicht verwenden, wenn

- es um eine einfache Auswahl geht: Panel;
- eine Kleinigkeit bestätigt werden soll: zweistufiger Knopf im Menü statt `confirm`-Ersatz.

## Verwendung

```html
<dialog class="kern-dialog" aria-labelledby="d-titel">
  <header class="kern-dialog__header"><h2 class="kern-title" id="d-titel">Liste bearbeiten</h2><span class="km-chip km-chip--muted">Quickliste</span>…</header>
  <section class="kern-dialog__body">…</section>
  <footer class="kern-dialog__footer">
    <button type="button" class="kern-btn kern-btn--tertiary km-dialog__start"><svg class="km-icon" aria-hidden="true">…</svg><span class="kern-label">Löschen</span></button>
    <button type="button" class="kern-btn kern-btn--secondary"><span class="kern-label">Abbrechen</span></button>
    <button type="button" class="kern-btn kern-btn--primary"><span class="kern-label">Speichern</span></button>
  </footer>
</dialog>
```

## Zustände

| Zustand | Auslöser | Darstellung |
|---|---|---|
| Offen | `showModal()` | zentriert, höchstens 48rem bzw. Fenster minus 2 × 16 px |
| Löschen, zweiter Schritt | `km-btn--danger` am KERN-Knopf | Fläche rot, Text `--km-color-on-attention` |

## Barrierefreiheit

- Modal mit `showModal()` (Fokusfang und Esc nativ), Titel über `aria-labelledby`, Fokus nach dem Schließen zurück an den Auslöser.
- Gefahr-Knopf: `--km-color-on-attention` auf danger 6,14 / 6,01 / 7,19 / 6,20 (Kobalt dunkel, Kobalt hell, Papier dunkel, Papier hell).
- Knöpfe nie unterstrichen.

## Beispiele

### Falsch

```js
if (confirm('Wirklich löschen?')) …   // Browser-Dialog
```

## Seitenregeln

Bearbeiten im Menü, Löschen unten, zweistufig, kein `confirm`. Entscheidung 24.

## Vergleich mit anderen Design-Systemen

| System | Name | Besonderheit | Quelle |
|---|---|---|---|
| KERN 2.8.2 | Dialog | Basis dieses Bausteins; Doku siehe KERN-Verweise in der Komponentenbeschreibung | – |

## Tokens

- `--km-color-on-attention`, `--km-color-accent`, `--km-icon`, `--km-space-xs`, `--km-space-m`; Rückmelde-Rolle `--km-color-feedback-danger`; Breite über `--kern-small` (laut Changelog 0.6.0 im Kit nicht definiert, Rückfall 48rem).
- `--border-radius-large: 0` in den Rollen (KERN-Wert unter 768 px).

## Offene Punkte

- Präfix `km-btn` neben `km-button` und `km-iconbtn`: drei Knopf-Präfixe.

## Regeln

- Was: Der Dialog ist der KERN-Dialog `kern-dialog` (natives `<dialog>` mit `showModal()`); das Kit ergänzt die zentrierte Lage, die Fußleiste in einer Reihe mit Knopf links (`km-dialog__start`), Etikett im Kopf, Icons in Knöpfen und den Gefahr-Zustand `km-btn--danger` für den zweiten Klick beim Löschen.
- Wann: Wenn mehrere Felder einer Sache bearbeitet werden oder eine Bestätigung Folgen hat; für eine einfache Auswahl das Panel `km-selectpanel`, für eine Kleinigkeit ein zweistufiger Knopf im Menü, nie ein `confirm`.
- Wie: `<dialog class="kern-dialog" aria-labelledby>` mit `kern-dialog__header` (`h2.kern-title`, optional `km-chip`), `kern-dialog__body` und `kern-dialog__footer`, Löschen als `kern-btn--tertiary km-dialog__start` links, dann `kern-btn--secondary` und `kern-btn--primary`, Icons als `svg.km-icon` mit `aria-hidden="true"` vor `kern-label`.
- Prüfen: Fertig ist es, wenn der Dialog mit `showModal()` zentriert öffnet (höchstens 48rem bzw. Fenster minus 2 × 16 px), Fokusfang und Esc nativ greifen, der Fokus nach dem Schließen an den Auslöser zurückgeht, der Gefahr-Knopf mit `--km-color-on-attention` auf danger mindestens 6,01 erreicht und Knöpfe nie unterstrichen sind.
