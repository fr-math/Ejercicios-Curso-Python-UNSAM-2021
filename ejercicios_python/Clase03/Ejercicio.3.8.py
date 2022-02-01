#%% 
# Ejercicio 3.8
import os
import csv

def costo_camion(nombre_archivo):
    '''Toma la ruta de un archivo tipo camión.csv y devuelve la suma de los valores de las columnas 
    de cajones por la de su precio respectivo, i.e., el costo total. Además avisa si hay celdas 
    incompletas.'''
    costo = 0.0
    f = open(nombre_archivo, 'rt', encoding='utf8')
    filas = csv.reader(f)
    next(f)
    for n_fila, fila in enumerate(filas, start=1):
        try:
            costo += int(fila[1]) * float(fila[2])
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar: {fila}')
    f.close()
    return(costo)

# >>> costo_camion('C:\\Users\\admin\\Downloads\\Comahue\\Curso Python UNSaM\\ejercicios_python\\Data\\camion.csv')
# 47671.15