"""
01_generate_code.py

🎯 Objetivo:
Demostrar cómo GitHub Copilot puede generar funciones completas a partir de comentarios.

🧠 Conceptos que se aprenden:
- Uso de sugerencias inline (autocompletado inteligente).
- Uso de Copilot Chat para explicar código y generar docstrings.
- Importancia del prompting claro en código.

🧩 Instrucciones para el estudiante:
1. Lee la función ya escrita "suma".
2. Usa GitHub Copilot para generar las funciones marcadas como TODO.
3. Usa Copilot Chat para pedir explicaciones o mejoras.
"""

def suma(a: float, b: float) -> float:
    """
    Devuelve la suma de dos números.

    :param a: Primer número.
    :param b: Segundo número.
    :return: Resultado de a + b.
    """
    return a + b


# TODO: Usa GitHub Copilot para generar una función que calcule el promedio
# de una lista de números. La función debe llamarse "promedio_lista" y
# debe manejar el caso de lista vacía lanzando un ValueError.


# TODO: Usa GitHub Copilot para generar una función llamada "maximo_lista"
# que reciba una lista de números y devuelva el valor máximo.
# Pide también a Copilot que agregue un docstring en español.


if __name__ == "__main__":
    # 🧠 Prueba tu código aquí
    lista = [10, 20, 30, 40]
    print("Suma:", suma(10, 5))
    # Ejecuta las nuevas funciones una vez que Copilot las genere.
