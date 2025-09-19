import pandas as pd, numpy as np
from datetime import datetime, timedelta

data = {...}
df = pd.DataFrame(data).set_index('empleado_id')

def ejercicio_10():
    vistas={'IT':df.loc[df['departamento']=='IT'],'Bogotá':df.loc[df['ciudad']=='Bogotá']}
    print("Métricas por depto:\n", df.groupby('departamento')['salario'].mean())
    print("\nMétricas por ciudad:\n", df.groupby('ciudad')['edad'].mean())
    print("\nTop salarios:\n", df.nlargest(5,'salario'))

if __name__=="__main__": ejercicio_10()
