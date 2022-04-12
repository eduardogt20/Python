#Herencia
class Animal:
    def comer(self):
        print("El animal esta comiendo")


class Perro(Animal):
    def __init__(self):
        self.color = "marron"

class Gato(Animal):
    def __init__(self):
        self.color = "marron"

perro = Perro()
perro.comer()

gato = Gato()
gato.comer()
