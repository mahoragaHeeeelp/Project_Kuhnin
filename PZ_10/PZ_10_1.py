# Вариант 5
""" Средствами языка Python сформировать текстовый файл (.txt),
содержащий последовательность из целых положительных и отрицательных чисел.
Сформировать новый текстовый файл (.txt) следующего вида,
предварительно выполнив обработку элементов:
исходные данные:
количество элементов:
сумма элементов:
элементы, умноженные на минимальный элемент: """

numbers = [10, -3, 7, -8, 15, 2, -1]

with open("input_numbers.txt", "w", encoding="utf-8") as f:
    for num in numbers:
        f.write(str(num) + " ")

count = len(numbers)
total_sum = sum(numbers)
min_element = min(numbers)

multiplied = [num * min_element for num in numbers]

with open("output_numbers.txt", "w", encoding="utf-8") as f:
    f.write("исходные данные:\n")
    f.write(" ".join(map(str, numbers)) + "\n")
    f.write(f"количество элементов: {count}\n")
    f.write(f"сумма элементов: {total_sum}\n")
    f.write("элементы, умноженные на минимальный элемент:\n")
    f.write(" ".join(map(str, multiplied)))

print("Файлы успешно созданы.")
