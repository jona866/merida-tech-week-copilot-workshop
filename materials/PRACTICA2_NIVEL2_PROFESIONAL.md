# 🧱 Práctica 2 – Nivel 2: Portafolio “Profesional”

> 🔼 Extensión de la práctica 2 base.  
> En este nivel llevaremos tu portafolio desde una versión funcional a una **versión profesional**, con código más organizado, contenido dinámico y mejores prácticas de diseño.

---

## 🎯 Objetivos del nivel

1. Separar contenido y presentación utilizando **archivos JSON** para los proyectos.  
2. Mejorar el **diseño visual** y la **responsividad** del sitio.  
3. Añadir **metaetiquetas SEO** y elementos de **accesibilidad**.  
4. Aplicar buenas prácticas de **organización del código y optimización**.  

---

## 📁 Estructura esperada del proyecto

```bash
portafolio-ia-workshop/
│
├── index.html
├── styles.css
├── script.js
├── data/
│   └── projects.json         # Datos dinámicos de proyectos
├── notes.txt
└── README.md
````

---

## 🪜 Paso 1 – Crear `data/projects.json` (contenido dinámico)

🎯 **Objetivo:** separar el contenido de los proyectos en un archivo JSON que luego se cargará con JavaScript.

1. Crea una carpeta llamada `data/` en la raíz del proyecto.
2. Dentro de ella, crea el archivo `projects.json`.
3. Agrega el siguiente contenido de ejemplo:

```json
[
  {
    "title": "Dashboard del Clima",
    "description": "Aplicación web que muestra el clima actual y el pronóstico utilizando una API pública.",
    "technologies": ["HTML", "CSS", "JavaScript", "API REST"],
    "demoUrl": "https://ejemplo.com/dashboard-clima",
    "repoUrl": "https://github.com/usuario/dashboard-clima"
  },
  {
    "title": "Explorador de Películas",
    "description": "Buscador de películas que consume una API externa y muestra los resultados con información básica.",
    "technologies": ["JavaScript", "Fetch API", "CSS"],
    "demoUrl": "https://ejemplo.com/explorador-peliculas",
    "repoUrl": "https://github.com/usuario/explorador-peliculas"
  },
  {
    "title": "Notas Interactivas de IA",
    "description": "Sitio web con artículos cortos sobre inteligencia artificial y ejemplos interactivos.",
    "technologies": ["HTML", "CSS", "JavaScript"],
    "demoUrl": "https://ejemplo.com/ia-notes",
    "repoUrl": "https://github.com/usuario/ia-notes"
  }
]
```

💬 **Prompt para Copilot Chat:**

```text
Genera un archivo JSON llamado projects.json que contenga una lista de 3 a 5 proyectos personales.
Cada proyecto debe incluir título, descripción, lista de tecnologías, URL de demo y URL de repositorio.
Usa nombres y descripciones realistas para un estudiante de ingeniería de software.
```

---

## 🪜 Paso 2 – Conectar el archivo JSON con tu HTML

🎯 **Objetivo:** generar las tarjetas de proyectos dinámicamente desde el archivo JSON.

1. En tu `index.html`, ubica la sección de proyectos y reemplaza su contenido estático:

```html
<section id="proyectos" class="section">
  <h2>Proyectos</h2>
  <div class="projects-grid" id="projects-container">
    <!-- Las tarjetas se cargarán dinámicamente desde projects.json -->
  </div>
</section>
```

2. Abre `script.js` y agrega (o pide a Copilot que genere) una función para cargar los datos:

💬 **Prompt para Copilot Chat:**

```text
Agrega una función en JavaScript que:
- Haga fetch al archivo "./data/projects.json"
- Recorra la lista de proyectos
- Cree dinámicamente una tarjeta HTML por cada proyecto con su título, descripción y tecnologías
- Inserte las tarjetas dentro del contenedor con id="projects-container"
Usa comentarios en español para explicar cada paso.
```

3. Guarda y ejecuta el sitio.
   Si todo está correcto, las tarjetas se generarán automáticamente desde el JSON.

✅ **Resultado esperado:**
Cada vez que modifiques `projects.json`, los cambios se reflejarán automáticamente en el portafolio sin editar el HTML.

---

## 🪜 Paso 3 – Mejorar el diseño en `styles.css`

🎯 **Objetivo:** aplicar un diseño más moderno, limpio y totalmente responsive.

### 💬 Prompt 1: Actualizar paleta y tipografía

```text
Sugiere una paleta de colores moderna y profesional para este portafolio.
Actualiza las variables CSS en :root y aplica una tipografía agradable.
Usa comentarios en español para explicar cada color.
```

👉 Ejemplo de estructura que puedes incluir:

```css
:root {
  --bg: #0f172a;
  --text: #f1f5f9;
  --accent: #38bdf8;
  --card-bg: #1e293b;
  --card-border: #334155;
  --font-main: 'Poppins', sans-serif;
}
```

### 💬 Prompt 2: Layout responsive con Grid o Flexbox

```text
Refactoriza los estilos para que la cuadrícula de proyectos use CSS Grid.
Debe mostrar 1 columna en móviles, 2 en tablets y 3 en escritorio.
Agrega comentarios en español describiendo los breakpoints.
```

👉 Ejemplo:

```css
.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
}
```

### 💬 Prompt 3: Efectos e interactividad visual

```text
Agrega animaciones suaves al hacer hover sobre las tarjetas de proyectos.
Usa transform, box-shadow y transition para crear una sensación moderna.
```

---

## 🪜 Paso 4 – Mejorar SEO y accesibilidad

🎯 **Objetivo:** optimizar el sitio para buscadores y usuarios.

### 💬 Prompt para SEO básico

```text
Agrega metaetiquetas SEO al head del HTML:
- title y description
- og:title, og:description, og:type
- language (es)
Usa una descripción profesional y breve del portafolio.
```

👉 Ejemplo:

```html
<meta name="description" content="Portafolio de desarrollo web e inteligencia artificial creado con GitHub Copilot.">
<meta property="og:title" content="Portafolio de [Tu Nombre]" />
<meta property="og:description" content="Proyectos de desarrollo web y aplicaciones con IA." />
<meta property="og:type" content="website" />
```

### 💬 Prompt para accesibilidad

```text
Revisa este HTML y sugiere mejoras de accesibilidad:
- Agrega alt en las imágenes
- Usa etiquetas semánticas correctas
- Asegura contraste suficiente entre texto y fondo
```

✅ **Resultado esperado:**
Un HTML semántico, accesible y optimizado para motores de búsqueda.

---

## 🪜 Paso 5 – Añadir microinteracciones y pequeños detalles

🎯 **Objetivo:** mejorar la experiencia visual con pequeños toques de movimiento.

💬 Prompt para Copilot Chat:

```text
Agrega animaciones sutiles a las secciones del portafolio:
- Efecto fade-in al cargar
- Transición de color al hacer hover en botones
Usa keyframes y transition para mantenerlo ligero.
```

👉 Ejemplo:

```css
.fade-in {
  opacity: 0;
  transform: translateY(10px);
  animation: fadeInUp 0.8s ease-out forwards;
}

@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
```

💡 Aplica la clase `.fade-in` a los títulos y tarjetas cuando se carguen.

---

## 🪜 Paso 6 – Reto adicional (opcional)

Selecciona uno o varios para personalizar tu portafolio:

1. **Sección de experiencia:**
   Agrega una línea de tiempo (timeline) con logros o estudios.

   💬 Prompt:

   ```text
   Crea una sección de "Experiencia" con un timeline vertical que muestre año, cargo y descripción breve.
   ```

2. **Versión multilenguaje (simulada):**
   Botones “ES / EN” que cambien el texto de algunas secciones.

   💬 Prompt:

   ```text
   Agrega botones ES/EN que cambien dinámicamente los textos principales del portafolio usando JavaScript.
   ```

3. **Preloader o efecto de carga:**
   Un spinner o texto de “Cargando portafolio…” antes de mostrar la página.

---

## ✅ Resultado final del Nivel 2

Tu portafolio ahora debe:

* Cargar proyectos desde `data/projects.json` ✅
* Mostrar un diseño moderno, responsivo y accesible ✅
* Tener metadatos SEO y etiquetas semánticas ✅
* Incluir microinteracciones visuales ✅
* Ser fácilmente escalable y mantenible ✅

---

## 🧭 Reflexión final

> “Pasamos de un sitio estático a un proyecto modular y escalable.
> Copilot ya no solo genera código, sino que colabora para mejorar arquitectura, diseño y calidad.”

💡 **Próximo paso:**
En el **Nivel 3** convertirás tu portafolio en una experiencia **interactiva con IA**, agregando un asistente inteligente que responda preguntas sobre ti y tus proyectos.

---

## 📚 Recursos útiles

* 📘 [Guía de CSS Grid – MDN](https://developer.mozilla.org/es/docs/Web/CSS/CSS_grid_layout)
* 🎨 [Paletas de colores modernas – Coolors](https://coolors.co/)
* ♿ [Checklist de accesibilidad web – W3C](https://www.w3.org/WAI/test-evaluate/preliminary/)
* 🧠 [Buenas prácticas HTML y SEO](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)

---

✨ **¡Felicidades!** Tu portafolio ahora luce como el de un profesional del desarrollo web moderno.
