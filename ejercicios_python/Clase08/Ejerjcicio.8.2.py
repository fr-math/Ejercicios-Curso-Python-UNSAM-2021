#!/usr/bin/env python3
# Ejercicio 8.2


import datetime


def es_primavera(fecha):
    if (fecha.month > 9 or (fecha.month == 9 and fecha.day >= 21)) and (fecha.month < 12 or (fecha.month == 12 and fecha.day <= 21)):
       primavera = True
    else:
        primavera = False
    return primavera 

def dias_hasta_primavera():
    fecha = datetime.date.today()
    if es_primavera(fecha):
        fecha_prim = fecha
    elif fecha.month == 12 and fecha.day >= 21:
        fecha_prim = datetime.date(fecha.year+1, 9, 21)
    else :
        fecha_prim = datetime.date(fecha.year, 9, 21)
    dias_faltantes = fecha_prim - fecha
    return dias_faltantes.days

def dias_hasta_prox_primavera():
    fecha = datetime.date.today()
    if fecha.month > 9 or (fecha.month == 9 and fecha.day >= 21):
        fecha_prim = datetime.date(fecha.year + 1, 9, 21)
    else :
        fecha_prim = datetime.date(fecha.year, 9, 21)
    dias_faltantes = fecha_prim - fecha
    return dias_faltantes.days



if __name__ == '__main__':
    if dias_hasta_primavera() != 0:
        print(f' Faltan {dias_hasta_primavera()} días hasta la próxima primavera.')
    else:
        print(f' Estamos en primavera!')
    print(f'Faltan {dias_hasta_prox_primavera()} días hasta la próxima primavera.')