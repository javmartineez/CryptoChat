# CryptoChat

**End-to-end encrypted terminal chat built on an RSA implementation written from scratch, plus the attacks that break it.**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Tests](https://img.shields.io/badge/tests-107%20passing-brightgreen?logo=pytest&logoColor=white)
![Dependencies](https://img.shields.io/badge/dependencies-none-lightgrey)

CryptoChat lets two users exchange RSA-encrypted messages from the terminal. Everything underneath is implemented by hand with **no cryptography libraries**: primality testing, the extended Euclidean algorithm, fast modular exponentiation, modular inverses, Euler's totient, key generation and padding. The project also shows *why* textbook RSA is insecure by running a chosen-plaintext attack against unpadded messages and recovering private keys from small moduli.

> Project for the *Discrete Mathematics* course, Universidad Pontificia Comillas (ICAI).

---

## Features

**Number theory library (`modular.py`)**
- Primality: trial division and a deterministic **Miller–Rabin** test; prime listing in an interval.
- Integer factorisation using the 6k ± 1 wheel.
- **Binary GCD** (Stein's algorithm), Bézout coefficients (extended Euclid), n-ary GCD / Bézout.
- **Fast modular exponentiation** (square-and-multiply, with negative exponents via inverses).
- Modular inverse, Euler's φ function, Legendre symbol, modular square roots.
- Systems of linear congruences with **non-coprime moduli** (generalised Chinese Remainder Theorem).

**RSA (`rsa.py`)**
- Key generation from a prime interval.
- Random-digit **padding** and its removal.
- Character-by-character string encryption and decryption.
- **Attacks**: private key recovery from (n, e) by factorising n, and a **chosen-plaintext codebook attack** that decrypts unpadded messages using only the public key.

**Chat (`criptochat.py`, `registrarusuario.py`)**
- User registration generates a key pair stored in `Usuarios/`.
- Interactive session: encrypt with the recipient's public key, decrypt with your own private key.

## Getting started

No external dependencies are needed to run the chat; `pytest` is only needed for the tests.

```bash
git clone https://github.com/javmartineez/CryptoChat.git
cd CryptoChat
```

Register users (creates `Usuarios/pub_<name>.txt` and `Usuarios/priv_<name>.txt`):

```bash
python registrarusuario.py
```

Start a chat session as `javito` talking to `miguel` (demo keys are included):

```bash
python criptochat.py javito miguel
```

```
encrypt (C), decrypt (D) or quit (S): C
Text to encrypt: Hello, CryptoChat!
Encrypted text:  99706533496 81464032764 17138981489 79904673226 ...
```

Break the sample cryptogram, which was encrypted without padding, using only its public key:

```bash
python romper_X.py
```

Run the test suite:

```bash
pip install pytest
python -m pytest -q
```

## Project structure

```
CryptoChat/
├── modular.py            # Modular arithmetic / number theory library
├── rsa.py                # RSA: key generation, padding, encryption, attacks
├── criptochat.py         # Interactive encrypted chat between two users
├── registrarusuario.py   # User registration and key generation
├── romper_X.py           # Chosen-plaintext attack on criptograma_X.txt
├── opcional.py           # Key-recovery attack on a padded message
├── excepciones.py        # Custom exceptions
├── Usuarios/             # Demo key files (toy-sized keys)
├── criptograma_X.txt     # Sample unpadded ciphertext
├── pruebas.ipynb         # Experiments: probabilistic primes and larger keys
└── test_*.py             # 107 pytest tests
```

> ⚠️ **Educational project.** The keys are deliberately small and the padding scheme is not cryptographically secure. Do not use this code to protect real data.

## Tech stack

Python (standard library only) · pytest

## Authors

- **Javier Martínez Berenguer** · [GitHub](https://github.com/javmartineez)
- **Javier Mochales López** · [GitHub](https://github.com/jmochales06)
