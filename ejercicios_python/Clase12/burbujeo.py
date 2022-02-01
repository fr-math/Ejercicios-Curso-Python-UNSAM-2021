#!/usr/bin/env python3
# burbujeo.py
# Ejercicio 12.2


def ord_burbujeo(lista):
    '''Ordena una lista por el método de la burbuja. 
    Pre: Los elementos de la lista deben ser comparables.
    Post: Devuelve una nueva lista con los elementos de la original ordenados. 
    No modifica la lista original. El orden de ordenamiento es 'creciente'.'''
    n = len(lista)
    lista = lista.copy()
    for i in range(n-1):
        for j in range(n-1):
            if lista[j] > lista[j+1]:
                aux = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = aux
    return lista


if __name__ == '__main__':
    lista_1 = [1, 2, -3, 8, 1, 5]
    lista_2 = [1, 2, 3, 4, 5]
    lista_3 = [0, 9, 3, 8, 5, 3, 2, 4]
    lista_4 = [10, 8, 6, 2, -2, -5]
    lista_5 = [2, 5, 1, 0]
    lista_6 = [1,-1,1,-1,1,-1,0]
    print(lista_1,' --> ',ord_burbujeo(lista_1))
    print(lista_2,' --> ',ord_burbujeo(lista_2))
    print(lista_3,' --> ',ord_burbujeo(lista_3))
    print(lista_4,' --> ',ord_burbujeo(lista_4))
    print(lista_5,' --> ',ord_burbujeo(lista_5))
    print(lista_6,' --> ',ord_burbujeo(lista_6))
    