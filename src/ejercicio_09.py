import pandas as pd, numpy as np
from datetime import datetime, timedelta

data = {...}
df = pd.DataFrame(data).set_index('empleado_id')

def ejercicio_09():
    f1=df.loc[(df['activo'])&(df['departamento'].isin(['IT','Finanzas']))&(df['salario']>60000)&(df['edad']<45)]
    f2=df.loc[(df['ciudad'].isin(['Bogotá','Medellín']))&(df['experiencia_años']>10)]
    print("Filtro1:\n",f1.describe())
    print("\nFiltro2:\n",f2.describe())

if __name__=="__main__": ejercicio_09()
