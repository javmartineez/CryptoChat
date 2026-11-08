import sys
import os
import rsa
import excepciones as ex


def sacar_ficheros(user1: str, user2: str) -> list[str,str,str]:
    """
    Gets the paths of the files holding user1's public and private keys and user2's
    public key. It also checks that the paths exist, raising an error otherwise.
    Args:
        -user1: main user, whose public and private keys are retrieved.
        -user2: secondary user, whose public key is the only one retrieved.

    Returns:
        -paths: list with the paths of the different files.

    Raises:
        -PathError: if the path to the keys of the given user does not exist.
    """
    paths = []      #list where the paths are stored
    path1_public = f"Usuarios/pub_{user1}.txt"      #public key path of the first user
    paths.append(path1_public)
    path1_priv = f"Usuarios/priv_{user1}.txt"       #private key path of the first user
    paths.append(path1_priv)
    path2_public = f"Usuarios/pub_{user2}.txt"      #public key path of the second user
    paths.append(path2_public)

    for path in paths:
        if not os.path.exists(path):        #check that the paths exist
            raise ex.PathError("The keys of all the users could not be found")
    return paths

def leer_claves(fichero: str) -> list[int]:
    """
    Reads the content of the file holding the keys and stores them in a list.
    Args:
        -fichero: path of the file to read.

    Returns:
        -lista: list with the keys as int.

    Raises: None.
    """
    lista = []      #list where the keys are stored
    with open(fichero) as f:        #open the file as f
        for linea in f:     #read line by line
            linea = int(linea.strip())      #strip the newline and convert to int
            lista.append(linea)
    return lista


def cifrar(n: int, e: int, pad: int) -> None:
    """
    Takes the text to encrypt and sends it to the rsa library.
    Once the encrypted text is obtained, it is printed on screen.
    Args:
        -n: RSA modulus.
        -e: RSA exponent.
        -pad: number of padding digits to use when encrypting the message.

    Returns: None.

    Exceptions:
        -NegativeValue: if pad has a negative value.
    """
    if pad < 0:
        raise ex.NegativeValue("The number of padding digits cannot be negative")

    text = input("Text to encrypt: ")
    cifrado = rsa.cifrar_cadena_rsa(text, n, e, pad)      #get the encrypted text as a list with one value per character
    print("Encrypted text: ", *cifrado)      #show the encrypted text


def descifrar(n: int, pad: int, d: int) -> None:
    """
    Takes an encrypted text and sends it to the rsa library to
    decrypt it. Once decrypted, it is printed on screen.
    Args:
        -n: RSA modulus.
        -pad: number of padding digits to use when decrypting the message.
        -d: RSA private key.

    Returns: None.

    Exceptions:
        -NegativeValue: if pad has a negative value.
    """
    if pad < 0:
        raise ex.NegativeValue("The number of padding digits cannot be negative")

    text = input("Text to decrypt: ")
    lista = list(map(int,text.split(" ")))      #convert the input text into a list of ints
    descifrado = rsa.descifrar_cadena_rsa(lista, n, d, pad)     #decrypt the text
    print(f"Decrypted text: {descifrado}")        #show the decrypted text

def users() -> tuple[str,str]:
    """
    Gets the users passed as command-line arguments.
    Args: None.

    Returns:
        -user1: main user.
        -user2: secondary user.

    Raises:None
    """
    arguments = sys.argv[1:]        #get the arguments from the second one onwards (the first one is the executed module criptochat.py)
    user1 = arguments[0]            #First user
    user2 = arguments[1]            #Second user
    return (user1, user2)

def main():
    """
    Main function that runs the rest of the code.
    """
    user1, user2 = users()      #get the users

    path1_pub, path1_priv, path2_pub = sacar_ficheros(user1, user2)     #get the paths of the different files

    n1, e1, pad1 = leer_claves(path1_pub)       #Public keys of the first user
    n2, e2, pad2 = leer_claves(path2_pub)       #Public keys of the second user
    d1, = leer_claves(path1_priv)               #Private key of the first user

    actividad = ""
    while actividad != "S":     #interaction loop that ends with the S/s argument
        actividad = input("encrypt (C), decrypt (D) or quit (S): ").upper()        #ask the user for the command to run
        if actividad == "C":        #command to encrypt a message
            cifrar(n2, e2, pad2)
        elif actividad == "D":      #command to decrypt a message
            descifrar(n1, pad1, d1)


if __name__ == "__main__":
    main()





