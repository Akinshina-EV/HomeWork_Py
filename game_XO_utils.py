import tkinter as tk


player = 'X'
board_game = []
game = True


def create_board_game(window):
    for row in range(3):
        rows = []
        for col in range(3):
            button = tk.Button(window, text='  ', padx=50, pady=50,
                               command=lambda x=row, y=col: click(x, y))
            button.grid(row=row, column=col)
            rows.append(button)
        board_game.append(rows)
    new_button = tk.Button(window, text='New game', command=new_game)
    new_button.grid(row=3, column=0, columnspan=3)


def new_game():
    global game
    for row in range(3):
        for col in range(3):
            board_game[row][col]['text'] = '  '
    game = True


def click(row, col):
    global player, game
    if game and board_game[row][col]['text'] == '  ':
        board_game[row][col]['text'] = player
        check_win(board_game, player)
        player = 'O' if player == 'X' else 'X'


def check_win(board, smb):
    global game
    board_trans = [[board[j][i]['text'] for j in range(len(board))] for i in
                   range(len(board[0]))]
    diagonal_1 = all([board[i][i]['text'] == smb for i in range(3)])
    diagonal_2 = all([board[0][2]['text'] == smb, board[1][1]['text'] == smb,
                      board[2][0]['text'] == smb])
    if any([check_row(board, smb), diagonal_1, diagonal_2,
            check_row(board_trans, smb)]):
        game = False


def check_row(board, smb):
    global game
    for row in board:
        if all([i == smb for i in row]):
            game = False
