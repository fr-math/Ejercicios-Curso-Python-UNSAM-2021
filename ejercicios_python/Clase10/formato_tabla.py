#!/usr/bin/env python3
# formato_tabla.py
# Ejercicio 9.5


class FormatoTabla:
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        raise NotImplementedError()

    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        raise NotImplementedError()

class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()

class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))

class FormatoTablaHTML(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print('<tr>',end='')
        for h in headers:
            print(f'<th>{h}</th>',end='')
        print('</tr>')

    def fila(self, data_fila):
        print('<tr>',end='')
        for d in data_fila:
            print(f'<td>{d}</td>',end='')
        print('</tr>')

def crear_formateador(nombre):
    '''Toma una extensión de archivo en formato str y devuelve una tabla en el
    formato especificado.'''
    if nombre == 'txt':
        formateador = FormatoTablaTXT()
    elif nombre == 'csv':
        formateador = FormatoTablaCSV()
    elif nombre == 'html':
        formateador = FormatoTablaHTML()
    else:
        raise RuntimeError(f'Unknown format {nombre}')
    return formateador

def imprimir_tabla(data_informe, formateador):
    #def imprimir_informe(data_informe, formateador):
    '''
    DocString
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)
