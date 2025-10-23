import sys
import os
import rsa
import excepciones as ex


def sacar_ficheros(user1: str, user2: str) -> list[str,str,str]:
    """
    Función encargada de obtener las rutas de los ficheros con las claves pública y privada de user1 y la clave
    pública de user2. Además confirma que existen las rutas lanzando un error en caso contrario.
    Args:
        -user1: usuario principal del que obtenemos las claves pública y privada.
        -user2: usuario secundario del que obtenemos únicamente la clave pública.

    Returns:
        -paths: lista de las rutas de los diferentes ficheros.

    Raises:
        -PathError: en caso de no existir la ruta a las claves del usuario asignado.
    """
    paths = []      #lista donde guardar las rutas
    path1_public = f"Usuarios/pub_{user1}.txt"      #ruta pública del primer usuario
    paths.append(path1_public)
    path1_priv = f"Usuarios/priv_{user1}.txt"       #ruta privada del primer usuario
    paths.append(path1_priv)
    path2_public = f"Usuarios/pub_{user2}.txt"      #ruta pública del segundo usuario
    paths.append(path2_public)

    for path in paths:
        if not os.path.exists(path):        #comprobamos la existencia de las rutas
            raise ex.PathError("No se encuentran las claves de todos los usuarios")
    return paths

def leer_claves(fichero: str) -> list[int]:
    """
    Lee el contenido de fichero donde se encuentran las claves guardándolas en una lista.
    Args:
        -fichero: ruta del fichero a leer.

    Returns:
        -lista: lista con las claves en formato int.

    Raises: None.
    """
    lista = []      #lista donde guardar las claves
    with open(fichero) as f:        #abrimos el fichero con el nombre de f
        for linea in f:     #leemos línea a línea
            linea = int(linea.strip())      #limpia el salto de línea y cambia el tipo a int
            lista.append(linea)
    return lista


def cifrar(n: int, e: int, pad: int) -> None:
    """
    Función que se encarga de tomar el texto a cifrar y mandarlo a la librería rsa.
    Una vez se obtiene el texto cifrado se muestra por pantalla.
    Args:
        -n: módulo para RSA.
        -e: exponente para RSA.
        -pad: número de dígitos de padding que deben usarse para el cifrado del mensaje.

    Returns: None.

    Exceptions:
        -NegativeValue: en caso de tener pad con un valor negativo.
    """
    if pad < 0:
        raise ex.NegativeValue("El número de digitos del padding no puede ser negativo")
    
    text = input("Texto para cifrar: ")
    cifrado = rsa.cifrar_cadena_rsa(text, n, e, pad)        #obtenemos el texto cifrado en forma de lista por cada valor del texto
    print(f"Texto cifrado: {cifrado}")      #mostramos el texto cifrado


def descifrar(n: int, pad: int, d: int) -> None:
    """
    Función que se encarga de tomar un texto cifrado y mandarlo a la librería rsa para
    descrifarlo. Una vez descifrado, lo muestra por pantalla.
    Args:
        -n: módulo para RSA.
        -pad: número de dígitos de padding que deben usarse para el descifrado del mensaje.
        -d: clave privada para RSA.

    Returns: None.

    Exceptions:
        -NegativeValue: en caso de tener pad con un valor negativo.
    """
    if pad < 0:
        raise ex.NegativeValue("El número de digitos del padding no puede ser negativo")
    
    text = input("Texto a descifrar: ")
    lista = list(map(int,text.split(" ")))      #el texto obtenido lo convertimos en una lista de ints
    descifrado = rsa.descifrar_cadena_rsa(lista, n, d, pad)     #desciframos el texto
    print(f"Texto descifrado: {descifrado}")        #mostramos el texto descrifrado

def users() -> tuple[str,str]:
    """
    Obtiene los usuarios enviados por terminal a modo de argumentos.
    Args: None.

    Returns:
        -user1: usuario principal.
        -user2: usuario secundario.

    Raises:None
    """
    arguments = sys.argv[1:]        #obtenemos los argumentos desde el segundo al final (el primero es el módulo ejecutado criptochat.py)
    user1 = arguments[0]            #Primer usuario
    user2 = arguments[1]            #Segundo usuario
    return (user1, user2)

def main():
    """
    Función principal que ejecuta el resto del código.
    """
    user1, user2 = users()      #obtiene los usuarios

    path1_pub, path1_priv, path2_pub = sacar_ficheros(user1, user2)     #obtiene las rutas de los diferentes ficheros

    n1, e1, pad1 = leer_claves(path1_pub)       #Claves públicas del primer usuario
    n2, e2, pad2 = leer_claves(path2_pub)       #Claves públicas del segundo usuario
    d1, = leer_claves(path1_priv)               #Clave privada del primer usuario

    actividad = ""
    while actividad != "S":     #bucle de interación que finaliza con el argumento S/s
        actividad = input("cifrar (C), descifrar (D) o salir (S): ").upper()        #pide al usuario el comando a ejecutar
        if actividad == "C":        #comando para cifrar un mensaje
            cifrar(n2, e2, pad2)
        elif actividad == "D":      #comando para descifrar un mensaje
            descifrar(n1, pad1, d1)


if __name__ == "__main__":
    main()


    
    


