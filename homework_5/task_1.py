import random

player_1 = input('\nВведите имя первого игрока: ')
player_2 = input('\nВведите имя второго игрока: ')
candy = int(input('\nВведите количество конфет: '))
tmp_1 = 0
tmp_2 = 0

whose_move = random.randrange(1, 3)

if whose_move == 1:
    print(f'\n{player_1}, ваш ход!')
else:
    print(f'\n{player_2}, ваш ход!')

while candy > 0:
    if candy > 28:
        tmp_1 = int(input(f'\n{player_1}, вы можете взять до 28 конфет включительно. \nСколько берёте?\n'))
        candy = candy - tmp_1
        if candy > 28:
            tmp_2 = int(input(f'\n{player_2}, вы можете взять до 28 конфет включительно. \nСколько берёте?\n'))
            candy = candy - tmp_2
            if candy >= 28:
                    print(f'\nОсталось {candy} конфет.')
        else:
            if player_1 == 1:
                print(f'\nОсталось {candy} конфет, их забирает {player_2}. Победа за вами!')
            else:
                print(f'\nОсталось {candy} конфет, их забирает {player_1}. Победа за вами!')
                break