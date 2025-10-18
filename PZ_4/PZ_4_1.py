"Вариант 5. Дано вещественное число - цена 1 кг конфет. Вывести стоимость 1.2, 1.4, ... 2кг конфет"
try:
    price = float(input())
    weight = 1.2
    while weight <= 2.0:
        print(f"{weight} кг: {price * weight:}")
        weight += 0.2
except ValueError:
    print("ошибка, жалко")
