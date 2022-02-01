#!/usr/bin/env python3
# ordenar_imgs.py
# Ejercicio 8.6


import os
import sys
import datetime

 
def crear_directorio(new_dir):
    '''Crea el directorio new_dir '''
    os.mkdir(new_dir)

def procesar_nombre(fname):
    '''Toma un nombre de un archivo en formato str y devuelve la fecha y el 
    nombre corregido en una tupla nombre,fecha.'''
    nombre = fname[:-13] + fname[-4:]
    fecha = datetime.datetime.strptime(fname[-12:-4], '%Y%m%d')
    return nombre,fecha

def procesar(fname,root=os.path.join('..','Data'),
             new_dir=os.path.join('..','Data','imgs_procesadas')):
    '''Toma un nombre de archivo en formato str, lo renombra, modifica la 
    fecha de última modificación y de acceso del archivo y lo mueve al 
    directorio nuevo. 
    '''
    nombre = procesar_nombre(fname)[0]
    os.rename(os.path.join(root,fname),
              os.path.join(new_dir,nombre))
    fecha = procesar_nombre(fname)[1]
    ts_acceso = fecha.timestamp()
    ts_modifi = fecha.timestamp()
    os.utime(os.path.join(new_dir,nombre),
             (ts_acceso, ts_modifi))

def extraer_png(root_dir,new_dir):
    '''Toma un directorio root_dir en formato str y renmbra, modifica la fecha
     de ultima modificación y mueve los archivos png al directorio new_dir. 
    Remueve los directorios que quedaron vacíos.
    '''
    for root, dirs, files in os.walk(root_dir):
        for name in files:
            if name[-4:] == '.png':
                procesar(name,root,new_dir)
    for root, dirs, files in os.walk(root_dir,topdown=False):
        for dir in dirs:
            if not os.listdir(os.path.join(root,dir)):
                os.rmdir(os.path.join(root,dir))


if __name__ == '__main__':    
    if len(sys.argv) != 3:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'directorio_original'
                         'directorio_destino')
    else:
        crear_directorio(sys.argv[2])
        extraer_png(sys.argv[1],sys.argv[2])
