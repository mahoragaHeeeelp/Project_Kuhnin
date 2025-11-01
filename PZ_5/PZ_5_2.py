""" Вариант 5. Описать функцию DigitCountSum(K, C, S), находящую количество С цифр целого положительного числа К,
а также их сумму S (K -- входной, С и S -- выходные параметры целого типа).
С помощью этой функции найти количество и сумму цифр
для каждого из пяти данных целых чисел. """ 

def dc(k):
  count = 0
  while k > 0:
    count += 1
    k // 10
  return count

def ds(k):
  total = 0 
  while k > 0 :
    total += k % 10
    k // 10
  return total 

try:
  print("введите 5 чисел")
  for i in range(1,6):
    num = int(input(f"число{i}: "))
    if num <= 0:
      print("нужно положительное число")
    else:
      c = dc(num)
      s = ds(num)
      print(f"число {num} кол-во цифр:{c}, сумма цифр: {s}")

except ValueError:
  print("ошибка")
  
