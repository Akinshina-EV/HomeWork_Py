# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.
#
#     Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math
from file_def import get_list_float

input_list = get_list_float()
result_list = []
for i in input_list:
    result_list.append(abs(i - int(i)))
diff_max_min_fractional_part = round(max(result_list), 10) - round(
    min(result_list), 10)
print(
    f'Разница между максимальным ({round(max(result_list), 10)}) и минимальным '
    f'({round(min(result_list), 10)}) значением дробной части элементов: '
    f'{round(diff_max_min_fractional_part, 10)}')
