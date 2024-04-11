import pandas as pd

# Leer el archivo Excel de entrada
df = pd.read_excel(r'C:\Repositorio\pruebas\python-pdf-export-excel\adelimitar.xlsx')

# Reorganizar los datos en nuevas columnas
df['CODIGO'] = df['CODIGO NOMBRE DE CUENTA TIPO DE CUENTA MOVIMIENTO NIVEL'].str.split(' ').str[0]
df['NOMBRE DE CUENTA'] = df['CODIGO NOMBRE DE CUENTA TIPO DE CUENTA MOVIMIENTO NIVEL'].str.split(' ').str[1]
df['TIPO DE CUENTA'] = df['CODIGO NOMBRE DE CUENTA TIPO DE CUENTA MOVIMIENTO NIVEL'].str.split(' ').str[2]
df['MOVIMIENTO'] = df['CODIGO NOMBRE DE CUENTA TIPO DE CUENTA MOVIMIENTO NIVEL'].str.split(' ').str[3]
df['NIVEL'] = df['CODIGO NOMBRE DE CUENTA TIPO DE CUENTA MOVIMIENTO NIVEL'].str.split(' ').str[4]

# Eliminar la columna original
df = df.drop(columns=['CODIGO NOMBRE DE CUENTA TIPO DE CUENTA MOVIMIENTO NIVEL'])

# Guardar el DataFrame como un nuevo archivo Excel
df.to_excel(r'C:\Repositorio\pruebas\python-pdf-export-excel\delimitando.xlsx', index=False)

print("¡La conversión de Excel a Excel se ha completado con éxito!")