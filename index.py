import pdfplumber
import pandas as pd
import io  # Añade esta línea al inicio de tu archivo

def convertir_pdf_a_excel(pdf_path, excel_path):
    # Lista para almacenar los datos de las tablas
    data = []

    # Abrir el archivo PDF
    with pdfplumber.open(pdf_path) as pdf:
        # Iterar sobre cada página del PDF
        for page in pdf.pages:
            # Extraer texto de la página
            text = page.extract_text()
            # Convertir texto a DataFrame de Pandas
            df = pd.read_csv(io.StringIO(text), delimiter="\t", header=None)
            # Agregar el DataFrame a la lista de datos
            data.append(df)

    # Combinar todas las tablas en un solo DataFrame
    df_combined = pd.concat(data)

    # Guardar el DataFrame como un archivo Excel
    df_combined.to_excel(excel_path, index=False)

# Ruta al archivo PDF de entrada
pdf_input_path = 'C:\Repositorio\pruebas\python-pdf-export-excel\C_CATALOGO.PDF'

# Ruta al archivo Excel de salida
excel_output_path = 'output.xlsx'

# Convertir el PDF a Excel
convertir_pdf_a_excel(pdf_input_path, excel_output_path)

print("¡La conversión de PDF a Excel se ha completado con éxito!")
