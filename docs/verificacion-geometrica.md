# Verificación geométrica y de empaquetado

> Generado por `scripts/verify_geometry.py` a partir de los SVG maestros y de
> los PNG/WebP exportados. Este documento sustituye a las cifras «a ojo» del
> borrador: todo lo que aparece aquí se recalcula en cada ejecución.

**Resultado global: 547 PASA · 0 FALLA**

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
| Maestros SVG | solidaridad: sin colores fijos fuera de defs (solo currentColor) | PASA | sin hex/rgb fuera de defs |
| Maestros SVG | solidaridad: sin <script> ni recursos externos | PASA | limpio |
| Maestros SVG | existe src/solidaridad-fill.svg | PASA | sí |
| Maestros SVG | solidaridad-fill: viewBox 0 0 32 32 | PASA | 0 0 32 32 |
| Maestros SVG | solidaridad-fill: role=img | PASA | img |
| Maestros SVG | solidaridad-fill: aria-label presente | PASA | Me solidarizo con vos |
| Maestros SVG | solidaridad-fill: sin width/height fijos | PASA | width=None height=None |
| Maestros SVG | solidaridad-fill: sin colores fijos fuera de defs (solo currentColor) | PASA | sin hex/rgb fuera de defs |
| Maestros SVG | solidaridad-fill: sin <script> ni recursos externos | PASA | limpio |
| Maestros SVG | existe src/solidaridad-me-sumo.svg | PASA | sí |
| Maestros SVG | solidaridad-me-sumo: viewBox 0 0 32 32 | PASA | 0 0 32 32 |
| Maestros SVG | solidaridad-me-sumo: role=img | PASA | img |
| Maestros SVG | solidaridad-me-sumo: aria-label presente | PASA | Me sumo |
| Maestros SVG | solidaridad-me-sumo: sin width/height fijos | PASA | width=None height=None |
| Maestros SVG | solidaridad-me-sumo: sin colores fijos fuera de defs (solo currentColor) | PASA | sin hex/rgb fuera de defs |
| Maestros SVG | solidaridad-me-sumo: sin <script> ni recursos externos | PASA | limpio |
| Maestros SVG | existe src/solidaridad-causa.svg | PASA | sí |
| Maestros SVG | solidaridad-causa: viewBox 0 0 32 32 | PASA | 0 0 32 32 |
| Maestros SVG | solidaridad-causa: role=img | PASA | img |
| Maestros SVG | solidaridad-causa: aria-label presente | PASA | Misma causa |
| Maestros SVG | solidaridad-causa: sin width/height fijos | PASA | width=None height=None |
| Maestros SVG | solidaridad-causa: sin colores fijos fuera de defs (solo currentColor) | PASA | sin hex/rgb fuera de defs |
| Maestros SVG | solidaridad-causa: sin <script> ni recursos externos | PASA | limpio |
| Maestros SVG | existe src/abrazo.svg | PASA | sí |
| Maestros SVG | abrazo: viewBox 0 0 32 32 | PASA | 0 0 32 32 |
| Maestros SVG | abrazo: role=img | PASA | img |
| Maestros SVG | abrazo: aria-label presente | PASA | Abrazo de apoyo |
| Maestros SVG | abrazo: sin width/height fijos | PASA | width=None height=None |
| Maestros SVG | abrazo: sin colores fijos fuera de defs (solo currentColor) | PASA | sin hex/rgb fuera de defs |
| Maestros SVG | abrazo: sin <script> ni recursos externos | PASA | limpio |
| Maestros SVG | existe src/abrazo-me-sumo.svg | PASA | sí |
| Maestros SVG | abrazo-me-sumo: viewBox 0 0 32 32 | PASA | 0 0 32 32 |
| Maestros SVG | abrazo-me-sumo: role=img | PASA | img |
| Maestros SVG | abrazo-me-sumo: aria-label presente | PASA | Abrazo, me sumo |
| Maestros SVG | abrazo-me-sumo: sin width/height fijos | PASA | width=None height=None |
| Maestros SVG | abrazo-me-sumo: sin colores fijos fuera de defs (solo currentColor) | PASA | sin hex/rgb fuera de defs |
| Maestros SVG | abrazo-me-sumo: sin <script> ni recursos externos | PASA | limpio |
| Maestros SVG | existe src/abrazo-causa.svg | PASA | sí |
| Maestros SVG | abrazo-causa: viewBox 0 0 32 32 | PASA | 0 0 32 32 |
| Maestros SVG | abrazo-causa: role=img | PASA | img |
| Maestros SVG | abrazo-causa: aria-label presente | PASA | Abrazo, misma causa |
| Maestros SVG | abrazo-causa: sin width/height fijos | PASA | width=None height=None |
| Maestros SVG | abrazo-causa: sin colores fijos fuera de defs (solo currentColor) | PASA | sin hex/rgb fuera de defs |
| Maestros SVG | abrazo-causa: sin <script> ni recursos externos | PASA | limpio |
| Maestros SVG | existe src/abrazo-mutuo.svg | PASA | sí |
| Maestros SVG | abrazo-mutuo: viewBox 0 0 32 32 | PASA | 0 0 32 32 |
| Maestros SVG | abrazo-mutuo: role=img | PASA | img |
| Maestros SVG | abrazo-mutuo: aria-label presente | PASA | Abrazo mutuo |
| Maestros SVG | abrazo-mutuo: sin width/height fijos | PASA | width=None height=None |
| Maestros SVG | abrazo-mutuo: sin colores fijos fuera de defs (solo currentColor) | PASA | sin hex/rgb fuera de defs |
| Maestros SVG | abrazo-mutuo: sin <script> ni recursos externos | PASA | limpio |
| Maestros SVG | existe src/corazon.svg | PASA | sí |
| Maestros SVG | corazon: viewBox 0 0 32 32 | PASA | 0 0 32 32 |
| Maestros SVG | corazon: role=img | PASA | img |
| Maestros SVG | corazon: aria-label presente | PASA | Solidaridad con corazón |
| Maestros SVG | corazon: sin width/height fijos | PASA | width=None height=None |
| Maestros SVG | corazon: sin colores fijos fuera de defs (solo currentColor) | PASA | sin hex/rgb fuera de defs |
| Maestros SVG | corazon: sin <script> ni recursos externos | PASA | limpio |
| Maestros SVG | existe src/corazon-fill.svg | PASA | sí |
| Maestros SVG | corazon-fill: viewBox 0 0 32 32 | PASA | 0 0 32 32 |
| Maestros SVG | corazon-fill: role=img | PASA | img |
| Maestros SVG | corazon-fill: aria-label presente | PASA | Solidaridad con corazón |
| Maestros SVG | corazon-fill: sin width/height fijos | PASA | width=None height=None |
| Maestros SVG | corazon-fill: sin colores fijos fuera de defs (solo currentColor) | PASA | sin hex/rgb fuera de defs |
| Maestros SVG | corazon-fill: sin <script> ni recursos externos | PASA | limpio |
| Maestros SVG | existe src/corazon-me-sumo.svg | PASA | sí |
| Maestros SVG | corazon-me-sumo: viewBox 0 0 32 32 | PASA | 0 0 32 32 |
| Maestros SVG | corazon-me-sumo: role=img | PASA | img |
| Maestros SVG | corazon-me-sumo: aria-label presente | PASA | Me sumo con corazón |
| Maestros SVG | corazon-me-sumo: sin width/height fijos | PASA | width=None height=None |
| Maestros SVG | corazon-me-sumo: sin colores fijos fuera de defs (solo currentColor) | PASA | sin hex/rgb fuera de defs |
| Maestros SVG | corazon-me-sumo: sin <script> ni recursos externos | PASA | limpio |
| Maestros SVG | existe src/corazon-causa.svg | PASA | sí |
| Maestros SVG | corazon-causa: viewBox 0 0 32 32 | PASA | 0 0 32 32 |
| Maestros SVG | corazon-causa: role=img | PASA | img |
| Maestros SVG | corazon-causa: aria-label presente | PASA | Misma causa con corazón |
| Maestros SVG | corazon-causa: sin width/height fijos | PASA | width=None height=None |
| Maestros SVG | corazon-causa: sin colores fijos fuera de defs (solo currentColor) | PASA | sin hex/rgb fuera de defs |
| Maestros SVG | corazon-causa: sin <script> ni recursos externos | PASA | limpio |
| Maestros SVG | existe src/corazon-sticker.svg | PASA | sí |
| Maestros SVG | corazon-sticker: viewBox 0 0 32 32 | PASA | 0 0 32 32 |
| Maestros SVG | corazon-sticker: role=img | PASA | img |
| Maestros SVG | corazon-sticker: aria-label presente | PASA | Solidaridad con corazón |
| Maestros SVG | corazon-sticker: sin width/height fijos | PASA | width=None height=None |
| Maestros SVG | corazon-sticker: sin colores fijos fuera de defs (solo currentColor) | PASA | sin hex/rgb fuera de defs |
| Maestros SVG | corazon-sticker: sin <script> ni recursos externos | PASA | limpio |
| Maestros SVG | existe src/solidaridad-sticker.svg | PASA | sí |
| Maestros SVG | solidaridad-sticker: viewBox 0 0 32 32 | PASA | 0 0 32 32 |
| Maestros SVG | solidaridad-sticker: role=img | PASA | img |
| Maestros SVG | solidaridad-sticker: aria-label presente | PASA | Me solidarizo con vos |
| Maestros SVG | solidaridad-sticker: sin width/height fijos | PASA | width=None height=None |
| Maestros SVG | solidaridad-sticker: sin colores fijos fuera de defs (solo currentColor) | PASA | sin hex/rgb fuera de defs |
| Maestros SVG | solidaridad-sticker: sin <script> ni recursos externos | PASA | limpio |
| Geometría | solidaridad: simetría especular exacta sobre x=16 | PASA | izquierda espejada == derecha |
| Geometría | solidaridad: contacto de hombros exacto en (16, 17.5) | PASA | (16.0, 17.5) / (16.0, 17.5) |
| Geometría | solidaridad-fill: simetría especular exacta sobre x=16 | PASA | izquierda espejada == derecha |
| Geometría | solidaridad-fill: contacto de hombros exacto en (16, 17.5) | PASA | (16.0, 17.5) / (16.0, 17.5) |
| Geometría | solidaridad-me-sumo: simetría especular exacta sobre x=16 | PASA | izquierda espejada == derecha |
| Geometría | solidaridad-me-sumo: contacto de hombros exacto en (16, 17.5) | PASA | (16.0, 17.5) / (16.0, 17.5) |
| Geometría | solidaridad-causa: simetría especular exacta sobre x=16 | PASA | izquierda espejada == derecha |
| Geometría | solidaridad-causa: contacto de hombros exacto en (16, 17.5) | PASA | (16.0, 17.5) / (16.0, 17.5) |
| Geometría | abrazo: simetría especular exacta sobre x=16 | PASA | izquierda espejada == derecha |
| Geometría | abrazo: contacto de hombros exacto en (16, 17.5) | PASA | (16.0, 17.5) / (16.0, 17.5) |
| Geometría | abrazo-me-sumo: simetría especular exacta sobre x=16 | PASA | izquierda espejada == derecha |
| Geometría | abrazo-me-sumo: contacto de hombros exacto en (16, 17.5) | PASA | (16.0, 17.5) / (16.0, 17.5) |
| Geometría | abrazo-causa: simetría especular exacta sobre x=16 | PASA | izquierda espejada == derecha |
| Geometría | abrazo-causa: contacto de hombros exacto en (16, 17.5) | PASA | (16.0, 17.5) / (16.0, 17.5) |
| Geometría | abrazo-mutuo: simetría especular exacta sobre x=16 | PASA | izquierda espejada == derecha |
| Geometría | abrazo-mutuo: contacto de hombros exacto en (16, 17.5) | PASA | (16.0, 17.5) / (16.0, 17.5) |
| Geometría | corazon: simetría especular exacta sobre x=16 | PASA | izquierda espejada == derecha |
| Geometría | corazon: contacto de hombros exacto en (16, 17.5) | PASA | (16.0, 17.5) / (16.0, 17.5) |
| Geometría | corazon-fill: simetría especular exacta sobre x=16 | PASA | izquierda espejada == derecha |
| Geometría | corazon-fill: contacto de hombros exacto en (16, 17.5) | PASA | (16.0, 17.5) / (16.0, 17.5) |
| Geometría | corazon-me-sumo: simetría especular exacta sobre x=16 | PASA | izquierda espejada == derecha |
| Geometría | corazon-me-sumo: contacto de hombros exacto en (16, 17.5) | PASA | (16.0, 17.5) / (16.0, 17.5) |
| Geometría | corazon-causa: simetría especular exacta sobre x=16 | PASA | izquierda espejada == derecha |
| Geometría | corazon-causa: contacto de hombros exacto en (16, 17.5) | PASA | (16.0, 17.5) / (16.0, 17.5) |
| Geometría | corazon-sticker: simetría especular exacta sobre x=16 | PASA | izquierda espejada == derecha |
| Geometría | corazon-sticker: contacto de hombros exacto en (16, 17.5) | PASA | (16.0, 17.5) / (16.0, 17.5) |
| Geometría | solidaridad-sticker: simetría especular exacta sobre x=16 | PASA | izquierda espejada == derecha |
| Geometría | solidaridad-sticker: contacto de hombros exacto en (16, 17.5) | PASA | (16.0, 17.5) / (16.0, 17.5) |
| Geometría | solidaridad: cabezas cx 11.8 / 20.2, cy 8.8, r 2.6 | PASA | cx=[11.8, 20.2], cy=[8.8, 8.8], r=2.6 |
| Geometría | solidaridad: separación visual entre cabezas = 2.0 u | PASA | 2.00 u (radio visual 3.20) |
| Geometría | solidaridad: cabeza unida al hombro (solape > 0) | PASA | solape 0.70 u |
| Geometría | solidaridad-fill: cabezas cx 11.8 / 20.2, cy 8.8, r 2.6 | PASA | cx=[11.8, 20.2], cy=[8.8, 8.8], r=2.6 |
| Geometría | solidaridad-fill: separación visual entre cabezas = 2.0 u | PASA | 2.00 u (radio visual 3.20) |
| Geometría | solidaridad-fill: cabeza unida al hombro (solape > 0) | PASA | solape 0.10 u |
| Geometría | abrazo: cabezas cx 11.8 / 20.2, cy 8.8, r 2.6 | PASA | cx=[20.2, 11.8], cy=[8.8, 8.8], r=2.6 |
| Geometría | abrazo: separación visual entre cabezas = 2.0 u | PASA | 2.00 u (radio visual 3.20) |
| Geometría | abrazo: cabeza unida al hombro (solape > 0) | PASA | solape 0.70 u |
| Geometría | abrazo-me-sumo: cabezas cx 11.8 / 20.2, cy 8.8, r 2.6 | PASA | cx=[20.2, 11.8], cy=[8.8, 8.8], r=2.6 |
| Geometría | abrazo-me-sumo: separación visual entre cabezas = 2.0 u | PASA | 2.00 u (radio visual 3.20) |
| Geometría | abrazo-me-sumo: cabeza unida al hombro (solape > 0) | PASA | solape 0.70 u |
| Geometría | abrazo-causa: cabezas cx 11.8 / 20.2, cy 8.8, r 2.6 | PASA | cx=[20.2, 11.8], cy=[8.8, 8.8], r=2.6 |
| Geometría | abrazo-causa: separación visual entre cabezas = 2.0 u | PASA | 2.00 u (radio visual 3.20) |
| Geometría | abrazo-causa: cabeza unida al hombro (solape > 0) | PASA | solape 0.70 u |
| Geometría | abrazo-mutuo: cabezas cx 11.8 / 20.2, cy 8.8, r 2.6 | PASA | cx=[11.8, 20.2], cy=[8.8, 8.8], r=2.6 |
| Geometría | abrazo-mutuo: separación visual entre cabezas = 2.0 u | PASA | 2.00 u (radio visual 3.20) |
| Geometría | abrazo-mutuo: cabeza unida al hombro (solape > 0) | PASA | solape 0.70 u |
| Geometría | corazon: cabezas cx 11.8 / 20.2, cy 8.8, r 2.6 | PASA | cx=[11.8, 20.2], cy=[8.8, 8.8], r=2.6 |
| Geometría | corazon: separación visual entre cabezas = 2.0 u | PASA | 2.00 u (radio visual 3.20) |
| Geometría | corazon: cabeza unida al hombro (solape > 0) | PASA | solape 0.70 u |
| Geometría | corazon-fill: cabezas cx 11.8 / 20.2, cy 8.8, r 2.6 | PASA | cx=[11.8, 20.2], cy=[8.8, 8.8], r=2.6 |
| Geometría | corazon-fill: separación visual entre cabezas = 2.0 u | PASA | 2.00 u (radio visual 3.20) |
| Geometría | corazon-fill: cabeza unida al hombro (solape > 0) | PASA | solape 0.10 u |
| Geometría | corazon-me-sumo: cabezas cx 11.8 / 20.2, cy 8.8, r 2.6 | PASA | cx=[11.8, 20.2], cy=[8.8, 8.8], r=2.6 |
| Geometría | corazon-me-sumo: separación visual entre cabezas = 2.0 u | PASA | 2.00 u (radio visual 3.20) |
| Geometría | corazon-me-sumo: cabeza unida al hombro (solape > 0) | PASA | solape 0.70 u |
| Geometría | corazon-causa: cabezas cx 11.8 / 20.2, cy 8.8, r 2.6 | PASA | cx=[11.8, 20.2], cy=[8.8, 8.8], r=2.6 |
| Geometría | corazon-causa: separación visual entre cabezas = 2.0 u | PASA | 2.00 u (radio visual 3.20) |
| Geometría | corazon-causa: cabeza unida al hombro (solape > 0) | PASA | solape 0.70 u |
| Geometría | solidaridad: área activa (3.6, 5.6)–(28.4, 26.7) | PASA | (3.60, 5.60, 28.40, 26.70) |
| Geometría | solidaridad-fill: área activa (4.2, 5.6)–(27.8, 26.1) | PASA | (4.20, 5.60, 27.80, 26.10) |
| Geometría | solidaridad-causa: área activa (3.6, 5.6)–(28.4, 28.0) | PASA | (3.60, 5.60, 28.40, 28.00) |
| Geometría | abrazo: área activa (3.6, 5.6)–(28.4, 26.7) | PASA | (3.60, 5.60, 28.40, 26.70) |
| Geometría | abrazo-causa: área activa (3.6, 5.6)–(28.4, 28.0) | PASA | (3.60, 5.60, 28.40, 28.00) |
| Geometría | abrazo-mutuo: área activa (3.6, 5.6)–(28.4, 26.7) | PASA | (3.60, 5.60, 28.40, 26.70) |
| Geometría | corazon: área activa (3.6, 5.6)–(28.4, 26.7) | PASA | (3.60, 5.60, 28.40, 26.70) |
| Geometría | corazon-fill: área activa (4.2, 5.6)–(27.8, 26.1) | PASA | (4.20, 5.60, 27.80, 26.10) |
| Geometría | corazon-causa: área activa (3.6, 5.6)–(28.4, 28.0) | PASA | (3.60, 5.60, 28.40, 28.00) |
| Geometría | solidaridad-me-sumo: el brazo entra desde fuera del viewBox (recorte intencional) | PASA | xmin=-2.60 (se recorta a 0), ymax=26.70 |
| Geometría | abrazo-me-sumo: el brazo entra desde fuera del viewBox (recorte intencional) | PASA | xmin=-2.60 (se recorta a 0), ymax=26.70 |
| Geometría | corazon-me-sumo: el brazo entra desde fuera del viewBox (recorte intencional) | PASA | xmin=-2.60 (se recorta a 0), ymax=26.70 |
| Sticker | dos animaciones animateTransform (una por figura) | PASA | 2 |
| Sticker | duración 0.55s en ambas | PASA | 2 |
| Sticker | overshoot de 0.6 u declarado | PASA | values -10→0.6→0 y 10→-0.6→0 |
| Sticker | splines coherentes con el plan | PASA | 2+2 |
| Sticker | respeta prefers-reduced-motion (documentado en CSS de la familia) | PASA | ver preview/preview.html y §Accesibilidad del documento maestro |
| Sticker | corazón: la figura izquierda y derecha conservan la entrada | PASA | 2 grupos |
| Sticker | corazón: aparece a los 0.35 s con escala 0→1.2→1 | PASA | 3 keyframes |
| Sticker | corazón: opacidad 0→1 al aparecer | PASA | animate opacity |
| Corazón | corazon: corazón centrado en (16, 11.4) | PASA | translate(16 11.4) · path de corazón |
| Corazón | corazon-me-sumo: corazón centrado en (16, 11.4) | PASA | translate(16 11.4) · path de corazón |
| Corazón | corazon-causa: corazón centrado en (16, 11.4) | PASA | translate(16 11.4) · path de corazón |
| Corazón | corazon-fill: corazón centrado en (16, 12.2) | PASA | translate(16 12.2) · path de corazón |
| Corazón | corazon-sticker: dos animaciones de figura + aparición del corazón | PASA | 2 translate + 1 scale · begin 0.35 s |
| Corazón | corazon-sticker: corazones en todas las variantes | PASA | 4 glifos + sticker |
| Máscaras | abrazo: máscara declarada y referenciada | PASA | ids=['abzMask'] refs=['abzMask'] |
| Máscaras | abrazo: ids únicos | PASA | 1 máscara(s) |
| Máscaras | abrazo: hueco de 4.8 u y mano de 3.1 u en la máscara | PASA | knockout |
| Máscaras | abrazo: brazo de 2.4 u y mano de 1.7 u dibujados | PASA | brazo + mano |
| Máscaras | abrazo-me-sumo: máscara declarada y referenciada | PASA | ids=['abzMsMask'] refs=['abzMsMask'] |
| Máscaras | abrazo-me-sumo: ids únicos | PASA | 1 máscara(s) |
| Máscaras | abrazo-me-sumo: hueco de 4.8 u y mano de 3.1 u en la máscara | PASA | knockout |
| Máscaras | abrazo-me-sumo: brazo de 2.4 u y mano de 1.7 u dibujados | PASA | brazo + mano |
| Máscaras | abrazo-causa: máscara declarada y referenciada | PASA | ids=['abzCausaMask'] refs=['abzCausaMask'] |
| Máscaras | abrazo-causa: ids únicos | PASA | 1 máscara(s) |
| Máscaras | abrazo-causa: hueco de 4.8 u y mano de 3.1 u en la máscara | PASA | knockout |
| Máscaras | abrazo-causa: brazo de 2.4 u y mano de 1.7 u dibujados | PASA | brazo + mano |
| Máscaras | abrazo-mutuo: máscara declarada y referenciada | PASA | ids=['abzMutL', 'abzMutR'] refs=['abzMutL', 'abzMutR'] |
| Máscaras | abrazo-mutuo: ids únicos | PASA | 2 máscara(s) |
| Máscaras | abrazo-mutuo: hueco de 4.8 u y mano de 3.1 u en la máscara | PASA | knockout |
| Máscaras | abrazo-mutuo: brazo de 2.4 u y mano de 1.7 u dibujados | PASA | brazo + mano |
| Maestros SVG | solidaridad: contenido dentro del viewBox | PASA | (3.60, 5.60, 28.40, 26.70) |
| Maestros SVG | solidaridad-fill: contenido dentro del viewBox | PASA | (4.20, 5.60, 27.80, 26.10) |
| Maestros SVG | «Me sumo»: desborde solo del brazo (esperado) | PASA | xmin=-2.60 |
| Maestros SVG | solidaridad-causa: contenido dentro del viewBox | PASA | (3.60, 5.60, 28.40, 28.00) |
| Maestros SVG | abrazo: contenido dentro del viewBox | PASA | (3.60, 5.60, 28.40, 26.70) |
| Maestros SVG | «Me sumo»: desborde solo del brazo (esperado) | PASA | xmin=-2.60 |
| Maestros SVG | abrazo-causa: contenido dentro del viewBox | PASA | (3.60, 5.60, 28.40, 28.00) |
| Maestros SVG | abrazo-mutuo: contenido dentro del viewBox | PASA | (3.60, 5.60, 28.40, 26.70) |
| Maestros SVG | corazon: contenido dentro del viewBox | PASA | (3.60, 5.60, 28.40, 26.70) |
| Maestros SVG | corazon-fill: contenido dentro del viewBox | PASA | (4.20, 5.60, 27.80, 26.10) |
| Maestros SVG | «Me sumo»: desborde solo del brazo (esperado) | PASA | xmin=-2.60 |
| Maestros SVG | corazon-causa: contenido dentro del viewBox | PASA | (3.60, 5.60, 28.40, 28.00) |
| Maestros SVG | sticker: pose final dentro del viewBox | PASA | (3.60, 5.60, 28.40, 26.70) |
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
| Exportación | ink/abrazo_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | ink/abrazo_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | ink/abrazo_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | ink/abrazo_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | ink/abrazo_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | ink/abrazo_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | ink/abrazo_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | ink/abrazo-me-sumo_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | ink/abrazo-me-sumo_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | ink/abrazo-me-sumo_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | ink/abrazo-me-sumo_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | ink/abrazo-me-sumo_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | ink/abrazo-me-sumo_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | ink/abrazo-me-sumo_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | ink/abrazo-causa_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | ink/abrazo-causa_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | ink/abrazo-causa_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | ink/abrazo-causa_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | ink/abrazo-causa_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | ink/abrazo-causa_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | ink/abrazo-causa_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | ink/abrazo-mutuo_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | ink/abrazo-mutuo_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | ink/abrazo-mutuo_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | ink/abrazo-mutuo_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | ink/abrazo-mutuo_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | ink/abrazo-mutuo_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | ink/abrazo-mutuo_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | ink/corazon_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | ink/corazon_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | ink/corazon_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | ink/corazon_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | ink/corazon_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | ink/corazon_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | ink/corazon_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | ink/corazon-fill_16.png (16×16, alfa) | PASA | (16, 16) RGBA |
| Exportación | ink/corazon-fill_20.png (20×20, alfa) | PASA | (20, 20) RGBA |
| Exportación | ink/corazon-me-sumo_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | ink/corazon-me-sumo_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | ink/corazon-me-sumo_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | ink/corazon-me-sumo_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | ink/corazon-me-sumo_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | ink/corazon-me-sumo_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | ink/corazon-me-sumo_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | ink/corazon-causa_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | ink/corazon-causa_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | ink/corazon-causa_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | ink/corazon-causa_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | ink/corazon-causa_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | ink/corazon-causa_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | ink/corazon-causa_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
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
| Exportación | teal/abrazo_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | teal/abrazo_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | teal/abrazo_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | teal/abrazo_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | teal/abrazo_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | teal/abrazo_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | teal/abrazo_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | teal/abrazo-me-sumo_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | teal/abrazo-me-sumo_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | teal/abrazo-me-sumo_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | teal/abrazo-me-sumo_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | teal/abrazo-me-sumo_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | teal/abrazo-me-sumo_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | teal/abrazo-me-sumo_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | teal/abrazo-causa_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | teal/abrazo-causa_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | teal/abrazo-causa_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | teal/abrazo-causa_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | teal/abrazo-causa_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | teal/abrazo-causa_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | teal/abrazo-causa_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | teal/abrazo-mutuo_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | teal/abrazo-mutuo_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | teal/abrazo-mutuo_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | teal/abrazo-mutuo_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | teal/abrazo-mutuo_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | teal/abrazo-mutuo_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | teal/abrazo-mutuo_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | teal/corazon_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | teal/corazon_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | teal/corazon_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | teal/corazon_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | teal/corazon_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | teal/corazon_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | teal/corazon_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | teal/corazon-fill_16.png (16×16, alfa) | PASA | (16, 16) RGBA |
| Exportación | teal/corazon-fill_20.png (20×20, alfa) | PASA | (20, 20) RGBA |
| Exportación | teal/corazon-me-sumo_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | teal/corazon-me-sumo_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | teal/corazon-me-sumo_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | teal/corazon-me-sumo_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | teal/corazon-me-sumo_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | teal/corazon-me-sumo_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | teal/corazon-me-sumo_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | teal/corazon-causa_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | teal/corazon-causa_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | teal/corazon-causa_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | teal/corazon-causa_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | teal/corazon-causa_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | teal/corazon-causa_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | teal/corazon-causa_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
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
| Exportación | violet/abrazo_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | violet/abrazo_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | violet/abrazo_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | violet/abrazo_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | violet/abrazo_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | violet/abrazo_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | violet/abrazo_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | violet/abrazo-me-sumo_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | violet/abrazo-me-sumo_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | violet/abrazo-me-sumo_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | violet/abrazo-me-sumo_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | violet/abrazo-me-sumo_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | violet/abrazo-me-sumo_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | violet/abrazo-me-sumo_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | violet/abrazo-causa_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | violet/abrazo-causa_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | violet/abrazo-causa_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | violet/abrazo-causa_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | violet/abrazo-causa_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | violet/abrazo-causa_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | violet/abrazo-causa_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | violet/abrazo-mutuo_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | violet/abrazo-mutuo_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | violet/abrazo-mutuo_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | violet/abrazo-mutuo_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | violet/abrazo-mutuo_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | violet/abrazo-mutuo_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | violet/abrazo-mutuo_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | violet/corazon_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | violet/corazon_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | violet/corazon_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | violet/corazon_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | violet/corazon_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | violet/corazon_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | violet/corazon_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | violet/corazon-fill_16.png (16×16, alfa) | PASA | (16, 16) RGBA |
| Exportación | violet/corazon-fill_20.png (20×20, alfa) | PASA | (20, 20) RGBA |
| Exportación | violet/corazon-me-sumo_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | violet/corazon-me-sumo_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | violet/corazon-me-sumo_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | violet/corazon-me-sumo_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | violet/corazon-me-sumo_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | violet/corazon-me-sumo_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | violet/corazon-me-sumo_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | violet/corazon-causa_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | violet/corazon-causa_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | violet/corazon-causa_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | violet/corazon-causa_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | violet/corazon-causa_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | violet/corazon-causa_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | violet/corazon-causa_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
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
| Exportación | white/abrazo_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | white/abrazo_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | white/abrazo_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | white/abrazo_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | white/abrazo_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | white/abrazo_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | white/abrazo_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | white/abrazo-me-sumo_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | white/abrazo-me-sumo_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | white/abrazo-me-sumo_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | white/abrazo-me-sumo_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | white/abrazo-me-sumo_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | white/abrazo-me-sumo_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | white/abrazo-me-sumo_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | white/abrazo-causa_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | white/abrazo-causa_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | white/abrazo-causa_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | white/abrazo-causa_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | white/abrazo-causa_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | white/abrazo-causa_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | white/abrazo-causa_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | white/abrazo-mutuo_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | white/abrazo-mutuo_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | white/abrazo-mutuo_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | white/abrazo-mutuo_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | white/abrazo-mutuo_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | white/abrazo-mutuo_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | white/abrazo-mutuo_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | white/corazon_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | white/corazon_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | white/corazon_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | white/corazon_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | white/corazon_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | white/corazon_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | white/corazon_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | white/corazon-fill_16.png (16×16, alfa) | PASA | (16, 16) RGBA |
| Exportación | white/corazon-fill_20.png (20×20, alfa) | PASA | (20, 20) RGBA |
| Exportación | white/corazon-me-sumo_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | white/corazon-me-sumo_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | white/corazon-me-sumo_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | white/corazon-me-sumo_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | white/corazon-me-sumo_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | white/corazon-me-sumo_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | white/corazon-me-sumo_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | white/corazon-causa_24.png (24×24, alfa) | PASA | (24, 24) RGBA |
| Exportación | white/corazon-causa_32.png (32×32, alfa) | PASA | (32, 32) RGBA |
| Exportación | white/corazon-causa_48.png (48×48, alfa) | PASA | (48, 48) RGBA |
| Exportación | white/corazon-causa_64.png (64×64, alfa) | PASA | (64, 64) RGBA |
| Exportación | white/corazon-causa_128.png (128×128, alfa) | PASA | (128, 128) RGBA |
| Exportación | white/corazon-causa_256.png (256×256, alfa) | PASA | (256, 256) RGBA |
| Exportación | white/corazon-causa_512.png (512×512, alfa) | PASA | (512, 512) RGBA |
| Exportación | regla de tamaños: B (silueta) solo 16 y 20 px | PASA | [16, 20] |
| Exportación | regla de tamaños: A (trazo) desde 24 px | PASA | min=24 |
| Exportación | regla de tamaños: familia desde 24 px | PASA | 24 |
| Exportación | regla de tamaños: serie «Abrazo» desde 24 px | PASA | 24–512 |
| Exportación | serie «Abrazo» sin 16/20 (ahí se usa la serie original) | PASA | solo ≥ 24 |
| Exportación | serie «Corazón»: B 16/20 y A desde 24 | PASA | B 16/20 · A 24–512 |
| Exportación | set completo de tamaños por tinta | PASA | 296 PNG |
| Exportación | sticker estático solidaridad-sticker ink 128px | PASA | ok |
| Exportación | sticker estático solidaridad-sticker ink 256px | PASA | ok |
| Exportación | sticker estático solidaridad-sticker ink 512px | PASA | ok |
| Exportación | sticker estático corazon-sticker ink 128px | PASA | ok |
| Exportación | sticker estático corazon-sticker ink 256px | PASA | ok |
| Exportación | sticker estático corazon-sticker ink 512px | PASA | ok |
| Exportación | sticker estático solidaridad-sticker teal 128px | PASA | ok |
| Exportación | sticker estático solidaridad-sticker teal 256px | PASA | ok |
| Exportación | sticker estático solidaridad-sticker teal 512px | PASA | ok |
| Exportación | sticker estático corazon-sticker teal 128px | PASA | ok |
| Exportación | sticker estático corazon-sticker teal 256px | PASA | ok |
| Exportación | sticker estático corazon-sticker teal 512px | PASA | ok |
| Exportación | sticker estático solidaridad-sticker violet 128px | PASA | ok |
| Exportación | sticker estático solidaridad-sticker violet 256px | PASA | ok |
| Exportación | sticker estático solidaridad-sticker violet 512px | PASA | ok |
| Exportación | sticker estático corazon-sticker violet 128px | PASA | ok |
| Exportación | sticker estático corazon-sticker violet 256px | PASA | ok |
| Exportación | sticker estático corazon-sticker violet 512px | PASA | ok |
| Exportación | sticker estático solidaridad-sticker white 128px | PASA | ok |
| Exportación | sticker estático solidaridad-sticker white 256px | PASA | ok |
| Exportación | sticker estático solidaridad-sticker white 512px | PASA | ok |
| Exportación | sticker estático corazon-sticker white 128px | PASA | ok |
| Exportación | sticker estático corazon-sticker white 256px | PASA | ok |
| Exportación | sticker estático corazon-sticker white 512px | PASA | ok |
| Exportación | WebP animado 512 (principal) | PASA | 122 KB |
| Exportación | GIF animado 512 (compatibilidad) | PASA | 65 KB |
| Exportación | WebP animado 256 | PASA | 64 KB |
| Exportación | Corazón: WebP animado 512 | PASA | 122 KB |
| Exportación | Corazón: GIF animado 512 | PASA | 65 KB |
| Exportación | Corazón: WebP animado 256 | PASA | 63 KB |
| Exportación | WebP animado 512×512 (frames únicos; los repetidos se fusionan con su duración) | PASA | (512, 512) · 15 frames |
| Exportación | convención de nombres {glifo}_{tamaño}.png | PASA | 296 archivos |

## Notas

- El brazo de «Me sumo» se dibuja a propósito desde fuera del `viewBox` para
  que entre por el borde; el recorte es intencional y no un error de caja.
- El sticker animado se exporta también frame a frame con la misma curva de
  easing que el SMIL, de modo que el WebP/GIF coincide con el SVG.
- La serie «Abrazo» usa una máscara knockout: el cuerpo derecho se recorta
  alrededor del brazo y de la mano, dejando 1.2 u de transparencia. No agrega
  un segundo color; el hueco toma el color del fondo.
- La serie «Corazón» coloca un corazón entre las cabezas; se lee como
  afecto/pareja además de apoyo, por eso es una serie aparte y no sustituye
  a la serie original.
- Las comprobaciones de color y accesibilidad se hacen sobre los maestros
  (`currentColor`, `role="img"`, `aria-label`); las tintas viven en el build.

---

*Documento generado automáticamente. No editar a mano: ejecutar `make verify`.*
