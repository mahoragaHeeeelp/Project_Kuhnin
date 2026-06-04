"""
Вариант 5. Блок 2.
Создайте класс "Фрукт", который содержит информацию о наименовании и весе фрукта.
Создайте классы "Яблоко" и "Апельсин", которые наследуются от класса "Фрукт" 
и содержат информацию о цвете.
"""
class Fruit:

    def set_base_info(self, name, weight):
        self.name = name
        self.weight = weight


class Apple(Fruit):

    def set_apple_info(self, name, weight, color):
        self.set_base_info(name, weight)
        self.color = color


class Orange(Fruit):

    def set_orange_info(self, name, weight, color):
        self.set_base_info(name, weight)
        self.color = color


apple_instance = Apple()
apple_instance.set_apple_info("Голден", 0.18, "Желтый")

print(apple_instance.name)
print(apple_instance.weight)
print(apple_instance.color)

orange_instance = Orange()
orange_instance.set_orange_info("Валенсия", 0.25, "Оранжевый")

print(orange_instance.name)
print(orange_instance.weight)
print(orange_instance.color)
