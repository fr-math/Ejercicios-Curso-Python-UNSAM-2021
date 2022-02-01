# generala.py
# Ejercicio 5.2 

import random
from collections import Counter

def tirar():
    tirada = [random.randint(1,6) for _ in range(5)]
    return tirada

def es_generala(tirada):
    generala = False
    if min(tirada) == max(tirada):
        generala = True
    return generala

def prob_generala(N):
    G = 0
    for _ in range(N):
        n_dados = 5
        tirada_1 = tirar()
        generala = False
        if es_generala(tirada_1):                                           #Tiro los 5 dados y si es generala, la anoto
            generala = True
        else:
            contador = Counter(tirada_1)
            [numero_elegido,veces] = contador.most_common(1)[0]             #Acá veo cual es el número que mas se repite y 
            juego = [numero_elegido for _ in range(veces)]                  #lo guardo en una lista. Y armo otra lista con  
            n_dados -= veces                                                #la jugada, del num repetido y las veces.
            tirada_2 = [random.randint(1,6) for _ in range(n_dados)]        #Acá tiro los dados restantes.
            tirada_2 += juego                                               #Y los agrego a la lista de la segunda tirada.
            if es_generala(tirada_2):                                       #De acá en mas repito.
                generala = True
            else:
                contador = Counter(tirada_2)
                (numero_elegido,veces) = contador.most_common(1)[0]
                juego = [numero_elegido for _ in range(veces)]
                n_dados -= veces
                tirada_3 = [random.randint(1,6) for _ in range(n_dados)]
                tirada_3 += juego 
                if es_generala(tirada_3):
                    generala = True        
        if generala:
            G += int(generala)                                              #Voy contando la cantidad de generalas.
    probabilidad = G/N                                                      #Y calculo la probabilidad.
    return probabilidad


if __name__ == '__main__':
    probabilidad = prob_generala(1000)
    print(f'Esta es la probabilidad de hacer una generala: {probabilidad:0.4f}')

#NOTA: Se puede hacer mas corto, pero traté de hacer que el código sea lo mas claro psoible. 
# Agregué un método de collections, que para la clase 2 o 3 no usé, pero ahora si, porque le 
# daba mas facilidad de lectura al código.