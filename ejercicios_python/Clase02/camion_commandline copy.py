'''

def costo_camion(nombre_archivo):
    import os
    import csv
    costo = 0.0
    f = open(nombre_archivo, 'rt')
    rows = csv.reader(f)
    next(f)
    try:
        for row in rows:
            costo += int(row[1]) * float(row[2])
    except ValueError:
        print('ATENCIÓN! Hay una celda con formato no válido ó incompleta.')
    f.close()
    return(costo)
'''
import csv
import sys

def costo_camion(nombre_archivo):
    costo = 0.0
    f = open(nombre_archivo, 'rt', encoding='utf8')
    rows = csv.reader(f)
    next(f)
    try:
        for row in rows:
            costo += int(row[1]) * float(row[2])
    except ValueError:
        print('ATENCIÓN! Hay una celda con formato no válido ó incompleta.')
    f.close()
    return(costo)

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'c:/Users/admin/Downloads/Comahue/Curso Python UNSaM/ejercicios_python/Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)
