# Ejercicio 4.5

'''
def invertir_lista(lista):
    invertida = []
    for e in lista[::-1]: 
        invertida.append(e)
    return invertida
'''

def invertir_lista(lista):
    invertida = []
    f_index = len(lista) - 1
    while f_index >= 0 :
        invertida.append(lista[f_index])
        f_index -= 1
    return invertida

if __name__ == '__main__':
    print('Test : invertir_lista()')
    print(invertir_lista([1,2,3,4,5]))
    print(invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))