import tkinter as tk

from game_XO_utils import create_board_game, new_game


window = tk.Tk()
window.title('"Крестики - Нолики"')

if __name__ == '__main__':
    create_board_game(window)
    new_game()
    window.mainloop()
