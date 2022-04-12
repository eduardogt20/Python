#Herencia Multinivel

class Padre:
    def __init__(self):
        self.nombre = "Padre"
    def caminar(self):
        print("Todos caminan")

class Hijo(Padre):
    def __init__(self):
        self.nombre = "Hijo"

class Nieto(Hijo):
    def __init__(self):
        self.nombre = "Nieto"

nieto = Nieto()
nieto.caminar()
