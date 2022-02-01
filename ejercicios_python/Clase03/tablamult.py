# Ejercicio 3.17

n_rows = 10
n_cols = 10
titulo = f'TABLA DE MULTIPLICAR'
separador = '-'*(n_cols*4 +7)


print(separador)
print(f'|{titulo:^45s}|')               #Las | las pongo a modo de separador horizontal, tipo borde de celda en tabla
print(separador)
print('| x  |',end='')
for i in range(0,10):
    print(f'{i:^4d}',end='')
print('|')
print(separador)
for i in range(0,10):
    row = i
    print(f'|{row:^4d}|',end='')
    column = -i
    for j in range(0,10):
        column += i 
        print(f'{column:^4d}',end='')
    print('|')
print(separador)