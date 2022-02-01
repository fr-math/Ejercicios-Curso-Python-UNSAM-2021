# figuritas.py 
# Ejercicio 5.17

import numpy as np
import random


def comprar_paquete(figus_total, figus_paquete):
    paquete = [random.randint(0,figus_total-1) for _ in range(figus_paquete)]
    return paquete