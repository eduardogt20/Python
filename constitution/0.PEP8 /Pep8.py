'''#Identacion
Si: # opcion 1
    foo = funcion_que_crea_bar(variable_1, variable2
                               variable_3)
    # opcion 2
    foo = funcion_que_crea_bar(
                  variable_1, variable2
                  variable_3)

No:
    foo = funcion_que_crea_bar(variable_1, variable2
                  variable_3)

#Tamaño maximo de linea 79 caracteres

# Separar las definiciones de las clases y funciones con dos líneas en blanco.

#Imports
Si: import os
    import sys

No: import os, sys

from subprocess import Popen, PIPE


Los imports deben agruparse en el siguiente orden:
 1. standard library. 1. 3rd party libraries. 1. local application.

#Espacios en blanco

#Dentro de paréntesis.

Yes: spam(ham[1], {eggs: 2})
No:  spam( ham[ 1 ], { eggs: 2 })

#Después de una coma. 

Yes: if x == 4: print x, y; x, y = y, x
No: if x == 4 : print x , y ; x , y = y , x

#Antes del paréntesis de una llamada a una función.

Yes: spam(1)
No:  spam (1)

#Antes del paréntesis de un índice.

Yes: dict['key'] = list[index]
No:  dict ['key'] = list [index]

#Alrededor de operadores.

Yes:

    i = i + 1
    submitted += 1
    x = x * 2 - 1
    hypot2 = x * x + y * y
    c = (a + b) * (a - b)

No:

    i=i+1
    submitted +=1
    x = x*2 - 1
    hypot2 = x*x + y*y
    c = (a+b) * (a-b)'''
