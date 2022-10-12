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

CANDIES_TAKE = 28


def options(choice):
    while True:
        if choice:
            category = input(
                f'Выберете соперника: "1" - Человек, "2" - Компьютер: \n')
        else:
            category = input('Выберете уровень сложности игры: "1" - легкий, '
                             '"2" - сложный: \n')
        if category.isdigit():
            category = int(category)
            if category in [1, 2]:
                category = True if category == 1 else False
                return category
        print('Некорректный ввод. Попробуйте еще раз!')


def greetings(count, gamer):
    if gamer:
        player1 = input('Введите имя Игрока 1: ')
        player2 = input('Введите имя Игрока 2: ')
    else:
        player1 = input('Введите имя Игрока: ')
        player2 = 'Компьютер'
    print(f'\nПеред вами {count} конфета. За один ход можно забрать не '
          f'более чем {CANDIES_TAKE} конфеты.')
    cur_player = random.choice([player1, player2])
    print(
        f'\nПроведем жеребьевку!\nПервый ход делает Игрок {cur_player}\n')
    return player1, player2, cur_player


def human_turn(player, count):
    while True:
        candies_taken = int(input(f'Введите сколько конфет берет Игрок '
                                  f'{player}: '))
        if 1 <= candies_taken <= CANDIES_TAKE:
            count -= candies_taken
            print(f'Осталось {count} конфет.\n')
            return count
        else:
            print(f'\nБольше {CANDIES_TAKE} конфет за ход брать нельзя!\n')


def computer_bot_turn(count, difficult):
    if difficult:
        candies_taken = random.randint(1, CANDIES_TAKE)
    else:
        candies_taken = count % (CANDIES_TAKE + 1)
        if candies_taken == 0:
            candies_taken = random.randint(1, CANDIES_TAKE)

    print(f'Компьютер берет {candies_taken} конфет.')
    count -= candies_taken
    print(f'Осталось {count} конфет.\n')
    return count


candies_count = 2021
print(f'Добро пожаловать в игру "{candies_count} конфета!"')
selection = True
opponent = options(selection)
player_1, player_2, current_player = greetings(candies_count, opponent)

if opponent:
    while True:
        candies_count = human_turn(current_player, candies_count)
        current_player = player_2 if current_player == player_1 else \
            player_1
        if 0 <= candies_count <= CANDIES_TAKE:
            break
    print(f'\nПобедил Игрок {current_player}!\nПоздравляем!!!')

selection = False
level = options(selection)

if not opponent:
    while True:
        if current_player == player_1:
            candies_count = human_turn(current_player, candies_count)
            current_player = player_2 if current_player == player_1 else \
                player_1
        else:
            candies_count = computer_bot_turn(candies_count, level)
            current_player = player_2 if current_player == player_1 else \
                player_1
        if 0 <= candies_count <= CANDIES_TAKE:
            break
    print(f'Победил Игрок {current_player}!\nПоздравляем!!!')
