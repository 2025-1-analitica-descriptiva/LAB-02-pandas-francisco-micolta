import pandas as pd
import os

def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    # Define la ruta al archivo tbl1.csv.
    # Ten en cuenta que la pregunta menciona 'tbl1.csv' pero tus datos son 'tbl1.tsv'.
    # Asumiré que es un error en la pregunta y que el archivo real es 'tbl1.tsv'.
    file_path = os.path.join(os.path.dirname(__file__), "..", "files", "input", "tbl1.tsv")
    
    # Carga el archivo TSV en un DataFrame de pandas.
    df = pd.read_csv(file_path, sep='\t') # Usamos sep='\t' porque los archivos son TSV

    # Obtiene los valores únicos de la columna 'c4', los convierte a mayúsculas
    # y luego los ordena alfabéticamente antes de convertirlos a una lista.
    unique_c4_values = sorted(df['c4'].str.upper().unique())

    return unique_c4_values
