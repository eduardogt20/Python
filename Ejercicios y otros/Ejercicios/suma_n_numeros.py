# Mostrar la suma de n numeros

numero = int(input("Ingrese el Numero que desea que se sume: "))
suma = 0
iterador = 1

while iterador <= numero:
    suma += iterador
    iterador += 1
    print(suma)

print(f"El resultado final de este seria:{suma}")
