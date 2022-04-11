#Operadores Logicos y Encadenados
'''
Son los Siguientes:
and / y  
or  / o 
not / no
'''

x = True
y = True

#and Las 2 verdaderas para ser verdadera
if x == y and x != y:
    print("Es true")
else:
    print("Es False")

#una de ellas tiene que ser verdadera para ser verdadera
if x == y or x > y:
    print("Or es True")

#Concatenacion

edad = 18

# Manera larga if edad >= 18 and edad < 65:

if 18 >= edad < 65:
    print("Estas en edad de Trabajar")