#Importar un modulo
import Modulos
Modulos.ladrido()

# Otra forma de importar
from Modulos import ladrido
ladrido()

#Importando desde Carpetas
from lib import perro

perro.ladrido()

#Importando Funcion especifica
from lib.perro import ladrido

ladrido()
