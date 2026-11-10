# Angabenliste und Maßnahmenliste (`km-deflist`, `km-measures`)

Status: stabil, im Lagebild im Einsatz · Story: `docs/index.html#angaben`, `#massnahmen` · CSS: `src/km-components.css`, Abschnitte „Lagebild-Umbau“ (`km-deflist`), „Für das Lagebild“ (Maßnahmen) · Stand: 2026-11-09

## Kurzbeschreibung

Die Angabenliste setzt Bezeichnung und Text als kompakte Liste in Fließtextgröße, etwa für den Steckbrief einer Website in einem Bereich (Adresse, Schutz, Hochladen). Die Maßnahmenliste zeigt Maßnahmen mit einem Punktwert rechts, gruppiert unter Kategorien, nachrangige Punkte gedämpft, darunter ein Hinweis und ein aufklappbarer Verlauf.

## Name und Abgrenzung

- `km-deflist` (`<dl>` mit `<div><dt><dd>`); `km-measures` (`__head`, `__label`, `__list`, `__list--rest`, `__item`, `__points`, `__hint`, `__more`).
- KERN-Beschreibungsliste `kern-description-list` bleibt für Formularseiten in Lesegröße.
- Tabelle: wenn mehrere Dinge mit gleichen Spalten verglichen werden.
- `km-facts`: wenige große Werte.

## Einsatz

### Verwenden, wenn

- eine Sache verschiedenartige Angaben hat: Angabenliste;
- Punkte bewertet werden: Maßnahmenliste.

### Nicht verwenden, wenn

- die Daten tabellarisch sind: Tabelle.

## Verwendung

```html
<dl class="km-deflist"><div><dt>Adresse</dt><dd>beispiel.de</dd></div><div><dt>Schutz</dt><dd><span class="km-pill km-pill--ok">Passwort</span>ein Passwort je Ordner</dd></div></dl>
<div class="km-measures"><p class="km-measures__label">Härtung</p><ul class="km-measures__list"><li class="km-measures__item">Kopfzeilen gesetzt<span class="km-measures__points">+5</span></li></ul><p class="km-measures__hint">Punkte aus 21 Kriterien.</p></div>
```

## Aufbau

| Teil | Funktion |
|---|---|
| `km-deflist` | Raster `max-content` / Rest, Abstand `--km-space-xs` / `--km-space-xl`; `dt` gedämpft, `dd` bis 72ch; Pill im `dd` mit Abstand. |
| `km-measures__label` | Versalien, gedämpft; zwischen Kategorien `--km-space-block`. |
| `km-measures__item` | Zeile mit Linie oben (nicht am ersten), Wert rechts. |
| `km-measures__points` | Mono, kräftig, grün; in `__list--rest` gedämpft. |
| `km-measures__more` | `<details>` mit Verlauf. |

## Zustände

Aus `src/km-components.css`, Abschnitte „Für das Lagebild“ und „Lagebild-Umbau“.

| Zustand | Auslöser | Darstellung | Tokens |
|---|---|---|---|
| Angabenliste | – | statisch, keine Zustände | – |
| Maßnahme | `km-measures__item` | Text voll, Linie oben ab der zweiten Zeile, Punkte grün | `--km-color-text`, `--km-color-border-card`, `--km-color-feedback-success` |
| Nachrangig | `km-measures__list--rest` | Text gedämpft, Punkte gedämpft statt grün | `--km-color-text-muted`, `--km-color-text-dim` |
| Verlauf zu | `details.km-measures__more` ohne `open` | nur die Zeile zum Aufklappen, gedämpft | `--km-color-text-dim` |
| Verlauf Hover | `summary:hover` | Text voll | `--km-color-text` |
| Verlauf offen | `details[open]` | Absatz darunter, gedämpft | `--km-color-text-muted` |
| Fokus Verlauf | `:focus-visible` am `summary` | kein eigener Rahmen im Kit, siehe offene Punkte | – |

Leer, Fehler und Laden gibt es im Kit nicht; negative Punkte haben keine eigene Farbe (offene Punkte).

## Barrierefreiheit

- Angabenliste als echtes `<dl>`.
- Punktwert mit Vorzeichen als Text, Farbe nicht allein.
- Kontrast (gerechnet): `dt` `--km-color-text-dim` auf `--km-color-section` 6,66 / 5,16 / 6,26 / 5,86; Punkte `success` auf `--km-color-card` 5,55 / 6,01 / 7,51 / 5,17 (Kobalt dunkel, Kobalt hell, Papier dunkel, Papier hell).

## Beispiele

### Falsch

```html
<p><b>Adresse:</b> beispiel.de<br><b>Schutz:</b> …</p>   <!-- Angaben als Fließtext mit Umbrüchen -->
```

## Seitenregeln

Abstand Etikett und Text per `gap`; Status als Etikett. Entscheidungen 12, 19.

## Vergleich mit anderen Design-Systemen

| System | Name | Besonderheit | Quelle |
|---|---|---|---|
| GOV.UK Design System | Summary list | „show information as a list of key facts“; `<dl>` mit Zeilen aus `dt`, `dd` und optionalem Aktions-`dd`; nicht für tabellarische Daten | design-system.service.gov.uk/components/summary-list |

## Tokens

`--km-font-size-s`, `--km-font-size-xs`, `--km-color-text`, `--km-color-text-muted`, `--km-color-text-dim`, `--km-color-border-card`, `--km-space-xs`, `--km-space-xl`, `--km-space-tight`, `--km-space-stack`, `--km-space-block`, `--km-space-group`; Rückmelde-Rollen: `--km-color-feedback-success`.

## Offene Punkte

- Negative Punkte haben keine eigene Farbe.
- Fokus am Verlauf: Die gemeinsame Fokus-Regel greift nur an Elementen mit `km-`-Klasse (`:is(a, button, input, select, summary, [tabindex])[class*="km-"]`); das `summary` in `km-measures__more` hat keine, die Klasse sitzt am `details`. Fokus nachmessen.
- Keine Aktionsspalte in der Angabenliste (GOV.UK hat „Ändern“); bei Bedarf als Kit-Variante.

## Regeln

- Was: Die Angabenliste `km-deflist` setzt Bezeichnung und Text als kompakte `<dl>`-Liste in Fließtextgröße, die Maßnahmenliste `km-measures` zeigt Maßnahmen mit Punktwert rechts unter Kategorien, nachrangige Punkte gedämpft (`km-measures__list--rest`), mit Hinweis und aufklappbarem Verlauf.
- Wann: Die Angabenliste für verschiedenartige Angaben zu einer Sache, die Maßnahmenliste, wenn Punkte bewertet werden; tabellarische Daten gehören in die Tabelle, wenige große Werte in `km-facts`.
- Wie: `<dl class="km-deflist">` mit `div`, `dt` und `dd` statt Fließtext mit Umbrüchen, Status als Etikett (`km-pill`) im `dd`, Abstand per `gap`; Maßnahmen als `km-measures__label`, `ul.km-measures__list` mit `km-measures__item` und `km-measures__points`, Verlauf in `km-measures__more`.
- Prüfen: Fertig ist es, wenn die Angabenliste ein echtes `<dl>` ist, der Punktwert mit Vorzeichen als Text dasteht und nicht nur in der Farbe, nachrangige Punkte gedämpft statt grün erscheinen, der Verlauf per Tastatur auf- und zuklappt und `dt` sowie Punkte in allen Themes mindestens 4,5:1 messen; offen: eigener Fokusrahmen am `summary` des Verlaufs, siehe Offene Punkte.
