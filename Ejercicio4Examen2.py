#4
import numpy as np
from scipy.sparse import random as sparse_random
from scipy.sparse import csr_matrix

# Dimensiones de las matrices
filas = 1000
columnas = 1000

# Generar matrices dispersas aleatorias
densidad = 0.01  # 1% de los elementos son diferentes de cero
matriz_A = sparse_random(filas, columnas, density=densidad, format='csr', dtype=np.float64)
matriz_B = sparse_random(columnas, filas, density=densidad, format='csr', dtype=np.float64)

# Multiplicar las matrices dispersas
matriz_resultante = matriz_A.dot(matriz_B)

# Mostrar información sobre la matriz resultante
print(f"La matriz resultante tiene forma: {matriz_resultante.shape}")
print();
print(f"{matriz_resultante.nnz} elementos no nulos")
