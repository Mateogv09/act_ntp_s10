import pandas as pd, numpy as np
from datetime import datetime, timedelta

data = {...}
df = pd.DataFrame(data)

def ejercicio_20():
    print("Aleatorias:\n", df.sample(10).describe())
    print("\nSistemáticas:\n", df.iloc[::10].describe())
    print("\nComparación depto:\n", df.groupby('departamento')['salario'].mean())

if __name__=="__main__": ejercicio_20()
