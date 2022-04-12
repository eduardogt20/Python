#Super

class Padre:
    def __init__(self):
        self.padre = "Bairon"
        print(f"El Padre se llama{self.padre}")
    def caminar(self):
        print("Esta caminando")

class Hijo(Padre):
    def __init__(self):
        super().__init__()
        self.hijo = "Matias"
        print(f"El Hijo se llama{self.hijo}")
        super().caminar
    def Saludar(self):
        super().caminar()
        print("Saludar")

hijo = Hijo()
hijo.Saludar()

