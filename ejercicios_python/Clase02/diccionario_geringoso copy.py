# Ejercicio 2.14

def traductor_geringoso(palabra):
    traducida = ''
    for c in palabra:
        traducida += c
        if c in 'aeiou':
            traducida += 'p' + c
        if c in 'AEIOU':
            traducida += 'P' + c
    return traducida 
            

def dic_gering(l_palabras):
    diccionario = dict()
    for palabra in l_palabras:
        diccionario[palabra] = traductor_geringoso(palabra)
    return diccionario

# Estamos usando la versión beta del traductor, que no tiene en cuenta diptongos/triptongos.
# No se valida la entrada en l_palabras. El ingreso por teclado se realiza a través de strings 
# por lo que si la implementación de la función 'dic_gering()' es mediante la función 'input()' 
# esto no debería traer apareados problemas de validación (a secas, sin castear).

