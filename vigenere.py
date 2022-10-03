# Implementación algoritmo de Vigenère

import sys
from itertools import cycle

texto = open(sys.argv[1])  # seleccionamos el archivo .txt
contenido = texto.read()

# Introducimos la palabra clave que va a usar para cifrar el texto
k = input("Introduce la palabra clave:")

# Miramos si el texto está en mayúsculas o minúsculas
if contenido == contenido.upper():
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    k.upper()
else:
    alfabeto = "abcdefghijklmnopqrstuvwxtz"
    k.lower()

# Conseguimos los desplazamientos que vamos a usar para las distintas letras de la clave
despCesar=[]

for c in k:
    despCesar += [alfabeto.index(c)]

print(despCesar)

list_cif = cycle(despCesar)
list_descif = cycle(despCesar)

# cycle -> recibe un argumento y el resultado es la repetición de este indefinidamente
# -> Ej: cycle('ABCD') --> A B C D A B C D ...

# Cifrado
cifrad = ""

for c in contenido:
    if c in alfabeto:
        cifrad += alfabeto[(alfabeto.index(c) + list_cif.__next__()) % (len(alfabeto))]

print(cifrad)

# Descifrado
descif = ""
i = 0
for c in cifrad:
    if c in alfabeto:
        descif += alfabeto[(alfabeto.index(c) - list_descif.__next__()) % (len(alfabeto))]

print(descif)
