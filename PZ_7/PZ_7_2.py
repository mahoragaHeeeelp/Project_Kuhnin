""" Вариант 7. Дана строка-предложение на русском языке и число K (0 < K < 10).
Зашифровать строку, выполнив циклическую замену каждой буквы на букву того же регистра,
расположенную в алфавите на K-й позиции после шифруемой буквы
(например, для K = 2 «A» перейдет в «B», «a» — в «в», «Б» — в «Г», «я» — в «б» и т. д.).
Букву «ё» в алфавите не учитывать, знаки препинания и пробелы не изменять. """ 

try:
    text = input("введите предложение на русском языке: ")
    K = int(input("введите K (0 < K < 10): "))
    if not (0 < K < 10):
        raise ValueError("K должно быть в диапазоне 0 < K < 10")
    
    result = []
    for char in text:
        if 'А' <= char <= 'Я':
            new_char = chr((ord(char) - ord('А') + K) % 32 + ord('А'))
            result.append(new_char)
        elif 'а' <= char <= 'я':
            new_char = chr((ord(char) - ord('а') + K) % 32 + ord('а'))
            result.append(new_char)
        else:
            result.append(char)
    
    print("зашифрованный текст:")
    print(''.join(result))

except Exception as e:
    print("ошибка: {e}")
