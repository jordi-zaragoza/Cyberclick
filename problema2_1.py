# ---------------------------- Problema1 2: Parte 1 --------------------------

def test1():
    """
    prueba que el resultado funciona para los ejemplos dados
    True -> Pasa el test
    """
    textos = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
    validez = [True, False, True]

    resultado = validez_politica_lista(textos)

    return resultado == validez


class Texto_input:
    def __init__(self,texto):
        """
        divide el texto en min,max,letra y contraseña
        """
        lista = texto.split(" ")

        numeros = lista[0].split("-")
        self.primer_numero = int(numeros[0])
        self.segundo_numero = int(numeros[1])
        self.letra = lista[1][0]
        self.contrasena = lista[2]


def validez_contrasena(texto_input):
    """
    comprueba si se cumple la política de repetición de una letra entre un minimo y un maximo numero de veces
    """
    minimo = texto_input.primer_numero
    maximo = texto_input.segundo_numero
    contrasena = texto_input.contrasena
    letra = texto_input.letra
    return minimo <= contrasena.count(letra) <= maximo


def formato_correcto(texto):
    """
    Hace algunas comprobaciones basicas del input
    """
    return texto and texto[0].isnumeric and texto[-1].isalpha() and ("-" in texto) and (":" in texto)


def validez_politica(texto):
    """
    comprueba la validez de la contraseña respecto a la politica
    """
    return validez_contrasena(Texto_input(texto)) if formato_correcto(texto) else False


def validez_politica_lista(lista_texto):
    """
    Nos devuelve una lista con los resultados True o False de la validez de la contraseña según la política
    """
    return [validez_politica(texto) for texto in lista_texto]


def cargar_lista():
    txt_file = open("input.txt", "r")
    file_content = txt_file.read()
    input_list = file_content.split("\n")
    return input_list


def problema2():
    """
    Función de resultado del problema 2 parte 1
    """
    return sum(validez_politica_lista(cargar_lista()))
