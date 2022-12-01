# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input("Введите число "))
lst = []
productOfNumbers = 0

for i in range(-n, n+1):
    lst.append(i)

with open('file.txt') as file:
    for item in file:
        if int(item) < len(lst):
            if productOfNumbers != 0:
                productOfNumbers = productOfNumbers*lst[int(item)]
            else:
                productOfNumbers = lst[int(item)] 
        else: 
            print("В списке нет позиции: ",item)

print(productOfNumbers)