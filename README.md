# Mundial 2026 Byron

Esta carpeta contiene la app lista para editar en Visual Studio Code.

## Archivos principales

- `index.html`: aqui esta casi todo el codigo de la app: diseno, botones, tablas, grupos, partidos y logica.
- `manifest.webmanifest`: datos para que el navegador la pueda instalar como app.
- `service-worker.js`: permite que la app cargue mejor y tenga soporte basico sin conexion.
- `icon.svg`: icono de la app.
- `run_app.py`: abre la app con Python para probar cambios localmente.

## Como abrirla en Visual Studio Code

1. Abre Visual Studio Code.
2. Ve a `File > Open Folder`.
3. Selecciona esta carpeta: `mundial-2026-byron-app`.
4. Abre `index.html` para cambiar textos, colores, equipos o funciones.

## Como probarla con Python

En la terminal de Visual Studio Code, dentro de esta carpeta, ejecuta:

```bash
python run_app.py
```

Si en tu equipo Python se llama `py`, usa:

```bash
py run_app.py
```

Luego abre:

```text
http://127.0.0.1:8000/index.html
```

## Donde cambiar tu nombre

Busca la palabra `Byron` dentro de `index.html` y cambia lo que quieras.

## Donde cambiar colores

En `index.html`, al inicio del bloque `<style>`, busca variables como:

```css
--pitch-1
--bg
--card
--neon
--gold
```

Esas controlan los colores principales.

## Donde cambiar equipos

En `index.html`, busca:

```js
const GROUPS
```

Ahí estan los grupos y selecciones.
