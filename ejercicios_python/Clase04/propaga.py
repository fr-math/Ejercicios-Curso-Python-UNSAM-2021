# Ejercicio 4.6

def propagar(vector):
    propagado = []
    flag = False                                #Esta es una bandera, que me dice cuando anteriormente se recorrió
    index = 0                                   #un 1 (True) o un -1 (False). Me indica cuando tengo que propagar y 
    while index < len(vector):                  #cuando no. Este while me recorre la lista al derecho.
        propagado.append(0)
        if vector[index] == 1:
            flag = True
            propagado[index] = 1
        if (vector[index] == 0) and flag:
            propagado[index] = 1
        if vector[index] == -1:
            flag = False
            propagado[index] = -1
        index += 1
    index -= 1                                  #Para que no haya IndexErrors, acomodo el índice para recorrer la lista 
    flag = False                                #en sentido inverso.
    while index >= 0:                           #Este while me recorre la lista en sentido inverso (al revés).
        if vector[index] == 1:
            flag = True
            propagado[index] = 1
        if (vector[index] == 0) and flag:
            propagado[index] = 1
        if vector[index] == -1:
            flag = False
        index -= 1
    return propagado

if __name__ == '__main__':
    print(propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]))
    print(propagar([ 0, 0, 0, 1, 0, 0]))