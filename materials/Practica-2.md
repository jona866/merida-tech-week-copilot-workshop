# 🧠 Práctica 2 – Creación de un Portafolio Web con GitHub Copilot y ChatGPT  

> 🎯 **Objetivo general:**  
Construir un **portafolio web personal** con HTML, CSS y JavaScript, utilizando **IA como asistente de desarrollo** en dos niveles:  
- **ChatGPT** → para idear, redactar y refinar contenido.  
- **GitHub Copilot (VS Code)** → para generar, editar y mejorar el código.  

Al finalizar esta práctica, tendrás un sitio **funcional y publicado** en **GitHub Pages**. 🚀  

---

## 🧩 Estructura general de la práctica  

| Fase | Herramienta principal | Resultado esperado |
|------|------------------------|--------------------|
| 1️⃣ Ideación de contenido | ChatGPT | Textos y estructura base del portafolio |
| 2️⃣ Configuración del entorno | GitHub + VS Code | Repositorio listo con extensiones activas |
| 3️⃣ Generación inicial del sitio | Copilot (Chat + Inline) | Archivos HTML, CSS y JS generados |
| 4️⃣ Edición y mejora del diseño | Copilot Edit / Agent | Código refactorizado, responsive y documentado |
| 5️⃣ Publicación | GitHub Pages | Sitio web disponible en línea |

---

## 🪜 Paso 1 – Idear tu portafolio con ChatGPT  

🎯 **Objetivo:** definir el contenido textual y la estructura antes de codificar.

### 💬 Prompt básico  
```text
Quiero crear un portafolio web sencillo para mostrar mi perfil profesional. 
Sugiere las secciones necesarias (por ejemplo: Sobre mí, Habilidades, Proyectos, Contacto) 
y genera ejemplos de texto breves en español para cada una. 
Mantén un tono profesional pero cercano.
````

### 💬 Prompt extendido

```text
Ayúdame a crear el contenido para un portafolio personal. 
Mi nombre es [Tu nombre], estudio [Tu carrera]. 
Mis intereses principales son [temas]. 
Sugiere títulos de secciones, descripciones cortas y 
2 o 3 ejemplos de proyectos ficticios con descripciones breves.
```

📝 **Guarda las respuestas** en un archivo `notes.txt` o mantenlas abiertas durante el desarrollo.

> 💡 ChatGPT aquí actúa como **diseñador de contenido** y **redactor técnico**.

---

## 🪜 Paso 2 – Configurar el entorno

### 1️⃣ Crear el repositorio en GitHub

* Nombre: `portafolio-ia-workshop`
* Visibilidad: **público**
* (Opcional) Agregar README

### 2️⃣ Clonar y abrir en VS Code

```bash
git clone https://github.com/TU_USUARIO/portafolio-ia-workshop.git
cd portafolio-ia-workshop
code .
```

### 3️⃣ Extensiones necesarias

* ✅ **GitHub Copilot**
* ✅ **GitHub Copilot Chat**

📍 Verifica que Copilot esté **encendido** (ícono en la barra inferior).

---

## 🪜 Paso 3 – Generar la base del proyecto con Copilot (Chat + Inline)

🎯 **Objetivo:** crear desde cero `index.html`, `styles.css` y `script.js`.

### 💬 Prompt en Copilot Chat

```text
Crea un portafolio web básico en HTML, CSS y JavaScript con las secciones:
Sobre mí, Habilidades, Proyectos y Contacto.
El diseño debe ser moderno, minimalista y responsive.
Genera index.html, styles.css y script.js en este repositorio.
Usa comentarios en español para explicar el código.
```

🔹 Copilot (Chat) puede crear directamente los archivos.

### 💡 Si no los crea automáticamente:

1. Crea el archivo manual (`index.html`).
2. Escribe un comentario:

   ```html
   <!-- Estructura básica del portafolio con header, main y footer -->
   ```
3. Presiona `Tab` → se insertará la sugerencia inline.

---

## 🪜 Paso 4 – Personalizar el contenido (Copilot Edit / Chat)

🎯 **Objetivo:** reemplazar textos genéricos y mejorar el diseño.

### 💬 En Copilot Chat

```text
Reemplaza los textos genéricos del portafolio con la siguiente información:
[pega aquí tus textos generados con ChatGPT].
Mejora la organización visual y la paleta de colores manteniendo un estilo profesional.
```

### ✏️ Usa Copilot Edit para refactorizar

Selecciona el archivo → clic derecho → **Copilot → Edit with prompt...**

```text
Refactoriza este código HTML agregando comentarios claros, 
etiquetas semánticas y enlaces de navegación con scroll suave.
```

### 💬 Para CSS

```text
Haz que este diseño sea responsive con flexbox o grid.
Agrega una sección hero con fondo degradado y tipografía moderna.
```

📘 **Consejo:**

* Usa **Chat** para pedir explicaciones o detalles.
* Usa **Edit** para reestructurar bloques completos.
* Usa **Inline** para insertar una línea o función rápida.

---

## 🪜 Paso 5 – Agregar interactividad (Copilot Agent)

🎯 **Objetivo:** añadir comportamientos simples en `script.js`.

### 💬 Prompts en Copilot Chat

1. **Modo oscuro/claro**

   ```text
   Agrega un botón que permita alternar entre modo oscuro y claro.
   El texto del botón debe cambiar entre “Modo oscuro” y “Modo claro”.
   ```
2. **Scroll suave**

   ```text
   Implementa scroll suave al hacer clic en los enlaces del menú de navegación.
   Usa JavaScript puro (sin librerías).
   ```
3. **Sincronización con CSS**

   ```text
   Asegúrate de que el botón de modo oscuro funcione correctamente 
   y actualiza los estilos en styles.css para ambos modos.
   ```

✅ **Resultado esperado:**

* Modo oscuro/claro funcionando.
* Scroll suave entre secciones.
* Año actual en el footer insertado automáticamente.

---

## 🪜 Paso 6 – Validar el resultado localmente

1. Abrir `index.html` en el navegador (o usando **Live Server**).
2. Verificar:

   * Navegación funcional 🧭
   * Diseño responsivo 📱
   * Scroll suave 🪄
   * Modo oscuro/claro 🌙☀️

---

## 🪜 Paso 7 – Publicar en GitHub Pages

```bash
git add .
git commit -m "Versión inicial del portafolio con IA"
git push origin main
```

Luego, en GitHub:

1. Ir a **Settings → Pages**
2. En **Source**, elegir: `main / (root)`
3. Guardar.

📎 El sitio estará disponible en unos segundos en:

```
https://TU_USUARIO.github.io/portafolio-ia-workshop/
```

---

## 💬 Prompts clave por fase

| Fase               | Herramienta       | Prompt recomendado                                                                   |
| ------------------ | ----------------- | ------------------------------------------------------------------------------------ |
| 💡 Ideación        | **ChatGPT**       | “Quiero un portafolio con secciones y textos breves en español.”                     |
| 🏗️ Estructura     | **Copilot Chat**  | “Genera index.html, styles.css y script.js para un portafolio moderno y responsive.” |
| 🎨 Personalización | **Copilot Edit**  | “Refactoriza y agrega mis textos personalizados en las secciones.”                   |
| ⚙️ Interactividad  | **Copilot Agent** | “Agrega modo oscuro y scroll suave.”                                                 |
| 🧾 Documentación   | **Copilot Chat**  | “Explica cada parte del código con comentarios en español.”                          |

---

## ✅ Resultado final esperado

| Archivo         | Descripción                             |
| --------------- | --------------------------------------- |
| `index.html`    | Estructura semántica del portafolio     |
| `styles.css`    | Estilos responsive, modo oscuro / claro |
| `script.js`     | Funciones JS para interactividad        |
| `notes.txt`     | Textos generados con ChatGPT            |
| 🌐 GitHub Pages | Sitio publicado en línea                |

---

## 💡 Buenas prácticas con IA

> ⚖️ **La IA no reemplaza al desarrollador, lo potencia.**

* ✍️ Escribe prompts claros y específicos.
* 🔄 Itera hasta que el resultado te satisfaga.
* 🔍 Revisa cada línea de código antes de ejecutar.
* 💬 Pregunta a Copilot *“Explain what this code does”* para aprender.

---

## 🧭 Reflexión final

> “En esta práctica, la IA no sustituye la creatividad humana, la expande.
> GitHub Copilot y ChatGPT son herramientas que permiten pasar de una idea a un resultado real en minutos.”

🌟 ¡Felicidades! Has construido tu primer sitio web con asistencia de IA.


