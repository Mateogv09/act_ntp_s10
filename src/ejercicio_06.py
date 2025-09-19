import pandas as pd, numpy as np
from datetime import datetime, timedelta

data = {...}
df = pd.DataFrame(data).set_index('empleado_id')

def ejercicio_06():
    print("Nombre contiene '1':\n", df.loc[df['nombre'].str.contains('1')])
    print("\nApellido termina en 5:\n", df.loc[df['apellido'].str.endswith('5')])
    print("\nCiudad empieza con B:\n", df.loc[df['ciudad'].str.startswith('B')])

if __name__=="__main__": ejercicio_06()
