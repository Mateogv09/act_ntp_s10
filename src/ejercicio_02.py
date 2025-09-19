import pandas as pd, numpy as np
from datetime import datetime, timedelta

data = {...}  # mismo bloque que ejercicio_01
df = pd.DataFrame(data).set_index('empleado_id')

def ejercicio_02():
    print("Mayores de 40:\n", df.loc[df['edad']>40])
    print("\nDepartamento IT:\n", df.loc[df['departamento']=='IT'])
    print("\nSalario >80000:\n", df.loc[df['salario']>80000])

if __name__=="__main__": ejercicio_02()
