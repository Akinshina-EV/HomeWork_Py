# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import random


N = input('Введите натуральное число N: ' )
list_of_N_elements = []
position = [45, 20, 4, 92, 10, 5, 79, 39, 63, 67,
             2, 52, 83, 59, 18, 41, 11, 22, 90, 3]
position.sort()
print(position)
if N.isdigit():
    N = int(N)
    prodact = 1
    for i in range(N):
        list_of_N_elements.append(random.randint(N * (-1), N))
    print(list_of_N_elements)
    for j in position:
        if j < len(list_of_N_elements):
            index = j
            prodact = prodact * list_of_N_elements[index]
            print(prodact)
        else:
            break
    # print(prodact)
else:
    print('Недопустимый ввод. Можно вводить только натуральное число.')
