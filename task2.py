# 2. Напишите программу, которая принимает на вход число N и выдает набор
# произведений чисел от 1 до N.
#
# Пример:
#
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = input('Введите натуральное число N: ')
number_of_progression = 1
product_of_numbers = []
if n.isdigit():
    for i in range(1, int(n) + 1):
        number_of_progression *= i
        product_of_numbers.append(number_of_progression)
    print(product_of_numbers)
else:
    print('Недопустимый ввод. Можно вводить только натуральное число.')
