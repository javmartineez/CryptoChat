import modular as mod
import rsa 

def main(): 
    """
    Función principal de ejecución encargada de crear nuevos usuarios y sus 
    correspondientes ficheros (público y privado). Dichos ficheros contienen: 
    Público
        n, e: clave pública 
        cifras de padding
    Privado: 
        d: clave privada

    Args: 
        None 
    Returns: 
        None
    Exceptions:
        None
    """

    print("=== Bienvenido a CriptoChat === \n")
    print("Regístrate para continuar \n")
    nombre = input("Nombre: ")
    min_primos = int(input("Valor minimo para generar clave RSA: "))
    max_primos = int(input("Valor minimo para generar clave RSA: "))
    pad_values = int(input("Número de cifras pading: "))

    n, e, d = rsa.generar_claves(min_primos, max_primos)        #clave pública y privada del usuario
    escribir_fichero(nombre, n, e, d, pad_values)       #crea el fichero con las claves del usuario


def escribir_fichero(nombre:str, n:int, e:int, d:int, pad_values:int) -> None:
    """
    Función encargada de abrir los ficheros y escribir los valores calculados
    para cada nuevo usuario.

    Args: 
        - nombre: Nombre del nuevo usuario
        - n, e: clave publica
        - d: clave privada
        - pad_values: cifras de padding

    Returns:
        None
    Exceptions:
        None
    """
    with open(f"Usuarios/pub_{nombre}.txt", "w", encoding="UTF-8") as pub_file:     #abre un nuevo fichero con las claves públicas de "nombre"

        pub_file.write(f"{n}\n")        #módulo para RSA
        pub_file.write(f"{e}\n")        #exponente para RSA
        pub_file.write(f"{pad_values}")     #digitos del padding para RSA
    
    with open(f"Usuarios/priv_{nombre}.txt", "w", encoding="UTF-8") as priv_file:   #abre un nuevo fichero con la clave privada de "nombre"
        priv_file.write(f"{d}")
        


if __name__ == "__main__":
    main()