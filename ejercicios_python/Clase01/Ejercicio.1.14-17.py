'''
# Ejercicio 1.14

>>> frutas[0]
'M'
>>> frutas[1]
'a'
>>> frutas[2]
'n'
>>> frutas[-1]        # Último caracter
'i'
>>> frutas[-2]        # Índices negativos se cuentan desde el final
'w'
>>>

>>> frutas[0] = 'm'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>>

# Ejercicio 1.15

>>> frutas = frutas + 'Pera'
>>> frutas
'Manzana,Naranja,Mandarina,Banana,KiwiPera'
>>>

>>> frutas = frutas.replace('Pera',',Pera')
>>> frutas
'Manzana,Naranja,Mandarina,Banana,Kiwi,Pera'
>>>

>>> frutas = 'Melón' + frutas
>>> frutas
'Melón,Manzana,Naranja,Mandarina,Banana,Kiwi,Pera'
>>>

# Ejercicio 1.16

>>> 'Naranja' in frutas
True
>>> 'nana' in frutas
True                        #'nana' dió True porque aparece en la cadena como parte de 'Banana'
>>> 'Lima' in frutas
False
>>>

# Ejercicio 1.17

>>> cadena = "Ejemplo con for"
>>> for c in cadena:
        print('caracter:', c)
'''

cadena = "Ejemplo con for"
cont = 0
for c in cadena:
    if (c=='o'):
        cont += 1
    print('caracter:', c)
print("Número de letras 'o' = ",cont)