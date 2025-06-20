import pandas as pd
import os

def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """
    # Define the file path. Based on our previous conversation,
    # the files are located in 'files/input/' relative to the project root.
    file_path = os.path.join(os.path.dirname(__file__), "..", "files", "input", "tbl0.tsv")
    
    # Load the tsv file into a pandas DataFrame
    df = pd.read_csv(file_path, sep='\t')

    # Get the number of columns using .shape[1]
    num_columns = df.shape[1]

    return num_columns
