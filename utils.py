'''
   - el archivo utils.py contendrá las siguientes funciones:
	    * row_id_validator (document): validará que todos los datos en la columna ID de fila (A) sean enteros.
	    * email_validator(document): validará que todos los datos en la columna de correo electrónico (G) sean un correo electrónico válido.
	    * sales_validator(document): validará que todos los datos en la columna de ventas sean un decimal válido.
     Todas las funciones recibirán el objeto pandas y devolverán una lista de dictados con las coordenadas y el valor de la celda incorrecta, ejemplo
    [{row: 1, column: 2, value: "wrong_val"},...]
'''

import pandas as pd

def row_id_validator(document):
    df = pd.read_excel(document)
    #df['row_id']
    l_errores = []
    for x, dato in enumerate(df['row_id']):
        #print(x, dato)
        if type(dato) == int:
            continue
        else:
            l_errores.append({'row': x, 'colum': 1, 'value': dato})
    return l_errores

def email_validator(document):
    df = pd.read_excel(document)
    l_errores = []
    for x, dato in enumerate(df['email']):
        #print(f'{x} {dato} {type(dato)}')
        if type(dato) != str:
            l_errores.append({'row': x, 'colum': 7, 'value': dato})
        else:
            if '@' in dato:
                continue
            else:
                l_errores.append({'row': x, 'colum': 7, 'value': dato})

    return l_errores

def sales_validator(document):
    df = pd.read_excel(document)
    #df['row_id']
    l_errores = []
    for x, dato in enumerate(df['sales']):
        if type(dato) == float:
            continue
        else:
            l_errores.append({'row': x, 'colum': 19, 'value': dato})
    return l_errores



