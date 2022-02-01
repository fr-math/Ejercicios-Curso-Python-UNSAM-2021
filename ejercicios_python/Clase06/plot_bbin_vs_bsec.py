# plot_bbin_vs_bsec.py 
# Ejercicio 6.20

import random
import matplotlib.pyplot as plt
import numpy as np


def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    contador = 0
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
        contador += 1
    return pos,contador

def busqueda_secuencial_(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps

def generar_lista(n, m):
    l = random.sample(range(m), k = n)
    l.sort()
    return l

def generar_elemento(m):
    return random.randint(0, m-1)

def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista,x)[1]
    comps_prom = comps_tot / k
    return comps_prom

def experimento_binario_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria(lista,x)[1]
    comps_prom = comps_tot / k
    return comps_prom

def graficar_bbin_vs_bseq(m, k, n=100, rango_x=(0,30), rango_y=(0,30)):
    '''
    Genera un gráfico comparando el método de busqueda secuencial respecto al
    de búsqueda binaria, para listas de numeros enteros menores o iguales a m, 
    de largo n. El numero de experimentos individuales realizados es k. El rango
    de graficación se muestra dentro de rango_x y rango_y.
    '''
    lista = generar_lista(n, m)
    largos = np.arange(256) + 1 
    comps_promedio_bin = np.zeros(256) 
    comps_promedio_sec = np.zeros(256) 
    for i, n in enumerate(largos):
        lista = generar_lista(n, m) 
        comps_promedio_sec[i] = experimento_secuencial_promedio(lista, m, k)
        comps_promedio_bin[i] = experimento_binario_promedio(lista, m, k)

    plt.plot(largos,comps_promedio_sec,label = 'Búsqueda Secuencial')
    plt.plot(largos,comps_promedio_bin,label = 'Búsqueda Binaria')
    plt.xlim(rango_x)
    plt.ylim(rango_y)
    plt.xlabel("Largo de la lista")
    plt.ylabel("Cantidad de comparaciones")
    plt.title("Complejidad de la Búsqueda Secuencial vs Binaria")
    plt.legend()
    plt.show()
    return


if __name__ == '__main__':
    graficar_bbin_vs_bseq(10000, 1000)