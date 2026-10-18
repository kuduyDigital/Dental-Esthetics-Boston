"""Build the Dental Esthetics Boston "Twin Arch" logo set as outlined SVGs.

The symbol is a tooth drawn from two true semicircular arches (two specialists, one standard;
it keeps the practice's existing double-arch heritage), engraved with a finer inner line.

Usage:  python scripts/make_logo.py .
Needs:  pip install fonttools brotli uharfbuzz
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from logo_lib import INK, NAVY, PAPER, fonts, svg, text  # noqa: E402

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
OUT = ROOT / "assets" / "logo"
OUT.mkdir(parents=True, exist_ok=True)
F = fonts(ROOT)
TITLE = "Dental Esthetics Boston — Hirayama & Papaspyridakos"

# ---------------------------------------------------------------- symbol (64 x 64 grid)
TOOTH = (
    "M14 25 A9 9 0 0 1 32 25 A9 9 0 0 1 50 25 V31 C50 40.5 46.4 46.5 43.4 54.2 "
    "C42.6 56.3 39.6 56.3 39 54.1 L36 44.6 C35.4 42.6 33.9 41.4 32 41.4 "
    "C30.1 41.4 28.6 42.6 28 44.6 L25 54.1 C24.4 56.3 21.4 56.3 20.6 54.2 "
    "C17.6 46.5 14 40.5 14 31 Z"
)


# Inner line: a true 4-unit inset of the crown only (r9 arches -> r5), so it never touches the
# outer notch or the root fork. It is the practice's double arch, drawn inside the tooth.
INNER = "M18 33 V25 A5 5 0 0 1 28 25 C28 28 30.4 29.8 32 31.2 C33.6 29.8 36 28 36 25 A5 5 0 0 1 46 25 V33"


def symbol(color, sw=1.7, inner=True):
    out = f'<path d="{TOOTH}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linejoin="round"/>'
    if inner:
        out += (
            f'<path d="{INNER}" fill="none" stroke="{color}" stroke-width="{sw * 0.62:.2f}" '
            f'stroke-linecap="round" stroke-linejoin="round" opacity="0.6"/>'
        )
    return out


# ---------------------------------------------------------------- wordmark block
def wordmark(color, cx, top):
    """DENTAL ESTHETICS / ——— BOSTON ——— / Hirayama & Papaspyridakos, centred on cx."""
    size = 25
    p1, w1 = text(F["serif400"], "DENTAL ESTHETICS", size, color, cx, top + 22, size * 0.12, "middle")
    bsize = 8.2
    p2, bw = text(F["sans600"], "BOSTON", bsize, color, cx, top + 41, bsize * 0.62, "middle")
    gap, lx = 10, cx - w1 / 2
    rules = (
        f'<path d="M{lx:.2f} {top + 38} H{cx - bw / 2 - gap:.2f} M{cx + bw / 2 + gap:.2f} {top + 38} H{lx + w1:.2f}" '
        f'stroke="{color}" stroke-width="0.8" opacity="0.55"/>'
    )
    p3, _ = text(F["italic"], "Hirayama & Papaspyridakos", 11.5, color, cx, top + 62, 0.1, "middle", 0.72)
    return p1 + rules + p2 + p3, w1


W1 = text(F["serif400"], "DENTAL ESTHETICS", 25, INK, 0, 0, 25 * 0.12)[1]


def horizontal(color):
    x0 = 106
    words, w1 = wordmark(color, x0 + W1 / 2, 2)
    body = (
        f'<g transform="translate(0 -1) scale(1.06)">{symbol(color)}</g>'
        f'<path d="M86 6 V62" stroke="{color}" stroke-width="0.8" opacity="0.35"/>'
        + words
    )
    return x0 + w1 + 2, 68, body


def compact(color):
    """Header lockup: no subtitle line, larger BOSTON, so it stays legible at ~40px tall."""
    x0 = 92
    cx = x0 + W1 / 2
    p1, w1 = text(F["serif400"], "DENTAL ESTHETICS", 25, color, cx, 24, 25 * 0.12, "middle")
    bsize = 9.6
    p2, bw = text(F["sans600"], "BOSTON", bsize, color, cx, 46, bsize * 0.6, "middle")
    gap, lx = 10, cx - w1 / 2
    rules = (
        f'<path d="M{lx:.2f} {42.6} H{cx - bw / 2 - gap:.2f} M{cx + bw / 2 + gap:.2f} {42.6} H{lx + w1:.2f}" '
        f'stroke="{color}" stroke-width="0.9" opacity="0.55"/>'
    )
    body = (
        f'<g transform="translate(0 -6) scale(0.94)">{symbol(color)}</g>'
        f'<path d="M76 4 V48" stroke="{color}" stroke-width="0.8" opacity="0.35"/>' + p1 + rules + p2
    )
    return x0 + w1 + 2, 52, body


def stacked(color):
    w = W1 + 4
    s = 1.5
    words, _ = wordmark(color, w / 2, 64 * s + 6)
    body = f'<g transform="translate({(w - 64 * s) / 2:.2f} 0) scale({s})">{symbol(color)}</g>' + words
    return w, 64 * s + 72, body


files = {
    "mark.svg": svg(64, 64, symbol(INK), TITLE),
    "mark-light.svg": svg(64, 64, symbol(PAPER), TITLE),
    # solid navy tile, single line: survives 16px
    "favicon.svg": svg(
        64, 64,
        f'<rect width="64" height="64" rx="14" fill="{NAVY}"/>'
        f'<g transform="translate(5.5 3) scale(0.83)">{symbol(PAPER, 3, inner=False)}</g>',
        "Dental Esthetics Boston",
    ),
}
for name, fn in (("logo-horizontal", horizontal), ("logo-compact", compact), ("logo-stacked", stacked)):
    for suffix, color in (("", INK), ("-light", PAPER)):
        w, h, body = fn(color)
        files[f"{name}{suffix}.svg"] = svg(w, h, body, TITLE)

for fname, content in files.items():
    (OUT / fname).write_text(content, encoding="utf-8")
print("wrote", len(files), "SVGs to", OUT)
