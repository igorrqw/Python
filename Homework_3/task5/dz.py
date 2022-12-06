# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#  Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Введите число: '))

fibo_nums = []

a, b = 1, 1
for i in range(n):
    fibo_nums.append(a)
    a, b = b, a + b

a, b = 0, 1
for i in range (n+1):
    fibo_nums.insert(0, a)
    a, b = b, a - b

print(fibo_nums)