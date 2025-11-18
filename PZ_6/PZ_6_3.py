try:
    N = int(input("введите размер списка N: "))
    A = []
    for i in range(N):
        element = int(input(f"введите элемент A[{i}]: "))
        A.append(element)
    
    result = A.copy()
    n = len(A)
    
    for i in range(n):
        if i == 0 and n > 1:
            if A[i] > A[i+1]:
                result[i] = 0
        elif i == n-1:
            if A[i] > A[i-1]:
                result[i] = 0
        else:
            if A[i] > A[i-1] and A[i] > A[i+1]:
                result[i] = 0
    
    print("результат после обнуления локальных максимумов:")
    print(result)

except Exception as e:
    print("произошла ошибка: {e}")
