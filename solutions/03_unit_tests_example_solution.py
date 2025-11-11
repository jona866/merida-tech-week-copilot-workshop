"""
03_unit_tests_example_solution.py

Solución de referencia para las pruebas unitarias del factorial.

Incluye:
- Casos básicos.
- Casos borde.
- Verificación de errores.

Se puede usar para:
- Comparar con los tests generados por los estudiantes.
- Mostrar buenas prácticas al escribir pruebas con unittest.
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
    """
    Conjunto de pruebas unitarias para la función factorial.
    """

    def test_factorial_de_cero(self):
        """El factorial de 0 debe ser 1."""
        self.assertEqual(factorial(0), 1)

    def test_factorial_de_uno(self):
        """El factorial de 1 debe ser 1."""
        self.assertEqual(factorial(1), 1)

    def test_factorial_de_tres(self):
        """El factorial de 3 debe ser 6."""
        self.assertEqual(factorial(3), 6)

    def test_factorial_de_cinco(self):
        """El factorial de 5 debe ser 120."""
        self.assertEqual(factorial(5), 120)

    def test_factorial_numero_grande(self):
        """El factorial de 10 debe ser 3 628 800."""
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_numero_negativo_lanza_error(self):
        """Debe lanzar ValueError cuando el número es negativo."""
        with self.assertRaises(ValueError):
            factorial(-1)


if __name__ == "__main__":
    unittest.main()
