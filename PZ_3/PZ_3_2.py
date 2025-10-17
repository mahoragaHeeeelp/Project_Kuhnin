try:
    num = int(input("введите трёхзначное число: "))
    suit = num // 100
    rank = num % 100

    suits = {1: "пик", 2: "треф", 3: "бубен", 4: "червей"}
    ranks = {11: "валет", 12: "дама", 13: "король", 14: "туз"}

    if suit in suits and rank in ranks:
        print(f"{ranks[rank]} {suits[suit]}")
    else:
        print("неверный номер карты")
except ValueError:
    print("ошибка, как так то")
