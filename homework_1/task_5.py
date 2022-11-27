# Напишите программу, которая принимает на вход координаты двух точек
#  и находит расстояние между ними в 2D пространстве.

import math

x1 = float(input('Введите значение для x1: '))
y1 = float(input('Введите значение для y1: '))
x2 = float(input('Введите значение для x2: '))
y2 = float(input('Введите значение для y2: '))

pythagorean_formula = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f'\nРасстояние между точками A и B в 2D пространстве равно {round(pythagorean_formula, 2)}')
