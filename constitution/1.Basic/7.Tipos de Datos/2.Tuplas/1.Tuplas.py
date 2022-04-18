#Tuplas

#Definicion de una tupla
datos = (1,2,3)
print(datos)

#Igual tupla
dato = 10 , 20
print(type(dato))

#Tupla vacia
datoss = ()

#Contar elementos 
len(datos)

#concatenar tuplas
conca = datos + dato
print(conca)

#Repetir una tupla n veces
date = (1,2,3)*5
print(date)

#Desempaquetado
n1, n2, n3 = datos
print(n2)

datos.index(1)

#Comprobar elementos
if 2 in datos:
    print("El 2 existe")

#No se puede asignar
datos = (1,3,2) #Si se puede sobrescribir 
datos[0] = 5 #Da un error Tupla = Inmutable
sorted(datos) #Ordena
print(datos[0]) 
