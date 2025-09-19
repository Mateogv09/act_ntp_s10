import pandas as pd, numpy as np
from datetime import datetime, timedelta

data = {...}
df = pd.DataFrame(data).set_index('empleado_id')

def ejercicio_05():
    df.loc[df['departamento']=='IT','salario']*=1.1
    df.loc[df['edad']>60,'activo']=False
    df.loc[df['departamento']=='RRHH','ciudad']='Bogotá'
    print(df.head(10))

if __name__=="__main__": ejercicio_05()
