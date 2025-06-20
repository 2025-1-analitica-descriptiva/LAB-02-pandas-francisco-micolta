import pandas as pd
import os

def pregunta_07():
    """
    Calcule la suma de la `c2` por cada letra de la `c1` del archivo
    `tbl0.tsv`.

    Rta/
    c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: c2, dtype: int64
    """
    # Define la ruta al archivo tbl0.tsv.
    file_path = os.path.join(os.path.dirname(__file__), "..", "files", "input", "tbl0.tsv")
    
    # Carga el archivo TSV en un DataFrame de pandas.
    df = pd.read_csv(file_path, sep='\t')

    # Agrupa por la columna 'c1' y calcula la suma de 'c2' para cada grupo.
    # Luego, ordena el resultado por el índice (las letras de c1) para coincidir con la Rta/.
    sum_c2_by_c1 = df.groupby('c1')['c2'].sum().sort_index()

    return sum_c2_by_c1
