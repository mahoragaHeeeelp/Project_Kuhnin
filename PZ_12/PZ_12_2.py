"""
Вариант 5
Сгенерировать матрицу, в которой нечетные элементы заменяются на 0
"""

import numpy as np

rows, cols = 5, 5
matrix = np.random.randint(1, 30, size=(rows, cols))

print("cгенерированая матрица:")
print(matrix)

for i in range(rows):
    for j in range(cols):
        if matrix[i, j] % 2 == 1:
            matrix[i, j] = 0

print("новая матрица:")
print(matrix)
