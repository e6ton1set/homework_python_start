# Найти расстояние между 2 точками в 2D пространстве
# c помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

from functools import reduce


a = list(map(int, input('Введите x и y для координаты А через запятую (2,3): ').split(','))) 
b = list(map(int, input('Введите x и y для координаты В через запятую (-2,-3): ').split(',')))

def get_distance_2D(a, b):
     rng = reduce(lambda x, y: (x + y)**(1/2), (map(lambda dot: (dot[1] - dot[0])**2, zip(a, b))))
     return round(rng, 2)
     
print(get_distance_2D(a, b))
