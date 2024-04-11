import numpy as np
import pandas as pd
import scipy.io as sp  

matriz_aleatoria= np.random.randint(11, size=(20,30,20,100))

nueva_matriz= matriz_aleatoria.copy()
nueva_matriz = nueva_matriz[:, :, :, 0]

print(f'Nueva matriz: {nueva_matriz}')
print(f'dimencion:',nueva_matriz.ndim)
print(f'tamaño:',nueva_matriz.shape)
print(f'numero de elementos:',nueva_matriz.size)
print(f'tipo de datos:',nueva_matriz.dtype)


matriz_2d= np.reshape(nueva_matriz,(100,120))
print(f' Matriz 2D: {matriz_2d}')

def matriz_dataframe(m):
    df= pd.DataFrame(m)
    return df 
data_resultado= matriz_dataframe(matriz_2d)
print(f'Data Frame: {data_resultado}')

def cargar_archivo(a):
    if a.endswith('.mat'):
        datos= sp.loadmat(a)
        return datos
    elif a.endswith('.csv'):
        datos= pd.read_csv(a, encoding='utf-8')
        return datos 
    else:
        print ('Archivo no compatible')

def suma_eje(arr, eje=None):
    return np.sum(arr, axis=eje)

def resta_eje(arr, eje=None):
    return np.subtract(arr, np.mean(arr, axis=eje), axis=eje)

def multiplicacion_eje(arr, eje=None):
    return np.prod(arr, axis=eje)

def division_eje(arr, eje=None):
    return np.divide(arr, np.mean(arr, axis=eje), axis=eje)

def logaritmo_eje(arr, eje=None):
    return np.log(arr, axis=eje)

def promedio_eje(arr, eje=None):
    return np.mean(arr, axis=eje)

def desviacion_estandar_eje(arr, eje=None):
    return np.std(arr,axis=eje)
