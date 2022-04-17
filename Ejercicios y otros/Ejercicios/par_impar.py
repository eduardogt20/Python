# Par impar

def ParImpar(numero):
    if (numero % 2) == 0:
        print("El numero es Par")
    else:
        print("El numero es Impar")

numero = int(input("Ingrese el numero a analizar: "))

ParImpar(numero)
