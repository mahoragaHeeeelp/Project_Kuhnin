try:
    A = int(input("Введите A: "))
    B = int(input("Введите B: "))
    print((A > 0) or (B < -2))
except ValueError:
    print("Ошибка, это печально")
