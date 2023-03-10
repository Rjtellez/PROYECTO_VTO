import pandas as pd
import functions.Vto as Vto

df = pd.read_csv("data/Estacion_PUEBLA__3_dias.csv",skiprows=9)

#extraer por numero de columna
df['fecha'] = pd.to_datetime(df['Fecha UTC'], format='%d/%m/%Y %H:%M')
dir= df[df.columns[7]]
mag= df[df.columns[8]]
print(df.head())
print(df.info())

u,v=Vto.convertir_a_uv(dir,mag)

Vto.grafica_de_astillas(df['fecha'],u,v)