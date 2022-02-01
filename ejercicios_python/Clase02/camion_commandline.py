# camion_commandline.py
# Ejercicio 2.10
# Nota : Como la consola no reconocía la ruta relativa (relative path) por razones de configuración 
# preexistentes, se decidió utilizar la ruta absoluta (full/absolute path). Dado que esto hace que 
# se pierda la generalidad, se recomienda cambiar la misma a la correspondiente en su máquina o 
# cambiar las rutas absolutas por relativas, i.e., 
#
# C:\\Users\\admin\\Downloads\\Comahue\\Curso Python UNSaM\\ejercicios_python\\Data\\camion.csv --> ../Data/camion.csv
#
# respectivamente. En caso contrario, no se asegura que el programa funcione.

import csv
import sys

def costo_camion(nombre_archivo):
    '''Toma la ruta de un archivo tipo camión.csv y devuelve la suma de los valores de las columnas 
    de cajones por la de su precio respectivo, i.e., el costo total. Además avisa si hay celdas 
    incompletas. '''
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

archivo = 'c:/Users/admin/Downloads/Comahue/Curso Python UNSaM/ejercicios_python/Data/camion.csv'
#archivo = 'c:/Users/admin/Downloads/Comahue/Curso Python UNSaM/ejercicios_python/Data/camion2.csv'
#archivo = 'c:/Users/admin/Downloads/Comahue/Curso Python UNSaM/ejercicios_python/Data/missing.csv'
#archivo = input("Ingrese la ruta del archivo del camión que desea calcular el costo:\t")

costo = costo_camion(archivo)
print(f'Costo total:\t{costo:0.2f}')

# Costo total:    47671.15
# Costo total:    19908.75
# ATENCIÓN! Hay una celda con formato no válido ó incompleta.
# Costo total:    23291.00
# Depende del archivo, probé con los de arriba poniendo el path a mano y da