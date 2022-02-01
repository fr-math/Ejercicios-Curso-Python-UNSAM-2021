# inclusive.py
# Ejercicio 1.22


frase = 'todos somos programadores'
palabras = frase.split()
nuevas_palabras = []
frase_t = ''
for palabra in palabras:
    if (palabra[-1] == 'o'):
        nueva_palabra = palabra[:-1] + 'e'
    elif len(palabra)>1 and (palabra[-2] == 'o'):
        nueva_palabra = palabra[:-2] + 'e' + palabra[-1]
    else:
        nueva_palabra = palabra
    nuevas_palabras.append(nueva_palabra)
frase_t = ' '.join(nuevas_palabras)
print(frase_t)