# Verificación geométrica y de empaquetado

> Generado por `scripts/verify_geometry.py` a partir de los SVG maestros y de
> los PNG/WebP exportados. Este documento sustituye a las cifras «a ojo» del
> borrador: todo lo que aparece aquí se recalcula en cada ejecución.

**Resultado global: 178 PASA · 0 FALLA**

## Hallazgos que corrigen el borrador v1.0

| Dato del borrador | Valor real medido | Acción |
|---|---|---|
| Gap de cabezas ≈ 1.8 u (visual ≈ 1.0) | 2.0 u de hueco (8.4 u entre centros, radio visual 3.2) | corregido en el documento maestro |
| Área activa y 5.0–26.7 | y 5.6–26.7 (la cabeza ya no lleva trazo de 2.4) | corregido |
| Cabeza con trazo 2.4 (anillo) | cabeza rellena con trazo 1.2 (radio visual 3.2) | corregido en SVG |
| Junta central 16.04 / 15.96 | punto compartido exacto (16, 17.5) | corregido en SVG |
| Base interior 14.8 / 17.2 | 13.6 / 18.4 (se evita el goteo central) | corregido en SVG |

## Acta de comprobaciones

| Bloque | Comprobación | Resultado | Valor medido |
|---|---|---|---|
| Maestros SVG | existe src/solidaridad.svg | PASA | sí |
| Maestros SVG | solidaridad: viewBox 0 0 32 32 | PASA | 0 0 32 32 |
| Maestros SVG | solidaridad: role=img | PASA | img |
| Maestros SVG | solidaridad: aria-label presente | PASA | Me solidarizo con vos |
| Maestros SVG | solidaridad: sin width/height fijos | PASA | width=None height=None |
| Maestros SVG | solidaridad: sin colores fijos (solo currentColor) | PASA | sin hex/rgb |
| Maestros SVG | solidaridad: sin <script> ni recursos externos | PASA | limpio |
| Maestros SVG | existe src/solidaridad-fill.svg | PASA | sí |
| Maestros SVG | solidaridad-fill: viewBox 0 0 32 32 | PASA | 0 0 32 32 |
| Maestros SVG | solidaridad-fill: role=img | PASA | img |
| Maestros SVG | solidaridad-fill: aria-label presente | PASA | Me solidarizo con vos |
| Maestros SVG | solidaridad-fill: sin width/height fijos | PASA | width=None height=None |
| Maestros SVG | solidaridad-fill: sin colores fijos (solo currentColor) | PASA | sin hex/rgb |
| Maestros SVG | solidaridad-fill: sin <script> ni recursos externos | PASA | limpio |
| Maestros SVG | existe src/solidaridad-me-sumo.svg | PASA | sí |
| Maestros SVG | solidaridad-me-sumo: viewBox 0 0 32 32 | PASA | 0 0 32 32 |
| Maestros SVG | solidaridad-me-sumo: role=img | PASA | img |
| Maestros SVG | solidaridad-me-sumo: aria-label presente | PASA | Me sumo |
| Maestros SVG | solidaridad-me-sumo: sin width/height fijos | PASA | width=None height=None |
| Maestros SVG | solidaridad-me-sumo: sin colores fijos (solo currentColor) | PASA | sin hex/rgb |
| Maestros SVG | solidaridad-me-sumo: sin <script> ni recursos externos | PASA | limpio |
| Maestros SVG | existe src/solidaridad-causa.svg | PASA | sí |
| Maestros SVG | solidaridad-causa: viewBox 0 0 32 32 | PASA | 0 0 32 32 |
| Maestros SVG | solidaridad-causa: role=img | PASA | img |
| Maestros SVG | solidaridad-causa: aria-label presente | PASA | Misma causa |
| Maestros SVG | solidaridad-causa: sin width/height fijos | PASA | width=None height=None |
| Maestros SVG | solidaridad-causa: sin colores fijos (solo currentColor) | PASA | sin hex/rgb |
| Maestros SVG | solidaridad-causa: sin <script> ni recursos externos | PASA | limpio |
| Maestros SVG | existe src/solidaridad-sticker.svg | PASA | sí |
| Maestros SVG | solidaridad-sticker: viewBox 0 0 32 32 | PASA | 0 0 32 32 |
| Maestros SVG | solidaridad-sticker: role=img | PASA | img |
| Maestros SVG | solidaridad-sticker: aria-label presente | PASA | Me solidarizo con vos |
| Maestros SVG | solidaridad-sticker: sin width/height fijos | PASA | width=None height=None |
| Maestros SVG | solidaridad-sticker: sin colores fijos (solo currentColor) | PASA | sin hex/rgb |
| Maestros SVG | solidaridad-sticker: sin <script> ni recursos externos | PASA | limpio |
| Geometría | solidaridad: simetría especular exacta sobre x=16 | PASA | izquierda espejada == derecha |
| Geometría | solidaridad: contacto de hombros exacto en (16, 17.5) | PASA | (16.0, 17.5) / (16.0, 17.5) |
| Geometría | solidaridad-fill: simetría especular exacta sobre x=16 | PASA | izquierda espejada == derecha |
| Geometría | solidaridad-fill: contacto de hombros exacto en (16, 17.5) | PASA | (16.0, 17.5) / (16.0, 17.5) |
| Geometría | solidaridad-me-sumo: simetría especular exacta sobre x=16 | PASA | izquierda espejada == derecha |
| Geometría | solidaridad-me-sumo: contacto de hombros exacto en (16, 17.5) | PASA | (16.0, 17.5) / (16.0, 17.5) |
| Geometría | solidaridad-causa: simetría especular exacta sobre x=16 | PASA | izquierda espejada == derecha |
| Geometría | solidaridad-causa: contacto de hombros exacto en (16, 17.5) | PASA | (16.0, 17.5) / (16.0, 17.5) |
| Geometría | solidaridad-sticker: simetría especular exacta sobre x=16 | PASA | izquierda espejada == derecha |
| Geometría | solidaridad-sticker: contacto de hombros exacto en (16, 17.5) | PASA | (16.0, 17.5) / (16.0, 17.5) |
| Geometría | solidaridad: cabezas cx 11.8 / 20.2, cy 8.8, r 2.6 | PASA | cx=[11.8, 20.2], cy=[8.8, 8.8], r=2.6 |
| Geometría | solidaridad: separación visual entre cabezas = 2.0 u | PASA | 2.00 u (radio visual 3.20) |
| Geometría | solidaridad: cabeza unida al hombro (solape > 0) | PASA | solape 0.70 u |
| Geometría | solidaridad-fill: cabezas cx 11.8 / 20.2, cy 8.8, r 2.6 | PASA | cx=[11.8, 20.2], cy=[8.8, 8.8], r=2.6 |
| Geometría | solidaridad-fill: separación visual entre cabezas = 2.0 u | PASA | 2.00 u (radio visual 3.20) |
| Geometría | solidaridad-fill: cabeza unida al hombro (solape > 0) | PASA | solape 0.10 u |
| Geometría | solidaridad: área activa (3.6, 5.6)–(28.4, 26.7) | PASA | (3.60, 5.60, 28.40, 26.70) |
| Geometría | solidaridad-fill: área activa (4.2, 5.6)–(27.8, 26.1) | PASA | (4.20, 5.60, 27.80, 26.10) |
| Geometría | solidaridad-causa: área activa (3.6, 5.6)–(28.4, 28.0) | PASA | (3.60, 5.60, 28.40, 28.00) |
| Geometría | «Me sumo»: el brazo entra desde fuera del viewBox (recorte intencional) | PASA | xmin=-2.60 (se recorta a 0), ymax=26.70 |
| Sticker | dos animaciones animateTransform (una por figura) | PASA | 2 |
| Sticker | duración 0.55s en ambas | PASA | 2 |
| Sticker | overshoot de 0.6 u declarado | PASA | values -10→0.6→0 y 10→-0.6→0 |
| Sticker | splines coherentes con el plan | PASA | 2+2 |
| Sticker | respeta prefers-reduced-motion (documentado en CSS de la familia) | PASA | ver preview/preview.html y §Accesibilidad del documento maestro |
| Maestros SVG | solidaridad: contenido dentro del viewBox | PASA | (3.60, 5.60, 28.40, 26.70) |
| Maestros SVG | solidaridad-fill: contenido dentro del viewBox | PASA | (4.20, 5.60, 27.80, 26.10) |
| Maestros SVG | «Me sumo»: desborde solo del brazo (esperado) | PASA | xmin=-2.60 |
| Maestros SVG | solidaridad-causa: contenido dentro del viewBox | PASA | (3.60, 5.60, 28.40, 28.00) |
| Maestros SVG | sticker: pose final dentro del viewBox | PASA | (3.60, 5.60, 28.40, 26.70) |
| Exportación | ink/solidaridad_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | ink/solidaridad_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | ink/solidaridad_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | ink/solidaridad_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | ink/solidaridad_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | ink/solidaridad_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | ink/solidaridad_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | ink/solidaridad-fill_16.png (16×16, alfa) | PASA | (16, 16) RGBA |
| Exportación | ink/solidaridad-fill_20.png (20×20, alfa) | PASA | (20, 20) RGBA |
| Exportación | ink/solidaridad-me-sumo_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | ink/solidaridad-me-sumo_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | ink/solidaridad-me-sumo_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | ink/solidaridad-me-sumo_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | ink/solidaridad-me-sumo_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | ink/solidaridad-me-sumo_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | ink/solidaridad-me-sumo_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | ink/solidaridad-causa_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | ink/solidaridad-causa_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | ink/solidaridad-causa_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | ink/solidaridad-causa_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | ink/solidaridad-causa_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | ink/solidaridad-causa_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | ink/solidaridad-causa_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | teal/solidaridad_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | teal/solidaridad_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | teal/solidaridad_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | teal/solidaridad_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | teal/solidaridad_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | teal/solidaridad_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | teal/solidaridad_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | teal/solidaridad-fill_16.png (16×16, alfa) | PASA | (16, 16) RGBA |
| Exportación | teal/solidaridad-fill_20.png (20×20, alfa) | PASA | (20, 20) RGBA |
| Exportación | teal/solidaridad-me-sumo_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | teal/solidaridad-me-sumo_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | teal/solidaridad-me-sumo_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | teal/solidaridad-me-sumo_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | teal/solidaridad-me-sumo_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | teal/solidaridad-me-sumo_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | teal/solidaridad-me-sumo_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | teal/solidaridad-causa_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | teal/solidaridad-causa_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | teal/solidaridad-causa_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | teal/solidaridad-causa_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | teal/solidaridad-causa_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | teal/solidaridad-causa_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | teal/solidaridad-causa_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | violet/solidaridad_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | violet/solidaridad_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | violet/solidaridad_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | violet/solidaridad_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | violet/solidaridad_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | violet/solidaridad_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | violet/solidaridad_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | violet/solidaridad-fill_16.png (16×16, alfa) | PASA | (16, 16) RGBA |
| Exportación | violet/solidaridad-fill_20.png (20×20, alfa) | PASA | (20, 20) RGBA |
| Exportación | violet/solidaridad-me-sumo_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | violet/solidaridad-me-sumo_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | violet/solidaridad-me-sumo_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | violet/solidaridad-me-sumo_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | violet/solidaridad-me-sumo_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | violet/solidaridad-me-sumo_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | violet/solidaridad-me-sumo_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | violet/solidaridad-causa_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | violet/solidaridad-causa_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | violet/solidaridad-causa_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | violet/solidaridad-causa_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | violet/solidaridad-causa_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | violet/solidaridad-causa_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | violet/solidaridad-causa_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | white/solidaridad_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | white/solidaridad_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | white/solidaridad_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | white/solidaridad_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | white/solidaridad_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | white/solidaridad_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | white/solidaridad_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | white/solidaridad-fill_16.png (16×16, alfa) | PASA | (16, 16) RGBA |
| Exportación | white/solidaridad-fill_20.png (20×20, alfa) | PASA | (20, 20) RGBA |
| Exportación | white/solidaridad-me-sumo_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | white/solidaridad-me-sumo_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | white/solidaridad-me-sumo_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | white/solidaridad-me-sumo_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | white/solidaridad-me-sumo_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | white/solidaridad-me-sumo_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | white/solidaridad-me-sumo_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | white/solidaridad-causa_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | white/solidaridad-causa_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | white/solidaridad-causa_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | white/solidaridad-causa_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | white/solidaridad-causa_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | white/solidaridad-causa_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | white/solidaridad-causa_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | regla de tamaños: B (silueta) solo 16 y 20 px | PASA | [16, 20] |
| Exportación | regla de tamaños: A (trazo) desde 24 px | PASA | min=24 |
| Exportación | regla de tamaños: familia desde 24 px | PASA | 24 |
| Exportación | set completo de tamaños por tinta | PASA | 92 PNG |
| Exportación | sticker estático ink 128px | PASA | ok |
| Exportación | sticker estático ink 256px | PASA | ok |
| Exportación | sticker estático ink 512px | PASA | ok |
| Exportación | sticker estático teal 128px | PASA | ok |
| Exportación | sticker estático teal 256px | PASA | ok |
| Exportación | sticker estático teal 512px | PASA | ok |
| Exportación | sticker estático violet 128px | PASA | ok |
| Exportación | sticker estático violet 256px | PASA | ok |
| Exportación | sticker estático violet 512px | PASA | ok |
| Exportación | sticker estático white 128px | PASA | ok |
| Exportación | sticker estático white 256px | PASA | ok |
| Exportación | sticker estático white 512px | PASA | ok |
| Exportación | WebP animado 512 (principal) | PASA | 122 KB |
| Exportación | GIF animado 512 (compatibilidad) | PASA | 65 KB |
| Exportación | WebP animado 256 | PASA | 64 KB |
| Exportación | WebP animado 512×512 (frames únicos; los repetidos se fusionan con su duración) | PASA | (512, 512) · 15 frames |
| Exportación | convención de nombres {glifo}_{tamaño}.png | PASA | 92 archivos |

## Notas

- El brazo de «Me sumo» se dibuja a propósito desde fuera del `viewBox` para
  que entre por el borde; el recorte es intencional y no un error de caja.
- El sticker animado se exporta también frame a frame con la misma curva de
  easing que el SMIL, de modo que el WebP/GIF coincide con el SVG.
- Las comprobaciones de color y accesibilidad se hacen sobre los maestros
  (`currentColor`, `role="img"`, `aria-label`); las tintas viven en el build.

---

*Documento generado automáticamente. No editar a mano: ejecutar `make verify`.*
