import pandas as pd, numpy as np
from datetime import datetime, timedelta

data = {...}
df = pd.DataFrame(data).set_index('empleado_id')

def clasificar(s):
    if s<50000: return "Bajo"
    elif s<90000: return "Medio"
    else: return "Alto"

def ejercicio_08():
    df['categoria']=df['salario'].apply(clasificar)
    print("Salario >promedio:\n", df.loc[df['salario']>df['salario'].mean()])
    print("\nSalario >=p75:\n", df.loc[df['salario']>=df['salario'].quantile(0.75)])
    print("\nDistribución:\n", df['categoria'].value_counts())

if __name__=="__main__": ejercicio_08()
