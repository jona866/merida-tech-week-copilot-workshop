"""
02_refactor_example.py

🎯 Objetivo:
Practicar la refactorización de código con GitHub Copilot.

🧠 Conceptos que se aprenden:
- Identificar código repetitivo y mejorar su estructura.
- Usar Copilot Chat para aplicar refactorizaciones sugeridas.
- Incorporar manejo de errores y documentación automática.

🧩 Instrucciones para el estudiante:
1. Observa que este código funciona, pero está mal organizado.
2. Usa Copilot Chat para refactorizarlo:
   - Elimina duplicación.
   - Extrae funciones auxiliares.
   - Agrega docstrings en español.
"""

def calcular_precio_total(productos):
    # Lista de productos: cada producto es una tupla (nombre, precio, cantidad)
    total = 0
    for producto in productos:
        if len(producto) != 3:
            # Falta manejo de errores
            continue

        nombre = producto[0]
        precio = producto[1]
        cantidad = producto[2]

        if precio < 0:
            # No se valida correctamente
            precio = 0

        subtotal = precio * cantidad
        print("Producto:", nombre, "Subtotal:", subtotal)
        total += subtotal

    print("Total:", total)
    return total


def ejemplo_uso():
    """
    Función de ejemplo que llama a calcular_precio_total.
    Se deja simple a propósito para que el estudiante pida mejoras con Copilot.
    """
    productos = [
        ("Laptop", 15000, 1),
        ("Mouse", 300, 2),
        ("Teclado", -500, 1),  # Precio inválido
        ("Monitor", 4500, 1),
        ("", 200, 3),          # Nombre vacío
    ]
    calcular_precio_total(productos)


if __name__ == "__main__":
    ejemplo_uso()

    # TODO: Usa Copilot Chat para:
    # - Refactorizar calcular_precio_total en funciones más pequeñas.
    # - Mejorar el manejo de errores.
    # - Agregar docstrings a todas las funciones en español.
    # - Opcional: devolver también un desglose por producto.
