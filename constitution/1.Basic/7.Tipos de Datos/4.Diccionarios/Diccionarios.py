#Diccionarios

personas = {
    "nombre" : "Bairon",
    "edad" : 17,
    "altura": 2
}

'''
print(personas)

personas["nombre"] = "Julio"

print(personas["nombre"])
'''
# = a print get
if "altura" in personas:
    print(personas["altura"])
else:
    print(personas)

#Comprovar si hay un valor en el diccionario
print(personas.get("altura", "No hay altura"))

#Eliminar un valor del diccionario
del personas["altura"]
print(personas)
