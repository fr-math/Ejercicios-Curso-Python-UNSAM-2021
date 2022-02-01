#!/usr/bin/env python3
# random_walk.py
# Ejercicio 7.12

import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    '''Toma un numero natural n y devuelve los pasos de una caminata aleatoria
     en un np.array de largo n'''
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

def generar_trayectorias(n,largo):
    '''Toma dos numeros naturales n y largo, y devuelve n caminatas 
    aleatorias en un np.array de longitud 'largo'. '''
    trayectorias = []
    for i in range(n):
        trayectoria = randomwalk(largo)
        trayectorias.append(trayectoria)
    return trayectorias

def mas_lejano(trayectorias):
    '''Toma una lista de trayectorias y devuelve la que mas se aleja del 
    origen de coordenadas.'''
    primera_vez = True
    for trayectoria in trayectorias:
        if primera_vez:
            max_distancia = max(abs(trayectoria))
            max_trayectoria = trayectoria
            primera_vez = False
        if (max(abs(trayectoria)) > max_distancia) and (not primera_vez):
            max_distancia = max(abs(trayectoria))
            max_trayectoria = trayectoria
    return max_trayectoria

def mas_cercano(trayectorias):
    '''Toma una lista de trayectorias y devuelve la que menos se aleja del 
    origen de coordenadas.'''
    primera_vez = True
    for trayectoria in trayectorias:
        if primera_vez:
            min_distancia = max(abs(trayectoria))
            min_trayectoria = trayectoria
            primera_vez = False
        if (max(abs(trayectoria)) < min_distancia) and (not primera_vez):
            min_distancia = max(abs(trayectoria))
            min_trayectoria = trayectoria
    return min_trayectoria



def plotear_grafico(cantidad=12,N = 100000):
    '''Plotea un gráfico de trayectorias aleatorias generadas por la funcion
    generar_trayectorias. La cantidad de trayectorias generadas está definida
    por omision a 12 y se puede elegir con el argumento opcional 'cantidad='.
    La longitud de las trayectorias es, por omision, 100000 y se puede elegir 
    con el argumento opcional 'N='.'''
    
    trayectorias = generar_trayectorias(cantidad,N)

    ax = plt.subplot(2, 1, 1)
    plt.xticks([]), plt.yticks([-500,0,500])
    for i,trayectoria in enumerate(trayectorias):
        ax.plot(trayectoria,label=f'{i}')
        ax.set_title(f'{cantidad} Caminatas al azar')
        plt.ylim(-800, 800)
        
    ax = plt.subplot(2, 2, 3)
    plt.plot(mas_lejano(trayectorias))
    plt.xticks([]), plt.yticks([-500, 0, 500])
    plt.ylim(-800, 800)
    ax.set_title('La caminata que mas se aleja')

    ax = plt.subplot(2, 2, 4) 
    plt.plot(mas_cercano(trayectorias))
    plt.xticks([]), plt.yticks([-500, 0, 500])
    plt.ylim(-800, 800)
    ax.set_title('La caminata que menos se aleja')
    
    plt.show()


if __name__ == '__main__':
    plotear_grafico()