import numpy as np
import matplotlib.pyplot as plt 
'''
suma = 1
sumb = 1
a = 0
b = 0
z = 2
for i in range(1,20):
    a = 4 * (i**2)
    b = a - 1 
    suma *= a  
    sumb *= b
    zi = a/b
    z *= zi
    #print(a,'/',b,'\t\t\t',suma,'/',sumb)
    print(z)
'''
for i in range(5,100000):
    if not ((10**i) % 227378054475):
        print(i)
