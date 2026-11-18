# Changelog

## v1.2.0 — 2026-11-18 · serie alternativa «Abrazo»

Suma una segunda lectura del mismo vínculo: la figura izquierda pasa el brazo
por encima del hombro de la derecha y la mano queda visible al otro lado. La
serie original queda intacta; «Abrazo» es una familia adicional.

### Añadido

- `src/abrazo.svg` (glifo principal), `src/abrazo-me-sumo.svg`,
  `src/abrazo-causa.svg` y `src/abrazo-mutuo.svg`.
- **112 PNG nuevos** de la serie (4 glifos × 7 tamaños × 4 tintas), de 24 a
  512 px, en `dist/png/{ink,teal,violet,white}/abrazo*`.
- Hoja de contactos propia: `preview/contact-sheet-abrazo.png`.
- Sección de la serie en `preview/preview.html`, README y documento maestro.
- `verify_geometry.py` amplía la verificación a **364 comprobaciones**: cuerpo
  simétrico, cabezas, áreas activas, máscaras knockout y exportación de la
  serie nueva.

### Técnica

El brazo se dibuja con la misma tinta sobre el cuerpo derecho; ese cuerpo se
recorta con una **máscara knockout** de 4.8 u que deja 1.2 u de transparencia a
cada lado del brazo y de la mano. El hueco toma el color del fondo: no hay un
segundo color en el SVG. La mano va en (26.6, 15.4), r 1.7; el brazo es
`M15.0 17.1 C18.0 13.4 22.9 13.0 26.6 15.4` con trazo 2.4.

### Límites

La serie funciona desde **24 px**; a 16 y 20 px se usa la serie original
(B · silueta). No se agregó sticker animado para «Abrazo» en esta versión.

### Sin cambios

- Serie original, licencias (CC BY 4.0 + MIT), sticker y política de tamaños.
- Repositorio: <https://github.com/osarevalo/solidaridad-emoticon>.

## v1.1.0 — 2026-11-15 · paquete de producción

Cierra el documento maestro v1.0 (borrador aprobado en DeepSeek) y lo convierte
en un paquete entregable: SVG finales, PNG/WebP exportados, sticker animado,
verificación automática y documentación.

### Corregido respecto del borrador v1.0

| Problema | Corrección |
|---|---|
| Las cabezas de la versión A eran círculos con trazo 2.4 sin relleno: se veían como **anillos/donuts**, no como cabezas. | Cabeza rellena (`fill="currentColor"`) con `stroke-width="1.2"`. Radio visual 3.2, igual en A y B. |
| La unión central estaba en 16.04 / 15.96: el cruce de trazos dejaba un pequeño nudo. | Punto compartido exacto **(16, 17.5)** en las dos figuras; el cruce queda limpio y simétrico. |
| Las patas internas bajaban a 14.8 / 17.2: a 32 px el hueco se cerraba y el centro parecía un «goteo». | Base interior **13.6 / 18.4**: los cuerpos se separan bajo el hombro y el hueco respira. |
| El documento decía «gap de cabezas ≈ 1.8 u (visual ≈ 1.0)». | El hueco real es **2.0 u** (centros a 8.4 u; radio visual 3.2). Corregido en el documento maestro. |
| El documento daba el área activa como y 5.0–26.7. | Con la cabeza corregida, el área activa es **y 5.6–26.7**. |
| El brazo de «Me sumo» arrancaba exactamente en x = 0 (cap redondo a medio recortar). | El brazo arranca en **x = −1.4**, fuera del `viewBox`: entra desde el borde con corte limpio. |
| Los SVG no traían `aria-label`/`role="img"` ni se verificaban. | Todos los maestros incluyen `role="img"` + `aria-label`; la verificación lo comprueba. |

### Añadido

- `scripts/build_assets.py`: PNG a tamaño exacto en cuatro tintas
  (`ink`, `teal`, `violet`, `white`), con alfa.
- `scripts/build_sticker.py`: sticker animado frame a frame (misma curva de
  easing que el SMIL) en WebP animado + GIF, y WebP estático.
- `scripts/verify_geometry.py`: 178 comprobaciones y acta en
  `docs/verificacion-geometrica.md`.
- `scripts/make_preview.py`: `preview/preview.html` autocontenido y
  `preview/contact-sheet.png`.
- `Makefile` con `setup / assets / sticker / verify / preview / all / zip`.
- `README.md`, `DOCUMENTO-MAESTRO.md` (v1.1) y este changelog.

### Publicación abierta — 2026-11-16

- Licencias definitivas: **arte y documentación CC BY 4.0**; **código MIT**.
  Textos completos en `LICENSE` y `LICENSE-ARTWORK`; resumen en `LICENCIA.md`.
- `ATRIBUCION.md` con fórmulas de crédito listas para web, video, impresión y
  derivados.
- Repositorio público: <https://github.com/osarevalo/solidaridad-emoticon>
  (release v1.1.0 con el ZIP).
- Sin cambios de dibujo ni de assets: la geometría verificada sigue idéntica.

### Decisiones de producción

- **B (silueta) se usa en 16 y 20 px; A (trazo) desde 24 px.** El borrador
  tenía una contradicción entre §9.1 y §10.3; se resuelve a favor de la tabla
  de exportación y de la legibilidad medida a 20 px.
- **Sticker monócromo** en las tintas de chat (ink) para que la plataforma lo
  recoloree o lo use tal cual; las tintas de marca quedan en PNG/SVG.
- **Licencias abiertas:** arte CC BY 4.0 + código MIT (ver «Publicación abierta»).
