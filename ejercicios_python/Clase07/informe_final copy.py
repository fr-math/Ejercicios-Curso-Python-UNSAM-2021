#!/usr/bin/env python3
# informe_funciones.py
# Ejercicio 7.4-7


import csv
import fileparse
import sys


def leer_camion(nombre_archivo):
    camion = fileparse.parse_csv(nombre_archivo, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    return camion

def leer_precios(nombre_archivo):
    lista_precios = fileparse.parse_csv(nombre_archivo, types = [str, float], has_headers = False)
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

def separador_externo():
    print('\n'+'*'*43)

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

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion,precios)
    imprimir_informe(informe)

def f_principal(parametros):
    camion = parametros[1]
    precios = parametros[2]
    informe_camion(camion,precios)


if __name__ == '__main__':
    if len(sys.argv) != 3 :
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion archivo_precios')
    else:
        f_principal(sys.argv)