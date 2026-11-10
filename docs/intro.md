# Kernmix

**Ein Remix von KERN.** Ein Design-System auf Basis des offenen Standards KERN, mit eigenem Klang.

## Die Idee

Ein Remix nimmt ein Original und macht daraus eine eigene Fassung. Das Original bleibt hörbar und wird genannt, der Remix setzt eigene Schwerpunkte. Kernmix macht das mit KERN: Der Standard von Bund und Ländern liefert die Grundspur aus Tokens, Rastern, Barrierefreiheit und Bausteinen. Kernmix legt darüber, was für Dashboards, Werkzeuge, Portfolios und größere, detaillierte Seiten fehlt, und mischt es so ab, dass alles zusammen klingt.

Am Mischpult laufen alle Kanäle in einen Mix. Jede Spur hat ihren Platz, nichts übersteuert, und am Ende klingt es wie ein Stück. So soll sich auch ein Design-System verhalten: viele Bausteine, ein Klang, egal auf welcher Seite.

## Warum ein Bassist so etwas baut

Wenn ich meine Rolle in Musikbegriffen beschreiben müsste: Ich bin der Bassist im Hintergrund. Ich halte den Rhythmus, sorge für Stabilität und überrasche gelegentlich mit einem Solo, immer mit Blick auf das Ganze und die Menschen, mit denen ich spiele.

Ein Design-System ist genau diese Rolle: Es gibt den Takt vor, damit alle anderen frei spielen können. Kernmix ist mein Bass für alle eigenen Projekte, von der Arbeitsoberfläche bis zum Musikblog Beyond Tape.

## Sechs Prinzipien

Die Prinzipien, nach denen ich gestalte, gelten auch für Kernmix. So zeigen sie sich im System:

1. **Design ist Kommunikation.** Jede Entscheidung ist erklärbar: Sie steht als ADR oder DDR mit Begründung und verworfenen Alternativen im System. Was sich nicht erklären lässt, ist nicht zu Ende gedacht.
2. **Nähe zum Code.** Der Code ist die Quelle. Bausteine entstehen im Kit, mit Story, Doku und Prüfung; Figma folgt, wo es gebraucht wird.
3. **Systeme vor Einzellösungen.** Neues entsteht zuerst als Baustein im Kit, dann auf der Seite. Eine Regel hat einen Bauweg, kein eigenes CSS je Projekt.
4. **Iteration über Perfektion.** Jede Version hat einen Release-Namen und einen Changelog. Varianten werden in Design-Runden nebeneinander gezeigt und entschieden, nicht am Schreibtisch.
5. **Barrierefreiheit als Standard.** Kontraste werden gerechnet, nicht geschätzt, in jedem Theme, hell und dunkel. Tastatur, Fokus und Screenreader gehören zu jedem Baustein, nicht in eine spätere Runde.
6. **Wirkung als Maßstab.** Ein Baustein ist gut, wenn Seiten damit besser werden, für Menschen und für Agenten. Prüfungen messen das; was nicht gemessen ist, gilt als offen.

## KERN-Updates laufen durch

- **Feste Version:** Das KERN-Kit liegt in fester Version in `vendor/kern/`, heute 2.8.2. Ein Update wird bewusst gezogen, nach Prüfung von Herkunft und Änderungen, nie automatisch.
- **Automatisch übernommen:** `tools/build.py` und `tools/einbetten.py` tragen geänderte KERN-Werte in alle km-Bausteine und in jede eingebettete Seite. Das geht, weil Bausteine nur Rollen lesen und die Rollen auf KERN-Semantik zeigen.
- **Brüche werden gemeldet:** Vor jedem Build prüft `tools/build.py`, ob jeder KERN-Token, den Kernmix liest oder ein Theme setzt, im Kit noch existiert. Umbenannte oder entfernte Tokens brechen den Build mit einer Liste ab, statt still auf einen Rückfallwert zu fallen.
- **Vorher und nachher gemessen:** Kontraste, Abstände, schmale Breite und Screenshots der Seiten werden vor und nach dem Update verglichen; Abweichungen stehen im Changelog.

## Wofür Kernmix da ist

- **Bauen mit Agenten:** Das Ziel ist eine Definition, die gut genug ist, dass Agenten und KI damit verlässlich Webseiten bauen. Dazu gehören Tokens in festen Ebenen, beschriebene Bausteine, begründete Entscheidungen (ADR und DDR), Seitenregeln als Prüfliste und Prüfungen, die Abweichungen melden.
- **Forschen und weiterentwickeln:** Erfahrungen aus der Arbeit an anderen Design-Systemen fließen hier ein und bleiben nachlesbar.
- **Nutzen:** Neue Projekte starten auf Kernmix. Hell und dunkel sind immer dabei; ein eigener Look entsteht als Theme, nicht als eigenes CSS.
- **Offen:** Kernmix soll als Open Source erscheinen.

## Was im Mix steckt

- **Die Grundspur:** das KERN-Kit, unverändert eingebunden. Für KERN-Bausteine gilt die Dokumentation von KERN.
- **Der Remix:** eigene Bausteine mit dem Präfix `km-`, Themes, Farbreihen und Tokens nach dem Schema von KERN.
- **Die Liner Notes:** Komponenten-Doku, Entscheidungen, Seitenregeln und Changelog. Jede Version hat einen Release-Namen.

## Kurz auf Englisch

Kernmix is ein Remix von KERN, the open design standard of the German federal and state governments. It keeps the original track intact and adds what dashboards, tools and detailed pages need: components with the `km-` prefix, themes, colour scales and tokens following KERN's scheme, plus documentation, decision records and checks good enough for AI agents to build pages that follow the rules. Like a bassist in a band, it keeps time so everything else can play freely.
