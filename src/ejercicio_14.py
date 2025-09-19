import pandas as pd, numpy as np
from datetime import datetime, timedelta

data = {...}
df = pd.DataFrame(data)

def ejercicio_14():
    print("Primeras3col:\n", df.iloc[:,:3])
    print("\nCols[1,4]:\n", df.iloc[:,[1,4]])
    print("\nÚltima col:\n", df.iloc[:,-1])
    print("\nFila5,cols2-4:\n", df.iloc[5,1:4])

if __name__=="__main__": ejercicio_14()
