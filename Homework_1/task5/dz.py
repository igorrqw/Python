# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

xa = int(input("Введите координату точки А по X "))
ya = int(input("Введите координату точки А по Y "))
xb = int(input("Введите координату точки В по X "))
yb = int(input("Введите координату точки В по Y "))
import math
distans = math.sqrt((xa-xb)**2+(ya-yb)**2)
distans = int(distans * 100)
distans = float(distans / 100)
print(f'Растояние между точкой A до точки B = {distans}')