"""
01_generate_code_solution.py

Solución de referencia para:
- Generación de funciones con GitHub Copilot.
- Manejo básico de errores.
- Uso de docstrings en español.

Este archivo puede usarse:
- Como guía para el instructor.
- Para que el estudiante compare su solución con una versión “limpia”.
"""

from typing import List


def suma(a: float, b: float) -> float:
    """
    Devuelve la suma de dos números.

    :param a: Primer número.
    :param b: Segundo número.
    :return: Resultado de a + b.
    """
    return a + b


def promedio_lista(numeros: List[float]) -> float:
    """
    Calcula el promedio de una lista de números.

    :param numeros: Lista de valores numéricos.
    :return: Promedio de los valores de la lista.
    :raises ValueError: Si la lista está vacía.
    """
    if not numeros:
        raise ValueError("La lista no puede estar vacía.")

    return sum(numeros) / len(numeros)


def maximo_lista(numeros: List[float]) -> float:
    """
    Devuelve el valor máximo de una lista de números.

    :param numeros: Lista de valores numéricos.
    :return: Valor máximo encontrado en la lista.
    :raises ValueError: Si la lista está vacía.
    """
    if not numeros:
        raise ValueError("La lista no puede estar vacía.")

    maximo = numeros[0]
    for numero in numeros[1:]:
        if numero > maximo:
            maximo = numero
    return maximo


if __name__ == "__main__":
    lista = [10, 20, 30, 40]

    print("Suma 10 + 5:", suma(10, 5))
    print("Promedio de la lista:", promedio_lista(lista))
    print("Máximo de la lista:", maximo_lista(lista))
