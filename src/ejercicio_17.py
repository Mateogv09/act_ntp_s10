import pandas as pd, numpy as np
from datetime import datetime, timedelta

data = {...}
df = pd.DataFrame(data)

def ejercicio_17():
    subset=df.iloc[:10,:4]
    mask=[True,False]*50
    print("Subset:\n", subset)
    print("\nBooleanos:\n", df.iloc[mask,:2])
    print("\nMedia subset:\n", subset.mean())

if __name__=="__main__": ejercicio_17()
