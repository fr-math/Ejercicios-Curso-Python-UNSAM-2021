# figuritas.py 
# Ejercicio 5.21

import numpy as np
import matplotlib.pyplot as plt
import random

### FIGURITAS

def crear_album(figus_total):
    lista_figus = np.zeros(figus_total)
    return lista_figus

def album_incompleto(A):
    incompleto = True
    if int(A.min()) != 0:
        incompleto = False
    return incompleto

def comprar_figu(figus_total):
    num_figurita = random.randint(0,figus_total-1)
    return num_figurita

def cuantas_figus(figus_total):
    contador_figus = 0
    album = crear_album(figus_total)
    while album_incompleto(album):
        figurita = comprar_figu(figus_total)
        album[figurita] += 1
        contador_figus += 1
    return contador_figus

def experimento_figus(n_repeticiones, figus_total):
    lista = np.array([cuantas_figus(figus_total) for _ in range(n_repeticiones)])
    promedio_figus = np.mean(lista)
    return promedio_figus

### PAQUETES

def comprar_paquete(figus_total, figus_paquete):
    paquete = [random.randint(0,figus_total-1) for _ in range(figus_paquete)]
    return paquete

def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)
    num_paquetes = 0
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        for figurita in paquete:
            album[figurita] += 1
        num_paquetes +=1
    return num_paquetes


if __name__ == '__main__':
    n_repeticiones3 = 1000
    figus_total3 = 670
    figus_paquete3 = 5
    lista3 = np.array([cuantos_paquetes(figus_total3, figus_paquete3) for _ in range(n_repeticiones3)])
    plt.hist(lista3,bins=50)
    plt.show()