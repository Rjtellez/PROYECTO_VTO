'''
Programa para trabajar con viento a componentes u v
'''
import numpy as np


def convertir_a_uv(direccion,magnitud):
    #Dirección en grados y magnitud en cualquier 
    u = -magnitud * np.sin(np.deg2rad(direccion))
    v = -magnitud * np.cos(np.deg2rad(direccion))
    return u, v

if __name__ == '__main__':
    mag = np.array([10,12])
    dir = np.array([90,110])
    U,V = convertir_a_uv(dir,mag)
    
