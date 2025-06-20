import pandas as pd
import os

def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna `c1` del
    archivo `tbl0.tsv`?

    Rta/
    c1
    A    8
    B    7
    C    5
    D    6
    E    14
    Name: count, dtype: int64

    """
    # Define the file path.
    file_path = os.path.join(os.path.dirname(__file__), "..", "files", "input", "tbl0.tsv")
    
    # Load the tsv file into a pandas DataFrame
    df = pd.read_csv(file_path, sep='\t')

    # Get the value counts for column 'c1'
    # .value_counts() automatically counts the unique occurrences in a Series.
    counts = df['c1'].value_counts()

    # Sort the results by index (the letters A, B, C...) to match the Rta/ example
    counts = counts.sort_index()

    return counts
