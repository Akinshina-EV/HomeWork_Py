# Создайте программу для игры в ""Крестики-нолики"".


def show(array: [list]):
    print('|', end=' ')
    print(*range(len(array)), sep=' | ', end=' | \n')
    print('—————————————')
    for i, row in enumerate(array):
        print('|', end=' ')
        print(*row, sep=' | ', end=f' | {i}\n')
        print('—————————————')


show([[' ']*3]*3)
