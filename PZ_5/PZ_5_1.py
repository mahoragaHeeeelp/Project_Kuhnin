
""" Вариант 5
С помощью функций получить вертикальную и горизонтальную линии.
Линия проводится многократной печатью символа.
Заключить слово в рамку из полученных линий. """
def cc (s):
    c = 0
    for i in s:
        c+= 1
    return c

try:
  w = str(input("слово-"))
  if w == "":
      print("ошибка")
  else:
      n = cc(w)
      top = '#' * (n+4)
      mid = '# ' + w + ' #'
      print(top)
      print(mid)
      print(top)

except ValueError:
    print("ошибка")
