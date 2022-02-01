#!/usr/bin/env python3
# Ejercicio 10.1

'''
>>> a = [1,9,4,25,16]
>>> i = a.__iter__()
>>> i
<listiterator object at 0x64c10>
>>> i.__next__()
1
>>> i.__next__()
9
>>> i.__next__()
4
>>> i.__next__()
25
>>> i.__next__()
16
>>> i.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>


>>> f = open('../Data/camion.csv')
>>> f.__iter__()    # Notar que esto apunta al método...
                    # ...que accede al archivo mismo.
<_io.TextIOWrapper name='../Data/camion.csv' mode='r' encoding='UTF-8'>
>>> next(f)
'nombre,cajones,precio\n'
>>> next(f)
'Lima,100,32.20\n'
>>> next(f)
'Naranja,50,91.10\n'
>>>
'''