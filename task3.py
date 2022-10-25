# 3. Задайте список из n чисел последовательности (1 + 1 / n) ** n и
# выведите на экран их сумму.
#
# Пример:
#
# 1 -> 2.0
# 2 -> 4.25
# 3 -> 6.62037037037037

n = input('Введите натуральное число n: ')
progression = []
sum_progression = 0
if n.isdigit():
    for i in range(1, int(n) + 1):
        progression.append((1 + 1 / i) ** i)
        sum_progression += progression[i - 1]
    print(sum_progression)
else:
    print('Недопустимый ввод. Можно вводить только натуральное число.')