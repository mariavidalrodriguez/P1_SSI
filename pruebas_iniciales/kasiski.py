# Implementación del método Kasiski

import sys

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

texto = open(sys.argv[1])  # seleccionamos el archivo .txt
contenido = texto.read()

for n in contenido: # Comprobamos que solo hay caracteres válidos en el texto introducido
    if (ord(n) < 65) or (ord(n) > 90):
        print("El mensaje introducido contiene caracteres no permitidos: ABCDEFGHIJKLMNOPQRSTUVWXYZ ")
        break

# Buscamos en el texto cadenas de 3 caracteres que se repitan y guardamos las distancias entre 2 cadenas repetidas


