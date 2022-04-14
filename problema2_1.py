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


def validez_contrasena(minimo, maximo, letra, contrasena):
    """
    comprueba si se cumple la política de repetición de una letra entre un minimo y un maximo numero de veces
    """
    return minimo <= contrasena.count(letra) <= maximo


def formato_texto(texto):
    """
    Hace algunas comprobaciones basicas del input
    """
    return texto and texto[0].isnumeric and texto[-1].isalpha() and ("-" in texto) and (":" in texto)


def separador_texto(texto):
    """
    divide el texto en min,max,letra y contraseña
    """
    lista = texto.split(" ")

    numeros = lista[0].split("-")
    num_min = int(numeros[0])
    num_max = int(numeros[1])

    letra = lista[1][0]

    contrasena = lista[2]

    return num_min, num_max, letra, contrasena


def validez_politica(texto):
    """
    comprueba la validez de la contraseña respecto a la politica
    """

    if formato_texto(texto):

        num_min, num_max, letra, contrasena = separador_texto(texto)

        return validez_contrasena(num_min, num_max, letra, contrasena)

    else:

        #         print("el texto: , ",texto," no tiene el formato correcto")
        return False


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
    input_list = cargar_lista()

    contrasenas_validas = validez_politica_lista(input_list)

    return sum(contrasenas_validas)
