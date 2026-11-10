# Vorlage: Komponenten-Doku in Kernmix

Diese Vorlage gilt für jeden Baustein von Kernmix (Präfix `km-`). Die Gliederung folgt einer verbreiteten Struktur für Komponenten-Dokus in Storybook (Kurzbeschreibung, Überblick, Verwendung, Aufbau, Regeln, Interaktion, Text, Varianten, Größen, Referenz, Verwandte, Theming), ergänzt um das, was ein offenes, persönliches System zusätzlich braucht: Name und Abgrenzung, alle Zustände als Tabelle, Barrierefreiheit als eigener Abschnitt, Bezug auf die Seitenregeln, ein belegter Vergleich mit anderen Design-Systemen und offene Punkte.

## Grundsätze

- Der Code ist die Quelle: `src/km-components.css` (Bausteine), `src/km-roles.css` (Rollen-Tokens), `src/themes/*.css` (Theme-Werte), `tools/bausteine.py` und `tools/bausteine_nachtrag.py` (Kurzbeschreibung und Beispiel-Markup, daraus Doku und Komponentenbeschreibung). Was die Doku sagt, muss dort stehen; Abweichungen kommen unter „Offene Punkte“, nicht still in den Text.
- Sprache Deutsch, Leser\*innen sind Entwickler\*innen und Gestalter\*innen, die den Baustein in einer eigenen Seite einsetzen. Keine Projekt-Interna, keine Kund\*innen, keine Personennamen außer dem Maintainer als Entscheider.
- Abschnitte, die nicht passen, entfallen; die Reihenfolge der übrigen bleibt.
- Jeder Abschnitt ist eine Aussage über den heutigen Stand. Kein Verlauf, keine früheren Fassungen; Änderungen stehen im `CHANGELOG.md`.
- Belege: Aussagen über andere Design-Systeme nur mit Quelle (Link, Abrufdatum). Was nicht geprüft ist, trägt „ungeprüft“.
- Kontrast gerechnet, nicht geschätzt: Werte für jedes Theme und jeden Modus, in dem der Baustein ausgeliefert wird.
- Höhen und Lagen gemessen (headless Chrome, `getBoundingClientRect`), wenn die Doku sie behauptet.
- Absätze und Listenpunkte je eine Zeile.
- Kurz und scanbar: ein Satz je Listenpunkt, lange Absätze als Punkte. Keine Entstehungsspuren (keine Namen mit Datum, kein „wie besprochen“); ein Datum steht nur einmal, als „Stand“ in der Kopfzeile. Messungen und Quellen gelten zum Stand.

## Gliederung

Datei: `docs/komponenten/<name>.md`, Name in Kleinbuchstaben wie die deutsche Bezeichnung (`tabelle.md`, `knopf.md`).

```markdown
# <Deutsche Bezeichnung> (`km-<block>`)

Status: <Entwurf | stabil | in Umbau>, <wo im Einsatz> · Story: `docs/index.html#<anker>`, `#<weitere>` · CSS: `src/km-components.css`, Abschnitt „<Abschnittsname>“ · Stand: <JJJJ-MM-TT>

## Kurzbeschreibung
Höchstens 120 Wörter, eher kürzer. Was der Baustein tut und welches Problem er löst. Keine Werbesprache, keine Interna.

## Name und Abgrenzung
- Technischer Name (Klasse) und Bezeichnung in der Oberfläche getrennt nennen.
- Was gehört zum Baustein, was nicht (Inhalt, Daten, Skript der Seite).
- Abgrenzung zu ähnlichen Bausteinen im System und zu KERN-Komponenten.
- Namensalternativen (bis zu fünf), wenn der Name noch nicht entschieden ist; Entscheidung trifft der Maintainer.

## Einsatz
### Verwenden, wenn
### Nicht verwenden, wenn

## Verwendung
Minimales Markup als Code-Block. Reihenfolge beim Einbinden: `kern.min.css`, `km.css`, Theme.

## Aufbau
Tabelle: Teil, Klasse, Funktion. Elemente mit Verhalten beschreiben, nicht nur den Inhalt.

## Varianten
Je Variante (Modifier `km-<block>--<variante>`): wann sie passt.

## Größen
Nur, wenn es mehrere gibt; sonst ein Satz.

## Zustände
Tabelle: Zustand, Auslöser (Attribut, Klasse, Pseudoklasse), Darstellung, Tokens. Immer prüfen: Ruhe, Hover, Fokus, gedrückt/gewählt, offen/zu, deaktiviert, leer, Fehler, Laden, dazu fachliche Zustände.

## Verhalten
Was das CSS leistet und was das Skript der Seite leisten muss (Klick, Tastatur, Zustand in Adresse und Speicher).

## Text und Wording
Beschriftungen, Höchstlänge je Textelement in Zeichen, Ton.

## Barrierefreiheit
- Rollen und Attribute (ARIA nur, wo natives HTML nicht reicht)
- Tastatur
- Fokus (Darstellung, Reihenfolge, Rückgabe)
- Kontrast: gerechnete Werte je Theme und Modus, Ziel Text ≥ 4,5, Bedienelemente ≥ 3
- Bewegung, Zoom, schmale Breite (390 px)

## Seitenregeln
Welche Regeln aus `docs/seitenregeln.md` den Baustein betreffen, als Verweis mit Kurzfassung.

## Vergleich mit anderen Design-Systemen
Tabelle: System, Name, Besonderheit, Quelle. Nur öffentliche Systeme, Quelle mit Abrufdatum, sonst „ungeprüft“.

## Verwandte Bausteine

## Tokens
Rollen-Tokens, die der Baustein liest, und Komponenten-Tokens (Haken zum Überschreiben). Harte Werte, die noch Token werden sollten, mit Datei:Zeile. Letzter Abschnitt vor den offenen Punkten.

## Offene Punkte
Widersprüche zwischen Code, Story und Seitenregeln, fehlende Zustände, Fragen an den Maintainer.

## Regeln
Je ein Satz, verdichtet nur aus dieser Datei, für Agenten übernehmbar; erscheint als Kasten „Regel:“ am Ende des Kapitels.
- Was: <was der Baustein ist, Varianten>
- Wann: <wann nehmen, wann stattdessen etwas anderes>
- Wie: <Markup, Klassen, ARIA, Tokens>
- Prüfen: <woran man erkennt, dass es fertig ist>
```

## Darstellung im Reiter „Komponenten“

`tools/build-storybook.py` setzt die Doku über `tools/komponenten_doku.py` im Aufbau D „Vier Fragen mit Kapitelleiste“ zusammen (Seitenregeln „Dokumentation“):

- **Kopf:** Titel, erster Satz bzw. die ersten zwei Sätze der Kurzbeschreibung als `km-lead`, der Rest als Punkte in der Karte „Überblick“; Fakten-Kacheln aus der Kopfzeile (Status, Stand, Kontrast der Vorschau, Varianten, Klassen, Quellen, Stories); offene Punkte als Hinweiskasten.
- **1 · Was ist es?** Beispiel, Überblick, In dieser Story, Varianten, Name und Abgrenzung.
- **2 · Wann nehmen?** Verwenden, wenn | Nicht verwenden, wenn (aus „Einsatz“), Verwandte Bausteine, Zusammenhang, Vergleich (breit).
- **3 · Wie bauen?** Aufbau und Klassen mit Grundmarkup aus „Verwendung“ (Kopieren im Block), Text und Wording, Tokens, Richtig | Falsch (aus „Beispiele“), Markup der Story.
- **4 · Wie prüfen?** Zustände (breit), Verhalten, Barrierefreiheit (Tabellen daraus als eigene breite Karte „Kontrast“), Größen, Bezug (Seitenregeln, Entscheidungen als Chips, Abschnitte ohne festen Platz).
- Jedes Kapitel endet mit dem Kasten „Regel:“ aus „Regeln“. Rechts läuft die Kapitelleiste mit. Eine halbe Karte ohne Partner geht über die ganze Zeile.

## Prüfen vor dem Abschluss

- Jede Klasse im Text gibt es in `src/km-components.css`; jede Story-Referenz gibt es in `docs/index.html`.
- Kurzbeschreibung höchstens 120 Wörter.
- Alle Zustände aus CSS und Story stehen in der Tabelle.
- Kontrastwerte gerechnet, Höhen gemessen, wo behauptet.
- Vergleich: jede Zeile mit Quelle oder „ungeprüft“.
- Text gegen KI-Floskeln gelesen.
