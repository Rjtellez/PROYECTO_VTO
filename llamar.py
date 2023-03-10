import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import functions.Vto as Vto

#datos desde excel
df= pd.read_excel("tabla p.vto.xlsx")

#extraer por numero de columna
dir= df[df.columns[0]]
mag= df[df.columns[1]]

print(dir)
print(Vto.convertir_a_rosa(dir))