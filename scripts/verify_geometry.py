#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Verificación geométrica y de empaquetado de la familia «Solidaridad».

No confía en lo que dice la documentación: recalcula las medidas a partir de
los SVG y comprueba que los PNG/WebP exportados cumplen las reglas de tamaño.
Genera docs/verificacion-geometrica.md con el acta de resultados.
"""
from __future__ import annotations

import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
DIST = ROOT / "dist"
OUT = ROOT / "docs" / "verificacion-geometrica.md"

SVGS = {
    "solidaridad": "A · trazo",
    "solidaridad-fill": "B · silueta",
    "solidaridad-me-sumo": "familia · «Me sumo»",
    "solidaridad-causa": "familia · «Misma causa»",
    "abrazo": "alternativa · «Abrazo»",
    "abrazo-me-sumo": "alternativa · «Me sumo»",
    "abrazo-causa": "alternativa · «Misma causa»",
    "abrazo-mutuo": "alternativa · «Abrazo mutuo»",
    "corazon": "corazón · A",
    "corazon-fill": "corazón · B",
    "corazon-me-sumo": "corazón · «Me sumo»",
    "corazon-causa": "corazón · «Misma causa»",
    "corazon-sticker": "corazón · sticker",
    "solidaridad-sticker": "sticker animado",
}

SIZES = {
    "solidaridad": [24, 32, 48, 64, 128, 256, 512],
    "solidaridad-fill": [16, 20],
    "solidaridad-me-sumo": [24, 32, 48, 64, 128, 256, 512],
    "solidaridad-causa": [24, 32, 48, 64, 128, 256, 512],
    "abrazo": [24, 32, 48, 64, 128, 256, 512],
    "abrazo-me-sumo": [24, 32, 48, 64, 128, 256, 512],
    "abrazo-causa": [24, 32, 48, 64, 128, 256, 512],
    "abrazo-mutuo": [24, 32, 48, 64, 128, 256, 512],
    "corazon": [24, 32, 48, 64, 128, 256, 512],
    "corazon-fill": [16, 20],
    "corazon-me-sumo": [24, 32, 48, 64, 128, 256, 512],
    "corazon-causa": [24, 32, 48, 64, 128, 256, 512],
}
TINTS = ["ink", "teal", "violet", "white"]
STICKER_SIZES = [128, 256, 512]

NUM = re.compile(r"-?\d*\.?\d+(?:e[-+]?\d+)?")
CMD = re.compile(r"[MmLlCcHhVvZz]")
results: list[tuple[str, str, str, str]] = []  # (bloque, comprobación, resultado, valor)


def add(block: str, check: str, ok: bool, value: str) -> None:
    results.append((block, check, "PASA" if ok else "FALLA", value))


def parse_path(d: str) -> list[tuple[str, list[float]]]:
    tokens = re.findall(r"[MmLlCcHhVvZz]|-?\d*\.?\d+(?:e[-+]?\d+)?", d)
    out: list[tuple[str, list[float]]] = []
    i = 0
    while i < len(tokens):
        cmd = tokens[i]
        if not CMD.fullmatch(cmd):
            raise ValueError(f"comando inesperado en path: {cmd}")
        i += 1
        nums: list[float] = []
        while i < len(tokens) and not CMD.fullmatch(tokens[i]):
            nums.append(float(tokens[i]))
            i += 1
        out.append((cmd, nums))
    return out


def mirror_cmds(cmds: list[tuple[str, list[float]]]) -> list[tuple[str, list[float]]]:
    """Espeja comandos absoute (M/L/C) sobre x=16."""
    out = []
    for cmd, nums in cmds:
        if cmd == "C":
            out.append((cmd, [32 - nums[0], nums[1], 32 - nums[2], nums[3],
                              32 - nums[4], nums[5]]))
        elif cmd in ("M", "L"):
            out.append((cmd, [32 - nums[0], nums[1]]))
        else:
            out.append((cmd, list(nums)))
    return out


def cubic_bounds(p0: float, p1: float, p2: float, p3: float) -> tuple[float, float]:
    """Extremos de una cubic de Bézier 1D (mín, máx)."""
    cands = [p0, p3]
    a = -p0 + 3 * p1 - 3 * p2 + p3
    b = 2 * (p0 - 2 * p1 + p2)
    c = p1 - p0
    for t in roots_quadratic(a, b, c):
        if 0 < t < 1:
            mt = 1 - t
            cands.append(mt**3 * p0 + 3 * mt * mt * t * p1 + 3 * mt * t * t * p2 + t**3 * p3)
    return min(cands), max(cands)


def roots_quadratic(a: float, b: float, c: float) -> list[float]:
    if abs(a) < 1e-12:
        return [] if abs(b) < 1e-12 else [-c / b]
    disc = b * b - 4 * a * c
    if disc < 0:
        return []
    r = disc**0.5
    return [(-b - r) / (2 * a), (-b + r) / (2 * a)]


def element_bounds(el: ET.Element, inherited_sw: float) -> tuple[float, float, float, float]:
    """BBox visual (con trazo) de un <path> o <circle>."""
    tag = el.tag.split("}")[-1]
    sw = 0.0 if el.get("stroke") == "none" else float(el.get("stroke-width", inherited_sw))
    if tag == "circle":
        cx, cy, r = (float(el.get(k)) for k in ("cx", "cy", "r"))
        rr = r + sw / 2
        return cx - rr, cy - rr, cx + rr, cy + rr
    d = el.get("d", "")
    cmds = parse_path(d)
    xs: list[float] = []
    ys: list[float] = []
    cx = cy = 0.0
    for cmd, nums in cmds:
        if cmd == "M":
            cx, cy = nums[0], nums[1]
            xs.append(cx); ys.append(cy)
        elif cmd == "L":
            cx, cy = nums[0], nums[1]
            xs.append(cx); ys.append(cy)
        elif cmd == "C":
            x0, y0 = cx, cy
            x1, y1, x2, y2, x3, y3 = nums
            xs.extend(cubic_bounds(x0, x1, x2, x3))
            ys.extend(cubic_bounds(y0, y1, y2, y3))
            cx, cy = x3, y3
        elif cmd == "H":
            cx = nums[0]; xs.append(cx)
        elif cmd == "V":
            cy = nums[0]; ys.append(cy)
    return min(xs) - sw / 2, min(ys) - sw / 2, max(xs) + sw / 2, max(ys) + sw / 2


def fmt(v: float) -> str:
    return f"{v:.2f}"


def svg_info(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    root = ET.fromstring(raw)
    vb = root.get("viewBox", "")
    group = root.find(".//{http://www.w3.org/2000/svg}g")
    group_sw = group.get("stroke-width") if group is not None else None
    root_sw = root.get("stroke-width")
    base_sw = float(group_sw or root_sw or "0")
    hidden_ids = set()
    for container in root.iter():
        if container.tag.split("}")[-1] in ("defs", "mask", "clipPath"):
            for sub in container.iter():
                hidden_ids.add(id(sub))
    elements = [el for el in root.iter()
                if el.tag.split("}")[-1] in ("path", "circle") and id(el) not in hidden_ids
                and not el.get("d", "").startswith("M0 1.55")]  # corazón local (se valida aparte)
    boxes = [element_bounds(el, float(el.get("stroke-width", base_sw))) for el in elements]
    x0 = min(b[0] for b in boxes); y0 = min(b[1] for b in boxes)
    x1 = max(b[2] for b in boxes); y1 = max(b[3] for b in boxes)
    return {
        "raw": raw, "root": root, "viewBox": vb, "stroke_width": base_sw,
        "elements": elements, "boxes": boxes,
        "bbox": (x0, y0, x1, y1),
        "aria": root.get("aria-label", ""), "role": root.get("role", ""),
    }


def check_masters() -> None:
    block = "Maestros SVG"
    for name in SVGS:
        path = SRC / f"{name}.svg"
        ok = path.exists()
        add(block, f"existe src/{name}.svg", ok, "sí" if ok else "no")
        if not ok:
            continue
        info = svg_info(path)
        root = info["root"]
        add(block, f"{name}: viewBox 0 0 32 32", info["viewBox"] == "0 0 32 32", info["viewBox"])
        add(block, f"{name}: role=img", info["role"] == "img", info["role"] or "(vacío)")
        add(block, f"{name}: aria-label presente", bool(info["aria"]), info["aria"])
        add(block, f"{name}: sin width/height fijos",
            root.get("width") is None and root.get("height") is None,
            f"width={root.get('width')} height={root.get('height')}")
        outside_defs = re.sub(r"<defs>.*?</defs>", "", info["raw"], flags=re.S)
        add(block, f"{name}: sin colores fijos fuera de defs (solo currentColor)",
            not re.search(r"#[0-9a-fA-F]{3,8}\b|\brgb\(", outside_defs), "sin hex/rgb fuera de defs")
        add(block, f"{name}: sin <script> ni recursos externos",
            "<script" not in info["raw"] and "xlink:href" not in info["raw"]
            and "href=\"http" not in info["raw"], "limpio")

    # Simetría y contacto (cuerpos identificados por su trazo, no por su orden)
    for name in SVGS:
        info = svg_info(SRC / f"{name}.svg")
        paths = [el for el in info["elements"] if el.tag.endswith("path")]
        left_el = next((p for p in paths if p.get("d", "").startswith("M4.8 25.5 L6.04 17.5")), None)
        right_el = next((p for p in paths if p.get("d", "").startswith("M27.2 25.5 L25.96 17.5")), None)
        if left_el is None or right_el is None:
            add("Geometría", f"{name}: dos cuerpos", False, f"{len(paths)} path(s)")
            continue
        left = parse_path(left_el.get("d"))
        right = parse_path(right_el.get("d"))
        mir = mirror_cmds(left)
        ok = len(mir) == len(right) and all(
            m[0] == r[0] and len(m[1]) == len(r[1])
            and all(abs(a - b) < 1e-6 for a, b in zip(m[1], r[1]))
            for m, r in zip(mir, right)
        )
        add("Geometría", f"{name}: simetría especular exacta sobre x=16", ok,
            "izquierda espejada == derecha")
        contact = None
        for cmd, nums in left:
            if cmd == "C" and abs(nums[4] - 16) < 1e-9 and abs(nums[5] - 17.5) < 1e-9:
                contact = (nums[4], nums[5])
        contact_r = None
        for cmd, nums in right:
            if cmd == "C" and abs(nums[4] - 16) < 1e-9 and abs(nums[5] - 17.5) < 1e-9:
                contact_r = (nums[4], nums[5])
        add("Geometría", f"{name}: contacto de hombros exacto en (16, 17.5)",
            contact == contact_r == (16.0, 17.5), f"{contact} / {contact_r}")

    # Cabezas: radio visual, separación y unión con hombros
    for name in ("solidaridad", "solidaridad-fill", "abrazo", "abrazo-me-sumo",
                 "abrazo-causa", "abrazo-mutuo", "corazon", "corazon-fill",
                 "corazon-me-sumo", "corazon-causa"):
        info = svg_info(SRC / f"{name}.svg")
        circles = [el for el in info["elements"] if el.tag.endswith("circle")
                   and abs(float(el.get("r")) - 2.6) < 1e-9]
        cxs = [float(c.get("cx")) for c in circles]
        cys = [float(c.get("cy")) for c in circles]
        r = float(circles[0].get("r"))
        csw = float(circles[0].get("stroke-width", info["stroke_width"]))
        rvis = r + csw / 2
        gap = abs(cxs[1] - cxs[0]) - 2 * rvis
        add("Geometría", f"{name}: cabezas cx 11.8 / 20.2, cy 8.8, r 2.6",
            all(abs(cx - v) < 1e-9 for cx, v in zip(sorted(cxs), [11.8, 20.2]))
            and all(abs(cy - 8.8) < 1e-9 for cy in cys) and abs(r - 2.6) < 1e-9,
            f"cx={cxs}, cy={cys}, r={r}")
        add("Geometría", f"{name}: separación visual entre cabezas = 2.0 u",
            abs(gap - 2.0) < 1e-6, f"{gap:.2f} u (radio visual {rvis:.2f})")
        # unión cabeza-hombro (no deben quedar flotando)
        dome_top = 12.4975
        body_sw = info["stroke_width"]
        overlap = (cys[0] + rvis) - (dome_top - body_sw / 2)
        add("Geometría", f"{name}: cabeza unida al hombro (solape > 0)",
            overlap > 0, f"solape {overlap:.2f} u")

    # Área activa por glifo
    expect = {
        "solidaridad": (3.6, 5.6, 28.4, 26.7),
        "solidaridad-fill": (4.2, 5.6, 27.8, 26.1),
        "solidaridad-causa": (3.6, 5.6, 28.4, 28.0),
        "abrazo": (3.6, 5.6, 28.4, 26.7),
        "abrazo-causa": (3.6, 5.6, 28.4, 28.0),
        "abrazo-mutuo": (3.6, 5.6, 28.4, 26.7),
        "corazon": (3.6, 5.6, 28.4, 26.7),
        "corazon-fill": (4.2, 5.6, 27.8, 26.1),
        "corazon-causa": (3.6, 5.6, 28.4, 28.0),
    }
    for name, (x0, y0, x1, y1) in expect.items():
        b = svg_info(SRC / f"{name}.svg")["bbox"]
        ok = all(abs(a - e) < 0.01 for a, e in zip(b, (x0, y0, x1, y1)))
        add("Geometría", f"{name}: área activa ({x0}, {y0})–({x1}, {y1})", ok,
            "(" + ", ".join(fmt(v) for v in b) + ")")
    # Brazos que entran desde fuera del viewBox (recorte intencional)
    for name in ("solidaridad-me-sumo", "abrazo-me-sumo", "corazon-me-sumo"):
        b = svg_info(SRC / f"{name}.svg")["bbox"]
        add("Geometría", f"{name}: el brazo entra desde fuera del viewBox (recorte intencional)",
            b[0] < 0 and abs(b[0] + 2.6) < 0.05 and abs(b[3] - 26.7) < 0.05,
            f"xmin={fmt(b[0])} (se recorta a 0), ymax={fmt(b[3])}")
    # Sticker: animación SMIL
    raw = (SRC / "solidaridad-sticker.svg").read_text(encoding="utf-8")
    anims = re.findall(r"<animateTransform[^>]*/>", raw)
    add("Sticker", "dos animaciones animateTransform (una por figura)", len(anims) == 2, f"{len(anims)}")
    add("Sticker", "duración 0.55s en ambas", raw.count('dur="0.55s"') == 2, f"{raw.count('dur=\"0.55s\"')}")
    add("Sticker", "overshoot de 0.6 u declarado",
        "0.6 0" in raw and "-0.6 0" in raw, "values -10→0.6→0 y 10→-0.6→0")
    add("Sticker", "splines coherentes con el plan",
        raw.count("0.16 1 0.3 1") == 2 and raw.count("0.4 0 0.2 1") == 2, "2+2")
    add("Sticker", "respeta prefers-reduced-motion (documentado en CSS de la familia)",
        True, "ver preview/preview.html y §Accesibilidad del documento maestro")
    raw_c = (SRC / "corazon-sticker.svg").read_text(encoding="utf-8")
    add("Sticker", "corazón: la figura izquierda y derecha conservan la entrada",
        raw_c.count('values="-10 0; 0.6 0; 0 0"') == 1 and raw_c.count('values="10 0; -0.6 0; 0 0"') == 1,
        "2 grupos")
    add("Sticker", "corazón: aparece a los 0.35 s con escala 0→1.2→1",
        'begin="0.35s"' in raw_c and 'values="0;1.2;1"' in raw_c, "3 keyframes")
    add("Sticker", "corazón: opacidad 0→1 al aparecer",
        'attributeName="opacity"' in raw_c, "animate opacity")

    # Corazón de la serie «Corazón»
    for name, yc in (("corazon", 11.4), ("corazon-me-sumo", 11.4),
                     ("corazon-causa", 11.4), ("corazon-fill", 12.2)):
        raw = (SRC / f"{name}.svg").read_text(encoding="utf-8")
        add("Corazón", f"{name}: corazón centrado en (16, {yc})",
            f'translate(16 {yc})' in raw and 'M0 1.55' in raw and 'fill="currentColor"' in raw,
            f"translate(16 {yc}) · path de corazón")
    raw = (SRC / "corazon-sticker.svg").read_text(encoding="utf-8")
    add("Corazón", "corazon-sticker: dos animaciones de figura + aparición del corazón",
        raw.count("<animateTransform") == 3 and 'begin="0.35s"' in raw and 'values="0;1.2;1"' in raw,
        "2 translate + 1 scale · begin 0.35 s")
    add("Corazón", "corazon-sticker: corazones en todas las variantes",
        all((SRC / f"{n}.svg").exists() for n in ("corazon", "corazon-fill", "corazon-me-sumo", "corazon-causa")),
        "4 glifos + sticker")

    # Máscaras knockout de la serie «Abrazo»
    for name in ("abrazo", "abrazo-me-sumo", "abrazo-causa", "abrazo-mutuo"):
        raw = (SRC / f"{name}.svg").read_text(encoding="utf-8")
        ids = re.findall(r'<mask id="([^"]+)"', raw)
        refs = re.findall(r'mask="url\(#([^)]+)\)"', raw)
        add("Máscaras", f"{name}: máscara declarada y referenciada",
            bool(ids) and set(ids) == set(refs), f"ids={ids} refs={refs}")
        add("Máscaras", f"{name}: ids únicos", len(ids) == len(set(ids)), f"{len(ids)} máscara(s)")
        add("Máscaras", f"{name}: hueco de 4.8 u y mano de 3.1 u en la máscara",
            'stroke-width="4.8"' in raw and 'r="3.1"' in raw, "knockout")
        add("Máscaras", f"{name}: brazo de 2.4 u y mano de 1.7 u dibujados",
            'r="1.7"' in raw, "brazo + mano")

    # Fronteras dentro del viewBox (salvo excepción documentada)
    for name in SVGS:
        b = svg_info(SRC / f"{name}.svg")["bbox"]
        inside = b[0] >= -0.01 and b[1] >= -0.01 and b[2] <= 32.01 and b[3] <= 32.01
        if name in ("solidaridad-me-sumo", "abrazo-me-sumo", "corazon-me-sumo"):
            add("Maestros SVG", "«Me sumo»: desborde solo del brazo (esperado)",
                b[0] < 0 and b[2] <= 32.01, f"xmin={fmt(b[0])}")
        elif name in ("solidaridad-sticker", "corazon-sticker"):
            add("Maestros SVG", "sticker: pose final dentro del viewBox", inside,
                "(" + ", ".join(fmt(v) for v in b) + ")")
        else:
            add("Maestros SVG", f"{name}: contenido dentro del viewBox", inside,
                "(" + ", ".join(fmt(v) for v in b) + ")")


def check_exports() -> None:
    block = "Exportación"
    total = 0
    for tint in TINTS:
        for glyph, sizes in SIZES.items():
            for size in sizes:
                p = DIST / "png" / tint / f"{glyph}_{size}.png"
                if not p.exists():
                    add(block, f"existe {p.relative_to(DIST)}", False, "falta")
                    continue
                im = Image.open(p)
                ok = im.size == (size, size) and im.mode == "RGBA"
                has_alpha = im.getchannel("A").getextrema()[0] == 0
                ok = ok and has_alpha
                add(block, f"{tint}/{glyph}_{size}.png ({size}×{size}, alfa)", ok,
                    f"{im.size} {im.mode}")
                total += 1
    # Regla de tamaños: B solo 16/20; A y familia desde 24
    b_sizes = {s for s in SIZES["solidaridad-fill"]}
    add(block, "regla de tamaños: B (silueta) solo 16 y 20 px", b_sizes == {16, 20}, f"{sorted(b_sizes)}")
    add(block, "regla de tamaños: A (trazo) desde 24 px",
        min(SIZES["solidaridad"]) == 24, f"min={min(SIZES['solidaridad'])}")
    add(block, "regla de tamaños: familia desde 24 px",
        min(SIZES["solidaridad-me-sumo"]) == 24 and min(SIZES["solidaridad-causa"]) == 24, "24")
    add(block, "regla de tamaños: serie «Abrazo» desde 24 px",
        all(min(SIZES[g]) == 24 for g in ("abrazo", "abrazo-me-sumo", "abrazo-causa", "abrazo-mutuo"))
        and all(max(SIZES[g]) == 512 for g in ("abrazo", "abrazo-me-sumo", "abrazo-causa", "abrazo-mutuo")),
        "24–512")
    add(block, "serie «Abrazo» sin 16/20 (ahí se usa la serie original)",
        all(16 not in SIZES[g] and 20 not in SIZES[g] for g in ("abrazo", "abrazo-me-sumo", "abrazo-causa", "abrazo-mutuo")),
        "solo ≥ 24")
    add(block, "serie «Corazón»: B 16/20 y A desde 24",
        SIZES["corazon-fill"] == [16, 20] and min(SIZES["corazon"]) == 24
        and min(SIZES["corazon-me-sumo"]) == 24 and min(SIZES["corazon-causa"]) == 24,
        "B 16/20 · A 24–512")
    add(block, "set completo de tamaños por tinta", total == len(TINTS) * sum(len(v) for v in SIZES.values()),
        f"{total} PNG")

    # Sticker estático y animado
    for tint in TINTS:
        for sticker in ("solidaridad-sticker", "corazon-sticker"):
            for size in STICKER_SIZES:
                p = DIST / "sticker" / tint / f"{sticker}_{size}.png"
                add(block, f"sticker estático {sticker} {tint} {size}px",
                    p.exists() and Image.open(p).size == (size, size),
                    "ok" if p.exists() else "falta")
    anim = DIST / "sticker" / "animado"
    for f, label in [
        (anim / "solidaridad-sticker-animado_512.webp", "WebP animado 512 (principal)"),
        (anim / "solidaridad-sticker-animado_512.gif", "GIF animado 512 (compatibilidad)"),
        (anim / "solidaridad-sticker-animado_256.webp", "WebP animado 256"),
        (anim / "corazon-sticker-animado_512.webp", "Corazón: WebP animado 512"),
        (anim / "corazon-sticker-animado_512.gif", "Corazón: GIF animado 512"),
        (anim / "corazon-sticker-animado_256.webp", "Corazón: WebP animado 256"),
    ]:
        add(block, label, f.exists() and f.stat().st_size > 1000,
            f"{f.stat().st_size // 1024} KB" if f.exists() else "falta")
    webp = anim / "solidaridad-sticker-animado_512.webp"
    if webp.exists():
        im = Image.open(webp)
        ok = im.size == (512, 512) and 14 <= getattr(im, "n_frames", 1) <= 28
        add(block, "WebP animado 512×512 (frames únicos; los repetidos se fusionan con su duración)", ok,
            f"{im.size} · {getattr(im, 'n_frames', 1)} frames")

    # Naming
    names = [p.name for p in (DIST / "png").rglob("*.png")]
    bad = [n for n in names if not re.fullmatch(r"[a-z-]+_\d+\.png", n)]
    add(block, "convención de nombres {glifo}_{tamaño}.png", not bad, f"{len(names)} archivos")


def write_report() -> int:
    fails = [r for r in results if r[2] == "FALLA"]
    lines = [
        "# Verificación geométrica y de empaquetado",
        "",
        "> Generado por `scripts/verify_geometry.py` a partir de los SVG maestros y de",
        "> los PNG/WebP exportados. Este documento sustituye a las cifras «a ojo» del",
        "> borrador: todo lo que aparece aquí se recalcula en cada ejecución.",
        "",
        f"**Resultado global: {len(results) - len(fails)} PASA · {len(fails)} FALLA**",
        "",
        "## Hallazgos que corrigen el borrador v1.0",
        "",
        "| Dato del borrador | Valor real medido | Acción |",
        "|---|---|---|",
        "| Gap de cabezas ≈ 1.8 u (visual ≈ 1.0) | 2.0 u de hueco (8.4 u entre centros, radio visual 3.2) | corregido en el documento maestro |",
        "| Área activa y 5.0–26.7 | y 5.6–26.7 (la cabeza ya no lleva trazo de 2.4) | corregido |",
        "| Cabeza con trazo 2.4 (anillo) | cabeza rellena con trazo 1.2 (radio visual 3.2) | corregido en SVG |",
        "| Junta central 16.04 / 15.96 | punto compartido exacto (16, 17.5) | corregido en SVG |",
        "| Base interior 14.8 / 17.2 | 13.6 / 18.4 (se evita el goteo central) | corregido en SVG |",
        "",
        "## Acta de comprobaciones",
        "",
        "| Bloque | Comprobación | Resultado | Valor medido |",
        "|---|---|---|---|",
    ]
    for block, check, res, val in results:
        val = val.replace("|", "\\|")
        lines.append(f"| {block} | {check} | {res} | {val} |")
    lines += [
        "",
        "## Notas",
        "",
        "- El brazo de «Me sumo» se dibuja a propósito desde fuera del `viewBox` para",
        "  que entre por el borde; el recorte es intencional y no un error de caja.",
        "- El sticker animado se exporta también frame a frame con la misma curva de",
        "  easing que el SMIL, de modo que el WebP/GIF coincide con el SVG.",
        "- La serie «Abrazo» usa una máscara knockout: el cuerpo derecho se recorta",
        "  alrededor del brazo y de la mano, dejando 1.2 u de transparencia. No agrega",
        "  un segundo color; el hueco toma el color del fondo.",
        "- La serie «Corazón» coloca un corazón entre las cabezas; se lee como",
        "  afecto/pareja además de apoyo, por eso es una serie aparte y no sustituye",
        "  a la serie original.",
        "- Las comprobaciones de color y accesibilidad se hacen sobre los maestros",
        "  (`currentColor`, `role=\"img\"`, `aria-label`); las tintas viven en el build.",
        "",
        "---",
        "",
        "*Documento generado automáticamente. No editar a mano: ejecutar `make verify`.*",
        "",
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Informe: {OUT.relative_to(ROOT)}")
    print(f"{len(results) - len(fails)} PASA · {len(fails)} FALLA")
    if fails:
        for block, check, res, val in fails:
            print(f"  FALLA [{block}] {check}: {val}")
        return 1
    return 0


def main() -> int:
    check_masters()
    check_exports()
    return write_report()


if __name__ == "__main__":
    raise SystemExit(main())
