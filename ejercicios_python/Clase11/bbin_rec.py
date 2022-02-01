#!/usr/bin/env python3
# larenga.py
# Ejercicio 11.13

def bbinaria_rec(lista, e):
    '''Toma una lista y un elemento y devuelve si el elemento está en la 
    lista.'''
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = (lista[0] == e)
    else:
        medio = len(lista)//2
        if lista[medio] <= e:
            res = bbinaria_rec(lista[medio:],e)
        else:
            res = bbinaria_rec(lista[:medio],e)
    return res

if __name__ == '__main__':
    #e1 = 5
    #e2 = 2
    e1 = 19
    e2 = 20
    lista = [_ for _ in range(0,25,2)]
    print(f'{e1} está en {lista} ?: {bbinaria_rec(lista, e1)}')
    print(f'{e2} está en {lista} ?: {bbinaria_rec(lista, e2)}')