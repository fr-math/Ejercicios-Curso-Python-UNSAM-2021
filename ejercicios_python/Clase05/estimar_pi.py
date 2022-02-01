# estimar_pi.py 
# Ejercicio 5.5

import random

def generar_punto():
    x = random.random()
    y = random.random()
    return x,y

if __name__ == '__main__':
    N = 100000
    M = 0
    for _ in range(N):
        (x,y) = generar_punto()
        if (x*x + y*y) <= 1:
            M +=1
    pi = 4 * M / N 
    print(f'Pi vale aproximadamente {pi:0.4f}')