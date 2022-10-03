# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
#     Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


from file_def import get_list_int, arithmetic_rounding

input_list = get_list_int()
count = arithmetic_rounding(len(input_list) / 2)
product_list = []
for i in range(count):
    product_list.append(input_list[i] * input_list[len(input_list) - i - 1])
print(f'Список из произведений пар чисел исходного списка\n'
      f'(парой считается первый и последний элемент, второй и предпоследний '
      f'и т.д.):\n{product_list}')
