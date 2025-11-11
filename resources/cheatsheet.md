# 🧠 Guía rápida: GitHub Copilot en VS Code  
**Taller: Desarrollo asistido por IA – GitHub Copilot para estudiantes de ingeniería**  
📅 Actualizado: Noviembre 2025  
📘 Basado en documentación oficial [docs.github.com/copilot](https://docs.github.com/copilot)

---

## 🎯 Objetivo del taller
Aprender a utilizar **GitHub Copilot** dentro de **Visual Studio Code** para mejorar la productividad en el desarrollo de software.  
Durante el taller aprenderás a:
- Usar autocompletado inteligente.
- Chatear con Copilot usando `@` y `/` comandos.
- Generar código, tests y documentación.
- Comprender buenas prácticas y limitaciones.
- Integrar IA en tus proyectos de ingeniería.

---

## 🚀 1. ¿Qué es GitHub Copilot?
Copilot es un asistente de programación con IA desarrollado por **GitHub y OpenAI**.  
Te sugiere líneas de código, explica funciones, genera pruebas, corrige errores y documenta proyectos.

💡 **Funciona en:**
- VS Code, Visual Studio, Neovim, JetBrains IDEs.
- GitHub.com (para PR reviews y commits).
- CLI de Copilot (en GitHub CLI).

---

## ⚙️ 2. Instalación rápida en VS Code

1. Abre **VS Code** → Extensiones (`Ctrl + Shift + X`).
2. Instala **GitHub Copilot** y **GitHub Copilot Chat**.
3. Inicia sesión con tu cuenta de GitHub.
4. (Opcional) Si eres estudiante, activa el **GitHub Student Developer Pack**:  
   🔗 [https://education.github.com/pack](https://education.github.com/pack)  
   > Te da acceso gratuito a Copilot y más herramientas de desarrollo.

---

## 💬 3. Modos de uso principales

| Modo | Descripción | Dónde se usa |
|------|--------------|--------------|
| 💡 **Inline Completions** | Sugerencias de código dentro del editor. | En cualquier archivo activo. |
| 💬 **Copilot Chat** | Ventana de chat contextual (preguntas, refactorización, explicaciones). | Barra lateral de VS Code. |
| 🤖 **Copilot Agent** | Ejecuta tareas autónomas (crear PRs, refactorizar proyectos completos). | En VS Code y GitHub.com. |

---

## 🧩 4. Prefijos de comandos (Copilot Chat)

### ⚡ Comandos con `/`  
Se escriben en el chat para ejecutar acciones rápidas:

| Comando | Función | Ejemplo |
|----------|----------|---------|
| `/new` | Inicia una nueva conversación. | `/new` |
| `/clear` | Limpia el historial del chat. | `/clear` |
| `/delete` | Elimina la conversación actual. | `/delete` |
| `/rename` | Cambia el nombre de la conversación. | `/rename "Taller Copilot"` |
| `/explain` | Pide que explique el código seleccionado. | `/explain` |
| `/fix` | Solicita una corrección del código activo. | `/fix` |
| `/tests` | Genera casos de prueba unitarios. | `/tests` |

💡 **Consejo:** escribe `/` en el chat para ver la lista de comandos disponibles en tu versión.

---

### 🧠 Menciones con `@`
Las menciones cambian el contexto o enfoque del modelo:

| Mención | Qué hace | Ejemplo de uso |
|----------|-----------|----------------|
| `@workspace` | Analiza todo el proyecto o repositorio abierto. | `@workspace explain how authentication works` |
| `@file` | Se centra solo en el archivo activo. | `@file summarize this code` |
| `@terminal` | Sugiere comandos de terminal o shell. | `@terminal create a virtual environment and install requests` |
| `@git` | Ayuda con Git y PRs. | `@git create a new branch and commit changes` |
| `@docs` | Busca y explica documentación relevante (si disponible). | `@docs what does this API return?` |

> 🎯 En el taller, probaremos varios de estos comandos sobre código real.

---

## 🧠 5. Ejemplos prácticos

### ✍️ Generar código desde comentarios
```python
# Calcular el factorial de un número entero no negativo
def factorial(n: int):
    ...
````

Copilot completará la función automáticamente.
➡ Presiona `Tab` para aceptar o `Alt + ]` / `Alt + [` para cambiar la sugerencia.

---

### 💬 Explicar un archivo completo

```
@workspace explain this file
```

---

### 🧪 Generar pruebas unitarias

```
/tests
```

o en el chat:

```
@generate unit tests for factorial()
```

---

### 🔧 Corregir código

Selecciona el bloque con error → abre el chat → escribe:

```
/fix
```

---

### 🗂 Crear documentación

```
@workspace document this module using Python docstrings
```

---

## 🧰 6. Atajos de teclado en VS Code

| Acción                                 | Windows / Linux    | macOS             |
| -------------------------------------- | ------------------ | ----------------- |
| Aceptar sugerencia                     | `Tab`              | `Tab`             |
| Ver siguiente sugerencia               | `Alt + ]`          | `Option + ]`      |
| Ver sugerencia anterior                | `Alt + [`          | `Option + [`      |
| Activar sugerencia manual              | `Alt + \`          | `Option + \`      |
| Abrir panel de chat Copilot            | `Ctrl + I`         | `Cmd + I`         |
| Abrir chat lateral                     | `Ctrl + Shift + I` | `Cmd + Shift + I` |
| Aceptar todas las sugerencias visibles | `Ctrl + Enter`     | `Cmd + Enter`     |

💡 Puedes personalizar estos atajos desde:
**File > Preferences > Keyboard Shortcuts** → busca “Copilot”.

---

## 🧩 7. Modelos de IA soportados (2025)

| Modelo           | Propósito                                      | Estado |
| ---------------- | ---------------------------------------------- | ------ |
| GPT-5            | Análisis profundo, comprensión contextual.     | GA     |
| GPT-5 mini       | Rápido y económico, ideal para autocompletado. | GA     |
| Claude Haiku 4.5 | Explicaciones y documentación.                 | GA     |
| Gemini 2.5 Pro   | Multimodal, compatible con imágenes y texto.   | GA     |

📄 Más info: [Supported AI models in GitHub Copilot](https://docs.github.com/en/copilot/reference/ai-models/supported-models)

---

## 📦 8. Cambios recientes (nov 2025)

* 🔄 **Knowledge Bases → Copilot Spaces:**
  Nueva forma de conectar documentación y código.
  [Docs → Knowledge Bases](https://docs.github.com/en/copilot/concepts/context/knowledge-bases)

* 🧭 **Agente con instrucciones personalizadas:**
  Las organizaciones pueden definir guías o estilos de código para el *Copilot Agent*.
  [Changelog → Coding Agent Instructions](https://github.blog/changelog/2025-11-05-copilot-coding-agent-supports-organization-custom-instructions/)

* ⚠️ **Extensiones antiguas** (tipo GitHub Apps) dejarán de funcionar el 10 de noviembre de 2025.
  Las de VS Code no se afectan.

---

## 🧩 9. Buenas prácticas durante el taller

| Situación                    | Recomendación                                             |
| ---------------------------- | --------------------------------------------------------- |
| Quieres una mejor sugerencia | Escribe comentarios descriptivos antes del código.        |
| Copilot no sugiere nada      | Presiona `Alt + \` para forzar una nueva sugerencia.      |
| Demasiado contexto abierto   | Cierra archivos irrelevantes para mejorar la precisión.   |
| Código sensible              | No uses Copilot en repositorios con datos confidenciales. |
| Quieres aprender más         | Pide explicaciones con `@workspace explain line 20`.      |

---

## 💡 10. Ejercicios sugeridos

1. **Completado automático:** Genera funciones desde comentarios.
2. **Explicación de código:** Usa `@workspace explain`.
3. **Refactorización:** Usa `@workspace optimize for readability`.
4. **Pruebas unitarias:** Genera tests con `/tests`.
5. **Documentación:** Usa `@workspace document this module`.

---

## 📚 11. Recursos útiles

* 🏠 [Documentación principal de Copilot](https://docs.github.com/copilot)
* 💬 [Copilot Chat en VS Code](https://code.visualstudio.com/docs/copilot/overview)
* 🎓 [GitHub Education Pack](https://education.github.com/pack)
* 🧩 [Copilot Extensions](https://docs.github.com/en/copilot/building-copilot-extensions/about-building-copilot-extensions)
* 📊 [Monitoreo de uso y facturación](https://docs.github.com/en/copilot/how-tos/monitoring-your-copilot-usage-and-entitlements)

---

## 🧭 12. Consejos finales

* Usa Copilot como **asistente**, no como reemplazo del razonamiento humano.
* Valida siempre la calidad y seguridad del código generado.
* Guarda tus mejores prompts y crea tu propia *“guía personal de Copilot”*.
* Experimenta con distintos lenguajes (Python, C#, JavaScript, SQL) para ver las diferencias.
* ¡Explora, falla y aprende! La clave es practicar y entender cómo Copilot interpreta tus instrucciones.

---

> ✨ **Recuerda:** cuanto más claro y específico sea tu comentario o prompt, mejores resultados obtendrás.
>
> Ejemplo:
> ❌ “Haz una función”
> ✅ “Crea una función en Python que lea un archivo CSV, cuente las filas y devuelva un diccionario con los totales por categoría.”
