#!/usr/bin/env python3
# time_ordenamiento.py
# Ejercicio 12.8

import numpy as np
import matplotlib.pyplot as plt
import time
import timeit as tt


def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    n = len(lista) - 1
    while n > 0:
        p = buscar_max(lista, 0, n)
        lista[p], lista[n] = lista[n], lista[p]
        n = n - 1

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
    for i in range(len(lista) - 1):
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)

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
    for i in range(n-1):
        for j in range(n-1):
            if lista[j] > lista[j+1]:
                aux = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = aux

def ord_mezcla(lista):
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = ord_mezcla(lista[:medio])
        der = ord_mezcla(lista[medio:])
        lista_nueva = mezcla(izq,der)
    return lista_nueva

def mezcla(lista1, lista2):
    i, j = 0, 0
    resultado = []
    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    resultado += lista1[i:]
    resultado += lista2[j:]
    return resultado

def generar_lista(N):
    lista = []
    for i in range(N):
        lista.append(np.random.randint(1,1001))
    return lista

def generar_listas(Nmax):
    lista = []
    for i in range(1,Nmax+1):
        lista.append(generar_lista(i))
    return lista

def experimento_timeit(Nmax):
    """
    Realiza un experimento usando timeit para evaluar el método
    de selección para ordenamiento de listas
    con las listas pasadas como entrada
    y devuelve los tiempos de ejecución para cada lista
    en un vector.
    El parámetro 'listas' debe ser una lista de listas.
    El parámetro 'num' indica el número de veces que repite el ordenamiento 
    para cada lista.
    """
    tiempos_sel = []
    tiempos_ins = []
    tiempos_bur = []
    tiempos_mez = []
    listas = generar_listas(Nmax)
    global lista
    for lista in listas:
        tiempo_sel = tt.timeit('ord_seleccion(lista.copy())', number = 100,
                              globals = globals())
        tiempo_ins = tt.timeit('ord_insercion(lista.copy())', number = 100, 
                              globals = globals())
        tiempo_bur = tt.timeit('ord_burbujeo(lista.copy())', number = 100, 
                              globals = globals())
        tiempo_mez = tt.timeit('ord_mezcla(lista.copy())', number = 100, 
                              globals = globals())
        tiempos_sel.append(tiempo_sel)
        tiempos_ins.append(tiempo_ins)
        tiempos_bur.append(tiempo_bur)
        tiempos_mez.append(tiempo_mez)
    tiempos_sel = np.array(tiempos_sel)
    tiempos_ins = np.array(tiempos_ins)
    tiempos_bur = np.array(tiempos_bur)
    tiempos_mez = np.array(tiempos_mez)
    return tiempos_sel, tiempos_ins, tiempos_bur, tiempos_mez

def graficar(experimento,Nmax):
    fig, ax = plt.subplots()
    x = np.arange(1,Nmax+1)
    ax.plot(x, experimento[0], label='Ord.Selección')  
    ax.plot(x, experimento[1], label='Ord.Inserción')
    ax.plot(x, experimento[2], label='Ord.Burbujeo')
    ax.plot(x, experimento[3], label='Ord.Mezcla')
    ax.set_xlabel('Largo lista')  
    ax.set_ylabel('Tiempo de ordenamiento (x 100)') 
    ax.set_title("Comparación entre métodos de ordenamiento") 
    ax.legend()
    plt.show()


if __name__ == '__main__':
    graficar(experimento_timeit(256),256)