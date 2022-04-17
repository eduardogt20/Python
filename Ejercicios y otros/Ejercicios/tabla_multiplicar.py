# tabla de multiplicar

tabla = int(input("Ingrese el numero de la tabla que desea ver: "))
iterador = 1 

print(f"La tabla del {tabla}")
while iterador <= 10:
    print(f"{tabla}X{iterador}={tabla * iterador}")
    iterador += 1

