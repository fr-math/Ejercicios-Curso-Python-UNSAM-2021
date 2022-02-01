#!/usr/bin/env python3
# canguros_buenos.py
# Ejercicio 9.11

#Mi Clase
class Canguro():
    '''Representa a un canguro con el contenido de su marsupio.'''
    def __init__(self,nombre,contenido_mar=None):
        self.nombre = nombre
        if not contenido_mar:
            self.contenido_marsupio = []
        else:
            self.contenido_marsupio = contenido_mar
    
    def meter_en_marsupio(self,objeto):
        '''Agrega un objeto al marsupio.'''
        self.contenido_marsupio.append(objeto)
    
    def __str__(self):
        '''Genera una cadena con el nombre del canguro y el contenido de su 
        marsupio.'''
        cadena = [self.nombre + ', y su contenido del marsupio es:']
        if len(self.contenido_marsupio) != 0:
            for obj in self.contenido_marsupio:
                str_obj = '   - ' + object.__str__(obj)
                cadena.append(str_obj)
        return '\n'.join(cadena)



# canguro_malo.py
"""Este código continene un 
bug importante y dificil de ver
"""
'''
class Canguro:
    """Un Canguro es un marsupial."""

    def __init__(self, nombre, contenido=None):

        # El error estaba acá, porque como argumento de init se recibía una 
        # lista vacía "contenido" si no se especificaba explicitamente. 
        # El tema es que los valores por omisión de la función se calculan 
        # en su definición y no cuando se las llama. Por esto, no es 
        # recomendable tener objetos mutables en los argumentos, porque 
        # al definir la función, se referencia al objeto mutable y luego, 
        # cuando se usa la función, se referencia a ese objeto (si se 
        # cumplen las condiciones) y se trabaja sobre ese objeto, en caso de 
        # ser mutable. Espero se entienda, estoy redactando realmente mal. 
        # La idea es que como la lista vacía es mutable, y los argumentos 
        # opcionales por omision de la función se definen al definir la 
        # funcion y no al llamarla, se va a referenciar siempre al mismo 
        # objeto que es el que se crea al definir la función, Si es mutable. 
        # Si no es mutable, esto no sucede. Por eso el None.
        
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        if not self.contenido marsupio:
            self.contenido marsupio = []
        else:
            self.contenido_marsupio = contenido

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)

#%%
madre_canguro = Canguro('Madre')
cangurito = Canguro('gurito')
madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio('llaves del auto')
madre_canguro.meter_en_marsupio(cangurito)

print(madre_canguro)

# Al ejecutar este código todo parece funcionar correctamente.
# Para ver el problema, imprimí el contenido de cangurito.

print(cangurito)
'''