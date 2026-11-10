# Seitenregeln: Werkzeugseiten auf Kernmix

Pflichtlektüre vor jeder neuen Seite und jeder Umstellung einer Seite auf Kernmix. Abgeleitet aus dem Umbau von Project Dashboard und Lagebild am 2026-11-08. Jede Regel nennt den Kit-Baustein, der sie umsetzt; gibt es keinen, kommt er zuerst ins Kit. Die Beispiele in Klammern sind die Stellen, an denen die Regel entstanden ist.

## Arbeitsweise

- **Erst Kit, dann Seite.** Kein Baustein wird auf einer Seite erfunden. Neues kommt zuerst nach `src/km-components.css` (oder Token nach `src/km-roles.css`), dazu Story in `tools/bausteine_nachtrag.py`, Zeile im `CHANGELOG.md`, Build (`tools/build.py`, `build-storybook.py`, `build-doku.py`) und erst dann `tools/einbetten.py <seite>` in jede Seite, die ihn nutzt.
- **Gleiches gleich bauen.** Was auf zwei Seiten vorkommt, sieht gleich aus und heißt gleich (Spaltenkopf, Knopf, Hinweistext). Eine Abweichung, die der Maintainer auf der einen Seite korrigiert, wird auf der anderen mitgezogen, ohne dass er es sagen muss.
- **Seitenregeln wandern ins Kit.** Findet sich auf einer Seite eigenes CSS für etwas, das ein Baustein sein könnte (Zeilennummer, Unterzeile, Aktionsspalte), wird es Kit-Variante und die Seitenregel fällt weg.
- **Nach jeder sichtbaren Änderung messen,** nicht schätzen: headless Chrome auf `file://`, `getBoundingClientRect` und `getComputedStyle`, bei Lageänderungen ein Screenshot-Ausschnitt. Keine Konsolenfehler; Inline-`//`-Kommentare mitten in JS-Zeilen verschlucken Code, Kommentare als `/* … */` oder in eigene Zeile.
- **Sicherung vor jedem Eingriff** in die Seite (`_backups/index-vor-<thema>-<zeit>.html`).

## Tokens (Entscheidungen 30 bis 35)

- **Ebenen wie KERN:** Core Token (Skala, Farbreihen `--kern-color-<reihe>-<stufe>`, eigene Reihen `--km-color-<reihe>-<stufe>` in `src/km-core.css`), Semantische Token (KERN-Semantik und Rollen `--km-*`), Komponenten-Tokens als Typ im Namen `--km-component-<baustein>-<teil>-<eigenschaft>`.
- **Bausteine lesen nur `--km-*`,** nie `--kern-*` direkt; Rollen zeigen auf KERN-Semantik oder eine benannte Erweiterung (`--km-metric-space-small-plus`), nie still auf die Skala.
- **Rückmeldefarben** über `--km-color-feedback-<art>` und `-background`; **Datenfarben** (Punkte, Ränder, Balken) über `--km-color-data-1` bis `-5`, nie Textfarbe; eine Seite belegt sie um, statt neue Hex-Werte zu setzen; neue Töne als Reihe in `src/km-core.css`.
- **Hell und dunkel nur über Tokens,** nie über `:root[data-theme=…]` in Bausteinen: die Seite setzt `data-theme`, das Kit liest `data-kern-theme` (gespiegelt) und `prefers-color-scheme`; modusabhängige Werte stehen in den Hell-Blöcken von `km-roles.css` bzw. `km-components.css`.
- **Zustände:** Hover über `--km-color-action-state-opacity-hover` (Anteil transparent, 92 %), gewählt über `--km-color-action-state-opacity-selected` (0,16); keine neuen Prozentzahlen in `color-mix`.
- **Ausschluss per `:not()` ändert die Spezifität:** ein weiteres `:not(.x)` macht die Regel stärker und kann andere Regeln überstimmen; zum Ausschließen ohne Spezifitätsänderung `:not(:where(.x))` nehmen (Kartenkopf, 0.6.0).

## Maße und Layout

- **Keine harten Werte:** keine px, keine Hex-Farben in Seiten-CSS; nur `--km-*`-Tokens und die Abstandsrollen (`--km-space-page`, `-section-x/-y`, `-block`, `-card`, `-group`, `-stack`, `-tight`). Fehlt ein Wert, wird er Token (Beispiel `--km-component-monogram-size`, `--km-table-tool-w`, `--km-drop-line`).
- **Seitenrahmen gleich:** Kopfzeile, Logo, Kopfknöpfe, Einklapp-Knopf und Icon-Leiste über die Komponenten-Tokens `--km-component-header-control-height`, `-monogram-size`, `-sidebar-toggle-size`, `-sidebar-rail-width`, `-sidebar-min-width`, `-sidebar-width` (alte Namen `--km-sidebar-w` usw. gehen nur noch lesend); keine eigenen Zahlen in der Seite.
- **Keine Überlappungen:** Nichts liegt über etwas anderem, auch nicht im Randfall (langer Name, eingeklappte Leiste, erster Eintrag neben dem Einklapp-Knopf). Breiten so wählen, dass Kopftext und Pfeil Platz haben (gemessen, z. B. 7rem für „WERKZEUG“ plus Pfeil).
- **Nur Lucide-Icons:** jedes Symbol ist ein Icon aus `assets/lucide.json` (Klasse `km-icon`), auch in Beispielen der Komponentenbeschreibung und in Texten, die Skripte setzen (`textContent = '✕ zurück'` war ein Fall); keine Schriftzeichen (⚙ ✕ × › ↗ ★ ✓ ▸ ▾ ☐ ⇄ ◎ ⚠) als Icon-Ersatz, die sitzen nie mittig und folgen nicht dem Theme. Prüfung: `tools/pruefe-seiten.py` und `dashboard-check.py` melden Knöpfe, Links, Etiketten und Köpfe, deren Text mit einem solchen Zeichen beginnt oder endet, und CSS-`content` mit solchen Zeichen.
- **Flex-Zeilen mit Text und `<code>`** (Überschriften in Flächen, Einführungstext) brauchen `flex-wrap: wrap` bzw. `overflow-wrap: break-word`, sonst laufen lange Pfade bei 390 px aus der Fläche und die Seite scrollt waagerecht (Dashboard, 0.6.0).
- **Symbol mittig zur ersten Zeile:** Icons, Zeilennummern, Pfeile stehen mittig zur ersten Textzeile, nicht zum Block und nicht an der Oberkante.
- **Kachel neben Titel:** Titel mit Unterzeile (Name und Rolle, Titel und Untertitel oder Kennung) → Kachel mittig zum ganzen Block; Titel allein, auch umbrechend → Kachel mittig zur ersten Zeile. Das Kit regelt beides in `km-card__head` und `km-agent__header`; Köpfe mit Kachel immer aus diesen Klassen bauen.
- **Icon und Text: ein Abstand (Entscheidung 41):** `--km-space-icon-text` (6 px) zwischen jedem Lucide-Icon und seinem Text, in Knöpfen, Seitenleiste, Zwischentiteln, Segmented Control, Chips, Panels und Etiketten; Kachel oder Kürzel zum Titel `--km-space-tile-title` (8 px). Keine eigenen Zahlen.
- **Abstände zwischen Etikett und Text** fest per `gap` (`--km-space-xs`), nie per Leerzeichen (`km-table__label`, Score „A ab 90“).
- **Farbkanten** (Gruppenzeile, Zeile in Arbeit, Karte) alle mit derselben Technik zeichnen: Innenschatten (`box-shadow: inset`), nie gemischt mit `border-left`, sonst stehen sie versetzt.

- **Schriften immer einbetten (seit 0.8.0):** Seiten auf Kobalt betten mit `einbetten.py --schriften` ein, sonst fehlt Atkinson Hyperlegible Next und es greift die Ersatzschrift; danach `document.fonts` prüfen. Tabellenziffern setzt das Kit nur an Zahlen, Daten und Zählern (seit 0.7.0), die Seite setzt nichts selbst.

## Typografie (Entscheidungen 38 bis 40)

- **Drei Textsorten:** Lesetext 16 px (fluid bis 18) mit Maß rund 70 Zeichen in Doku, Entscheidungen und auf der Komponenten-Seite (Rolle `km-prose`, Einleitung `km-lead`); Arbeitstext 14 px in Tabellen, Karten und Seitenleiste; Beschriftung 12 px, nie für Absätze. Größen, Zeilenhöhen, Maße und Abstände nur über die Tokens `--km-typography-*`, `--km-metric-measure-*`, `--km-space-paragraph`, `-heading-above`, `-heading-below`.
- **Farbe nach Rolle:** Überschriften, Namen und Werte `--km-color-text`; Lesetext `--km-color-text-muted` (≥ 7:1 auf allen Flächen); Nebeninfo `--km-color-text-dim` (≥ 4,5:1).
- **Maß in em, nicht ch:** 1ch ist in Atkinson 1,43 und in Inter 1,30 mittlere Zeichen breit; `--km-metric-measure-default` (32em) ergibt rund 70 Zeichen. Nach einem Schriftwechsel neu messen.
- **Mono nur für Kennungen**, die man kopiert oder abtippt (Pfad, Klasse, Token, Ticket); Datum, Stunden und Umfang stehen in der Textschrift mit gleich breiten Ziffern, Umfang nicht fett. Pfade und Dateinamen im Fließtext stehen in `<code>`.
- **Generierte Inhalte (Markdown) erzeugen dieselben Bausteine wie Handgeschriebenes:** Tabellen als `km-table-wrap` + `km-table` und nach dem Laden durch `kmTabelle`, Lesetext als `km-prose`, offene Fragen und Hinweise als `km-callout`, nie rohe `<table>`, `<ul>` oder `<pre>` ohne Kit-Klasse. Neue Spaltennamen aus Doku-Tabellen kommen in `SPALTEN` (`src/km-table.js`). Prüfung: `tools/pruefe-seiten.py` (Komponenten, Doku, Entscheidungen) meldet 0 Funde.
- **Zwei Themes auf einer Seite:** beide per `--zusatz-theme` einbetten und über `media` der `<style data-kern-theme-name>` umschalten, nicht über eine zweite Datei; die Wahl vor dem ersten Zeichnen setzen (kleines Skript direkt hinter `KERN-SYSTEM:END`).

## Navigation (Seitenleiste)

- **Sprünge sofort:** Jede Sprungnavigation (Seitenleiste, Doku-Navigation, Entscheidungen) springt ohne Animation (`html { scroll-behavior: auto }` im Kit, `behavior: 'instant'` in Skripten) und markiert das Ziel sofort (`aria-current`, setzt `kmPopup` für `km-sidebar__item` mit `href="#…"` oder `data-target`). Ein Scroll-Beobachter setzt nach einem Sprung kurz aus, die Adresse bekommt den Anker per `history.replaceState`, der markierte Eintrag bleibt in der Navigation sichtbar (`scrollIntoView({ block: 'nearest' })`), ein Aufruf mit Anker springt beim Laden direkt dorthin.

- **Navi wie Inhalt:** Gruppen folgen den Spalten der Seite; Bereiche der Mitte oben ohne eigene Überschrift, rechte Spalte als Gruppe „Rechte Spalte“; was im Inhalt unter einem Bereich liegt, steht eingerückt darunter (`km-sidebar__branch`, `__nest`). Story „Seitenleiste: Hierarchie wie im Inhalt“.
- **Alles klappbar, auch die erste Ebene:** jede Gruppe und jeder Eintrag mit Unterebene (`km-sidebar__label-btn`, `km-sidebar__branch-toggle`, `aria-expanded`), Zustand in localStorage. Der Klapp-Pfeil steht direkt hinter dem Text im Abstand `--km-space-xs`, wie bei den Gruppen, nicht am rechten Rand.
- **Klappen und Funktion getrennt:** Ein Eintrag mit Unterebene (Gruppe oder Bereich wie „Listen“) klappt per Klick auf Text oder Symbol nur auf und zu, wie die Gruppen-Überschriften; er springt nicht und wechselt keine Ansicht. Eine Funktion dazu (Bearbeiten, Verwalten, Sprung zur Verwaltung) steht als Symbol rechts in derselben Zeile (`km-sidebar__row` + `km-sidebar__action`, Lucide `settings`, Name als `title` und `aria-label`); eingeklappt ist es ausgeblendet. Ein Klick auf das Symbol markiert den Eintrag seiner Zeile als aktuell und hebt alle anderen Markierungen auf (`km-popup.js`).
- **Schalter im Eintrag:** Ausblendbare Bereiche haben den Schalter rechts im selben Eintrag (`km-sidebar__row` + `km-switch`), keine zweite Liste nur mit Schaltern.
- **Reihenfolge der Filtergruppen unter der Übersicht:** Kunden, dann Typen, dann weitere (Phase, Schutz, Merkmale; Merkmale = Eigenschaften aus den Daten wie Live oder Offene Aufgaben, nicht von Hand). Jede Gruppe mit „Alle“ und Zähler, Zähler folgen den anderen Filtern.
- **Eine Linie mit dem Logo:** Icons der obersten Einträge, Gruppenüberschriften und Einklapp-Knopf (eingeklappt) beginnen auf derselben Linie wie das Logo-Icon im Kopf; Einträge der Unterebene fluchten mit deren Überschrift. Der Auswahlstrich steht davor (`--km-sidebar-inset`).
- **Eingeklappt nur Icons:** `km-sidebar--rail` an der Leiste, sobald sie eingeklappt ist; jeder oberste Eintrag braucht deshalb ein Icon (`km-sidebar__icon`) und seinen Namen als `title`. Icons stehen in einer Achse mit dem Ausklapp-Knopf.
- **Nichts springt beim Wählen:** Zustände ändern nie die Schriftstärke oder Breite eines Eintrags, in der Seitenleiste wie in der Segmented Control (Entscheidung 36) (gewählt = Farbe, Strich, Tönung); lange Namen einzeilig mit „…“ und vollem Namen im `title`, statt mehrzeilig umzubrechen.
- **Erster Eintrag neben dem Einklapp-Knopf** endet vor dem Knopf, auch wenn er einen Klapp-Pfeil hat.
- **Unterebenen beim ersten Textzeichen (DDR 47):** Aufgeklappte Unterebenen beginnen dort, wo der Text ihrer Kategorie beginnt: unter einem Eintrag um dessen Icon plus Abstand (`--km-component-sidebar-indent-item`), unter einem Gruppen-Label um das Label-Icon plus Abstand (`--km-component-sidebar-indent-label`). Die Regel steht im Kit, nicht in der Seite; die oberste Ebene bleibt auf der Linie des Logos, der eingeklappte Modus ist ausgenommen. Messen: erstes Textzeichen der Kategorie gegen ersten Punkt, Icon oder Text der Einträge, Abweichung höchstens 1 px.
- **Hervorhebung einheitlich (DDR 47):** Ein gewählter Eintrag mit Klapp-Pfeil ist genauso breit hervorgehoben wie einer ohne: die ganze Zeile trägt Fläche, Strich links und Hover, der Pfeil bleibt direkt hinter dem Text.
- **Eine Navigation, nur Kit-Klassen:** Jede Seite baut ihre Navigation aus der Kit-Seitenleiste (`km-sidebar`, `__group`, `__label-btn`, `__list`, `__item`, `__icon`, `__text`, `__count`); ein Baum mit Pfaden (Komponentenbeschreibung) ist `km-sidebar__group--tree`. Auswahl, Hover, Abstände, Einzug, Zeilenhöhe und Icons kommen nur aus dem Kit, die Seite setzt dafür keine eigenen Regeln; fehlt etwas, kommt es als Baustein ins Kit. Prüfung: `tools/pruefe-seiten.py` meldet Selektoren der Seite mit `:hover` oder `[aria-current|pressed|selected]`, die Links oder Knöpfe in einer `<nav>` treffen und im letzten Glied keine `km-`-Klasse tragen.

## Filter und Zustand

- **Vorgefertigte Filter schließen sich aus:** Kunde, Typ, Phase bzw. Schutz sind exklusiv; eine Wahl hebt die anderen auf (Kombinationen ergaben sonst oft 0 Treffer). Schutz hebt den Typ auf.
- **Filterwahl schaltet die Spaltensortierung ab** und stellt die Gruppenreihenfolge wieder her.
- **Filter öffnet, was er zeigt:** eingeklappte Gruppen mit Treffern werden geöffnet, der Sprung geht an den Anfang des Bereichs.
- **Spalten folgen den sichtbaren Zeilen,** egal über welchen Filter: Spalten, die für keinen sichtbaren Zeilentyp gelten, blenden sich aus (Lagebild: nur Ordner sichtbar → PHP, php2shell, Spuren weg).
- **Adresse und Speicher:** Filter, Sortierung, Suche in der Adresse (teilbar) und in localStorage. Eine gemerkte Spaltenauswahl erscheint nur in der Adresse, wenn der Nutzer sie gerade geändert hat, nicht beim Laden.
- **Logo setzt zurück:** Filter, Suche, Sortierung, Auf- und Zuklappen; die Spaltenauswahl und abgehakte Aufgaben bleiben. Danach ist die Adresse sauber.
- **Bereichsklick** („Übersicht“) setzt Kunden-, Typ- und Phasenfilter zurück und entfernt den Anker aus der Adresse.
- **Filter wirken auf alle Bereiche mit denselben Dingen:** Zeigt eine Seite Projekte (Hosts, Dateien) in mehreren Bereichen, gilt ein Filter der Navigation in jedem davon (Übersicht, Karten, Aufgaben, Synergien, Listen, Fokus); welche Dinge passen, entscheidet eine Stelle (die Übersicht). Die Filter stehen dann als eigene Gruppe „Filter“ oberhalb der Bereiche (`km-sidebar__group--filter`), nicht als Unterebene eines Bereichs. Oben in jedem betroffenen Bereich zeigt eine Filter-Leiste (`km-filterchips--bar`) die aktiven Filter mit × zum Aufheben; Ausgeblendetes trägt `km-filtered`, Zähler zählen es nicht mit.
- **Seitenleiste bleibt stabil, Inhalt filtert:** Einträge der Seitenleiste (Kunden, Typen, Phasen, Merkmale, Listen) verschwinden nie und ändern ihre Position nicht, wenn gefiltert wird; nur Tabellen und Kartengruppen blenden leere Gruppen aus, bei jedem aktiven Filter (auch Phase und Schalter). Sonst springt die Leiste unter dem Mauszeiger.
- **Sprungziele:** Ein Filter in der Seitenleiste (Liste, Merkmal) springt ganz nach oben; ein Reiter im Inhalt bringt seinen Bereich an die Oberkante; Bearbeiten im Inhalt (Verschieben, Löschen, Hinzufügen) hält die Lage des Bereichs im Fenster.
- **Merkmale statt Sammelgruppe:** Eine Filtergruppe für Eigenschaften aus den Daten heißt „Merkmale“ (nicht „Pflege“), beginnt mit „Alle“, hat ein Merkmal zur Zeit und springt auf „Alle“ zurück, sobald ein anderer Filter gewählt wird. Merkmale werden berechnet, nicht von Hand gepflegt; Handgepflegtes gehört in Listen.
- **Zähler zeigen, was der Klick zeigt:** Ein Zähler in der Seitenleiste nennt genau die Zahl der Einträge, die nach dem Klick im Inhalt stehen, unter allen übrigen aktiven Filtern; nach jeder Filteränderung neu rechnen.
- **Kopierte Zeilen (Fokus, Listen):** Zeilen, die aus einer Tabelle in einen zweiten Bereich kopiert werden, übernehmen Spaltenauswahl und Spaltenbreiten der Quelle und bekommen ihre Knöpfe über Delegation am Dokument, nie über Listener an der Kopie (`cloneNode` kopiert keine Listener). Spalten ausblenden und Breiten neu setzen nach jedem Neuaufbau.
- **Reihenfolge verwalten:** Sortierbare Einträge (Listen, Bereiche) bekommen eine Verwaltungsansicht als Tabelle: rechts Ziehgriff, Hoch, Runter, Löschen (zweistufig, ohne Browser-Dialog); feste Einträge (z. B. vorn, automatisch) tragen statt Knöpfen einen Hinweis. Keine Tastenkürzel wie Alt + Pfeil als einziger Weg.
- **Zähler folgen den Filtern überall (0.13.0):** Auch Gruppen innerhalb eines Bereichs (Kartengruppen der Projektdetails, Gruppen einer Tabelle) zählen nur Sichtbares; eine Gruppe ohne sichtbaren Eintrag verschwindet samt Kopf (`km-filtered`), wie leere Gruppen der Übersicht. Seiten, deren Bereiche andere Dinge zeigen, filtern dort nur, wofür es die Eigenschaft gibt (Lagebild: Weitere Server nur nach Kunde), und zeigen die Filter-Leiste nur dort.

## Tabellen

- **Tabellen nur über `kmTabelle()` bauen:** Jede `km-table` läuft nach dem Aufbau durch `window.kmTabelle(table, { nummern, sortieren })`; die Funktion setzt Rollen, Kopf-Icons, Datum, Umfang und Aktionsspalte nach der Liste unten. Neue Spaltennamen kommen in die Zuordnung `SPALTEN` in `src/km-table.js`, nicht in die Seite. `dashboard-check.py` meldet Tabellen ohne Bauweg, Köpfe ohne Icon und Aktionen nicht zuletzt.
- **Eine Standard-Tabelle überall:** `km-table` mit Spaltenrollen `km-table__key` (Kennung), `__nowrap` (Wert), `__text`/`__text--wide` (Fließtext), `__num` (Zahl). Namen in der ersten Spalte, auch Hostnamen und Pfade, tragen `km-table__name` (Textschrift, fett, Winkel in Unterzeilen); `__key` mit Mono nur für weitere Kennungen. Werte brechen nie um, Zeilen sind gleich hoch, Zusatzangaben stehen neben dem Wert, nicht darunter. Zellen beginnen oben.
- **Rolle je Spalte (eine Liste für alle Seiten, 09.11.2026):** Gleiche Spalte, gleiche Rolle, egal ob die Klasse im HTML, in einem Generator oder per Script aus dem Spaltennamen (Lagebild `ROLLE`) gesetzt wird. Neue Spalten erst hier eintragen.
  - Name (Projekt, Host, Ordner, Agent): Zelle `__nowrap`, Name darin `km-table__name`, ggf. mit `km-table__tool`
  - Weitere Kennung, die man kopiert oder abtippt (Demo-Link, Pfad als Wert, Ticket-Kennung): `__key` (Mono)
  - Kurzer Wert (Kunde/Organisation, Typ, Modell, Was läuft, PHP, Schutz, Benutzer, Passwort, Wann, Links, Datei): `__nowrap`
  - Status als Etikett (Phase, Score, Spuren, php2shell): `__nowrap` mit `km-pill`
  - Datum: `__date` + `__nowrap`, relative Angabe darunter `__date-rel`
  - Zahl (Anzahl, Dateien): `__num`; Stunden `__hours` + `__nowrap`; Umfang mit Balken `__scope` + `__nowrap`
  - Fließtext (Beschreibung, Tech Stack, Darf, Liefert, Was, Wie, Prüfung): `__text`; lange Listen (Maßnahmen): `__text` + `__text--wide`
  - Aktionen: `__actions`, immer letzte Spalte, Knöpfe rechtsbündig, Spalte nur so breit wie die Knöpfe; den freien Platz nimmt die Namensspalte; `__actions--start` nur in Doku-Tabellen, wo Aktionen vorn stehen
  - Bekannte Abweichung: „Umfang“ im Lagebild ohne Balken bleibt `__nowrap`.
- **Nummer, Symbol und Name auf einer Linie:** Vor dem Namen steht ein Monogramm oder ein Symbol; beide sitzen mittig zur Namenszeile, die laufende Nummer ebenso. Das regelt das Kit für `km-monogram` und für ein Symbol (`svg`) direkt im `km-table__name`; Seiten setzen dafür keine eigenen Abstände.
- **Kopf-Icons in jeder Spalte;** die Aktionsspalte zeigt nur das Icon, der Name steht als `kern-sr-only`.
- **Laufende Nummer:** `km-table--numbered`; Gruppenzeilen und ausgeblendete Zeilen zählen nicht, die Zahl sitzt mittig zur ersten Zeile bzw. zum Monogramm.
- **Nummer nur, wo die Reihenfolge zählt:** `km-table--numbered` bei Projekt-, Datei- und Ergebnislisten, nicht bei Aufbau-, Zustands- oder Token-Tabellen der Doku.
- **Doku-Tabellen nach Rolle:** „Teil“ ist Name (`km-table__name`, Textschrift, kräftig), „Klasse“ und „Token“ sind Kennung (`km-table__key`, Mono, normal) mit Kopieren-Knopf in der Aktionsspalte rechts, „Funktion“ und „Beschreibung“ sind Fließtext (`__text`). Code in Zellen steht als Code (Backticks werden zu `<code>`); `tools/pruefe-seiten.py` prüft das.
- **Typ neben dem Namen:** `km-table__tool` (Code/Desktop/Archiv, WordPress/Ordner …) als eigene kleine Spalte rechts im Namensfeld, im Kopf als Knopf, der nach Typ sortiert (Pfeil, keine Unterstreichung).
- **Unterzeilen:** `km-table__row--sub` mit Einrückungswinkel am Namen (`km-table__name`, auch ohne Link); die Zeilennummer rückt nicht ein; Unterzeilen bleiben beim Sortieren unter ihrer Elternzeile. Versionen, Doku-Unterseiten u. Ä. sind Unterzeilen des Ordners, mit Titel und Datum der Live-Seite in „Was läuft“.
- **Gruppenzeilen** `km-table__group` mit Farbkante als Innenschatten, klappbar, mit Anzahl.
- **Aktionen rechts:** letzte Spalte `km-table__actions` mit `km-table__actions-row` und `km-iconbtn`, nicht sortierbar, in jedem Spalten-Set sichtbar. Kopier-Knöpfe gehören dorthin, nicht in die Namens- oder Wertzelle. Bei Zugängen drei Knöpfe in fester Reihenfolge: Link (Kopier-Icon), Passwort (Schlüssel-Icon wie der Spaltenkopf), Link + Benutzer + Passwort als eine Nachricht (Sprechblase). Werte erst beim Klick aus der Zeile lesen.
- **Aktionen immer ganz rechts, fest, mit Verlauf:** nie in einer mittleren Spalte, auch nicht in Dokumentlisten. Die Spalte bleibt beim waagerechten Scrollen stehen (`position: sticky` über `km-table__actions:last-child`), der Inhalt davor läuft in einem Verlauf aus, solange rechts noch etwas kommt (`km-scroll--more` am Rahmen).
- **Name zuerst, gleiche Anordnung überall:** erste Spalte ist der Name (Projekt, Datei, Host), dann Werte, Fließtext, Datum, zuletzt Aktionen. Dokumentlisten folgen derselben Ordnung wie die Projektübersicht: Datei, Typ, Beschreibung, Umfang, Update, Aktionen.
- **Jede Tabelle im Rahmen** (`km-table-wrap`), wie die Projektübersicht; keine Tabelle frei im Inhalt.
- **Tabellen nicht verstecken:** keine Aufklapp-Zeile („… anzeigen“) vor einer Tabelle; Tabelle immer offen, darüber eine Zwischenüberschrift `km-subhead` mit Icon und Anzahl.
- **Kompakt nur für Dokumentlisten** (`km-table--compact`), sonst Standard-Tabelle.
- **Spaltenauswahl mit Sets** (`km-colpicker__set`): einige benannte Kombinationen und „Alle“; Name und Aktionen sind immer dabei; ein Set ist gedrückt, wenn die Auswahl ihm genau entspricht.
- **Status als Etikett** (`km-pill`, `--ok/--warn/--danger/--neutral`); leer heißt „ohne Wert“, nicht „ok“.

## Karten

- **Kartenkopf** `km-card__head` mit Kachel und Titel; der Titel hat eine Mindestbreite, Etiketten rutschen darunter, statt den Titel senkrecht zu quetschen.
- **Info-Karten nebeneinander** (`km-card--info` im Raster) statt Tabellen, wenn Inhalte Text sind.
- **Farbstrich links nur an der innersten Karte;** äußere Container-Karten haben keinen Akzentstrich.

## Bedienzeilen

- **Gleich hoch nebeneinander:** Eingabefeld, Auswahl (Dropdown), Segmented Control und Knopf in einer Zeile sind gleich hoch. Immer in `km-toolbar` setzen, die streckt alle auf die höchste; nie eigene Höhen an einzelnen Elementen. Nach jeder neuen Bedienzeile die Höhen per `getBoundingClientRect()` messen.

## Auswahl, Menüs und Segmented Control

- **Jedes Panel schließt mit Esc und mit Klick daneben:** danach Fokus zurück auf den auslösenden Knopf (bei Klick daneben nur, wenn der Fokus im Panel lag). Das Kit erledigt das für jeden Knopf mit `aria-expanded="true"`, der ein schwebendes Panel öffnet (`aria-haspopup` oder Panel per `aria-controls` bzw. als nächstes Geschwister, absolut oder fest positioniert): `src/km-popup.js`, eingebettet mit `einbetten.py`, auf den System-Seiten verlinkt. Eigene Handler der Seite laufen zuerst; das Kit schließt, was danach noch offen ist. Schwebende Vorschau (`km-peek`) schließt mit Esc. Prüfung: `dashboard-check.py` und `tools/pruefe-seiten.py` öffnen jeden Panel-Knopf headless und testen Esc, Klick daneben und Fokus.

- **Auswahl mit Suche statt freiem Feld:** Wo aus einer Menge gewählt wird (Projekte einer Liste, Icon), öffnet ein Knopf mit Text, Anzahl und Pfeil (`km-button`) das Panel `km-selectpanel` (Muster „SelectPanel“ bei Primer, Combobox mit Listbox-Popup im WAI-ARIA-Leitfaden): Fokus im Filterfeld, darunter alle Einträge mit Kästchen und Monogramm in einer scrollenden Liste (`km-selectpanel__list`), ausgewählte zuerst, Fuß mit „95 Projekte · 4 ausgewählt“; Enter nimmt den ersten passenden Treffer, Esc, Klick daneben oder erneuter Klick schließen. Nur das Icon-Raster zeigt höchstens 48 Treffer, weil es 1.857 Icons sind.
- **Ein Knopf-Baustein für Text-Knöpfe:** `km-button` in Textschrift, so hoch wie Segmented Control und Eingabefeld; keine Text-Knöpfe in Mono-Schrift, keine Segment-Optik für Knöpfe, die nichts auswählen. Nur-Icon-Knöpfe bleiben `km-iconbtn`.
- **Fokus am Suchfeld nur einmal:** der Rahmen des Felds wird kräftig, das Eingabefeld darin bekommt keinen zweiten Rahmen.
- **Seltene Aktionen als Knopf, nicht als großes Feld:** „Neue Liste“ ist ein eigener Knopf in eigener Gruppe neben dem Segmented Control (`km-segmented` mit einem Knopf), nicht Teil davon, weil er nichts auswählt; so hoch wie ein Segment. Der Name wird im Menü eingegeben.
- **Jede Liste von Dingen ist die Standard-Tabelle:** Projekte, Dateien, Hosts erscheinen überall wie in der Projektübersicht: laufende Nummer (`km-table--numbered`), Name mit Monogramm/Favicon (`km-table__name` + `km-monogram`), Werte wie Phase als Pill, Aktionen rechts. Auch in Auswahlmenüs steht das Monogramm vor dem Namen. Keine abgespeckte Eigen-Tabelle.
- **Viele Segmente brechen um** (`km-segmented--wrap`), statt aus dem Bereich zu laufen; Segmente tragen ihr Icon vor dem Namen und die Anzahl dahinter.
- **Bearbeiten im Menü:** Name, Icon und Löschen einer Sache stehen gesammelt hinter „… bearbeiten“; Löschen unten im Menü, zweistufig („Wirklich löschen?“), kein `confirm`, nie neben dem Segmented Control.
- **Icons:** Lucide 1.49.0 (`assets/lucide.json`). Wo Nutzer\*innen etwas benennen (Listen), ein Icon vorschlagen und eine Auswahl aus allen Icons mit Suche anbieten; die Suche läuft über die englischen Lucide-Begriffe.
- **Begriffe:** die rechte Spalte heißt „Sidebar“ (Dashboard und Lagebild, 2026-11-09); `km-segmented` heißt „Segmented Control“, seine Teile Segmente; „Reiter“ nur für echte Tabs.

- **Ausgewählt bleibt ausgewählt, auch unter der Maus:** Gedrückte Knöpfe, Sets, Segmente und gewählte Einträge der Seitenleiste behalten ihre Farbe, wenn die Maus darüber steht; Hover darf nur nicht ausgewählte Elemente aufhellen. Im Kit gesammelt am Ende von `src/km-components.css`; jeder neue Baustein mit Auswahl-Zustand bekommt dort eine Zeile.
- **Global denken:** Jede Rückmeldung zu einem Element gilt für das ganze Design-System: erst prüfen, ob das Problem ein Baustein im Kit ist, dort beheben und in Dashboard und Lagebild einbetten, nicht nur an der gemeldeten Stelle.

## Filter und Verlauf

- **Ein Filter zur Zeit aus der Navigation:** Eine neue Auswahl (Kunde, Typ, Phase, Schalter, Bereich, Suche) hebt einen gesetzten Listenfilter auf.
- **Zurück und Vorwärts zeigen genau die gewählte Ansicht:** Jede Filterwahl ist ein Schritt im Verlauf; das Wiederherstellen legt keinen neuen Schritt an (sonst ist Vorwärts weg); auch Schritte nach einem Sprung auf einen Anker (`#…`) stellen die Auswahl aus der Adresse wieder her.
- **Adresse mit Auswahl zeigt die Übersicht von oben:** Aufruf mit `?kunde=…`, `?typ=…`, `?phase=…` und Zurück/Vorwärts springen zur Übersicht; Zurück nach einem Anker-Sprung stellt die alte Position her.

## Kopfzeile

- Knöpfe rechts in fester Reihenfolge der Seite, gleiche Höhe (`km-iconbtn--label`), Theme-Schalter ganz rechts. Befehlsknöpfe kopieren den Befehl, sie führen nichts aus.

## Dokumentation

- **Nie hinter Aufklapp-Elementen:** Dokumentation ist sofort sichtbar, ohne `details`, Toggles oder Reiter innerhalb einer Doku; gegliedert über Zwischenüberschriften (`km-subhead` mit Icon) und feste Abschnitte, kurze Abschnitte nebeneinander, lange untereinander. Auch Code-Beispiele und Markup stehen offen da.
- **Eine Story je Baustein:** Varianten eines Bausteins stehen in seiner einen Story, je Variante mit Zwischenüberschrift; im Kit aufgegangene Vorschläge erscheinen nicht mehr unter „Proposals“.
- **Doku im Stil der Einführung (seit 0.9.0):** Jede Doku-Seite und jeder Baustein beginnt mit Titel und Einleitung (`km-hero`, `km-lead`); Inhalte stehen als Karten mit Icon im Raster (`km-cards--wide` bzw. `--two`, `km-card` mit `km-card__tile`), nicht als Fließtext-Block: Einsatz, Abgrenzung, Zustände, Barrierefreiheit, Richtig und Falsch je eine Karte. Grafiken in voller Breite als `km-figure` mit Bildunterschrift, Inline-SVG mit `--km-*`-Farben, damit sie dem Theme folgen; Zitate als `km-callout--quote`; Tabellen als Standard-Tabelle; Code als `km-codeblock`; Lesetext in `km-prose`. Nichts ist aufklappbar. Vorbild und Quelle: `tools/einfuehrung.py` (Startseite in Komponentenbeschreibung und Doku). Prüfung bei 390 px: keine waagerechte Scrollleiste, breite Vorführungen scrollen in ihrer `km-figure__media`.
- **Komponenten-Doku: Fakten als Kacheln, Rubriken als Karten im Raster, Paare nebeneinander (DDR 48):** Kopf mit Titel, Zweck als `km-lead` (ein bis zwei Sätze) und Fakten-Kacheln im Raster mit gleichen Spalten (`km-facts--cols`: Status, Klasse, Varianten, Stand, Kontrast, Stories, Quellen); dann Vorschau, dann Rubriken als Karten mit Icon in `km-cards--two`. Paare stehen nebeneinander (Verwenden | Nicht verwenden, Verhalten | Barrierefreiheit, Richtig | Falsch, Abgrenzung | Verwandte, Tokens | Bezug); Tabellen, Markup und Vergleich über die ganze Breite, ebenso eine halbe Karte ohne Partner. Listen kurz, ein Satz je Punkt.
- **Komponenten-Doku im Aufbau D „Vier Fragen mit Kapitelleiste“:** Titel, Einleitung, Fakten-Kacheln, offene Punkte als Hinweiskasten (`km-callout--attention`) oben, dann vier Kapitel „1 · Was ist es?“ (Beispiel, Überblick, Varianten, Name und Abgrenzung), „2 · Wann nehmen?“ (Verwenden, Nicht verwenden, Verwandte, Zusammenhang, Vergleich), „3 · Wie bauen?“ (Aufbau mit Grundmarkup, Text, Tokens, Richtig, Falsch, Markup der Story), „4 · Wie prüfen?“ (Zustände, Verhalten, Barrierefreiheit mit Kontrast, Größen, Bezug); jedes Kapitel endet mit dem Kasten „Regel:“ aus `## Regeln` der Quelle (`- Was:`, `- Wann:`, `- Wie:`, `- Prüfen:`, je ein Satz nur aus derselben Datei). Kapiteltitel `km-doc__title--icon`, rechts die Kapitelleiste `km-chapters__nav` (markiert beim Scrollen, Sprung ohne Animation, schmal über dem Inhalt), Code mit Kopieren oben rechts im Block (`km-codeblock__box`). Jeder Inhalt genau einmal, nichts aufklappbar, nichts frei stehend; Über jedem Kapiteltitel 64 px (`--km-space-heading-major`). Quelle: `tools/komponenten_doku.py`.
- **Ein Listenzeichen (DDR 46):** Alle ungeordneten Listen tragen den Pfeil (Lucide chevron-right als Maske) in Kartenfarbe bzw. Akzent, mittig zur ersten Zeile; zentral im Kit für `km-prose`, `km-panel` und `km-list`. Seiten setzen keine eigenen Listenzeichen.
- **Datum deutsch:** In Kacheln, Tabellen und Fließtext `TT.MM.JJJJ` (09.11.2026); ausgeschrieben („9. November 2026“) nur in Überschriften. ISO-Datum nur in Dateinamen und Kopfzeilen von Quelldateien.
- **Listen zweispaltig nur für viele kurze, gleichartige Punkte (0.13.0):** Eine Liste darf auf breiten Flächen zweispaltig stehen (`km-prose--columns`), wenn ihre Punkte einzeln für sich stehen und keine Reihenfolge von oben nach unten tragen (Changelog je Version, Sammlungen von Änderungen oder Merkmalen). Jede Spalte ist mindestens `--km-metric-measure-column` breit (24em, rund 52 Zeichen), sonst einspaltig; ein Punkt wird nie über zwei Spalten getrennt (`break-inside: avoid`). Nicht zweispaltig: Schrittfolgen, Anleitungen, Listen unter fünf Punkten, Listen mit Unterpunkten, die länger als der Hauptpunkt sind. Messen: Spaltenzahl bei 1440 und 390 px, kein Punkt mit zwei Teilen.
- **Entscheidungen: Kopf als Meta-Zeile, fünf Abschnitte:** Unter dem Titel eine Zeile `km-metaline` (Typ · Status als Pill · Datum `TT.MM.JJJJ` · Tags · Bezug mit Links), Bedienelement der Karte (Umschalter Text/Markdown) rechts darin als `km-metaline__end`; keine Fakten-Kacheln, wenn alle Werte kurz sind. Was der Kopf zeigt, steht nicht noch einmal im Text. Die Text-Ansicht rendert die Quelle ab dem ersten Abschnitt nach `## Status` in Reihenfolge (Kontext, Entscheidung, Begründung, Folgen, Verlauf als Zwischentitel mit Icon); offene Fragen offener Einträge rechts unter „Deine Bewertung“, entschiedener im Text.
- **Seitenfuß der System-Seiten:** Komponentenbeschreibung, Doku und Entscheidungen tragen unten links die Eckleiste (`km-corner`) mit Changelog, Impressum und Datenschutz, immer zusammen.
- **Eckleiste verdeckt nichts (0.13.0):** Steht die Eckleiste (`km-corner`) neben einer Seitenleiste, endet der Scrollbereich der Navigation über ihr: die Seite gibt der Navigation unten `--km-component-corner-space` frei (`margin-bottom` an der scrollenden Navigation bzw. weniger `max-height` bei `position: sticky`), statt nur Innenabstand am Ende. Eingeklappt (Rail) zeigt das Kit die Einträge der Eckleiste untereinander und nur als Icon; jeder Eintrag braucht deshalb ein Lucide-Icon und einen `title`. Messen: kein Eintrag der Navigation schneidet die Eckleiste, aufgeklappt, gescrollt und eingeklappt, bei 900 und 600 px Fensterhöhe; die Eckleiste ragt nicht in die Mitte.

## Geheimnisse

- **Passwörter starten verdeckt,** jedes Feld einzeln umschaltbar (`km-secret`), dazu ein Knopf „Passwörter“ in der Kopfzeile für alle; dieser Zustand wird nie gespeichert.
- Passwörter erscheinen nie in Doku, Storys, Changelog, Memory oder Ausgaben; Prüfungen geben nur Anzahlen aus.

## Prüfen vor der Meldung

- **Keine Kundenbezüge in Geteiltem:** In allem, was Kernmix weitergibt (Doku, Entscheidungen, Komponentenbeschreibung, Design-Runden, `src/`, `dist/`, `tools/`, README, Changelog), stehen keine Kunden-, Projekt- oder Personennamen Dritter; Herkunft heißt „aus früherer Design-System-Arbeit“, Beispiele sind erfunden („Kunde A“, „Projekt 1“). Eigene Projekte (Dashboard, Lagebild, KI-Design-Runde, Startklar, Beyond Tape, Projektschau, Ferienjob-Finder) dürfen genannt werden. Prüfung: `tools/pruefe-sperrliste.py` meldet 0 Treffer; `tools/build-online.py` ruft sie vor und nach dem Bauen auf und bricht sonst ab.
- Keine JS-Fehler, Seiten-Prüfskript ohne Befund (Dashboard die Strukturprüfung des Dashboards, Lagebild Zahlen-Check: alle Geheimnisse verdeckt, Marker intakt).
- Gemessen statt behauptet: Abstände, Mittigkeit, Überlappung, Zeilenhöhe; Screenshot-Ausschnitt bei Lageänderungen; beide Themes, wenn Farben betroffen sind.

## Kontrast und schmale Breite (aus der Sichtprüfung 2026-11-08)

- **Fokus an `tabindex`-Elementen:** KERN nimmt `[tabindex]` den Fokusrahmen (`outline: 0` bei `:focus-visible`); das Kit setzt ihn für km-Elemente wieder. Eigene fokussierbare Elemente brauchen deshalb eine km-Klasse, sonst fehlt der Fokus (Startklar, 0.10.0).
- **Antworten zurücksetzbar:** Wo eine Frage mit Knöpfen beantwortet wird, setzt ein zweiter Klick auf die gewählte Antwort sie zurück (`km-answer`, Skript der Seite); keine eigene Leeren-Schaltfläche.
- **Kein Abblenden mit `opacity` für Inhalt.** Gedämpfter Text bekommt `--km-color-text-dim` oder `--km-color-text-muted`; `opacity` nur für echte Deaktivierung (`--km-opacity-disabled`) und vorübergehende Zustände (Ziehen). „Erledigt“ ist kein deaktivierter Zustand.
- **Ränder von Eingabefeldern und Kästchen ≥ 3:1** über `--km-color-border-input`; Datenfarben (Werkzeug, Kategorie) auf der Fläche ≥ 3:1, je Modus.
- **Keine Schriftzeichen als Icon**, auch nicht in CSS (`content: "›"`, „▲▼“, „×“): Lucide als Maske (`--km-mask-*`) oder SVG; Sortierpfeil ist ein flaches Dreieck (`--km-sort-w`, `--km-sort-h`).
- **Schmal (390 px) prüfen:** keine waagerechte Scrollleiste der Seite. Raster mit `minmax(min(Xrem, 100%), 1fr)`, breite Tabellen und Grafiken in scrollenden Rahmen mit `position: relative`, lange Pfade und Titel dürfen unter 40rem umbrechen, zweispaltige Bausteine stapeln per Container-Abfrage.
- **Grafiken haben eine Hochformat-Fassung (0.13.0):** Erklärgrafiken (Inline-SVG in `km-figure`) gibt es quer und hoch mit denselben Inhalten (`km-figure__wide` und `km-figure__tall` in derselben `km-figure__media`); das Kit zeigt die Hochformat-Fassung, sobald die Fläche schmaler als 56rem ist (Container-Abfrage, greift auch in schmalen Spalten). Die Hochformat-Fassung ist 250 Einheiten breit (`HOCH_B` in `tools/grafik_stil.py`, Umbruch mit `zeilen()`/`text_zeilen()`), höchstens `--km-component-figure-tall-max-width` breit dargestellt. Messen: kleinste Schrift in der sichtbaren Fassung bei 390 px mindestens 12 px gerendert (Schriftgröße × gerenderte Breite / viewBox-Breite), kein Text über seinen Kasten hinaus.
- **Beispiele in Stories ohne harte Farben:** Platzhalterfarben über Theme-Tokens (Akzent, Signal, Werkzeugfarben), keine Kundenfarben.

## Breite und Ausrichtung

- **Text schmal, breite Bausteine voll (DDR 44):** Fließtext, Listen, Überschriften und Hinweise höchstens ~70 Zeichen; Tabellen, Abbildungen, Kartenraster und Code nutzen die volle Breite des Inhalts.
- **Kästchen und Icons mittig zur ersten Zeile (DDR 45, ergänzt DDR 42):** Kästchen erben Schrift und Zeilenhöhe der Zeile; Etiketten in einer Textzeile machen die Zeile nicht höher. Nach dem Bau messen: Mitte Kästchen zu Mitte erste Zeile ≤ 1 px.
- **Titel-Link ohne Unterstreichung:** Logo und Name, die zur Startseite führen, sind nicht unterstrichen.
- **Zwischentitel in Jade (DDR 49):** Abschnittstitel und Überzeilen der Doku-Seiten in der Zweitfarbe `--km-color-heading-secondary`, eine Farbe für alle Bereiche; Grafiken je Grafik eine Akzentfarbe.
- Über Zwischentiteln im Lauftext steht `--km-space-heading` (32 px), so viel wie über den Abschnittstiteln der Einführung.
- Text- und Markdown-Ansicht eines Dokuments zeigen denselben Inhalt in derselben Reihenfolge; die Text-Ansicht setzt nur Überschriften und Auszeichnung.
- **Scrollende Seitenleiste:** Hat der Container der `km-sidebar` einen eigenen Scrollbereich (`overflow: auto`), bekommt sie die Klasse `km-sidebar--scroll` (Innenrand links `--km-sidebar-inset`, gleich großer negativer Außenrand, Scrollen eingebaut). Sonst schneidet der Scrollbereich die Auswahlfläche links ab, die über das Icon hinausreicht.
- **„Alle“ ist eine Auswahl:** In jeder Filtergruppe der Seitenleiste (Kunden, Typ, Phase) zeigt „Alle“ den gedrückten Zustand (`aria-pressed="true"`), solange in der Gruppe nichts anderes gewählt ist, auch beim ersten Laden.
- **Eine Textkante je Ebene:** In der Seitenleiste beginnen alle Texte einer Ebene an derselben Stelle. Vor jedem Text steht ein Platz so breit wie ein Icon (`--km-icon-s`); Farbpunkte stehen links darin, Einträge ohne Icon („Alle“, Phasen) beginnen links auf Höhe der Icons und Farbpunkte, Schalter stehen rechts. Auswahl immer über die ganze Zeile mit Strich davor, auch bei Einträgen mit Unterebene.
- **Etikett mit ×:** Ein Filter-Etikett mit × ist als Ganzes die Fläche zum Aufheben: Hover und Klick auf dem ganzen Etikett, technisch bleibt der ×-Knopf der eine Knopf (Name, Tastatur).
- **Abstand über Titeln:** Über grünen Abschnittstiteln (`km-doc__title`) stehen 64 px (`--km-space-heading-major`), über Zwischentiteln 32 px (`--km-space-heading`); ein Abschnittstitel hat nie weniger Luft als ein Zwischentitel.
- **Gruppen-Überschriften der Seitenleiste:** Alle Gruppen-Überschriften, ob oberste Ebene oder Untergruppe, stehen hell in Kapitälchen mit Icon davor, wie im Prototyp (Filter, Status, Kunden, Typ, Stand). Das gilt auch für die Pfade im Baum der Komponentenbeschreibung (seit 0.15.0 `km-sidebar__group--tree`).
- **Impressum und Datenschutz:** stehen am Ende der Seitenleiste unten links mit Abstand (`km-sidebar__legal`), scrollen mit, nicht festgeheftet, gedämpft; „Nach oben“ (`km-totop`) rechts unten auf jeder langen Seite.
- **Titelzeile im Hinweiskasten (2026-11-09):** In `km-callout--attention` wird ein Absatz, dessen einziges Element ein `<strong>` ist, als Titelzeile in Versalien gesetzt, auch wenn danach noch Text steht. Text mit fettem Einstieg deshalb als zwei Absätze bauen: `<p><strong>Titel</strong></p><p>Text</p>`.
- **Hinweiskasten unter dem Kopf eng:** Ein Hinweiskasten direkt unter Kopf oder Fakten steht mit `--km-space-group` darunter, nicht mit dem Abschnittsabstand.
- **Trenner am vorderen Teil:** In einer umbrechenden Zeile mit Trennern („·“) hängt der Trenner am vorderen Teil; keine Zeile beginnt mit einem Trenner.
