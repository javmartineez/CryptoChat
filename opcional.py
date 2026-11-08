import rsa

texto = "In the middle of the forest, where the trees seemed to whisper stories from other times, a small compass spun aimlessly on a rock. Nobody knew who had left it there, but every dawn it pointed to a different place. Some said it marked lost dreams; others, that it showed the way to what one longs for most. Meanwhile, a hummingbird watched from above, convinced that even forgotten objects have their own destiny."
n_min = 1000000000
n_max = 1000900000
digitos_padding = 3
n, d, e = rsa.generar_claves(n_min, n_max)
texto_cifrado = rsa.cifrar_cadena_rsa(texto, n, e, digitos_padding)
mensaje_hackeado = rsa.ataque_texto_elegido_pad(texto_cifrado, n, e, digitos_padding)