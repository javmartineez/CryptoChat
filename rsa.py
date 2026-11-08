"""
rsa.py

Discrete Mathematics - IMAT
ICAI, Universidad Pontificia Comillas

Group: GP09B
Members:
    - Javier Mochales López
    - Javier Martínez Berenguer

Description:
Library for encrypting and decrypting with the RSA algorithm.
"""
import modular as mod
from typing import Tuple,List
import random


def generar_claves(min_primo:int,max_primo:int)-> Tuple[int,int,int]:
    """Picks two primes between min_primo (included) and max_primo (excluded) and returns
    n,e,d
    where (n,e) is the public key and d the private key for RSA

    Args:
        min_primo (int): Lower bound for the primes p1 and p2 used in the key
        max_primo (int): Upper bound for the primes p1 and p2 used in the key

    Returns:
        n (int): RSA modulus, the product of two primes p1 and p2 such that
            min_primo<=p1, p2 < max_primo
        e (int): Public key exponent for RSA with modulus n=p1*p2
        d (int): Private key exponent for RSA with modulus n

    Raises:
        ValueError: If no pair of distinct primes p1,p2 can be found between min_primo and max_primo
    """
    if min_primo > max_primo:       #Check that the small prime is lower than the large prime
        raise ValueError ("Badly built interval (min > max)")

    lista_primos = mod.lista_primos(min_primo, max_primo)       #get the list of primes between min_primo (included) and max_primo (excluded)
    if len(lista_primos) < 2:      #If the list is empty it is not valid, at least two primes are needed
        raise ValueError("Interval not wide enough")

    p, q = random.sample(lista_primos, k= 2)    #get two distinct random primes from lista_primos

    n = p*q       #RSA modulus
    phi_n = (p-1)*(q-1)     #Euler's phi function of n

    e = 3
    while not mod.coprimos(e, phi_n):      #if exponent 3 is not coprime with phi_n, randomly search for an e until one is found
        e = random.randint(4, phi_n)        #e must always be lower than phi_n

    d = mod.inversa_mod_p(e, phi_n)     #private key of the main user

    return (n, e, d)



def aplicar_padding(m:int, digitos_padding:int)->int:
    """Given a message and a number of padding digits, appends
    digitos_padding random digits to the right of the message

    Args:
        m (int): Message without padding
        digitos_padding (int): Non-negative number of padding digits

    Returns:
        int: integer made of the digits of m followed by digitos_padding random digits.

    Raises: None

    Example:
        aplicar_padding(24,2)=2419
        aplicar_padding(24,2)=2403
        aplicar_padding(24,3)=24718
        aplicar_padding(24,3)=24845
        aplicar_padding(24,0)=24
    """
    if digitos_padding == 0:        #When adding 0 digits, return the number unchanged
        return m
    else:
        vals_padding = random.choices(range(10), k=digitos_padding)       #get "digitos_padding" numbers between 0-9, repetitions allowed
        vals_padding = ''.join(map(str, vals_padding))     #convert the list values to str and join them with an empty delimiter

        m_padded = str(m) + vals_padding       #join the message with the padding
        return int(m_padded)


def eliminar_padding(m:int,digitos_padding:int)->int:
    """Given a message with digitos_padding padding digits at
    its end, removes those random digits and returns
    the remaining digits of the message

    Args:
        m (int): Message with padding
        digitos_padding (int): Non-negative number of padding digits

    Returns:
        int: integer obtained by removing the last digitos_padding digits of m.

    Raises: None

    Example:
        eliminar_padding(2454,1)=245
        eliminar_padding(2454,2)=24
        eliminar_padding(2454,3)=2
        eliminar_padding(2432,2)=24
        eliminar_padding(2432,0)=2432
    """
    if len(str(m)) <= digitos_padding: return 0

    return m if digitos_padding == 0 else int(str(m)[:-digitos_padding])    #if there is no padding return m, otherwise return m without its last "digitos_padding" digits


def cifrar_rsa(m:int,n:int,e:int,digitos_padding:int)->int:
    """Given an integer message m, a modulus and an exponent forming
    an RSA public key, with m<n*10^{-digitos_padding}, and a number
    of padding digits, applies the padding to the message and encrypts it
    using RSA with modulus n and exponent e.

    Args:
        m (int): Original plaintext message (without padding)
        n (int): Modulus of the RSA public key
        e (int): Exponent of the RSA public key
        digitos_padding (int): Non-negative number of padding digits

    Returns:
        int: integer obtained by adding the padding to m and applying RSA.

    Raises: None
    """

    num = aplicar_padding(m, digitos_padding)       #add the padding to the message
    return mod.potencia_mod_p(num, e, n)        #encrypt the padded message


def descifrar_rsa(c:int,n:int,d:int,digitos_padding:int)->int:
    """Given an integer ciphertext c that was encrypted with RSA using
    digitos_padding padding digits at the end of the message, and the
    modulus and private exponent n and d forming the RSA private key whose pair was
    used to encrypt c, decrypts c and removes the padding, returning
    the original message.

    Args:
        c (int): Original plaintext message (without padding)
        n (int): Modulus of the RSA public key used for encryption
        d (int): Exponent of the RSA private key whose pair was used to encrypt c
        digitos_padding (int): Non-negative number of padding digits used to encrypt c

    Returns:
        int: integer obtained by decrypting c using RSA with modulus m and exponent e and then removing the padding from the result.

    Raises: None
    """
    descifrado = eliminar_padding(mod.potencia_mod_p(c, d, n), digitos_padding)       #decrypt the message obtaining the character code and returning the original value
    return descifrado


def codificar_cadena(s:str)->List[int]:
    """Converts a string into the list of
    integers representing the unicode value of each of its characters.

    Args:
        s (str): plain text string

    Returns:
        int: list of integers representing the unicode code of each character of the string s.

    Raises: None.

    Example:
        codificar_cadena("¡Hola mundo!")=[161, 72, 111, 108, 97, 32, 109, 117, 110, 100, 111, 33]
    """
    codes = [ord(character) for character in s]     #convert the message into character codes

    return codes




def decodificar_cadena(m:List[int])->str:
    """Converts a list of integers representing unicode characters
    into the string they represent.

    Args:
        m (List[int]): list of integers representing the unicode codes of a string.

    Returns:
        str: the string they represent

    Raises:
        ValueError: If any of the integers is not a valid unicode character.

    Example:
        decodificar_cadena([161, 72, 111, 108, 97, 32, 109, 117, 110, 100, 111, 33])="¡Hola mundo!"
    """

    try:
        return ''.join(chr(num) for num in m)       #join the characters represented by each element of the list

    except (TypeError, ValueError) as e:        #check that every value is valid Unicode
        raise ValueError("Some element is not a valid Unicode integer") from e



def cifrar_cadena_rsa(s:str,n:int,e:int,digitos_padding:int)->List[int]:
    """Encrypts a string character by character using RSA with public key (n,e)
    and digitos_padding padding digits at the end of the message, and returns the list of integers
    representing the corresponding encrypted message.
    Args:
        s (str): plaintext
        n (int): RSA modulus
        e (int): RSA public key
        digitos_padding (int): non-negative number of padding digits to use when encrypting the message.

    Returns:
        List[int]: list of integers representing the message encrypted with RSA for the given key.

    Raises: None
    """
    cifrado = []    #stores the encrypted values
    for valor in s:     #encrypt each value of the message separately
        valor_cifrado = cifrar_rsa(ord(valor), n, e, digitos_padding)
        cifrado.append(valor_cifrado)

    return cifrado


def descifrar_cadena_rsa(cList:List[int],n:int,d:int,digitos_padding:int)->str:
    """Given a message encrypted with RSA using the public key whose associated private key is (n,d)
    and digitos_padding padding digits at the end of the message, returns the original string.
    Args:
        cList (List[int]): list of integers representing the encrypted message
        n (int): RSA modulus
        d (int): RSA private key
        digitos_padding (int): non-negative number of padding digits used to encrypt cList.

    Returns:
        str: string with the plaintext corresponding to the encrypted message cList.

    Raises:
        ValueError: If, after decoding, any of the integers of the message is not a valid unicode character.
    """
    mensaje = ""        #string where the decrypted message is built
    for c in cList:     #iterate over each encrypted value
        try:
            descifrado = chr(descifrar_rsa(c, n, d, digitos_padding))
            mensaje += descifrado       #append the decrypted value to the message

        except (TypeError, ValueError) as e:        #check that every value is valid Unicode
            raise ValueError("Some element is not a valid Unicode integer") from e

    return mensaje


def romper_clave(n:int,e:int)->int:
    """From a valid public key (n,e), recovers the private key d such that
    de = 1 (mod phi(n)).

    Args:
        n (int): RSA modulus
        e (int): RSA public key

    Returns:
        int: private key d

    Raises:
        ValueError: If there is no private key d compatible with the public key (n,e).
    """
    try:
        d = mod.inversa_mod_p(e, mod.euler(n))      #cracked private key
        return d
    except (ZeroDivisionError, ValueError) as e:        #check that every value is valid Unicode
            raise ValueError("There is no private key d compatible with the public key") from e


def ataque_texto_elegido(cList:List[int],n:int,e:int)->str:
    """Runs a chosen-plaintext attack on a message that has been encrypted
    with plain RSA without padding, using only its public key.

    Args:
        cList (List[int]): list of integers representing the encrypted message
        n (int): RSA modulus
        e (int): RSA public key

    Returns:
        str: decrypted plaintext for the encrypted message cList

    Raises:
        ValueError: If the message does not correspond to any plaintext encoded with RSA without padding.
    """
    #Main idea: using the public key, we build a codebook with every
    #possible encoded m for each character. The dictionary is filled
    #as we go through the list.


    codebook = {}

    for i in range(256):
        #use the public key to generate the code dictionary
        chr_coded = mod.potencia_mod_p(i, e, n)
        codebook[chr_coded] = i

    #go through the list to build the message
    m = []
    for chr_coded in cList:
        if chr_coded in codebook:
            m.append(chr(codebook[chr_coded]))
        else:
            raise ValueError ("Message does not correspond to any plaintext encoded with RSA without padding")

    #convert the message to a string
    m_str = ''.join(m)
    return m_str

def ataque_texto_elegido_pad(cList: List[int], n, e, digitos_padding: int) -> str:
    d = romper_clave(n, e)
    mensaje = descifrar_cadena_rsa(cList, n, d, digitos_padding)
    print(mensaje)


if __name__ == "__main__":
    #assert(rsa.eliminar_padding(rsa.aplicar_padding(m,digitos_padding),digitos_padding)==m)
    print(eliminar_padding(aplicar_padding(1,1),1))
