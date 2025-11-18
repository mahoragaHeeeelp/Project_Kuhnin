""" Вариант 5. Дано целое число N (1 < N < 26).
Вывести N последних строчных (то есть маленьких)
букв латинского алфавита в обратном порядке (начиная с буквы «z»). """ 

try:
    N = int(input("введите N (1 < N < 26): "))
    if not (1 < N < 26):
        raise ValueError("N должно быть в диапазоне 1 < N < 26")
    
    result = []
    for i in range(N):
        letter = chr(ord('z') - i)
        result.append(letter)
    
    print("результат:")
    print(' '.join(result))

except Exception as e:
    print("ошибка: {e}")
