# fileparse.py
# Ejercicio 6.6-9

import csv

def parse_csv(nombre_archivo, select = None, types=None, has_headers=True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    Se puede seleccionar el tipo de dato de cada columna, sabiendo su índice y asignandole una lista con las funciones conversoras a el parámetro types.
    En caso de no haber encabezados, se puede omitir la lectura de los mismos asignandole False al parámetro has_headers (has_headers=False). Esto devuelve una lista de tuplas.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        if has_headers:
            encabezados = next(filas)
            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select
            else:
                indices = []
            registros = []
            for fila in filas:
                if not fila:    
                    continue
                if indices:
                    fila = [fila[index] for index in indices]
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ]
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
        else:
            registros = []
            for fila in filas:
                if not fila:    
                    continue
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ]
                registros.append(tuple(fila))
    return registros