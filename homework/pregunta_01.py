import pandas as pd
import os # Necesitas importar el módulo os para trabajar con rutas de archivos

def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    # Construimos la ruta al archivo de forma robusta.
    # os.path.dirname(__file__) nos da el directorio donde está este script (homework/).
    # Luego, '..' sube un nivel (a /workspaces/LAB-02-pandas-francisco-micolta/).
    # Después, entramos en 'files' y luego en 'input' para encontrar 'tbl0.tsv'.
    file_path = os.path.join(os.path.dirname(__file__), "..", "files", "input", "tbl0.tsv")
    
    # print(f"Intentando cargar desde: {file_path}") # Línea útil para depurar si falla de nuevo

    df = pd.read_csv(file_path, sep='\t')

    num_rows = df.shape[0]

    return num_rows