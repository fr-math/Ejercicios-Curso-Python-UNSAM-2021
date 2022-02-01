# Ejercicio 2.1

'''
>>> import os
>>> os.getcwd()
'C:\\Users\\admin\\Downloads\\Comahue\\Curso Python UNSaM\\ejercicios_python\\' # La salida va a cambiar
>>>
# Path : 'C:\\Users\\admin\\Downloads\\Comahue\\Curso Python UNSaM\\ejercicios_python\\Clase02\\'

>>> with open('C:\\Users\\admin\\Downloads\\Comahue\\Curso Python UNSaM\\ejercicios_python\\Data\\camion.csv', 'rt', encoding='utf8') as f:
...     data = f.read()

>>> data
'nombre,cajones,precio\n"Lima",100,32.20\n"Naranja",50,91.10\n"Caqui",150,83.44\n"Mandarina",200,51.23\n"Durazno",95,40.37\n"Mandarina",50,65.10\n"Naranja",100,70.44\n'
>>> print(data)
nombre,cajones,precio
"Lima",100,32.20
"Naranja",50,91.10
"Caqui",150,83.44
"Mandarina",200,51.23
"Durazno",95,40.37
"Mandarina",50,65.10
"Naranja",100,70.44
>>>

>>> with open('C:\\Users\\admin\\Downloads\\Comahue\\Curso Python UNSaM\\ejercicios_python\\Data\\camion.csv', 'rt', encoding='utf8') as f:
...     for line in f:
...         print(line, end = '')
...
nombre,cajones,precio
Naranja,50,91.1
Caqui,150,103.44
Mandarina,200,51.23
Durazno,95,40.37
Mandarina,50,65.1
Naranja,100,70.44
>>>

>>> f = open('C:\\Users\\admin\\Downloads\\Comahue\\Curso Python UNSaM\\ejercicios_python\\Data\\camion.csv', 'rt', encoding='utf8')
>>> headers = next(f)
>>> headers
'nombre,cajones,precio\n'
>>> for line in f:
...     print(line, end = '')
...
Naranja,50,91.1
Caqui,150,103.44
Mandarina,200,51.23
Durazno,95,40.37
Mandarina,50,65.1
Naranja,100,70.44
>>> f.close()
>>>

>>> f = open('C:\\Users\\admin\\Downloads\\Comahue\\Curso Python UNSaM\\ejercicios_python\\Data\\camion.csv', 'rt', encoding='utf8')
>>> headers = next(f).split(',')
>>> headers
['nombre', 'cajones', 'precio\n']
>>> for line in f:
...     row = line.split(',')
...     print(row)
...
['Naranja', '50', '91.1\n']
['Caqui', '150', '103.44\n']
['Mandarina', '200', '51.23\n']
['Durazno', '95', '40.37\n']
['Mandarina', '50', '65.1\n']
['Naranja', '100', '70.44\n']
>>> f.close()


# Ejercicio 2.2

import os 

costo = 0.0
f = open('C:\\Users\\admin\\Downloads\\Comahue\\Curso Python UNSaM\\ejercicios_python\\Data\\camion.csv', 'rt', encoding='utf8')
next(f)
for line in f:
    lista_linea = line.split(',')
    costo = costo + int(lista_linea[1]) * float(lista_linea[2])
f.close()
print(f'Costo total ${costo:0.2f}')


# Ejercicio 2.3

import os 

costo = 0.0
cantidad = 0
f = open('C:\\Users\\admin\\Downloads\\Comahue\\Curso Python UNSaM\\ejercicios_python\\Data\\precios.csv', 'rt', encoding='utf8')
next(f)
for line in f:
    lista_linea = line.split(',')
    if lista_linea[0] == 'Naranja':
        costo = float(lista_linea[1])
f.close()
print(f'El precio de la naranja es:\t${costo:0.2f}')


# Ejercicio 2.4

>>> import gzip
>>> with gzip.open('C:\\Users\\admin\\Downloads\\Comahue\\Curso Python UNSaM\\ejercicios_python\\Data\\camion.csv.gz', 'rt', encoding='utf8') as f:     
...     for line in f:
...         print(line, end='')
...
nombre,cajones,precio
Naranja,50,91.1
Caqui,150,103.44
Mandarina,200,51.23
Durazno,95,40.37
Mandarina,50,65.1
Naranja,100,70.44
>>>
'''