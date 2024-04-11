import numpy as np 
matriz_aleatoria= np.random.randint(11, size=(20,30,20,100))

print(f'Matriz: ', matriz_aleatoria)
print(f'Dimension de la matriz: ', matriz_aleatoria.ndim) 
print(f'Tamaño de la matriz: ', matriz_aleatoria.size)