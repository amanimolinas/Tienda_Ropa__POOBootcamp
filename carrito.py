class Carrito:
    def __init__(self):
        self.__productos = {}

    def agregar_producto(self, producto, cantidad):
        if producto in self.__productos:
            self.__productos[producto] += cantidad
        else:
            self.__productos[producto] = cantidad

    def mostrar_resumen(self):
        print("\nResumen de la compra:")
        total = 0
        for producto, cantidad in self.__productos.items():
            subtotal = producto._precio * cantidad
            print(f"{producto._nombre} - Cantidad: {cantidad}, Subtotal: ${subtotal:.2f}")
            total += subtotal
        print(f"Total a pagar: ${total:.2f}")