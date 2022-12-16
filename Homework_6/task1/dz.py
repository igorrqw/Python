# Наибольший общий делитель
# В модуле math есть функция math.gcd(a, b), возвращающая наибольший общий делитель (НОД) двух чисел.
#  Вычислите и напечатайте наибольший общий делитель для списка натуральных чисел. Ввод чисел продолжается до ввода пустой строки.
# Входные данные Выходные данные
# 36 6
# 12
# 144
# 18

import math
from functools import reduce

lst = []

while True:
    num = input("Введите число: ")
    if num == '':
        break
    lst.append(int(num))

def find_gcd(list):
    x = reduce(math.gcd, list)
    return x

print(lst)
print(find_gcd(lst))