# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.


import random

count = int(input(f'Задайте длину списка числовой последовательности: '))
number_list = [random.randint(1, count) for _ in range(count)]
result_list = []
print(f'Исходный список: {number_list}')

for i in range(count):
    mark = True
    for j in range(count):
        if number_list[i] == number_list[j] and i != j:
            mark = False
            break
    if mark:
        result_list.append(number_list[i])
print(
    f'Список неповторяющихся элементов исходной последовательности: '
    f'{result_list}')
