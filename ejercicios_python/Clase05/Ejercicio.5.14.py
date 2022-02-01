# figuritas.py 
# Ejercicio 5.14

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


if __name__ == '__main__':
    n_repeticiones = 1000
    figus_total = 6
    lista = np.array([cuantas_figus(figus_total) for _ in range(1000)])
    promedio_figus = np.mean(lista)
    print(f'En promedio, hay que comprar {promedio_figus:0.0f} figuritas ({promedio_figus:0.2f}), para llenar el álbum de {figus_total} espacios.')