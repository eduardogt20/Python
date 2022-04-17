#Desempaquetado de Lista

lista = [1,2,3]

#Primitiva
numero1=lista[0]

#Elegante
numero1, *otros = lista

print(numero1, otros)
