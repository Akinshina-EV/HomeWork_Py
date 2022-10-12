# Создайте программу для игры в ""Крестики-нолики"".


import random


def show(board: [list]):
    print('\t|', end=' ')
    print(*range(len(board)), sep=' | ', end=' | \n')
    print('——— —————————————')
    for i, row in enumerate(board):
        print(i, end=' ')
        print('  |', end=' ')
        print(*row, sep=' | ', end=' | \n')
        print('——— —————————————')


def get_cord(array, symbl):
    while True:
        coord = input(f'Введите координаты "{symbl}" через пробел: ')
        if len(coord) == 2:
            if coord.isdigit():
                if all(int(coordinate) in range(0, 3) for coordinate in coord):
                    coord_x = int(coord[0])
                    coord_y = int(coord[1])
                    if array[coord_x][coord_y] == ' ':
                        array[coord_x][coord_y] = symbl
                        return array
        print('Некорректный ввод.')


def check_win(arr_board, mark):
    arr_trans = [[arr_board[j][i] for j in range(len(arr_board))] for i in
                 range(len(arr_board[0]))]
    diagonal_1 = all([arr_board[i][i] == mark for i in range(3)])
    diagonal_2 = all([arr_board[0][2] == mark, arr_board[1][1] == mark,
                      arr_board[2][0] == mark])
    if any([check_row(arr_board, mark), diagonal_1, diagonal_2,
            check_row(arr_trans, mark)]):
        return True
    return False


def check_row(array_r, flag):
    for row in array_r:
        if all([i == flag for i in row]):
            return True
    return False


print(f'Добро пожаловать в игру "Крестики - Нолики!"')
player1 = {'symbol': '0'}
player2 = {'symbol': '0'}
player1['name'] = input('Введите имя Игрока 1: ')
player2['name'] = input('Введите имя Игрока 2: ')
cur_player = random.choice([player1, player2])
cur_player['symbol'] = 'X'
print(f'\nПроведем жеребьевку!\nПервый ход делает Игрок {cur_player["name"]}, '
      f'он ходит: {cur_player["symbol"]}.\n')
print(f'\nПеред вами игровое поле с указанием координат. Чтобы сделать ход, '
      f'введите координаты клетки в формате "XY":')
board_game = [[' '] * 3 for _ in range(3)]
show(board_game)

while True:
    board_game = get_cord(board_game, cur_player['symbol'])
    show(board_game)
    win = check_win(board_game, cur_player['symbol'])
    if win:
        print(f'Победил игрок {cur_player["name"]}!\nПоздравляем!!!')
        break
    cur_player = player2 if cur_player == player1 else player1
