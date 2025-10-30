import rsa

texto = "En medio del bosque, donde los árboles parecían susurrar historias de otros tiempos, una pequeña brújula giraba sin rumbo sobre una roca. Nadie sabía quién la había dejado allí, pero cada amanecer apuntaba a un lugar distinto. Algunos decían que marcaba los sueños perdidos; otros, que señalaba el camino hacia aquello que más se anhela. Mientras tanto, un colibrí observaba desde lo alto, convencido de que incluso los objetos olvidados tienen su propio destino."
n_min = 1000000000
n_max = 1000900000
digitos_padding = 3
n, d, e = rsa.generar_claves(n_min, n_max)
texto_cifrado = rsa.cifrar_cadena_rsa(texto, n, e, digitos_padding)
mensaje_hackeado = rsa.ataque_texto_elegido_pad(texto_cifrado, n, e, digitos_padding)