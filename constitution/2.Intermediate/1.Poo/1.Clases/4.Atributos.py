#Atributos

class Persona:
    def __init__(self, apellido):
        self.__nombre = "Bairon" #Atributo privado
        #Quieres que otros no toquen el atributo
        #self._nombre = "Bairon" 
        self.apellido = apellido

bairon = Persona("Mir")
print(bairon.__dict__)
print(bairon._Persona__nombre)
