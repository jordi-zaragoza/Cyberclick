# ---------------------------- Problema1 2: Parte 1 --------------------------

def test1():
    textos = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
    validez = [True, False, True]
    return validez == validez_politica_lista(textos)


def problema2():
    return sum(validez_politica_lista(cargar_lista()))


def cargar_lista():
    return open("input.txt", "r").read().split("\n")


def validez_politica_lista(lista_texto):
    return [validez_politica(texto) for texto in lista_texto]


def validez_politica(texto):
    return validez_contrasena(Texto_input(texto)) if formato_correcto(texto) else False


class Texto_input:
    def __init__(self, texto):
        lista = texto.split(" ")
        numeros = lista[0].split("-")
        self.primer_numero = int(numeros[0])
        self.segundo_numero = int(numeros[1])
        self.letra = lista[1][0]
        self.contrasena = lista[2]


def validez_contrasena(texto_input):
    minimo = texto_input.primer_numero
    maximo = texto_input.segundo_numero
    contrasena = texto_input.contrasena
    letra = texto_input.letra
    return minimo <= contrasena.count(letra) <= maximo


def formato_correcto(texto):
    return texto and texto[0].isnumeric and texto[-1].isalpha() and ("-" in texto) and (":" in texto)