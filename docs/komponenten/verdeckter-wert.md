# Verdeckter Wert (`km-secret`)

Status: stabil, im Lagebild im Einsatz · Story: `docs/index.html#verdeckt` · CSS: `src/km-components.css`, Abschnitt „Für das Lagebild“ · Stand: 2026-11-09

## Kurzbeschreibung

Der verdeckte Wert zeigt ein Passwort oder einen Schlüssel zunächst als Platzhalter. Ein Klick auf den Knopf zeigt den Wert, ein zweiter verdeckt ihn wieder. Daneben steht ein Kopier-Knopf, der nach dem Kopieren kurz grün wird. Wert und Verhalten liefert die Seite; der verdeckte Zustand wird nie gespeichert.

## Name und Abgrenzung

- Klasse `km-secret`, Zustand `aria-pressed`; Kopieren `km-iconbtn` mit `km-iconbtn--done`.
- Kein Eingabefeld: zum Eingeben eines Passworts gilt das KERN-Eingabefeld.

## Einsatz

### Verwenden, wenn

- eine Werkzeugseite Zugänge mit Passwörtern oder Schlüsseln zeigt, die auf Bildschirmfotos und bei geteiltem Bildschirm nicht sichtbar sein dürfen (Entscheidung 26), etwa die Demo-Ordner im Lagebild (das Migrationsprotokoll);
- der Wert in einer Tabellenzelle steht, Spalte „Passwort“ mit Rolle `__nowrap` (`docs/seitenregeln.md`, „Rolle je Spalte“; CSS `.km-table td > .km-secret`).

### Nicht verwenden, wenn

- ein Passwort eingegeben wird: KERN-Eingabefeld.

## Verwendung

```html
<button type="button" class="km-secret" aria-pressed="false" aria-label="Passwort anzeigen">••••••</button><button type="button" class="km-iconbtn" aria-label="Passwort kopieren">…</button>
```

## Aufbau, Größen, Zustände

| Zustand | Auslöser | Darstellung |
|---|---|---|
| Verdeckt | `aria-pressed="false"` | Platzhalter, Mono 12 px, Fläche `inset`, Rand `border-card`, mindestens 5.5rem breit, `--km-control-height` hoch |
| Gezeigt | `aria-pressed="true"` | Wert, Rand im Akzent (auch unter der Maus) |
| Hover | `:hover` | Rand `border-section` |
| Kopiert | `km-iconbtn--done` am Nachbarn | grün |

## Barrierefreiheit

- Die Beschriftung für Screenreader wechselt mit dem Zustand („Passwort anzeigen“ / „Passwort verdecken“), weil der sichtbare Inhalt der Platzhalter ist.
- Gezeigte Werte nicht in `aria-live` ansagen.
- Kontrast: Text `--km-color-text` auf `--km-color-inset` 12,88 / 14,57 / 12,06 / 16,15; Rand gezeigt Akzent auf `inset` 7,52 / 6,14 / 7,43 / 7,42 (Kobalt dunkel, Kobalt hell, Papier dunkel, Papier hell).

## Beispiele

### Falsch

Passwort im Klartext in Story, Doku, Changelog oder Ausgabe; verdeckten Zustand in localStorage speichern.

## Seitenregeln

- „Geheimnisse“: Passwörter starten verdeckt, jedes Feld einzeln umschaltbar, Knopf „Passwörter“ in der Kopfzeile für alle, Zustand nie gespeichert; Werte nie in Doku, Stories, Memory; Werte erst beim Klick aus der Zeile lesen.
- Entscheidung 26.

## Vergleich mit anderen Design-Systemen

| System | Name | Besonderheit | Quelle |
|---|---|---|---|
| GOV.UK Design System | Password input | ungeprüft | – |

## Tokens

- `--km-control-height`, `--km-font-mono`, `--km-font-size-xs`, `--km-tracking-caps`, `--km-color-text`, `--km-color-inset`, `--km-color-border-card`, `--km-color-border-section`, `--km-color-accent`.
- Hart: `min-width: 5.5rem`.

## Offene Punkte

- Der Wechsel der Beschriftung (`aria-label`) ist Sache der Seite; ein Vertrag (welche Texte) fehlt im Kit.

## Regeln

- Was: Der verdeckte Wert `km-secret` zeigt ein Passwort oder einen Schlüssel zunächst als Platzhalter, ein Klick zeigt den Wert, ein zweiter verdeckt ihn wieder; daneben steht ein Kopier-Knopf `km-iconbtn`, der nach dem Kopieren mit `km-iconbtn--done` kurz grün wird.
- Wann: Für Passwörter und Schlüssel auf Werkzeugseiten, die auf Bildschirmfotos und bei geteiltem Bildschirm nicht sichtbar sein dürfen, auch in einer Tabellenzelle der Spalte „Passwort“; zum Eingeben eines Passworts gilt das KERN-Eingabefeld, nicht dieser Baustein.
- Wie: `button.km-secret` mit `aria-pressed` und einem `aria-label`, das mit dem Zustand wechselt („Passwort anzeigen“ / „Passwort verdecken“), Kopier-Knopf daneben mit `aria-label`; Passwörter starten verdeckt, jedes Feld einzeln umschaltbar, der Wert wird erst beim Klick aus der Zeile gelesen und nie in Doku, Stories oder Memory geschrieben.
- Prüfen: Fertig ist es, wenn verdeckt und gezeigt (Rand im Akzent, auch unter der Maus) unterscheidbar sind, der Text auf `--km-color-inset` in allen Themes mindestens 4,5:1 misst, gezeigte Werte nicht in `aria-live` angesagt werden und der verdeckte Zustand nirgends gespeichert wird.
