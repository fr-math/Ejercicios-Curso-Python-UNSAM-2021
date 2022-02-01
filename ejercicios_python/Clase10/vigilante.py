#!/usr/bin/env python3
# vigilante.py
# Ejercicio 10.7


import os
import time


def vigilar(filename):
    f = open(filename)
    f.seek(0, os.SEEK_END)
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.5)
            continue
        else:
            yield line


if __name__ == '__main__':
    import informe_final

    camion = informe_final.leer_camion ('../Data/camion.csv')

    for line in vigilar('../Data/mercadolog.csv'):  
        fields = line.split(',')
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])
        if nombre in camion:    
            print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')