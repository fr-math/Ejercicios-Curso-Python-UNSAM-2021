import pandas as pd
import os

directorio = '../Data'
archivo = 'arbolado-en-espacios-verdes.csv'
fname = os.path.join(directorio,archivo)
df = pd.read_csv(fname)

df.head() #el argumento es el nro de filas a mostrar, 5 por omision
df.tail() #idem anterior    

df.columns
df.index

df[['altura_tot', 'diametro', 'inclinacio']].describe() # datos estadísticos de las columnas seleccionadas

df['nombre_com']
df['nombre_com'].unique() #muestra solo una vez cada dato distinto

df['nombre_com'] == 'Ombú' #pregunta cuales en nombre_com tienen el valor Ombú

(df['nombre_com'] == 'Ombú').sum()

cant_ejemplares = df['nombre_com'].value_counts()
cant_ejemplares.head(10)

df_jacarandas = df[df['nombre_com'] == 'Jacarandá']

cols = ['altura_tot', 'diametro', 'inclinacio']
df_jacarandas = df_jacarandas[cols]
df_jacarandas.tail()

df_jacarandas.describe()

df_jacarandas = df[df['nombre_com'] == 'Jacarandá'][cols].copy()
df_jacarandas.plot.scatter(x = 'diametro', y = 'altura_tot')

import seaborn as sns

sns.scatterplot(data = df_jacarandas, x = 'diametro', y = 'altura_tot')

import matplotlib.pyplot as plt
plt.show()

cant_ejemplares.index

df.loc[165]
cant_ejemplares.loc['Eucalipto']

df_jacarandas.iloc[0]
cant_ejemplares.iloc[0:3]
df_jacarandas.iloc[-5:,2]

df_jacarandas_diam = df_jacarandas['diametro']
type(df_jacarandas)
type(df_jacarandas_diam)

pd.date_range('20200923', periods = 7)
pd.date_range('20200923 14:00', periods = 7)
pd.date_range('20200923 14:00', periods = 6, freq = 'H')

pd.Series([1, 2, 3, 4, 5, 6], index = pd.date_range('20200923 14:00', periods = 6, freq = 'H'))


import numpy as np

idx = pd.date_range('20200923 14:00', periods = 120, freq = 'min')
s1 = pd.Series(np.random.randint(-1,2,120), index = idx)
s2 = s1.cumsum()
s2.plot()
plt.show()
w = 5 # ancho en minutos de la ventana
s3 = s2.rolling(w,min_periods=1).mean()
s3.plot()
plt.show()
df_series_23 = pd.DataFrame([s2, s3]).T  # armo un dataframe con ambas series
df_series_23.plot()
plt.show()

horas = 8
idx = pd.date_range('20200923 14:00', periods = horas*60, freq = 'min')
nombres = ['Pedro', 'Santiago', 'Juan', 'Andrés','Bartolomé','Tiago','Isca','Tadeo','Mateo','Felipe','Simón','Tomás']

df_walks = pd.DataFrame(np.random.randint(-1,2,[horas*60,12]).cumsum(axis=0), index = idx, columns = nombres)
df_walks.plot()
plt.show()
w = 45
df_walk_suav = df_walks.rolling(w, min_periods = 1).mean() # datos suavizados
nsuav = ['S_' + n for n in nombres]
df_walk_suav.columns = nsuav # cambio el nombre de las columnas
                             # para los datos suavizados
df_walk_suav.plot()
plt.show()

df_walk_suav.to_csv('caminata_apostolica.csv')