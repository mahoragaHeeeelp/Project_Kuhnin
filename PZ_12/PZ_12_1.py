"""
Вариант 5
В матрице элементы второго столбца возвести в квадрат.
"""

import random

rows = int(input("введите количество строк "))
cols = int(input("введите количество столбцов "))

matrix = list(map(lambda i: list(map(lambda j: random.randint(1, 20), range(cols))), range(rows)))

print("исходная матрица ")
for row in matrix:
    print(row)

matrix = list(map(lambda row: row[:1] + [row[1] ** 2] + row[2:] if len(row) > 1 else row, matrix))

print("новая матрица ")
for row in matrix:
    print(row)
