import sys
import os


def sacar_ficheros(user1: str, user2: str):
    paths = []
    path1_public = f"Usuarios/pub_{user1}.txt"
    paths.append(path1_public)
    path1_priv = f"Usuarios/priv_{user1}.txt"
    paths.append(path1_priv)
    path2_public = f"Usuarios/pub_{user2}.txt"
    paths.append(path2_public)

    for path in paths:
        if os.path.exists(path):
            return "No se encuentran las claves de todos los usuarios"
    return paths

def leer_claves(fichero: str) -> list:
    lista = []
    with open(fichero) as f:
        for linea in f:
            linea = linea.strip()
            lista.append(linea)
    return lista




arguments = sys.argv[1:]
user1 = arguments[0]
user2 = arguments[1]
paths = sacar_ficheros(user1, user2)
[n1, e1, pad1] = leer_claves(paths[0])
[n2, e2, pad2] = leer_claves(paths[2])
d, = leer_claves(paths[1])



    
    


