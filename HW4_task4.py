# Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
# степени k.
#
#     Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random

import numpy as np
from sympy import symbols


def get_pol(power, limit_value_coefficient):
    coefficient = [random.randint(0, limit_value_coefficient) for _ in
                   range(power + 1)]
    x = symbols('x')
    list_of_variable = list([x ** i for i in range(power + 1)].__reversed__())
    pol = sum(map(np.prod, (zip(coefficient, list_of_variable))))
    return str(pol).replace('**', '^') + ' = 0'


if __name__ == '__main__':
    polynomial = get_pol(2, 100)
    with open('task4.txt', 'w', encoding='utf-8') as data:
        data.write(polynomial)
