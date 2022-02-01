# taductor_geringoso.py
# Ejercicio 2.14

def traductor_geringoso(palabra):
    '''Toma una palabra en formato string y devuelve su traducción al geringoso, tambien en formato string'''
    traducida = ''
    for c in palabra:
        traducida += c
        if c in 'aeiou':
            traducida += 'p' + c
        if c in 'AEIOU':
            traducida += 'P' + c
    return traducida 
            

def diccionario_geringoso(list_palabras):
    diccionario = dict()
    for palabra in list_palabras:
        diccionario[palabra] = traductor_geringoso(palabra)
    return diccionario

# Estamos usando la versión beta del traductor, que no tiene en cuenta diptongos/triptongos.

