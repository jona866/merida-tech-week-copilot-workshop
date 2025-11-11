"""
02_refactor_example_solution.py

Versión refactorizada de ejemplo para:
- Separar responsabilidades en funciones pequeñas.
- Mejorar el manejo de errores.
- Documentar el código con docstrings en español.

Esta solución sirve como referencia para comparar:
- Código original vs código refactorizado.
"""

from dataclasses import dataclass
from typing import Iterable, List, Tuple, Optional


@dataclass
class Producto:
    """
    Representa un producto con nombre, precio y cantidad.
    """
    nombre: str
    precio: float
    cantidad: int


def convertir_a_producto(producto_raw: Tuple) -> Optional[Producto]:
    """
    Convierte una tupla cruda en un objeto Producto válido.

    :param producto_raw: Tupla con el formato (nombre, precio, cantidad).
    :return: Instancia de Producto si es válida, de lo contrario None.
    """
    if len(producto_raw) != 3:
        return None

    nombre, precio, cantidad = producto_raw

    # Validaciones básicas
    if not isinstance(nombre, str) or not nombre:
        return None
    if not isinstance(precio, (int, float)) or precio < 0:
        return None
    if not isinstance(cantidad, int) or cantidad <= 0:
        return None

    return Producto(nombre=nombre, precio=float(precio), cantidad=cantidad)


def calcular_subtotal(producto: Producto) -> float:
    """
    Calcula el subtotal de un producto.

    :param producto: Instancia de Producto.
    :return: Subtotal = precio * cantidad.
    """
    return producto.precio * producto.cantidad


def calcular_precio_total(productos_raw: Iterable[Tuple]) -> float:
    """
    Calcula el precio total de una lista de productos crudos.

    Cada producto crudo es una tupla con el formato:
    (nombre, precio, cantidad).

    :param productos_raw: Iterable de tuplas de productos.
    :return: Suma total de todos los subtotales.
    """
    total = 0.0
    productos_validos: List[Producto] = []

    for producto_raw in productos_raw:
        producto = convertir_a_producto(producto_raw)
        if producto is None:
            print(f"[ADVERTENCIA] Producto inválido ignorado: {producto_raw}")
            continue

        productos_validos.append(producto)

    for producto in productos_validos:
        subtotal = calcular_subtotal(producto)
        print(f"Producto: {producto.nombre} | Cantidad: {producto.cantidad} | Subtotal: {subtotal}")
        total += subtotal

    print("Total:", total)
    return total


def ejemplo_uso() -> None:
    """
    Función de ejemplo que muestra el uso de calcular_precio_total
    con una lista de productos crudos.
    """
    productos = [
        ("Laptop", 15000, 1),
        ("Mouse", 300, 2),
        ("Teclado", -500, 1),  # Precio inválido -> ignorado
        ("Monitor", 4500, 1),
        ("", 200, 3),          # Nombre vacío -> ignorado
    ]
    calcular_precio_total(productos)


if __name__ == "__main__":
    ejemplo_uso()
