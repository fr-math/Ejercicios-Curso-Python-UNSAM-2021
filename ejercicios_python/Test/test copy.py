

def merge_sort(lista, comp=0):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    
    if comp == False:
        comp = 0
    lista_nueva = []
    
    if len(lista) < 2:
        lista_nueva = lista
        comp += 1
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio], comp)
        der = merge_sort(lista[medio:], comp)
        lista_aux, comp_aux = merge(izq, der)
        lista_nueva = lista_aux
        comp += comp_aux
        comp += 1
    return lista_nueva, comp

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    comp = lista1[1] + lista2[1]
    
    while(i < len(lista1[0]) and j < len(lista2[0])):
        print(type(lista1[0][i]), '\t', type(lista2[0][j]) )
        if (lista1[0][i] < lista2[0][j]):
            resultado.append(lista1[0][i])
            i += 1
            comp += 1
        else:
            resultado.append(lista2[0][j])
            j += 1
            comp += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado, comp


if __name__ == '__main__':
    print(merge_sort([5,4,3,2,1]))