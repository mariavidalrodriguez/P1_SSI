# Implementación del método Kasiski

import sys
import re

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

texto = open(sys.argv[1])  # seleccionamos el archivo .txt
contenido = texto.read()

for n in contenido: # Comprobamos que solo hay caracteres válidos en el texto introducido
    if (ord(n) < 65) or (ord(n) > 90):
        print("El mensaje introducido contiene caracteres no permitidos: ABCDEFGHIJKLMNOPQRSTUVWXYZ ")
        break

# Buscamos en el texto cadenas de 3 caracteres que se repitan y guardamos las distancias entre 2 cadenas repetidas

cadenas_rep = []
cadena = contenido[0:3]

text_sep = [] # aqui guardamos cada cadena de longitud 3
for i in range(0, len(contenido), 3):
    text_sep.append(contenido[i:i+3])
# print("Texto separado:", text_sep)

# Obtenemos las cadenas de 3 letras que se repiten en nuestro texto
i = 0
desplz = []
for pos in text_sep:
    first = contenido.find(contenido[i:i+3]) # devuelve la posición del primer elemento encontrado
    last = contenido.rfind(contenido[i:i+3]) # devuelve la posición del último elemento encontrado
    if first == last:
        first = []
        last = []
    else:
        if contenido[i:i+3] not in cadenas_rep:
            cadenas_rep.append(contenido[i:i+3])
            result = last - first
            desplz.append(result)
            print("Cadena:", contenido[i:i+3], "repetida: ", contenido.count(contenido[i:i+3]), "veces")
    i = i + 3

print("Cadenas repetidas:", cadenas_rep)
print("Desplazamiento: ", desplz)



