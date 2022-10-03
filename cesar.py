# Introducimos el texto a cifrar
texto=input("Introduzca el texto a cifrar: ")

# Creamos la cadena de caracteres
if texto==texto.upper():
    alf="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
else:
    alf="abcdefghijklmnopqrstuvwxtz"

# Definimos el valor del desplazamiento
k=int(input("Valor de desplazamiento: "))

# Creamos la cadena donde almacenará el texto cifrado
cifrad=""

# Cifrado
for c in texto:
    if c in alf:
        cifrad += alf[(alf.index(c) + k) % (len(alf))]
    else:
        cifrad +=c

print(cifrad)

# Descifrado
descif = ""
for c in cifrad:
    if c in alf:
        descif += alf[(alf.index(c) - k) % (len(alf))]
    else:
        descif += c

print(descif)
