# Closures 

def contador():
    conteo = 0

    def incrementar():
        nonlocal conteo
        conteo = conteo + 1
        return conteo

    return incrementar

incrementar = contador()

print(incrementar()) # 1
print(incrementar()) # 2
print(incrementar()) # 3
