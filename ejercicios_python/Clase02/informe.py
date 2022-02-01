# Ejercicio 3.9
# Importación de módulos/bibliotecas

import csv 

# Definición de funciones

def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            cajon = dict(zip(headers,row))
            cajon['cajones'] = int(cajon['cajones'])
            cajon['precio'] = float(cajon['precio'])
            camion.append(cajon)
    return camion

def leer_precios(nombre_archivo):
    precios = {}
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        try:
            for row in rows:
                precios[row[0]] = float(row[1])
        except IndexError:
            print('Hay líneas incompletas o vacías')
    return precios

# Programa

#camion = leer_camion('../Data/camion.csv')
camion = leer_camion('../Data/fecha_camion.csv')
precios = leer_precios('../Data/precios.csv')

costo_camion = 0.0
recaudacion = 0.0
diferencia = 0.0

for s in camion:
    costo_camion += s['cajones'] * s['precio']
    recaudacion += s['cajones'] * precios[s['nombre']]
diferencia = recaudacion - costo_camion

print(f'*************************************\n\t* BALANCE DE VENTAS *\t\n*************************************\n Costo del camión:\t${costo_camion:0.2f}\n Recaudación :\t\t${recaudacion:0.2f}\n Diferencia:\t\t${diferencia:0.2f}\n*************************************\n Ganancia bruta:\t${diferencia:0.2f}\n*************************************')