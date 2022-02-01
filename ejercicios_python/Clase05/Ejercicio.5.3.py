# Ejercicio 5.3

import random
from collections import Counter

def lista_cumpleaños(cant_personas):
    lista_cumples = [ random.randint(1,365) for _ in range(cant_personas)]
    return lista_cumples

def proba_mismo_cumple(num_ciclos, num_personas):
    cant_repetidos = 0
    for _ in range(num_ciclos):
        contador = Counter(lista_cumpleaños(num_personas))
        (cumple, veces) = contador.most_common(1)[0]
        if veces > 1:
            cant_repetidos += 1
    proba = cant_repetidos / num_ciclos
    return proba

if __name__ == '__main__':
    n_ciclos = 100000
    print(f'La probabilidad de que, entre 30 personas, dos cumplan el mismo día, es de (aproximadamente):\t{proba_mismo_cumple(n_ciclos,30):.5f}')    
    num_personas = 2
    while proba_mismo_cumple(n_ciclos,num_personas) <= 0.5:
        num_personas +=1
    print(f'La cantidad mínima de personas para que sea más probable que dos cumplan el mismo día a que cumplan todos dias distintos, es de (aproximadamente):\t{num_personas}')