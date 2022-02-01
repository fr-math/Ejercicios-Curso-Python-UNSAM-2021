#!/usr/bin/env python3
# Ejercicio 7.12

import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

N = 100000
'''
plt.plot(randomwalk(N))
plt.xlabel("Tiempo (s)")
plt.ylabel("Distancia al origen (m)")
plt.show()
'''

for _ in range(12):
    plt.plot(randomwalk(N),color=hex(np.random.randint(16777215))
plt.show()