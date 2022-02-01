#!/usr/bin/env python3
# ordenar_imgs.py
# Ejercicio 8.6


import os
import sys


def archivos_png(directorio):
    '''Toma un directorio en formato str y devuelve una lista de los archivos
    de formato .png en formato str.'''
    list_png = []
    for root, dirs, files in os.walk(directorio):
        for name in files:
            if (os.path.join(root, name)[-4:] == '.png'):
                list_png.append(name)
    return list_png


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'directorio')
    else:
        print(archivos_png(sys.argv[1]))