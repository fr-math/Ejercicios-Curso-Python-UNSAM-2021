# Ejercicio 5.7

import numpy as np

v1 = np.arange(1,20,2)      
v2 = np.linspace(1,19,10)
type(v1[0])                                       #<class 'numpy.int32'>
type(v2[0])                                       #<class 'numpy.float64'>
x = np.ones(2, dtype=np.int64)
x                                                 #array([1, 1], dtype=int64)

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
np.sort(arr)                                      #array([1, 2, 3, 4, 5, 6, 7, 8])

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
np.concatenate((a,b))                             #array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
np.concatenate((x,y), axis=0)                     #array([[1, 2],
                                                  #       [3, 4],
                                                  #       [5, 6]])

array_ejemplo = np.array([[[0, 1, 2, 3], [4, 5, 6, 7]], [[0, 1, 2, 3], [4, 5, 6, 7]], [[0 ,1 ,2, 3], [4, 5, 6, 7]]])
array_ejemplo.ndim                                # 3
array_ejemplo.shape                               # (3, 2, 4)
array_ejemplo.size                                # 24

a = np.arange(6)
print(a)
b = a.reshape(3,2)
print(b)

a = np.array([1,2,3,4,5,6])
a.shape
vec_fila = a[np.newaxis, :]
vec_fila.shape
vec_col = a[:,np.newaxis]
vec_col.shape

data = np.array([1,2,3])
data[1]
data[0:2]
data[1:]
data[-2:]

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[a < 5])
five_up = (a >= 5)
print(a[five_up])
pares = a[a%2==0] 
print(pares)
c = a[(a>2) & (a<11)]
print(c)
five_up = (a > 5) | (a == 5)
print(five_up)

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b = np.nonzero(a < 5)
print(b) 
lista_de_coordenadas = list(zip(b[0], b[1]))
print(lista_de_coordenadas)

data = np.array([1, 2])
ones = np.ones(2, dtype=int)
data * data