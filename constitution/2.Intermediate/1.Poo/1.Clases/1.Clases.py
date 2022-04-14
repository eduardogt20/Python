# Clases

# Clase
class Persona:
    # Constructor
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def caminar(self):
        print(f"{self.nombre} esta Caminado")


Bairon = Persona("Bairon", "Garita")

Bairon.caminar()
