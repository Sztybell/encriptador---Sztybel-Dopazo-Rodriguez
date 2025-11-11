# Cifrado César
# Desplaza cada letra del mensaje según un número dado

def cifrar_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            resultado += chr((ord(caracter) - base + desplazamiento) % 26 + base)
        else:
            resultado += caracter
    return resultado

def descifrar_cesar(texto, desplazamiento):
    return cifrar_cesar(texto, -desplazamiento)

if __name__ == "__main__":
    mensaje = input("Ingrese un texto: ")
    n = int(input("Ingrese el desplazamiento: "))
    cifrado = cifrar_cesar(mensaje, n)
    print("Texto cifrado:", cifrado)
    print("Texto descifrado:", descifrar_cesar(cifrado, n))
