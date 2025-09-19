import pandas as pd, numpy as np
from datetime import datetime, timedelta

data = {...}
df = pd.DataFrame(data)

def ejercicio_12():
    print("10–20:\n", df.iloc[9:20])
    print("\nÚltimas10:\n", df.iloc[-10:])
    print("\nFilas pares:\n", df.iloc[::2])
    print("\nCada tercera:\n", df.iloc[::3])

if __name__=="__main__": ejercicio_12()
