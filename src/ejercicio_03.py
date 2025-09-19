import pandas as pd, numpy as np
from datetime import datetime, timedelta

data = {...}
df = pd.DataFrame(data).set_index('empleado_id')

def ejercicio_03():
    print("IT con salario>70000:\n", df.loc[(df['departamento']=='IT')&(df['salario']>70000)])
    print("\nVentas o Marketing:\n", df.loc[df['departamento'].isin(['Ventas','Marketing'])])
    print("\nActivos con >5 años exp:\n", df.loc[(df['activo'])&(df['experiencia_años']>5)])

if __name__=="__main__": ejercicio_03()
