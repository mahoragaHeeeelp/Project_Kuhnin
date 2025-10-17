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
