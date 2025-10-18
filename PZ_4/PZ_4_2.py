""" Вариант 5. Дано целое число N(>0). Используя операции деления нацело и взятия остатка от деления, 
найти количество и сумму его цифр."""
try:
    n = int(input())
    count = 0
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        count += 1
        n //= 10
    print(count, total)
except ValueError:
    print("эхх, ошибка")
