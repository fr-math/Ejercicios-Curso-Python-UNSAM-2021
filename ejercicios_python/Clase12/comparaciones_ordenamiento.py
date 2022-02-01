#!/usr/bin/env python3
# comparaciones_ordenamiento.py
# Ejercicio 12.2


import numpy as np
import matplotlib.pyplot as plt


def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada. Devuelve la cantidad de comparaciones
       realizadas."""
    n = len(lista) - 1
    cont = 0
    while n > 0:
        p = buscar_max(lista, 0, n)
        cont += n
        lista[p], lista[n] = lista[n], lista[p]
        n = n - 1
    return cont

def buscar_max(lista, a, b):
    """Pre: La lista no debe ser vacía.
        Post: Devuelve la posición del máximo elemento en un segmento de
        lista de elementos comparables.
        a y b son las posiciones inicial y final del segmento"""
    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max

def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada. Devuelve la cantidad de comparaciones 
       realizadas."""
    cont = 0
    for i in range(len(lista) - 1):
        cont += 1
        if lista[i + 1] < lista[i]:
            cont += reubicar(lista, i + 1)
    return cont

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""
    v = lista[p]
    j = p
    cont = 0
    while j > 0 and v < lista[j - 1]:
        cont += 1
        lista[j] = lista[j - 1]
        j -= 1
    lista[j] = v
    return cont

def ord_burbujeo(lista):
    """Ordena una lista de elementos según el método de burbujeo.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada. Devuelve la cantidad de comparaciones 
       realizadas."""
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

def ord_mezcla(lista,cont=0):
    """Ordena una lista de elementos según el método de mezcla (merge sort).
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada. Devuelve una tupla con la lista ordenada 
       en la primera posicion y la cantidad de comparaciones realizadas en la 
       segunda."""
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = ord_mezcla(lista[:medio],cont)
        der = ord_mezcla(lista[medio:],cont)
        lista_mer, cont_mer = mezcla(izq, der)
        lista_nueva = lista_mer
        cont = cont_mer
    return lista_nueva,cont

def mezcla(lista1, lista2):
    """Arma una lista a partir de los elementos de dos listas. La lista 
       resultante está ordenada.
       Pre: los elementos de ambas listas deben ser comparables.
       Post: la lista está ordenada. Devuelve una tupla con la lista ordenada 
       en la primera posicion y la cantidad de comparaciones realizadas en la 
       segunda."""
    i, j = 0, 0
    resultado = []
    n_comp = lista1[1] + lista2[1]
    while(i < len(lista1[0]) and j < len(lista2[0])):
        n_comp += 1
        if (lista1[0][i] < lista2[0][j]):
            resultado.append(lista1[0][i])
            i += 1
        else:
            resultado.append(lista2[0][j])
            j += 1
    resultado += lista1[0][i:]
    resultado += lista2[0][j:]
    return resultado,n_comp


def generar_lista(N):
    ''' Genera una lista de tamaño especificado con elementos aleatorios entre 
        1 y 1000.
        Pre: Se debe ingresar un entero positivo como argumento (longitud de 
        la lista).
        Post: Devuelve una lista aleatoria de longitud especificada.'''
    lista = []
    for i in range(N):
        lista.append(np.random.randint(1,1001))
    return lista

def experimento(N):
    ''' Ordena una lista aleatoria de tamaño especificado por los metodos de 
        ordenamiento de seleccion, insercion, burbujeo y mezcla.
        Pre: Se debe ingresar un entero positivo.
        Post: Devuelve una lista con la cantidad de comparaciones realizadas 
        por los distintos metodos utilizados. [sel,ins,bur,mez]'''
    lista = generar_lista(N)
    lista_1 = lista.copy()
    lista_2 = lista.copy()
    lista_3 = lista.copy()
    lista_4 = lista.copy()
    result = [ord_seleccion(lista_1), ord_insercion(lista_2),
             ord_burbujeo(lista_3), ord_mezcla(lista_4,0)[1]]
    return result

def experimento_vectores(Nmax):
    ''' Cuenta la cantidad de comparaciones de cuatro métodos de ordenamiento 
        distintos entre 1 y Nmax, y devuelve una tupla de vectores con la 
        cantidad de comparaciones de cada método. 
        Pre: Nmax debe ser un entero positivo.
        Post: los vectores son del tipo numpy.array().'''
    lis_sel = []
    lis_ins = []
    lis_bur = []
    lis_mez = []
    for N in range(1,Nmax+1):
        lis_sel.append(experimento(N)[0])
        lis_ins.append(experimento(N)[1])
        lis_bur.append(experimento(N)[2]) 
        lis_mez.append(experimento(N)[3])       
    vec_sel = np.array(lis_sel)
    vec_ins = np.array(lis_ins)
    vec_bur = np.array(lis_bur)
    vec_mez = np.array(lis_mez)
    return vec_sel, vec_ins, vec_bur, vec_mez

def graficar(experimento,Nmax):
    ''' Grafica un experimento.
        Pre: Se debe ingresar un experimento y el largo de los vectores que 
        devuelve el mismo.
        Post: Grafico.'''
    fig, ax = plt.subplots()
    x = np.arange(1,Nmax+1)
    ax.plot(x, experimento[0], label='Ord.Selección')  
    ax.plot(x, experimento[1], label='Ord.Inserción')
    ax.plot(x, experimento[2], '.', label='Ord.Burbujeo')
    ax.plot(x, experimento[3], label='Ord.Mezcla')
    ax.set_xlabel('Largo lista')  
    ax.set_ylabel('Cantidad de comparaciones') 
    ax.set_title("Comparación entre métodos de ordenamiento") 
    ax.legend()
    plt.show()


if __name__ == '__main__':
    #print(ord_mezcla([5,4,3,2,1]))
    #print(ord_mezcla([10,9,8,7,6,5,4,3,2,1]))
    graficar(experimento_vectores(512),512)    
    