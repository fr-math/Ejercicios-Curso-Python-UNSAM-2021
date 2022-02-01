#!/usr/bin/env python3
# lote.py
# Ejercicio 9.1

class Lote:
    def __init__(self,nombre,cajones,precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
    
    def costo(self):
        return self.cajones * self.precio
    
    def vender(self,cantidad):
        self.cajones -= cantidad

    def __repr__(self):
        return f"Lote('{self.nombre}', {self.cajones}, {self.precio})"


'''
class Jugador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.salud = 100

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

    def lastimar(self, pts):
        self.salud -= pts


import fileparse
with open('../Data/camion.csv') as lineas:
    camion_dicts = fileparse.parse_csv(lineas, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
camion = [lote.Lote(d['nombre'],d['cajones'],d['precio']) for d in camion_dicts]
camion
sum([c.costo() for c in camion])
'''