#Scope

mensaje = "Hola"

def mostrar(nombre):
    global mensaje
    mensaje = "adios"

mostrar("Manuel")
print(mensaje)
