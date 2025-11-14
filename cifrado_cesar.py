# Cifrado César
# En este cifrado se corre cada letra una cantidad fija de lugares en el abecedario.
# Ejemplo: con desplazamiento 3, la A pasa a ser D, la B pasa a ser E, etc.

texto = input("Escribí el texto que querés cifrar o descifrar: ").upper()
desp = int(input("Cuántos lugares querés desplazar: "))
modo = input("Querés (E)ncriptar o (D)esencriptar?: ").upper()

resultado = ""

for letra in texto:
    if letra.isalpha():  # Solo trabaja con letras, deja el resto igual
        base = 65  # El código ASCII de 'A'
        if modo == "D":
            # Para desencriptar, se resta el desplazamiento
            nueva = chr((ord(letra) - base - desp) % 26 + base)
        else:
            # Para encriptar, se suma el desplazamiento
            nueva = chr((ord(letra) - base + desp) % 26 + base)
        resultado += nueva
    else:
        # Si hay espacios o símbolos, los deja igual
        resultado += letra

print("Resultado final:", resultado)
