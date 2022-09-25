#Algoritmo de cifrado simétrico por sustitución monoalfabeto

import sys

print(sys.argv)

texto = sys.argv[3]

#Creamos la cadena de caracteres
if texto==texto.upper():
    alfb_cif ="UVWXYZNOPQRSTHIJKLMABCDEFG"
    alfabeto ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
else:
    alfb_cif="uvwxyznopqrsthijklmabcdefg"
    alfabeto = "abcdefghijklmnopqrstuvwxtz"

#Creamos la cadena donde almacenará el texto cifrado
cifrad=""
descif=""

#Cifrado
for c in texto:
    if c in alfabeto:
        cifrad += alfb_cif[alfabeto.index(c)]
    else:
        cifrad +=c

print(cifrad)

#Descifrado
for c in cifrad:
    if c in alfb_cif:
        descif += alfabeto[alfb_cif.index(c)]
    else:
        descif += c

print(descif)