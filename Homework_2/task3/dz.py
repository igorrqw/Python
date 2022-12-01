# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

n = int(input("Введите число : "))
lst = []
for i in range(1, n):
    lst.append((1+1/i)**i)
s = sum(lst)
print(s)