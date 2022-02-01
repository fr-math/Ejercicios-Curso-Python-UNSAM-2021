#%%
# Ejercicio 2.2
# Como programa

import os 

costo = 0.0
f = open('C:\\Users\\admin\\Downloads\\Comahue\\Curso Python UNSaM\\ejercicios_python\\Data\\camion.csv', 'rt', encoding='utf8')
next(f)
for line in f:
    lista_linea = line.split(',')
    costo = costo + int(lista_linea[1]) * float(lista_linea[2])
f.close()
print(f'Costo total ${costo:0.2f}')

#%%
# Como función

def costo_camion(nombre_archivo):
    import os
    costo = 0.0
    f = open(nombre_archivo, 'rt', encoding='utf8')
    next(f)
    for line in f:
        lista_linea = line.split(',')
        costo += int(lista_linea[1]) * float(lista_linea[2])
    f.close()
    return(costo)

costo = costo_camion('C:\\Users\\admin\\Downloads\\Comahue\\Curso Python UNSaM\\ejercicios_python\\Data\\camion.csv')
print(f'Costo total ${costo:0.2f}')

#%%
# Captando errores

def costo_camion(nombre_archivo):
    import os
    costo = 0.0
    f = open(nombre_archivo, 'rt', encoding='utf8')
    next(f)
    try:
        for line in f:
            lista_linea = line.split(',')
            costo += int(lista_linea[1]) * float(lista_linea[2])
    except ValueError:
        print('ATENCIÓN! Hay una celda con formato no válido ó incompleta.')
    f.close()
    return(costo)

#%%
# Ejercicio 2.9

def costo_camion(nombre_archivo):
    import os
    import csv
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
#%%
# Ejercicio 3.8
import os
import csv

def costo_camion(nombre_archivo):
    #Toma la ruta de un archivo tipo camión.csv y devuelve la suma de los valores de las columnas 
    #de cajones por la de su precio respectivo, i.e., el costo total. Además avisa si hay celdas 
    #incompletas.
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

#%%
# Ejercicio 3.9

import os
import csv

def costo_camion(nombre_archivo):
    costo = 0.0
    f = open(nombre_archivo, 'rt', encoding='utf8')
    filas = csv.reader(f)
    encabezados = next(f).strip()
    encabezados = encabezados.split(',')
    for n_fila, fila in enumerate(filas, start=1):
        record = dict(zip(encabezados,fila))
        print(record)
        try:
            ncajones = int(record['cajones'])
            precio = float(record['precio'])
            costo += ncajones * precio
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar: {fila}')
    f.close()
    return(costo)


