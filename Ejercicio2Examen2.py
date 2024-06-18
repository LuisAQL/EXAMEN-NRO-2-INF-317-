#2
import numpy as np
from scipy.sparse import coo_matrix

# Definimos las listas de aristas para cada grafo
edges1 = [(0, 1), (1, 2), (2, 3)]
edges2 = [(0, 2), (1, 3)]

# Encontramos el número máximo de nodos para determinar el tamaño de la matriz
max_node = max(max(u, v) for u, v in edges1 + edges2) + 1

# Función para convertir listas de aristas a matrices dispersas
def edges_to_sparse_matrix(edges, size):
    # Obtener los nodos de origen (row) y destino (col)
    row = [u for u, v in edges]
    col = [v for u, v in edges]
    # Asignar un valor de 1 a cada arista
    data = [1] * len(edges)
    # Crear y retornar la matriz dispersa
    return coo_matrix((data, (row, col)), shape=(size, size))

# Convertimos las listas de aristas a matrices dispersas
sparse_matrix1 = edges_to_sparse_matrix(edges1, max_node)
sparse_matrix2 = edges_to_sparse_matrix(edges2, max_node)

# Mostramos las matrices dispersas
print("Matriz dispersa del Grafo 1:")
print(sparse_matrix1)

print("\nMatriz dispersa del Grafo 2:")
print(sparse_matrix2)


