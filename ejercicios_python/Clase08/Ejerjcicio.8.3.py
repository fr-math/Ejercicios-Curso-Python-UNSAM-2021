#!/usr/bin/env python3
# Ejercicio 8.3


import datetime


def licencia(fecha,dias):
    dias_lic = datetime.timedelta(dias,0,0)
    fecha_incorporación = fecha + dias_lic
    return fecha_incorporación

def dia_reincorporacion(fin_licencia):
    reincorporacion = fin_licencia
    if fin_licencia.weekday() == 5:
        reincorporacion.day += 2
    elif fin_licencia.weekday() == 6:
        reincorporacion.day += 1
    return reincorporacion



if __name__ == '__main__':
    fecha = datetime.date(2020, 9, 26)
    dias = 200
    fin_licencia = licencia(fecha,dias)
    reincorporacion = dia_reincorporacion(fin_licencia)
    print(f'El dia de reincorporación es {reincorporacion}')
