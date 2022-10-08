# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


import sympy

from HW4_task4 import get_pol


def read_file(path):
    with open(path, 'r') as f:
        pol = f.read().replace(' = 0', '')
    return pol


pol1_path = 'task5_1.txt'
pol2_path = 'task5_2.txt'

polynomial1 = get_pol(3, 100)
with open(pol1_path, 'w') as data:
    data.write(polynomial1)

polynomial2 = get_pol(2, 10)
with open(pol2_path, 'w') as data:
    data.write(polynomial2)

pol1 = sympy.poly(read_file(pol1_path))
pol2 = sympy.poly(read_file(pol2_path))
pol_sum = pol1.add(pol2)

with open('task5_3.txt', 'w', encoding='utf-8') as data:
    data.write(f'{str(pol_sum.as_expr()).replace("**", "^")} = 0')
