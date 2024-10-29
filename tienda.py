class Tienda:
    def __init__(self):
        self._productos = []  # Lista privada de productos

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def mostrar_productos(self):
        for producto in self._productos:
            print(producto)

    def procesar_compra(self, productos_a_comprar):
        total = sum(producto.precio for producto in productos_a_comprar)
        print(f"Total de la compra: ${total}")

    def obtener_producto(self, indice):
        # Verifica si el índice es válido antes de acceder a la lista
        if 0 <= indice < len(self._productos):
            return self._productos[indice]
        else:
            raise IndexError("El índice del producto no es válido")