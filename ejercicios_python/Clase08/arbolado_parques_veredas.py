#!/usr/bin/env python3
# arbolado_parques_veredas.py
# Ejercicio 8.9


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


def importar_dataset(directorio,archivo):
    '''Toma un directorio y un archivo y carga el archivo como un dataframe.
    '''
    fname = os.path.join(directorio,archivo)
    df = pd.read_csv(fname)
    return df

def extraer_datos_especie(nombre_especie_veredas,
                        nombre_especie_parques,
                        df_veredas,
                        df_parques):
    '''Toma el nombre cientifico de una especie de arbol en dos dataframe (del
    tipo "arbolado-en-espacios-verdes.csv" y 
    "arbolado-publico-lineal-2017-2018.csv") devuelve un dataframe nuevo con 
    los datos de altura total, diametro, nombre científico y ambiente (parque 
    o vereda) de los espécimenes en cuestión, con los nombres de columna del 
    dataframe de veredas.'''
    #Selecciono columnas de interes
    cols_veredas = ['altura_arbol', 'diametro_altura_pecho',
                    'nombre_cientifico']
    cols_parques = ['altura_tot', 'diametro', 'nombre_cie']
    #Armo los df de parques y veredas con las columnas de interes
    df_arbol_veredas = df_veredas[df_veredas['nombre_cientifico'] == 
                                  nombre_especie_veredas][cols_veredas].copy()     
    df_arbol_parques = df_parques[df_parques['nombre_cie'] == 
                                  nombre_especie_parques][cols_parques].copy()
    #Cambio el nombre de las columnas al dataframe de parques para que 
    #coincida con el de las veredas
    dict_nombres = dict(zip(cols_parques,cols_veredas))
    df_arbol_parques.rename(columns=dict_nombres,inplace=True)
    #Agrego la columna "ambiente" seteado por defecto con el valor 
    #parque/vereda
    df_arbol_veredas['ambiente'] = ['vereda']*len(df_arbol_veredas.index)
    df_arbol_parques['ambiente'] = ['parque']*len(df_arbol_parques.index)
    #Concateno los dos dataframes
    df_arbol = pd.concat([df_arbol_veredas, df_arbol_parques])
    return df_arbol

if __name__ == '__main__':
    directorio = '../Data'
    archivo_veredas = 'arbolado-publico-lineal-2017-2018.csv'
    archivo_parques = 'arbolado-en-espacios-verdes.csv'
    df_veredas = importar_dataset(directorio,archivo_veredas)
    df_parques = importar_dataset(directorio,archivo_parques)
    df_tipas = extraer_datos_especie('Tipuana tipu',
                                     'Tipuana Tipu',
                                      df_veredas,
                                      df_parques)
    df_tipas.boxplot('diametro_altura_pecho',by = 'ambiente')
    plt.show()
    df_tipas.boxplot('altura_arbol',by = 'ambiente')
    plt.show()