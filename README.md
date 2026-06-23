# Cantina Collectibles — catálogo Star Wars

Catálogo web de mi colección de Star Wars en venta. **Venta local en San Juan, Puerto Rico.**

🌐 **Sitio en vivo:** https://estebi123.github.io/star-wars-collection-/

El sitio tiene buscador, filtros por tipo y episodio, galería de fotos, y un
selector de idioma **Español / Inglés** (por defecto en Español).

## Qué hay en esta carpeta
- `index.html` → el sitio (liviano; las fotos NO van adentro, las llama de `img/`).
- `img/` → todas las fotos (una o varias por pieza, ej. `001-1.jpg`, `001-2.jpg`).
- `products.json` → los datos del catálogo (nombre, línea, año, tipo, episodio, precio, condición, fotos).
- `build_site.py` → regenera `index.html` a partir de `products.json`.
- `CLAUDE.md` → notas del proyecto para Claude/Cowork.
- `.github/workflows/build.yml` → regenera el sitio automáticamente al subir cambios.

## Cómo cambiar un precio
1. Abre `products.json` y busca la pieza por su `id` (ej. `"id":"043"`).
2. Cambia el número en `"price"`.
3. Haz **commit** del `products.json`. La GitHub Action regenera el `index.html` sola
   (espera 1–2 min y refresca el sitio).
   - Si prefieres hacerlo manual: corre `python build_site.py` y sube el `index.html`.

## Cómo añadir una pieza nueva
1. Saca fotos sobre fondo blanco (frente + dorso + detalles). Pásalas a la PC.
2. Optimízalas (~1100px) y guárdalas en `img/` con el próximo id (`117-1.jpg`, ...).
3. Añade un objeto a `products.json` con el mismo formato que los demás.
4. Sube `products.json` y las fotos nuevas a GitHub (el `index.html` se regenera solo).

> 💡 Tip: abre esta carpeta en **Claude Cowork** y pídele que añada las piezas nuevas;
> lee este README y el `CLAUDE.md` y sigue las convenciones automáticamente.

## Formato de cada pieza en products.json
```json
{"id":"117","name":"...","line":"...","year":"2005","cat":"Figures",
 "ep":"III","price":16,"offer":false,"cond":"...","photos":["img/117-1.jpg","img/117-2.jpg"]}
```
- `cat`: Figures / Vehicles / Games / Oddities / Print
- `ep`:  I / II / III / IV / V / VI / Saga
- `price`: número (o `null` = "Make offer")
