#!/usr/bin/env python3
# Ejercicio 8.8


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


#importo el dataset
directorio = '../Data'
archivo = 'arbolado-publico-lineal-2017-2018.csv'
fname = os.path.join(directorio,archivo)
df = pd.read_csv(fname)
#armo el dataframe de las columnas que se quieren
cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
df_lineal = df[cols_sel].copy()
#elijo especies y armo un nuevo dataframe
especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]
#armo un boxplot de los altos agrupados por especie. 
df_lineal_seleccion.boxplot('altura_arbol', by = 'nombre_cientifico')
plt.title('Gráfico de cajas de las alturas de los arboles, agrupadas por nombre científico.')
plt.xlabel('Especies')
plt.show()
sns.pairplot(data = df_lineal_seleccion[cols_sel], hue = 'nombre_cientifico')
plt.show()