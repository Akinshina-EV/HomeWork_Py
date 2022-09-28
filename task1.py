# Напишите программу, которая принимает на вход вещественное число и
# показывает сумму его цифр. Пример:
#
# 6782 -> 23
# 0,56 -> 11
#

def sum_diginal_number(number):
    sum = 0
    while (number != 0):
        sum = sum + number % 10
        number = number // 10
    return sum


number = input('Введите число: ' )
replacement = {'-': None, '.': None}
result_number = number.maketrans(replacement)
number = number.translate(result_number)
if number.isdigit():
    sum = sum_diginal_number(int(number))
    print(f'Сумма цифр числа равна: {sum}')
else:
    print('Недопустимый ввод. Можно вводить только числа')
