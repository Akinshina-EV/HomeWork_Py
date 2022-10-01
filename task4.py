# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

n = input('Введите натуральное число N: ')
list_of_n_elements = []
data = open('file.txt', 'r')
position = [line.strip() for line in data]
data.close()
result_position = [int(item) for item in position]
result_position.sort()
index = []
if n.isdigit():
    n = int(n)
    prodact = 1
    for i in range(n):
        list_of_n_elements.append(random.randint(n * (-1), n))
    print(f'Исходный список: {list_of_n_elements}')
    for j in result_position:
        if j < len(list_of_n_elements):
            index.append(j)
            prodact *= list_of_n_elements[j]
        else:
            continue
    print(f'Произведение элементов на позициях {index}: {prodact}')
else:
    print('Недопустимый ввод. Можно вводить только натуральное число.')
