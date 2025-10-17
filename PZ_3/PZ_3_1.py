try:
    A = int(input("введите A: "))
    B = int(input("введите B: "))
    print((A > 0) or (B < -2))
except ValueError:
    print("ошибка, это печально")
