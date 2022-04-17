# Arboles 

# Un árbol binario es un árbol que tiene máximo dos nodos descendientes (izquierdo y derecho). 
class Arbol(object):
  def __init__(self):
    self.der = None    # Rama derecha del árbol
    self.izq  = None    # Rama izquierda del árbol
    self.dato  = None    # Dato del nodo del árbol
    
raiz = Arbol()
raiz.dato = 'Raiz'
raiz.izq = Arbol()
raiz.izq.dato = 'Izquierda'
raiz.der = Arbol()
raiz.der.dato = 'Derecha'
print(raiz.izq.dato)

# De esta misma forma se puede ir aumentando el tamaño del árbol y agregándole mas información:
class Arbol(object):
  def __init__(self):
    self.der = None
    self.izq  = None
    self.dato  = None
    
raiz = Arbol()
raiz.dato = 'Raiz'
raiz.izq = Arbol()
raiz.izq.dato = 'Izquierda'
raiz.der = Arbol()
raiz.der.dato = 'Derecha'
raiz.izq.izq = Arbol()
raiz.izq.izq.dato = 'Izquierda 2'
raiz.izq.der = Arbol()
raiz.izq.der.dato = 'Izquierda - Derecha'

# Lógicamente, si se quiere definir un árbol que no sea binario, entonces se aumentan las posibles ramas en ‘__init__’:
class Arbol(object):
  def __init__(self):
    self.der  = None
    self.der2 = None
    self.cent = None
    self.izq  = None
    self.izq2 = None
    self.dato = None
