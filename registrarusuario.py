import modular as mod
import random

def main(): 
    print("=== Bienvenido a CriptoChat === \n")
    print("Regístrate para continuar \n")
    nombre = input("Nombre: ")
    p1 = int(input("Valor minimo para generar clave RSA: "))
    p2 = int(input("Valor minimo para generar clave RSA: "))
    pad_values = int(input("Número de cifras pading: "))

    n, e, d = determinar_valores(p1, p2)
    escribir_fichero(nombre, n, e, d, pad_values)

def determinar_valores(p1, p2):
    
    lista_primos = mod.lista_primos(p1, p2)
    p = random.choice(lista_primos)
    q = random.choice(lista_primos)

    n = p * q 
    phi_n = (p-1)*(q-1)

    e = 2
    while not mod.coprimos(e, phi_n):
        e = random.randint(2, phi_n)

    d = mod.inversa_mod_p(e, phi_n)

    return n, e, d

def escribir_fichero(nombre:str, n:int, e:int, d:int, pad_values:int):
    
    with open(f"Usuarios/pub_{nombre}.txt", "w", encoding="UTF-8") as pub_file: 
        pub_file.write(f"{n}\n")
        pub_file.write(f"{e}\n")
        pub_file.write(f"{pad_values}")
    
    with open(f"Usuarios/priv_{nombre}.txt", "w", encoding="UTF-8") as priv_file:
        priv_file.write(f"{d}")
        


if __name__ == "__main__":
    main()