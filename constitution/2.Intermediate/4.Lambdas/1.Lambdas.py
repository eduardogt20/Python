#Lambda

#Sumar con funcion normal
def sumar(x,y):
    return x+y

print(sumar(4,2))

#Suma con Lambda

suma = lambda x , y : x + y 

print(suma(4,2))

lista = [1,2,3,4,5,6,7,8,9,10]
lista_filtrada = filter(lambda numero:numero % 2 == 0 , lista)

pares = list(lista_filtrada)

print (pares)
