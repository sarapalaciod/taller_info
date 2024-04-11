import numpy as np 

matriz_aleatoria= np.random.randint(11, size=(20,30,20,100))

nueva_matriz= matriz_aleatoria.copy()
nueva_matriz = nueva_matriz[:, :, :, 0]

print(f'Nueva matriz: {nueva_matriz}')
print(f'dimencion:',nueva_matriz.ndim)
print(f'tamaño:',nueva_matriz.shape)
print(f'numero de elementos:',nueva_matriz.size)
print(f'tipo de datos:',nueva_matriz.dtype)
