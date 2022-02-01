# figuritas.py 
# Ejercicio 5.18

import numpy as np
import random

def crear_album(figus_total):
    lista_figus = np.zeros(figus_total)
    return lista_figus

def album_incompleto(A):
    incompleto = True
    if int(A.min()) != 0:
        incompleto = False
    return incompleto

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