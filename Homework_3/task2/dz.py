# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

lst = [2, 3, 4, 5, 6]
lenNewLst = 0

if len(lst) % 2 != 0:
    lenNewLst = len(lst)//2 + 1
else:
    lenNewLst = len(lst)//2

newLst = []
for i in range(lenNewLst):
   newLst.append(lst[i]*lst[len(lst)-i-1])

print(newLst)