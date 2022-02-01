#!/usr/bin/env python3
# ticker.py
# Ejercicio 10.15


from vigilante import vigilar
import csv
import informe_final
import formato_tabla


def parsear_datos(lines):
    '''
    Parsea los datos provenientes de un productor regresando las filas 
    producidas en un diccionario.
    '''
    rows = csv.reader(lines)
    rows = ((row[index] for index in [0,1,2]) for row in rows)
    types = [str, float, int]
    rows = ((func(val) for func, val in zip(types, row)) for row in rows) 
    headers = ['nombre', 'precio', 'volumen']
    rows = (dict(zip(headers, row)) for row in rows)
    return rows

def imprimir_informe(rows, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, precio, volumen) 
    '''
    formateador.encabezado(['Nombre', 'Precio', 'Volumen'])
    for row in rows:
        linea = (str(value) for value in row.values())
        formateador.fila(linea)

def ticker(camion_file, log_file, fmt):
    '''
    Genera un informe en tiempo real y lo imprime en pantalla, a partir de
    los elementos de un lote de un camion de verdura, acorde a los precios 
    generados en un log.
    '''
    camion = informe_final.leer_camion(camion_file)
    rows = parsear_datos(vigilar(log_file))
    rows = (row for row in rows if row['nombre'] in camion)
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(rows,formateador)
    


if __name__ == '__main__':
   ticker('../Data/camion.csv', '../Data/mercadolog.csv','txt')
   #ticker('../Data/camion.csv', '../Data/mercadolog.csv','csv')
   #ticker('../Data/camion.csv', '../Data/mercadolog.csv','html')
    
        