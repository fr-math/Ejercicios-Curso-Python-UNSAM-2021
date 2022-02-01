#!/usr/bin/env python3
# camion.py
# Ejercicio 10.14

class Camion:

    def __init__(self, lotes):
        self.lotes = lotes

    def __iter__(self):
        return self.lotes.__iter__()

    def __len__(self):
        return self.lotes.__len__()

    def __getitem__(self,i):
        return self.lotes.__getitem__(i)
    
    def __repr__(self):
        return f'Camion({self.lotes})'

    def __str__(self):
        cadena_titulo = f'Camion con {self.lotes.__len__()} lotes:\n'
        cadena_lotes = '\n'.join(lote.__str__() for lote in self.lotes)
        return cadena_titulo + cadena_lotes
    
    def __contains__(self, nombre):
        return any(lote.nombre == nombre for lote in self.lotes)

    def precio_total(self):
        return sum(l.costo() for l in self.lotes)

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total