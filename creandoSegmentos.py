import pandas as pd

# Leer el archivo Excel de entrada
df = pd.read_excel(r'C:\Repositorio\pruebas\python-pdf-export-excel\separandoCol.xlsx')

# Definir una función para dividir el código en segmentos
def split_codigo(codigo):
    # Convertir el código a una cadena y rellenar con espacios hasta tener 7 caracteres
    codigo = str(codigo).ljust(15)
    # Dividir el código en segmentos y unirlos con comas
    segmentos = list(codigo[0]) + list(codigo[1]) + [codigo[i:i+2] for i in range(2, 15, 2)]
    # Convertir cada segmento a una cadena encerrada entre comillas simples
    segmentos = ["'{}'".format(seg) for seg in segmentos]
    return ','.join(segmentos)

# Aplicar la función a la columna 'CODIGO' y crear una nueva columna para los segmentos
df['segmentos'] = df['CODIGO'].apply(split_codigo)  

# Guardar el DataFrame como un nuevo archivo Excel
df.to_excel(r'C:\Repositorio\pruebas\python-pdf-export-excel\creandoSegmentos.xlsx', index=False)

print("¡La conversión de Excel a Excel se ha completado con éxito!")

