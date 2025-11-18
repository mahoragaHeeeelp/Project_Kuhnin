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
