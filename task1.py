# Напишите программу, которая принимает на вход вещественное число и
# показывает сумму его цифр. Пример:
#
# 6782 -> 23
# 0,56 -> 11
#


number = input('Введите число: ')
number = number.replace('-', '').replace('.', '').replace(',', '')

if number.isdigit():
    number = int(number)
    sum_digits = 0
    while number != 0:
        sum_digits += number % 10
        number //= 10
    print(f'Сумма цифр числа равна: {sum_digits}')
else:
    print('Недопустимый ввод. Можно вводить только числа.')
