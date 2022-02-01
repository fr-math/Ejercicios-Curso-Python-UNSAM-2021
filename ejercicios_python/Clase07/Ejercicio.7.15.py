#!/usr/bin/env python3
# Ejercicio 7.15

import numpy as np
import matplotlib.pyplot as plt

n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)

plt.figure()
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.xticks([])
plt.yticks([])

for x, y in zip(X, Y):
    plt.scatter(x, y, facecolor = plt.cm.viridis(np.arctan2(y, x)), alpha = 0.5)
    
plt.show()