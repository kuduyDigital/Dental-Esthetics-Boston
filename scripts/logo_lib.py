"""Shared helpers: outline text with HarfBuzz shaping + fontTools, and SVG wrappers."""
import io
from pathlib import Path

import uharfbuzz as hb
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

INK, PAPER, NAVY = "#121820", "#FAF9F6", "#1F3A56"


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
    tt, hbfont = font
    scale = size / tt["head"].unitsPerEm
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(hbfont, buf, {"kern": True, "liga": True})
    gs, order = tt.getGlyphSet(), tt.getGlyphOrder()
    pen = SVGPathPen(gs)
    cx = x
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        t = TransformPen(pen, (scale, 0, 0, -scale, cx + pos.x_offset * scale, baseline - pos.y_offset * scale))
        gs[order[info.codepoint]].draw(t)
        cx += pos.x_advance * scale + tracking
    return pen.getCommands(), cx - x - tracking


def width(font, text, size, tracking=0.0):
    return text_path(font, text, size, tracking=tracking)[1]


def text(font, s, size, color, x, baseline, tracking=0.0, anchor="start", opacity=None):
    w = width(font, s, size, tracking)
    if anchor == "middle":
        x -= w / 2
    d, _ = text_path(font, s, size, x=x, baseline=baseline, tracking=tracking)
    op = f' opacity="{opacity}"' if opacity is not None else ""
    return f'<path d="{d}" fill="{color}"{op}/>', w


def svg(w, h, body, title):
    title = title.replace("&", "&amp;")
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.2f} {h:.2f}" width="{w:.0f}" height="{h:.0f}" '
        f'role="img" aria-label="{title}"><title>{title}</title>{body}</svg>\n'
    )


def fonts(root: Path):
    f = root / "assets" / "fonts"
    return {
        "serif300": load(f / "newsreader-latin-wght-normal.woff2", 300),
        "serif400": load(f / "newsreader-latin-wght-normal.woff2", 400),
        "serif500": load(f / "newsreader-latin-wght-normal.woff2", 480),
        "italic": load(f / "newsreader-latin-wght-italic.woff2", 340),
        "sans600": load(f / "public-sans-latin-600-normal.woff2"),
        "sans400": load(f / "public-sans-latin-400-normal.woff2"),
    }
