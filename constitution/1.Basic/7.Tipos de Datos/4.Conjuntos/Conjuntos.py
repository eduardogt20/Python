#Conjuntos

#Definicion
nombres = {"Roger", "Syd"}

#Intereccion
conjunto1 = {"Roger", "Syd"}
conjunto2 = {"Roger"}

interseccion = conjunto1 & conjunto2

#Union
conjunto1 = {"Roger", "Syd"}
conjunto2 = {"Luna"}

union = conjunto1 | conjunto2

#Diferencia
conjunto1 = {"Roger", "Syd"}
conjunto2 = {"Roger"}

diferencia = conjunto1 - conjunto2


#Verificar 
print("Roger" in nombres) # True
