# Задача Измените код одной-двух решенных ранее задач (с прошлых семинаров или домашних работ),
# применив лямбды, filter, map, zip, enumerate, списочные выражения.

# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# lst = [1.1, 1.2, 3.1, 5, 10.01]
# newLst = []
# for i in lst:
#     if i%1 != 0:
#         newLst.append(round(i%1, 2))

# print(max(newLst) - min(newLst))

# Новое решение задачи
# Ссылка на предыдущее решение: https://github.com/igorrqw/Python/blob/main/Homework_3/task3/dz.py


lst = [1.1, 1.2, 3.1, 5, 10.01]
filter_list = list(filter(lambda x: x%1 != 0 , lst))
result_list = list(map(lambda x: round(x%1, 2) , filter_list))
print(max(result_list) - min(result_list))