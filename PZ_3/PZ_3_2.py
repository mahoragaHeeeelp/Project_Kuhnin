"""Вариант 5. Мастям игральных карт присвоены порядковые номера: 1 - пики, 2 - трефы, 3 - бубны, 4 - червы.
Достоинству карт присвоены номера: 11 - валет, 12 - дама, 13 - король, 14 - туз. Дано трёхзначное число, в котором первая цифра
указывает на масть, а вторые две на достоинство карты. Вывести соответствующее название карты вида "дама червей", "туз треф" и т.п."""

try:
    number = input("введите трехзначное число: ")

    if len(number) != 3 or not number.isdigit():
        raise ValueError("ошибка")

    suit_n = int(number[0])
    rank_k = int(number[1:])

    if suit_n == 1:
        suit = "пики"
    elif suit_n == 2:
        suit = "трефы"
    elif suit_n == 3:
        suit = "бубны"
    elif suit_n == 4:
        suit = "черви"
    else:
        raise ValueError("недопустимый номер")

    if rank_k == 11:
        rank = "валет"
    elif rank_k == 12:
        rank = "дама"
    elif rank_k == 13:
        rank = "король"  
    elif rank_k == 14:
        rank = "туз"
    else:
        raise ValueError("недопустимое достоинство.")

    print(f"{rank} {suit}")

except ValueError as e:
    print(f"Ошибка: {e}")
