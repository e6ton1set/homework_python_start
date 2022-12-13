# Сумма элементов вещественного числа с помощью
# использования **лямбд, filter, map, zip, enumerate, list comprehension

num = input('Введите вещественное число (например, 8.9): ')
result = sum(map(int, num.replace('.', '')))
print (f'\nСумма элементов вещественного числа {num} = {result}')