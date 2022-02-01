#!/usr/bin/env python3
# fileparse.py
# Ejercicio 7.6-7


import csv


def parse_csv(iterable, select = None, types=None, has_headers=True, silence_errors=False):
    '''
    Parsea un iterable de texto con el formato de salida de archivo CSV leido por el csv.reader en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    Se puede seleccionar el tipo de dato de cada columna, sabiendo su índice y asignandole una lista con las funciones conversoras a el parámetro types.
    En caso de no haber encabezados, se puede omitir la lectura de los mismos asignandole False al parámetro has_headers (has_headers=False). Esto devuelve una lista de tuplas.
    '''
    filas = csv.reader(iterable)
    if has_headers:
        encabezados = next(filas)
        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []
        registros = []
        for i,fila in enumerate(filas):
            if not fila:    
                continue
            if indices:
                fila = [fila[index] for index in indices]
            if types:
                try:
                    fila = [func(val) for func, val in zip(types, fila) ]
                    registro = dict(zip(encabezados, fila))
                    registros.append(registro)
                except ValueError as e:
                    if not silence_errors:
                        print(f'Fila {i-1}: No pude convertir {fila}\nFila {i-1}: Motivo: {e}')
    else:
        if select:
            raise RuntimeError("Para seleccionar, necesito encabezados.")
        registros = []
        for i,fila in enumerate(filas):
            if not fila:    
                continue
            if types:
                try:
                    fila = [func(val) for func, val in zip(types, fila) ]
                    registros.append(tuple(fila))
                except ValueError as e:
                    if not silence_errors:
                        print(f'Fila {i-1}: No pude convertir {fila}\nFila {i-1}: Motivo: {e}')
    return registros
    

if __name__ == '__main__':
    parse_csv('../Data/precios.csv', select = ['nombre','precio'], has_headers = False)
    camion = parse_csv('../Data/missing.csv', types = [str, int, float])
    print(camion)
    camion = parse_csv('../Data/missing.csv', types = [str,int,float], silence_errors = True)
    print(camion)
