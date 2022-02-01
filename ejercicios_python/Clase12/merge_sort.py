#!/usr/bin/env python3
# merge_sort.py
# 


def merge_sort(lista,cont):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio],cont)
        der = merge_sort(lista[medio:],cont)
        lista_nueva = merge(izq, der)[0]
        cont += merge(izq, der)[1]
    return lista_nueva,cont

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    while(i < len(lista1[0]) and j < len(lista2[0])):
        if (lista1[0][i] < lista2[0][j]):
            resultado.append(lista1[0][i])
            i += 1
        else:
            resultado.append(lista2[0][j])
            j += 1
        cont = i+j
    resultado += lista1[0][i:]
    resultado += lista2[0][j:]
    return resultado,cont


if __name__ == '__main__':
    print(merge_sort([3, 1, 0, 4, 2],0))