# figuritas.py 
# Ejercicio 5.i for i in range(9,25)

import numpy as np
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



if __name__ == '__main__':
    n_repeticiones2 = 100
    figus_total2 = 670
    promedio_figus2 = experimento_figus(n_repeticiones2,figus_total2)
    print(f'En promedio, hay que comprar {promedio_figus2:0.0f} figuritas ({promedio_figus2:0.2f}), para llenar el álbum de {figus_total2} espacios.')