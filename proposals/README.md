# Proposals

Vorschläge für neue Bausteine oder Erweiterungen von KERN. Je Vorschlag eine HTML-Datei; die Komponentenbeschreibung zeigt sie unter „Proposals“ (`python3 tools/build-storybook.py`).

Erste Zeile ist der Kopf: `<!-- titel: … | status: Vorschlag | datum: JJJJ-MM-TT | bezug: … -->`. Danach eigenes CSS mit Präfix `kmp-` (Proposal, noch nicht im Kit), nur `--km-*`-Tokens, dann das Markup, bei Bedarf ein kleines Skript. Wird ein Vorschlag angenommen, wandert er nach `src/km-components.css` und `tools/bausteine.py` und die Datei bekommt `status: übernommen`.

Übernommen und nicht mehr unter „Proposals“ gezeigt (Story nur noch bei den Bausteinen, Datei bleibt als Historie):

- `segmented-control.html`: übernommen in Kit, siehe Story „Segmented Control“.
