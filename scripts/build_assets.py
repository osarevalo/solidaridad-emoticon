#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Genera los PNG de la familia «Solidaridad» a partir de los SVG maestros.

Uso:
    python scripts/build_assets.py            # todo
    python scripts/build_assets.py --only ink # una sola tinta

Requiere: cairosvg, pillow  (ver scripts/requirements.txt)
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import cairosvg
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
DIST = ROOT / "dist"

TINTS = {
    "ink": "#1F2933",
    "teal": "#2B7A78",
    "violet": "#8E44AD",
    "white": "#FFFFFF",
}

# Tamaños por glifo. Regla: B (silueta) para 16 y 20 px; A (trazo) desde 24 px.
SIZES = {
    "solidaridad": [24, 32, 48, 64, 128, 256, 512],
    "solidaridad-fill": [16, 20],
    "solidaridad-me-sumo": [24, 32, 48, 64, 128, 256, 512],
    "solidaridad-causa": [24, 32, 48, 64, 128, 256, 512],
}

# El sticker se exporta como pose final (sin SMIL) en PNG y WebP.
STICKER_SIZES = [128, 256, 512]


def strip_animation(svg: str) -> str:
    svg = re.sub(r"<animateTransform[^>]*/>", "", svg)
    svg = re.sub(r"\s+", " ", svg)
    return svg


def render_svg(svg: str, size: int, out: Path, tint: str) -> None:
    """Renderiza un SVG a PNG cuadrado de `size` px con fondo transparente."""
    data = svg.replace("currentColor", tint).replace("#CURRENTCOLOR", tint)
    out.parent.mkdir(parents=True, exist_ok=True)
    cairosvg.svg2png(
        bytestring=data.encode("utf-8"),
        write_to=str(out),
        output_width=size,
        output_height=size,
        background_color=None,
    )


def check_png(path: Path, size: int) -> None:
    im = Image.open(path)
    if im.size != (size, size):
        raise SystemExit(f"PNG fuera de tamaño: {path} -> {im.size}")
    if im.mode not in ("RGBA", "LA", "P"):
        raise SystemExit(f"PNG sin canal alfa: {path} -> {im.mode}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", choices=sorted(TINTS), help="exportar una sola tinta")
    args = ap.parse_args()
    tints = [args.only] if args.only else list(TINTS)

    generated = 0
    missing = 0
    for tint in tints:
        color = TINTS[tint]
        for glyph, sizes in SIZES.items():
            svg = (SRC / f"{glyph}.svg").read_text(encoding="utf-8")
            for size in sizes:
                out = DIST / "png" / tint / f"{glyph}_{size}.png"
                render_svg(svg, size, out, color)
                check_png(out, size)
                generated += 1

        # Sticker estático (pose final) por tinta
        sticker = strip_animation((SRC / "solidaridad-sticker.svg").read_text(encoding="utf-8"))
        for size in STICKER_SIZES:
            out = DIST / "sticker" / tint / f"solidaridad-sticker_{size}.png"
            render_svg(sticker, size, out, color)
            check_png(out, size)
            generated += 1

    # Verificar que los SVG fuente existen y que el set de tamaños cubre lo esperado
    for glyph in list(SIZES) + ["solidaridad-sticker"]:
        if not (SRC / f"{glyph}.svg").exists():
            print(f"FALTA: src/{glyph}.svg", file=sys.stderr)
            missing += 1
    if missing:
        return 1

    print(f"OK: {generated} PNG generados en {DIST}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
