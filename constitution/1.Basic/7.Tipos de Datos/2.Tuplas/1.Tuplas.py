#Tuplas

#Definicion de una tupla
datos = (1,2,3)
print(datos)

#Igual tupla
dato = 10 , 20
print(type(dato))

#Tupla vacia
datoss = ()

#concatenar tuplas
conca = datos + dato
print(conca)

#Repetir una tupla varias veces
date = (1,2,3)*5
print(date)

#Desempaquetado
n1, n2, n3 = datos
print(n2)

#Comprobar elementos
if 2 in datos:
    print("El 2 existe")

#No se puede asignar
datos = (1,2,3) #Si se puede sobre escribir 
datos[0] = 5 #Da un error no se puede
print(datos[0])
