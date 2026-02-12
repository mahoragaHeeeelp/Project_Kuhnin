# Вариант 5
"""  Из предложенного текстового файла (text18-5.txt) вывести на экран его содержимое,
количество символов в тексте
cформировать новый файл, в который поместить текст в стихотворной форме,
предварительно заменив символы нижнего регистра на верхний. """

file_path = "text18-5.txt"

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

print("содержимое файла")
print(text)

char_count = len(text)
print("\nКоличество символов в тексте", char_count)

upper_text = text.upper()

with open("text18-5_upper.txt", "w", encoding="utf-8") as f:
    f.write(upper_text)

print("\n новый файл создан")
