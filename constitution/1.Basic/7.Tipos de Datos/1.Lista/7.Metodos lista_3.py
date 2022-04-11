#Metodos lista

lista = [3,4,2,1,5]

lista.sort()

print(lista)

print(sorted(lista))

Productos = [
    ("producto0",20),
    ("producto1",40),
    ("producto2",5),
] 
def ordenar_items(item):
    return item[1]

Productos.sort(key=ordenar_items)
print(Productos)
