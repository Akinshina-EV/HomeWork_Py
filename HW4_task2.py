# Задайте натуральное число N. Напишите программу, которая составит список
# простых множителей числа N.


number = int(input('Введите натуральное число: N = '))
N = number
factors = []
for i in range(2, int(number ** 0.5) + 2):
    while number % i == 0:
        factors.append(i)
        number /= i
print(f'Список простых множителей числа {N}: {factors}')
