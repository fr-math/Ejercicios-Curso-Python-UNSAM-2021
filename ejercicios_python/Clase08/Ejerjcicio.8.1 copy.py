import datetime

fecha_hora = datetime.datetime.now()
print(fecha_hora)

fecha = datetime.date.today()
print(fecha)

print(dir(datetime))

d = datetime.date(2019, 4, 13)
print(d)

timestamp = datetime.date.fromtimestamp(1326244364)
print('Fecha =', timestamp)

hoy = datetime.date.today()

print('Año actual:', hoy.year)
print('Mes actual:', hoy.month)
print('Día actual:', hoy.day)
print('Día de la semana:', hoy.weekday())

# datetime(year, month, day, hour, minute, second, microsecond)
b = datetime(2021, 4, 21, 6, 53, 31, 342260)
print(b)
#Los primeros tres argumentos, year, month y day del constructor datetime() 
# son obligatorios. Los otros tienen a 0 como valor por omisión.

from datetime import datetime

a = datetime(2021, 4, 21, 6, 53, 31, 342260)
print('año =', a.year)
print('mes =', a.month)
print('día =', a.day)
print('hora =', a.hour)
print('minuto =', a.minute)
print('timestamp =', a.timestamp())

print(dir(datetime))