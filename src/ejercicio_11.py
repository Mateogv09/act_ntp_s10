import pandas as pd, numpy as np
from datetime import datetime, timedelta

data = {...}
df = pd.DataFrame(data)

def ejercicio_11():
    print("Primera fila:\n", df.iloc[0])
    print("\nPrimeras5:\n", df.iloc[:5])
    print("\nÚltima:\n", df.iloc[-1])
    print("\nEspecíficas:\n", df.iloc[[2,10,50]])

if __name__=="__main__": ejercicio_11()
