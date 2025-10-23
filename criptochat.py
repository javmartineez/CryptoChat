import sys
import os
import random
import modular as m


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
            return "No se encuentran las claves de todos los usuarios"
    return paths

def leer_claves(fichero: str) -> list:
    lista = []
    with open(fichero) as f:
        for linea in f:
            linea = linea.strip()
            lista.append(linea)
    return lista


def cifrar(n, e, pad):
    text = input("Texto para cifrar: ")
    cifrado = ""
    for i in text:
        random_values = random.choices(range(10), k = int(pad))
        cifrado += m.potencia_mod_p(i + random_values, e, n) + " "
    return cifrado



def main():
    arguments = sys.argv[1:]
    user1 = arguments[0]
    user2 = arguments[1]
    paths = sacar_ficheros(user1, user2)
    if type(paths) == str:
        return paths
    [n1, e1, pad1] = leer_claves(paths[0])
    [n2, e2, pad2] = leer_claves(paths[2])
    d, = leer_claves(paths[1])

    actividad = ""
    while actividad != "c":
        actividad = input("cifrar (C), descifrar (D) o salir (S): ").upper()
        if actividad == "C":
            cifrado = cifrar(n2, e2, pad2)
            print(f"Texto cifrado: {cifrado}")

if __name__ == "__main__":
    main()


    
    


