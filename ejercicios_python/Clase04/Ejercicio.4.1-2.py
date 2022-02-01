# Ejercicio 4.1
def invertir_lista(lista):
    '''Recibe una lista L y la develve invertida.'''
    invertida = []
    i = len(lista)
    while i > 0:    # tomo el último elemento 
        i = i-1
        invertida.append (lista.pop(i))  # paso clave (*)
    return invertida

l = [1, 2, 3, 4, 5]    
m = invertir_lista(l)
print(f'Entrada {l}, Salida: {m}')

# El método list.pop(i) remueve el elemento i de la lista list y devuelve el elemento i


# Ejercicio 4.2

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion = []
    registro = {}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:                              #
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('./Data/camion.csv')
pprint(camion)

# Como cada elemento del diccionario "registro" es pasado al ciclo por referencia, al iterar 
# en la segunda fila, se sobreescriben los valores de cada clave en el mismo, al ser un objeto 
# mutable. Esto causa que la lista de diccionarios "camion", modifique en cada ciclo todos sus 
# elementos, al estar referenciados a el diccionario "registro".