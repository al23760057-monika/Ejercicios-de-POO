class Platillo:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        print(f"Este es el platillo{self.nombre} y cuesta ${self.precio}")

    def tipo(self):
        print(f"......")

        