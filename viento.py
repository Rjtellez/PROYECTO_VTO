# correr es shift + bloq mayus + F10
# programa para trabajar con vto.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def promedio(dir,mag):
    #promedio vectorial del viento
    U, V = convertir_a_uv(dir,mag)
    uprom = np.nanmean(U)
    vprom = np.nanmean(V)
    dirprom, magprom = convertir_a_dirmag(uprom,vprom)
    return dirprom,magprom

def convertir_a_uv(direccion, magnitud):
    # dirección en  grados y magnitud en lo que sea
    u = np.round(-magnitud * np.sin(np.deg2rad(direccion)), decimals=14)
    v = np.round(-magnitud * np.cos(np.deg2rad(direccion)), decimals=14)
    return u, v

def convertir_a_dirmag(u,v):
    #dirección en  grados y magnitud en lo que sea
    mag = np.sqrt(np.power(u,2)+np.power(v,2))
    dir = np.remainder(np.rad2deg(np.arctan2(-u,-v)),360)
    return dir, mag

def promedio(dir,mag):
    #promedio vectorial del viento
    U, V = convertir_a_uv(dir,mag)
    uprom = np.nanmean(U)
    vprom = np.nanmean(V)
    dirprom, magprom = convertir_a_dirmag(uprom,vprom)
    return dirprom,magprom

def convertir_a_rosa(direccion):
    #convertir a rosa de vientos
    directions = np.array('N NNE NE ENE E ESE SE SSE S SSW SW WSW W WNW NW NNW N NAN'.split())
    bins = np.arange(11.25, 372, 22.5)
    serie = pd.Series(directions[np.digitize(direccion, bins)])
    return serie.replace('NAN', np.nan)

if __name__ == '__main__':
#datos inventados o insertados directo
    # mag = np.array([10,12])
    # dir = np.array([90,110])

#extraer datos desde excel con el nombre de la columna
    #df = pd.read_excel("dir y mag vto.xlsx")
    #dir = df['direccion']
    #mag = df['magnitud']

#extraer datos desde excel con el numero de columna
    df = pd.read_excel("dir y mag vto.xlsx")
    dir = df[df.columns[0]]
    mag = df[df.columns[1]]

#promedio del viento de excel
    # dirprom,magprom = promedio(dir,mag)
    # DF3 = pd.DataFrame({'DIRPROM': [dirprom], 'MAGPROM': [magprom]})
    # DF3.to_excel('direccion_promedio.xlsx')
    print(dir)
    print(convertir_a_rosa(dir))

#comando producto principal (main)
#convertir
    #U, V = convertir_a_uv(dir, mag)
   # DF = {'U': U, 'V': V}
#comprimimos en data frame
    #DF2 = pd.DataFrame(DF)
#salidas
    #print(U, V)
    #DF2.to_excel('salida.xlsx',index=False)

    #print(DF2)

#salida gráfica

    #x = DF2["U"]
    #y = DF2["V"]
    #plt.plot(x,y)
    #plt.xlabel("velocid zonal, kt")
    #plt.ylabel("velocidad meridional, kt")
    #plt.title("vto")
    #plt.show()

    #print(convertir_a_dirmag(np.array([-10,7]),np.array([10,5])))



