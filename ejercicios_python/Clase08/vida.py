#!/usr/bin/env python3
# vida.py
# Ejercicio 8.1


from datetime import datetime
#import datetime


#def vida_en_segundos(fecha_nac):
#    tiempo_inicial = datetime.datetime.strptime(fecha_nac, '%d/%m/%Y')
#    tiempo_final = datetime.datetime.now()
#    tiempo_vivido = tiempo_final - tiempo_inicial
#    return tiempo_vivido.total_seconds()

def vida_en_segundos(fecha_nac):
    '''Toma una fecha de nacimiento como str con formato dd/mm/AAAA y devuelve
    el tiempo vivido en segundos hasta el momento actual. Se considera que el 
    nacimiento se produjo a las 00:00 hs'''
    return (datetime.now() - 
            datetime.strptime(fecha_nac, '%d/%m/%Y')).total_seconds()


if __name__ == '__main__':
    fecha = input('Ingrese su fecha de nacimiento con el formato dd/mm/AAAA, donde d,m,A son números naturales:\t')
    print(f'Usted ha vivido {vida_en_segundos(fecha)}s en total.')