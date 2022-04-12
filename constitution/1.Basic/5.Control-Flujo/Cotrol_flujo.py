#Condicionales
edad = 16

if edad > 18:
    print("Eres mayor de edad")
elif edad <= 16:
    print("Eres menor de edad")
else:
    print("No tienes edad eres un vampiro")

# Operador ternario
#<resultado_si_es_verdadero> if <condicion> else <resultado_si_es_falso>
mensaje = "Mayor de edad" if edad>=18 else "Menor de edad"

print(mensaje)
