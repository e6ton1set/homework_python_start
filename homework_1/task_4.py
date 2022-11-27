# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter_position = int(input('Введите номер четверти: '))

if quarter_position == 1:
    print('\nВозможные значения координат: x > 0 and y > 0')

elif quarter_position == 2:
    print('\nВозможные значения координат: x < 0 and y > 0')

elif quarter_position == 3:
    print('\nВозможные значения координат: x < 0 and y < 0')

elif quarter_position == 4:
    print('\nВозможные значения координат: x > 0 and y < 0')

else:
    print('\nОшибка. Такой четверти не существует.')