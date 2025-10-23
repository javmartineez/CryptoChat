import sys
import os
import random
import modular as m
import rsa


def sacar_ficheros(user1: str, user2: str):
    paths = []
    path1_public = f"Usuarios/pub_{user1}.txt"
    paths.append(path1_public)
    path1_priv = f"Usuarios/priv_{user1}.txt"
    paths.append(path1_priv)
    path2_public = f"Usuarios/pub_{user2}.txt"
    paths.append(path2_public)

    for path in paths:
        if not os.path.exists(path):
            raise ValueError("No se encuentran las claves de todos los usuarios")
    return paths

def leer_claves(fichero: str) -> list:
    lista = []
    with open(fichero) as f:
        for linea in f:
            linea = int(linea.strip())
            lista.append(linea)
    return lista


def cifrar(n, e, pad):
    text = input("Texto para cifrar: ")
    cifrado = rsa.cifrar_cadena_rsa(text, n, e, pad)
    print(f"Texto cifrado: {cifrado}")

def descifrar(n, pad, d):
    text = input("Texto a descifrar: ")
    lista = list(map(int,text.split(" ")))
    descifrado = rsa.descifrar_cadena_rsa(lista, n, d, pad)
    print(f"Texto descifrado: {descifrado}")

def users():
    arguments = sys.argv[1:]
    user1 = arguments[0]
    user2 = arguments[1]
    return (user1, user2)

def main():
    user1, user2 = users()

    path1_pub, path1_priv, path2_pub = sacar_ficheros(user1, user2)

    n1, e1, pad1 = leer_claves(path1_pub)
    n2, e2, pad2 = leer_claves(path2_pub)
    d1, = leer_claves(path1_priv)

    actividad = ""
    while actividad != "S":
        actividad = input("cifrar (C), descifrar (D) o salir (S): ").upper()
        if actividad == "C":
            cifrar(n2, e2, pad2)
        elif actividad == "D":
            descifrar(n1, pad1, d1)


if __name__ == "__main__":
    main()


    
    


