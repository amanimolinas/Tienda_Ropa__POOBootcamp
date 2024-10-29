class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre  # Encapsulación
        self._precio = precio  # Encapsulación


 # Getters
    def get_nombre(self):
        return self._nombre

    def get_precio(self):
        return self._precio

    # Setters
    def set_precio(self, nuevo_precio):
        self._precio = nuevo_precio

    def __str__(self):
        return f"{self._nombre}: ${self._precio}"
