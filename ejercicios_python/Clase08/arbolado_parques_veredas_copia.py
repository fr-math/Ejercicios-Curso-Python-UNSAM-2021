#!/usr/bin/env python3
# arbolado_parques_veredas.py
# Ejercicio 8.9


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


def importar_dataset(directorio,archivo):
    '''Toma un directorio y un archivo y carga el archivo como un dataframe.
    '''
    fname = os.path.join(directorio,archivo)
    df = pd.read_csv(fname)
    return df


if __name__ == '__main__':
    directorio = '../Data'
    archivo_veredas = 'arbolado-publico-lineal-2017-2018.csv'
    archivo_parques = 'arbolado-en-espacios-verdes.csv'

    #importo datasets
    df_veredas = importar_dataset(directorio,archivo_veredas)
    df_parques = importar_dataset(directorio,archivo_parques)

    #selecciono columnas útiles
    cols_veredas = ['altura_arbol', 'diametro_altura_pecho',
                    'nombre_cientifico']
    cols_parques = ['altura_tot', 'diametro', 'nombre_cie']

    #defino nuevos dataframes con las columnas útiles
    df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 
                                  'Tipuana tipu'][cols_veredas].copy()     
    df_tipas_parques = df_parques[df_parques['nombre_cie'] == 
                                  'Tipuana Tipu'][cols_parques].copy()

    #renombro las columnas del dataframe de las veredas
    dict_nombres = dict(zip(cols_parques,cols_veredas))
    df_tipas_parques.rename(columns=dict_nombres,inplace=True)    
    
    #agrego la columna ambiente a cada dataframe
    df_tipas_veredas['ambiente'] = ['vereda']*len(df_tipas_veredas.index)
    df_tipas_parques['ambiente'] = ['parque']*len(df_tipas_parques.index)
    
    #concatenamos los dos dataframes
    df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

    #hacemos un boxplot de los diámetros a la altura del pecho separado por 
    #ambiente
    df_tipas.boxplot('diametro_altura_pecho',by = 'ambiente')
    plt.show()
    df_tipas.boxplot('altura_arbol',by = 'ambiente')
    plt.show()