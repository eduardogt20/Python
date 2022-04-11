#Parametros xarg

def sumar(n1, n2, n3):
    total = n1+n2+n3
    return total

print(sumar(1,2,3))

def sumar_x_args(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print (sumar_x_args(1,2,3,4,5,6))
