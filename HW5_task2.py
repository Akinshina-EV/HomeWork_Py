# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг
# после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать
# не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний
# ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у
# своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота ""интеллектом""


import random


def get_first_player(count):
    return player_1 if random.randint(1, count) == 1 else player_2


candies_count = 100
candies_take = 28
print(f'Добро пожаловать в игру "{candies_count} конфета!"')
opponent = int(input('Выберете соперника: "1" - Человек, "2" - Компьютер: \n'))

if opponent == 1:
    player_1, player_2 = input('Введите имя Игрока 1: '), input(
        'Введите имя Игрока 2: ')
    current_player = get_first_player(3)
    print(
        f'\nПроведем жеребьевку!\nПервый ход делает Игрок {current_player}\n')
    print(f'Перед вами {candies_count} конфета. За один ход можно забрать не '
          f'более чем {candies_take} конфеты.')
    while True:
        candies_taken = int(input(f'\nВведите сколько конфет берет Игрок '
                                  f'{current_player}: '))
        if 1 <= candies_taken <= candies_take:
            current_player = player_2 if current_player == player_1 else \
                player_1
            candies_count -= candies_taken
            print(f'Осталось {candies_count} конфет.')
        else:
            candies_taken = int(input(
                f'\nБольше {candies_take} конфет за ход брать нельзя!\n'
                f'Введите сколько конфет берет Игрок {current_player}: '))
            if 1 <= candies_taken <= candies_take:
                current_player = player_2 if current_player == player_1 else \
                    player_1
                candies_count -= candies_taken
                print(f'Осталось {candies_count} конфет.')
        if 0 <= candies_count <= candies_take:
            break
    print(f'\nПобедил Игрок {current_player}!\nПоздравляем!!!')

elif opponent == 2:
    difficulty_level = int(input(
        'Выберете уровень сложности игры: "1" - легкий, "2" - сложный: \n'))
    player_1 = input('Введите имя Игрока: ')
    player_2 = 'Компьютер'
    current_player = get_first_player(3)
    print(
        f'\nПроведем жеребьевку!\nПервый ход делает Игрок {current_player}\n')
    print(f'Перед вами {candies_count} конфета. За один ход можно забрать не '
          f'более чем {candies_take} конфет.')

    if difficulty_level == 1:
        if current_player == player_1:
            while True:
                player_1_take = int(
                    input(f'\nВведите сколько конфет берет Игрок '
                          f'{player_1}: '))
                if 1 <= player_1_take <= 28:
                    candies_count -= player_1_take
                    print(f'Осталось {candies_count} конфет.\n')
                    current_player = player_2
                else:
                    while not 1 <= player_1_take <= candies_take:
                        player_1_take = int(input(
                         f'Больше {candies_take} конфет за ход брать нельзя!'
                         f'\nВведите сколько конфет берет Игрок {player_1}: '))
                    if 1 <= player_1_take <= candies_take:
                        candies_count -= player_1_take
                        print(f'Осталось {candies_count} конфет.')
                        current_player = player_2
                if candies_count >= candies_take:
                    player_2_take = random.randint(1, candies_take)
                    print(f'\nКомпьютер берет {player_2_take} конфет.')
                    candies_count -= player_2_take
                    print(f'Осталось {candies_count} конфет.')
                    current_player = player_1
                if 0 <= candies_count <= candies_take:
                    break
            print(f'\nПобедил Игрок {current_player}!\nПоздравляем!!!')

        elif current_player == player_2:
            while True:
                if candies_count >= candies_take:
                    player_2_take = random.randint(1, candies_take)
                    print(f'\nКомпьютер берет {player_2_take} конфет.')
                    candies_count -= player_2_take
                    print(f'Осталось {candies_count} конфет.')
                    current_player = player_1
                if 0 <= candies_count <= candies_take:
                    break
                player_1_take = int(input(
                    f'\nВведите сколько конфет берет Игрок {player_1}: '))
                if 1 <= player_1_take <= 28:
                    candies_count -= player_1_take
                    print(f'Осталось {candies_count} конфет.')
                    current_player = player_2
                else:
                    while not 1 <= player_1_take <= candies_take:
                        player_1_take = int(input(
                            f'\nБольше {candies_take} конфет за ход брать '
                            f'нельзя!\nВведите сколько конфет берет Игрок '
                            f'{player_1}: '))
                    if 1 <= player_1_take <= candies_take:
                        candies_count -= player_1_take
                        print(f'Осталось {candies_count} конфет.')
                        current_player = player_2
                if 0 <= candies_count <= candies_take:
                    break
            print(f'Победил Игрок {current_player}!')

    elif difficulty_level == 2:
        if current_player == player_1:
            while True:
                player_1_take = int(input(
                    f'\nВведите сколько конфет берет Игрок {player_1}: '))
                if 1 <= player_1_take <= 28:
                    candies_count -= player_1_take
                    print(f'Осталось {candies_count} конфет.')
                    current_player = player_2
                else:
                    while not 1 <= player_1_take <= candies_take:
                        player_1_take = int(input(
                            f'\nБольше {candies_take} конфет за ход брать '
                            f'нельзя!\nВведите сколько конфет берет Игрок '
                            f'{player_1}: '))
                    if 1 <= player_1_take <= candies_take:
                        candies_count -= player_1_take
                        print(f'Осталось {candies_count} конфет.')
                        current_player = player_2
                if candies_count >= candies_take:
                    player_2_take = candies_count % (candies_take + 1)
                    if player_2_take == 0:
                        player_2_take = random.randint(1, candies_take)
                    print(f'\nКомпьютер берет {player_2_take} конфет.')
                    candies_count -= player_2_take
                    print(f'Осталось {candies_count} конфет.')
                    current_player = player_1
                if 0 <= candies_count <= candies_take:
                    break
            print(f'Победил Игрок {current_player}!\nПоздравляем!!!')

        elif current_player == player_2:
            while True:
                if candies_count >= candies_take:
                    player_2_take = candies_count % (candies_take + 1)
                    if player_2_take == 0:
                        player_2_take = random.randint(1, candies_take)
                    print(f'\nКомпьютер берет {player_2_take} конфет.')
                    candies_count -= player_2_take
                    print(f'Осталось {candies_count} конфет.')
                    current_player = player_1
                if 0 <= candies_count <= candies_take:
                    break
                player_1_take = int(
                    input(f'\nВведите сколько конфет берет Игрок '
                          f'{player_1}: '))
                if 1 <= player_1_take <= 28:
                    candies_count -= player_1_take
                    print(f'Осталось {candies_count} конфет.')
                    current_player = player_2
                else:
                    while not 1 <= player_1_take <= candies_take:
                        player_1_take = int(input(
                            f'\nБольше {candies_take} конфет за ход брать '
                            f'нельзя!\nВведите сколько конфет берет Игрок '
                            f'{player_1}: '))
                    if 1 <= player_1_take <= candies_take:
                        candies_count -= player_1_take
                        print(f'Осталось {candies_count} конфет.')
                        current_player = player_2
                if 0 <= candies_count <= candies_take:
                    break
            print(f'Победил Игрок {current_player}!\nПоздравляем!!!')
    else:
        print('Некорректный ввод. Попробуйте войти в игру еще раз!')
else:
    print('Некорректный ввод. Попробуйте войти в игру еще раз!')
