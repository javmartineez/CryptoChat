import modular as mod
import rsa

def main():
    """
    Main function in charge of creating new users and their
    corresponding files (public and private). These files contain:
    Public
        n, e: public key
        padding digits
    Private:
        d: private key

    Args:
        None
    Returns:
        None
    Exceptions:
        None
    """

    print("=== Welcome to CriptoChat === \n")
    print("Sign up to continue \n")
    nombre = input("Name: ")
    min_primos = int(input("Minimum value to generate the RSA key: "))
    max_primos = int(input("Minimum value to generate the RSA key: "))
    pad_values = int(input("Number of padding digits: "))

    n, e, d = rsa.generar_claves(min_primos, max_primos)        #user's public and private key
    escribir_fichero(nombre, n, e, d, pad_values)       #create the file with the user's keys


def escribir_fichero(nombre:str, n:int, e:int, d:int, pad_values:int) -> None:
    """
    Opens the files and writes the values computed
    for each new user.

    Args:
        - nombre: name of the new user
        - n, e: public key
        - d: private key
        - pad_values: padding digits

    Returns:
        None
    Exceptions:
        None
    """
    with open(f"Usuarios/pub_{nombre}.txt", "w", encoding="UTF-8") as pub_file:     #open a new file with the public keys of "nombre"

        pub_file.write(f"{n}\n")        #RSA modulus
        pub_file.write(f"{e}\n")        #RSA exponent
        pub_file.write(f"{pad_values}")     #RSA padding digits

    with open(f"Usuarios/priv_{nombre}.txt", "w", encoding="UTF-8") as priv_file:   #open a new file with the private key of "nombre"
        priv_file.write(f"{d}")



if __name__ == "__main__":
    main()
