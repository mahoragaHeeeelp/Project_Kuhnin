try:
    N = int(input("введите размер списка N: "))
    A = []
    for i in range(N):
        element = int(input(f"введите элемент A[{i}]: "))
        A.append(element)
    
    K = int(input("введите K: "))
    L = int(input("введите L: "))
    
    if not (1 < K < L < N):
        raise ValueError("условие 1 < K < L < N не выполняется")
    
    k_idx = K - 1
    l_idx = L - 1
    
    segment = A[k_idx:l_idx+1]
    reversed_segment = segment[::-1]
    A[k_idx:l_idx+1] = reversed_segment
    
    print("результат после переворота:")
    print(A)

except Exception as e:
    print("произошла ошибка: {e}")
