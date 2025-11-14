import customtkinter as ctk
import tkinter.messagebox as messagebox

# =========================
#  CIFRADO VIGENERE
# =========================

class Vigenere:
    def __init__(self, texto, clave):
        self.texto = texto.lower()
        self.clave = clave.lower()

    def cifrar(self):
        resultado = ""
        clave_extendida = ""
        indice_clave = 0

        for letra in self.texto:
            if letra.isalpha():
                clave_extendida += self.clave[indice_clave % len(self.clave)]
                indice_clave += 1
            else:
                clave_extendida += letra

        for i in range(len(self.texto)):
            letra = self.texto[i]
            if letra.isalpha():
                desplazamiento = ord(clave_extendida[i]) - ord('a')
                letra_cifrada = chr((ord(letra) - ord('a') + desplazamiento) % 26 + ord('a'))
                resultado += letra_cifrada
            else:
                resultado += letra

        return resultado

    def descifrar(self):
        resultado = ""
        clave_extendida = ""
        indice_clave = 0

        for letra in self.texto:
            if letra.isalpha():
                clave_extendida += self.clave[indice_clave % len(self.clave)]
                indice_clave += 1
            else:
                clave_extendida += letra

        for i in range(len(self.texto)):
            letra = self.texto[i]
            if letra.isalpha():
                desplazamiento = ord(clave_extendida[i]) - ord('a')
                letra_descifrada = chr((ord(letra) - ord('a') - desplazamiento) % 26 + ord('a'))
                resultado += letra_descifrada
            else:
                resultado += letra

        return resultado


# =========================
#  CIFRADO PLAYFAIR
# =========================

class Playfair:
    def __init__(self, texto, clave):
        self.texto = texto.lower().replace("j", "i")
        self.clave = clave.lower().replace("j", "i")

    def armar_matriz(self):
        letras = ""
        for c in self.clave:
            if c not in letras and c.isalpha():
                letras += c
        for c in "abcdefghijklmnopqrstuvwxyz":
            if c not in letras and c != "j":
                letras += c
        matriz = [list(letras[i:i+5]) for i in range(0, 25, 5)]
        return matriz

    def buscar_pos(self, matriz, letra):
        for i in range(5):
            for j in range(5):
                if matriz[i][j] == letra:
                    return i, j
        return None

    def procesar_texto(self):
        texto = self.texto.replace(" ", "")
        pares = []
        i = 0

        while i < len(texto):
            a = texto[i]
            if i + 1 < len(texto):
                b = texto[i+1]
                if a == b:
                    b = "x"
                    pares.append(a + b)
                    i += 1
                else:
                    pares.append(a + b)
                    i += 2
            else:
                pares.append(a + "x")
                i += 1
        return pares

    def cifrar(self):
        matriz = self.armar_matriz()
        pares = self.procesar_texto()
        resultado = ""

        for par in pares:
            a, b = par
            fila_a, col_a = self.buscar_pos(matriz, a)
            fila_b, col_b = self.buscar_pos(matriz, b)

            if fila_a == fila_b:
                resultado += matriz[fila_a][(col_a + 1) % 5]
                resultado += matriz[fila_b][(col_b + 1) % 5]
            elif col_a == col_b:
                resultado += matriz[(fila_a + 1) % 5][col_a]
                resultado += matriz[(fila_b + 1) % 5][col_b]
            else:
                resultado += matriz[fila_a][col_b]
                resultado += matriz[fila_b][col_a]

        return resultado

    def descifrar(self):
        matriz = self.armar_matriz()
        pares = self.procesar_texto()
        resultado = ""

        for par in pares:
            a, b = par
            fila_a, col_a = self.buscar_pos(matriz, a)
            fila_b, col_b = self.buscar_pos(matriz, b)

            if fila_a == fila_b:
                resultado += matriz[fila_a][(col_a - 1) % 5]
                resultado += matriz[fila_b][(col_b - 1) % 5]
            elif col_a == col_b:
                resultado += matriz[(fila_a - 1) % 5][col_a]
                resultado += matriz[(fila_b - 1) % 5][col_b]
            else:
                resultado += matriz[fila_a][col_b]
                resultado += matriz[fila_b][col_a]

        return resultado


# =========================
#  CIFRADO RSA
# =========================

class RSA:
    def generar_claves(self):
        p = 11
        q = 13
        n = p * q
        phi = (p - 1) * (q - 1)
        e = 5

        d = pow(e, -1, phi)

        return (e, n), (d, n)

    def cifrar(self, mensaje, clave_publica):
        e, n = clave_publica
        return pow(mensaje, e, n)

    def descifrar(self, cifrado, clave_privada):
        d, n = clave_privada
        return pow(cifrado, d, n)


# =========================
#  INTERFAZ GRAFICA
# =========================

class MenuPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Encriptador")
        self.geometry("600x450")

        ctk.CTkLabel(self, text="Seleccioná un método de cifrado:", font=("Arial", 18)).pack(pady=20)

        ctk.CTkButton(self, text="Vigenère", command=self.abrir_vigenere).pack(pady=10)
        ctk.CTkButton(self, text="Playfair", command=self.abrir_playfair).pack(pady=10)
        ctk.CTkButton(self, text="RSA", command=self.abrir_rsa).pack(pady=10)

    def abrir_vigenere(self):
        VigenereVentana()

    def abrir_playfair(self):
        PlayfairVentana()

    def abrir_rsa(self):
        RSAVentana()


# =========================
#  VENTANAS INDIVIDUALES
# =========================

class VigenereVentana(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Vigenère")
        self.geometry("500x350")

        ctk.CTkLabel(self, text="Texto:").pack()
        self.texto = ctk.CTkEntry(self, width=400)
        self.texto.pack()

        ctk.CTkLabel(self, text="Clave:").pack()
        self.clave = ctk.CTkEntry(self, width=400)
        self.clave.pack()

        ctk.CTkButton(self, text="Cifrar", command=self.cifrar).pack(pady=10)
        ctk.CTkButton(self, text="Descifrar", command=self.descifrar).pack(pady=5)

        self.resultado = ctk.CTkTextbox(self, width=450, height=100)
        self.resultado.pack(pady=10)

    def cifrar(self):
        vig = Vigenere(self.texto.get(), self.clave.get())
        self.resultado.delete("1.0", "end")
        self.resultado.insert("end", vig.cifrar())

    def descifrar(self):
        vig = Vigenere(self.texto.get(), self.clave.get())
        self.resultado.delete("1.0", "end")
        self.resultado.insert("end", vig.descifrar())


class PlayfairVentana(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Playfair")
        self.geometry("500x350")

        ctk.CTkLabel(self, text="Texto:").pack()
        self.texto = ctk.CTkEntry(self, width=400)
        self.texto.pack()

        ctk.CTkLabel(self, text="Clave:").pack()
        self.clave = ctk.CTkEntry(self, width=400)
        self.clave.pack()

        ctk.CTkButton(self, text="Cifrar", command=self.cifrar).pack(pady=10)
        ctk.CTkButton(self, text="Descifrar", command=self.descifrar).pack(pady=5)

        self.resultado = ctk.CTkTextbox(self, width=450, height=100)
        self.resultado.pack(pady=10)

    def cifrar(self):
        pf = Playfair(self.texto.get(), self.clave.get())
        self.resultado.delete("1.0", "end")
        self.resultado.insert("end", pf.cifrar())

    def descifrar(self):
        pf = Playfair(self.texto.get(), self.clave.get())
        self.resultado.delete("1.0", "end")
        self.resultado.insert("end", pf.descifrar())


class RSAVentana(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("RSA")
        self.geometry("500x350")

        self.rsa = RSA()
        self.pub, self.priv = self.rsa.generar_claves()

        ctk.CTkLabel(self, text=f"Clave pública: e={self.pub[0]}, n={self.pub[1]}").pack(pady=5)
        ctk.CTkLabel(self, text=f"Clave privada: d={self.priv[0]}, n={self.priv[1]}").pack(pady=5)

        ctk.CTkLabel(self, text="Número a cifrar: (solo números)").pack()
        self.numero = ctk.CTkEntry(self, width=200)
        self.numero.pack()

        ctk.CTkButton(self, text="Cifrar", command=self.cifrar).pack(pady=10)
        ctk.CTkButton(self, text="Descifrar", command=self.descifrar).pack(pady=5)

        self.resultado = ctk.CTkTextbox(self, width=450, height=100)
        self.resultado.pack(pady=10)

    def cifrar(self):
        try:
            n = int(self.numero.get())
            cif = self.rsa.cifrar(n, self.pub)
            self.resultado.delete("1.0", "end")
            self.resultado.insert("end", str(cif))
        except:
            messagebox.showerror("Error", "Ingresá un número válido.")

    def descifrar(self):
        try:
            n = int(self.numero.get())
            dec = self.rsa.descifrar(n, self.priv)
            self.resultado.delete("1.0", "end")
            self.resultado.insert("end", str(dec))
        except:
            messagebox.showerror("Error", "Ingresá un número válido.")


# =========================
#  EJECUTAR APP
# =========================

app = MenuPrincipal()
app.mainloop()
