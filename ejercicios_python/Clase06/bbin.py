# bbin.py
# Ejercicio 6.14-5

def donde_insertar(lista, x, verbose=False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    pos = -1 
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d}|{medio:3d}|{der:>3d} ')
        if lista[medio] == x:
            pos = medio    
            break
        else:
            pos = izq 
        if lista[medio] > x:
            der = medio - 1 
        else:               
            izq = medio + 1 
        if medio == 0 and lista[medio] < x:
            pos = 1 
        if medio == len(lista)-1 and lista[medio] < x:
            pos = len(lista)
    return pos

def insertar(lista, x):
    '''Inserta el elemento x en la lista, de manera que la lista resultante se mantenga ordenada.'''
    pos = donde_insertar(lista,x)
    if x not in lista:    
        lista.insert(pos,x)
    return pos

if __name__ == '__main__':
    lista = [0,2,4,6]
    print(insertar(lista,7),'-->',lista)