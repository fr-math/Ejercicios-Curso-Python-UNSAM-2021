#!/usr/bin/env python3
# lote.py
# Ejercicio 9.1

import numpy as np


class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def dist_origen(self):
        return np.sqrt(self.x**2 + self.y**2)
    
    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'Punto({self.x}, {self.y})'

    def __add__(self, b):
      return Punto(self.x + b.x, self.y + b.y)


class Rectangulo(Punto):
    def __init__(self,punto1,punto2):
        self.punto1 = punto1
        self.punto2 = punto2
        self.x1 = punto1.x
        self.y1 = punto1.y
        self.x2 = punto2.x
        self.y2 = punto2.y

    def base(self):
        return abs(self.x2 - self.x1)
    
    def altura(self):
        return abs(self.y2 - self.y1)
    
    def area(self):
        return self.base() * self.altura()

    def desplazar(self,desplazamiento):
        self.punto1.mover(desplazamiento.x,desplazamiento.y)
        self.punto2.mover(desplazamiento.x,desplazamiento.y)
        return Rectangulo(self.punto1, self.punto2)
    
    def rotar(self):
        if self.punto2.x < self.punto1.x:
            if self.punto2.y < self.punto1.y:
                aux = self.punto1 
                self.punto1 = self.punto2
                self.punto2 = aux
            else:
                aux = self.punto1 
                self.punto1.x = self.punto2.x
                self.punto2.x = aux.x
        else:
            if self.punto2.y < self.punto1.y:
                aux = self.punto1 
                self.punto1.y = self.punto2.y
                self.punto2.y = aux.y
        self.punto1.x = self.punto2.x
        self.punto2.mover(self.altura(),-self.base()+self.altura())
        return Rectangulo(self.punto1, self.punto2)

    def __str__(self):
        return f'({self.punto1},{self.punto2})'

    def __repr__(self):
        return f'Rectangulo({self.punto1},{self.punto2})'