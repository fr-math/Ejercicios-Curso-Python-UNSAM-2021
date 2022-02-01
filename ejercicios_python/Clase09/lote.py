#!/usr/bin/env python3
# lote.py
# Ejercicio 9.9

class Lote:
    def __init__(self,nombre,cajones,precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
    
    def costo(self):
        '''Devuelve el costo de un lote.'''
        return self.cajones * self.precio
    
    def vender(self,cantidad):
        '''Vende una cantidad de cajones.'''
        self.cajones -= cantidad

    def __repr__(self):
        return f"Lote('{self.nombre}', {self.cajones}, {self.precio})"
    
    def __str__(self):
        return f"('{self.nombre}', {self.cajones}, {self.precio})"