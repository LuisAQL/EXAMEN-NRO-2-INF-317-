#5
import numpy as np
import scipy.sparse as sps
import multiprocessing as mp
import time

# Crear matrices sparse aleatorias
size = 1000
density = 0.01
A = sps.random(size, size, density=density, format='csr')
B = sps.random(size, size, density=density, format='csr')

# Función para multiplicar filas de la matriz A por la matriz B
def multiply_row(row_index):
    return A.getrow(row_index).dot(B)

# Crear un pool de procesos
num_processes = mp.cpu_count()
pool = mp.Pool(processes=num_processes)

# Medir el tiempo de ejecución
start_time = time.time()

# Multiplicar las filas de manera paralela
result_rows = pool.map(multiply_row, range(size))

# Unir los resultados en una matriz sparse
result = sps.vstack(result_rows)

# Cerrar el pool de procesos
pool.close()
pool.join()

# Calcular y mostrar el tiempo de ejecución
end_time = time.time()
execution_time = end_time - start_time
print("Tiempo de ejecución:", execution_time, "segundos")

# Mostrar el resultado de la multiplicación
print("Resultado de la multiplicación:")
print(result.toarray())
