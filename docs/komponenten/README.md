# Komponenten-Dokus

Hier steht je Baustein von Kernmix (Werkzeug-Bausteine, Präfix `km-`) eine Doku nach der [Vorlage](vorlage.md). Quelle der Bausteine sind `tools/bausteine.py` und `tools/bausteine_nachtrag.py` (Kurzbeschreibung und Beispiel-Markup, daraus `docs/index.html` und die Komponentenbeschreibung), das CSS steht in `src/km-components.css`. Die Token-Ebenen beschreibt [`../tokens-ebenen.md`](../tokens-ebenen.md).

Stand 2026-11-09: 65 Stories, 32 Komponenten-Dokus, 65 von 65 Stories mit Doku. Eine Doku kann mehrere eng verwandte Stories abdecken; eine Story kann mehrere Dokus berühren (die erste ist ihre Heimat).

## KERN-Bausteine

Für Bausteine des KERN-Kits selbst (`kern-*`, Gruppe „KERN-Standard“ in der Komponentenbeschreibung) gibt es hier keine eigene Doku. Die Komponentenbeschreibung verweist je KERN-Story auf den Code im offiziellen Repository (`gitlab.opencode.de/kern-ux/kern-ux-plain`, Tag der eingebundenen Version) und auf die Seite der Komponente auf kern-ux.de; die Liste steht in `tools/build-storybook.py` (`KERN_DOKU`). Eigene Erweiterungen eines KERN-Bausteins (z. B. Dialog-Zusätze) haben eine Doku hier.

## In der Komponentenbeschreibung

`tools/build-storybook.py` zeigt unter dem Titel jeder Erweiterungs-Story die zugeordneten Dokus als aufklappbare Abschnitte. Die Zuordnung Story → Doku steht dort in `DOKU` (Schlüssel ist der Anker aus `tools/bausteine*.py`); eine neue Story ohne Eintrag meldet der Build. Das Markdown setzt die Funktion `md()` aus `tools/build-entscheidungen.py` um, ergänzt um Tabellen, Code-Blöcke und Links.

## Für Agenten

Vor dem Bauen einer Seite: `../seitenregeln.md`, dann die Doku jedes Bausteins, den die Seite nutzt, besonders die Abschnitte „Einsatz“, „Beispiele“ und „Offene Punkte“. Kontrastwerte sind für die Themes Kobalt und Papier je hell und dunkel gerechnet (headless Chrome, WCAG-Formel).

## Dokus

| Doku | Klassen | Heimat-Stories |
|---|---|---|
| [Agenten-Karte](agent.md) | `km-agent` | `#agent`, `#agenten-varianten` |
| [Antwort-Knöpfe](antwort.md) | `km-answer` | `#antwort` |
| [Aufgabe und Vorschläge](aufgabe.md) | `km-task`, `km-suggest` | `#aufgabe`, `#aufgabe-loeschen`, `#vorschlaege` |
| [Auswahl mit Suche](auswahl-mit-suche.md) | `km-selectpanel` | `#selectpanel` |
| [Bereich](bereich.md) | `km-section`, `km-subhead`, `km-cardgroup`, `km-focus` | `#bereich`, `#fokus`, `#gruppe`, `#bedienteile` |
| [Dialog-Zusätze](dialog.md) | `km-dialog`, `km-btn--danger` | `#dialog` |
| [Einführung, Einleitung und Funktionsraster](einfuehrung.md) | `km-intro`, `km-hero`, `km-features` | `#einfuehrung`, `#hero`, `#funktionen` |
| [Pill und Chip](etikett.md) | `km-pill`, `km-chip` | `#chip-pill`, `#noten` |
| [Filter-Leiste und Filtergruppe](filterleiste.md) | `km-filterchips--bar`, `km-sidebar__group--filter` | `#filterleiste` |
| [Grafik „Wer ruft wen auf“](grafik.md) | `km-graph` | `#grafik`, `#grafik-zustaende` |
| [Icon-Knopf](icon-knopf.md) | `km-iconbtn` | `#zustaende` |
| [Karte](karte.md) | `km-card`, `km-cards` | `#karte`, `#projektkarte`, `#info-karte`, `#kuerzel` |
| [Kennzahlen](kennzahlen.md) | `km-facts`, `km-bars`, `km-histo` | `#fakten`, `#kacheln-raster`, `#kennzahlen` |
| [Meta-Zeile](metaline.md) | `km-metaline` | `#metaline` |
| [Kleinteile](kleinteile.md) | `km-clear`, `km-info`, `km-count`, `km-dot`, `km-caret`, `km-peek`, `km-timelog` | `#zeitlog`, `#kleinteile`, `#einheitlich`, `#werkzeugfarben`, `#vorschaukarte` |
| [Knopf mit Text](knopf.md) | `km-button` | `#knopf` |
| [Kopfzeile](kopfzeile.md) | `km-header`, `km-quicklinks`, `km-brand` | `#quicklinks` |
| [Angabenliste und Maßnahmenliste](listen.md) | `km-deflist`, `km-measures` | `#massnahmen`, `#angaben` |
| [Monogramm](monogramm.md) | `km-monogram` | (nur als zweite Doku zugeordnet) |
| [Schalter und Kästchen](schalter.md) | `km-switch`, `km-check`, `km-demo`, `km-sync` | `#schalter`, `#kontrollkaestchen` |
| [Segmented Control](segmented-control.md) | `km-segmented`, `km-segmented--wrap` | `#segmented` (beide Varianten) |
| [Prüfkarte, Feld und Begriff](pruefkarte.md) | `km-criterion`, `km-field`, `km-term` | `#pruefkarte` |
| [Score und Fortschritt](score.md) | `km-score`, `km-progress` | `#score` |
| [Seitenleiste](seitenleiste.md) | `km-sidebar` | `#seitenleiste`, `#sidebar-hierarchie`, `#sidebar-rail` |
| [Seitenrahmen: Fläche, Fußzeile, Eckleiste, Nach oben](seitenrahmen.md) | `km-page`, `km-footer`, `km-corner`, `km-totop` | `#teilstuecke`, `#eckleiste` |
| [Spaltenauswahl](spaltenauswahl.md) | `km-colpicker` | `#zustaende-skript` |
| [Suchfeld und Bedienzeile](suchfeld.md) | `km-searchbox`, `km-toolbar`, `km-filterchips` | `#suche`, `#suchfeld` |
| [Tabelle](tabelle.md) | `km-table` | `#tabelle`, `#tabelle-spalten`, `#tabelle-regeln`, `#unterzeilen`, `#zahlenliste` |
| [Hinweis, Fließtext und Textlinks](text.md) | `km-note`, `km-prose`, `km-link`, `km-details` | `#fliesstext`, `#textlinks` |
| [Trefferliste der Suche](trefferliste.md) | `km-results` | `#treffer-kopf`, `#trefferliste`, `#suchhinweise` |
| [Verdeckter Wert](verdeckter-wert.md) | `km-secret` | `#verdeckt` |
| [Ziehen und Ablegen](ziehen.md) | `km-dnd`, `km-resizer` | (nur als zweite Doku zugeordnet) |

## Alle Stories

Reihenfolge wie in `docs/index.html`. „Klassen“ nennt bis zu vier Blöcke, die die Story zeigt.

| Story | Klassen | Anker | Doku |
|---|---|---|---|
| Seitenleiste | `km-sidebar`, `km-switch` | `#seitenleiste` | [seitenleiste.md](seitenleiste.md), [schalter.md](schalter.md) |
| Bereich | `km-card`, `km-section` | `#bereich` | [bereich.md](bereich.md) |
| Karte | `km-card`, `km-card--accent-left`, `km-card--accent-top`, `km-card--interactive` | `#karte` | [karte.md](karte.md) |
| Projektkarte | `km-card`, `km-card--accent-left`, `km-card--collapsible`, `km-chip` | `#projektkarte` | [karte.md](karte.md), [kennzahlen.md](kennzahlen.md) |
| Einführung | `km-intro` | `#einfuehrung` | [einfuehrung.md](einfuehrung.md) |
| Fakten-Kacheln | `km-fact`, `km-facts` | `#fakten` | [kennzahlen.md](kennzahlen.md) |
| Aufgabe | `km-chip`, `km-iconbtn`, `km-iconbtn--attention`, `km-iconbtn--danger` | `#aufgabe` | [aufgabe.md](aufgabe.md), [icon-knopf.md](icon-knopf.md) |
| Kürzel-Karte | `km-card`, `km-card--accent-top`, `km-cards`, `km-chip` | `#kuerzel` | [karte.md](karte.md) |
| Zwischenüberschrift, Hinweis, Farbpunkte | `km-dots`, `km-note`, `km-subhead` | `#gruppe` | [bereich.md](bereich.md), [text.md](text.md), [kleinteile.md](kleinteile.md) |
| Chip und Pill | `km-chip`, `km-pill`, `km-pill--danger`, `km-pill--info` | `#chip-pill` | [etikett.md](etikett.md) |
| Schalter und Demo | `km-demo`, `km-switch` | `#schalter` | [schalter.md](schalter.md) |
| Eckleiste | `km-corner`, `km-demo`, `km-demo--fixed` | `#eckleiste` | [seitenrahmen.md](seitenrahmen.md), [schalter.md](schalter.md) |
| Suche: Filter und Ergebnisse | `km-filterchips`, `km-results`, `km-toolbar` | `#suche` | [suchfeld.md](suchfeld.md), [trefferliste.md](trefferliste.md) |
| Quicklinks | `km-monogram`, `km-quicklinks` | `#quicklinks` | [kopfzeile.md](kopfzeile.md), [monogramm.md](monogramm.md) |
| Fußzeile mit Kennzahlen | `km-bars`, `km-histo` | `#kennzahlen` | [kennzahlen.md](kennzahlen.md), [seitenrahmen.md](seitenrahmen.md) |
| Agenten-Karte | `km-agent` | `#agent` | [agent.md](agent.md) |
| Grafik „Wer ruft wen auf“ | `km-graph` | `#grafik` | [grafik.md](grafik.md) |
| Segmented Control | `km-segmented` | `#segmented` | [segmented-control.md](segmented-control.md) |
| Suchfeld mit Spalten-Auswahl | `km-colpicker`, `km-iconbtn`, `km-iconbtn--label`, `km-searchbox` | `#suchfeld` | [suchfeld.md](suchfeld.md), [spaltenauswahl.md](spaltenauswahl.md) |
| Vorschläge | `km-iconbtn`, `km-iconbtn--label`, `km-section`, `km-suggest` | `#vorschlaege` | [aufgabe.md](aufgabe.md) |
| Zeitlog | `km-timelog` | `#zeitlog` | [kleinteile.md](kleinteile.md) |
| Info-i, Sync-Schalter, Nach oben | `km-infoi`, `km-sync`, `km-sync--on`, `km-totop` | `#kleinteile` | [kleinteile.md](kleinteile.md), [schalter.md](schalter.md), [seitenrahmen.md](seitenrahmen.md) |
| Tabelle | `km-chip`, `km-chip--extern`, `km-iconbtn`, `km-iconbtn--attention` | `#tabelle` | [tabelle.md](tabelle.md), [monogramm.md](monogramm.md), [etikett.md](etikett.md) |
| Grafik: Knoten, Kanten und Zustände | `km-graph` | `#grafik-zustaende` | [grafik.md](grafik.md) |
| Tabelle: Spalten und Verhalten | `km-iconbtn`, `km-iconbtn--label`, `km-monogram`, `km-scroll--more` | `#tabelle-spalten` | [tabelle.md](tabelle.md) |
| Vorschaukarte | `km-peek` | `#vorschaukarte` | [kleinteile.md](kleinteile.md) |
| Fließtext, Details und Kartenfußnote | `km-card`, `km-details`, `km-prose` | `#fliesstext` | [text.md](text.md), [karte.md](karte.md) |
| Dialog-Zusätze | `km-btn--danger`, `km-dialog`, `km-note` | `#dialog` | [dialog.md](dialog.md) |
| Hervorgehobener Bereich | `km-focus`, `km-table` | `#fokus` | [bereich.md](bereich.md) |
| Suchhinweise | `km-results`, `km-results--hints` | `#suchhinweise` | [trefferliste.md](trefferliste.md) |
| Aufgabe: Löschen bestätigen | `km-task` | `#aufgabe-loeschen` | [aufgabe.md](aufgabe.md) |
| Agenten: Raster und Varianten | `km-agent` | `#agenten-varianten` | [agent.md](agent.md) |
| Zustände | `km-iconbtn`, `km-iconbtn--label`, `km-iconbtn--on`, `km-pill` | `#zustaende` | [icon-knopf.md](icon-knopf.md), [tabelle.md](tabelle.md), [aufgabe.md](aufgabe.md), [etikett.md](etikett.md), [kopfzeile.md](kopfzeile.md) |
| Suche: Kopf der Trefferliste | `km-filterchips`, `km-iconbtn`, `km-iconbtn--label`, `km-results` | `#treffer-kopf` | [trefferliste.md](trefferliste.md), [suchfeld.md](suchfeld.md) |
| Fußzeile, Bereichskopf und Kleinteile | `km-card`, `km-card--sub`, `km-focus`, `km-footer` | `#teilstuecke` | [seitenrahmen.md](seitenrahmen.md), [bereich.md](bereich.md), [karte.md](karte.md), [text.md](text.md) |
| Ziehen, Leisten und Suchfelder | `km-brand`, `km-card`, `km-card--sub-2`, `km-cardgroup` | `#bedienteile` | [bereich.md](bereich.md), [suchfeld.md](suchfeld.md), [kopfzeile.md](kopfzeile.md), [ziehen.md](ziehen.md) |
| Zustände per Skript | `km-cardgroup`, `km-colpicker`, `km-focus`, `km-footer` | `#zustaende-skript` | [spaltenauswahl.md](spaltenauswahl.md), [suchfeld.md](suchfeld.md), [aufgabe.md](aufgabe.md), [bereich.md](bereich.md), [seitenrahmen.md](seitenrahmen.md) |
| Noten A bis D | `km-pill`, `km-pill--grade`, `km-pill--grade-a`, `km-pill--grade-b` | `#noten` | [etikett.md](etikett.md) |
| Maßnahmen mit Punktwert | `km-measures` | `#massnahmen` | [listen.md](listen.md) |
| Verdeckter Wert | `km-iconbtn`, `km-iconbtn--done`, `km-secret` | `#verdeckt` | [verdeckter-wert.md](verdeckter-wert.md), [icon-knopf.md](icon-knopf.md) |
| Einleitung mit Kennzahlen | `km-fact`, `km-facts`, `km-hero` | `#hero` | [einfuehrung.md](einfuehrung.md), [kennzahlen.md](kennzahlen.md) |
| Funktionsraster | `km-feature`, `km-features` | `#funktionen` | [einfuehrung.md](einfuehrung.md) |
| Suche: Trefferliste | `km-iconbtn`, `km-iconbtn--label`, `km-results`, `km-segmented` | `#trefferliste` | [trefferliste.md](trefferliste.md), [segmented-control.md](segmented-control.md) |
| Kontrollkästchen | `km-check`, `km-demo`, `km-task` | `#kontrollkaestchen` | [schalter.md](schalter.md) |
| Kleinteile: Schließen, Info, Zähler, Punkt, Pfeil | `km-caret`, `km-caret--zu`, `km-clear`, `km-count` | `#einheitlich` | [kleinteile.md](kleinteile.md) |
| Textlinks | `km-link`, `km-link--datei`, `km-link--extern`, `km-link--projekt` | `#textlinks` | [text.md](text.md) |
| Tabelle: Unterprojekte | `km-iconbtn`, `km-iconbtn--label`, `km-pill`, `km-pill--aktiv` | `#unterzeilen` | [tabelle.md](tabelle.md) |
| Werkzeugfarben | `km-dot` | `#werkzeugfarben` | [kleinteile.md](kleinteile.md) |
| Kennzahlen als Tabellen | `km-pill`, `km-pill--grade`, `km-pill--grade-a`, `km-pill--grade-b` | `#zahlenliste` | [tabelle.md](tabelle.md), [kennzahlen.md](kennzahlen.md) |
| Angabenliste | `km-deflist`, `km-pill`, `km-pill--ok` | `#angaben` | [listen.md](listen.md) |
| Kennzahlen im Raster | `km-fact`, `km-fact--danger`, `km-fact--ok`, `km-facts` | `#kacheln-raster` | [kennzahlen.md](kennzahlen.md) |
| Knopf mit Text | `km-button`, `km-toolbar` | `#knopf` | [knopf.md](knopf.md) |
| Auswahl mit Suche | `km-check`, `km-searchbox`, `km-selectpanel`, `km-selectpanel--open` | `#selectpanel` | [auswahl-mit-suche.md](auswahl-mit-suche.md) |
| Seitenleiste: eingeklappt, nur Icons | `km-sidebar`, `km-sidebar--rail`, `km-switch` | `#sidebar-rail` | [seitenleiste.md](seitenleiste.md) |
| Seitenleiste: Hierarchie wie im Inhalt | `km-sidebar`, `km-switch` | `#sidebar-hierarchie` | [seitenleiste.md](seitenleiste.md), [schalter.md](schalter.md) |
| Tabelle: einheitliche Regeln | `km-iconbtn`, `km-iconbtn--label`, `km-table`, `km-table-wrap` | `#tabelle-regeln` | [tabelle.md](tabelle.md) |
| Info-Karte | `km-card`, `km-card--accent-left`, `km-card--info`, `km-cards` | `#info-karte` | [karte.md](karte.md) |
| Antwort-Knöpfe | `km-answer`, `km-answer__opt--ok`, `--danger`, `--warn` | `#antwort` | [antwort.md](antwort.md) |
| Prüfkarte, Feld und Begriff | `km-criterion`, `km-field`, `km-term`, `km-answer` | `#pruefkarte` | [pruefkarte.md](pruefkarte.md), [antwort.md](antwort.md) |
| Score und Fortschritt | `km-score`, `km-progress`, `km-pill--grade-e` | `#score` | [score.md](score.md), [etikett.md](etikett.md) |
| Kopfzeile | `km-header`, `km-header__title`, `km-header__icon`, `km-header__actions` | `#kopfzeile` | [kopfzeile.md](kopfzeile.md), [seitenrahmen.md](seitenrahmen.md) |

## Bausteine im CSS ohne eigene Story

`km-toolbar` (nur als Hülle in anderen Stories, Doku [suchfeld.md](suchfeld.md)). Varianten eines Bausteins stehen immer in seiner einen Story, `km-segmented--wrap` also in `#segmented`.
