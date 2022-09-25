# Algoritmo de cifrado simétrico por sustitución monoalfabeto

import sys

texto = open(sys.argv[1])  # seleccionamos el archivo .txt
contenido = texto.read()

# Creamos la cadena de caracteres
if contenido == contenido.upper():
    alfb_cif = "UVWXYZNOPQRSTHIJKLMABCDEFG"
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
else:
    alfb_cif = "uvwxyznopqrsthijklmabcdefg"
    alfabeto = "abcdefghijklmnopqrstuvwxtz"

# Creamos la cadena donde almacenará el texto cifrado
cifrad=""
descif=""

# Seleccionamos la acción que queremos realizar, cifrar o descifrar un texto
accion = input("Elija una opción:1) Cifrar 2) Descifrar\n")

if accion == "1":
    #Cifrado

    for c in contenido:
        if c in alfabeto:
            cifrad += alfb_cif[alfabeto.index(c)]
        else:
            cifrad += c
    print(cifrad)
elif accion == "2":
    # Descifrado
    for c in contenido:
        if c in alfb_cif:
            descif += alfabeto[alfb_cif.index(c)]
        else:
            descif += c
    print(descif)
else:
    print("No ha pulsado un número válido")

