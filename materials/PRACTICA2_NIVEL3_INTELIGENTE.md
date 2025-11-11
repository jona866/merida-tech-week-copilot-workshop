# 🤖 Práctica 2 – Nivel 3: Portafolio “Inteligente”

> 🔼 Sobre el Nivel 2: ahora tu portafolio incorpora un **asistente tipo chatbot** que responde preguntas sobre tus habilidades y proyectos, simulando un modelo de IA localmente con JavaScript.  
> No se conecta a ningún servicio real — pero reproduce el flujo típico de una integración con IA.

---

## 🎯 Objetivos del nivel

1. Crear un **asistente virtual flotante** dentro del portafolio.  
2. Simular respuestas “inteligentes” a partir de un archivo local `faq.json`.  
3. Entender el flujo de comunicación entre la **UI → lógica → datos (JSON)**.  
4. Visualizar cómo se integraría una **API real (como Azure OpenAI)** en un futuro.

---

## 📁 Estructura esperada del proyecto

```bash
portafolio-ia-workshop/
│
├── index.html
├── styles.css
├── script.js
├── data/
│   ├── projects.json
│   └── faq.json           # Base de conocimiento local del asistente
├── notes.txt
└── README.md
````

---

## 🪜 Paso 1 – Crear `data/faq.json`

🎯 **Objetivo:** definir una “base de conocimiento” con preguntas frecuentes y respuestas predefinidas.

1. Crea el archivo `faq.json` dentro de la carpeta `data/`.
2. Agrega el siguiente contenido:

```json
[
  {
    "question": "¿Qué tecnologías dominas?",
    "keywords": ["tecnologías", "habilidades", "skills"],
    "answer": "Trabajo principalmente con HTML, CSS, JavaScript y Python. También tengo experiencia con APIs REST y conceptos básicos de inteligencia artificial."
  },
  {
    "question": "¿En qué tipo de proyectos te interesa colaborar?",
    "keywords": ["proyectos", "colaborar", "interesa"],
    "answer": "Me interesan proyectos relacionados con desarrollo web, dashboards interactivos y aplicaciones que integren modelos de IA."
  },
  {
    "question": "¿Tienes experiencia trabajando en equipo?",
    "keywords": ["equipo", "colaboración", "trabajo"],
    "answer": "Sí, he trabajado en proyectos académicos colaborativos utilizando GitHub para control de versiones y organización de tareas."
  },
  {
    "question": "¿Cómo puedo contactarte?",
    "keywords": ["contacto", "contactarte", "email"],
    "answer": "Puedes escribirme por correo o a través de mi perfil de LinkedIn. Los enlaces están en la sección de Contacto."
  }
]
```

💬 **Prompt para Copilot Chat:**

```text
Genera un archivo faq.json con preguntas frecuentes y respuestas sobre mi perfil profesional.
Incluye campos "question", "keywords" y "answer", en español.
Hazlo coherente para un portafolio de estudiante o desarrollador junior.
```

---

## 🪜 Paso 2 – Crear el asistente dentro del `index.html`

🎯 **Objetivo:** agregar el contenedor HTML del chat flotante al sitio.

1. Abre tu `index.html`.
2. Antes del cierre de la etiqueta `</body>`, agrega:

```html
<!-- 💬 Asistente Inteligente del Portafolio -->
<div class="assistant-widget">
  <button id="assistant-toggle" class="assistant-toggle">💬 Asistente</button>

  <div class="assistant-panel" id="assistant-panel">
    <div class="assistant-header">
      <h3>Asistente del Portafolio</h3>
      <button id="assistant-close" class="assistant-close">✕</button>
    </div>

    <div class="assistant-messages" id="assistant-messages">
      <div class="assistant-message assistant-message--bot">
        ¡Hola 👋! Soy el asistente de este portafolio.  
        Puedes preguntarme sobre mis habilidades, proyectos o contacto.
      </div>
    </div>

    <form id="assistant-form" class="assistant-form">
      <input
        type="text"
        id="assistant-input"
        placeholder="Escribe tu pregunta aquí..."
        autocomplete="off"
      />
      <button type="submit">Enviar</button>
    </form>
  </div>
</div>
```

💬 **Prompt alternativo para Copilot Chat:**

```text
Agrega al final del HTML un widget de chat flotante con:
- Un botón para abrir/cerrar
- Un panel con mensajes tipo chat
- Un input y botón para enviar
- Un mensaje inicial de bienvenida del asistente
```

---

## 🪜 Paso 3 – Estilos del asistente en `styles.css`

🎯 **Objetivo:** crear un diseño moderno, flotante y legible, sin afectar al resto del sitio.

Agrega al final del archivo `styles.css`:

```css
/* === ASISTENTE INTELIGENTE === */

.assistant-widget {
  position: fixed;
  bottom: 1.5rem;
  right: 1.5rem;
  z-index: 50;
}

.assistant-toggle {
  border-radius: 999px;
  padding: 0.6rem 1rem;
  border: none;
  background-color: var(--accent, #38bdf8);
  color: #0f172a;
  cursor: pointer;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
  transition: transform 0.2s ease;
}

.assistant-toggle:hover {
  transform: scale(1.05);
}

.assistant-panel {
  position: fixed;
  bottom: 4.5rem;
  right: 1.5rem;
  width: 320px;
  max-height: 420px;
  background-color: var(--card-bg, #1e293b);
  color: var(--text, #f1f5f9);
  border-radius: 1rem;
  box-shadow: 0 14px 40px rgba(0, 0, 0, 0.6);
  display: none;
  flex-direction: column;
  overflow: hidden;
}

.assistant-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.6rem 0.9rem;
  border-bottom: 1px solid #334155;
}

.assistant-messages {
  padding: 0.75rem;
  flex: 1;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  font-size: 0.85rem;
}

.assistant-message {
  padding: 0.5rem 0.7rem;
  border-radius: 0.75rem;
  max-width: 80%;
  line-height: 1.4;
}

.assistant-message--bot {
  align-self: flex-start;
  background-color: #1f2937;
}

.assistant-message--user {
  align-self: flex-end;
  background-color: var(--accent, #38bdf8);
  color: #0f172a;
}

.assistant-form {
  display: flex;
  gap: 0.4rem;
  padding: 0.6rem 0.8rem;
  border-top: 1px solid #334155;
}

.assistant-form input {
  flex: 1;
  border-radius: 999px;
  border: 1px solid #475569;
  padding: 0.4rem 0.75rem;
  background-color: transparent;
  color: inherit;
}

.assistant-form button {
  border-radius: 999px;
  border: none;
  background-color: var(--accent, #38bdf8);
  color: #0f172a;
  padding: 0.4rem 0.9rem;
  cursor: pointer;
}
```

💬 **Prompt para Copilot Chat:**

```text
Agrega estilos CSS para que el asistente se muestre como un chat flotante moderno y minimalista,
alineado con el modo oscuro del portafolio.
Incluye transiciones suaves y estilo para mensajes del usuario y del bot.
```

---

## 🪜 Paso 4 – Lógica del asistente en `script.js`

🎯 **Objetivo:** simular respuestas inteligentes con datos locales.

1. Abre tu `script.js`.
2. Al final del archivo, agrega este bloque (puedes pedir ayuda a Copilot con prompts como los siguientes).

💬 **Prompt principal:**

```text
Agrega la lógica del asistente virtual:
- Carga faq.json usando fetch()
- Escucha los clics en el botón Asistente para abrir/cerrar el panel
- Captura el texto del usuario desde el input
- Busca coincidencias de palabras clave en faq.json
- Devuelve la respuesta correspondiente o un mensaje genérico
Agrega comentarios en español.
```

📄 **Código sugerido:**

```js
// === ASISTENTE INTELIGENTE ===
let faqData = [];

// Cargar las preguntas y respuestas desde faq.json
fetch("./data/faq.json")
  .then((res) => res.json())
  .then((data) => {
    faqData = data;
  })
  .catch((err) => console.error("Error al cargar faq.json:", err));

// Elementos del DOM
const toggleBtn = document.getElementById("assistant-toggle");
const panel = document.getElementById("assistant-panel");
const closeBtn = document.getElementById("assistant-close");
const form = document.getElementById("assistant-form");
const input = document.getElementById("assistant-input");
const messages = document.getElementById("assistant-messages");

// Mostrar / ocultar el panel
toggleBtn.addEventListener("click", () => {
  panel.style.display = panel.style.display === "flex" ? "none" : "flex";
});
closeBtn.addEventListener("click", () => {
  panel.style.display = "none";
});

// Manejar envío de mensaje
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const question = input.value.trim();
  if (!question) return;
  addMessage(question, "user");
  input.value = "";

  // Simular “pensando...”
  setTimeout(() => {
    const answer = getAssistantAnswer(question);
    addMessage(answer, "bot");
  }, 600);
});

// Agregar mensaje al chat
function addMessage(text, sender) {
  const msg = document.createElement("div");
  msg.classList.add("assistant-message");
  msg.classList.add(
    sender === "bot"
      ? "assistant-message--bot"
      : "assistant-message--user"
  );
  msg.textContent = text;
  messages.appendChild(msg);
  messages.scrollTop = messages.scrollHeight;
}

// Buscar respuesta simulada
function getAssistantAnswer(question) {
  const q = question.toLowerCase();

  for (const item of faqData) {
    if (item.keywords.some((kw) => q.includes(kw))) {
      return item.answer;
    }
  }

  return "No estoy seguro de eso 🤔, pero puedes revisar la sección de proyectos o contacto para más información.";
}
```

---

## 🪜 Paso 5 – Mejorar la experiencia (simulación “IA” real)

🎯 **Objetivo:** dar sensación de inteligencia, incluso sin conexión a un modelo.

💬 **Prompt para Copilot Chat:**

```text
Mejora la experiencia del asistente agregando:
- Un mensaje temporal de “Pensando...” antes de la respuesta
- Enlaces interactivos cuando mencione secciones (por ejemplo #proyectos o #contacto)
- Normalización de texto (sin acentos, todo en minúsculas) para mejorar coincidencias
```

Puedes añadir lo siguiente:

```js
function normalizeText(text) {
  return text
    .toLowerCase()
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "");
}

function getAssistantAnswer(question) {
  const q = normalizeText(question);

  for (const item of faqData) {
    if (item.keywords.some((kw) => q.includes(kw))) {
      return item.answer;
    }
  }

  return "No tengo una respuesta exacta 🤖, pero revisa la sección de <a href='#proyectos'>proyectos</a> para saber más.";
}
```

---

## 🪜 Paso 6 – Prueba final

1. Abre tu sitio localmente o con **Live Server**.
2. Haz clic en el botón 💬 **Asistente**.
3. Escribe preguntas como:

   * “¿Qué tecnologías usas?”
   * “¿Cómo puedo contactarte?”
   * “¿Tienes experiencia en equipo?”
4. Observa cómo responde basándose en tu archivo `faq.json`.

✅ **Resultado esperado:**
El asistente simula respuestas coherentes y “conversacionales”, incluso sin una IA real detrás.

---

## 🧠 Explicación conceptual

> Aunque las respuestas del asistente se generan localmente, este patrón replica el flujo de trabajo de una **integración real con IA**:

| Etapa                  | Equivalente actual        | En un sistema con IA real             |
| ---------------------- | ------------------------- | ------------------------------------- |
| UI del chat            | HTML + CSS + JS           | Igual                                 |
| Entrada del usuario    | input y evento `submit`   | Texto enviado a una API               |
| Fuente de conocimiento | `faq.json`                | Modelo o base vectorial               |
| Lógica de respuesta    | búsqueda de coincidencias | respuesta generada por el modelo      |
| Visualización          | renderizado en DOM        | igual, con streaming o tipado animado |

---

## ⚙️ Ideas para expandir

1. Conectar el asistente a un **Azure OpenAI endpoint** usando `fetch()`.
2. Enviar las preguntas a un backend y devolver respuestas generadas por GPT.
3. Agregar memoria de conversación con `localStorage`.
4. Permitir que los usuarios dejen mensajes personalizados.

💬 Prompt conceptual para discusión:

```text
Explica cómo podría conectarse este asistente a una API de Azure OpenAI.
Incluye pasos generales y precauciones de seguridad (API key, validación, etc.).
```

---

## ✅ Resultado final del Nivel 3

| Elemento             | Descripción                                     |
| -------------------- | ----------------------------------------------- |
| `faq.json`           | Base de conocimiento con preguntas y respuestas |
| `index.html`         | Asistente visible y funcional                   |
| `styles.css`         | Estilos modernos del chat flotante              |
| `script.js`          | Lógica simulada de IA local                     |
| 💬 Chatbot funcional | Interactivo y realista                          |

---

## 🧭 Reflexión final

> “En este nivel transformaste tu portafolio en una experiencia interactiva.
> Aunque las respuestas son simuladas, el flujo es idéntico al de un asistente real con IA.”

🌟 **Has construido tu primer sistema conversacional de front-end.**
El siguiente paso sería conectar este mismo flujo con una API real de IA y explorar el poder de Azure OpenAI.

---

## 📚 Recursos recomendados

* 🤖 [Azure OpenAI Service – Documentación oficial](https://learn.microsoft.com/es-es/azure/ai-services/openai/)
* 💬 [Guía de chatbots en JavaScript – MDN](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Fetching_data)
* 🎨 [Diseño de interfaces conversacionales](https://uxdesign.cc/designing-conversational-interfaces-8c11a8e7d7a2)
* 🧠 [Prompt Engineering Fundamentals (Microsoft Learn)](https://learn.microsoft.com/en-us/training/modules/introduction-prompt-engineering/)

---

✨ **¡Felicidades!** Tu portafolio ahora simula inteligencia, responde a los usuarios y demuestra cómo la IA puede integrarse de manera práctica y educativa.
