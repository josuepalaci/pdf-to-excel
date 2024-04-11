import pandas as pd

# Leer el archivo Excel de entrada
df = pd.read_excel(r'C:\Repositorio\pruebas\python-pdf-export-excel\output.xlsx')

# Definir la expresión regular para extraer los datos
regex = r'(?P<CODIGO>\d+)\s(?P<NOMBRE_DE_CUENTA>.+?)\s(?P<TIPO_DE_CUENTA>ACTIVO|PASIVO|PATRIMONIO|COSTOS|INGRESOS|LIQUIDACION|ORDEN \(SALDO ACREEDOR\)|ORDEN \(SALDO DEUDOR\))\s(?P<MOVIMIENTO>SI|NO)\s(?P<NIVEL>[0-6])'

# Aplicar la expresión regular para extraer los datos en nuevas columnas
df = df['CODIGO NOMBRE DE CUENTA TIPO DE CUENTA MOVIMIENTO NIVEL'].str.extract(regex)

# Guardar el DataFrame como un nuevo archivo Excel
df.to_excel(r'C:\Repositorio\pruebas\python-pdf-export-excel\separandoCol.xlsx', index=False)

print("¡La conversión de Excel a Excel se ha completado con éxito!")