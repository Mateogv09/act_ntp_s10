import pandas as pd, numpy as np
from datetime import datetime, timedelta

data = {...}
df = pd.DataFrame(data)

def ejercicio_13():
    print("Pos[0,5,10]:\n", df.iloc[[0,5,10]])
    print("\nAleatorias:\n", df.sample(5))
    print("\nStats:\n", df.iloc[[0,5,10]].describe())

if __name__=="__main__": ejercicio_13()
