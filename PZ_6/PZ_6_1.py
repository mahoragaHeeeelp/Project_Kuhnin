""" Вариант 5 . Дано целое число N (>2). Сформировать и вывести целочисленный список размера
10, содержащий 10 первых элементов последовательности чисел Фибоначчи FK: F1
= 1, F2 = 1, FK = FK-2 + FK-1, K = 3,4,... . """ 


try:
    N = int(input("Введите N (>2): "))
    if N <= 2:
        raise ValueError("N должно быть больше 2")
    
    fib = [1, 1]
    
    for i in range(2, N):
        next_fib = fib[i-2] + fib[i-1]
        fib.append(next_fib)
    
    print("первые", N, "чисел фибоначчи:")
    print(fib)

except Exception as e:
    print("ошибка: {e}")
