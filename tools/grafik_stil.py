"""Gemeinsamer Stil der Kernmix-Grafiken (animierte, klickbare Inline-SVGs): Klassen, Farben über Kit-Tokens, Bewegung nur ohne
prefers-reduced-motion, Lucide-Icons. Genutzt von tools/build-grafiken.py (Einführung) und von Seiten-Generatoren, die Grafiken im
selben Stil brauchen (Project Dashboard: tools/build-skills.py, Shortcuts). scope() macht die Stilregeln einer Grafik eindeutig,
damit sie inline in einer Seite nichts anderes treffen."""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LUC = {k: v['i'] for k, v in json.loads((ROOT / 'assets/lucide.json').read_text(encoding='utf-8')).items()}


def ic(name, x, y, size=24, cls='ic'):
    s = size / 24
    return f'<g class="{cls}" transform="translate({x} {y}) scale({s:.3f})">{LUC[name]}</g>'


STIL = '''
.f{fill:var(--km-color-card,#151d33);stroke:var(--km-color-border-section,#3d4a70);stroke-width:1.5;transition:stroke .2s,fill .2s}
.i{fill:var(--km-color-inset,#1b253e);stroke:var(--km-color-border-card,#2c3756);stroke-width:1.5}
.a{fill:var(--fb,var(--km-color-accent,#8fa6ff))}
.kante{fill:var(--fb,var(--km-color-accent,#8fa6ff))}
.l{stroke:var(--km-color-border-section,#3d4a70);stroke-width:2;fill:none}
.flow{stroke:var(--fb,var(--km-color-accent,#8fa6ff));stroke-width:2.5;fill:none;stroke-dasharray:7 9}
.h{fill:var(--km-color-text,#e8ecf8);font-size:22px;font-weight:700}
.t{fill:var(--km-color-text,#e8ecf8);font-size:17px;font-weight:600}
.m{fill:var(--km-color-text-muted,#b4bdd6);font-size:14px}
.k{fill:var(--km-color-text-dim,#8c96b3);font-size:12px;letter-spacing:.08em;font-weight:600}
.c{fill:var(--km-color-on-accent,#0c1120);font-size:15px;font-weight:700}
.ic{fill:none;stroke:var(--fb,var(--km-color-accent,#8fa6ff));stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.icon{fill:none;stroke:var(--km-color-on-accent,#0c1120);stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.lk{cursor:pointer;outline:none}
.lk:hover .f,.lk:focus-visible .f{stroke:var(--fb,var(--km-color-accent,#8fa6ff));fill:var(--km-color-inset,#1b253e)}
.lk:focus-visible .f{stroke-width:3}
.anim{animation-play-state:running}
.flowan{animation:kmfxflow 1.1s linear infinite}
.fader{animation:kmfxfader 5s ease-in-out infinite alternate;transform-box:fill-box}
.puls{animation:kmfxpuls 3.2s ease-in-out infinite}
.out{animation:kmfxout 4s ease-in-out infinite}
.ebene{animation:kmfxein .7s ease-out both}
.tropfen{animation:kmfxtropfen 2.8s linear infinite}
.schritt{animation:kmfxschritt 10s ease-in-out infinite}
.at{fill:var(--km-color-attention,#f59e0b)}
.ca{fill:var(--km-color-on-attention,#0e1324);font-size:15px;font-weight:700}
.ica{fill:none;stroke:var(--km-color-attention,#f59e0b);stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.iconat{fill:none;stroke:var(--km-color-on-attention,#0e1324);stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.lu{fill:none;stroke:var(--km-color-attention,#f59e0b);stroke-width:2;stroke-dasharray:6 6}
.luan{animation:kmfxflow 1.6s linear infinite}
.mono{font-family:var(--km-font-mono,monospace)}
.lk:hover .a,.lk:focus-visible .a,.lk:hover .at,.lk:focus-visible .at{stroke:var(--km-color-text,#e8ecf8);stroke-width:2}
@keyframes kmfxflow{to{stroke-dashoffset:-32}}
@keyframes kmfxfader{0%{transform:translateY(0)}100%{transform:translateY(var(--weg,40px))}}
@keyframes kmfxpuls{0%,100%{opacity:1}50%{opacity:.82}}
@keyframes kmfxout{0%,100%{stroke:var(--km-color-border-section,#3d4a70)}12%,30%{stroke:var(--fb,var(--km-color-accent,#8fa6ff))}}
@keyframes kmfxein{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}
@keyframes kmfxtropfen{from{transform:translateY(0);opacity:0}10%{opacity:1}90%{opacity:1}to{transform:translateY(330px);opacity:0}}
@keyframes kmfxschritt{0%,100%{stroke:var(--km-color-border-section,#3d4a70);stroke-width:1.5}8%,18%{stroke:var(--fb,var(--km-color-accent,#8fa6ff));stroke-width:3}}
@media (prefers-reduced-motion: reduce){.flowan,.fader,.puls,.out,.ebene,.tropfen,.schritt,.luan{animation:none}}
'''


def scope(svg_text, prefix):
    """Inline-SVG für eine Seite: id am <svg>, Titel-IDs eindeutig, jede Stilregel (auch in Listen und in @media) auf #prefix beschränkt."""
    s = svg_text.replace('id="t"', f'id="{prefix}-t"').replace('id="d"', f'id="{prefix}-d"').replace('aria-labelledby="t d"', f'aria-labelledby="{prefix}-t {prefix}-d"')
    s = s.replace('<svg ', f'<svg id="{prefix}" ', 1)
    def regeln(css):
        out = []
        for m in re.finditer(r'(@media[^{]+)\{((?:[^{}]*\{[^}]*\})*)\s*\}|(@keyframes[^{]+\{(?:[^{}]*\{[^}]*\})*\s*\})|([^{}@]+)\{([^}]*)\}', css):
            if m.group(1): out.append(m.group(1) + '{' + regeln(m.group(2)) + '}')
            elif m.group(3): out.append(m.group(3).strip())
            else: out.append(','.join(f'#{prefix} {x.strip()}' for x in m.group(4).split(',') if x.strip()) + '{' + m.group(5) + '}')
        return ''.join(out)
    return re.sub(r'<style>(.*?)</style>', lambda m: '<style>' + regeln(m.group(1)) + '</style>', s, flags=re.S)


# Hochformat-Fassung (0.13.0): gleiche Inhalte senkrecht, 250 Einheiten breit, damit die kleinste Schrift (12) bei 390 px Fenster
# mindestens 12 px gerendert wird (schmalste gemessene Fläche: 250 px im Dashboard). Die Seite zeigt sie über km-figure__tall.
HOCH_B = 250


def zeilen(text, n):
    """Text an Wortgrenzen auf Zeilen zu höchstens n Zeichen verteilen (für Texte in der Hochformat-Fassung)."""
    out = []
    for w in text.split():
        if out and len(out[-1]) + 1 + len(w) <= n: out[-1] += ' ' + w
        else: out.append(w)
    return out


def text_zeilen(cls, x, y, text, n, abstand=18, extra=''):
    """Mehrzeiliger SVG-Text: (Markup, y der letzten Zeile)."""
    zs = zeilen(text, n)
    return ''.join(f'<text class="{cls}" x="{x}" y="{y + k * abstand}"{extra}>{z}</text>' for k, z in enumerate(zs)), y + (len(zs) - 1) * abstand
