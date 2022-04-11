#lambda Maps

productos = [
    ("producto1",10),
    ("producto2",20),
    ("producto3",30),
    ("producto4",40),
]

for producto in productos:
    print(producto[0])

precios = map(lambda producto:producto[1],productos)

print(precios)
