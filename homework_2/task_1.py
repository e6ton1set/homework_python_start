# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр (сделать для строки).

num = input('Введите вещественное число: ')

def sum_float(num):
    return sum(map(int, num.replace('.','').replace('-','').replace(',','')))

result = sum_float(num)

print(f'\nСумма цифр в числе {num} = {result}')