# figuritas.py 
# Ejercicio 5.11

import numpy as np
import random

### FIGURITAS

def album_incompleto(A):
    incompleto = True
    if int(A.min()) != 0:
        incompleto = False
    return incompleto