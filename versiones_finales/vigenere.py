# Implementación algoritmo de Vigenère

import sys
from itertools import cycle


alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

texto = open(sys.argv[1])
contenido = texto.read()

# Comprobamos que solo hay caracteres válidos en el texto introducido
for n in contenido:
    if (ord(n) < 65) or (ord(n) > 90):
        print("El mensaje introducido contiene caracteres no permitidos: ABCDEFGHIJKLMNOPQRSTUVWXYZ ")
        break

# Decidimos que acción se va a realizar: (1) Cifrar o (2) Descifrar

accion = input("Seleccione la acción a realizar: 1) Cifrar 2) Descifrar\n")

# Introducimos y comprobamos la palabra clave que va a usar para cifrar el texto

k = input("Introduce la palabra clave: ")

# Comprobamos que solo hay caracteres válidos en la clave introducida
for n in k:
    if (ord(n) < 65) or (ord(n) > 90):
        print("El mensaje introducido contiene caracteres no permitidos: ABCDEFGHIJKLMNOPQRSTUVWXYZ ")
        break

# Conseguimos los desplazamientos que vamos a usar para las distintas letras de la clave

despCesar = []
for c in k:
    despCesar += [alfabeto.index(c)]
print(despCesar)
clave = cycle(despCesar)

resultado = ""

if accion == "1":
    for c in contenido:
        resultado += alfabeto[(alfabeto.index(c) + clave.__next__()) % len(alfabeto)]
    print(resultado)
elif accion == "2":
    for c in contenido:
        resultado += alfabeto[(alfabeto.index(c) - clave.__next__()) % len(alfabeto)]
    print(resultado)
else:
    print("La opción elegida no es válida\n")
