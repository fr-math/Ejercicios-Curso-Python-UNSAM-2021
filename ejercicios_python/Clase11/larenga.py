#!/usr/bin/env python3
# larenga.py
# Ejercicio 11.9

def pascal(n, k):
    '''Calcula el término (n,k) del triángulo de Pascal, donde n es la fila, y
    k la columna, contando desde 0.'''
    if n == 0:
        coef = 0
    elif k == 0 or k == n:
        coef = 1
    else:
        coef = pascal(n-1,k-1) + pascal(n-1,k)
    return coef

if __name__ == '__main__':
    intro = f'Probando, probando... Un, dos, tres,... \n'
    chorus = f'El corazón tiene razones que la razón ignora...\n'
    end = f'Si el final es en donde partí!'
    print(intro + chorus)
    for n in range(6):
        print(' '*5*(5-n),end='')
        for k in range(n+1):
            print(f'{pascal(n,k):^5}',end=' '*5)
        print('\n')
    print(end)
    