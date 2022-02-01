#!/usr/bin/env python3
# Ejercicio 10.8


def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line


if __name__ == '__main__':
    from vigilante import vigilar
    lines = vigilar('../Data/mercadolog.csv')
    naranjas = filematch(lines, 'Naranja')
    for line in naranjas:
            print(line)