from tienda import Tienda
from carrito import Carrito
from ropa import Camisa, Pantalon, Zapato

def realizar_compra(tienda):
    carrito = Carrito()

    while True:
        tienda.mostrar_productos()

        try:
            opcion = int(input("Porfavor selecciona el número del producto que deseas comprar (0 para salir): "))
            if opcion == 0:
                break

            cantidad = int(input("Ingrese la cantidad que desea comprar "))
            producto = tienda.obtener_producto(opcion - 1)

            if producto:
                carrito.agregar_producto(producto, cantidad)
                print(f"Agregaste {cantidad} unidades de {producto._nombre} al carrito.")
            else:
                print("Producto no válido.")
        
        except (ValueError, IndexError):
            print("Opción inválida, intenta de nuevo.")

    carrito.mostrar_resumen()

if __name__ == "__main__":
    tienda = Tienda()

    tienda.agregar_producto(Camisa("Camisa de Hombre", 128.00, "M", "Algodon",  "Negro"))
    tienda.agregar_producto(Pantalon("Pantalon Jogger", 40.00, "G", "Algodon", "Nike"))
    tienda.agregar_producto(Pantalon("Jeans", 70.00, "L", "Denim", "Indian Paraguay"))
    tienda.agregar_producto(Zapato("Taco alto", 50.00, 37))

    realizar_compra(tienda)
