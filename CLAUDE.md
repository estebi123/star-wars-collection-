# CLAUDE.md — Cantina Collectibles

Memoria del proyecto para Claude / Cowork. Léeme antes de hacer cambios.

## Qué es esto
Catálogo web estático de una colección de Star Wars en venta. Venta **local en
Puerto Rico (San Juan), en persona, sin envío**. Publicado con GitHub Pages en:
https://estebi123.github.io/star-wars-collection-/

## Archivos
- `products.json` — los datos del catálogo (la fuente de verdad). Editar aquí.
- `build_site.py` — genera `index.html` a partir de `products.json`. Correr tras editar.
- `index.html` — el sitio generado (NO editar a mano; se regenera).
- `img/` — fotos optimizadas (~1100px de lado largo, JPEG ~85). Una o varias por pieza
  (`001-1.jpg`, `001-2.jpg`, ...). El frente es `-1`, dorso `-2`, detalle `-3`.
- `.github/workflows/build.yml` — al hacer push de `products.json` o `build_site.py`,
  regenera y commitea `index.html` automáticamente.

## Esquema de cada pieza en products.json
{"id":"117","name":"...","line":"...","year":"2005","cat":"Figures",
 "ep":"III","price":16,"offer":false,"cond":"...","photos":["img/117-1.jpg","img/117-2.jpg"]}
- `cat`: Figures / Vehicles / Games / Oddities / Print
- `ep`:  I / II / III / IV / V / VI / Saga
- `price`: número (o null = "Make offer")
- `offer`: actualmente **false** en todas (el "or best offer" está apagado).
- `cond`: texto en inglés. Debe existir su traducción en el dict `COND_ES` de build_site.py.

## Idiomas
El sitio tiene selector ES/EN (por defecto Español, recuerda la elección).
- Nombres de piezas (`name`) y líneas (`line`) se quedan en INGLÉS (nombres propios oficiales).
- Las condiciones (`cond`) se traducen vía el dict `COND_ES` en build_site.py.
  Si añades una pieza con una `cond` nueva, AÑADE su traducción a COND_ES.

## Reglas de precio (decisiones del dueño)
- **No bajar precios.** Subir solo cuando el mercado claramente lo justifique.
- Venta local PR sin envío: el comparable de eBay debe incluir $20–35 de envío a PR,
  así que los precios locales suelen estar bien aunque superen el precio "pelado" de eBay.
- Precios son estimados estilo catálogo / valor de mercado aproximado.

## Para añadir una pieza nueva
1. Optimiza las fotos a ~1100px y guárdalas en `img/` con el próximo id.
2. Añade el objeto a `products.json` (mismo esquema).
3. Si la `cond` es nueva, añade su traducción a `COND_ES` en build_site.py.
4. `python build_site.py` (o solo haz push: la GitHub Action lo regenera).
5. Sube `products.json`, las fotos y `index.html` a GitHub.

## Para publicar
GitHub Pages sirve desde la rama `main`. Tras subir cambios, espera 1–2 min y refresca.
