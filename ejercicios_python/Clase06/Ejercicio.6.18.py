def incrementar(s):
    carry = 1
    l = len(s)

    for i in range(l-1,-1,-1):
        if (s[i] == 1 and carry == 1):
            s[i] = 0
            carry = 1
        else:
            s[i] = s[i] + carry
            carry = 0
    return s

def listar_secuencias(n):
    lista = [0]*n
    lista_sec = [[0]*n]
    #for _ in range(2**n -1):
    while lista != ([1]*n):
        lista_aux = lista.copy()
        lista = incrementar(lista_aux)
        lista_sec.append(lista)
    return lista_sec

# Número de listas de longitud n = 2^n
# Número de listas de longitud n+1 = 2^{n+1}


if __name__ == '__main__':
    lista = listar_secuencias(20)
    #print(lista)
    print(lista[0])
    print(lista[len(lista)-1])
    print(len(lista))
'''
listar_secuencias() es una función exponencial en n de orden O(2^n)
porque su número de operaciones es #P(A) donde #A=n.
(donde # denota cardinal, P(X) es el powerset de X y n es un natural
'''