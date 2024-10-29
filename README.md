# Sistema de Compra de Ropa con POO

Este proyecto tiene como objetivo desarrollar un programa de compra de ropa utilizando Programación Orientada a Objetos (POO) en Python. El sistema permite a los usuarios seleccionar entre diferentes ítems de ropa, como camisas, pantalones y zapatos, y procesar la compra de estos productos.

El propósito de este proyecto es:
- Proporcionar una interfaz sencilla para que los usuarios puedan comprar ropa.
- Implementar conceptos de POO, incluyendo herencia, encapsulación, polimorfismo y abstracción, a través de clases que representan productos de ropa y la tienda.

## Estructura del Proyecto

- **menu.py**: Ejecuta el programa principal
- **producto.py**: Clase base que representa un producto general.
- **camisa**: Clase que hereda de ropa, representa camisas con atributos específicos como talla, tipo de tela y color.
- **pantalon**: Clase que hereda de ropa, representa pantalones con atributos específicos como talla, tipo de tela y marca.
- **zapato**: Clase que hereda de Producto, representa zapatos con atributos específicos como talla.
- **tienda.py**: Clase que gestiona los productos disponibles y procesa las compras.
- **carrito.py**: Donde se almacenan los productos seleccionados.

## Funcionalidades

El sistema incluye las siguientes funcionalidades:

- Mostrar la lista de productos disponibles.
- Permitir al usuario seleccionar un producto para comprar.
- Solicitar la cantidad deseada para la compra.
- Procesar la compra y mostrar un resumen de la transacción.
- Manejar errores y validar las selecciones del usuario.
