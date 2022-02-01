# Ejercicio 1.19
'''
>>> frutas = 'Melón,Manzana,Naranja,Mandarina,Banana,Kiwi,Pera'
>>> frutas.lower()
'melón,manzana,naranja,mandarina,banana,kiwi,pera'
>>> frutas
'Melón,Manzana,Naranja,Mandarina,Banana,Kiwi,Pera'
>>> lowersyms = frutas.lower()
>>> frutas.find('Mandarina')
22
>>> frutas[13:17]
',Nar'
>>> frutas = frutas.replace('Kiwi','Melón')
>>> frutas
'Melón,Manzana,Naranja,Mandarina,Banana,Melón,Pera'
>>> nombre = '   Naranja   \n'
>>> nombre = nombre.strip()
>>> nombre
'Naranja'

# Ejercicio 1.20

nombre = 'Naranja'
cajones = 100
precio = 91.1
f'{cajones} cajones de {nombre} a ${precio:0.2f}'


# Ejercicio 1.21

>>> texto = 'Hoy es 6/8/2020. Mañana será 7/8/2020.'
>>> import re
>>> re.findall(r'\d+/\d+/\d+', texto)
['6/8/2020', '7/8/2020']
>>> re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\2-\1', texto)
'Hoy es 2020-8-6. Mañana será 2020-8-7.'
>>>


# Ejercicio 1.22

>>> frutas = 'Frambuesa,Manzana,Naranja,Mandarina,Banana,Sandía,Pera'
>>> lista_frutas = frutas.split(',')

>>> lista_frutas[0]
'Frambuesa'
>>> lista_frutas[1]
'Manzana'
>>> lista_frutas[-1]
'Pera'
>>> lista_frutas[-2]
'Sandía'
>>>
>>> lista_frutas[2] = 'Granada'
>>> lista_frutas
['Frambuesa', 'Manzana', 'Granada', 'Mandarina', 'Banana', 'Sandía', 'Pera']
>>>
>>> lista_frutas[0:3]
['Frambuesa', 'Manzana', 'Granada']
>>> lista_frutas[-2:]
['Sandía', 'Pera']
>>>
>>> compra = []
>>> compra.append('Pera')
>>> compra
['Pera']
>>> lista_frutas[-2:] = compra
>>> lista_frutas
['Frambuesa', 'Manzana', 'Granada', 'Mandarina', 'Banana', 'Pera']
>>>

# Ejercicio 1.23

>>> for s in lista_frutas:
        print('s =', s)
s= Frambuesa
s= Manzana
s= Granada
s= Mandarina
s= Banana
s= Pera
>>>


# Ejercicio 1.24

>>> 'Granada' in lista_frutas # ¿Está 'Granada' IN `lista_frutas`?
True
>>> 'Lima' in lista_frutas # ¿Está 'Lima' IN `lista_frutas`?
False
>>> 'Limon' not in lista_frutas # ¿Está 'Limon' NOT IN `lista_frutas`?
True
>>>


# Ejercicio 1.25

>>> lista_frutas.append('Mango') # agregar 'Mango'
>>> lista_frutas
['Frambuesa', 'Manzana', 'Granada', 'Mandarina', 'Banana', 'Pera', 'Mango']
>>>
>>> lista_frutas.insert(1,'Lima') # Insertar 'Lima' como segundo elemento
>>> lista_frutas
['Frambuesa', 'Lima', 'Manzana', 'Granada', 'Mandarina', 'Banana', 'Pera', 'Mango']
>>>
>>> lista_frutas.remove('Mandarina') # Borrar 'Mandarina'
>>> lista_frutas
['Frambuesa', 'Lima', 'Manzana', 'Granada', 'Banana', 'Pera', 'Mango']
>>>
>>> lista_frutas.append('Banana') # Agregar 'Banana'
>>> lista_frutas
['Frambuesa', 'Lima', 'Manzana', 'Granada', 'Banana', 'Pera', 'Mango', 'Banana']
>>>
>>> lista_frutas.index('Banana') # Encontrar la primera aparición de 'Banana'
>>> lista_frutas
4
>>> lista_frutas[4]
'Banana'
>>>
>>> lista_frutas.count('Banana')
2
>>>
>>> lista_frutas.remove('Banana') # Borrar la primer aparición de 'Banana'
>>> lista_frutas
['Frambuesa', 'Lima', 'Manzana', 'Granada', 'Pera', 'Mango', 'Banana']
>>>


# Ejercicio 1.26

>>> lista_frutas.sort()
>>> lista_frutas
['Banana', 'Frambuesa', 'Granada', 'Lima', 'Mango', 'Manzana', 'Pera']
>>>
>>> lista_frutas.sort(reverse=True)
>>> lista_frutas
['Pera', 'Manzana', 'Mango', 'Lima', 'Granada', 'Frambuesa', 'Banana']
>>>


# Ejercicio 1.27

>>> lista_frutas = ['Banana', 'Mango', 'Frambuesa', 'Pera', 'Granada', 'Manzana', 'Lima']
>>> a = ','.join(lista_frutas)
>>> a
'Banana,Mango,Frambuesa,Pera,Granada,Manzana,Lima'
>>> b = ':'.join(lista_frutas)
>>> b
'Banana:Mango:Frambuesa:Pera:Granada:Manzana:Lima'
>>> c = ''.join(lista_frutas)
>>> c
'BananaMangoFrambuesaPeraGranadaManzanaLima'
>>>


# Ejercicio 1.28

>>> nums = [101, 102, 103]
>>> items = ['spam', lista_frutas, nums]
>>> items
['spam', ['Banana', 'Mango', 'Frambuesa', 'Pera', 'Granada', 'Manzana', 'Lima'], [101, 102, 103]]
>>>
>>> items[0]
'spam'
>>> items[0][0]
's'
>>> items[1]
['Banana', 'Mango', 'Frambuesa', 'Pera', 'Granada', 'Manzana', 'Lima']
>>> items[1][1]
'Mango'
>>> items[1][1][2]
'n'
>>> items[2]
[101, 102, 103]
>>> items[2][1]
102
>>>
'''



