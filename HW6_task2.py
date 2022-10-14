# Дана последовательность чисел. Получить список уникальных элементов заданной
# последовательности, список повторяемых и убрать дубликаты из заданной
# последовательности.
#
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]


import itertools


number_input = input('Введите последовательность натуральных чисел: ')
number_lst = [int(num) for num in number_input.split()]
number_without_repeat = list(set(number_lst))
number_lst_sort = sorted(number_lst)
number_lst_unique = []
number_lst_repeat = []
for num, num_lst in itertools.groupby(number_lst_sort):
    if len(list(num_lst)) == 1:
        number_lst_unique.append(num)
    else:
        number_lst_repeat.append(num)
print(f'Исходная последовательность чисел: {number_lst}')
print(f'Список неповторяющихся чисел исходной последовательности: '
      f'{number_lst_unique}')
print(f'Список повторяющихся чисел исходной последовательности: '
      f'{number_lst_repeat}')
print(f'Список без дубликатов повторяющихся чисел исходной последовательности:'
      f' {number_without_repeat}')