#Object
class Animal(object):
    def comer(self):
        print("El animal esta comiendo")


class Perro(Animal):
    def __init__(self):
        self.color = "marron"

class Gato(Animal):
    def __init__(self):
        self.color = "marron"

print(issubclass(Perro, Animal))
