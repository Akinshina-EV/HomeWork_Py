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
if '.' in number:
    number_list = number.split('.')
    integer_part = int(number_list[0])
    fractional_part = int(number_list[1])
    sum = sum_diginal_number(integer_part) + sum_diginal_number(fractional_part)
else:
    number = int(number)
    sum = sum_diginal_number(number)
print(f'Сумма цифр числа равна: {sum}')
