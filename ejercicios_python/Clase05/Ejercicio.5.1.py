#Ejercicio 5.1 (generala)

import random

def tirar():
    tirada = [random.randint(1,6) for _ in range(5)]
    return tirada

def es_generala(tirada):
    generala = False
    if min(tirada) == max(tirada):
        generala = True
    return generala

if __name__ == '__main__':
    N = 100000
    M = 1000000
    G = sum([es_generala(tirar()) for i in range(N)])
    H = sum([es_generala(tirar()) for i in range(M)])
    prob = G/N
    prob2 = H/M
    print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
    print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
    print(f'Tiré {M} veces, de las cuales {H} saqué generala servida.')
    print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob2:.6f}.')
    '''
    - Los resultados varían mas con N=100000 que con N=1000000 porque hay una menor apreciación en la escala 
    en la que se mide.
    - En promedio, sale generala servida 1 vez cada 1297 veces.
    - P(A) = (1/6)^4 (el primer dado fija el número y despues es la probabilidad de que salga el mismo 4 veces
    seguidas)
    '''