# termometro.py 
# Ejercicio 5.6

import random


def medir_temp(n):
    mu = 0              # media
    sigma = 0.2         # sd
    lista_temp = [(37.5 + random.normalvariate(mu,sigma)) for _ in range(n)]
    return lista_temp

def resumen_temp(n):
    lista_temp = medir_temp(n)
    if n%2:                                           #impar
        mediana = sorted(lista_temp)[int((n-1)/2)]
    else:
        mediana = (sorted(lista_temp)[int(n/2)] + sorted(lista_temp)[int(n/2) - 1] ) / 2
    resumen = (max(lista_temp), min(lista_temp), sum(lista_temp)/n, mediana)
    return resumen

if __name__ == '__main__':
    res_1 = resumen_temp(1000)
    res_2 = resumen_temp(1001)
    print (f'{res_1}\n{res_2}')