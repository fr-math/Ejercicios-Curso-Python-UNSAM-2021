# arboles.py

import csv

def leer_arboles(nombre_archivo):
    arboleda = []
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        arboles = csv.reader(f)
        encabezados = next(arboles)
        for arbol in arboles:
            linea = dict(zip(encabezados, arbol))
            arboleda.append(linea)
    return arboleda

'''
def medidas_de_especies(especies, arboleda):
    medidas = {}
    for especie in especies:
        medidas[especie] = [(float(arbol['altura_tot']) , float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie]
    return medidas
'''

def medidas_de_especies(especies, arboleda):
    medidas = { especie : [(float(arbol['altura_tot']) , float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie] for especie in especies}
    return medidas



if __name__ == '__main__':
    arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
    
    #Ejercicio 4.16
    alturas_jacaranda = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

    #Ejercicio 4.16
    alturas_diam_jacaranda = [(float(arbol['altura_tot']) , float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

    lista_especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    dicc_arb = medidas_de_especies(lista_especies, arboleda)
    print(len(dicc_arb['Eucalipto']),'\t',len(dicc_arb['Palo borracho rosado']),'\t',len(dicc_arb['Jacarandá']))
