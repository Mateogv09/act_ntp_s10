import pandas as pd, numpy as np
from datetime import datetime, timedelta

data = {...}
df = pd.DataFrame(data)

def ejercicio_16():
    print("Cada2da:\n", df.iloc[::2])
    print("\nInverso:\n", df.iloc[::-1])
    print("\nCada5ta desde3:\n", df.iloc[2::5])
    print("\nComb paso:\n", df.iloc[::4,::3])

if __name__=="__main__": ejercicio_16()
