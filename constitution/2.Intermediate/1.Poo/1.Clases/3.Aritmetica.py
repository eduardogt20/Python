#Aritmetica de objetos
#https://rszalski.github.io/magicmethods/

class Punto:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return self.a + other.a and self.b + other.b

punta_a = Punto(1,2)
punta_b = Punto(3,4)

print(punta_a.b + punta_b.b)
