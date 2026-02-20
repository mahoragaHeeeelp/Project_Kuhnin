"""
Вариант 5.
Из последовательности на n целых чисел создать новую последовательность, в 
которой каждый последующий элемент равен квадрату суммы двух соседних элементов.
"""

def solve_task_1():
    n_list = list(map(int, input("введите числа через пробел: ").split()))
    
    if len(n_list) < 2:
        print("нужно хотя бы два числа!")
        return

    result = [(n_list[i] + n_list[i+1])**2 for i in range(len(n_list) - 1)]
    print(result)

solve_task_1()
