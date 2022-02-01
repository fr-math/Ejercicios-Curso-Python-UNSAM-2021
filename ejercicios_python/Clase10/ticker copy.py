#!/usr/bin/env python3
# ticker.py
# Ejercicio 10.8


from vigilante import vigilar
import csv
import informe_final
import formato_tabla


def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]
    

def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def filtrar_datos(rows, nombres):
    for row in rows:
        if row['nombre'] in nombres:
            yield row

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows

def imprimir_informe(rows, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, precio, volumen) 
    '''
    formateador.encabezado(['Nombre', 'Precio', 'Volumen'])
    for row in rows:
        linea = [str(value) for value in row.values()]
        formateador.fila(linea)

def ticker(camion_file, log_file, fmt):
    camion = informe_final.leer_camion(camion_file)
    rows = parsear_datos(vigilar(log_file))
    rows = filtrar_datos(rows, camion)
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(rows,formateador)
    


if __name__ == '__main__':
   ticker('../Data/camion.csv', '../Data/mercadolog.csv','txt')
   ticker('../Data/camion.csv', '../Data/mercadolog.csv','csv')
   ticker('../Data/camion.csv', '../Data/mercadolog.csv','html')
    
        