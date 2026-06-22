# Cantina Collectibles — catálogo Star Wars

## Qué hay en esta carpeta
- `index.html`  → el sitio (liviano, ~20 KB). Las fotos NO van adentro; las llama de `img/`.
- `img/`        → todas las fotos (una o varias por pieza, ej. `001-1.jpg`, `001-2.jpg`).
- `products.json` → los datos del catálogo (nombre, línea, año, tipo, episodio, precio, condición, fotos).
- `build_site.py` → regenera `index.html` a partir de `products.json`.

## Para ver el sitio
Abre `index.html` con doble clic. Tiene que estar en la misma carpeta que `img/`.

## Para subirlo a GitHub Pages
1. En tu repo: **Add file → Upload files**.
2. Arrastra el `index.html` Y la carpeta `img/` completa (GitHub conserva la estructura).
3. **Commit changes**. Espera 1–2 min y refresca fuerte.

## Para añadir figuras nuevas
1. Saca fotos sobre fondo blanco (sábana). Frente + dorso + detalles de daño.
2. Mételas en una carpeta y pásalas a la PC.
3. Por cada pieza nueva: añade un objeto a `products.json` con el próximo id (038, 039, ...)
   y guarda sus fotos en `img/` como `038-1.jpg`, `038-2.jpg`, etc.
4. Corre `python build_site.py` para regenerar `index.html`.
5. Sube a GitHub.

### Formato de cada pieza en products.json
{"id":"038","name":"...","line":"...","year":"2005","cat":"Figures",
 "ep":"III","price":20,"offer":true,"cond":"...","photos":["img/038-1.jpg","img/038-2.jpg"]}
- cat: Figures / Vehicles / Games / Oddities / Print
- ep:  I / II / III / IV / V / VI / Saga
- price: número (o null = "Make offer")

## Usarlo con Claude Cowork (recomendado para las 50+ que faltan)
Abre esta carpeta en Cowork y pídele algo como:
"Aquí está mi carpeta de fotos nuevas en [ruta]. Para cada pieza: identifícala,
busca precio de venta, recorta/optimiza la foto, guárdala en img/ con el próximo id,
añade la entrada a products.json y corre build_site.py."
Cowork puede leer la carpeta de fotos y editar estos archivos directamente.
