# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

number = int(input('Введите цифру от 1 до 7, где 1 - понедельник, 2 - вторник и т.д.: '))

if number <= 5 and number > 0:
    print('\nСегодня рабочий день.')
elif number <= 7:
    print('\nСегодня выходной, ура!')
else:
    print('\nОшибка! Введите цифру от 1 до 7.')
   