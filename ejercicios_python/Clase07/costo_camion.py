#!/usr/bin/env python3
# costo_camion.py
# Ejercicio 6.12

# ATENCIÓN: Tenemos en cuenta que los módulos 'fileparse' e 'informe_funciones' no se encuentran dentro de los 
# archivos adjuntos. Además tenemos presente que las funciones importadas involucradas pueden ser definidas 
# localmente (en este namespace) o importadas desde el namespace del módulo pertinente. Dejamos comentadas las 
# sentencias que corresponden a la importación de dichos módulos y su implementación.

import informe_final
import csv 
import fileparse

'''
def parse_csv(nombre_archivo, select = None, types=None, has_headers=True):
    
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    Se puede seleccionar el tipo de dato de cada columna, sabiendo su índice y asignandole una lista con las funciones conversoras a el parámetro types.
    En caso de no haber encabezados, se puede omitir la lectura de los mismos asignandole False al parámetro has_headers (has_headers=False). Esto devuelve una lista de tuplas.
    
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
'''

def leer_camion(nombre_archivo):
    camion = fileparse.parse_csv(nombre_archivo, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    #camion = parse_csv(nombre_archivo, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    return camion


def costo_camion(nombre_archivo):
    costo = 0.0
    camion = informe_final.leer_camion(nombre_archivo)
    #camion = leer_camion(nombre_archivo)
    for s in camion:
        costo += s['cajones'] * s['precio']
    f = open(nombre_archivo, 'rt', encoding='utf8')
    return(costo)

if __name__ == '__main__':
    camion = costo_camion('../Data/fecha_camion.csv')
    costo = '$' + f'{camion:0.2f}'
    print(f'El costo del camion es {costo}')