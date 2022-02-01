# Ejercicio 2.11

import csv
f = open('c:\\Users\\admin\\Downloads\\Comahue\\Curso Python UNSaM\\ejercicios_python\\Data\\camion.csv', encoding='utf8')
filas = csv.reader(f)
next(filas)
fila = next(filas)
fila
t = (fila[0], int(fila[1]), float(fila[2]))
t
cost = t[1] * t[2]
cost
print(f'{cost:0.2f}')
t[1] = 75
t = (t[0], 75, t[2])
t
nombre, cajones, precio = t
nombre
cajones
precio
t = (nombre, 2*cajones, precio)
t

# Ejercicio 2.12

d = {'nombre' : fila[0],'cajones' : int(fila[1]),'precio' : float(fila[2])}
d
cost = d['cajones'] * d['precio']
cost
d['cajones'] = 75
d
d['fecha'] = (14,8,2021)
d['cuenta'] = 12345
d

# Ejercicio 2.13

for k in d:
    print('k =',k)
for k in d:
    print(k, '=', d[k])
items = d.items()
items
for k, v in d.items():
    print(k, '=', v)
list(d)
claves = d.keys()
claves
nuevos_items =  [('nombre','Manzanas'),('cajones',100),('precio',490.1),('fecha',(14,8,2021))]
nuevos_items
d = dict(nuevos_items)
d

