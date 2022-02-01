#!/usr/bin/env python3

#%% Ejercicio 12.1
print('lista : [0, 9, 3, 8, 5, 3, 2, 4]')
print('pasos algoritmo ordenamiento por selección')
print('[0, 9, 3, 8, 5, 3, 2, 4]')
print('[0, 4, 3, 8, 5, 3, 2, 9]')
print('[0, 4, 3, 2, 5, 3, 8, 9]')
print('[0, 4, 3, 2, 3, 5, 8, 9]')
print('[0, 3, 3, 2, 4, 5, 8, 9]')
print('[0, 3, 2, 3, 4, 5, 8, 9]')
print('[0, 2, 3, 3, 4, 5, 8, 9]')
print('pasos algoritmo ordenamiento por inserción')
print('[0, 9, 3, 8, 5, 3, 2, 4]')
print('[0, 9, 3, 8, 5, 3, 2, 4]')
print('[0, 3, 9, 8, 5, 3, 2, 4]')
print('[0, 3, 8, 9, 5, 3, 2, 4]')
print('[0, 3, 5, 8, 9, 3, 2, 4]')
print('[0, 3, 3, 5, 8, 9, 2, 4]')
print('[0, 2, 3, 3, 5, 8, 9, 4]')
print('[0, 2, 3, 3, 4, 5, 8, 9]')
#%% 12.4
import random


def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    n = len(lista) - 1
    cont = 0
    while n > 0:
        p = buscar_max(lista, 0, n)
        cont += n
        lista[p], lista[n] = lista[n], lista[p]
        n = n - 1
    return cont

def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""
    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max

def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    cont = 0
    for i in range(len(lista) - 1):
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)
            cont += (i+1)
    return cont

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""
    v = lista[p]
    j = p
    while j > 0 and v < lista[j - 1]:
        lista[j] = lista[j - 1]
        j -= 1
    lista[j] = v

def ord_burbujeo(lista):
    n = len(lista)
    cont = 0
    for i in range(n-1):
        for j in range(n-1):
            if lista[j] > lista[j+1]:
                cont += 1
                aux = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = aux
    return cont

def generar_lista(N):
    lista = []
    for i in range(N):
        lista.append(random.randint(1,1000))
    return lista

def experimento(N):
    lista = generar_lista(N)
    lista_1 = lista.copy()
    lista_2 = lista.copy()
    lista_3 = lista.copy()
    result = [ord_seleccion(lista_1), ord_insercion(lista_2),
             ord_burbujeo(lista_3)]
    return result

def experimento_global(N,k):
    contador = [0, 0, 0] #[cont_sel, cont_ins, cont_bur]
    promedios = [0, 0, 0] #[prom_sel, prom_ins, prom_bur]
    for i in range(k):
        for i in range(3):
            contador[i] += experimento(N)[i]
    for i in range(3):
        promedios[i] = contador[i]/k
    print(f'Promedios:')
    print(f'SELECCION     INSERCION     BURBUJEO')
    print(f'{promedios[0]:>9}     {promedios[1]:>9}     {promedios[2]:>8}')


if __name__ == '__main__':
    experimento_global(10,100)