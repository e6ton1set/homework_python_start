# Задайте словарь из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.

num = int(input('Введите число N: '))

dictionary = {}

sum_element_dictionary = 0

for i in range(1, num + 1):
    dictionary[i] = round((1+(1/i))**i, 3)
    sum_element_dictionary += dictionary[i]
print(dictionary)
print(f'\nСумма значений словаря равна {round(sum_element_dictionary, 3)}')