#!/usr/bin/env python3
# hojas_ISO.py
# Ejercicio 11.13

def medidas_hoja_A(N):
    '''Toma un entero N mayor o igual a cero y devuelve una tupla con los 
    valores del ancho y el largo de una hoja AN.'''
    if N == 0:
        ancho = 841
        largo = 1189
    else:
        ancho = medidas_hoja_A(N-1)[1] // 2
        largo = medidas_hoja_A(N-1)[0] 
    return ancho, largo

if __name__ == '__main__':
    for _ in range(8):
        print(f'Hoja A{_} : ancho x largo = ' + 
             f'{medidas_hoja_A(_)[0]}mm x {medidas_hoja_A(_)[1]}mm')
