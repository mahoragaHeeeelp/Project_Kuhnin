"""
Вариант 5
Сгенерировать матрицу, в которой нечетные элементы заменяются на 0
"""

import random

rows = int(input("введите количество строк "))
cols = int(input("введите количество столбцов "))


matrix = list(map(lambda i: list(map(lambda j: random.randint(1, 30), range(cols))), range(rows)))
print("сгенерированная матрица")

for row in matrix:
    print(row)

matrix = list(map(lambda row: list(map(lambda x: 0 if x % 2 == 1 else x, row)), matrix))

print("новая матрица")
for row in matrix:
    print(row)
