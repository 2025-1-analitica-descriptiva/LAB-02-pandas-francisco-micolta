import pandas as pd
import os

def pregunta_04():
    """
    Calcule el promedio de `c2` por cada letra de la `c1` del archivo
    `tbl0.tsv`.

    Rta/
    c1
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    Name: c2, dtype: float64
    """
    # Define la ruta al archivo tbl0.tsv.
    file_path = os.path.join(os.path.dirname(__file__), "..", "files", "input", "tbl0.tsv")
    
    # Carga el archivo TSV en un DataFrame de pandas.
    df = pd.read_csv(file_path, sep='\t')

    # Agrupa por la columna 'c1' y calcula el promedio de 'c2' para cada grupo.
    # Luego, ordena el resultado por el índice (las letras de c1) para coincidir con la Rta/.
    promedio_c2_por_c1 = df.groupby('c1')['c2'].mean().sort_index()

    return promedio_c2_por_c1
