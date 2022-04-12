#Propiedades generales

class Punto:
    c = 14
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def mostrar_puntos(self):
        print(f"{self.a}, {self.b}")

punto_a = Punto(1,2)
punto_b = Punto(3,4)

print(punto_a.b)
print(punto_a.c)
