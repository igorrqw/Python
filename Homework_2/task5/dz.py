# Реализуйте алгоритм перемешивания списка(shuffle использовать нельзя, другие методы из библиотеки random - можно).

import random
list = [1, 2, 3, 4, 5, 6, 7, 8]
mixList = sorted(list, key=lambda A: random.random())
print(mixList)