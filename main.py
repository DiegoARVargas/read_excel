import pandas as pd
from utils import row_id_validator, email_validator, sales_validator

def main():
    document = input('Escribe el nombre del documento excel incluye .xls al final. Ejemplo pruebaexcel.xls: ')
    archivo = pd.read_excel(document)
    print(archivo)
    
    a = row_id_validator(document)
    b = email_validator(document)
    c = sales_validator(document)

    print('*'*100)
    print(a)
    print('*'*100)
    print(b)
    print('*'*100)
    print(c)
    

if __name__ == '__main__':
    main()
