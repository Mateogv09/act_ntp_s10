import pandas as pd, numpy as np
from datetime import datetime, timedelta

data = {...}
df = pd.DataFrame(data)

def ejercicio_15():
    df.iloc[0,2]=99
    df.iloc[1:3,3]=50000
    df.iloc[4:6,[2,3]]=123
    print(df.head(10))

if __name__=="__main__": ejercicio_15()
