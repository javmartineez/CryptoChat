import re 
import rsa 

def leer_fichero(ruta):

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