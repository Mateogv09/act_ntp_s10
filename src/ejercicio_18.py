import pandas as pd, numpy as np
from datetime import datetime, timedelta

data = {...}
df = pd.DataFrame(data)

def ejercicio_18():
    idx=list(df[df['edad']>40].index[:5])
    print("Idx dinámicos:",idx)
    print("\nPercentil>75 salario:\n", df[df['salario']>df['salario'].quantile(0.75)])

if __name__=="__main__": ejercicio_18()
