# ---------------------------- Problema1 1 --------------------------

def es_multiplo(numero, multiplo):
    return not bool(numero % multiplo)


def problema1():
    cadena = list(range(1, 100))
    cadena_nueva = []

    for numero in cadena:
        multiplo_de_tres = es_multiplo(numero, 3)
        multiplo_de_cinco = es_multiplo(numero, 5)
        
        if multiplo_de_tres and multiplo_de_cinco:
            cadena_nueva.append("cyberclick")

        elif multiplo_de_tres:
            cadena_nueva.append("cyber")

        elif multiplo_de_cinco:
            cadena_nueva.append("click")        

        else:
            cadena_nueva.append(numero)
            
    return cadena_nueva
