#!/usr/bin/env python3
# torre_control.py
# Ejercicio 9.12


class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0

class TorreDeControl(Cola):
    '''Representa una torre de control, con dos colas, una de arribos y otra 
    de partidas.'''
    def __init__(self):
        self.arribos = Cola()
        self.partidas = Cola()

    def nuevo_arribo(self,arribo):
        '''Agrega un arribo a la cola de arribos.'''
        self.arribos.encolar(arribo)
    
    def nueva_partida(self,partida):
        '''Agrega una partida a la cola de partidas.'''
        self.partidas.encolar(partida)

    def ver_estado(self):
        '''Muestra el estado actual de la torre de control.'''
        if not self.arribos.esta_vacia():
            s = 'Vuelos esperando para aterrizar: ' + ', '.join(self.arribos.items)
            print(s)
        if not self.partidas.esta_vacia():
            s = 'Vuelos esperando para aterrizar: ' + ', '.join(self.partidas.items)
            print(s)
        if self.arribos.esta_vacia() and self.partidas.esta_vacia():
            print('No hay vuelos en espera.')
        
    def asignar_pista(self):
        '''Asigna pistas a los aviones, considerando prioridad los arribos 
        por sobre las partidas. Si no hay partidas, lo imprime en pantalla. 
        '''
        if not self.arribos.esta_vacia():
            print(f'El vuelo {self.arribos.desencolar()} aterrizó con éxito.')
        elif self.partidas.esta_vacia():
            print('No hay vuelos en espera.')
        else:
            print(f'El vuelo {self.partidas.desencolar()} despegó con éxito.')
            