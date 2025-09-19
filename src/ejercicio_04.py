import pandas as pd, numpy as np
from datetime import datetime, timedelta

data = {...}
df = pd.DataFrame(data).set_index('empleado_id')

def ejercicio_04():
    print("Nombre y salario:\n", df.loc[:,['nombre','salario']].head(10))
    print("\nRango nombre→departamento:\n", df.loc[:, 'nombre':'departamento'].head(10))
    print("\nMayores de 50 (nombre,salario):\n", df.loc[df['edad']>50,['nombre','salario']].head(10))

if __name__=="__main__": ejercicio_04()
