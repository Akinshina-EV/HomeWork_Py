# 5. Реализуйте алгоритм перемешивания списка.

import random

element_of_list = input('Введите элементы списка через пробел: ')
input_list = element_of_list.split(' ')
print(f'Исходный список: {input_list}')
random.shuffle(input_list)
print(f'Исходный список, элементы в котором перемешаны в случайном порядке: {input_list}')
