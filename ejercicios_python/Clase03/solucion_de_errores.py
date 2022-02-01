# solucion_de_errores.py 
# Ejercicios de errores en el código 
# %%
# Ejercicio 3.1. Función tiene_a()
# Comentario: El error era semántico y estaba adentro del ciclo while (Linea 7) 
#   Lo solucioné eliminando el else y poniendo el return False afuera del ciclo. 
#   A continuación va el código corregido, 
# 
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False
# tiene_a('UNSAM 2021') --> False
# tiene_a('abracadabra') --> True
# tiene_a('La novela 1984 de George Orwell') --> True
# %% 
# Ejercicio 3.2. Función tiene_a()
# Comentario: El error era de sintaxis y estaba en las líneas 1,4,5 (missing ":") 
#   y 8 (syntax error, Falso is not defined ).
#   Lo solucioné agregando los ":" y cambiando "Falso" por "False". 
#   A continuación va el código corregido, 
# 
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False
# tiene_a('UNSAM 2021') --> False
# tiene_a('La novela 1984 de George Orwell') --> True   
# %% 
# Ejercicio 3.3. Función tiene_uno() 
# Comentario: El error era de tipo (TypeError), estaba en la definición del argumento, 
#   que debía ser del tipo string. Al ingresar un dato que no sea de tipo string, 
#   crashea. 
#   Lo solucioné casteando como string la variable "expresión" en las líneas 2 y 6. 
#   A continuación va el código corregido,
#
def tiene_uno(expresion):
    n = len(str(expresion))
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if str(expresion)[i] == '1':
            tiene = True
        i += 1
    return tiene

#tiene_uno('UNSAM 2020')
#tiene_uno('La novela 1984 de George Orwell')
#tiene_uno(1984)
#%%
#Ejercicio 3.4. Función suma() 
#   Comentario: El error es semántico, la función suma regresa None, pues no está 
#   definido el return en línea 3. 
#   Lo solucioné agregándole un return c.
#   A continuación va el código corregido,
#
def suma(a,b):
    c = a + b
    return c
    
#a = 2
#b = 3
#c = suma(a,b)
#print(f"La suma da {a} + {b} = {c}")
#%%
# Ejercicio 3.5. Función leer_camión() 
#   Comentario: El error es semántico, la función pisa el valor de la variable fila, 
#   sobre la cual se itera. La variable "camion" es una lista de diccionarios. Esta 
#   agrega en cada iteración el valor de "registro". Como registro es una variable 
#   global para el ciclo for, y al pasarse por referencia a "camión", sobreescribe 
#   su valor en cada ciclo, por lo que el resultado final de "camion" es una lista con  
#   n elementos iguales. Si se define "registro" localmente dentro del ciclo, este 
#   error no se produciría. 
#   Lo solucioné definiendo la variable "registro" dentro del ciclo. 
#   A continuación va el código corregido,
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)