# 🧭 Ruta de Aprendizaje – Práctica 1: GitHub Copilot en un proyecto existente

## 🎯 Objetivo General
Aprender a usar GitHub Copilot dentro de Visual Studio Code para generar, refactorizar, probar y documentar código en un proyecto ya existente.

---

## 1️⃣ Calentamiento: generación de código

📁 Archivo: `examples/01_generate_code.py`

1. Observa la función `suma` ya implementada.
2. Usa GitHub Copilot para completar las funciones marcadas con `TODO`:
   - `promedio_lista`
   - `maximo_lista`
3. Usa Copilot Chat para pedir:
   > "Explain what this function does and how it works."
4. Pide también a Copilot que agregue docstrings en español.

---

## 2️⃣ Refactorización de código

📁 Archivo: `examples/02_refactor_example.py`

1. Ejecuta el script y observa la salida.
2. Usa Copilot Chat para refactorizar:
   > "Refactor this function to remove duplicated code, add error handling, and add Spanish docstrings."
3. Compara el código original con el refactorizado.

---

## 3️⃣ Pruebas unitarias

📁 Archivo: `examples/03_unit_tests_example.py`

1. Revisa los tests existentes.
2. Usa Copilot para generar más métodos de prueba en la clase `TestFactorial`.
3. Ejecuta los tests con:
   ```bash
   python -m unittest examples/03_unit_tests_example.py
