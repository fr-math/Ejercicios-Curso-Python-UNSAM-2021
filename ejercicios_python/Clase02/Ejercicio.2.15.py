import os

precios = {}  # Empezamos con un diccionario vacío

with open('C:\\Users\\admin\\Downloads\\Comahue\\Curso Python UNSaM\\ejercicios_python\\Data\\camion.csv', 'rt', encoding='utf8') as f:
    next(f)
    for line in f:
        row = line.split(',')
        precios[row[0]] = float(row[1])