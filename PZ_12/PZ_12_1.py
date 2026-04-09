"""
Вариант 5
1. В матрице элементы второго столбца возвести в квадрат.
"""


import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Исходная матрица:")
print(matrix)

matrix[:, 1] = matrix[:, 1] ** 2

print("новая матрица - ")
print(matrix)
