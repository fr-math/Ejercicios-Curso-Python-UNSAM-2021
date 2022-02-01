# informe_funciones.py
# Ejercicio 6.4-5/11

# ATENCIÓN: Tenemos en cuenta que el módulo 'fileparse' no se encuentra dentro de los archivos adjuntos. Además 
# tenemos presente que la funcion parse_csv puede ser definida localmente (en este namespace) o importada desde 
# el namespace del módulo fileparse. Dejamos comentadas las sentencias que corresponden a la importación de 
# dicho módulo y su implementación.

import csv 
#import fileparse


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

def leer_camion(nombre_archivo):
    #camion = fileparse.parse_csv(nombre_archivo, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    camion = parse_csv(nombre_archivo, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    return camion

def leer_precios(nombre_archivo):
    #lista_precios = fileparse.parse_csv(nombre_archivo, types = [str, float], has_headers = False)
    lista_precios = parse_csv(nombre_archivo, types = [str, float], has_headers = False)
    precios = dict(lista_precios)
    return precios

def hacer_informe(lista_cajones, precios):
    lista_informe = [] # lista = [(nombre,cajones,precio,cambio)]
    for cajon in lista_cajones:
        cajon_aux = (str(cajon['nombre']), int(cajon['cajones']), float(precios[cajon['nombre']]), float(precios[cajon['nombre']] - cajon['precio']))
        lista_informe.append(cajon_aux)
    return lista_informe

def separador_interno():
    print(('-'*10 + ' ')*4)
    return

def separador_externo():
    print('\n'+'*'*43)
    return

def imprimir_informe(informe):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    encabezado_formateado = f'{headers[0]:>10} {headers[1]:>10} {headers[2]:>10} {headers[3]:>10}'  #Un poco de formato no mas
    separador_externo()
    print(encabezado_formateado)
    separador_interno()
    for nombre, cajones, precio, cambio in informe:
            precio = f'$'+f'{precio:.2f}'
            print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')
    separador_externo()
    return

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion,precios)
    imprimir_informe(informe)
    return

if __name__ == '__main__':
    informe_camion('../Data/camion.csv','../Data/precios.csv')