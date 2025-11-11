"""
03_unit_tests_example.py

🎯 Objetivo:
Practicar la generación de pruebas unitarias con ayuda de GitHub Copilot.

🧠 Conceptos que se aprenden:
- Uso de la librería estándar `unittest` en Python.
- Generación de nuevos casos de prueba con Copilot Chat.
- Importancia de validar entradas y errores.

🧩 Instrucciones para el estudiante:
1. Verifica o ajusta la función factorial (ya incluida aquí o en test.py).
2. Usa Copilot Chat para generar más métodos de prueba.
3. Ejecuta los tests desde la terminal con:
   python -m unittest examples/03_unit_tests_example.py
"""

import unittest


def factorial(n: int) -> int:
    """
    Calcula el factorial de un número entero no negativo.

    :param n: Número entero no negativo.
    :return: Factorial de n.
    :raises ValueError: Si n es negativo.
    """
    if n < 0:
        raise ValueError("El número debe ser no negativo.")
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


class TestFactorial(unittest.TestCase):
    def test_factorial_de_cero(self):
        """El factorial de 0 debe ser 1."""
        self.assertEqual(factorial(0), 1)

    def test_factorial_de_un_numero_pequeno(self):
        """El factorial de 5 debe ser 120."""
        self.assertEqual(factorial(5), 120)

    # TODO: Usa GitHub Copilot para generar más casos de prueba:
    # - factorial de 1
    # - factorial de 3
    # - verificar que lanza ValueError cuando n es negativo
    # - opcional: probar un número más grande


if __name__ == "__main__":
    unittest.main()
