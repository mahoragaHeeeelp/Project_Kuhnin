""" Вариант 5. Описать функцию DigitCountSum(K, C, S), находящую количество С цифр целого положительного числа К,
а также их сумму S (K -- входной, С и S -- выходные параметры целого типа).
С помощью этой функции найти количество и сумму цифр
для каждого из пяти данных целых чисел. """ 



def dc(k):
    count = 0
    while k > 0:
        count += 1
        k //= 10
    return count

def ds(k):
    total = 0
    while k > 0:
        total += k % 10
        k //= 10
    return total


def DigitCountSum(K, C, S):
    C = dc(K)
    S = ds(K)
    return C, S

try:
    print("Введите 5 целых положительных чисел:")
    
    i = 1 
    while i <= 5:
        num_input = input(f"число {i}: ").strip()
        
        if num_input == "":
            print("Ошибка: введите число.")
            continue  
        
        try:
            num = int(num_input)
            if num <= 0:
                print("Ошибка: нужно положительное число.")
                continue  
            
           
            c, s = DigitCountSum(num, 0, 0)  
            
            print(f"число {num} кол-во цифр: {c}, сумма цифр: {s}")
            i += 1  
            
        except ValueError:
            print("Ошибка: введите целое число.")
            
except Exception as e:
    print("Неизвестная ошибка:", e)
