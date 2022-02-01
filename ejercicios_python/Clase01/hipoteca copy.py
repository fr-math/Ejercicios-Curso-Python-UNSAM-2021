# hipoteca.py
#
# IMPORTANTE! POR MOTIVOS DE ARCHIVADO Y SOURCE CONTROL, SE DEJARON TODAS LAS VERSIONES
# DE "hipoteca.py" EN EL ARCHIVO COMO COMENTARIOS. SI DESEA EJECUTAR UNA EN PARTICULAR, 
# REHUBIQUE LAS COMILLAS TRIPLES EN EL LUGAR ADECUADO.
#
# Archivo de ejemplo
# Ejercicio de hipoteca

# Ejercicio 1.7
'''
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual

print('Total pagado', round(total_pagado, 2))


# Ejercicio 1.8

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0

while saldo > 0:
    mes += 1
    saldo = saldo * (1+tasa/12) - pago_mensual
    if (mes <= 12):
        saldo -= 1000
        total_pagado = total_pagado + pago_mensual + 1000
    else:
        total_pagado = total_pagado + pago_mensual

print('Total pagado:', round(total_pagado, 2),'(en', mes, 'meses).')


# Ejercicio 1.9

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    mes += 1
    saldo = saldo * (1+tasa/12) - pago_mensual
    if (mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin):
        saldo -= pago_extra
        total_pagado = total_pagado + pago_mensual + pago_extra
    else:
        total_pagado = total_pagado + pago_mensual

print('Total pagado:    ', round(total_pagado, 2), '\nMeses:    ',mes)


# Ejercicio 1.10

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    mes += 1
    if (saldo < pago_mensual):
        total_pagado += saldo
        saldo = 0
        print(mes, round(total_pagado,2), saldo)
        break
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
    if (mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin):
        saldo -= pago_extra
        total_pagado = total_pagado + pago_extra
    print(mes, round(total_pagado, 2), round(saldo, 2))

print('Total pagado:    ', round(total_pagado, 2), '\nMeses:    ',mes)


# Ejercicio 1.11

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    mes += 1
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
    if (mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin):
        saldo -= pago_extra
        total_pagado += pago_extra
    if (saldo * (1+tasa/12) < pago_mensual):
        total_pagado += saldo * (1+tasa/12)
        saldo = 0
        mes += 1    
    print(mes, round(total_pagado, 2), round(saldo, 2))
print('Total pagado:\t', round(total_pagado, 2), '\nMeses:\t\t',mes)


# v.2
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    mes += 1
    if (mes >= pago_extra_mes_comienzo) and (mes <= pago_extra_mes_fin):
        a_pagar = pago_mensual + pago_extra
    else:
        a_pagar = pago_mensual
    if saldo * (1+tasa/12) < a_pagar:
        a_pagar = saldo * (1+tasa/12)
    saldo = saldo * (1+tasa/12) - a_pagar
    total_pagado += a_pagar
    print(mes, round(total_pagado, 2), round(saldo, 2))
print('Total pagado:\t', round(total_pagado, 2), '\nMeses:\t\t',mes)
'''

# Ejercicio 1.20

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000


print('Mes N° \t Total Pagado \t Saldo')
while saldo > 0:
    mes += 1
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
    if (mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin):
        saldo -= pago_extra
        total_pagado += pago_extra
    if (saldo * (1+tasa/12) < pago_mensual):
        total_pagado += saldo * (1+tasa/12)
        saldo = 0
        mes += 1    
    print(f'{mes} \t {round(total_pagado, 2)} \t {round(saldo, 2)}')

print(f'\nTotal pagado: \t {round(total_pagado, 2)}\nMeses: \t\t {mes}')