import pandas as pd, numpy as np
from datetime import datetime, timedelta

data = {...}
df = pd.DataFrame(data)

def ejercicio_19():
    print("Aleatoria:\n", df.sample(5))
    print("\nSistemática cada7:\n", df.iloc[::7])
    print("\nEstratificada depto:\n", df.groupby('departamento').apply(lambda x: x.sample(1)))

if __name__=="__main__": ejercicio_19()
