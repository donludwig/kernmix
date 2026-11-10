# Meta-Zeile (`km-metaline`)

Status: stabil, auf der Seite „Entscheidungen“ im Einsatz · Story: `docs/index.html#metaline` · CSS: `src/km-components.css`, Abschnitt „Meta-Zeile (km-metaline)“ · Stand: 2026-11-09

## Kurzbeschreibung

Die Meta-Zeile zeigt kurze Eckdaten eines Dokuments in einer Zeile unter dem Titel: Typ, Status als Pill, Datum, Tags und Bezüge als Links. Ein Bedienelement der Karte steht rechts in derselben Zeile. Sie ersetzt Fakten-Kacheln, wenn alle Werte kurz sind; bei wenig Breite bricht sie zwischen den Teilen um.

## Name und Abgrenzung

- Klassen: Zeile `km-metaline`, Teil `km-metaline__item`, Bedienelement rechts `km-metaline__end`.
- Zum Baustein gehören Zeile, Teile, Trenner und der rechte Platz; Pill, Links und Segmented Control darin sind eigene Bausteine.
- `km-facts`: Fakten-Kacheln für längere oder mehr Werte.

## Einsatz

### Verwenden, wenn

- ein Dokument unter dem Titel wenige kurze Eckdaten zeigt (Typ · Status · Datum · Tags · Bezug).

### Nicht verwenden, wenn

- Werte lang sind oder eine Unterzeile brauchen: Fakten-Kacheln (`km-facts`).

## Verwendung

```html
<div class="km-metaline">
  <span class="km-metaline__item">ADR</span>
  <span class="km-metaline__item"><span class="km-pill km-pill--warn">Proposed</span></span>
  <span class="km-metaline__item">08.11.2026</span>
  <span class="km-metaline__item">ergänzt durch <a class="km-link" href="#">30</a>, <a class="km-link" href="#">31</a></span>
  <span class="km-metaline__end">…</span>
</div>
```

## Aufbau

| Teil | Klasse | Funktion |
|---|---|---|
| Zeile | `km-metaline` | Flex mit Umbruch, mittig ausgerichtet, Schrift `--km-typography-font-size-body-small`, Text `--km-color-text-muted`. |
| Teil | `km-metaline__item` | bricht nicht in sich um (Kommas bleiben direkt hinter Links); die Zeile bricht nur zwischen den Teilen. |
| Trenner | `km-metaline__item::after` | Mittelpunkt hinter jedem Teil, auf das ein weiterer Teil folgt, in `--km-color-text-dim`; bricht die Zeile um, endet die obere mit „·“, keine Zeile beginnt damit. |
| Bedienelement | `km-metaline__end` | rechts in derselben Zeile (`margin-left: auto`). |

## Zustände

| Zustand | Auslöser | Darstellung | Tokens |
|---|---|---|---|
| Eine Zeile | genug Breite | Teile mit „·“ getrennt, Bedienelement rechts | `--km-space-xs` |
| Umgebrochen | wenig Breite | nächste Zeile beginnt mit einem Teil, Zeilenabstand `--km-space-2xs` | `--km-space-2xs` |

## Verhalten

- Reine Darstellung; was die Teile zeigen und was das Bedienelement umschaltet, setzt das Skript der Seite.
- Was der Kopf zeigt, steht nicht noch einmal im Text (Seitenregeln „Entscheidungen“).

## Text und Wording

- Datum als `TT.MM.JJJJ`.
- Kurze Werte; Bezüge als Links mit Komma getrennt.

## Barrierefreiheit

- Trenner kommt aus CSS (`content`) und ist kein eigenes Element.
- Kontrast (gerechnet in der Story, headless Chrome):

| Paar | Kobalt dunkel | Kobalt hell | Papier dunkel | Papier hell |
|---|---|---|---|---|
| Teil `--km-color-text-muted` | 10,33 | 8,51 | 10,28 | 8,19 |
| Link | 9,30 | 6,14 | 9,03 | 7,29 |
| Pill | 7,21 | 5,42 | 9,36 | 5,14 |
| Trenner `--km-color-text-dim` | 7,02 | 5,56 | 6,51 | 5,61 |

## Seitenregeln

Aus `docs/seitenregeln.md`: Entscheidungen zeigen unter dem Titel eine Zeile `km-metaline` (Typ · Status als Pill · Datum · Tags · Bezug mit Links), das Bedienelement der Karte rechts darin als `km-metaline__end`; keine Fakten-Kacheln, wenn alle Werte kurz sind (Entscheidung 50).

## Verwandte Bausteine

`km-facts` (Fakten-Kacheln), `km-pill`, `km-link`, `km-segmented`.

## Tokens

Rollen: `--km-typography-font-size-body-small`, `--km-color-text-muted`, `--km-color-text-dim`, `--km-space-xs`, `--km-space-2xs`, `--km-space-s`.

- Komponenten-Tokens: keine.

## Regeln

- Was: Die Meta-Zeile `km-metaline` zeigt kurze Eckdaten eines Dokuments in einer Zeile unter dem Titel, mit einem Bedienelement rechts.
- Wann: Nur, wenn alle Werte kurz sind; sonst Fakten-Kacheln.
- Wie: Je Wert ein `km-metaline__item`, Status als `km-pill`, Bezüge als `km-link`, Bedienelement in `km-metaline__end`; die Trenner setzt das CSS.
- Prüfen: Fertig ist es, wenn bei 390 px keine Zeile mit „·“ beginnt und Text in allen Themes mindestens 4,5:1 misst.
