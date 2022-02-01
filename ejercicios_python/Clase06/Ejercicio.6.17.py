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

if __name__ == '__main__':
    lista = [1, 1, 1, 1, 1]
    print(incrementar(lista))

''' incrementar() : O(n)'''