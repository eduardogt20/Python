# Docstrings 

def incrementar(n):
    """Incrementa un numero""" # Docstrings def
    return n + 1


"""Modulo Perro

Este modulo hace ... bla bla bla y provee las siguientes clases:

- Perro
...
"""

class Perro:
    """Una clase que representa un perro"""
    def __init__(self, nombre, edad):
        """Inicializar un nuevo perro"""
        self.nombre = nombre
        self.edad = edad

    def ladrido(self):
        """Permite ladrar al perro"""
        print('WOF!')



