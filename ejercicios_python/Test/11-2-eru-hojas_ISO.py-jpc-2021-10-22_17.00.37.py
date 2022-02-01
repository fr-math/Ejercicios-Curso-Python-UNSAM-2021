#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 14:59:50 2021

@author: Juampi
"""

'''
La norma ISO 216 especifica tamaños de papel. 
Es el estándar que define el popular tamaño de papel A4 (210 mm de ancho y 297 mm de largo). 
Las hojas A0 miden 841 mm de ancho y 1189 mm de largo. A partir de la A0 las siguientes medidas, 
digamos la A(N+1), se definen doblando al medio la hoja A(N). 
Siempre se miden en milímetros con números enteros: entonces la hoja A1 mide 594 mm de ancho (y no 594.5) por 841 mm de largo.

Escribí una función recursiva medidas_hoja_A(N) que para una entrada N mayor que cero, 
devuelva el ancho y el largo de la hoja A(N) calculada recursivamente a partir de las medidas de la hoja A(N−1), 
usando la hoja A0 como caso base. La función debe devolver el ancho y el largo -en ese orden- en una tupla.

A0 = (841,1189)
A1 = (1189/2, 841)
A2 = (841/2, 1189/2)
A3 = (1189/(2*2), 841/2)
'''
#%%
def medidas_hoja_A(N):
    '''
    Función que permite conocer las dimensiones de una hoja A(N) según la norma ISO 216.
    
    Parameters
    ----------
    N : entero mayor o igual a 0.
        
    Returns
    -------
    Tupla con dimensiones de la hoja A(N) en formato (altura, ancho).

    '''
    if N == 0:
        a = 841
        l = 1189 
        return (a, l)
    else:
        medida_ancho = medidas_hoja_A(N-1)[1]//2
        medida_largo = medidas_hoja_A(N-1)[0]
        return (medida_ancho, medida_largo)

'''
#Prueba de que funciona#

for num in range(0,10):
    print(medidas_hoja_A(num))
'''