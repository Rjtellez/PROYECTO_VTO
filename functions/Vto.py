#programa para trabajar con vto.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def grafica_de_astillas(time, u, v, **kw):
    width = kw.pop('width', 0.002)
    headwidth = kw.pop('headwidth', 0)
    headlength = kw.pop('headlength', 0)
    headaxislength = kw.pop('headaxislength', 0)
    angles = kw.pop('angles', 'uv')
    ax = kw.pop('ax', None)

    if angles != 'uv':
        raise AssertionError("Stickplot angles must be 'uv' so that"
                             "if *U*==*V* the angle of the arrow on"
                             "the plot is 45 degrees CCW from the *x*-axis.")

    #time, u, v = map(np.asanyarray, (time, u, v))
    if not ax:
        fig, ax = plt.subplots()

    q = ax.quiver(time, [[0] * len(time)], u, v,
                  angles='uv', width=width, headwidth=headwidth,
                  headlength=headlength, headaxislength=headaxislength,
                  **kw)

    
    ax.axes.get_yaxis().set_visible(False)
    #ax.xaxis_date()
    plt.show()
    return q

def convertir_a_rosa(direccion):
    rosas = np.array(['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW', 'N', 'NaN'])
    bins = np.arange(11.25, 372, 22.5)
    return pd.Series(rosas[np.digitize(np.remainder(direccion,360), bins)])

def convertir_a_uv(direccion,magnitud):
    #direccion en grados y magnitud en lo que sea
    u= np.round(-1*magnitud * np.sin(np.deg2rad(direccion)),decimals=14)
    v= np.round(-1*magnitud * np.cos(np.deg2rad(direccion)),decimals=14)
    return u,v

def convertir_a_dirmag(u,v):
    #lo que sea en direccion en grados y magnitud
    mag= np.sqrt(np.power(u,2)+np.power(v,2))
    dir= np.remainder(np.rad2deg(np.arctan2(-1*u,-1*v)),360)
    return dir,mag

def promedio(dir,mag):
    #promedio vectorial del viento
    u,v=convertir_a_uv(dir,mag)
    uprom= np.nanmean(u)
    vprom=np.nanmean(v)
    dirprom,magprom= convertir_a_dirmag(uprom,vprom)
    return dirprom,magprom

if __name__ == '__main__':

#ENTRADAS
#datos directos en python
    # mag= np.array( [10,12])
    # dir= np.array([90,110] )

#datos desde excel
    df= pd.read_excel("tabla p.vto.xlsx")
    #extraer por nombre de la columna
    #dir= df["direccion"]
    #mag= df["magnitud"]
#extraer por numero de columna
    dir= df[df.columns[0]]
    mag= df[df.columns[1]]

#COMANDO PRINCIPAL (MAIN)

#promedio del vto en excel
    #dirprom,magprom=promedio(dir,mag)
    #DF=pd.concat(dirprom,magprom)
    #DF.to_excel("tablaprom p.vtopython.xlsx",index=False)

    print(dir)
    #print(convertir_a_rosa(dir))
#cambiar datos a componentes cartesianas
    #U,V= convertir_a_uv(dir,mag)
    #comprimir en un dataframe, pero antes agrupados en un diccionario
    #DF=pd.DataFrame({"U":U,"V":V})

#SALIDAS

#pantalla de python
    #print(U,V)
    #print(convertir_a_dirmag(np.array([-10,7]),np.array([-10,7])))

#a doc de excel
    #DF.to_excel("tabla p.vtopython.xlsx",index=False)

#salida en forma grafica
    #x=DF['U']
    #y=DF['V']
    #plt.plot(x,y)
    #plt.xlabel('Velocidad zonal, kt')
    #plt.ylabel("Velocidad meridional, kt")
    #plt.show()
    #plt.title("Grafica de viento")