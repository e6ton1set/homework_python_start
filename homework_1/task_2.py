
x = int(input('Введите число X: '))
y = int(input('Введите число Y: '))
z = int(input('Введите число Z: '))

for x in range(2):
        for y in range(2):
            for z in range(2):
                print(f'X = {x}, Y = {y}, Z = {z}')
                print(not (x or y or z) == (not x and not y and not z))
                