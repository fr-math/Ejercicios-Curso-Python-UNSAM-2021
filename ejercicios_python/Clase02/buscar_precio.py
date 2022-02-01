# buscar_precio.py
# Ejercicio 2.7
# Nota : Como la consola no reconocía la ruta relativa (relative path) por razones de configuración 
# preexistentes, se decidió utilizar la ruta absoluta (full/absolute path). Dado que esto hace que 
# se pierda la generalidad, se recomienda cambiar la misma a la correspondiente en su máquina o 
# cambiar las rutas absolutas por relativas, i.e., 
#
# C:\\Users\\admin\\Downloads\\Comahue\\Curso Python UNSaM\\ejercicios_python\\Data\\precios.csv --> ../Data/precios.csv
#
# respectivamente. En caso contrario, no se asegura que el programa funcione.

import os

def buscar_precio(fruta):
    '''Busca en el archivo el precio de una fruta por su nombre, si está imprime su valor en pantalla,
     si no imprime que no está en el listado.'''
    costo = False
    f = open('C:\\Users\\admin\\Downloads\\Comahue\\Curso Python UNSaM\\ejercicios_python\\Data\\precios.csv', 'rt', encoding='utf8')
    next(f)
    for line in f:
        lista_linea = line.split(',')
        if lista_linea[0] == fruta:
            costo = float(lista_linea[1])
            print(f'El precio de un cajón de {fruta} es:\t${costo:0.2f}')
    if costo == False:
        print(f'{fruta} no figura en el listado de precios.')
    f.close()
    return

# >>> buscar_precio('Frambuesa')
# El precio de un cajón de Frambuesa es:  $34.35
# >>> buscar_precio('Kale')
# Kale no figura en el listado de precios.
# >>>