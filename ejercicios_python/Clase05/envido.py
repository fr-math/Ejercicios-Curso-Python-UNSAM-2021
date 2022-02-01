# envido.py
# Ejercicio 5.4

import random


def valor_envido(mano):
    combinaciones = [0]
    if mano[0][1] == mano[1][1]: 
        if (int(mano[0][0]) <= 7) and (int(mano [1][0]) <= 7):
            combinaciones.append(int(mano[0][0]) + int(mano [1][0]) + 20)
        if (int(mano[0][0]) <= 7) and (int(mano [1][0]) > 7):
            combinaciones.append(int(mano[0][0]) + 20)
        if (int(mano[0][0]) > 7) and (int(mano [1][0]) <= 7):
            combinaciones.append(int(mano [1][0]) + 20)
        if (int(mano[0][0]) > 7) and (int(mano [1][0]) > 7):
            combinaciones.append(20)
    if mano[0][1] == mano[2][1]: 
        if (int(mano[0][0]) <= 7) and (int(mano [2][0]) <= 7):
            combinaciones.append(int(mano[0][0]) + int(mano [2][0]) + 20)
        if (int(mano[0][0]) <= 7) and (int(mano [2][0]) > 7):
            combinaciones.append(int(mano[0][0]) + 20)
        if (int(mano[0][0]) > 7) and (int(mano [2][0]) <= 7):
            combinaciones.append(int(mano [2][0]) + 20)
        if (int(mano[0][0]) > 7) and (int(mano [2][0]) > 7):
            combinaciones.append(20)
    if mano[1][1] == mano[2][1]: 
        if (int(mano[1][0]) <= 7) and (int(mano [2][0]) <= 7):
            combinaciones.append(int(mano[1][0]) + int(mano [2][0]) + 20)
        if (int(mano[1][0]) <= 7) and (int(mano [2][0]) > 7):
            combinaciones.append(int(mano[1][0]) + 20)
        if (int(mano[1][0]) > 7) and (int(mano [2][0]) <= 7):
            combinaciones.append(int(mano [2][0]) + 20)
        if (int(mano[1][0]) > 7) and (int(mano [2][0]) > 7):
            combinaciones.append(20)    
    sum_envido = int(max(combinaciones)) 
    return sum_envido

if __name__ == '__main__' :
    N = 100000
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    palos = ['oro', 'copa', 'espada', 'basto']
    naipes = [(valor,palo) for valor in valores for palo in palos]
    cont_31 = 0
    cont_32 = 0
    cont_33 = 0
    for _ in range(N):
        mano_actual = random.sample(naipes,k=3)
        envido = valor_envido(mano_actual)
        if envido == 31:
            cont_31 += 1
        if envido == 32:
            cont_32 += 1
        if envido == 33:
            cont_33 += 1
    prob_31 = cont_31/N
    prob_32 = cont_32/N
    prob_33 = cont_33/N
    print(f'Las probabilidades de sacar 31, 32 o 33 en el envido son:\n 31 :\t{prob_31} \n 32 :\t{prob_32} \n 33 :\t{prob_33}')
    print(f'Vemos que las probabilidades de sacar 31 son aproximadamente el doble de sacar 32 o 33,\n dado que 31 se puede formar con los pares (4,7) y (5,6), mientras que 32 y 33 solo con\n los pares (5,7) y (6,7) respectivamente.')