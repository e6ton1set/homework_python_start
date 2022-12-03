# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# - 45 -> 101101

num = int(input('Введите целое число: '))
result_str = ''

while num > 0:
    result_str = str(num % 2) + result_str
    num = num // 2

print(result_str)