# Задайте натуральное число N. Напишите программу, которая составит список
# простых множителей числа N.


number = int(input('Введите натуральное число: N = '))
n = number
factors = []
for i in range(2, int(number ** 0.5) + 2):
    while number % i == 0:
        factors.append(i)
        number //= i
if number != 1:
    factors.append(number)
print(f'Список простых множителей числа {n}: {factors}')
