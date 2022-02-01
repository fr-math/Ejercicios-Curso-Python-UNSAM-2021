# Ejercicio 3.13
# Importación de módulos/bibliotecas

import csv 

# Definición de funciones

def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        lineas = csv.reader(f)
        encabezados = next(lineas)
        for n_linea,linea in enumerate(lineas, start=1):
            try:
                cajon = dict(zip(encabezados,linea))
                cajon['cajones'] = int(cajon['cajones'])
                cajon['precio'] = float(cajon['precio'])
                camion.append(cajon)
            except (KeyError,ValueError):
                print(f'ATENCIÓN: La línea {n_linea} del archivo {nombre_archivo} está incompleta o vacía o no la pude interpretar.')
    return camion

def leer_precios(nombre_archivo):
    precios = {}
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        for n_row,row in enumerate(rows, start=1):
            try:
                precios[row[0]] = float(row[1])
            except IndexError:
                print(f'ATENCIÓN: La línea {n_row} del archivo {nombre_archivo} está incompleta o vacía o no la pude interpretar.')
    return precios

def hacer_informe(lista_cajones, precios):
    lista_informe = [] # lista = [(nombre,cajones,precio,cambio)]
    for cajon in lista_cajones:
        cajon_aux = (str(cajon['nombre']), int(cajon['cajones']), float(precios[cajon['nombre']]), float(precios[cajon['nombre']] - cajon['precio']))
        lista_informe.append(cajon_aux)
    return lista_informe

# Programa

camion = leer_camion('../Data/camion.csv')
#camion = leer_camion('../Data/camion2.csv')
#camion = leer_camion('../Data/camion_blancos.csv')
#camion = leer_camion('../Data/fecha_camion.csv')
precios = leer_precios('../Data/precios.csv')
informe = hacer_informe(camion,precios)
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
encabezado_formateado = f'{headers[0]:>10} {headers[1]:>10} {headers[2]:>10} {headers[3]:>10}'  #Un poco de formato no mas
def separador_interno():
    print(('-'*10 + ' ')*4)
def separador_externo():
    print('\n'+'*'*43)


separador_externo()
print(encabezado_formateado)
separador_interno()
for nombre, cajones, precio, cambio in informe:
        precio = f'$'+f'{precio:.2f}'
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')
separador_externo()

