# ---------------------------- Problema1 1 --------------------------

def es_multiplo(numero, multiplo):
    """
    Devuelve True o False dependiendo de si es multiplo o no
    
    input:
    numero -> el numero que queremos evaluar
    multiplo -> el multiplo
    
    output:
    devuelve un booleano con la respuesta
    """
    return not bool(numero % multiplo)


def problema1():      
    """
    Esta función devuelve el resultado del problema 1
    """
    
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
