import pandas as pd
import os

def pregunta_11():
    """
    Construya una tabla que contenga `c0` y una lista separada por ',' de
    los valores de la columna `c4` del archivo `tbl1.tsv`.

    Rta/
          c0      c4
    0      0   b,f,g
    1      1   a,c,f
    2      2 a,c,e,f
    3      3     a,b
    ...
    37    37 a,c,e,f
    38    38     d,e
    39    39   a,d,f
    """
    # Define la ruta al archivo tbl1.tsv
    file_path = os.path.join(os.path.dirname(__file__), "..", "files", "input", "tbl1.tsv")
    
    # Carga el archivo TSV en un DataFrame de pandas
    df = pd.read_csv(file_path, sep='\t')

    # Para cada c0, agrupa los valores de c4.
    # La columna c4 ya tiene strings como "a,b,c", por lo que necesitamos:
    # 1. Separar esos strings en listas de elementos (usando .str.split(',')).
    # 2. "Explotar" esas listas para tener un elemento por fila (usando .explode()).
    # 3. Agrupar nuevamente por c0.
    # 4. Ordenar los elementos de c4 para cada grupo y unirlos con ','.
    
    # Primero, expandimos las cadenas de 'c4' en filas separadas
    df_exploded = df.assign(c4=df['c4'].str.split(',')).explode('c4')

    # Ahora agrupamos por 'c0', y para cada grupo,
    # ordenamos los elementos de 'c4' y los unimos con una coma.
    result = df_exploded.groupby('c0')['c4'].apply(lambda x: ','.join(sorted(x.unique())))
    
    # Convertimos la Serie resultante a DataFrame.
    # Reset_index() convierte el índice 'c0' en una columna normal.
    result = result.reset_index()

    return result
