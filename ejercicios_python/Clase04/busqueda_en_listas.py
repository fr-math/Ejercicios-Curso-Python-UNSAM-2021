# Ejercicio 4.3


def buscar_u_elemento(lista,elemento):
    f_index = len(lista) - 1
    while f_index >= 0 and lista[f_index] != elemento:
        f_index -= 1
    return f_index

def buscar_n_elemento(lista,elemento):
    index = 0
    contador = 0
    while index < len(lista):
        if lista[index] == elemento:
            contador += 1
        index += 1
    return contador


# Ejercicio 4.4

def maximo(lista):
    primer_elemento = True
    for elemento in lista: 
        if primer_elemento:
            max = elemento
            primer_elemento = False
        if max <= elemento:
            max = elemento
    return max

def minimo(lista):
    primer_elemento = True
    for elemento in lista: 
        if primer_elemento:
            max = elemento
            primer_elemento = False
        if max >= elemento:
            max = elemento
    return max



if __name__ == '__main__':
    print('Test : buscar_u_elemento()\n')
    print(buscar_u_elemento([1,2,3,2,3,4],1))
    print(buscar_u_elemento([1,2,3,2,3,4],2))
    print(buscar_u_elemento([1,2,3,2,3,4],3))
    print(buscar_u_elemento([1,2,3,2,3,4],5))
    print('Test : buscar_n_elemento()\n')
    print(buscar_n_elemento([1,2,3,2,3,4],1))
    print(buscar_n_elemento([1,2,3,2,3,4],2))
    print(buscar_n_elemento([1,2,3,2,3,4],3))
    print(buscar_n_elemento([1,2,3,2,3,4],5))

    print('Test : maximo()\n')
    print(maximo(([1,2,7,2,3,4])))
    print(maximo(([1,2,3,4])))
    print(maximo(([-5,4])))
    print(maximo(([-5,-4]))) 
    print('Test : minimo()\n')
    print(minimo(([1,2,7,2,3,4])))
    print(minimo(([1,2,3,4])))
    print(minimo(([-5,4])))
    print(minimo(([-5,-4]))) 