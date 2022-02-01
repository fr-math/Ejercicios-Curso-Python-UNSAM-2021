# figuritas.py 
# Ejercicio 5.16

import numpy as np
import random


def simular_paquete(figus_total,figus_paquete):
    paquete = [random.randint(0,figus_total-1) for _ in range(figus_paquete)]
    return paquete


if __name__ == '__main__':
    paquete_figus = simular_paquete(670,5)
    print(paquete_figus)
