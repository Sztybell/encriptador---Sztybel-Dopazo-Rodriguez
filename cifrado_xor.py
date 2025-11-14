# Cifrado XOR en Python
# Hecho para mostrar cómo funciona de forma sencilla

# Pedimos al usuario que escriba el texto
texto = input("Escribí el texto que querés encriptar o desencriptar: ")

# Pedimos una clave (un número cualquiera)
clave = int(input("Poné una clave numérica (por ejemplo 7): "))

# Variable donde guardamos el resultado
resultado = ""

# Recorremos letra por letra el texto
for letra in texto:
    # Usamos XOR (^) entre el código ASCII de la letra y la clave
    cifrado = ord(letra) ^ clave
    # Convertimos el número resultante otra vez a letra
    resultado += chr(cifrado)

# Mostramos el texto cifrado o descifrado (es el mismo proceso)
print("\nResultado:")
print(resultado)

# Nota:
# Si copiás el resultado y lo pasás otra vez por el programa con la misma clave,
# vas a recuperar el texto original (así funciona XOR).
