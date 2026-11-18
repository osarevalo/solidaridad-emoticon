#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Genera la hoja de contactos (PNG) y la vista previa autocontenida (HTML)."""
from __future__ import annotations

import datetime as dt
import io
import re
from pathlib import Path

import cairosvg
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
OUT = ROOT / "preview"

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

GLYPHS = [
    ("solidaridad", "A · trazo", "solidaridad.svg", "24–512 px"),
    ("solidaridad-fill", "B · silueta", "solidaridad-fill.svg", "16 y 20 px"),
    ("solidaridad-me-sumo", "«Me sumo»", "solidaridad-me-sumo.svg", "≥ 24 px"),
    ("solidaridad-causa", "«Misma causa»", "solidaridad-causa.svg", "≥ 24 px"),
    ("solidaridad-sticker", "Sticker", "solidaridad-sticker.svg", "animado · 512"),
]

ABRAZO_GLYPHS = [
    ("abrazo", "Abrazo", "abrazo.svg", "brazo por encima del hombro · ≥ 24 px"),
    ("abrazo-me-sumo", "Abrazo · «me sumo»", "abrazo-me-sumo.svg", "alguien más se acerca · ≥ 24 px"),
    ("abrazo-causa", "Abrazo · «misma causa»", "abrazo-causa.svg", "misma base / misma causa · ≥ 24 px"),
    ("abrazo-mutuo", "Abrazo mutuo", "abrazo-mutuo.svg", "los dos brazos por encima · ≥ 24 px"),
]

INK = "#1F2933"
TEAL = "#2B7A78"
VIOLET = "#8E44AD"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_B if bold else FONT, size)


def render(name: str, size: int, tint: str) -> Image.Image:
    svg = (SRC / f"{name}.svg").read_text(encoding="utf-8").replace("currentColor", tint)
    png = cairosvg.svg2png(bytestring=svg.encode("utf-8"), output_width=size, output_height=size)
    return Image.open(io.BytesIO(png)).convert("RGBA")


def paste_center(canvas: Image.Image, im: Image.Image, cx: int, cy: int) -> None:
    canvas.alpha_composite(im, (int(cx - im.width / 2), int(cy - im.height / 2)))


def rounded(draw: ImageDraw.ImageDraw, box, radius: int, fill: str, outline: str | None = None, width: int = 1) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def checks_count() -> int:
    report = ROOT / "docs" / "verificacion-geometrica.md"
    if report.exists():
        m = re.search(r"Resultado global:\s*(\d+)\s*PASA", report.read_text(encoding="utf-8"))
        if m:
            return int(m.group(1))
    return 0


def contact_sheet() -> Path:
    W, H = 1920, 1332
    sheet = Image.new("RGBA", (W, H), "#FFFFFF")
    d = ImageDraw.Draw(sheet)

    d.text((80, 54), "Solidaridad", font=font(56, True), fill=INK)
    d.text((80, 124), "Paquete de emoticones · apoyo y solidaridad", font=font(26), fill="#475467")
    meta = "v1.2.0 · 9 glifos · 16–512 px · monocromo"
    d.text((W - 80 - d.textlength(meta, font=font(20)), 84), meta, font=font(20), fill="#667085")
    d.line((80, 186, W - 80, 186), fill="#E4E7EC", width=2)

    # --- fila 1: los cinco glifos -------------------------------------------------
    cards = [(80 + i * 360, 210, 80 + i * 360 + 340, 620) for i in range(5)]
    for (x0, y0, x1, y1), (name, label, filename, sizes) in zip(cards, GLYPHS):
        rounded(d, (x0, y0, x1, y1), 18, "#FFFFFF", "#E4E7EC", 2)
        im = render(name, 250, INK)
        paste_center(sheet, im, (x0 + x1) // 2, y0 + 138)
        d.text((x0 + 24, y0 + 292), label, font=font(23, True), fill=INK)
        d.text((x0 + 24, y0 + 326), filename, font=font(16), fill="#667085")
        d.text((x0 + 24, y0 + 354), sizes, font=font(15), fill="#98A2B3")

    # --- fila 2: escalera de tamaños ---------------------------------------------
    d.text((80, 668), "Escalera de tamaños", font=font(30, True), fill=INK)
    d.text((80, 710), "Los PNG se exportan a tamaño exacto; el SVG escala sin pérdida.", font=font(18), fill="#667085")
    ladder = [
        ("solidaridad", 256, "A"), ("solidaridad", 128, "A"), ("solidaridad", 96, "A"),
        ("solidaridad", 64, "A"), ("solidaridad", 48, "A"), ("solidaridad", 32, "A"),
        ("solidaridad", 24, "A"), ("solidaridad-fill", 20, "B"), ("solidaridad-fill", 16, "B"),
    ]
    x = 120
    baseline = 1005
    group_pos: dict[str, int] = {}
    for name, size, letter in ladder:
        group_pos.setdefault(letter, x)
        im = render(name, size, INK)
        sheet.alpha_composite(im, (x, baseline - size))
        label = f"{size}"
        d.text((x + size / 2 - d.textlength(label, font=font(15)) / 2, baseline + 12), label,
               font=font(15), fill="#667085")
        d.text((x + size / 2 - 5, baseline + 34), letter, font=font(12), fill="#98A2B3")
        x += max(size, 70) + 40
    d.text((group_pos["A"], baseline + 56), "A · trazo (≥ 24 px)", font=font(14), fill="#667085")
    d.text((group_pos["B"], baseline + 56), "B · silueta (16–20 px)", font=font(14), fill="#667085")

    # --- fila 3: tintas ----------------------------------------------------------
    rounded(d, (80, 1110, W - 80, 1232), 18, INK)
    d.text((112, 1134), "Tintas", font=font(22, True), fill="#FFFFFF")
    rounded(d, (230, 1124, 760, 1220), 12, "#FFFFFF")
    tints = [("ink", INK, "#1F2933"), ("teal", TEAL, "#2B7A78"),
             ("violet", VIOLET, "#8E44AD"), ("white", "#FFFFFF", "#FFFFFF")]
    tx = 252
    for _, color, hexv in tints:
        rounded(d, (tx, 1136, tx + 56, 1192), 10, color, "#D0D5DD", 1)
        d.text((tx, 1198), hexv, font=font(13), fill="#475467")
        tx += 126
    im = render("solidaridad", 92, "#FFFFFF")
    sheet.alpha_composite(im, (820, 1124))
    d.text((930, 1138), "Una tinta por uso.", font=font(19, True), fill="#FFFFFF")
    d.text((930, 1170), "currentColor en los maestros;\nlas tintas viven en el build.", font=font(17),
           fill="#D0D5DD", spacing=6)

    # --- pie ---------------------------------------------------------------------
    today = dt.date.today().isoformat()
    checks = checks_count()
    foot1 = f"Verificación geométrica: {checks} comprobaciones · 0 fallas  ·  docs/verificacion-geometrica.md"
    foot2 = f"Arte CC BY 4.0 · Código MIT  ·  github.com/osarevalo/solidaridad-emoticon  ·  {today}"
    foot3 = "Serie alternativa «Abrazo»: preview/contact-sheet-abrazo.png  ·  solo ≥ 24 px"
    d.text((80, 1250), foot1, font=font(16), fill="#98A2B3")
    d.text((80, 1276), foot2, font=font(16), fill="#98A2B3")
    d.text((80, 1302), foot3, font=font(15), fill="#98A2B3")

    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "contact-sheet.png"
    sheet.convert("RGB").save(path, optimize=True)
    return path


def abrazo_contact_sheet() -> Path:
    W, H = 1920, 1190
    sheet = Image.new("RGBA", (W, H), "#FFFFFF")
    d = ImageDraw.Draw(sheet)
    d.text((80, 54), "Serie alternativa · Abrazo", font=font(52, True), fill=INK)
    d.text((80, 122), "Brazo por encima del hombro, con la mano visible al otro lado", font=font(25), fill="#475467")
    meta = "v1.2.0 · 4 glifos · 24–512 px · una sola tinta"
    d.text((W - 80 - d.textlength(meta, font=font(19)), 84), meta, font=font(19), fill="#667085")
    d.line((80, 184, W - 80, 184), fill="#E4E7EC", width=2)
    cards = [(80 + i * 460, 210, 80 + i * 460 + 420, 610) for i in range(4)]
    for (x0, y0, x1, y1), (name, label, filename, sizes) in zip(cards, ABRAZO_GLYPHS):
        rounded(d, (x0, y0, x1, y1), 18, "#FFFFFF", "#E4E7EC", 2)
        im = render(name, 260, INK)
        paste_center(sheet, im, (x0 + x1) // 2, y0 + 138)
        d.text((x0 + 24, y0 + 292), label, font=font(23, True), fill=INK)
        d.text((x0 + 24, y0 + 326), filename, font=font(16), fill="#667085")
        d.text((x0 + 24, y0 + 354), sizes, font=font(14), fill="#98A2B3")
    d.text((80, 660), "Escala del glifo principal", font=font(30, True), fill=INK)
    d.text((80, 700), "El brazo y la mano se sostienen desde 24 px; a 16/20 se usa la serie original.", font=font(18), fill="#667085")
    x = 120; baseline = 980
    for size in (256, 128, 96, 64, 48, 32, 24):
        im = render("abrazo", size, INK)
        sheet.alpha_composite(im, (x, baseline - size))
        d.text((x + size / 2 - 14, baseline + 12), f"{size}", font=font(15), fill="#667085")
        x += size + 42
    rounded(d, (80, 1020, W - 80, 1130), 18, INK)
    d.text((112, 1042), "Tinta blanca / oscuro", font=font(20, True), fill="#FFFFFF")
    sheet.alpha_composite(render("abrazo", 80, "#FFFFFF"), (370, 1032))
    sheet.alpha_composite(render("abrazo-me-sumo", 80, "#FFFFFF"), (490, 1032))
    d.text((620, 1040), "La separación del brazo es una máscara knockout: el hueco toma el color del fondo.", font=font(17), fill="#D0D5DD")
    d.text((620, 1068), "No hay un segundo color en el SVG: el hueco es transparencia.", font=font(17), fill="#D0D5DD")
    checks = checks_count()
    d.text((80, 1152), f"Verificación: {checks} comprobaciones · 0 fallas  ·  docs/verificacion-geometrica.md", font=font(15), fill="#98A2B3")
    d.text((80, 1174), "Arte CC BY 4.0 · Código MIT  ·  github.com/osarevalo/solidaridad-emoticon", font=font(15), fill="#98A2B3")
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "contact-sheet-abrazo.png"
    sheet.convert("RGB").save(path, optimize=True)
    return path


def html() -> Path:
    def svg(name: str, size: int, css: str = "") -> str:
        raw = (SRC / f"{name}.svg").read_text(encoding="utf-8").strip()
        raw = raw.replace("<svg ", f'<svg style="width:{size}px;height:{size}px;{css}" ', 1)
        return raw

    checks = checks_count()
    abrazo_cards = ""
    for name, label, filename, sizes in ABRAZO_GLYPHS:
        abrazo_cards += f"""
        <article class="card">
          <div class="glyph">{svg(name, 128)}</div>
          <h3>{label}</h3>
          <code>{filename}</code>
          <p class="muted">{sizes}</p>
        </article>"""

    glyph_cards = ""
    for name, label, filename, sizes in GLYPHS:
        glyph_cards += f"""
        <article class="card">
          <div class="glyph">{svg(name, 128)}</div>
          <h3>{label}</h3>
          <code>{filename}</code>
          <p class="muted">{sizes}</p>
        </article>"""

    ladder_rows = "".join(
        f'<figure class="step"><div>{svg("solidaridad", s)}</div><figcaption>{s} px</figcaption></figure>'
        for s in (128, 64, 48, 32, 24)
    )
    ladder_b = "".join(
        f'<figure class="step"><div>{svg("solidaridad-fill", s)}</div><figcaption>{s} px</figcaption></figure>'
        for s in (20, 16)
    )
    tints = "".join(
        f'<figure class="tint" style="color:{c}">{svg("solidaridad", 84)}<figcaption>{hexv}</figcaption></figure>'
        for c, hexv in [(INK, "#1F2933"), (TEAL, "#2B7A78"), (VIOLET, "#8E44AD")]
    )
    sticker = svg("solidaridad-sticker", 256)

    doc = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Solidaridad · paquete de emoticones</title>
<style>
  :root {{
    --ink: #1F2933; --muted: #667085; --line: #E4E7EC;
    --bg: #FAFAF8; --card: #FFFFFF; --teal: #2B7A78;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0; background: var(--bg); color: var(--ink);
    font: 16px/1.55 system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  }}
  .wrap {{ max-width: 1080px; margin: 0 auto; padding: 48px 24px 72px; }}
  header h1 {{ font-size: clamp(34px, 5vw, 56px); margin: 0 0 6px; letter-spacing: -.02em; }}
  header p.lead {{ font-size: 20px; color: var(--muted); margin: 0 0 18px; }}
  .chips {{ display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 8px; }}
  .chip {{
    border: 1px solid var(--line); background: #fff; border-radius: 999px;
    padding: 4px 12px; font-size: 13px; color: var(--muted);
  }}
  section {{ margin-top: 56px; }}
  h2 {{ font-size: 26px; margin: 0 0 6px; letter-spacing: -.01em; }}
  .sub {{ color: var(--muted); margin: 0 0 22px; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 16px; }}
  .card {{
    background: var(--card); border: 1px solid var(--line); border-radius: 16px;
    padding: 22px 20px 18px; text-align: center;
  }}
  .card .glyph {{ color: var(--ink); display: flex; justify-content: center; min-height: 132px; align-items: center; }}
  .card h3 {{ font-size: 16px; margin: 12px 0 2px; }}
  .card code {{ font-size: 12.5px; color: var(--teal); }}
  .muted {{ color: var(--muted); }}
  .card p {{ margin: 4px 0 0; font-size: 13px; }}
  .ladder {{ display: inline-flex; flex-wrap: wrap; align-items: flex-end; gap: 26px; background: #fff;
             border: 1px solid var(--line); border-radius: 16px; padding: 28px; }}
  .step {{ margin: 0; text-align: center; color: var(--ink); }}
  .step > div {{ display: flex; align-items: flex-end; justify-content: center; }}
  .step figcaption {{ font-size: 12px; color: var(--muted); margin-top: 8px; }}
  .rule {{ display: flex; gap: 36px; flex-wrap: wrap; margin-top: 14px; }}
  .rule .box {{ flex: 1 1 300px; background: #fff; border: 1px solid var(--line); border-radius: 16px; padding: 20px 22px; }}
  .rule h3 {{ margin: 0 0 10px; font-size: 17px; }}
  .rule ul {{ margin: 0; padding-left: 20px; }}
  .rule li {{ margin: 4px 0; }}
  .tints {{ display: flex; gap: 18px; flex-wrap: wrap; }}
  .tint {{ margin: 0; background: #fff; border: 1px solid var(--line); border-radius: 14px;
           padding: 18px 22px 12px; text-align: center; }}
  .tint figcaption {{ font-size: 12.5px; color: var(--muted); margin-top: 6px; }}
  .dark {{ background: var(--ink); border-radius: 16px; padding: 26px 30px; color: #fff; }}
  .dark .tint {{ background: transparent; border-color: #344054; }}
  .dark .tint figcaption {{ color: #D0D5DD; }}
  .sticker {{ background: #fff; border: 1px solid var(--line); border-radius: 16px;
              padding: 30px; display: flex; gap: 34px; align-items: center; flex-wrap: wrap; }}
  .sticker .note {{ max-width: 420px; color: var(--muted); font-size: 14.5px; }}
  .sticker .note strong {{ color: var(--ink); }}
  table {{ width: 100%; border-collapse: collapse; background: #fff; border: 1px solid var(--line);
           border-radius: 12px; overflow: hidden; font-size: 14.5px; }}
  th, td {{ text-align: left; padding: 10px 14px; border-bottom: 1px solid var(--line); }}
  th {{ background: #F9FAFB; font-size: 12.5px; text-transform: uppercase; letter-spacing: .04em; color: var(--muted); }}
  tr:last-child td {{ border-bottom: 0; }}
  code, pre {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }}
  pre {{ background: var(--ink); color: #E4E7EC; border-radius: 12px; padding: 16px 18px; overflow: auto; font-size: 13px; }}
  footer {{ margin-top: 64px; padding-top: 20px; border-top: 1px solid var(--line);
            color: var(--muted); font-size: 13.5px; }}
  footer a {{ color: var(--teal); }}
  .ok {{ color: var(--teal); font-weight: 600; }}
</style>
</head>
<body>
<div class="wrap">
  <header>
    <h1>Solidaridad</h1>
    <p class="lead">«Me solidarizo con vos» · apoyo y solidaridad, sin caridad desde arriba.</p>
    <div class="chips">
      <span class="chip">9 glifos</span><span class="chip">SVG maestro 32 × 32</span>
      <span class="chip">PNG 16–512 px</span><span class="chip">monocromo · currentColor</span>
      <span class="chip">sticker animado</span><span class="chip">serie Abrazo</span><span class="chip">{checks} comprobaciones · 0 fallas</span>
      <span class="chip">arte CC BY 4.0</span><span class="chip">código MIT</span>
    </div>
  </header>

  <section>
    <h2>Los cinco glifos</h2>
    <p class="sub">Dos figuras idénticas que se inclinan hasta tocarse los hombros. Las cabezas no se tocan.</p>
    <div class="grid">{glyph_cards}
    </div>
  </section>

  <section>
    <h2>Escala</h2>
    <p class="sub">B (silueta) para 16 y 20 px; A (trazo) desde 24 px. Los tamaños pequeños se muestran a tamaño real.</p>
    <div class="ladder">
      {ladder_rows}
      <div style="width:2px;align-self:stretch;background:var(--line)"></div>
      {ladder_b}
    </div>
  </section>

  <section>
    <h2>Tintas</h2>
    <p class="sub">Un solo color por uso. Los maestros usan <code>currentColor</code>; las tintas se aplican en el build o por CSS.</p>
    <div class="tints">{tints}</div>
    <div class="dark" style="margin-top:18px">
      <div class="tints">
        <figure class="tint" style="color:#FFFFFF">{svg("solidaridad", 84)}<figcaption>#FFFFFF · fondos oscuros</figcaption></figure>
        <figure class="tint" style="color:#FFFFFF">{svg("solidaridad-me-sumo", 84)}<figcaption>Familia · «Me sumo»</figcaption></figure>
      </div>
    </div>
  </section>

  <section>
    <h2>Serie alternativa · Abrazo</h2>
    <p class="sub">Brazo por encima del hombro, con la mano al otro lado. Una máscara knockout separa el brazo del cuerpo sin usar un segundo color. Solo desde 24 px: a 16/20 se usa la serie original.</p>
    <div class="grid">{abrazo_cards}
    </div>
    <p class="sub" style="margin-top:14px">Hoja de contactos de la serie: <a href="contact-sheet-abrazo.png">contact-sheet-abrazo.png</a>.</p>
  </section>

  <section>
    <h2>Sticker animado</h2>
    <p class="sub">Las figuras entran desde los bordes, chocan los hombros con un overshoot de 0.6 u y se asientan en 550 ms.</p>
    <div class="sticker">
      <div style="color:var(--ink)">{sticker}</div>
      <div class="note">
        <p><strong>Animación SMIL</strong> en el SVG maestro. En navegadores se reproduce sola.</p>
        <p>Exportado también como <strong>WebP animado</strong> (recomendado, conserva alfa) y <strong>GIF</strong> (compatibilidad), más PNG/WebP estático de 512 px para WhatsApp/Telegram.</p>
        <p>El equivalente CSS respeta <code>prefers-reduced-motion</code>.</p>
      </div>
    </div>
  </section>

  <section>
    <h2>Geometría verificada</h2>
    <p class="sub">Recalculada por <code>scripts/verify_geometry.py</code>; el acta completa está en <code>docs/verificacion-geometrica.md</code>.</p>
    <table>
      <tr><th>Parámetro</th><th>Valor</th></tr>
      <tr><td>Canvas / viewBox</td><td>32 × 32 · <code>0 0 32 32</code></td></tr>
      <tr><td>Contacto de hombros</td><td>(16.0, 17.5) exacto, compartido por las dos figuras</td></tr>
      <tr><td>Cabezas</td><td>r 2.6 · cy 8.8 · cx 11.8 / 20.2 · radio visual 3.2</td></tr>
      <tr><td>Hueco entre cabezas</td><td>2.0 u (sin tocarse)</td></tr>
      <tr><td>Trazo A / B</td><td>2.4 round · B relleno + 1.2</td></tr>
      <tr><td>Base interior</td><td>13.6 / 18.4 (los cuerpos se separan bajo el hombro)</td></tr>
      <tr><td>Área activa A</td><td>x 3.6–28.4 · y 5.6–26.7</td></tr>
      <tr><td>Simetría</td><td>espejo exacto sobre x = 16</td></tr>
    </table>
  </section>

  <section>
    <h2>Reglas</h2>
    <div class="rule">
      <div class="box">
        <h3>Hacer</h3>
        <ul>
          <li>Mantener las dos figuras al mismo nivel y tamaño.</li>
          <li>Usar una sola tinta; el significado no depende del color.</li>
          <li>Usar A ≥ 24 px y B en 16/20 px.</li>
          <li>Conservar <code>role="img"</code> + <code>aria-label</code>.</li>
          <li>Respetar <code>prefers-reduced-motion</code> en el sticker.</li>
        </ul>
      </div>
      <div class="box">
        <h3>No hacer</h3>
        <ul>
          <li>Corazón sobre o entre las cabezas (lee «pareja»).</li>
          <li>Figuras de distinta altura o tamaño (lee caridad).</li>
          <li>Manos que dan o sostienen desde arriba.</li>
          <li>Bicolor contrastante (lee «dos bandos»).</li>
          <li>Degradados o sombras (ruido a 16 px).</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <h2>Uso rápido</h2>
<pre>&lt;svg class="icono" role="img" aria-label="Me solidarizo con vos"&gt;
  ... contenido de src/solidaridad.svg ...
&lt;/svg&gt;

.icono {{ width: 24px; height: 24px; color: #1F2933; }}</pre>
    <p class="sub">Para PNG: <code>dist/png/ink/solidaridad_32.png</code>. Para fondo oscuro: <code>dist/png/white/</code>.</p>
  </section>

  <footer>
    <p><strong>Solidaridad v1.2.0</strong> · paquete generado el {dt.date.today().isoformat()} ·
    <span class="ok">{checks} comprobaciones PASA · 0 FALLA</span></p>
    <p>Contenido: <code>src/</code> (maestros), <code>dist/png/</code> (4 tintas), <code>dist/sticker/</code>,
    <code>docs/</code>, <code>preview/</code>. Léase también <code>DOCUMENTO-MAESTRO.md</code> y <code>README.md</code>.</p>
    <p>Licencias: arte y documentación <a href="../LICENSE-ARTWORK">CC BY 4.0</a> · código
    <a href="../LICENSE">MIT</a>. Atribución: «Solidaridad» © 2026 osarevalo —
    <a href="https://github.com/osarevalo/solidaridad-emoticon">github.com/osarevalo/solidaridad-emoticon</a>.</p>
  </footer>
</div>
</body>
</html>
"""
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "preview.html"
    path.write_text(doc, encoding="utf-8")
    return path


def main() -> int:
    sheet = contact_sheet()
    abrazo_sheet = abrazo_contact_sheet()
    page = html()
    print(f"OK: {sheet.relative_to(ROOT)}")
    print(f"OK: {abrazo_sheet.relative_to(ROOT)}")
    print(f"OK: {page.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
