
def propagar(vector):
    hubo_cambios = 0
    # Creo una copia exacta de la lista
    # Pero que no tiene el mismo puntero
    # Que la lista original
    vector_nuevo = vector[:]
    length = len(vector_nuevo)
    for ind, elem in enumerate(vector_nuevo):
        if elem == 1:
            # Si no estamos en el indice = 0
            # Y si el elemento del indice anterior es 0
            # Prende fuego el fosforo
            # Marca la variable `hubo_cambios`
            if (ind != 0) and (vector[ind - 1] == 0):
                vector_nuevo[ind-1] = 1
                hubo_cambios = 1
            # Si el indice posterior no es el último (length)
            # Y si el elemento del indice posterior es 0
            # Prende fuego el fosforo
            # Marca la variable `hubo_cambios`
            if (ind + 1 < length) and (vector[ind + 1] == 0):
                vector_nuevo[ind + 1] = 1
                hubo_cambios = 1
    # Si hubo cambios en la funcion
    # Es necesario corroborar si debe haber mas
    # Llamada recursiva a la funcion (se llama a si misma)
    if hubo_cambios:
        return propagar(vector_nuevo)
    return vector_nuevo


lista_1 = [0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0]
# propagar(lista_1)
# [0, 0, 0, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1]

lista_2 = [ 0, 0, 0, 1, 0, 0]
# propagar([ 0, 0, 0, 1, 0, 0])
# [1, 1, 1, 1, 1, 1]


#f = [0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]
#prop = propagar(f)
#print(prop)      


lista_1 = [ 0, 0, 0, 1, 0, 0]
lista_2 = [ 0, 0, 0, 0, 0, -1]
lista_3 = [ 0, 0, 0, 0, 0, 1]
lista_4 = []
lista_5 = [ 0 for _ in range(1000) ] + [1]
lista_6 = [1] + [ 0 for _ in range(1000) ]
lista_7 = [ (i% 6)//2-1 for i in range(200) ]
lista_8 = [ -1*((i% 6)//2-1) for i in range(60) ]
propagada_1 = propagar(lista_1) #
propagada_2 = propagar(lista_2) #
propagada_3 = propagar(lista_3) #
propagada_4 = propagar(lista_4)
propagada_5 = propagar(lista_5) #
propagada_6 = propagar(lista_6) #
propagada_7 = propagar(lista_7) #
propagada_8 = propagar(lista_8) #

#impresion = f'{lista_1}\t-->\t{propagada_1}\n{lista_2}\t-->\t{propagada_2}\n{lista_3}\t-->\t{propagada_3}\n{lista_4}\t-->\t{propagada_4}\n{lista_5}\t-->\t{propagada_5}\n{lista_6}\t-->\t{propagada_6}\n{lista_7}\t-->\t{propagada_7}\n{lista_8}\t-->\t{propagada_8}'
impresion = f'{lista_1}\t-->\t{propagada_1}'
print(impresion)
