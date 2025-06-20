import pandas as pd
import os

def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """
    # Define las rutas a los archivos
    file_path_tbl0 = os.path.join(os.path.dirname(__file__), "..", "files", "input", "tbl0.tsv")
    file_path_tbl2 = os.path.join(os.path.dirname(__file__), "..", "files", "input", "tbl2.tsv")
    
    # Carga los archivos TSV en DataFrames de pandas
    df0 = pd.read_csv(file_path_tbl0, sep='\t')
    df2 = pd.read_csv(file_path_tbl2, sep='\t')

    # Realiza la unión (merge) de los dos DataFrames usando 'c0' como clave.
    # Un 'inner' merge es apropiado aquí, ya que solo nos interesan las filas que existen en ambos.
    merged_df = pd.merge(df0, df2, on='c0', how='inner')

    # Agrupa el DataFrame unido por 'c1' y calcula la suma de 'c5b'.
    # Luego, ordena el resultado por el índice ('c1') para coincidir con la Rta/.
    sum_c5b_by_c1 = merged_df.groupby('c1')['c5b'].sum().sort_index()

    return sum_c5b_by_c1
