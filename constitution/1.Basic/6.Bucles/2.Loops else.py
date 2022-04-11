#For loops else
enviado = True

for n in range(4):
    print("Intento de envio",n + 1 )
    if enviado:
        print("Mensaje enviado")
        break
else:
    print("Mensaje no enviado")
