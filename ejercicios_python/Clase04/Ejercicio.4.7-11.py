# Ejercicio 4.7

'''
nums = [1,2,3,4]
cuadrados = [x * x for x in nums]
cuadrados
dobles = [2 * x for x in nums if x > 2]
dobles
'''

# Ejercicio 4.8

'''
camion = leer_camion('../Data/camion.csv')
costo = sum([s['cajones'] * s['precio'] for s in camion])
costo

precios = leer_precios('../Data/precios.csv')
valor = sum([s['cajones'] * precios[s['nombre']] for s in camion])
valor

[s['cajones'] * s['precio'] for s in camion]

sum(_)
'''

# Ejercicio 4.9

'''
mas100 = [s for s in camion if s['cajones'] > 100]
mas100

myn = [s for s in camion if s['nombre'] in {'Mandarina','Naranja'}]
myn

costo10k = [s for s in camion if s['cajones'] * s['precio'] > 10000]
costo10k
'''

# Ejercicio 4.10

'''
nombre_cajones = [(s['nombre'],s['cajones']) for s in camion]
nombre_cajones

nombres = {s['nombre'] for s in camion}
nombres

stock = {nombre: 0 for nombre in nombres}
stock

for s in camion:
    stock[s['nombre']] += s['cajones']

camion_precios = {nombre: precios[nombre] for nombre in nombres}
camion_precios
'''

# Ejercicio 4.11

'''
import csv

f = open('../Data/fecha_camion.csv')
rows = csv.reader(f)
headers = next(rows)
headers

select = ['nombre','cajones','precio']

indices = [headers.index(ncolumna) for ncolumna in select]
indices

row = next(rows)
record = {ncolumna: row[index] for ncolumna,index in zip(select,indices)}
record

camion = [{ ncolumna: row[index] for ncolumna, index in zip(select,indices)} for row in rows]
camion
'''