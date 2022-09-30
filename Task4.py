# Напишите программу, которая по заданному номеру четверти, показывает диапазон
# возможных координат точек в этой четверти (x и y).

print('Введите номер четверти координатной плоскости:')
number_quarter = int(input())
if number_quarter == 1:
    x = 'x > 0'
    y = 'y > 0'
elif number_quarter == 2:
    x = 'x < 0'
    y = 'y > 0'
elif number_quarter == 3:
    x = 'x < 0'
    y = 'y < 0'
elif number_quarter == 4:
    x = 'x > 0'
    y = 'y < 0'
else:
    print('Такой четверти не существует')
    x = False
    y = False
print(f'Диапазон возможных координат точек в этой четверти: {x}, {y}')
