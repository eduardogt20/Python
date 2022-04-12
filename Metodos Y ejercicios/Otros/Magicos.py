#Metodos magicos

class Persona:
    def __init__(self):
        self.nombre = ("Bairon")
    def __str__(self):
        return f"Este objeto se llama {self.nombre}"
bairon = Persona()

print(str(bairon))

