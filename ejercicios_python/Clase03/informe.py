# Ejercicio 3.9

import os
import csv

def costo_camion(nombre_archivo):
    costo = 0.0
    f = open(nombre_archivo, 'rt', encoding='utf8')
    filas = csv.reader(f)
    encabezados = next(f)
    encabezados = encabezados.strip().split(',')
    for n_fila, fila in enumerate(filas, start=1):
        record = dict(zip(encabezados,fila))
        try:
            ncajones = int(record['cajones'])
            precio = float(record['precio'])
            costo += ncajones * precio
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar: {fila}')
    f.close()
    return(costo)

#camion = costo_camion('../Data/fecha_camion.csv')