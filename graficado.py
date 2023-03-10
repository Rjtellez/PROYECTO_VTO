import pandas as pd
import matplotlib.pyplot as plt
import math
import Vto

#datos desde excel
df= pd.read_excel("confechas.xlsx")

#extraer por numero de columna
fechas= df[df.columns[0]]
dir= df[df.columns[1]]
mag= df[df.columns[2]]

u,v=Vto.convertir_a_uv(dir,mag)

Vto.stick_plot(fechas,u,v)