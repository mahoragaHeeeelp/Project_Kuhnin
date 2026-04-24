"""
Вариант 5
В матрице элементы второго столбца возвести в квадрат.
"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("исходная матрица")
for row in matrix:
    print(row)

for i in range(len(matrix)):
    matrix[i][1] = matrix[i][1] ** 2

print("новая матрица")
for row in matrix:
    print(row)
