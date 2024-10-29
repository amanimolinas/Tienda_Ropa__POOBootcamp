from producto import Producto 

class Ropa(Producto):
    def __init__(self, nombre, precio, talla, tipo_tela):
        super().__init__(nombre, precio)
        self._talla = talla
        self._tipo_tela = tipo_tela

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self._talla}, Tipo de Tela: {self._tipo_tela}")


class Camisa(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tela, color):
        super().__init__(nombre, precio, talla, tipo_tela)
        self._color = color


    def __str__(self):
        return f"Camisa: {self._nombre} (Talla: {self._talla}) Precio: ${self._precio} Color: {self._color} Tipo de tela: {self._tipo_tela}"



class Pantalon(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tela, marca):
        super().__init__(nombre, precio, talla,  tipo_tela)

        self._marca= marca

    def __str__(self):
        return f"Pantalón: {self._nombre} (Talla: {self._talla}) Precio: ${self._precio} Marca: {self._marca} Tipo de tela: {self._tipo_tela}"


class Zapato(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self._talla = talla

    @property
    def talla(self):
        return self.__talla

    def __str__(self):
        return f"Zapato: {self._nombre} (Talla: {self._talla}) Precio: ${self._precio}"
