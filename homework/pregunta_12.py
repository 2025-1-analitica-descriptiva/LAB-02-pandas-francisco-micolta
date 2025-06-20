import pandas as pd
import os

def pregunta_12():
    """
    Construya una tabla que contenga `c0` y una lista separada por ','
    de los valores de la columna `c5a` y `c5b` (unidos por ':') de la
    tabla `tbl2.tsv`.

    Rta/
          c0                           c5
    0      0  bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1      1            aaa:3,ccc:2,ddd:0,hhh:9
    2      2            ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37    37                    eee:0,fff:2,hhh:6
    38    38                    eee:0,fff:9,iii:2
    39    39                    ggg:3,hhh:8,jjj:5
    """
    # Define la ruta al archivo tbl2.tsv
    file_path = os.path.join(os.path.dirname(__file__), "..", "files", "input", "tbl2.tsv")
    
    # Carga el archivo TSV en un DataFrame de pandas
    df = pd.read_csv(file_path, sep='\t')

    # Combina las columnas 'c5a' y 'c5b' en una nueva columna temporal 'c5_combined'
    # usando ':' como separador. Convertimos c5b a string para la unión.
    df['c5_combined'] = df['c5a'] + ':' + df['c5b'].astype(str)

    # Agrupamos por 'c0'. Para cada grupo:
    # 1. Tomamos los valores de 'c5_combined'.
    # 2. Los ordenamos alfabéticamente.
    # 3. Los unimos en una sola cadena usando ','.
    result = df.groupby('c0')['c5_combined'].apply(lambda x: ','.join(sorted(x)))

    # Convertimos la Serie resultante a un DataFrame y reseteamos el índice.
    result = result.reset_index()

    # Renombramos la columna 'c5_combined' a 'c5' según la Rta/.
    result.rename(columns={'c5_combined': 'c5'}, inplace=True)

    return result
