import pandas as pd, numpy as np
from datetime import datetime, timedelta

data = {...}
df = pd.DataFrame(data).set_index('empleado_id')

def ejercicio_07():
    en2022=df.loc[df['fecha_ingreso'].dt.year==2022]
    ult2=df.loc[df['fecha_ingreso']>=datetime.now()-timedelta(days=730)]
    trim1=df.loc[df['fecha_ingreso'].dt.month<=3]
    print("2022:",len(en2022),"Ult2años:",len(ult2),"Trim1:",len(trim1))

if __name__=="__main__": ejercicio_07()
