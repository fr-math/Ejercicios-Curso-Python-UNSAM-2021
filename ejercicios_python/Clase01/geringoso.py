# Ejercicio 1.18
'''
cadena = input('Ingrese la palabra o frase que desea traducir al geringoso (versión beta):\t')
capadepenapa = ''
for c in cadena:
    capadepenapa += c
    if (c=='a'):
        capadepenapa += 'pa'
    elif(c=='e'):
        capadepenapa += 'pe'
    elif(c=='i'):
        capadepenapa += 'pi'
    elif(c=='o'):
        capadepenapa += 'po'
    elif(c=='u'):
        capadepenapa += 'pu'
    elif(c=='A'):
        capadepenapa += 'pa'
    elif(c=='E'):
        capadepenapa += 'pe'
    elif(c=='I'):
        capadepenapa += 'pi'
    elif(c=='O'):
        capadepenapa += 'po'
    elif(c=='U'):
        capadepenapa += 'pu'

print(cadena,'\t',capadepenapa)
'''

# La versión beta no tiene en cuenta diptongos / triptongos

#v2.

cadena = input('Ingrese la palabra o frase que desea traducir al geringoso (versión beta):\t')
capadepenapa = ''
for c in cadena:
    capadepenapa += c
    if c in 'aeiou':
        capadepenapa += 'p' + c
    if c in 'AEIOU':
        capadepenapa += 'P' + c
print(capadepenapa)