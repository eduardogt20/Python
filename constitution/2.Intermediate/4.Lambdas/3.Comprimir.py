#Comprimir funciones

productos = [
    ("producto1",10),
    ("producto2",20),
    ("producto3",30),
    ("producto4",40),
]

#filtrado
productos_filtrados = list(filter(lambda item: item[1] >= 100, productos))
print(f"productos_filtrados{productos_filtrados}")

#mapeado
productos_mapeados = list(map(lambda producto:producto[1],productos))
print(f"productos_mapeados{productos_mapeados}")

# = a filtrado
prod_fil_comprimidos = [item for item in productos if item[1]>=100]
print(prod_fil_comprimidos)

# = a mapeado
prod_map_comprimidos = [item[1] for item in productos]
print(prod_map_comprimidos)
