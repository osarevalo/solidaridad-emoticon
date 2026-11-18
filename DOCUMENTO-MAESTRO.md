# Emoticón «Solidaridad» — documento maestro de diseño

> **Nombre:** Solidaridad · «Me solidarizo con vos» · «Hombro con hombro»
> **Estado:** diseño aprobado y **terminado** · paquete de producción v1.3.0
> **Versión del documento:** 1.3 · 2026-11-18
> **Formato maestro:** SVG · `viewBox="0 0 32 32"`
> **Uso:** documento único y autocontenido. Contiene brief, brainstorming,
> decisión, correcciones de ejecución, geometría verificada, código fuente,
> plan de exportación, handoff y próximos pasos.
> **Licencias:** arte y documentación CC BY 4.0 · código MIT
> (`LICENSE-ARTWORK`, `LICENSE`). Repositorio:
> <https://github.com/osarevalo/solidaridad-emoticon>.

Este documento cierra el borrador v1.0 redactado en DeepSeek. Al llevar el
diseño a SVG renderizado se detectaron cuatro defectos de ejecución que el
borrador no podía ver (cabezas en anillo, nudo central, «goteo» en la base y
cifras de separación incorrectas). Están corregidos, documentados en el
[CHANGELOG](CHANGELOG.md) y comprobados por `scripts/verify_geometry.py`
(547 comprobaciones, 0 fallas). La versión 1.2 agrega la **serie alternativa
«Abrazo»** (§15) y la 1.3 la serie **«Corazón»** (§16): la serie original con un
corazón entre las dos figuras. Ambas son series adicionales; la original no
cambia.

---

## Índice

1. [Brief y objetivo](#1--brief-y-objetivo)
2. [Criterios de diseño](#2--criterios-de-diseño)
3. [Lluvia de ideas (12 conceptos)](#3--lluvia-de-ideas-12-conceptos)
4. [Finalistas y decisión](#4--finalistas-y-decisión)
5. [Del boceto al archivo final: correcciones de ejecución](#5--del-boceto-al-archivo-final-correcciones-de-ejecución)
6. [Geometría final verificada](#6--geometría-final-verificada)
7. [Código fuente de los cinco SVG](#7--código-fuente-de-los-cinco-svg)
8. [Sticker animado](#8--sticker-animado)
9. [Plan de exportación](#9--plan-de-exportación)
10. [Hoja de especificaciones (handoff)](#10--hoja-de-especificaciones-handoff)
11. [Qué NO hacer](#11--qué-no-hacer)
12. [Verificación](#12--verificación)
13. [Próximos pasos](#13--próximos-pasos)
14. [Changelog](#14--changelog)
15. [Serie alternativa «Abrazo»](#15--serie-alternativa-abrazo)
16. [Serie «Corazón»](#16--serie-corazón)

---

## 1 · Brief y objetivo

Se necesita un emoticón que simbolice **la solidaridad**: un «me solidarizo con
vos» o «me solidarizo con esta causa».

**Principio rector:** evitar que el ícono se lea como **caridad desde arriba**.
La solidaridad se comunica como **horizontalidad, acompañamiento y suma**, no
como rescate ni asistencia.

**Diferenciación obligatoria** respecto de emojis existentes:

| Emoji existente | Lectura actual |
|---|---|
| 🤝 | Acuerdo / trato |
| 🫶 | Corazón con manos / cariño |
| 🫂 | Abrazo / consuelo |

El nuevo ícono ocupa un espacio semántico distinto: **presencia sostenida junto
a otro**, no acuerdo ni afecto romántico.

---

## 2 · Criterios de diseño

- **Mismo nivel.** Manos y figuras a la misma altura, sin jerarquía visual.
- **Mutualidad.** Debe leerse «estoy con vos», no «te rescato».
- **Legibilidad a 16 × 16 px.** Silueta simple, pocos elementos, sin detalles finos.
- **Funciona en monocromo.** No depender del color para transmitir el significado.
- **Inclusivo.** Figuras abstractas, sin género, edad ni raza explícitos.
- **Diferenciado.** No confundirse con 🤝, 🫶 ni 🫂.
- **Implementable.** Debe sobrevivir al render real a 16, 24 y 32 px.

---

## 3 · Lluvia de ideas (12 conceptos)

| # | Concepto | Descripción visual | Lectura |
|---|---|---|---|
| 1 | **Hombro con hombro** | Dos figuras abstractas lado a lado, un brazo sobre el hombro del otro, pequeño corazón o línea en el punto de unión | «No estás solo/a» |
| 2 | **Manos al mismo nivel** | Dos manos abiertas, simétricas, sosteniendo juntas un corazón/estrella pequeña | Apoyo mutuo, no caridad |
| 3 | **Paraguas compartido** | Dos siluetas bajo un mismo paraguas; lluvia solo afuera | Refugio compartido |
| 4 | **Cadena de manos** | Círculo de brazos/manos entrelazados, estilo pictograma | Comunidad / solidaridad colectiva |
| 5 | **Puente de manos** | Dos manos que se encuentran y forman un pequeño puente | Unir distancias |
| 6 | **Círculos intersectados** | Dos círculos que se superponen; en la intersección, un corazón | «Mi causa se cruza con la tuya» |
| 7 | **Raíces entrelazadas** | Dos tallos/raíces que se sostienen bajo tierra | Apoyo invisible y profundo |
| 8 | **Fuego compartido** | Dos manos protegen una llama común | Cuidar una causa / lucha |
| 9 | **Abrigo compartido** | Una prenda cubre dos hombros | Solidaridad práctica |
| 10 | **Empujar juntos** | Dos figuras empujando una misma puerta/caja | Esfuerzo colectivo |
| 11 | **Brazo en hombro mutuo** | Dos figuras con brazos cruzados por detrás, gesto recíproco | Acompañamiento |
| 12 | **Mano que se suma** | Una mano ya tomando otra, y una tercera mano acercándose al grupo | «Me sumo» |

---

## 4 · Finalistas y decisión

### Finalistas

1. **Hombro con hombro** — Dos figuras abstractas, mismo tamaño, brazos
   entrelazados y un corazón mínimo en la unión. El más directo para «me
   solidarizo con vos».
2. **Manos al mismo nivel sosteniendo un corazón** — Muy legible, pero requiere
   diferenciación explícita de 🫶: manos **abiertas y horizontales**,
   sosteniendo, no formando el corazón.
3. **Paraguas compartido** — Muy claro para causas/crisis, pero puede leerse
   como protección paternalista. Funciona solo si las dos figuras son iguales y
   están hombro con hombro.

### Decisión

**Concepto elegido: «Hombro con hombro».**

Pictograma de **dos siluetas idénticas que se inclinan una hacia la otra hasta
tocar el hombro**. Sin corazón, sin flechas: la solidaridad está en el contacto
y en la simetría.

- El **corazón se descartó a propósito** (ver §11): sobre o entre las cabezas el
  ícono se lee como «pareja».
- **Los hombros se tocan, las cabezas no.** Ese es el gesto: presencia física
  compartida sin fusión de identidades.

---

## 5 · Del boceto al archivo final: correcciones de ejecución

El borrador v1.0 definía la idea, pero algunas decisiones solo se pueden juzgar
al renderizar el SVG a tamaño real. Estas son las correcciones aplicadas en la
versión de producción:

| # | Lo que decía / hacía el borrador | Lo que mostró el render | Corrección aplicada |
|---|---|---|---|
| 1 | Cabeza como `<circle r="2.6"/>` dentro de un grupo con `stroke-width="2.4"` y sin relleno. | A 32 px las cabezas se veían como **anillos/donuts**, no como cabezas. | Cabeza rellena (`fill="currentColor"`) con `stroke-width="1.2"`; radio visual 3.2, igual en A y B. |
| 2 | Cuerpos terminaban en 16.04 / 15.96 (desfase de 0.08 para que «se tocaran»). | El cruce de los dos trazos dejaba un **nudo** sucio en el centro. | Las dos figuras comparten exactamente el punto **(16, 17.5)**; el cruce queda limpio y la simetría sigue siendo exacta. |
| 3 | Patas internas en 14.8 / 17.2. | A 32 px el hueco central se cerraba y parecía un **«goteo»** colgando entre los cuerpos. | Base interior en **13.6 / 18.4**: los cuerpos se separan bajo el hombro y el hueco respira. |
| 4 | «Gap de cabezas ≈ 1.8 u (visual ≈ 1.0)» y «área activa y 5.0–26.7». | Medición real: hueco **2.0 u**; área activa **y 5.6–26.7**. | Cifras corregidas en §6; el borrador no se copia, se recalcula. |
| 5 | Brazo de «Me sumo» arrancando en x = 0. | El cap redondo quedaba medio recortado en el borde. | El brazo arranca en **x = −1.4**, fuera del `viewBox`, y entra con corte limpio. |

La regla que no cambió: **los hombros se tocan, las cabezas no.**

---

## 6 · Geometría final verificada

Medidas recalculadas por `scripts/verify_geometry.py` a partir de los SVG
(no transcritas a mano). El acta completa con las 178 comprobaciones está en
[`docs/verificacion-geometrica.md`](docs/verificacion-geometrica.md).

| Parámetro | Valor |
|---|---|
| Canvas | 32 × 32 |
| `viewBox` | `0 0 32 32` |
| Punto de contacto de hombros | **(16.0, 17.5)** — exacto, compartido por los dos cuerpos |
| Cabeza | r 2.6 · cy 8.8 · cx 11.8 (izq.) / 20.2 (der.) |
| Radio visual de cabeza | 3.2 (relleno 2.6 + trazo 1.2 / 2) |
| Hueco entre cabezas | **2.0 u** (centros a 8.4 u) |
| Cúpula del hombro (línea central) | y ≈ 12.4975 en t = 0.5 |
| Solape cabeza–hombro | 0.70 u en A · 0.10 u en B (cuello unido, no flotante) |
| Trazo A | 2.4 · `stroke-linecap="round"` + `stroke-linejoin="round"` |
| Trazo B | relleno sólido + `stroke-width="1.2"` |
| Base interior | 13.6 / 18.4 |
| Área activa A | x 3.6–28.4 · y 5.6–26.7 |
| Área activa B | x 4.2–27.8 · y 5.6–26.1 |
| Área activa «Misma causa» | x 3.6–28.4 · y 5.6–28.0 (línea de suelo) |
| «Me sumo» | el brazo desborda a propósito hasta x = −2.6; el `viewBox` lo recorta en 0 |
| Simetría | espejo exacto sobre `x = 16` |
| Sticker | translate ±10 u → overshoot ±0.6 u → 0; 550 ms; splines `0.16 1 0.3 1` y `0.4 0 0.2 1` |

**Regla de oro:** si las cabezas se tocan, se lee «pareja». Si los hombros no se
tocan, se lee «dos personas». La tensión entre ambos extremos es el diseño.

---

## 7 · Código fuente de los cinco SVG

Los maestros no llevan color fijo: usan `currentColor`. No tienen `width` ni
`height`, para que escalen desde CSS. Todos llevan `role="img"` y `aria-label`.

### 7.1 · Versión A — trazo (`src/solidaridad.svg`, ≥ 24 px)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" fill="none" role="img" aria-label="Me solidarizo con vos">
  <g stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">
    <path d="M4.8 25.5 L6.04 17.5 C7.07 10.83 17.07 10.83 16 17.5 L13.6 25.5"/>
    <circle cx="11.8" cy="8.8" r="2.6" fill="currentColor" stroke-width="1.2"/>
    <path d="M27.2 25.5 L25.96 17.5 C24.93 10.83 14.93 10.83 16 17.5 L18.4 25.5"/>
    <circle cx="20.2" cy="8.8" r="2.6" fill="currentColor" stroke-width="1.2"/>
  </g>
</svg>
```

### 7.2 · Versión B — silueta (`src/solidaridad-fill.svg`, 16 y 20 px)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" fill="currentColor" stroke="currentColor"
     stroke-width="1.2" stroke-linejoin="round" role="img" aria-label="Me solidarizo con vos">
  <path d="M4.8 25.5 L6.04 17.5 C7.07 10.83 17.07 10.83 16 17.5 L13.6 25.5 Z"/>
  <circle cx="11.8" cy="8.8" r="2.6"/>
  <path d="M27.2 25.5 L25.96 17.5 C24.93 10.83 14.93 10.83 16 17.5 L18.4 25.5 Z"/>
  <circle cx="20.2" cy="8.8" r="2.6"/>
</svg>
```

### 7.3 · «Me sumo» (`src/solidaridad-me-sumo.svg`, ≥ 24 px)

Par base + brazo que entra desde el borde izquierdo y apoya la mano en el
hombro: «alguien más se acerca».

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" fill="none" role="img" aria-label="Me sumo">
  <g stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">
    <path d="M4.8 25.5 L6.04 17.5 C7.07 10.83 17.07 10.83 16 17.5 L13.6 25.5"/>
    <circle cx="11.8" cy="8.8" r="2.6" fill="currentColor" stroke-width="1.2"/>
    <path d="M27.2 25.5 L25.96 17.5 C24.93 10.83 14.93 10.83 16 17.5 L18.4 25.5"/>
    <circle cx="20.2" cy="8.8" r="2.6" fill="currentColor" stroke-width="1.2"/>
    <path d="M-1.4 22.5 C0.3 19.8 3.1 17.6 6.8 16.9"/>
  </g>
</svg>
```

> El brazo arranca en x = −1.4 a propósito: el `viewBox` lo recorta y la mano
> entra desde el borde sin un cap redondo a medio dibujar.

### 7.4 · «Misma causa» (`src/solidaridad-causa.svg`, ≥ 24 px)

Par base + línea de suelo compartida: «misma base / misma causa».

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" fill="none" role="img" aria-label="Misma causa">
  <g stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">
    <path d="M4.8 25.5 L6.04 17.5 C7.07 10.83 17.07 10.83 16 17.5 L13.6 25.5"/>
    <circle cx="11.8" cy="8.8" r="2.6" fill="currentColor" stroke-width="1.2"/>
    <path d="M27.2 25.5 L25.96 17.5 C24.93 10.83 14.93 10.83 16 17.5 L18.4 25.5"/>
    <circle cx="20.2" cy="8.8" r="2.6" fill="currentColor" stroke-width="1.2"/>
    <path d="M6.5 26.8 H25.5"/>
  </g>
</svg>
```

> Alternativa descartada: bandera entre las cabezas. El hueco real es de 2.0 u y
> la bandera se convierte en mancha por debajo de 32 px.

### 7.5 · Sticker animado (`src/solidaridad-sticker.svg`)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" fill="none" role="img" aria-label="Me solidarizo con vos">
  <g stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">
    <g>
      <animateTransform attributeName="transform" type="translate"
        values="-10 0; 0.6 0; 0 0" keyTimes="0;0.75;1" dur="0.55s"
        calcMode="spline" keySplines="0.16 1 0.3 1;0.4 0 0.2 1" fill="freeze"/>
      <path d="M4.8 25.5 L6.04 17.5 C7.07 10.83 17.07 10.83 16 17.5 L13.6 25.5"/>
      <circle cx="11.8" cy="8.8" r="2.6" fill="currentColor" stroke-width="1.2"/>
    </g>
    <g>
      <animateTransform attributeName="transform" type="translate"
        values="10 0; -0.6 0; 0 0" keyTimes="0;0.75;1" dur="0.55s"
        calcMode="spline" keySplines="0.16 1 0.3 1;0.4 0 0.2 1" fill="freeze"/>
      <path d="M27.2 25.5 L25.96 17.5 C24.93 10.83 14.93 10.83 16 17.5 L18.4 25.5"/>
      <circle cx="20.2" cy="8.8" r="2.6" fill="currentColor" stroke-width="1.2"/>
    </g>
  </g>
</svg>
```

---

## 8 · Sticker animado

Las figuras entran desde los bordes, hacen contacto y hay un **overshoot de
0.6 u** que se asienta: lee como «choque de hombros» en vez de «deslizamiento».
Duración total **550 ms**. La pausa inicial y final alarga el bucle a ≈ 1.08 s.

### Equivalente CSS (para web)

Los valores están en unidades del `viewBox`; hay que escalarlos al tamaño real
con `transform: translateX(calc(...))` o mediante un contenedor con
`transform: scale()`. Ejemplo para 32 px (1 u = 1 px):

```css
@keyframes sol-izq { 0% { transform: translateX(-10px); } 75% { transform: translateX(.6px); } 100% { transform: translateX(0); } }
@keyframes sol-der { 0% { transform: translateX(10px); }  75% { transform: translateX(-.6px); } 100% { transform: translateX(0); } }
.sol-izq { animation: sol-izq .55s cubic-bezier(.16,1,.3,1) forwards; }
.sol-der { animation: sol-der .55s cubic-bezier(.16,1,.3,1) forwards; }
@media (prefers-reduced-motion: reduce) {
  .sol-izq, .sol-der { animation: none; }
}
```

> Nota: `cubic-bezier(.16,1,.3,1)` reproduce el tramo rápido; el segundo tramo
> (`0.4 0 0.2 1`) solo se usa en el SMIL para el asentamiento. Para la web, el
> resultado visual es equivalente al SVG animado.

### Exportación animada

- `dist/sticker/animado/solidaridad-sticker-animado_512.webp` — **recomendado**
  (alfa real, bucle, 512 × 512, ~144 KB).
- `dist/sticker/animado/solidaridad-sticker-animado_256.webp` — variante ligera.
- `dist/sticker/animado/solidaridad-sticker-animado_512.gif` — compatibilidad
  (paleta de 255 colores + transparencia).

El build reproduce el easing frame a frame en Python, de modo que WebP/GIF
coinciden con el SVG. Los frames idénticos se fusionan con su duración (15
frames únicos de los 28 nominales).

---

## 9 · Plan de exportación

### 9.1 · Set de tamaños

| Tamaño | Versión | Uso |
|---|---|---|
| 16 px | B (silueta) | bandeja de emojis, favicon |
| 20 px | B (silueta) | UI compacta |
| 24 px | A (trazo) | UI estándar |
| 32 px | A (trazo) | maestro de referencia |
| 48 px | A (trazo) | reacciones, Slack / Discord |
| 64 px | A (trazo) | stickers |
| 128 px | A (trazo) | web / marketing |
| 256 px | A (trazo) | retina |
| 512 px | A (trazo) | app store, prensa, sticker |

**Regla resuelta:** B en **16 y 20 px**; A desde **24 px**. La familia extendida
(«Me sumo», «Misma causa»), la serie «Abrazo» y la serie «Corazón» solo desde
24 px (salvo la B de 16/20 de Corazón). El borrador se
contradecía entre §9.1 y §10.3; manda la legibilidad medida.

### 9.2 · Tintas

| Tinta | Hex | Uso |
|---|---|---|
| ink | `#1F2933` | por defecto (texto/UI) |
| teal | `#2B7A78` | acento solidario |
| violet | `#8E44AD` | acento alternativo |
| white | `#FFFFFF` | fondos oscuros |

Monocromo por uso: **nunca** dos tintas simultáneas en el mismo glifo. Los SVG
maestros usan `currentColor`; las tintas viven en el build (`dist/png/<tinta>/`).

### 9.3 · Convención de nombres

```text
solidaridad_{size}.png                 # A, tamaño exacto
solidaridad-fill_{16,20}.png           # B
solidaridad-me-sumo_{size}.png
solidaridad-causa_{size}.png
solidaridad-sticker_{128,256,512}.png  # pose final
solidaridad-sticker-animado_{256,512}.webp
solidaridad-sticker-animado_512.gif
```

### 9.4 · Comandos de conversión

Los SVG son los maestros; los PNG se generan en el build:

```bash
make setup     # .venv + cairosvg + pillow
make assets    # PNG de las 4 tintas + WebP estáticos
make sticker   # WebP animado + GIF
make verify    # geometría + integridad de la exportación
make preview   # hoja de contactos + preview.html
make all
```

Para un uso puntual sin el build:

```bash
cairosvg src/solidaridad.svg -o solidaridad_128.png -s 4   # 32 × 4 = 128 px
```

(cairosvg escala por múltiplo del `viewBox`: 32 → 128 = factor 4.)

### 9.5 · Estructura de entregables

```text
solidaridad-emoticon/
  src/                         5 SVG maestros
  dist/png/{ink,teal,violet,white}/   tamaño exacto, alfa
  dist/sticker/{tinta}/         PNG + WebP estático 128/256/512
  dist/sticker/animado/         WebP animado 256/512 + GIF 512
  preview/preview.html          vista previa autocontenida
  preview/contact-sheet.png     hoja de contactos
  docs/verificacion-geometrica.md
  DOCUMENTO-MAESTRO.md
  README.md · CHANGELOG.md · LICENCIA.md
  LICENSE · LICENSE-ARTWORK · ATRIBUCION.md
```

---

## 10 · Hoja de especificaciones (handoff)

### 10.1 · Identidad

| Campo | Valor |
|---|---|
| Nombre | Solidaridad · «Me solidarizo con vos» |
| Shortcodes | `:solidaridad:` `:con-vos:` `:hombro-con-hombro:` |
| Categoría | Personas / vínculos |
| `aria-label` | «Me solidarizo con vos» (familia: «Me sumo», «Misma causa») |
| Variantes | A (trazo), B (silueta), «Me sumo», «Misma causa», sticker |

### 10.2 · Geometría (unidades del `viewBox`)

| Elemento | Valor |
|---|---|
| Canvas | 32 × 32 · `viewBox="0 0 32 32"` |
| Área activa A | x 3.6–28.4 · y 5.6–26.7 |
| Trazo A | 2.4 · round cap + round join |
| Trazo B | relleno + 1.2 · round join |
| Cabeza | r 2.6 · cy 8.8 · cx 11.8 / 20.2 · radio visual 3.2 |
| Cuerpo izq. | `M4.8 25.5 L6.04 17.5 C7.07 10.83 17.07 10.83 16 17.5 L13.6 25.5` |
| Cuerpo der. | `M27.2 25.5 L25.96 17.5 C24.93 10.83 14.93 10.83 16 17.5 L18.4 25.5` |
| Contacto hombros | (16.0, 17.5) — exacto, compartido |
| Hueco de cabezas | 2.0 (visual; centros a 8.4) |
| Simetría | espejo exacto sobre x = 16 |

### 10.3 · Reglas de tamaño

- ≥ 24 px → Versión A (trazo).
- 16–20 px → Versión B (silueta); switch automático por tamaño.
- ≥ 24 px → habilitar familia extendida.
- < 24 px → **prohibido** «Me sumo» y «Misma causa».

### 10.4 · Color

- Token: `currentColor`. Nunca hardcodear en el SVG maestro.
- Monocromo únicamente.
- Prohibido bicolor contrastante (lee «dos bandos») y degradados (ruido a 16 px).
- Variantes de tinte único: `#1F2933`, `#2B7A78`, `#8E44AD`, `#FFFFFF`.

### 10.5 · Accesibilidad

- Siempre `role="img"` + `aria-label`.
- Decorativo → `aria-hidden="true"` en el contenedor.
- Sticker: respetar `prefers-reduced-motion` (equivalente CSS incluido).
- El significado no depende del color: funciona en monocromo.

### 10.6 · Integración web

```html
<!-- Ícono de reacción -->
<button class="reaccion" aria-label="Me solidarizo con vos">
  <svg class="icono" role="img" aria-label="Me solidarizo con vos" viewBox="0 0 32 32">
    <!-- contenido de src/solidaridad.svg (sin el <svg> exterior) -->
  </svg>
</button>
```

```css
.icono { width: 24px; height: 24px; color: #1F2933; }
.reaccion:focus-visible { outline: 2px solid #2B7A78; outline-offset: 2px; }
```

React/JSX: el mismo SVG como componente con `className`, `role` y
`aria-label`; no usar `dangerouslySetInnerHTML` salvo que se sanitice.

### 10.7 · Sticker: plataformas

| Plataforma | Formato | Nota |
|---|---|---|
| WhatsApp | WebP animado 512 × 512 | límite de tamaño vigente ~500 KB; este sticker pesa ~144 KB |
| Telegram | WebP/PNG 512 × 512 | acepta GIF como respaldo |
| Slack / Discord | PNG 48–128 px | usar la versión A o B según tamaño |

Verificar los límites vigentes de cada plataforma al publicar.

### 10.8 · Licencias

| Contenido | Licencia |
|---|---|
| Arte (`src/`, `dist/`, `preview/`) y documentación | CC BY 4.0 |
| Código (`scripts/`, `Makefile`, `package.json`) | MIT |

Uso comercial permitido. El arte exige atribución (título, autor, fuente,
licencia), enlace a CC BY 4.0 e indicación de cambios; fórmulas listas en
`ATRIBUCION.md`. El código solo exige conservar el aviso MIT. Textos completos:
`LICENSE-ARTWORK` y `LICENSE`. Repositorio:
<https://github.com/osarevalo/solidaridad-emoticon>.

---

## 11 · Qué NO hacer

| Prohibido | Motivo |
|---|---|
| ❤️ sobre o entre las cabezas | Se lee pareja / amor, no solidaridad |
| Corazón entre las cabezas | No entra: el hueco real es de 2.0 u; se ve como una mancha |
| Figuras de distinta altura o tamaño | Introduce jerarquía → caridad, no solidaridad |
| Manos «sosteniendo» o «dando» | Se lee asistencia desde arriba |
| Brazos que no se tocan | Pierde el «estoy con vos» |
| Cabeza en anillo (trazo grueso sin relleno) | Se lee donut/aro, no cabeza |
| Contorno + relleno mezclados dentro de la misma versión | Inconsistencia a 16 px; A y B son las dos únicas variantes |
| Rotar las figuras fuera del eje | Rompe la tangencia de hombros |
| Bicolor contrastante | Lee «dos bandos», lo contrario de solidaridad |
| Degradados / sombras | Ruido a 16 px |

---

## 12 · Verificación

`scripts/verify_geometry.py` recalcula, no copia. Cubre:

1. **Maestros:** `viewBox`, `role`, `aria-label`, ausencia de `width`/`height`,
   ausencia de colores fijos, ausencia de scripts/recursos externos.
2. **Geometría:** simetría espejo exacta sobre x = 16, punto de contacto
   compartido (16, 17.5), cabeza (r, cy, cx), hueco de 2.0 u, solape
   cabeza–hombro, áreas activas y desbordes de caja.
3. **Sticker:** dos `animateTransform`, duración 0.55 s, overshoot ±0.6 u,
   splines declarados.
4. **Máscaras de «Abrazo»:** máscara declarada y referenciada, ids únicos,
   hueco de 4.8 u, mano de 3.1 u y brazo de 2.4 u con mano de 1.7 u.
5. **Exportación:** 296 PNG de familia (4 tintas × 74 tamaños) + 24 PNG de
   stickers (4 tintas × 3 tamaños × 2 stickers), todos a tamaño exacto y con
   alfa; regla B 16/20 vs A ≥ 24, serie Abrazo 24–512, serie Corazón B 16/20 y
   A 24–512, WebP animados 512 × 512, GIF, WebP estáticos, convención de nombres.

Resultado: **547 PASA · 0 FALLA**. Acta:
[`docs/verificacion-geometrica.md`](docs/verificacion-geometrica.md).

---

## 13 · Próximos pasos

Lo que queda es decisión y validación externa, no diseño:

- [x] **Licencia decidida:** arte y documentación **CC BY 4.0**, código **MIT**
      (`LICENSE-ARTWORK`, `LICENSE`). Repositorio público:
      <https://github.com/osarevalo/solidaridad-emoticon>.
- [x] **Serie «Abrazo» integrada** (v1.2.0): 4 glifos, 112 PNG, hoja propia y
      verificación de máscaras.
- [x] **Serie «Corazón» integrada** (v1.3.0): 5 glifos, 92 PNG + 12 de sticker,
      hoja propia y sticker animado.
- [ ] Revisión con lector de pantalla en contexto real (bandeja de emojis).
- [ ] Prueba de legibilidad a 16 px en pantalla no-retina.
- [ ] Si el sistema de íconos del producto usa grilla de 24 × 24, generar una
      variante con el mismo diseño sobre 24 (trazo ≈ 1.8, cabeza r ≈ 1.95).
- [ ] Validar el sticker en la plataforma destino (límites de tamaño/formato
      vigentes de WhatsApp/Telegram).
- [ ] Opcional: WebP animado en las tintas de marca (hoy el animado es ink).
- [ ] Opcional: variante bicolor **solo** si una marca la exige; hoy está
      prohibida por diseño.

---

## 14 · Changelog

| Versión | Cambio |
|---|---|
| 1.0 | Documento maestro inicial (DeepSeek). Concepto «Hombro con hombro». Geometría «a ojo»: cabezas con trazo 2.4, unión 16.04/15.96, base 14.8/17.2, gap 1.8. |
| 1.1 | Cierre de producción: cabezas rellenas (trazo 1.2), unión exacta (16, 17.5), base 13.6/18.4, gap real 2.0, brazo de «Me sumo» desde x = −1.4, `role`/`aria-label`, 92 PNG de familia + 12 de sticker, WebP animado + GIF, verificación automática (178 comprobaciones), README, hoja de contactos y vista previa. Publicación abierta (2026-11-16): licencias CC BY 4.0 + MIT, repo público y release. |
| 1.2 | Serie alternativa «Abrazo»: 4 glifos nuevos (`abrazo`, `abrazo-me-sumo`, `abrazo-causa`, `abrazo-mutuo`), 112 PNG (4 tintas × 7 tamaños), hoja `contact-sheet-abrazo.png`, máscara knockout para el brazo, verificación ampliada a 364 comprobaciones y release v1.2.0. |
| 1.3 | Serie «Corazón»: 5 glifos con corazón centrado entre las figuras (A, B, me sumo, misma causa, sticker), 92 PNG + 12 de sticker, hoja `contact-sheet-corazon.png`, sticker animado con aparición del corazón, verificación ampliada a 547 comprobaciones y release v1.3.0. |

---

## 15 · Serie alternativa «Abrazo»

### 15.1 · Concepto

Cuatro glifos que leen el mismo vínculo desde otro gesto: **la figura izquierda
pasa el brazo por encima del hombro de la derecha y la mano queda visible al
otro lado**. Es una serie adicional; la serie original («Hombro con hombro») no
se modifica.

| Archivo | `aria-label` | Uso |
|---|---|---|
| `src/abrazo.svg` | Abrazo de apoyo | glifo principal |
| `src/abrazo-me-sumo.svg` | Abrazo, me sumo | alguien más se acerca |
| `src/abrazo-causa.svg` | Abrazo, misma causa | misma base / misma causa |
| `src/abrazo-mutuo.svg` | Abrazo mutuo | los dos brazos por encima |

### 15.2 · Técnica: máscara knockout

El brazo se dibuja con la misma tinta sobre el cuerpo derecho. Para que se lea
sin agregar un segundo color, el cuerpo derecho se recorta con una **máscara**
que deja **1.2 u de transparencia** a cada lado del brazo y de la mano:

- brazo: `M15.0 17.1 C18.0 13.4 22.9 13.0 26.6 15.4` · trazo 2.4 · round cap;
- mano: círculo r 1.7 en (26.6, 15.4);
- máscara: el mismo camino con trazo 4.8 y la mano con r 3.1;
- orden de capas: cuerpo derecho recortado → brazo → cuerpo izquierdo (así el
  inicio del brazo queda oculto detrás del hombro izquierdo).

El hueco es transparencia: sobre fondo claro se ve blanco y sobre fondo oscuro
se ve oscuro. No hay un segundo color en el SVG.

### 15.3 · Geometría y tamaños

La base es idéntica a la serie original: cabezas r 2.6 en (11.8/20.2, 8.8),
contacto de hombros (16, 17.5), base interior 13.6/18.4. La serie se exporta en
**24–512 px** (4 tintas × 4 glifos × 7 tamaños = 112 PNG). A 16/20 px no se
usa: ahí sigue la versión B de la serie original.

### 15.4 · Código maestro del glifo principal

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" fill="none" role="img" aria-label="Abrazo de apoyo">
  <defs>
    <mask id="abzMask" maskUnits="userSpaceOnUse" x="0" y="0" width="32" height="32">
      <rect x="0" y="0" width="32" height="32" fill="#fff"/>
      <path d="M15.0 17.1 C18.0 13.4 22.9 13.0 26.6 15.4" fill="none" stroke="#000"
            stroke-width="4.8" stroke-linecap="round" stroke-linejoin="round"/>
      <circle cx="26.6" cy="15.4" r="3.1" fill="#000"/>
    </mask>
  </defs>
  <g stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" mask="url(#abzMask)">
    <path d="M27.2 25.5 L25.96 17.5 C24.93 10.83 14.93 10.83 16 17.5 L18.4 25.5"/>
    <circle cx="20.2" cy="8.8" r="2.6" fill="currentColor" stroke-width="1.2"/>
  </g>
  <g stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">
    <path d="M15.0 17.1 C18.0 13.4 22.9 13.0 26.6 15.4" fill="none"/>
    <circle cx="26.6" cy="15.4" r="1.7" fill="currentColor" stroke="none"/>
  </g>
  <g stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">
    <path d="M4.8 25.5 L6.04 17.5 C7.07 10.83 17.07 10.83 16 17.5 L13.6 25.5"/>
    <circle cx="11.8" cy="8.8" r="2.6" fill="currentColor" stroke-width="1.2"/>
  </g>
</svg>
```

Las variantes están en `src/abrazo-me-sumo.svg`, `src/abrazo-causa.svg` y
`src/abrazo-mutuo.svg`; todas comparten la misma base y la misma máscara.

### 15.5 · Verificación

`make verify` comprueba para la serie: existencia, `viewBox`, `role`,
`aria-label`, ausencia de colores fijos fuera de `defs`, simetría de los cuerpos,
contacto de hombros, cabezas, área activa, frontera del `viewBox` (incluido el
brazo de «Me sumo» que entra desde fuera) y las máscaras (declarada,
referenciada, ids únicos, hueco y mano). Resultado global: **364 PASA · 0 FALLA**.

---

## 16 · Serie «Corazón»

### 16.1 · Concepto

Tercera serie: **la serie original con un corazón entre las dos figuras**. Es
una variante pedida de forma explícita; el corazón también se lee como afecto o
pareja, por eso queda separada de «Hombro con hombro» y no la sustituye.

| Archivo | `aria-label` | Uso |
|---|---|---|
| `src/corazon.svg` | Solidaridad con corazón | glifo principal A |
| `src/corazon-fill.svg` | Solidaridad con corazón | silueta B (16/20) |
| `src/corazon-me-sumo.svg` | Me sumo con corazón | alguien más se acerca |
| `src/corazon-causa.svg` | Misma causa con corazón | misma base / misma causa |
| `src/corazon-sticker.svg` | Solidaridad con corazón | sticker animado |

### 16.2 · Geometría y animación

- Corazón centrado en **(16, 11.4)** en A y **(16, 12.2)** en B, tamaño
  3.1 × 3.1 u, apoyado en el hueco entre las cabezas.
- En el sticker aparece a los **0.35 s**, con escala 0 → 1.2 → 1 y opacidad
  0 → 1; las figuras conservan la entrada desde los bordes del sticker original.
- Sin máscaras ni segundo color: es un path relleno con `currentColor`.

### 16.3 · Código maestro

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" fill="none" role="img" aria-label="Solidaridad con corazón">
  <g stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">
    <path d="M4.8 25.5 L6.04 17.5 C7.07 10.83 17.07 10.83 16 17.5 L13.6 25.5"/>
    <circle cx="11.8" cy="8.8" r="2.6" fill="currentColor" stroke-width="1.2"/>
    <path d="M27.2 25.5 L25.96 17.5 C24.93 10.83 14.93 10.83 16 17.5 L18.4 25.5"/>
    <circle cx="20.2" cy="8.8" r="2.6" fill="currentColor" stroke-width="1.2"/>

  </g>
  <g transform="translate(16 11.4) scale(1.0)"><path d="M0 1.55 C-0.9 0.75 -1.55 0.15 -1.55 -0.55 C-1.55 -1.15 -1.1 -1.55 -0.55 -1.55 C-0.25 -1.55 0 -1.35 0 -1.1 C0 -1.35 0.25 -1.55 0.55 -1.55 C1.1 -1.55 1.55 -1.15 1.55 -0.55 C1.55 0.15 0.9 0.75 0 1.55 Z" fill="currentColor"/></g>
</svg>
```

### 16.4 · Exportación

PNG de 16/20 (B) y 24–512 (A) en las cuatro tintas; sticker PNG/WebP estático
128/256/512 y WebP/GIF animado. La verificación comprueba el corazón centrado,
la animación y los mismos criterios de la serie original. Resultado global:
**547 PASA · 0 FALLA**.

---

*Documento único de trabajo · paquete v1.3.0 · listo para usar y para continuar.*
