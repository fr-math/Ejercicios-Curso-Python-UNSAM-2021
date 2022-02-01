# arboles.py

#Importación de módulos
import matplotlib.pyplot as plt
import numpy as np
import csv
import os 


#Definición de funciones
def leer_arboles(nombre_archivo):
    arboleda = []
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        arboles = csv.reader(f)
        encabezados = next(arboles)
        for arbol in arboles:
            linea = dict(zip(encabezados, arbol))
            arboleda.append(linea)
    return arboleda

def medidas_de_especies(especies, arboleda):
    medidas = { especie : [(float(arbol['altura_tot']) , float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie] for especie in especies}
    return medidas

def histograma_alturas_jacaranda():
    arboleda = leer_arboles(os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv'))
    alturas_jacaranda = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
    plt.figure()
    plt.hist(alturas_jacaranda,bins=50)
    plt.xlabel("Altura (m)")
    plt.ylabel("Cantidad de Jacarandás (unidades)")
    plt.title("Histograma de las alturas de los Jacarandás en parques porteños.")
    plt.show()
    return

def scatter_hd(lista_de_pares):
    vector_de_pares = np.array(lista_de_pares)
    d = vector_de_pares.T[1]
    h = vector_de_pares.T[0]
    plt.figure()
    plt.scatter(d,h,c=d*h,alpha=0.2)
    plt.xlabel("Diámetro (cm)")
    plt.ylabel("Altura (m)")
    plt.title("Relación diámetro-alto para Jacarandá")
    plt.show()
    return

def dispersion_diam_vs_alt(especies, arboleda=False):
    arboleda = leer_arboles(os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv'))
    medidas = medidas_de_especies(especies, arboleda)
    for especie in especies:
        vector_de_pares = np.array(medidas[especie])
        d = vector_de_pares.T[1]
        h = vector_de_pares.T[0]
        plt.figure()
        plt.scatter(d,h,c=d*h,alpha=0.2)
        plt.xlim(0,180) 
        plt.ylim(0,50) 
        plt.xlabel("Diámetro (cm)")
        plt.ylabel("Altura (m)")
        titulo = 'Relación diámetro-alto para ' + especie
        plt.title(titulo)
        plt.show()
    return


#Programa
if __name__ == '__main__':
    arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
    alturas_diam_jacaranda = [(float(arbol['altura_tot']) , float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
    lista_especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    histograma_alturas_jacaranda()
    scatter_hd(alturas_diam_jacaranda)
    dispersion_diam_vs_alt(lista_especies,arboleda)
