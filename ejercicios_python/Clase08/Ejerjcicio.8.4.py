#!/usr/bin/env python3
# Ejercicio 8.4


import datetime


def dias_habiles(inicio, fin, feriados):
    '''Recibe una fecha de inicio y una fecha de fin, ambos str con formato 
    dd/mm/AAAA y una lista de feriados. Devuelve una lista con las fechas de 
    los días habiles entre la fecha de inicio y fin inclusive, en formato str.
    '''

    date_inicio = datetime.datetime.strptime(inicio, '%d/%m/%Y')
    date_fin = datetime.datetime.strptime(fin, '%d/%m/%Y')
    if date_fin < date_inicio:
        raise RuntimeError(f'La fecha de inicio es posterior a la fecha de finalización.')
    try:
        fecha = date_inicio
        habiles = []
        while fecha <= date_fin:
            if (fecha.weekday() < 4 and fecha not in feriados):
                habiles.append(fecha.strftime('%d/%m/%Y'))
            fecha += datetime.timedelta(days=1)
    except RuntimeError as e:
        print(e)
    return habiles


if __name__ == '__main__':
    feriados = ['12/10/2020', '23/11/2020', '7/12/2020', '8/12/2020', '25/12/2020']
    inicio = '20/09/2020'
    fin = '10/10/2020'
    habiles = dias_habiles(inicio,fin,feriados)
    print(habiles)

