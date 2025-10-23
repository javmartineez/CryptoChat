import modular as mod
import rsa 
import random

def main(): 
    print("=== Bienvenido a CriptoChat === \n")
    print("Regístrate para continuar \n")
    nombre = input("Nombre: ")
    min_primos = int(input("Valor minimo para generar clave RSA: "))
    max_primos = int(input("Valor minimo para generar clave RSA: "))
    pad_values = int(input("Número de cifras pading: "))

    n, e, d = rsa.generar_claves(min_primos, max_primos)
    escribir_fichero(nombre, n, e, d, pad_values)


def escribir_fichero(nombre:str, n:int, e:int, d:int, pad_values:int):
    
    with open(f"Usuarios/pub_{nombre}.txt", "w", encoding="UTF-8") as pub_file: 
        pub_file.write(f"{n}\n")
        pub_file.write(f"{e}\n")
        pub_file.write(f"{pad_values}")
    
    with open(f"Usuarios/priv_{nombre}.txt", "w", encoding="UTF-8") as priv_file:
        priv_file.write(f"{d}")
        


if __name__ == "__main__":
    main()