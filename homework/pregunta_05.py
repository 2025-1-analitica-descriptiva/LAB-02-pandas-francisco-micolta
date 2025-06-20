import pandas as pd
import os

def pregunta_05():
    """
    Calcule el valor máximo de `c2` por cada letra en la columna `c1` del
    archivo `tbl0.tsv`.

    Rta/
    c1
    A    9
    B    9
    C    9
    D    7
    E    9
    Name: c2, dtype: int64
    """
    # Define la ruta al archivo tbl0.tsv.
    file_path = os.path.join(os.path.dirname(__file__), "..", "files", "input", "tbl0.tsv")
    
    # Carga el archivo TSV en un DataFrame de pandas.
    df = pd.read_csv(file_path, sep='\t')

    # Agrupa por la columna 'c1' y calcula el valor máximo de 'c2' para cada grupo.
    # Luego, ordena el resultado por el índice (las letras de c1) para coincidir con la Rta/.
    max_c2_por_c1 = df.groupby('c1')['c2'].max().sort_index()

    return max_c2_por_c1
