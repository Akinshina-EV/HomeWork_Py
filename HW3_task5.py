# Задайте число. Составьте список чисел Фибоначчи, в том числе для
# отрицательных индексов.
#
#     Пример:
#
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


import math

limit_fib = int(input('Введите число: '))
pos_part_fib = [0, 1]
neg_part_fib = []
for i in range(2, limit_fib + 1):
    pos_part_fib.append(pos_part_fib[i - 1] + pos_part_fib[i - 2])
for j in range(-limit_fib, 0):
    neg_part_fib.append(int(math.pow((-1), (j + 1)) * pos_part_fib[-j]))
fib_list = neg_part_fib + pos_part_fib
if limit_fib == 0:
    print(0)
else:
    print(f'Список чисел Фибоначчи для последовательности ({-limit_fib}, '
          f'{limit_fib}):\n{fib_list}')
