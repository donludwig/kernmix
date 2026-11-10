# Aufgabe und Vorschläge (`km-task`, `km-suggest`)

Status: stabil, im Dashboard im Einsatz · Story: `docs/index.html#aufgabe`, `#aufgabe-loeschen`, `#vorschlaege`, `#zustaende`, `#zustaende-skript`, `#trefferliste` (`--treffer`) · CSS: `src/km-components.css`, Abschnitte „Aufgabe“, „KI-Vorschläge“, „Info-i, Nach oben, Sync-Schalter, Suchfeld“ (`__confirm`) · Stand: 2026-11-09

## Kurzbeschreibung

Die Aufgabe ist eine Karte mit Kästchen zum Abhaken, Titel samt Kennung und Status-Pill, Kurztext, nächstem Schritt, Meta mit Projektlink, aufklappbaren Details und einer Aktionsleiste unten. „In Arbeit“ zeigt eine Kante in der Signalfarbe, erledigt wird gedämpft statt abgeblendet. Löschen braucht einen zweiten Schritt direkt in der Karte. Vorschläge (`km-suggest`) sind automatisch erzeugte Aufgaben in einem gestrichelten, aufklappbaren Block, die man übernehmen oder zurückstellen kann.

## Name und Abgrenzung

- `km-task` (`__check`, `__body`, `__title`, `__id`, `__text`, `__next`, `__meta`, `__details`, `__actions`, `__confirm`, `__confirm-yes`, `__status`), Varianten `--starred`, `--dragging`, `--deactivated`, `--treffer`; `km-suggest` (`__summary`, `__note`, `__list`, `__task`, `__task--promoted`, `__tag`, `__promote`, `__demote`).
- `km-card`: allgemeine Karte ohne Kästchen. Tickets selbst (Inhalt, Fälligkeit) liefert die Seite.

## Einsatz

### Verwenden, wenn

Aufgaben mit Status und nächstem Schritt in einer Spalte oder Projektkarte stehen.

### Nicht verwenden, wenn

eine reine Checkliste ohne Status gebraucht wird: Liste mit `km-check`.

## Verwendung

```html
<div class="km-task km-task--starred">
  <input type="checkbox" class="km-task__check" aria-label="Erledigt: Nutzertest vorbereiten">
  <div class="km-task__body">
    <div class="km-task__title"><span>Nutzertest vorbereiten</span><span class="km-task__id">DEMO-1</span><span class="km-pill km-pill--info">in 4 Tagen</span></div>
    <p class="km-task__text">Fünf Termine vorbereiten.</p>
    <p class="km-task__next"><strong>Nächster Schritt:</strong> Aufgaben schreiben.</p>
  </div>
  <div class="km-task__actions"><button type="button" class="km-iconbtn" aria-label="Bearbeiten">…</button><button type="button" class="km-iconbtn km-iconbtn--danger" aria-label="Löschen">…</button></div>
</div>
```

## Zustände

| Zustand | Auslöser | Darstellung | Tokens |
|---|---|---|---|
| Offen | – | Kartenfläche, Status als Pill (offen = info, wartet = warn, erledigt = ok, überfällig = danger) | – |
| Hover | `:hover` | Rand `border-section` | – |
| In Arbeit | `km-task--starred` | Kante links in der Signalfarbe (Innenschatten) | `--km-color-attention` |
| Erledigt | `__check:checked` | Text gedämpft (kein Abblenden) | `--km-color-text-muted` |
| Details zu | `details.km-task__details` | nur „Details“ mit Pfeil | – |
| Details offen | `details.km-task__details[open]` | Notizen unter der Zeile, Pfeil nach unten; die Story zeigt beide Zustände (DEMO-1 zu, DEMO-3 offen) | – |
| Löschen bestätigen | `km-task__confirm` | Rahmen rot, 8 % Tönung, Bestätigen gefüllt rot | `--km-color-feedback-danger`, `--km-color-on-attention` |
| Ziehen | `--dragging` | 40 % abgeblendet, gestrichelt | – |
| Ausgeschaltet | `--deactivated` | gesetzt vom Skript | – |
| Sprungziel | `--treffer` | Rahmen in Fokusfarbe | `--km-color-focus` |
| Vorschlag | `km-suggest__task` | gestrichelter Rand, Etikett „KI“ | – |
| Übernommen | `__task--promoted` | durchgezogener Rand, Status im Akzent | – |

## Verhalten

Abhaken, Stern, Bearbeiten, Löschen (zweistufig, kein `confirm`), Ziehen, Übernehmen: Skript der Seite.

## Text und Wording

Titel als Tätigkeit („Nutzertest vorbereiten“); nächster Schritt mit „Nächster Schritt:“; Status-Pill mit Frist („in 4 Tagen“).

## Barrierefreiheit

- Kästchen mit `aria-label` „Erledigt: <Titel>“.
- Erledigt bleibt lesbar: gedämpft ≥ 4,5 (`--km-color-text-muted` auf `--km-color-card` 7,89 / 7,85 / 8,57 / 7,79).
- „In Arbeit“ nicht nur über die Kante: der Stern-Knopf trägt `aria-pressed`.
- Bestätigen: `--km-color-on-attention` auf danger 6,14 / 6,01 / 7,19 / 6,20; Hinweistext auf 8 % Tönung 12,79 / 13,91 / 11,48 / 15,59 (Kobalt dunkel, Kobalt hell, Papier dunkel, Papier hell).

## Beispiele

### Falsch

```html
<div class="km-task" style="opacity:.4">…erledigt…</div>      <!-- Abblenden für Inhalt -->
<button onclick="confirm('Löschen?')">…</button>             <!-- Browser-Dialog statt zweitem Schritt -->
```

## Seitenregeln

- Kein Abblenden mit `opacity` für Inhalt („Erledigt“ ist nicht deaktiviert); Farbkanten als Innenschatten; Löschen zweistufig ohne `confirm`.
- Entscheidungen: 15, 18, 24.

## Vergleich mit anderen Design-Systemen

| System | Name | Besonderheit | Quelle |
|---|---|---|---|
| GOV.UK Design System | Task list | ungeprüft | – |

## Verwandte Bausteine

`km-check`, `km-pill`, `km-iconbtn`, `km-chip`, `km-card`, `km-dnd`.

## Tokens

- `--km-color-card`, `--km-color-border-card`, `--km-color-border-section`, `--km-color-track`, `--km-color-text`, `--km-color-text-muted`, `--km-color-text-dim`, `--km-color-attention`, `--km-color-on-attention`, `--km-color-accent`, `--km-color-focus`, `--km-space-block`, `--km-border-width-accent`.
- Rückmelde-Rollen: `--km-color-feedback-danger`.
- Hart: Tönungen 8, 12, 30 %, `font-weight: 600`, `!important` in `__task--promoted`.

## Offene Punkte

- Regeln für `__text`, `__next`, `__actions`, `__body` stehen doppelt (Abschnitt „Feinwerte aus dem Dashboard“ überschreibt den ersten).
- `--deactivated` hat keine eigene Darstellung im Kit, nur Ausnahmen für `__confirm`.
- `km-suggest__promote` und `__demote` in Mono (gemeinsame Knopf-Regel).

## Regeln

- Was: `km-task` ist eine Aufgabenkarte mit Kästchen `km-task__check`, Titel mit `__id` und Status-Pill, Kurztext, nächstem Schritt, Details und Aktionsleiste (Varianten `--starred` für in Arbeit, `--dragging`, `--deactivated`, `--treffer`); `km-suggest` sind automatisch erzeugte Aufgaben in einem gestrichelten, aufklappbaren Block, die man übernimmt (`__task--promoted`) oder zurückstellt.
- Wann: Für Aufgaben mit Status und nächstem Schritt in einer Spalte oder Projektkarte; eine reine Checkliste ohne Status ist eine Liste mit `km-check`, eine Karte ohne Kästchen `km-card`.
- Wie: Kästchen mit `aria-label` „Erledigt: <Titel>“, Titel als Tätigkeit, „Nächster Schritt:“, Status-Pill mit Frist und `km-iconbtn` in `km-task__actions`; Erledigt gedämpft über `--km-color-text-muted` statt `opacity`, Farbkanten als Innenschatten, Löschen zweistufig über `km-task__confirm` ohne `confirm`, Verhalten im Skript der Seite.
- Prüfen: Fertig ist es, wenn jeder Zustand der Tabelle erreichbar ist (Details zu und offen), erledigter Text mindestens 4,5:1 misst (7,79 und höher), „In Arbeit“ nicht nur über die Kante, sondern auch über `aria-pressed` am Stern-Knopf erkennbar ist und der Bestätigen-Knopf mit `--km-color-on-attention` auf danger mindestens 6,01 erreicht.
