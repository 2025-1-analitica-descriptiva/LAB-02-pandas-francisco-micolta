import pandas as pd
import os

def pregunta_10():
    """
    Construya una tabla que contenga `c1` y una lista separada por ':' de los
    valores de la columna `c2` para el archivo `tbl0.tsv`.

    Rta/
                              c2
    c1
    A              1:1:2:3:6:7:8:9
    B                1:3:4:5:6:8:9
    C                    0:5:6:7:9
    D                  1:2:3:5:5:7
    E    1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """
    # Define la ruta al archivo tbl0.tsv
    file_path = os.path.join(os.path.dirname(__file__), "..", "files", "input", "tbl0.tsv")
    
    # Carga el archivo TSV en un DataFrame de pandas
    df = pd.read_csv(file_path, sep='\t')

    # Agrupamos por 'c1'. Para cada grupo, tomamos los valores de 'c2',
    # los ordenamos, los convertimos a string y los unimos con ':'.
    # El resultado de esto es una Pandas Series.
    result_series = df.groupby('c1')['c2'].apply(lambda x: ':'.join(map(str, sorted(x))))

    # Ordena el índice (c1) para asegurar la misma salida que en el ejemplo.
    result_series = result_series.sort_index()

    # --- CAMBIOS CLAVE AQUÍ ---
    # 1. Convierte la Serie a un DataFrame.
    #    La columna de valores se llamará 'c2' por defecto si el nombre de la serie es 'c2'.
    result_df = result_series.to_frame()

    # 2. Renombra el índice para que coincida con lo que el test espera.
    result_df.index.name = '_c1' # El test espera que el índice se llame '_c1'

    return result_df