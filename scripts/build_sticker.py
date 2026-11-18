#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Genera los stickers animados de «Solidaridad» y «Corazón».

Reproduce en Python la animación SMIL del maestro (translate + spline) para
poder exportar frame a frame: WebP animado (formato recomendado, con alfa) y
GIF (compatibilidad). También exporta WebP estático a partir de los PNG.

Salidas en dist/sticker/animado/ y WebP estáticos junto a los PNG.
"""
from __future__ import annotations

import re
import shutil
import subprocess
import tempfile
from pathlib import Path

import cairosvg
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
DIST = ROOT / "dist"

TINT = "#1F2933"
FPS = 25
FRAME_MS = 1000 // FPS
DUR = 0.55          # duración total de la animación (s), coincide con el SMIL
KEY = 0.75 * DUR    # 0.4125 s: fin del primer tramo
HOLD_OFF = 3        # frames quieto fuera de cuadro
HOLD_END = 10       # frames quieto en la pose final
SIZES = [256, 512]
HEART_BEGIN = 0.35
HEART_DUR = 0.4

TPL = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" fill="none"
     role="img" aria-label="Me solidarizo con vos">
  <g stroke="{tint}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">
    <g transform="translate({lx:.4f} 0)">{left}</g>
    <g transform="translate({rx:.4f} 0)">{right}</g>
  </g>
</svg>
"""


def bezier_y_at_x(x1: float, y1: float, x2: float, y2: float, x: float) -> float:
    """Devuelve y de una cubic-bezier(x1,y1,x2,y2) para un x dado (0..1)."""
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    lo, hi = 0.0, 1.0
    for _ in range(60):
        t = (lo + hi) / 2
        mt = 1 - t
        bx = 3 * mt * mt * t * x1 + 3 * mt * t * t * x2 + t * t * t
        if bx < x:
            lo = t
        else:
            hi = t
    t = (lo + hi) / 2
    mt = 1 - t
    return 3 * mt * mt * t * y1 + 3 * mt * t * t * y2 + t * t * t


def translate_at(t: float) -> float:
    """Desplazamiento horizontal (unidades del viewBox) del grupo izquierdo."""
    if t <= KEY:
        u = t / KEY
        e = bezier_y_at_x(0.16, 1, 0.3, 1, u)
        return -10.0 + 10.6 * e
    u = min(1.0, (t - KEY) / (DUR - KEY))
    e = bezier_y_at_x(0.4, 0, 0.2, 1, u)
    return 0.6 - 0.6 * e


def extract_figures(sticker: str = "solidaridad-sticker") -> tuple[str, str]:
    """Extrae los dos bloques (path + circle) del maestro del sticker."""
    svg = (SRC / f"{sticker}.svg").read_text(encoding="utf-8")
    paths = re.findall(r"<path d=\"([^\"]+)\"/>", svg)
    circles = re.findall(r"<circle [^>]+/>", svg)
    if len(paths) < 2 or len(circles) != 2:
        raise SystemExit(f"el maestro {sticker} no tiene 2 figuras")
    left = f'<path d="{paths[0]}"/>{circles[0]}'.replace("currentColor", TINT)
    right = f'<path d="{paths[1]}"/>{circles[1]}'.replace("currentColor", TINT)
    return left, right


def extract_corazon() -> tuple[str, str, str]:
    """Extrae figuras y corazón del sticker con corazón."""
    svg = (SRC / "corazon-sticker.svg").read_text(encoding="utf-8")
    paths = re.findall(r'<path d="([^"]+)"[^>]*/>', svg)
    circles = re.findall(r"<circle [^>]+/>", svg)
    if len(paths) != 3 or len(circles) != 2:
        raise SystemExit("el maestro corazon-sticker no tiene 2 figuras + corazón")
    left = f'<path d="{paths[0]}"/>{circles[0]}'.replace("currentColor", TINT)
    right = f'<path d="{paths[1]}"/>{circles[1]}'.replace("currentColor", TINT)
    return left, right, paths[2]


def heart_state(t: float) -> tuple[float, float]:
    """Escala y opacidad del corazón en el tiempo t (s)."""
    if t < HEART_BEGIN:
        return 0.0, 0.0
    u = min(1.0, (t - HEART_BEGIN) / HEART_DUR)
    if u <= 0.75:
        e = bezier_y_at_x(0.16, 1, 0.3, 1, u / 0.75)
        scale = 1.2 * e
    else:
        e = bezier_y_at_x(0.4, 0, 0.2, 1, (u - 0.75) / 0.25)
        scale = 1.2 + (1.0 - 1.2) * e
    return scale, min(1.0, u / 0.2)


CORAZON_TPL = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" fill="none"
     role="img" aria-label="Solidaridad con corazón">
  <g stroke="{tint}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">
    <g transform="translate({lx:.4f} 0)">{left}</g>
    <g transform="translate({rx:.4f} 0)">{right}</g>
  </g>
  <g transform="translate(16 11.4) scale({hs:.4f})">
    <path d="{heart}" fill="{tint}" opacity="{op:.3f}"/>
  </g>
</svg>
"""


def frame_svg(left: str, right: str, t: float) -> str:
    tx = translate_at(t)
    return TPL.format(tint=TINT, lx=tx, rx=-tx, left=left, right=right)


def frame_corazon_svg(left: str, right: str, heart: str, t: float) -> str:
    tx = translate_at(t)
    hs, op = heart_state(t)
    return CORAZON_TPL.format(tint=TINT, lx=tx, rx=-tx, left=left, right=right,
                              heart=heart, hs=hs, op=op)


def render_frames(size: int, outdir: Path) -> list[Path]:
    left, right = extract_figures()
    times: list[float] = [0.0] * HOLD_OFF
    times += [min(DUR, i / FPS) for i in range(0, int(round(DUR * FPS)) + 1)]
    times += [DUR] * HOLD_END
    frames: list[Path] = []
    for i, t in enumerate(times):
        svg = frame_svg(left, right, t)
        out = outdir / f"frame-{size}-{i:03d}.png"
        cairosvg.svg2png(
            bytestring=svg.encode("utf-8"),
            write_to=str(out),
            output_width=size,
            output_height=size,
            background_color=None,
        )
        frames.append(out)
    return frames


def render_corazon_frames(size: int, outdir: Path) -> list[Path]:
    left, right, heart = extract_corazon()
    times: list[float] = [0.0] * HOLD_OFF
    times += [min(DUR, i / FPS) for i in range(0, int(round(DUR * FPS)) + 1)]
    times += [DUR] * HOLD_END
    frames: list[Path] = []
    for i, t in enumerate(times):
        svg = frame_corazon_svg(left, right, heart, t)
        out = outdir / f"frame-cor-{size}-{i:03d}.png"
        cairosvg.svg2png(
            bytestring=svg.encode("utf-8"),
            write_to=str(out),
            output_width=size,
            output_height=size,
            background_color=None,
        )
        frames.append(out)
    return frames


def encode_webp_anim(frames: list[Path], out: Path) -> None:
    if shutil.which("ffmpeg") is None:
        print("aviso: ffmpeg no disponible, se omite WebP animado")
        return
    stem = frames[0].name.rsplit("-", 1)[0]  # frame-<size>
    pat = str(frames[0].parent / f"{stem}-%03d.png")
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-framerate", str(FPS),
        "-i", pat,
        "-c:v", "libwebp_anim",
        "-lossless", "1",
        "-pix_fmt", "yuva420p",
        "-loop", "0",
        str(out),
    ]
    subprocess.run(cmd, check=True)


def encode_gif(frames: list[Path], out: Path) -> None:
    imgs = [Image.open(f).convert("RGBA") for f in frames]
    pal_frames = []
    for im in imgs:
        alpha = im.getchannel("A").point(lambda a: 255 if a >= 128 else 0)
        p = im.convert("RGB").convert("P", palette=Image.Palette.ADAPTIVE, colors=255)
        p.paste(255, mask=alpha.point(lambda a: 255 if a == 0 else 0))
        p.info["transparency"] = 255
        pal_frames.append(p)
    pal_frames[0].save(
        out,
        save_all=True,
        append_images=pal_frames[1:],
        duration=FRAME_MS,
        loop=0,
        transparency=255,
        disposal=2,
        optimize=True,
    )


def static_webp() -> int:
    count = 0
    for png in sorted((DIST / "sticker").rglob("*-sticker_*.png")):
        out = png.with_suffix(".webp")
        Image.open(png).save(out, format="WEBP", lossless=True, quality=100)
        count += 1
    return count


def main() -> int:
    anim = DIST / "sticker" / "animado"
    anim.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        tmpdir = Path(tmp)
        for sticker, renderer in (
            ("solidaridad", render_frames),
            ("corazon", render_corazon_frames),
        ):
            for size in SIZES:
                frames = renderer(size, tmpdir)
                webp = anim / f"{sticker}-sticker-animado_{size}.webp"
                encode_webp_anim(frames, webp)
                if size == 512:
                    encode_gif(frames, anim / f"{sticker}-sticker-animado_512.gif")
                print(f"OK animado {sticker} {size}px: {webp.name} ({len(frames)} frames)")
    n = static_webp()
    print(f"OK: {n} WebP estáticos")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
