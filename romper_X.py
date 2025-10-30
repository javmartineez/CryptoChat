import rsa 
from typing import Tuple, List

def leer_fichero(ruta:str) -> Tuple:
    """
    Función encargada de leer el criptograma X y obtener la 
    clave pública y generar una lista del mensaje encriptado 

    Args: 
        - ruta: ruta al fichero criptograma_X.txt
    Returns: 
        - n, e: clave pública 
        - encrypted_text(list): lista con cada caracter cifrado
    """

    with open(ruta, "r", encoding="utf-8") as f:
        lines = f.read().strip().splitlines()

    n_str, e_str = lines[0].split(":", 1)[1].split()

    encrypted_text = [int(tok) for tok in " ".join(lines[1:]).split()]

    return int(n_str), int(e_str), encrypted_text



if __name__ == "__main__":

    ruta_X = "criptograma_X.txt"
    n, e, encrypted_text = leer_fichero(ruta_X)
    m = rsa.ataque_texto_elegido(encrypted_text, n, e)
    print(m)