# Найти факториал с помощью
# использования **лямбд, filter, map, zip, enumerate, list comprehension

from math import factorial


num = int(input('Введите число: '))
print(list(map(lambda x: ((x == 0) and 1) or x * factorial(x -1),list(range(1,num+1)))))