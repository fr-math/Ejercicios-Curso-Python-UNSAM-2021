#!/usr/bin/env python3
# alquiler.py
# Ejercicio 11.14

import numpy as np
import matplotlib.pyplot as plt

def ajuste_lineal_simple(x,y):
    '''Toma dos arreglos del mismo tamaño y devuelve los coeficientes de la 
    pendiente y ordenada al origen que mejor ajustan una regresión lineal en 
    una tupla.'''
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b

def recta_ajuste(ajuste_lineal,minx = 70.0,maxx = 180.0):
    '''Toma una tupla de pendiente y ordenada al origen y genera los puntos de
     una recta de regresión en el plano en una tupla de arreglos.'''
    grilla_x = np.linspace(start = minx, stop = maxx, num = 1000)
    grilla_y = grilla_x*ajuste_lineal[0] + ajuste_lineal[1]
    return grilla_x, grilla_y

def grafico_scatter_vs_lineal(x,y,recta_aj):
    '''Toma dos arreglos del mismo tamaño y una tupla de arreglos (recta de 
    regresión) y grafica el scatterplot y la recta de regresión. '''
    plt.scatter(x = x, y = y)
    plt.title('y ajuste lineal')
    plt.plot(recta_aj[0], recta_aj[1], c = 'green')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()    


if __name__ == '__main__':
    #DATOS
    superficie = np.array([150.0, 120.0, 170.0, 80.0])
    alquiler = np.array([35.0, 29.6, 37.4, 21.0])
    #AJUSTE LINEAL
    a, b = ajuste_lineal_simple(superficie, alquiler)
    #GRAFICO
    grafico_scatter_vs_lineal(superficie, alquiler, 
                             recta_ajuste(ajuste_lineal_simple(superficie, 
                                                               alquiler)))
    #ERRORES
    errores = alquiler - (a*superficie + b)
    print(errores)
    print("ECM:", (errores**2).mean())