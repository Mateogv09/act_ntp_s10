import pandas as pd, numpy as np
from datetime import datetime, timedelta

data = {
    'empleado_id': range(1, 101),
    'nombre': [f'Empleado_{i}' for i in range(1, 101)],
    'apellido': [f'Apellido_{i}' for i in range(1, 101)],
    'edad': np.random.randint(22, 65, 100),
    'departamento': np.random.choice(['Ventas','Marketing','IT','RRHH','Finanzas'],100),
    'salario': np.random.randint(30000,120000,100),
    'fecha_ingreso':[datetime(2020,1,1)+timedelta(days=np.random.randint(0,1460)) for _ in range(100)],
    'activo': np.random.choice([True,False],100,p=[0.85,0.15]),
    'ciudad': np.random.choice(['Bogotá','Medellín','Cali','Barranquilla','Cartagena'],100),
    'experiencia_años': np.random.randint(1,20,100)
}
df = pd.DataFrame(data).set_index('empleado_id')

def ejercicio_01():
    print("Empleado ID=5:\n", df.loc[5])
    print("\nEmpleados IDs 10,15,20:\n", df.loc[[10,15,20]])
    print("\nEmpleados del 25 al 30:\n", df.loc[25:30])

if __name__=="__main__": ejercicio_01()
