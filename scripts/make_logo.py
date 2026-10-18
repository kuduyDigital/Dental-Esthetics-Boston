"""Build the Dental Esthetics Boston logo set as outlined SVGs (no font dependency)."""
import io
import sys
from pathlib import Path

import uharfbuzz as hb
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

ROOT = Path(sys.argv[1])
FONTS = ROOT / "assets" / "fonts"
OUT = ROOT / "assets" / "logo"
OUT.mkdir(parents=True, exist_ok=True)

INK, PAPER = "#121820", "#FAF9F6"


def load(path, wght=None):
    f = TTFont(path)
    if wght is not None and "fvar" in f:
        f = instancer.instantiateVariableFont(f, {"wght": wght})
    f.flavor = None
    buf = io.BytesIO()
    f.save(buf)
    data = buf.getvalue()
    return TTFont(io.BytesIO(data)), hb.Font(hb.Face(data))


def text_path(font, text, size, x=0.0, baseline=0.0, tracking=0.0):
    """Return (svg path d, advance width) for text shaped with HarfBuzz (kerning included)."""
    tt, hbfont = font
    upem = tt["head"].unitsPerEm
    scale = size / upem
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(hbfont, buf, {"kern": True, "liga": True})
    glyphset = tt.getGlyphSet()
    order = tt.getGlyphOrder()
    pen = SVGPathPen(glyphset)
    cx = x
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        name = order[info.codepoint]
        t = TransformPen(pen, (scale, 0, 0, -scale, cx + pos.x_offset * scale, baseline - pos.y_offset * scale))
        glyphset[name].draw(t)
        cx += pos.x_advance * scale + tracking
    return pen.getCommands(), cx - x - tracking


def width(font, text, size, tracking=0.0):
    return text_path(font, text, size, tracking=tracking)[1]


serif = load(FONTS / "newsreader-latin-wght-normal.woff2", 300)
serif_mono = load(FONTS / "newsreader-latin-wght-normal.woff2", 340)
sans = load(FONTS / "public-sans-latin-600-normal.woff2")

# --- The mark: a double-ring seal (the two rings nod to the practice's current double-arch logo)
# around a light italic serif "DE" monogram.
MW = MH = 56
STROKE = 1.3
italic = load(FONTS / "newsreader-latin-wght-italic.woff2", 330)


def monogram(color, cx, baseline, size):
    track = -size * 0.02
    w = width(italic, "DE", size, tracking=track)
    d, _ = text_path(italic, "DE", size, x=cx - w / 2 - size * 0.02, baseline=baseline, tracking=track)
    return f'<path d="{d}" fill="{color}"/>'


def mark_group(color, ox=0.0, oy=0.0, s=1.0):
    c = MW / 2
    return (
        f'<g transform="translate({ox} {oy}) scale({s})">'
        f'<circle cx="{c}" cy="{c}" r="{c - 1}" fill="none" stroke="{color}" stroke-width="{STROKE}"/>'
        f'<circle cx="{c}" cy="{c}" r="{c - 4.5}" fill="none" stroke="{color}" stroke-width="{STROKE * 0.5}" opacity="0.5"/>'
        + monogram(color, c, c + 7.2, 21)
        + "</g>"
    )


def favicon_group(bg, fg, size):
    c = size / 2
    return f'<circle cx="{c}" cy="{c}" r="{c}" fill="{bg}"/>' + monogram(fg, c, c + size * 0.15, size * 0.5)


def svg(w, h, body, title, bg=None):
    title = title.replace("&", "&amp;")  # SVG files are XML
    rect = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.2f} {h:.2f}" '
        f'width="{w:.0f}" height="{h:.0f}" role="img" aria-label="{title}">'
        f"<title>{title}</title>{rect}{body}</svg>\n"
    )


NAME = "Dental Esthetics Boston"
SUB = "HIRAYAMA & PAPASPYRIDAKOS"
TITLE = "Dental Esthetics Boston — Hirayama & Papaspyridakos"


def horizontal(color):
    name_size, sub_size = 30, 7.6
    name_w = width(serif, NAME, name_size, tracking=-0.2)
    sub_track = sub_size * 0.26
    sub_w = width(sans, SUB, sub_size, tracking=sub_track)
    gap = 18
    x0 = MW + gap
    d_name, _ = text_path(serif, NAME, name_size, x=x0, baseline=34, tracking=-0.2)
    d_sub, _ = text_path(sans, SUB, sub_size, x=x0 + 1, baseline=52, tracking=sub_track)
    rule = f'<path d="M{x0 + 1} 42.5 H{x0 + 34}" stroke="{color}" stroke-width="0.8" opacity="0.6"/>'
    w = x0 + max(name_w, sub_w) + 2
    body = mark_group(color) + f'<path d="{d_name}" fill="{color}"/>' + rule + f'<path d="{d_sub}" fill="{color}" opacity="0.72"/>'
    return w, MH, body


def stacked(color):
    name_size, sub_size = 30, 7.6
    name_w = width(serif, NAME, name_size, tracking=-0.2)
    sub_track = sub_size * 0.26
    sub_w = width(sans, SUB, sub_size, tracking=sub_track)
    w = max(name_w, sub_w) + 4
    mark_s = 1.25
    mx = (w - MW * mark_s) / 2
    d_name, _ = text_path(serif, NAME, name_size, x=(w - name_w) / 2, baseline=MH * mark_s + 34, tracking=-0.2)
    d_sub, _ = text_path(sans, SUB, sub_size, x=(w - sub_w) / 2, baseline=MH * mark_s + 52, tracking=sub_track)
    h = MH * mark_s + 58
    body = mark_group(color, mx, 0, mark_s) + f'<path d="{d_name}" fill="{color}"/>' + f'<path d="{d_sub}" fill="{color}" opacity="0.72"/>'
    return w, h, body


files = {}
files["mark.svg"] = svg(MW, MH, mark_group(INK), TITLE)
files["mark-light.svg"] = svg(MW, MH, mark_group(PAPER), TITLE)
for name, fn in (("logo-horizontal", horizontal), ("logo-stacked", stacked)):
    w, h, body = fn(INK)
    files[f"{name}.svg"] = svg(w, h, body, TITLE)
    w, h, body = fn(PAPER)
    files[f"{name}-light.svg"] = svg(w, h, body, TITLE)

# favicon: solid seal so the monogram survives 16px
files["favicon.svg"] = svg(64, 64, favicon_group("#1F3A56", PAPER, 64), "Dental Esthetics Boston")

for fname, content in files.items():
    (OUT / fname).write_text(content, encoding="utf-8")
    print(fname, len(content))
