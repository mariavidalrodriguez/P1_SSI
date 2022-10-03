# Algoritmo de cifrado simétrico por sustitución monoalfabeto

# Sintaxis de ejecución: python3 .\monoalfabeto.py <ruta_fichero_texto>

import sys

abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # abecedario en claro


def getModo():
    modo = input("Escoja la acción a realizar: 1) Cifrado 2) Descifrado\n")
    mensaje = comprobCaracter(contenido)
    clave = getClave()
    al_abc = gen_despabecedario(clave)
    abc = gen_abc(al_abc)

    if modo == "1":
        cifrado(mensaje, abc)
    elif modo == "2":
        descifrado(mensaje, abc)
    else:
        print("Error, no ha elegido ninguna de las opciones disponibles.\n")
        getModo()


def comprobCaracter(texto):  # comprobamos que el texto tenga solo caracteres válidos
    for n in texto:
        if (ord(n) < 65) or (ord(n) > 90):
            raise ValueError(
                "El texto introducido contiene caracteres no permitidos. Abecedario válido: ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def getClave():
    clave = input("Introduzca la clave: ")
    res = 0
    for n in clave:
        res = res + ord(n)
    return res


def gen_despabecedario(key):  # generamos una lista con los nº que serán las correspondencias entre letras
    l_random = []
    for n in range(26):
        a = (3 * key + 5) % 26
        key = key + 1
        l_random.append(a)
    return l_random


def gen_abc(lista):  # encriptamos el abecedario -> usamos el abecedario encriptado para cifrar y descifrar el texto
    abc = ""
    for n in lista:
        abc = abc + (chr(65 + n))
    print("El abecedario encriptado es el siguiente: ", abc)
    return abc


def cifrado(texto, alf_cif):
    tabla = str.maketrans(abecedario, alf_cif)
    res = texto.translate(tabla)
    print("Texto cifrado: ", res)


def descifrado(texto, alf_desc):
    tabla = str.maketrans(alf_desc, abecedario)
    res = texto.translate(tabla)
    print("Texto descifrado: ", res)


if __name__ == 'monoalbeto__':
    texto = open(sys.argv[1])
    contenido = texto.read()
    print(contenido)
    # getModo()
