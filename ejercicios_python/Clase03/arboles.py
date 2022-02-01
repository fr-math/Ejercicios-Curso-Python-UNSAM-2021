# arboles.py
#%%
import csv
from collections import Counter

def leer_parque(nombre_archivo, parque):
    lista_parque = []
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        arboles = csv.reader(f)
        encabezados = next(arboles)
        for arbol in arboles:
            linea = dict(zip(encabezados,arbol))
            if linea['espacio_ve']==parque:
                arbol_parque = linea
                lista_parque.append(arbol_parque)
    return lista_parque

def especies(lista_arboles):
    especie_arbol = []
    for arbol in lista_arboles:
        especie_arbol.append(arbol['nombre_com'])
    conjunto_especies = set(especie_arbol)
    return conjunto_especies

def contar_ejemplares(lista_arboles):
    dict_especies = Counter()
    for arbol in lista_arboles:
        dict_especies[arbol['nombre_com']] += 1
    return dict_especies

def obtener_inclinaciones(lista_arboles,especie):
    inclinaciones = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            inclinaciones.append(arbol['inclinacio'])
    return inclinaciones


def especimen_mas_inclinado(lista_arboles):
    lista_especies = list(especies(lista_arboles))
    maximo = 0.0
    for especie in lista_especies:
        if maximo < float(max(obtener_inclinaciones(lista_arboles,especie))):
            maximo = float(max(obtener_inclinaciones(lista_arboles,especie)))
            especie_max = especie
    par = [especie_max,maximo]
    return par


def especie_promedio_mas_inclinada(lista_arboles):
    lista_especies = list(especies(lista_arboles))
    maximo = 0.0
    for especie in lista_especies:
        promedio = 0.0
        lista_inclinaciones = list(map(float,obtener_inclinaciones(lista_arboles,especie))) #Abajo explico como funciona
        promedio = sum(lista_inclinaciones)/int(len(lista_inclinaciones))
        if maximo <= promedio:
            maximo = promedio
            especie_max = especie
    par = [especie_max,maximo]
    return par

#Explicacion map() : La función map toma una función y un objeto iterable(pueden ser varios) 
# y crea un iterador nuevo usando cada elemento del objeto iterable. Termina cuando el iterable 
# mas corto del objeto termina. Devuelve un objeto tipo map.


#gral_paz = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
#los_andes = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS')
#centenario = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO')

#print(len(gral_paz))
#especies_gral_paz = especies(gral_paz)
#print(especies_gral_paz)

#de_las_vict = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'DE LAS VICTORIAS')
#print(len(de_las_vict))
#especies_de_las_vict = especies(de_las_vict)
#print(especies_de_las_vict)

#comunes_gral_paz = contar_ejemplares(gral_paz).most_common(5)
#comunes_los_andes = contar_ejemplares(los_andes).most_common(5)
#comunes_centenario = contar_ejemplares(centenario).most_common(5)
#print(comunes_gral_paz,'\n',comunes_los_andes,'\n',comunes_centenario)

#incli_gral_paz = especimen_mas_inclinado(gral_paz)
#incli_los_andes = especimen_mas_inclinado(los_andes)
#incli_centenario = especimen_mas_inclinado(centenario)
#print(incli_centenario,'\t',incli_gral_paz,'\t',incli_los_andes)

#prom_incli_gral_paz = especie_promedio_mas_inclinada(gral_paz)
#prom_incli_los_andes = especie_promedio_mas_inclinada(los_andes)
#prom_incli_centenario = especie_promedio_mas_inclinada(centenario)
#print(prom_incli_centenario,'\t',prom_incli_gral_paz,'\t',prom_incli_los_andes)

''' 
Preguntas extras: ¿Qué habría que cambiar para obtener la especie con un ejemplar más 
inclinado de toda la ciudad y no solo de un parque? ¿Podrías dar la latitud y longitud
de ese ejemplar? ¿Y dónde se encuentra (lat,lon) el ejemplar más alto? ¿De qué especie 
es? 

Para obtener la especie con el ejemplar mas inclinado de toda la ciudad, habría que, o 
bien iterar sobre cada uno de los parques (para se podría generar un iterable con el 
nombre de cada parque, preferentemente lista o tupla y recorrerlo) y llamar en cada 
parque la función especimen_mas_inclinado() o generar una nueva función que tome el 
archivo de la ciudad y extraiga los datos correspondientes.
'''

def especie_mas_inclinada_ciudad(nombre_archivo):
    datos_mas_inclinada = {}
    claves = ['nombre_com','inclinacion','latitud','longitud','ubicacion']
    valores = [0,0,0,0,0]
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        arboles = csv.reader(f)
        encabezados = next(arboles)
        inclinacion = 0.0
        longitud = 0.0
        latitud = 0.0
        nombre_comun = ''
        for arbol in arboles:
            linea = dict(zip(encabezados,arbol))
            if inclinacion < float(linea['inclinacio']) :
                inclinacion = float(linea['inclinacio'])
                longitud = float(linea['long'])
                latitud = float(linea['lat'])
                nombre_comun = linea['nombre_com']
            valores = [nombre_comun,inclinacion,latitud,longitud,(latitud,longitud)]
    datos_mas_inclinada = dict(zip(claves,valores))
    return datos_mas_inclinada

#test = especie_mas_inclinada_ciudad('../Data/arbolado-en-espacios-verdes.csv')
#print(test)