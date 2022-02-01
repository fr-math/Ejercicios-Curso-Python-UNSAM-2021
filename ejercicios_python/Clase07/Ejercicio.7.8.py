#!/usr/bin/env python3
# Ejercicio.7.8.py
# Ejercicio 7.8


def sumar_enteros_1(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    suma = 0
    if desde <= hasta: 
        for numero in range(desde,hasta):
            suma += numero
    return suma 

def sumar_enteros_2(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    suma = 0
    if desde <= hasta:
        suma = (hasta*(hasta+1)/2 - desde*(desde+1)/2)
    return suma