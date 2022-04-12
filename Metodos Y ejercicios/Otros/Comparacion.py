#Comparacion de objetos

class Punto:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __eq__(self,other):
        return self.a == other.a and self.b == other.b

punto_a = Punto(1,2)
punto_b = Punto(1,2)

print(punto_a == punto_b)
