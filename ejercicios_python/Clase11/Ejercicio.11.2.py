#!/usr/bin/env python3
# Ejercicio 11.3

#%% 11.2
def triangular(n):
    ''' Toma un numero natural y suma todos los numeros naturales anteriores, 
    hasta el valor del argumento inclusive.'''
    acum = 0
    if n > 0:
        acum = n + triangular(n-1)
    return acum

#%% 11.3
def cant_digitos(n):
    ''' Toma un numero natural y devuelve la cantidad de dígitos que tiene,
    en base decimal.'''
    cadena = str(n)
    digitos = 0
    if len(cadena) != 0:
        digitos += 1 + cant_digitos(cadena[1:])
    return digitos

#%% 11.4 
def es_potencia(n, b):
    ''' Toma dos numeros naturales y devuelve si el primero es potencia del
    segundo.'''    
    def calculo_pot(n, b):
        resto = n
        if n >= b :
            resto = calculo_pot(n//b,b)
        return resto
    if n < 0:
        n = -n
    if b < 0:
        b = -b
    if calculo_pot(n,b) == 1:
        potencia = True
    else:
        potencia = False
    return potencia

#%% 11.5 
def posiciones(a,b):
    '''Toma dos cadenas y devuelve una lista con las posiciones de la primer 
    cadena donde se repite la segunda.'''
    def constr_lista(cad1,cad2,lista):
        if len(cad1) >= len(cad2):
            if cad2 in cad1:
                if cad2[:] == cad1[-len(cad2):]:
                    lista.append(len(cad1)-len(cad2))
                    constr_lista(cad1[:-len(cad2)],cad2,lista)
                else:
                    constr_lista(cad1[:-1],cad2,lista)
        return lista 
    lista = []
    idx = len(a) - len(b)
    if idx >= 0:
        constr_lista(a,b,lista)
    return lista[::-1]

#%% 11.6
def par(n):
    '''Toma un numero natural y devuelve si es par.'''
    if n == 1:
        flag = False
    else:
        if impar(n-1):
            flag = True
        else:
            flag = False
    return flag

def impar(n):
    '''Toma un numero natural y devuelve si es impar.'''
    if n == 1:
        flag = True
    else:
        if par(n-1):
            flag = True
        else:
            flag = False
    return flag

#%% 11.7
def maximo(lista):
    try:
        lista = lista.copy()
        max = lista[0]
        if lista[1] > lista[0]:
            max = maximo(lista[1:])
    except IndexError as e:
        print('No me pude ejecutar porque: ', e)
    return max

#%% 11.8 VER
'''
def replicar(lista, n):
    def replicacion(lista,n):
        for i in range(n-1):
            lista.insert(0,lista[0])
        return lista
    m = len(lista) * 3
    if len(lista) < m:
        replicacion(lista[3:],n)
    return lista
'''
#%% 11.10 VER   
def combinaciones(lista, k):
    return
            
#%%

if __name__ == '__main__':
    #print(triangular(10))
    #print(cant_digitos(999))
    #print(es_potencia(8, 2))
    #print(es_potencia(64, 4))
    #print(es_potencia(70, 10))
    #print(es_potencia(1, 3))
    #print(posiciones('Un tete a tete con Tete', 'te'))
    #print(par(10), impar(10))
    #print(par(11), impar(11))
    print(maximo([0,2,3,4,5,-1,-7,7]))
    #print(replicar([1,2,3,4],3))