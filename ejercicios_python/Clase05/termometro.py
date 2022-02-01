# termometro.py 
# Ejercicio 5.8

import numpy as np
import random

def medir_temp(n):
    mu = 0              # media
    sigma = 0.2         # sd
    lista_temp = np.array([(37.5 + random.normalvariate(mu,sigma)) for _ in range(n)])
    np.save('../Data/temperaturas',lista_temp)
    return lista_temp

def resumen_temp(n):
    lista_temp = medir_temp(n)                                                              
    if n%2:                                                                                 #impar
        mediana = sorted(lista_temp)[int((n-1)/2)]                                          #tomo el del medio
    else:                                                                                   #par
        mediana = (sorted(lista_temp)[int(n/2)] + sorted(lista_temp)[int(n/2) - 1] ) / 2    #tomo el promedio de los dos del medio
    resumen = (max(lista_temp), min(lista_temp), sum(lista_temp)/n, mediana)                #(*) Nota al final
    return resumen

if __name__ == '__main__':
    res = resumen_temp(999)
    print (f'{res}')

#(*)Nota: En el módulo statistics hay una funcion para la mediana "median()". 
# Además, la funcion se puede hacer en una sola línea de la siguiente manera: 
# resumen = (max(medir_temp(n)), min(medir_temp(n)), mean(medir_temp(n)), median(medir_temp(n))) 
# que queda bonita, pero si no estás acosutmbrado es un dolor leerlo. Además 
# hay que importar statistics.