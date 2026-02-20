"""
Вариант 5.
Составить генератор (yield), который переведет символы строки из нижнего 
регистра в верхний.
"""
def upper_gen(text):
    for char in text:
        yield char.upper()

input_str = input("введите строку в нижнем регистре: ")
for symbol in upper_gen(input_str):
    print(symbol, end="")
print()
