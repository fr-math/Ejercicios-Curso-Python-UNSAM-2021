#!/usr/bin/env python3
# documentacion.py
# Ejercicio 7.10


def valor_absoluto(n):
    '''Toma un numero y devuelve su valor absoluto.'''
    # Comentario, me hace algo de ruido que haya dos return, se podría modificar de manera que no haya 
    # dos agregando una variable nueva y guardando el valor absoluto en ella.
    if n >= 0:
        return n
    else:
        return -n 
    #No hay invariantes de ciclo (no hay ciclo)


def suma_pares(l):
    '''Toma un iterable y devuelve la suma de todos los elementos pares del iterable.'''
    res = 0         
    for e in l:         
        if e % 2 ==0:
            res += e
        else:                   #Este else se podría evitar, no hace nada.
            res += 0
                                #Se le podrían dar nombres un poco mas explicativos a las variables, dado que el código es cortito.
    return res
    #Invariante de ciclo: res, es la suma de todos los pares del iterable hasta la iteración e.

def veces(a, b):
    '''Toma un float y un entero no negativo y devuelve el producto entre ambos.'''
    res = 0
    nb = b
    while nb != 0:              # Se puede implementar un for que hace que el producto sea mas entendible, o un producto directamente.
        #print(nb * a + res)
        res += a
        nb -= 1
    return res
    #Invariante de ciclo: res, es la suma de "b-nb+1" veces "a", para cada iteración nb.

def collatz(n):
    '''Toma un numero natural y devuelve el tiempo de su órbita, en la conjetura de collatz.'''
    res = 1

    while n!=1:             
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1
                        
    return res
    #Invariante de ciclo: res, es la cantidad de órbitas hasta el momento halladas.