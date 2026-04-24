"""
Вариант 5
Сгенерировать матрицу, в которой нечетные элементы заменяются на 0
"""

import random

rows, cols = 5, 5
matrix = [[random.randint(1, 30) for i in range(cols)] for i in range(rows)]

print("cгенерированая матрица:")
for row in matrix:
    print(row)


for i in range(rows):
    for j in range(cols):
        if matrix[i][j] % 2 == 1:
            matrix[i][j] = 0

print("новая матрица:")
for row in matrix:
    print(row)
